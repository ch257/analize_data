# -*- coding: utf-8 -*

import time
import datetime
from datetime import datetime as dt, date, time as tm

from modules.common_2_0.TableIterator import *

class TableTools:
	def __init__(self, errors):
		self._errors = errors

	def _fill_cross(self, dt, tm, columns1, columns2, cross_columns, rec1, rec2, output_table):
		output_table['<DATE>'].append(dt)
		output_table['<TIME>'].append(tm)
		for col in columns1:
			if col not in cross_columns:
				output_table['t1.' + col].append(rec1[col])
		for col in columns2:
			if col not in cross_columns:
				output_table['t2.' + col].append(rec2[col])

	def _fill_left(self, dt, tm, columns1, columns2, cross_columns, rec1, output_table):
		output_table['<DATE>'].append(dt)
		output_table['<TIME>'].append(tm)
		for col in columns1:
			if col not in cross_columns:
				output_table['t1.' + col].append(rec1[col])
		for col in columns2:
			if col not in cross_columns:
				output_table['t2.' + col].append(None)
				
	def _fill_right(self, dt, tm, columns1, columns2, cross_columns, rec2, output_table):
		output_table['<DATE>'].append(dt)
		output_table['<TIME>'].append(tm)
		for col in columns1:
			if col not in cross_columns:
				output_table['t1.' + col].append(None)
		for col in columns2:
			if col not in cross_columns:
				output_table['t2.' + col].append(rec2[col])
				
	def full_join(self, table1, columns1, table2, columns2):
		if self._errors.error_occured:
			return None
		
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
						self._fill_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						self._fill_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
						ti2.rec_cnt -= 1
						break
					else:
						self._fill_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
				elif date1 < date2:
					self._fill_left(date2, time2, columns1, columns2, cross_columns, rec1, output_table)
					ti2.rec_cnt -= 1
					break
				else:
					self._fill_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		while not ti1.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			self._fill_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
		
		while not ti2.EOD:
			rec2, rec_cnt2 = ti2.next_rec()
			date2 = rec2['<DATE>']
			time2 = rec2['<TIME>']
			self._fill_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		return output_table, output_columns
				
	def left_join(self, table1, columns1, table2, columns2):
		if self._errors.error_occured:
			return None

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
						self._fill_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						self._fill_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
						ti2.rec_cnt -= 1
						break
				elif date1 < date2:
					self._fill_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
					ti2.rec_cnt -= 1
					break
		
		while not ti1.EOD:
			rec1, rec_cnt1 = ti1.next_rec()
			date1 = rec1['<DATE>']
			time1 = rec1['<TIME>']
			self._fill_left(date1, time1, columns1, columns2, cross_columns, rec1, output_table)
		
		return output_table, output_columns
				
	def right_join(self, table1, columns1, table2, columns2):
		if self._errors.error_occured:
			return None

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
						self._fill_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						ti2.rec_cnt -= 1
						break
					else:
						self._fill_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
				elif date1 < date2:
					ti2.rec_cnt -= 1
					break
				else:
					self._fill_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		while not ti2.EOD:
			rec2, rec_cnt2 = ti2.next_rec()
			date2 = rec2['<DATE>']
			time2 = rec2['<TIME>']
			self._fill_right(date2, time2, columns1, columns2, cross_columns, rec2, output_table)
		
		return output_table, output_columns
				
	def inner_join(self, table1, columns1, table2, columns2):
		if self._errors.error_occured:
			return None

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
						self._fill_cross(date1, time1, columns1, columns2, cross_columns, rec1, rec2, output_table)
						break
					elif time1 < time2:
						ti2.rec_cnt -= 1
						break
				elif date1 < date2:
					ti2.rec_cnt -= 1
					break
		
		return output_table, output_columns

	def gen_datetime_table(self, date_period, time_period, exclude_date_periods = [], exclude_time_periods = []):
		columns = ['<DATE>', '<TIME>']
		table = {}
		for  col in columns:
			table[col] = []
		pass
		
	def time_range(self, start, stop, step):
		rng = []
		start_time = dt.strptime(start, '%H:%M:%S')
		stop_time = dt.strptime(stop, '%H:%M:%S')
		if stop_time == dt.strptime('00:00:00', '%H:%M:%S'): 
			stop_time = dt.strptime(stop, '%H:%M:%S') + datetime.timedelta(days=1)
		step_time = dt.strptime(step, '%H:%M:%S').time()
		step_time = datetime.timedelta(hours=step_time.hour, minutes=step_time.minute, seconds=step_time.second)
		
		curr_time = start_time
		while not self.errors.error_occured:
			if curr_time >= stop_time:
				break
			else:
				rng.append(curr_time.time())
			curr_time += step_time
		
		return rng
	
	def generate_time_range(self, start, stop, step, exclude=[]):
		rng = []
		start_time = dt.strptime(start, '%H:%M:%S')
		stop_time = dt.strptime(stop, '%H:%M:%S')
		if stop_time == dt.strptime('00:00:00', '%H:%M:%S'): 
			stop_time += datetime.timedelta(days=1)
		step_time = dt.strptime(step, '%H:%M:%S').time()
		step_time = datetime.timedelta(hours=step_time.hour, minutes=step_time.minute, seconds=step_time.second)
		
		for excl_cnt in range(len(exclude)):
			excl = exclude[excl_cnt].split('-')
			excl[0] = dt.strptime(excl[0], '%H:%M:%S')
			excl[1] = dt.strptime(excl[1], '%H:%M:%S')
			if excl[1] == dt.strptime('00:00:00', '%H:%M:%S'):
				excl[1] += datetime.timedelta(days=1)
			
			exclude[excl_cnt] = [excl[0], excl[1]]

		curr_time = start_time
		while not self.errors.error_occured:
			if curr_time >= stop_time:
				break
			else:
				in_exclude = False
				for excl in exclude: 
					if excl[0] <= curr_time and excl[1] > curr_time:
						in_exclude = True
						break
				if not in_exclude:
					rng.append(tm.strftime(curr_time.time(), '%H%M%S'))
			curr_time += step_time
		
		return rng