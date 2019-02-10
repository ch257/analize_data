# -*- coding: utf-8 -*

from modules.common.Files import *
from modules.common.Tools import *

class CSVParser:
	def __init__(self, errors):
		self.errors = errors
		
	def csv2table(self, file_path, file_format):
		if self.errors.error_occured:
			return None
		
		list_separator = file_format['list_separator']
		decimal_symbol = file_format['decimal_symbol']
		encoding = file_format['encoding']
		file_column_types = file_format['file_column_types']
		
		tools = Tools(self.errors)
		file = Files(self.errors)
		
		table = {}
		columns = []
		file.open_file(file_path, 'r', encoding)
		while not self.errors.error_occured:
			line = file.read_line()
			if line:
				line = line.strip('\n')
				columns = tools.explode(line, list_separator)
			else:
				self.errors.raise_error('File ' + file_path + ' is empty')
			break
			
		column_types = tools.shape_column_types(columns, file_column_types)
		# column_formats = tools.shape_column_formats(columns, all_column_formats)
		
		for col in columns:
			table[col] = []
		
		while not self.errors.error_occured:
			line = file.read_line()
			if line:
				line = line.strip('\n')
				if line:
					rec = tools.line2rec(line, columns, list_separator)
					tools.type_rec(rec, column_types)
					tools.add_rec_to_table(rec, table)
			else:
				break
			
		file.close_file()
		
		return table
		
	def table2csv(self, table, file_path, file_format):
		if self.errors.error_occured:
			return None
			
		list_separator = file_format['list_separator']
		decimal_symbol = file_format['decimal_symbol']
		encoding = file_format['encoding']
		file_column_types = file_format['file_column_types']
		
		tools = Tools(self.errors)
		file = Files(self.errors)
		
		
		