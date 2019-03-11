# -*- coding: utf-8 -*

from modules.common_1_0.Errors import *
from modules.common_1_0.SettingsReader import *
from modules.common_1_0.Tools import *
from modules.common_1_0.CSVParser import *
from modules.common_1_0.TableIterator import *
#######################


class Levels:
	def __init__(self):
		self.errors = Errors()
		self.settings_reader = SettingsReader(self.errors)
		self.settings = {}
	
	def main(self, args):
		self.settings = self.settings_reader.read_settings(args)
		
		# csv_parser = CSVParser(self.errors)
		# table, columns = csv_parser.csv2table(input_file_path, input_file_format)
		
		# csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		
		print(self.settings)
		
		if self.errors.error_occured:
			self.errors.print_errors()
		else:
			print('OK\n')