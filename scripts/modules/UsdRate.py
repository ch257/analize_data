# -*- coding: utf-8 -*

from modules.common_2_0.Errors import *
from modules.common_2_0.SettingsReader import *
from modules.common_2_0.CSVParser import *
from modules.common_2_0.TableIterator import *
from modules.common_2_0.TableTools import *
from modules.common_2_0.FileSystem import *
from modules.common_2_0.Files import *
#######################


class UsdRate:
	def __init__(self):
		self._errors = Errors()
	
	def main(self, args):
		settings_reader = SettingsReader(self._errors)
		settings = settings_reader.read(args)
		# print(settings['usd_rate'])
		input_folder_path = settings['input_folder']['path']
		output_folder_path = settings['output_folder']['path']
		
		input_file_format = settings['input_file']['format']
		
		ur_table, ur_columns = csv_parser.csv2table(ur_file_path, ur_file_format)
		
		fs = FileSystem(self._errors)
		csv_parser = CSVParser(self._errors)
		file_list = fs.get_folder_list(input_folder_path)
		for ticker in settings['usd_rate']:
			for file_name in file_list:
				f_ticker = file_name.split('_')[0]
				if f_ticker == ticker:
					input_file_path = input_folder_path + file_name
					table, columns = csv_parser.csv2table(input_file_path, input_file_format)
					print(ticker)
		
		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')