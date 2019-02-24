# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class EquityA:
	
	def __init__(self):
		self.buffer = Buffer(1)
		self.dyn_eqv = 0
		self.stat_eqv = 0
		self.eqv = 0
		self.lots_balance = 0
		
	def calc_by_lots(self, price, lots=0):
		self.lots_balance += lots
		if self.buffer.is_ready:
			self.dyn_eqv += (price - self.buffer.buff[0]) * self.lots_balance
			self.stat_eqv -= price * lots
			if self.dyn_eqv == 0:
				self.eqv = self.stat_eqv
			else:
				self.eqv = self.dyn_eqv
			
		else:
			self.stat_eqv -= price * lots
			self.eqv = 0
		
		self.buffer.slide(price)
		return self.eqv
		
	def calc_by_lots_balance(self, price, lots_balance):
		self.lots_balance = lots_balance
		if self.buffer.is_ready:
			self.dyn_eqv += (price - self.buffer.buff[0]) * self.lots_balance
			if self.dyn_eqv == 0:
				self.eqv = self.stat_eqv
			else:
				self.eqv = self.dyn_eqv
			
		else:
			self.eqv = 0
		
		self.buffer.slide(price)
		return self.eqv

