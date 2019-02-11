# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class EquityA:
	
	def __init__(self):
		self.buffer = Buffer(1)
		self.eqv = 0
		
	def calc(self, new_item):
		if self.buffer.is_ready:
			self.eqv += new_item - self.buffer.buff[0] 
		
		self.buffer.slide(new_item)
		
		return self.eqv

