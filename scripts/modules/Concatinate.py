# -*- coding: utf-8 -*

from modules.common_2_0.Errors import *
from modules.common_2_0.SettingsReader import *
from modules.common_2_0.CSVParser import *
from modules.common_2_0.TableIterator import *
from modules.common_2_0.TableTools import *
from modules.common_2_0.FileSystem import *
from modules.common_2_0.Files import *
#######################


class Concatinate:
	def __init__(self):
		self._errors = Errors()
	
	def main(self, args):
		settings_reader = SettingsReader(self._errors)
		settings = settings_reader.read(args)
		# print(settings)
		input_folder_path = settings['input_folder']['path']
		output_folder_path = settings['output_folder']['path']
		tickers = settings['contracts']['tickers']
		header = settings['contracts']['header']
		
		fs = FileSystem(self._errors)
		fs.create_folder_branch(output_folder_path)
		concatinated_f = Files(self._errors)
		curr_f = Files(self._errors)
		concatinated_f_names = []
		for ticker in tickers:
			folder_list = fs.get_folder_list(input_folder_path + ticker)
			for folder in folder_list:
				timeframe_list = fs.get_folder_list(input_folder_path + ticker + '\\' + folder)
				for timeframe in timeframe_list:
					concatinated_f_name = ticker + '_' + timeframe + '.txt'
					concatinated_f_path = output_folder_path + concatinated_f_name
					if concatinated_f_name in concatinated_f_names:
						concatinated_f.open_file(concatinated_f_path, 'a')
					else:
						concatinated_f.open_file(concatinated_f_path, 'w')
						concatinated_f.write_line(header)
						concatinated_f_names.append(concatinated_f_name)

					print(concatinated_f_name)
					path = input_folder_path + ticker + '\\' + folder + '\\' + timeframe
					file_list = fs.get_folder_list(path)
					for f_name in file_list:
						curr_f_path = path + '\\' + f_name
						curr_f.open_file(curr_f_path, 'r')
						while not self._errors.error_occured:
							line = curr_f.read_line()
							if line != '':
								line = line.rstrip('\n')
								if line != '' and line != header:
									concatinated_f.write_line(line)
							else:
								break
						
						curr_f.close_file()
					concatinated_f.close_file()

		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')