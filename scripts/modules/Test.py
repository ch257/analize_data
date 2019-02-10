# -*- coding: utf-8 -*

from modules.common.Errors import *
from modules.common.IniParser import *
from modules.common.Files import *
from modules.common.Tools import *
from modules.common.CSVParser import *

#######################


class Test:
	def __init__(self):
		self.errors = Errors()
		self.ini_encoding = 'utf-8'
		self.ini_parser = IniParser(self.errors)
		# self.settings = {}
	
	def read_settings(self, args):
		if len(args) < 2:
			self.errors.raise_error('no ini file path')
		else:
			encoding = self.ini_encoding
			if len(args) > 2:
				encoding = args[2]
				
			ini_file_path = args[1]
			self.ini_parser.read_ini(args[1], encoding)
	
	def main(self, args):
		self.read_settings(args)
		
		input_file_path = self.ini_parser.get_param('input', 'file_path')
		input_file_format = {}
		input_file_format_section = self.ini_parser.get_param('input', 'file_format')
		input_file_format['list_separator'] = self.ini_parser.get_param(input_file_format_section, 'list_separator', 'escape')
		input_file_format['decimal_symbol'] = self.ini_parser.get_param(input_file_format_section, 'decimal_symbol', 'escape')
		input_file_format['encoding'] = self.ini_parser.get_param(input_file_format_section, 'encoding')
		
		input_file_column_types_section = self.ini_parser.get_param(input_file_format_section, 'file_column_types')
		input_file_column_formats_section = self.ini_parser.get_param(input_file_format_section, 'file_column_formats')
		input_file_format['file_column_types'] = self.ini_parser.get_param(input_file_column_types_section)
		input_file_format['file_column_formats'] = self.ini_parser.get_param(input_file_column_formats_section)
		
		output_file_path = self.ini_parser.get_param('output', 'file_path')
		output_file_format = {}
		output_file_format_section = self.ini_parser.get_param('output', 'file_format')
		output_file_format['list_separator'] = self.ini_parser.get_param(output_file_format_section, 'list_separator', 'escape')
		output_file_format['decimal_symbol'] = self.ini_parser.get_param(output_file_format_section, 'decimal_symbol', 'escape')
		output_file_format['encoding'] = self.ini_parser.get_param(output_file_format_section, 'encoding')
		
		output_file_column_types_section = self.ini_parser.get_param(output_file_format_section, 'file_column_types')
		output_file_column_formats_section = self.ini_parser.get_param(output_file_format_section, 'file_column_formats')
		output_file_format['file_column_types'] = self.ini_parser.get_param(output_file_column_types_section)
		output_file_format['file_column_formats'] = self.ini_parser.get_param(output_file_column_formats_section)
		
		csv_parser = CSVParser(self.errors)
		table, columns = csv_parser.csv2table(input_file_path, input_file_format)
		
		csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		# print(table['<DATE>'])
		# print(table['<TIME>'])
		
		# print('{:.2f}'.format(1534.545))
		# print('{}'.format('dfg'))
		
		
		
		if self.errors.error_occured:
			self.errors.print_errors()
		else:
			print('OK\n')