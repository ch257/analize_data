# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class OrdersExec:
	
	def __init__(self, order_holder):
		self.log = []
		self.order_holder = order_holder
		self.market_price = 0

	def exec(self, high_price, low_price, market_price):
		self.market_price = market_price
		print(self.order_holder.open_orders_balance)
			
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
		
