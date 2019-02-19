# -*- coding: utf-8 -*

from modules.indicators.Buffer import *
from modules.indicators.EquityA import *
from modules.trading.OrdersHolder import *

class OrdersExec:
	
	def __init__(self):
		self.log = []
		self.order_holder = OrdersHolder()
		self.market_price = 0
		self.high_price = 0 
		self.low_price = 0
		self.h_eqv = EquityA()
		self.l_eqv = EquityA()
		self.result_eqv = EquityA()
		self.h_eqv_val = 0
		self.l_eqv_val = 0
		self.result_eqv_val = 0

	def exec_orders(self, high_price, low_price, market_price):
		self.market_price = market_price
		self.high_price = high_price
		self.low_price = low_price
		# print(self.order_holder.open_orders)
		# print(self.non_loss_price())
		# for _idx in self.order_holder.pending_orders:
			# status = self.order_holder.pending_orders[_idx]['status']
			# type = self.order_holder.pending_orders[_idx]['type']
			# price = self.order_holder.pending_orders[_idx]['price']
			# lots = self.order_holder.pending_orders[_idx]['lots']
			# print(price, lots, status)
			# if status == 'act':
				# if type == 'limit':
					# if lots > 0:
						# if low_price < price:
							# self.order_holder.exec_pending_order(_idx)
					# elif lots < 0:
						# if high_price > price:
							# self.order_holder.exec_pending_order(_idx)
				# elif type == 'stop':
					# if lots < 0:
						# if low_price < price:
							# self.order_holder.exec_pending_order(_idx)
					# elif lots > 0:
						# if high_price > price:
							# self.order_holder.exec_pending_order(_idx)
			
		
	def calc_equty(self):
		self.result_eqv.calc_by_lots(self.market_price, 0)
		self.h_eqv_val = self.h_eqv.calc_by_lots_balance(self.high_price, self.order_holder.open_lots_balance)
		self.l_eqv_val = self.l_eqv.calc_by_lots_balance(self.low_price, self.order_holder.open_lots_balance)
		self.log = [self.h_eqv_val, self.l_eqv_val, self.result_eqv_val, self.non_loss_price()]
		
	def non_loss_price(self):
		nlp = None
		if len(self.order_holder.open_orders) > 0:
			nlp = 0
			lots_sum = 0
			for _idx in self.order_holder.open_orders:
				order = self.order_holder.open_orders[_idx]
				nlp += order['price'] * order['lots']
				lots_sum += order['lots']
			nlp = nlp / lots_sum
		
		return nlp
		
	def BuyMarket(self, lots):
		self.order_holder.add_open_order(self.market_price, lots)
		self.result_eqv_val = self.result_eqv.calc_by_lots(self.market_price, lots)
		self.log = [self.h_eqv_val, self.l_eqv_val, self.result_eqv_val]
		# print('Buy:', self.market_price)

	def SellMarket(self, lots):
		self.order_holder.add_open_order(self.market_price, -lots)
		self.result_eqv_val = self.result_eqv.calc_by_lots(self.market_price, -lots)
		self.log = [self.h_eqv_val, self.l_eqv_val, self.result_eqv_val]
		# print('Sell:', self.market_price)

	# def BuyLimit(self, lots, price):
		# if price < self.market_price:
			# self.order_holder.add_pending_order(price, lots, 'limit')

	# def SellLimit(self, lots, price):
		# if price > self.market_price:
			# self.order_holder.add_pending_order(price, -lots, 'limit')

	# def BuyStop(self, lots, price):
		# if price > self.market_price:
			# self.order_holder.add_pending_order(price, lots, 'stop')
		
	# def SellStop(self, lots, price):
		# if price < self.market_price:
			# self.order_holder.add_pending_order(price, -lots, 'stop')
			
	# def CancelBuyLimits(self):
		# for _idx in self.order_holder.pending_orders:
			# type = self.order_holder.pending_orders[_idx]['type']
			# lots = self.order_holder.pending_orders[_idx]['lots']
			# if type == 'limit' and lots > 0:
				# self.order_holder.cancel_pending_order(_idx)
	
	# def CancelSellLimits(self):
		# for _idx in self.order_holder.pending_orders:
			# type = self.order_holder.pending_orders[_idx]['type']
			# lots = self.order_holder.pending_orders[_idx]['lots']
			# if type == 'limit' and lots < 0:
				# self.order_holder.cancel_pending_order(_idx)
	
		
