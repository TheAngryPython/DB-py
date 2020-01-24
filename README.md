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

db.js()
# returns full json

db.save()
# save db to file

```
