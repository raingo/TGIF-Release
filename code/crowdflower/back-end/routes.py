#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

from flask import Flask, request, render_template
from flask.ext.jsonpify import jsonify
app = Flask(__name__)
import random
import os.path as osp

import sys
import language_check
this_dir = osp.dirname(__file__)
language_check.set_directory(osp.join(this_dir, '3rdparty', 'LanguageTool-3.0'))

print >> sys.stderr, language_check.get_directory()
print >> sys.stderr, 'if it is not 3.0, please consider upgrade'


from nltk import word_tokenize
import eval

from collections import defaultdict


@app.before_first_request
def setup_logging():
    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        from logging import Formatter
        file_handler = RotatingFileHandler(filename = 'logs/flask.log', maxBytes=100000000, backupCount=10)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'
                ))
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)

def load_test_data():
    sents = {}
    with open('./test-data.sorted') as reader:
        for line in reader:
            fields = line.strip().split('\t')
            url = fields[0].replace('http:', 'https:')
            sents[url] = fields[2:]
    return sents

test_sents = load_test_data()

class MyTokenizer():
    def tokenize(self, coco):
        res = {}
        for k, v in coco.items():
            res_v = []
            for line in v:
                line = line['caption']
                tags = corenlp.parse_doc(line.lower())['sentences'][0]
                res_v.append(' '.join(tags['tokens']))
            res[k] = res_v
        return res



eval_tokenizer = MyTokenizer()
def check_gold(url, target, resp):
    pos_res = '(see the reason below)'
    #pos_res = '1'
    if resp is None:
        if url in test_sents:
            score, _ = eval.eval(target, test_sents[url], scorer, eval_tokenizer)
            app.logger.info(score)
            if score > .2:
                return pos_res
            else:
                return target

    # for the sake of non distinguisable test and normal, return randomly
    if random.random() < .5:
        return target
    else:
        return pos_res

def defense(target):
    if len(target) > 500:
        return "The sentence is too long."
    else:
        return None


def is_ascii(target):
    try:
        target.decode('ascii')
    except:
        return "English words only."
    else:
        return None



def num_words(target):
    target = filter(lambda x:not x.isdigit(), target)
    tokens = word_tokenize(target)
    if len(tokens) > 25:
        return 'The sentence is too long.'
    elif len(tokens) < 8:
        return 'The sentence is too short. (digits are not counted)'
    else:
        return None

# https://github.com/brendano/stanford_corenlp_pywrapper
# pip install
# install stanford-corenlp-full-2014-08-27 to this-dir, so that osp.join(this_dir, "stanford-corenlp-full-2014-08-27/*") are the jars
from stanford_corenlp_pywrapper import CoreNLP
def start_corenlp():
    proc = CoreNLP("pos",
            corenlp_jars=[osp.join(this_dir, "3rdparty/stanford-corenlp-full-2015-04-20/*")], comm_mode = 'SOCKET')
    return proc

tool = None
scorer = None
corenlp = None
import time
def _restart_service():
    global tool, scorer, corenlp
    # recreate the language_check tool after exception
    # should be better if we can just restart from gunicorn
    # has to be successful!!
    # eventuall, this will be terminated by gunicorn because of timeout
    while True:
        try:
            scorer = eval.init()
            tool = language_check.LanguageTool('en-US')
            tool.disabled.update([u'UPPERCASE_SENTENCE_START'])
            corenlp = start_corenlp()
            app.logger.info("service started")
        except Exception as ioe:
            time.sleep(5)
            app.logger.error(ioe)
            pass
        else:
            break

_restart_service()

def check_verb(target):
    target = target.lower()
    wh = set(['that', 'who', 'which', 'whom'])
    if False and 'ing' in target:
        # to not to train workers to use ING only
        if random.random() < .5:
            return None
    tags = corenlp.parse_doc(target)['sentences'][0]
    prev = ''
    for tag, word in zip(tags['pos'], tags['tokens']):
        if tag.startswith('VB') and tag != 'VBG' and prev not in wh:
            return None
        prev = word

    return '''Ungrammatical sentence. A grammatical sentence should have a subject, verb and object. Please refer to the instructions for acceptable sentences. Examples of Ungrammatical sentences,
    A female gymnast on the uneven bars.
    Someone coming into the house, carrying his skateboard. (Correction: Someone came into the house, carrying his skateboard.)
'''


def lm_check(target):
    matches = tool.check(target)
    matches = matches[:3]
    if len(matches) != 0:
        return '\n'.join([str(m) for m in matches])
    else:
        return None

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
def num_sents(target):
    target= target.replace(';', '.')
    sents = tokenizer.tokenize(target)
    if len(sents) > 1:
        return 'Only single sentence is allowed.'
    else:
        return None

'''
swear words are scraped by:
pip install lxml
printf '%s\n' {a..z} | xargs -L 1 -I {}  python xpath.py '//td[@valign="top"]/b/text()' http://www.noswearing.com/dictionary/'{}' | grep -v Slang
'''

def load_bl_pat():
    bl = ['clip', 'movie', 'film', 'I', 'We', 'Our', 'like it', 'like', 'camera', 'screen', 'sex', 'suicide', 'video', 'series', 'me', 'you', 'your', 'maybe', 'seems', 'seem', 'looks like', 'believe', 'seen', 'could be', 'there is', 'there are', 'there exists', 'sentence']
    import re
    with open('./swear-words') as reader:
        for line in reader:
            bl.append(line.strip())
    bl_pat = re.compile(r'\b%s\b' % '\\b|\\b'.join(set(bl)), flags=re.IGNORECASE)
    return bl_pat

bl_pat = load_bl_pat()
def blacklist_words(target):
    m = bl_pat.search(target.lower())
    if m:
        return '''Please describe only the visible content using an appropriate, complete and concise sentence.
    Unacceptable examples:
        "I like this GIF very much."
        "This video is not good, in bad quality."
    Rules:
        Do NOT use Not Safe For Work (NSFW) words
        Do NOT Mention objects not present in the GIF, e.g., yourself.
        Do NOT make subjective/imaginative judgments about the GIF.
        Do NOT use 'there is' phrases.
        '''
    else:
        return None

def check_history(target, url):
    app.logger.info(url)

    if url == 'test' or url in test_sents:
        # Dont check history for testing
        return None

    target = target.lower()

    if target in history:
        return 'We found a very similar sentence in our records. Please rephrase the sentence.'
    else:
        history.add(target)
        return None

from entity_extract import entity_extract
def check_entity(target):
    entity = entity_extract(target)
    if 'Asian' in target:
        entity = ['Asian']
    if entity:
        return 'Names such as "%s" should not be mentioned' % entity[0]
    else:
        return None

import traceback
@app.route('/')
def index():
    query = request.args.get('q', '').strip()
    url = request.args.get('url', '')
    retry = 3

    for i in range(retry):
        try:
            res = defense(query) or is_ascii(query) or num_words(query) or num_sents(query) or check_history(query, url) or blacklist_words(query) or check_verb(query) or check_entity(query) or lm_check(query)
            app.logger.info(res)
            gold = check_gold(url, query, res)
            break
        except Exception as ioe:
            tb = traceback.format_exc()
            app.logger.error(tb)
            res = "Rare internal failure happened. Please try again by refreshing the page. %s" % (ioe)
            gold = '0'
            _restart_service()

            pass

    return jsonify(status = res, gold = gold)

print >> sys.stderr, 'test here: http://codepen.io/raingo/pen/YXBwgY'

history = set()
if __name__ == '__main__':
    # deploy mode in ./deploy.sh
    app.run(host='0.0.0.0', port = 8083, debug = True)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
