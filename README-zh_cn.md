# sequence2hash - 将序列转为哈希值
=================
这个工具将 序列中的有效值 转为 哈希值，并在key字段中包含有效值的路径

## Features
-----------
- 将序列中的有效值转为哈希值
- 在key字段里展示有效值的路径
- 有效值 not () , [] , {} , None , ''

## Requirements
---------------
- 不需要任何第三方库

## Installation
---------------
```Bash
pip install sequence2hash
```

## Quick Start
--------------
```Python
parameters = {
    'queryKey': '',
    'constraints': {
        'ids': [],
        'phids': (),
        'name': '运营平台',
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
```Python
import sequence2hash
for x in sequence2hash.flatten(parameters):
    print(x)
```
```Bash
{'key': ['constraints', 'name'], 'value': '运营平台'}
{'key': ['constraints', 'members', '0'], 'value': 'Bunoob'}
{'key': ['constraints', 'members', '1'], 'value': 1944}
{'key': ['constraints', 'members', '2'], 'value': 'Google'}
{'key': ['constraints', 'isMilestone'], 'value': True}
{'key': ['constraints', 'colors', '0'], 'value': 'blue'}
{'key': ['constraints', 'colors', '2'], 'value': 'red'}
{'key': ['order'], 'value': 'newest'}
```