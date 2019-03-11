# -*- coding: utf-8 -*


class Files:
	def __init__(self, errors):
		self._errors = errors
		self.handler = None
	
	def open_file(self, path, mode='r', encoding='utf-8'):
		if self._errors.error_occured:
			return None
		
		try:
			self.handler = open(path, mode, encoding = encoding)
		except Exception as e:
			self._errors.raise_error('Can\'t open file ' + path)
	
	def close_file(self):
		if self.handler:
			self.handler.close()
			self.handler = None
	
	def read_line(self):
		if self._errors.error_occured:
			return None
		
		line = self.handler.readline()
		return line
	
	def write_line(self, line):
		if self._errors.error_occured:
			return None
		
		self.handler.write(line + "\n")
		