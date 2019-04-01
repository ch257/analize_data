# -*- coding: utf-8 -*

from modules.common_2_0.Errors import *
from modules.common_2_0.SettingsReader import *
from modules.common_2_0.CSVParser import *
from modules.common_2_0.TableIterator import *
from modules.common_2_0.Tools import *
#######################


class Join:
	def __init__(self):
		self._errors = Errors()
	
	def main(self, args):
		settings_reader = SettingsReader(self._errors)
		settings = settings_reader.read(args)
		# print(settings)
		
		csv_parser = CSVParser(self._errors)
		input_folder_path = settings['input_folder']['path']
		input_file_format = settings['input_file']['format']
		
		input_file_path1 = input_folder_path + 'join_test1.txt'
		input_file_path2 = input_folder_path + 'join_test2.txt'
		
		table1, columns1 = csv_parser.csv2table(input_file_path1, input_file_format)
		table2, columns2 = csv_parser.csv2table(input_file_path2, input_file_format)
		
		print(table1)
		print(table2)
		
		# table_i = TableIterator(self._errors, table, columns)
		# while not table_i.EOD:
			# rec, rec_cnt = table_i.next_rec()
			# print(rec)
		
		
		# output_file_path = settings['output_file']['path']
		# output_file_format = settings['output_file']['format']
		# csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		
		
		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')