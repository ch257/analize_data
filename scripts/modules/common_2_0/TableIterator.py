# -*- coding: utf-8 -*

from modules.common_2_0.Tools import *

class TableIterator:
	
	def __init__(self, errors, table, columns):
		self._errors = errors
		self._tools = Tools(self._errors)
		self.table = table
		self.rec_cnt = -1
		self.length = len(table[columns[0]]) - 1
		if self._errors.error_occured or self.length < 0:
			self.EOD = True
		else:
			self.EOD = False
			
	def next_rec(self):
		if self._errors.error_occured:
			self.EOD = True
			return None, None
			
		self.rec_cnt += 1
		if self.rec_cnt < self.length:
			rec = self._tools.get_rec_from_table(self.rec_cnt, self.table)
		else:
			rec = self._tools.get_rec_from_table(self.rec_cnt, self.table)
			self.EOD = True
		
		return rec, self.rec_cnt
