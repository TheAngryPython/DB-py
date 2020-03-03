import json, sys, codecs, os

class parser:
	def __init__(self, file, encoding = 'utf-8', debug = False, create = True, mode = 'r'):
		if os.path.exists(file) and create:
			self.file = codecs.open(file, mode, encoding = encoding).read().replace('\n','')
		else:
			self.file = codecs.open(file, 'w+', encoding = encoding).write('{}')
		self.js = json.loads(self.file)
		self.path = file
		self.encoding = encoding
		self.debug = debug

	def __setitem__(self, key, value):
		self.js[key] = value
		return self.js[key]

	def __getitem__(self, key):
		return self.js[key]

	def save(self):
		file = self.path
		if self.debug == True:
			codecs.open(file, 'w', encoding = self.encoding).write(json.dumps(self.js, sort_keys=True, indent=4))
		elif self.debug == False:
			codecs.open(file, 'w', encoding = self.encoding).write(json.dumps(self.js))
		return file

	def add_section(self, name, default = None):
		if name in self.js:
			raise SystemExit(1)
		else:
			if default != None:
				schema = default
				self.js[name] = {}
				i = self.js[name]
				self.js[name] = i.setdefault('data', schema)['data']
			else:
				self.js[name] = {}
			return self.js[name]

	def get(self, section, name):
		if name in self.js[section]:
			return self.js[section][name]
		else:
			raise SystemExit(1)

	def set(self, section, name, value):
		self.js[section][name] = value
		return self.js[section][name]

	def get_section(self, section):
		return self.js[section]

	def update(self, mode = 'r'):
		self.save()
		self.file = codecs.open(self.path, mode, encoding = self.encoding).read().replace('\n','')
		return self.js

	def js(self):
		return self.js
