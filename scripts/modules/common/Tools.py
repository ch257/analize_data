# -*- coding: utf-8 -*

import time
import datetime
from datetime import datetime as dt, date, time as tm

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
			if rec.get(col) != None:
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
				
		elif value_type == 'yyyymmdd':
			return dt.strptime(value, '%Y%m%d') #.date()
			
		elif value_type == 'hhmmss':
			return dt.strptime(value, '%H%M%S') #.time()
			
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
		
		elif value_type == 'escape':
			return  self.escape_sequence(value)
			
		else:
			self.errors.raise_error('Unknown type ' + value_type)
			return value
	
	def type2str(self, value, value_format):
		if self.errors.error_occured:
			return None
		
		if value == None:
			return ''
		
		if value_format == '%Y%m%d':
			return dt.strftime(value, '%Y%m%d')
			
		elif value_format == '%H%M%S':
			return dt.strftime(value, '%H%M%S')
			
		else:
			return value_format.format(value)
	
	def shape_column_types(self, columns, file_column_types):
		if self.errors.error_occured:
			return None
			
		column_types = {}
		for col in columns:
			if file_column_types.get(col) != None:
				column_types[col] = file_column_types[col]
			else:
				# self.errors.raise_error('Unknown column ' + col + ' for type detecting')
				# break
				column_types[col] = 'num'
				
		return column_types
		
	def shape_column_formats(self, columns, all_column_formats):
		if self.errors.error_occured:
			return None
			
		column_formats = {}
		for col in columns:
			if all_column_formats.get(col) != None:
				column_formats[col] = all_column_formats[col]
			else:
				# self.errors.raise_error('Unknown column ' + col + ' for format detecting')
				# break
				column_formats[col] = '{:.2f}'
		
		return column_formats
	
	def type_rec(self, rec, column_types):
		if self.errors.error_occured:
			return None
		
		for col in rec:
			rec[col] = self.str2type(rec[col], column_types[col])
			
	def str_rec(self, rec, column_formats):
		if self.errors.error_occured:
			return None
		
		for col in rec:
			rec[col] = self.type2str(rec[col], column_formats[col])
	
	def add_rec_to_table(self, rec, table):
		if self.errors.error_occured:
			return None
		
		for col in table:
			if rec.get(col) != None:
				table[col].append(rec[col])
			else:
				table[col].append(None)
	
	def get_rec_from_table(self, rec_cnt, table):
		if self.errors.error_occured:
			return None
		
		rec = {}
		for col in table:
			rec[col] = table[col][rec_cnt]
		
		return rec
		
	def add_columns(self, adv_columns, table, columns):
		if self.errors.error_occured:
			return None
		
		for adv_col in adv_columns:
			columns.append(adv_col)
			table[adv_col] = []
			length = len(table[columns[0]])
			for i in range(length):
				table[adv_col].append(None)
		
	def update_cells(self, cell_columns, cell_values, rec_cnt, table):
		if self.errors.error_occured:
			return None
		
		length = min(len(cell_columns), len(cell_values))
		for cnt in range(length):
			if table.get(cell_columns[cnt]) != None:
				table[cell_columns[cnt]][rec_cnt] = cell_values[cnt]
				
	def escape_sequence(self, seq):
			
		if seq == "'\\t'":
			seq = seq.replace("'\\t'", '\t')
		elif seq == "','":
			seq = seq.replace("','", ',')
		elif seq == "'.'":
			seq = seq.replace("','", ',')
		elif seq == "';'": 
			seq = seq.replace("';'", ';')
		elif seq == "''":
			seq = seq.replace("''", '')
		else:
			self.errors.raise_error('Unknown escape sequence ' + seq)
		return seq
		
		
