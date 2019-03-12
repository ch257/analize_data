# -*- coding: utf-8 -*

from modules.common.Tools import *

class TableIterator:
	
	def __init__(self, errors, table, columns):
		self.errors = errors
		self.tools = Tools(errors)
		self.table = table
		self.rec_cnt = -1
		self.length = len(table[columns[0]]) - 1
		if self.errors.error_occured or self.length < 0:
			self.EOD = True
		else:
			self.EOD = False
			
	def get_next_rec(self):
		if self.errors.error_occured:
			self.EOD = True
			return None
			
		self.rec_cnt += 1
		if self.rec_cnt < self.length:
			rec = self.tools.get_rec_from_table(self.rec_cnt, self.table)
		else:
			rec = self.tools.get_rec_from_table(self.rec_cnt, self.table)
			self.EOD = True
		
		return rec, self.rec_cnt
