import json
try:
	import configparser
except ImportError:
	import ConfigParser as configparser

class Converter:

	def from_path(self, path, encoding = 'utf-8', str = False):
		config = configparser.ConfigParser()
		config.read(path, encoding = encoding)
		js = {}
		for a in config.sections():
			for key in config[a]:
				js[a] = key
		if str == False:
			return js
		else:
			return json.dumps(js)

	def from_config(self, config, str = False):
		js = {}
		for a in config.sections():
			for key in config[a]:
				js[a] = key
		if str == False:
			return js
		else:
			return json.dumps(js)
