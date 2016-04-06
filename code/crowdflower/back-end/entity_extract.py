import os
import sys
import commands
import json
import urllib
import pdb

import requests
# Given stdin, extract the entities
# Output: term offset entity_num entity1 entity2 ...


head = {'Accept': 'application/json'}
payload = {'text': "", 'confidence': '0.5', 'spotter': 'Default', \
        'disambiguator': 'Default', 'policy': 'whitelis', 'support': 0, 'types':''}
api = 'http://spotlight.sztaki.hu:2222/rest/candidates'

def query(text):
    payload['text'] = text
    r = requests.get(api, params=payload, headers=head)
    return r.json()

def extract_type(text, configs):
    A = query(text)
    #print A

    # parse the json file
    if 'annotation' not in A or 'surfaceForm' not in A['annotation']:
        return None

    sur_form = A['annotation']['surfaceForm']

    if type(sur_form) is dict:
        sur_form = [sur_form]

    term_num = len(sur_form)
    for i in range(term_num):
        term = sur_form[i]['@name']
        offset = sur_form[i]['@offset']
        entities = sur_form[i]['resource']

        if type(entities) is dict:
            entities = [entities]

        for j in range(len(entities)):
            entity = entities[j]
            if '@types' in entity:
                support = int(entity['@support'])
                for t in entity['@types'].split(','):
                    t = t.strip()
                    if t in configs and support > configs[t]:
                        return term, entity

def entity_extract(text):
    #text = text.lower()
    configs = {'Person':100,
            'Work':200,
            'Place':500,
            'Organization':1000,
            'Event': 1000,
            'Artwork':50,
            'Athlete':4,
            'Book':100,
            'CollegeCoach':4,
            'Country':1000,
            'Language':1000
            }
    cfgs = {}
    for c, thre in configs.items():
        cfgs['DBpedia:' + c] = thre

    #print cfgs
    return extract_type(text, cfgs)

def main():
    print entity_extract('Mad max looks out of a car window')
    print entity_extract('This Asian woman is singing a song.')
    print entity_extract('in a scene from Lord Of The Rings, someone is hanging from a ledge')
    print entity_extract('A young Chinese man is singing the gesturing with his hands')
    print entity_extract('Spock and Kirk together with phase rs out, Spock looks away')
    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
