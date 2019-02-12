# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class ArbitrageTrading:
	
	def __init__(self):
		self.log = []
			
	def calc(self, open_long, open_short, close_long, close_short, high_price, low_price, market_price):
		self.log = []
		
