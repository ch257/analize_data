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
		list_separator = self.ini_parser.get_param('input', 'list_separator', 'escape')
		decimal_symbol = self.ini_parser.get_param('input', 'decimal_symbol', 'escape')
		
		input_file = Files(self.errors)
		tools = Tools(self.errors)
		
		input_file.open_file(input_file_path)
		while not self.errors.error_occured:
			line = input_file.read_line()
			if line:
				line = line.strip('\n')
				columns = tools.explode(line, list_separator)
			else:
				self.errors.raise_error('File ' + input_file_path + ' is empty')
			break
		
		while not self.errors.error_occured:
			line = input_file.read_line()
			if line:
				line = line.strip('\n')
				if line:
					rec = tools.line2rec(line, columns, list_separator)
				
				print(rec)
			else:
				break
			
		input_file.close_file()
		
		if self.errors.error_occured:
			self.errors.print_errors()
		else:
			print('OK\n')