# -*- coding: utf-8 -*

from modules.indicators.Buffer import *
from modules.indicators.EquityA import *

class OrdersExec:
	
	def __init__(self, order_holder):
		self.log = []
		self.order_holder = order_holder
		self.market_price = 0
		self.h_eqv = EquityA()
		self.l_eqv = EquityA()

	def exec(self, high_price, low_price, market_price):
		self.market_price = market_price
		h_eqv_val = self.h_eqv.calc_by_lots_balance(high_price, self.order_holder.open_orders_balance)
		l_eqv_val = self.l_eqv.calc_by_lots_balance(low_price, self.order_holder.open_orders_balance)
		self.log = [h_eqv_val, l_eqv_val]
		print(self.log)
		# print(self.order_holder.open_orders_balance)
			
	def BuyMarket(self, lots):
		self.order_holder.add_open_order(self.market_price, lots)

	def SellMarket(self, lots):
		self.order_holder.add_open_order(self.market_price, -lots)

	def BuyLimit(self, lots, price):
		pass

	def SellLimit(self, lots, price):
		pass

	def BuyStop(self, lots, price):
		pass
		
	def SellStop(self, lots, price):
		pass
		
