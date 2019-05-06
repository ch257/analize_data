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
	
	def shape_moex_rate(self, r_file_path, input_file_format):
		t_tools = TableTools(self._errors)
		tools = Tools(self._errors)
		
		start_time = '10:00:00'
		stop_time = '00:00:00'
		step_time = '00:01:00'
		exclude_time = ('18:46:00', '19:01:00')
		start_date = '01.12.2018'
		stop_date = dt.strftime((dt.today()), '%d.%m.%Y')
		step_date = 1
		
		date_period = (start_date, stop_date)
		time_period = (start_time, stop_time)
		exclude_time_periods = [exclude_time]
		dt_table, dt_columns = t_tools.gen_datetime_table(date_period, step_date, time_period, step_time, exclude_time_periods=exclude_time_periods)
		
		r_csv_parser = CSVParser(self._errors)
		r_table, r_columns = r_csv_parser.csv2table(r_file_path, input_file_format)
		tools.add_columns(['<TM_RATE>'], r_table, r_columns)
		
		ti = TableIterator(self._errors, r_table, r_columns)
		while not ti.EOD:
			rec, rec_cnt = ti.next_rec()
			while not ti.EOD:
				f_rec, f_rec_cnt = ti.next_rec()
				if f_rec['<DATE>'] > rec['<DATE>'] and f_rec['<TIME>'] == rec['<TIME>']:
					tools.update_cells(['<TM_RATE>'], [f_rec['<RATE>']], rec_cnt, r_table)
					ti.rec_cnt = rec_cnt
					break	
		
		joined_table, joined_columns = t_tools.left_join(dt_table, dt_columns, r_table, r_columns)
		
		ti = TableIterator(self._errors, joined_table, joined_columns)
		tools.add_columns(['<YESTERDAY_RATE>', '<TOMORROW_RATE>'], joined_table, joined_columns)
		
		last_yesterday_rate = None
		last_tomorrow_rate = None
		rate_time = dt.strptime('18:30:00', '%H:%M:%S')
		while not ti.EOD:
			rec, rec_cnt = ti.next_rec()
			tools.update_cells(['<YESTERDAY_RATE>'], [last_yesterday_rate], rec_cnt, joined_table)
			tools.update_cells(['<TOMORROW_RATE>'], [last_tomorrow_rate], rec_cnt, joined_table)	
			
			if rec['<TIME>'] == rate_time:
				if rec['t2.<RATE>']:
					last_yesterday_rate = rec['t2.<RATE>']
					last_tomorrow_rate = rec['t2.<TM_RATE>']
			
		# ti = TableIterator(self._errors, joined_table, joined_columns)	
		# while not ti.EOD:
			# rec, rec_cnt = ti.next_rec()
			# print(rec['<DATE>'], rec['<TIME>'], rec['t2.<RATE>'], rec['<YESTERDAY_RATE>'], rec['<TOMORROW_RATE>'])
		
		return joined_table, joined_columns
	
	def main(self, args):
		settings_reader = SettingsReader(self._errors)
		settings = settings_reader.read(args)
		# print(settings['usd_rate'])
		input_folder_path = settings['input_folder']['path']
		output_folder_path = settings['output_folder']['path']
		
		input_file_format = settings['input_file']['format']
		output_file_format = settings['output_file']['format']
		
		ur_csv_parser = CSVParser(self._errors)
		ur_file_path = settings['rate_file']['usd_rate_file_path']
		ur_table, ur_columns = self.shape_moex_rate(ur_file_path, input_file_format)
		
		csv_parser = CSVParser(self._errors)
		t_tools = TableTools(self._errors)
		tools = Tools(self._errors)
		fs = FileSystem(self._errors)
				
		# csv_parser.table2csv(ur_table, ur_columns, output_folder_path + '..\\moex_rates\\rates.txt', output_file_format)
		
		file_list = fs.get_folder_list(input_folder_path)
		for ticker in settings['usd_rate']:
			usd_rate_mlt = float(settings['usd_rate'][ticker])
			for file_name in file_list:
				f_ticker = file_name.split('_')[0]
				if f_ticker == ticker:
					input_file_path = input_folder_path + file_name
					table, columns = csv_parser.csv2table(input_file_path, input_file_format)
					joined_table, joined_columns = t_tools.left_join(table, columns, ur_table, ur_columns)
					
					yd_table = tools.create_table(columns)
					tm_table = tools.create_table(columns)
					
					oi = TableIterator(self._errors, joined_table, joined_columns)
					while not oi.EOD:
						rec, rec_cnt = oi.next_rec()
						tm_table['<TICKER>'].append(rec['t1.<TICKER>'])
						tm_table['<PER>'].append(rec['t1.<PER>'])
						tm_table['<DATE>'].append(rec['<DATE>'])
						tm_table['<TIME>'].append(rec['<TIME>'])
						tm_table['<VOL>'].append(rec['t1.<VOL>'])
						if rec['t2.<TOMORROW_RATE>']:
							mlt = rec['t2.<TOMORROW_RATE>'] * usd_rate_mlt
							tm_table['<OPEN>'].append(rec['t1.<OPEN>'] * mlt)
							tm_table['<HIGH>'].append(rec['t1.<HIGH>'] * mlt)
							tm_table['<LOW>'].append(rec['t1.<LOW>'] * mlt)
							tm_table['<CLOSE>'].append(rec['t1.<CLOSE>'] * mlt)
						else:
							tm_table['<OPEN>'].append(None)
							tm_table['<HIGH>'].append(None)
							tm_table['<LOW>'].append(None)
							tm_table['<CLOSE>'].append(None)
					
					csv_parser.table2csv(tm_table, columns, output_folder_path + 'tm_' + file_name, output_file_format)
					
					oi = TableIterator(self._errors, joined_table, joined_columns)
					while not oi.EOD:
						rec, rec_cnt = oi.next_rec()
						yd_table['<TICKER>'].append(rec['t1.<TICKER>'])
						yd_table['<PER>'].append(rec['t1.<PER>'])
						yd_table['<DATE>'].append(rec['<DATE>'])
						yd_table['<TIME>'].append(rec['<TIME>'])
						yd_table['<VOL>'].append(rec['t1.<VOL>'])
						# if rec['t2.<YESTERDAY_RATE>']:
						mlt = rec['t2.<YESTERDAY_RATE>'] * usd_rate_mlt
						yd_table['<OPEN>'].append(rec['t1.<OPEN>'] * mlt)
						yd_table['<HIGH>'].append(rec['t1.<HIGH>'] * mlt)
						yd_table['<LOW>'].append(rec['t1.<LOW>'] * mlt)
						yd_table['<CLOSE>'].append(rec['t1.<CLOSE>'] * mlt)
						# else:
							# yd_table['<OPEN>'].append(None)
							# yd_table['<HIGH>'].append(None)
							# yd_table['<LOW>'].append(None)
							# yd_table['<CLOSE>'].append(None)
					
					csv_parser.table2csv(yd_table, columns, output_folder_path + 'yd_' + file_name, output_file_format)
		
		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')