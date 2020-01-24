# JSON config parser
Json-based configuration parser, similar to configparser
[Download](https://github.com/TheAngryPython/DB-py/blob/master/db.py)

## Install
```
pip install jsondbparser
```

## Use
```python
import jsondbparser	as db
db = db.parser('file.txt', encoding = 'utf-8', debug = False)

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

db.save(file = 'file1.txt')
# save db to file

```
