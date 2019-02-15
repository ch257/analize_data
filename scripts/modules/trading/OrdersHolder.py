# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class OrdersHolder:
	
	def __init__(self):
		self.log = []
		self.pending_orders = {}
		self.open_orders = {}
		self.open_lots = {}
		
		self.open_order_cnt = 0
		self.pending_order_cnt = 0
		
		self.open_lots_balance = 0
		
	def add_open_order(self, price, lots):
		self.open_orders[self.open_order_cnt] = {
			'date': None,
			'time': None,
			'price': price,
			'lots': lots
		}
		
		self.open_order_cnt += 1
		self.open_lots_balance += lots
	
	def add_pending_order(self, price, lots):
		self.pending_orders[self.pending_order_cnt] = {
			'date': None,
			'time': None,
			'price': price,
			'lots': lots,
			'status': 'reg'
		}
		
		self.pending_order_cnt += 1
		
	def exec_pending_order(self, _idx):
		price = self.pending_orders[_idx]['price']
		lots = self.pending_orders[_idx]['lots']
		self.add_open_order(price, lots)
		self.pending_orders[_idx]['status'] = 'ex'
