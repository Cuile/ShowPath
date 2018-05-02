#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='sequence2hash',
    version='1.0.1',
    keywords='tuple dict list sequence hash key/value',
    packages=['sequence2hash'],

    url='https://github.com/Cuile/sequence2hash',
    description='将 序列中的有效值 转为 哈希值，并在key字段中包含有效值的路径',
    long_description_content_type='text/markdown',
    long_description='''
    # sequence2hash - Convert sequence to hash
    This tool converts a valid value in a sequence to a hash and contains a path to a valid value in the key field
    
    ## Features
    - Convert valid values ​​in the sequence to hashes
    - Paths showing valid values ​​in the key field
    - Valid values ​​not (), [], {}, None, ''
                  
    ## Examples
    Define the sequence variable:
    ```Python
    parameters = {
        'queryKey': '',
        'constraints': {
            'ids': [],
            'phids': (),
            'name': 'Operating platform'
            'members': ('Bunoob', 1944, 'Google'),
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
    ```
    Transfer:
    ```Python
    import sequence2hash
    for x in sequence2hash.flatten(parameters):
        print(x)
    ```
    Output:
    ```Bash
    {'key': ['constraints', 'name'], 'value': 'Operating platform'}
    {'key': ['constraints', 'members', '0'], 'value': 'Bunoob'}
    {'key': ['constraints', 'members', '1'], 'value': 1944}
    {'key': ['constraints', 'members', '2'], 'value': 'Google'}
    {'key': ['constraints', 'isMilestone'], 'value': True}
    {'key': ['constraints', 'colors', '0'], 'value': 'blue'}
    {'key': ['constraints', 'colors', '2'], 'value': 'red'}
    {'key': ['order'], 'value': 'newest'}
    ```
    ''',

    author='cuile',
    author_email='i@cuile.com'
)
