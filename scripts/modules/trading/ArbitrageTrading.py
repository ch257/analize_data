# -*- coding: utf-8 -*

from modules.indicators.Buffer import *
from modules.indicators.EquityA import *

class ArbitrageTrading:
	
	def __init__(self, order_exec):
		self.order_exec = order_exec
		self.log = []
		self.lots = 0
			
	def trade(self, open_long, open_short, close_long, close_short):
		if open_long:
			self.order_exec.SellMarket(1)
		if open_short:
			self.order_exec.BuyMarket(1)
		
		self.log = []
		
