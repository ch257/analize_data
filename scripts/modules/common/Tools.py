# -*- coding: utf-8 -*

class Tools:
	def __init__(self, errors):
		self.errors = errors
	
	def explode(self, line, sep=','):
		if self.errors.error_occured:
			return None
		
		str_array = line.split(sep)
		
		return str_array
	
	def implode(self, str_array, sep=','):
		if self.errors.error_occured:
			return None
		
		line = sep.join(str_array)
		
		return line
		
	def line2rec(self, line, cols, sep=','):
		if self.errors.error_occured:
			return None
		
		rec = {}
		str_array = self.explode(line, sep)
		length = min(len(str_array), len(cols))
		for cnt in range(length):
			rec[cols[cnt]] = str_array[cnt]

		return rec
		
	def rec2line(self, rec, cols, sep=','):
		if self.errors.error_occured:
			return None
		
		str_array = []
		for col in cols:
			if rec.get(col):
				str_array.append(rec[col])
		
		line = self.implode(str_array, sep)
		
		return line
		
	def str2type(self, value, value_type):
		if self.errors.error_occured:
			return None
		
		if value_type == 'str':
			return value
		
		elif value_type == 'int':
			return int(value)
		
		elif value_type == 'num' or value_type == 'float':
			return float(value)
		
		elif value_type == 'bool':
			if value == '1':
				return True
			else:
				return False
		
		elif value_type == 'str_array':
			return self.explode(value)
		
		elif value_type == 'int_array':
			int_array = []
			str_array = self.explode(value)
			for s in str_array:
				int_array.append(int(s))
			return int_array
		
		elif value_type == 'num_array' or value_type == 'float_array':
			float_array = []
			str_array = self.explode(value)
			for s in str_array:
				float_array.append(float(s))
			return float_array
		
		elif value_type == 'bool_array':
			bool_array = []
			str_array = self.explode(value)
			for s in str_array:
				if value == '1':
					bool_array.append(True)
				else:
					bool_array.append(False)
			return bool_array
		
		else:
			self.errors.raise_error('Unknown type ' + value_type)
			return value