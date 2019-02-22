# -*- coding: utf-8 -*

from modules.indicators.Buffer import *
from modules.indicators.EquityA import *

class ResEquity:
	
	def __init__(self):
		self.log = []
		
		self.h_eqv = EquityA()
		self.l_eqv = EquityA()
		self.r_eqv = EquityA()
		
	def calc(self, high_price, low_price, price, lots, open_lots_balance):
		h_eqv_val = self.h_eqv.calc_by_lots_balance(high_price, open_lots_balance)
		l_eqv_val = self.l_eqv.calc_by_lots_balance(low_price, open_lots_balance)
		r_eqv_val = self.r_eqv.calc_by_lots(price, lots)
		print(self.r_eqv.stat_eqv)
		
		return h_eqv_val, l_eqv_val, r_eqv_val