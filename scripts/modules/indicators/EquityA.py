# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class EquityA:
	
	def __init__(self):
		self.buffer = Buffer(1)
		self.eqv = 0
		self.lots_balance = 0
		
	def calc_by_lots(self, new_item, lots=0):
		self.lots_balance += lots
		if self.buffer.is_ready:
			self.eqv += (new_item - self.buffer.buff[0]) * self.lots_balance
		
		self.buffer.slide(new_item)
		return self.eqv

	def calc_by_lots_balance(self, new_item, lots_balance):
		self.lots_balance = lots_balance
		if self.buffer.is_ready:
			self.eqv += (new_item - self.buffer.buff[0]) * self.lots_balance
		
		self.buffer.slide(new_item)
		return self.eqv


