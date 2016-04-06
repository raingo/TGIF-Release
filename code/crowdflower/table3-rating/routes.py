#!/usr/bin/env python
from flask import Flask, render_template, json, request, Response, redirect, url_for
import random
app = Flask('Rate dataset')

from flask_wtf import Form
from wtforms import RadioField
from wtforms.validators import DataRequired
import uuid
import os.path as osp

_questions = [
        ('obj', 'Objective/Subjective of the sentence', ['Objective', 'Neutral', 'Subjective']),
        ('missing', 'Compared with the sentence, is there missing information in the animated GIF?', ['Yes', 'No']),
        ('redundent', 'Compared with the sentence, is there redundent information in the animated GIF?', ['Yes', 'No']),
        ('segment', 'How the animated GIF got segmented?', ['Good', 'OK', 'Bad'])
        ]

class MyForm(Form):
    pass

def get_chs(chs):
    ret = []
    for i, ch in enumerate(chs):
        ret.append(('value-%d' % i, ch))
    return ret

for name, question, choices in _questions:
    setattr(MyForm, name, RadioField(question, validators=[DataRequired()], choices = get_chs(choices)))

def load_data(path = './randomized.tsv'):

    res = []

    with open(path) as reader:
        for line in reader:
            fields = line.strip().split('\t')
            res.append((fields[0], fields[1], fields[2]))

    return res

db = load_data()

@app.route('/')
def index():
    return redirect('/0')

@app.route('/<int:lid>', methods=['GET', 'POST'])
def submit(lid):
    form = MyForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        save_path = osp.join('data', '%d@%s' % (lid, uuid.uuid4()))
        with open(save_path, 'w') as writer:
            print >> writer, lid,
            for name, question, choices in _questions:
                print >> writer, getattr(form, name).data,
            print >> writer
        return redirect('/%d' % (lid + 1))
    return render_template('submit.html', form = form, url = db[lid][1], sent = db[lid][2], rd = random.choice(range(len(db))))

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8086, threaded=True)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
