# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class OrdersHolder:
	
	def __init__(self):
		self.log = []
		self.open_orders = {}
		self.open_orders_log = {}
		self.pending_orders_log = {}
		
		self.open_lots_balance = 0
		self.prev_lots_balance = 0
		
		# self.pending_orders = {}
		# self.open_orders = {}
		
		# self.open_lots_balance = 0
		# self.last_open_price = 0
		
		# self.buy_stop_order_cnt = 0
		# self.sell_stop_order_cnt = 0
		# self.last_buy_stop_price = 0
		# self.last_sell_stop_price = 0
		
		# self.buy_limit_order_cnt = 0
		# self.sell_limit_order_cnt = 0
		# self.last_buy_limit_price = 0
		# self.last_sell_limit_price = 0

		
	def add_open_order(self, price, lots):
		order = {
			# 'date': None,
			# 'time': None,
			'price': price,
			'lots': lots
		}
		self.open_orders_log[len(self.open_orders_log)] = order
		
		self.prev_lots_balance = self.open_lots_balance
		self.open_lots_balance += lots
		if self.prev_lots_balance > 0:
			if self.open_lots_balance  <= 0:
				self.open_orders = {}
				if self.open_lots_balance < 0:
					self.open_orders[len(self.open_orders)] = order
			elif self.open_lots_balance  > 0:
				self.open_orders[len(self.open_orders)] = order
		elif self.prev_lots_balance < 0:
			if self.open_lots_balance  >= 0:
				self.open_orders = {}
				if self.open_lots_balance > 0:
					self.open_orders[len(self.open_orders)] = order
			elif self.open_lots_balance  < 0:
				self.open_orders[len(self.open_orders)] = order
		else:
			self.open_orders[len(self.open_orders)] = order
	
	# def add_pending_order(self, price, lots, type):
		# self.pending_orders[len(self.pending_orders)] = {
			# 'date': None,
			# 'time': None,
			# 'price': price,
			# 'lots': lots,
			# 'status': 'act',
			# 'type': type
		# }
		# if type == 'stop':
			# if lots > 0:
				# self.buy_stop_order_cnt += 1
			# elif lots < 0:
				# self.sell_stop_order_cnt += 1
			# self.stop_order_cnt += 1
		# elif type == 'limit':
			# if lots > 0:
				# self.buy_limit_order_cnt += 1
			# elif lots < 0:
				# self.sell_limit_order_cnt += 1
			# self.limit_order_cnt += 1
		
	# def exec_pending_order(self, _idx):
		# price = self.pending_orders[_idx]['price']
		# lots = self.pending_orders[_idx]['lots']
		# type = self.pending_orders[_idx]['type']
		# self.add_open_order(price, lots)
		# self.pending_orders[_idx]['status'] = 'ex'
		# if type == 'stop':
			# if lots > 0:
				# self.buy_stop_order_cnt -= 1
			# elif lots < 0:
				# self.sell_stop_order_cnt -= 1
			# self.stop_order_cnt -= 1
		# elif type == 'limit':
			# if lots > 0:
				# self.buy_limit_order_cnt -= 1
			# elif lots < 0:
				# self.sell_limit_order_cnt -= 1
			# self.limit_order_cnt -= 1
		
	# def cancel_pending_order(self, _idx):
		# type = self.pending_orders[_idx]['type']
		# self.pending_orders[_idx]['status'] = 'cncl'
		# lots = self.pending_orders[_idx]['lots']
		# if type == 'stop':
			# if lots > 0:
				# self.buy_stop_order_cnt -= 1
			# elif lots < 0:
				# self.sell_stop_order_cnt -= 1
			# self.stop_order_cnt -= 1
		# elif type == 'limit':
			# if lots > 0:
				# self.buy_limit_order_cnt -= 1
			# elif lots < 0:
				# self.sell_limit_order_cnt -= 1
			# self.limit_order_cnt -= 1
