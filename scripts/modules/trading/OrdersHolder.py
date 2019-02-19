# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class OrdersHolder:
	
	def __init__(self):
		self.log = []
		self.open_orders = {}
		self.open_orders_log = {}
		self.pending_orders = {}
		
		self.open_lots_balance = 0
		
		self.buy_stop_lots_balance = 0
		self.sell_stop_lots_balance = 0
		
		self.buy_limit_lots_balance = 0
		self.sell_limit_lots_balance = 0

		
	def add_open_order(self, price, lots):
		order = {
			# 'date': None,
			# 'time': None,
			'price': price,
			'lots': lots
		}
		self.open_orders_log[len(self.open_orders_log)] = order
		
		if self.open_lots_balance > 0:
			if order['lots'] < 0:
				remain_lots = order['lots']
				
				_idx = 0
				while _idx < len(self.open_orders) and remain_lots <= 0:
					open_order = self.open_orders[_idx]
					remain_lots += open_order['lots']
					_idx += 1
				found_idx = _idx - 1
				
				if remain_lots > 0:
					self.open_orders[found_idx]['lots'] = remain_lots
					for _idx in range(len(self.open_orders)):
						if found_idx < len(self.open_orders):
							self.open_orders[_idx] = self.open_orders[found_idx]
						else:	
							self.open_orders.pop(_idx)
						found_idx += 1
				
				elif remain_lots < 0:
					order['lots'] = remain_lots
					self.open_orders = {}
					self.open_orders[0] = order
				
				else:
					self.open_orders = {}
			
			elif order['lots'] > 0:
				self.open_orders[len(self.open_orders)] = order
		
		elif self.open_lots_balance < 0:
			if order['lots'] > 0:
				remain_lots = order['lots']
				
				_idx = 0
				while _idx < len(self.open_orders) and remain_lots >= 0:
					open_order = self.open_orders[_idx]
					remain_lots += open_order['lots']
					_idx += 1
				
				if remain_lots < 0:
					self.open_orders[_idx - 1]['lots'] = remain_lots
					for _i in range(len(self.open_orders)):
						if _idx - 1 < len(self.open_orders):
							self.open_orders[_i] = self.open_orders[_idx - 1]
						else:	
							self.open_orders.pop(_i)
						_idx += 1
				
				elif remain_lots > 0:
					order['lots'] = remain_lots
					self.open_orders = {}
					self.open_orders[0] = order
				
				else:
					self.open_orders = {}
			
			elif order['lots'] < 0:
				self.open_orders[len(self.open_orders)] = order
				
		else:
			self.open_orders[0] = order
				
		self.prev_lots_balance = self.open_lots_balance
		self.open_lots_balance += lots
	
	def add_pending_order(self, price, lots, type):
		self.pending_orders[len(self.pending_orders)] = {
			# 'date': None,
			# 'time': None,
			'price': price,
			'lots': lots,
			'type': type,
			'status': 'act'
		}
		if type == 'stop':
			if lots > 0:
				self.buy_stop_lots_balance += lots
			elif lots < 0:
				self.sell_stop_lots_balance += lots
		elif type == 'limit':
			if lots > 0:
				self.buy_limit_lots_balance += lots
			elif lots < 0:
				self.sell_limit_lots_balance += lots
		
	def exec_pending_order(self, _idx):
		price = self.pending_orders[_idx]['price']
		lots = self.pending_orders[_idx]['lots']
		type = self.pending_orders[_idx]['type']
		self.add_open_order(price, lots)
		self.pending_orders[_idx]['status'] = 'ex'
		if type == 'stop':
			if lots > 0:
				self.buy_stop_lots_balance -= lots
			elif lots < 0:
				self.sell_stop_lots_balance -= lots
		elif type == 'limit':
			if lots > 0:
				self.buy_limit_lots_balance -= lots
			elif lots < 0:
				self.sell_limit_lots_balance -= lots
		
	def cancel_pending_order(self, _idx):
		type = self.pending_orders[_idx]['type']
		self.pending_orders[_idx]['status'] = 'cncl'
		lots = self.pending_orders[_idx]['lots']
		if type == 'stop':
			if lots > 0:
				self.buy_stop_lots_balance -= lots
			elif lots < 0:
				self.sell_stop_lots_balance -= lots
		elif type == 'limit':
			if lots > 0:
				self.buy_limit_lots_balance -= lots
			elif lots < 0:
				self.sell_limit_lots_balance -= lots
