# JSON config parser
Json-based configuration parser, similar to configparser

## Install
```
pip install jsondbparser
```

## Use
```python
from jsondbparser import core as parser

db = parser.parser('file.txt', encoding = 'utf-8', debug = False)

db.add_section('section')
# adds section

db.set('section', 'name', 'value')
# changes or adds value

db.get('section', 'name')
# returns 'value'

db.get_section('section')
# returns json section

db['section']['name']
# returns 'value'

db['section']['name'] = 'test'
# returns 'test'

db.save()
# save db to file, return relative path


from jsondbparser import convert

convert.from_path('file.txt', str = False)
# convert config file to json, return json

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('file.txt')

convert.from_config(config, str = False)
# convert config to json, return json
```
