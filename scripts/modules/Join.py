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
	
	def fil_cross(self, dt, tm, columns1, columns2, cross_columns, rec1, rec2, output_table):
		output_table['<DATE>'].append(dt)
		output_table['<TIME>'].append(tm)
		for col in columns1:
			if col not in cross_columns:
				output_table['t1.' + col].append(rec1[col])
		for col in columns2:
			if col not in cross_columns:
				output_table['t2.' + col].append(rec2[col])

	def fil_left(self, dt, tm, columns1, columns2, cross_columns, rec1, output_table):
		output_table['<DATE>'].append(dt)
		output_table['<TIME>'].append(tm)
		for col in columns1:
			if col not in cross_columns:
				output_table['t1.' + col].append(rec1[col])
		for col in columns2:
			if col not in cross_columns:
				output_table['t2.' + col].append(None)
				
	def fil_right(self, dt, tm, columns1, columns2, cross_columns, rec2, output_table):
		output_table['<DATE>'].append(dt)
		output_table['<TIME>'].append(tm)
		for col in columns1:
			if col not in cross_columns:
				output_table['t1.' + col].append(None)
		for col in columns2:
			if col not in cross_columns:
				output_table['t2.' + col].append(rec2[col])
				
	def full_join(self, table1, columns1, table2, columns2):
		cross_columns = ['<DATE>', '<TIME>']
		output_table = {
			'<DATE>': [], 
			'<TIME>': []
		}
		output_columns = cross_columns
		for col in columns1:
			if col not in cross_columns:	
				output_columns.append('t1.' + col)
				output_table['t1.' + col] = []
		for col in columns2:
			if col not in cross_columns:	
				output_columns.append('t2.' + col)
				output_table['t2.' + col] = []
			
		ti1 = TableIterator(self._errors, table1, columns1)
		ti2 = TableIterator(self._errors, table2, columns2)
		while not ti1.EOD and not ti2.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			while not ti2.EOD:
				rec2, rec_cnt2 = ti2.next_rec()
				date2 = rec2['<DATE>']
				time2 = rec2['<TIME>']
				if date1 == date2:
					if time1 == time2:
						self.fil_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						self.fil_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
						ti2.rec_cnt -= 1
						break
					else:
						self.fil_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
				elif date1 < date2:
					self.fil_left(date2, time2, columns1, columns2, cross_columns, rec1, output_table)
					ti2.rec_cnt -= 1
					break
				else:
					self.fil_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		while not ti1.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			self.fil_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
		
		while not ti2.EOD:
			rec2, rec_cnt2 = ti2.next_rec()
			date2 = rec2['<DATE>']
			time2 = rec2['<TIME>']
			self.fil_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		return output_table, output_columns
				
	def left_join(self, table1, columns1, table2, columns2):
		cross_columns = ['<DATE>', '<TIME>']
		output_table = {
			'<DATE>': [], 
			'<TIME>': []
		}
		output_columns = cross_columns
		for col in columns1:
			if col not in cross_columns:	
				output_columns.append('t1.' + col)
				output_table['t1.' + col] = []
		for col in columns2:
			if col not in cross_columns:	
				output_columns.append('t2.' + col)
				output_table['t2.' + col] = []
			
		ti1 = TableIterator(self._errors, table1, columns1)
		ti2 = TableIterator(self._errors, table2, columns2)
		while not ti1.EOD and not ti2.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			while not ti2.EOD:
				rec2, rec_cnt2 = ti2.next_rec()
				date2 = rec2['<DATE>']
				time2 = rec2['<TIME>']
				if date1 == date2:
					if time1 == time2:
						self.fil_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						self.fil_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
						ti2.rec_cnt -= 1
						break
				elif date1 < date2:
					self.fil_left(date2, time2, columns1, columns2, cross_columns, rec1, rec2, output_table)
					ti2.rec_cnt -= 1
					break
		
		while not ti1.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			self.fil_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
		
		return output_table, output_columns
				
	def right_join(self, table1, columns1, table2, columns2):
		cross_columns = ['<DATE>', '<TIME>']
		output_table = {
			'<DATE>': [], 
			'<TIME>': []
		}
		output_columns = cross_columns
		for col in columns1:
			if col not in cross_columns:	
				output_columns.append('t1.' + col)
				output_table['t1.' + col] = []
		for col in columns2:
			if col not in cross_columns:	
				output_columns.append('t2.' + col)
				output_table['t2.' + col] = []
			
		ti1 = TableIterator(self._errors, table1, columns1)
		ti2 = TableIterator(self._errors, table2, columns2)
		while not ti1.EOD and not ti2.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			while not ti2.EOD:
				rec2, rec_cnt2 = ti2.next_rec()
				date2 = rec2['<DATE>']
				time2 = rec2['<TIME>']
				if date1 == date2:
					if time1 == time2:
						self.fil_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						ti2.rec_cnt -= 1
						break
					else:
						self.fil_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
				elif date1 < date2:
					ti2.rec_cnt -= 1
					break
				else:
					self.fil_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		while not ti2.EOD:
			rec2, rec_cnt2 = ti2.next_rec()
			date2 = rec2['<DATE>']
			time2 = rec2['<TIME>']
			self.fil_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		return output_table, output_columns
				
	def inner_join(self, table1, columns1, table2, columns2):
		cross_columns = ['<DATE>', '<TIME>']
		output_table = {
			'<DATE>': [], 
			'<TIME>': []
		}
		output_columns = cross_columns
		for col in columns1:
			if col not in cross_columns:	
				output_columns.append('t1.' + col)
				output_table['t1.' + col] = []
		for col in columns2:
			if col not in cross_columns:	
				output_columns.append('t2.' + col)
				output_table['t2.' + col] = []
			
		ti1 = TableIterator(self._errors, table1, columns1)
		ti2 = TableIterator(self._errors, table2, columns2)
		while not ti1.EOD and not ti2.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			while not ti2.EOD:
				rec2, rec_cnt2 = ti2.next_rec()
				date2 = rec2['<DATE>']
				time2 = rec2['<TIME>']
				if date1 == date2:
					if time1 == time2:
						self.fil_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						ti2.rec_cnt -= 1
						break
				elif date1 < date2:
					ti2.rec_cnt -= 1
					break
		
		return output_table, output_columns

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
		
		joined_table, joined_columns = self.left_join(table1, columns1, table2, columns2)
		oi = TableIterator(self._errors, joined_table, joined_columns)
		while not oi.EOD:
			rec, rec_cnt = oi.next_rec()
			print(rec['<DATE>'].date(), rec['<TIME>'].time(), rec['t1.<VOL>'], rec['t2.<VOL>'])


		
		
		# output_file_path = settings['output_file']['path']
		# output_file_format = settings['output_file']['format']
		# csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		
		
		if self._errors.error_occured:
			self._errors.print_errors()
		else:
			print('OK\n')