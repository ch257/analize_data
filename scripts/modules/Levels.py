# -*- coding: utf-8 -*

from modules.common_1_0.Errors import *
from modules.common_1_0.SettingsReader import *
from modules.common_1_0.CSVParser import *
from modules.common_1_0.TableIterator import *
from modules.common_1_0.Tools import *
#######################


class Levels:
	def __init__(self):
		self._errors = Errors()
	
	def main(self, args):
		settings_reader = SettingsReader(self._errors)
		settings = settings_reader.read(args)
		
		csv_parser = CSVParser(self._errors)
		input_file_path = settings['input_file']['path']
		input_file_format = settings['input_file']['format']
		table, columns = csv_parser.csv2table(input_file_path, input_file_format)
		
		# csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		
		print(table)
		
		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')