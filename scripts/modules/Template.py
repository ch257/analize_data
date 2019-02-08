# -*- coding: utf-8 -*

from modules.common.Errors import *
from modules.common.IniParser import *

class Template:
	def __init__(self):
		self.errors = Errors()
		self.ini_encoding = 'utf-8'
		self.ini_parser = IniParser(self.errors)
		self.settings = {}
	
	def read_settings(self, args):
		if len(args) < 2:
			self.errors.raise_error('No ini file path')
		else:
			encoding = self.ini_encoding
			if len(args) > 2:
				encoding = args[2]
				
			ini_file_path = args[1]
			self.ini_parser.read_ini(args[1], encoding)
	
	def set_params(self, args):
		self.read_settings(args)
		self.settings['g2'] = {}
		self.settings['g3'] = {}
		self.settings['g2']['p1'] = self.ini_parser.get_param('g2', 'p1', 'str_array')
		self.settings['g3'] = self.ini_parser.get_param('g3')
		
		
	def main(self, args):
		self.set_params(args)
		print(self.settings)
		g1_p2 = self.ini_parser.get_param('g1', 'p2')
		print(g1_p2)
		
		
		if self.errors.error_occured:
			self.errors.print_errors()
		else:
			print('OK\n')