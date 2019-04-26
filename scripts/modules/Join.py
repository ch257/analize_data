# -*- coding: utf-8 -*

from modules.common_2_0.Errors import *
from modules.common_2_0.SettingsReader import *
from modules.common_2_0.CSVParser import *
from modules.common_2_0.TableIterator import *
from modules.common_2_0.TableTools import *
#######################


class Join:
	def __init__(self):
		self._errors = Errors()
	
	def main(self, args):
		settings_reader = SettingsReader(self._errors)
		settings = settings_reader.read(args)
		# print(settings)
		
		csv_parser1 = CSVParser(self._errors)
		csv_parser2 = CSVParser(self._errors)
		input_folder_path = settings['input_folder']['path']
		input_file_format = settings['input_file']['format']
		
		input_file_path1 = input_folder_path + 'join_test1.txt'
		input_file_path2 = input_folder_path + 'join_test2.txt'
		
		table1, columns1 = csv_parser1.csv2table(input_file_path1, input_file_format)
		table2, columns2 = csv_parser2.csv2table(input_file_path2, input_file_format)
		
		t_tools = TableTools(self._errors)
		
		joined_table, joined_columns = t_tools.left_join(table1, columns1, table2, columns2)
		oi = TableIterator(self._errors, joined_table, joined_columns)
		while not oi.EOD:
			rec, rec_cnt = oi.next_rec()
			# print(rec['<DATE>'].date(), rec['<TIME>'].time(), rec['t1.<VOL>'], rec['t2.<VOL>'])
			print(rec['<DATE>'].date(), rec['<TIME>'].time(), rec['t2.<RATE>'])


		
		
		# output_file_path = settings['output_file']['path']
		# output_file_format = settings['output_file']['format']
		# csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		
		
		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')