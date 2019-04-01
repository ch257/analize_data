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
		
		csv_parser1 = CSVParser(self._errors)
		csv_parser2 = CSVParser(self._errors)
		input_folder_path = settings['input_folder']['path']
		input_file_format = settings['input_file']['format']
		
		input_file_path1 = input_folder_path + 'join_test1.txt'
		input_file_path2 = input_folder_path + 'join_test2.txt'
		
		table1, columns1 = csv_parser1.csv2table(input_file_path1, input_file_format)
		table2, columns2 = csv_parser2.csv2table(input_file_path2, input_file_format)
		
		ti1 = TableIterator(self._errors, table1, columns1)
		ti2 = TableIterator(self._errors, table2, columns2)
		while not ti1.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			v1 = rec1['<VOL>']
			while not ti2.EOD:
				rec2, rec_cnt2 = ti2.next_rec()
				date2 = rec2['<DATE>']
				time2 = rec2['<TIME>']
				v2 = rec2['<VOL>']
				if date1 == date2:
					# print(date1.date(), '=', date2.date(), ' ', time1.time(), '=', time2.time(), ' ', v1, '=', v2)
					if time1 == time2:
						print(date1.date(), '=', date2.date(), ' ', time1.time(), '=', time2.time(), ' ', v1, '=', v2)
						break
					elif time1 < time2:
						print(date1.date(), '=', date2.date(), ' ', time1.time(), '=', 'null', ' ', 'null')
						ti2.rec_cnt -= 1
						break
				elif date1 < date2:
					print(date1.date(), '=', 'null', ' ', time1.time(), '=', 'null', ' ', 'null')
					ti2.rec_cnt -= 1
					break
				
		
		
		# output_file_path = settings['output_file']['path']
		# output_file_format = settings['output_file']['format']
		# csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		
		
		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')