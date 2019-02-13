# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class OrdersHolder:
	
	def __init__(self):
		self.log = []
		self.pending_orders = {}
		self.open_orders = {}
		self.open_lots = {}
		
	
		
