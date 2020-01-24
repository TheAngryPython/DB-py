import json

class parser:
	def __init__(self, file, encoding = 'utf-8', debug = False):
		self.file = open(file, 'r', encoding = encoding).read().replace('\n','')
		if len(self.file) == 0:
			self.file = open(file, 'w+', encoding='utf-8').write('{}')
		self.js = json.loads(self.file)
		self.path = file
		self.encoding = encoding
		self.debug = debug

	def save(self):
		file = self.path
		if self.debug == True:
			open(file, 'w', encoding='utf-8').write(json.dumps(self.js, sort_keys=True, indent=4))
		elif self.debug == False:
			open(file, 'w', encoding='utf-8').write(json.dumps(self.js))

	def add_section(self, name):
		if name in self.js:
			raise SystemExit(1)
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
		return js[section]

	def js(self):
		return self.js
