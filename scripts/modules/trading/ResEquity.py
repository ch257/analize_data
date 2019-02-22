# -*- coding: utf-8 -*

from modules.indicators.Buffer import *
from modules.indicators.EquityA import *

class ResEquity:
	
	def __init__(self):
		self.log = []
		
		self.h_eqv = EquityA()
		self.l_eqv = EquityA()
		self.result_eqv = EquityA()
		
	def calc(self, high_price, low_price, price, lots_balance, lots):
		pass