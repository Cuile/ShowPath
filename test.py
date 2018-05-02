#!/usr/bin/python
# -*- coding: utf-8 -*-


import sequence2hash

parameters = {
    'queryKey': '',
    'constraints': {
        'ids': [],
        'phids': [],
        'name': '运营平台',
        'members': [],
        'watchers': [],
        'status': '',
        'isMilestone': True,
        'icons': [],
        'colors': ['blue', '', 'red', ''],
        'parents': [],
        'ancestors': [],
    },
    'attachments': {
        'subscribers': None
    },
    'order': 'newest',
    'before': '',
    'after': '',
    'limit': {}
}

for x in sequence2hash.flatten(parameters):
    print(x)
