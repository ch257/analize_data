# -*- coding: utf-8 -*

import numpy as np
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc 

class Plotter:
	def __init__(self, errors):
		self.errors = errors
		self.ax = []
		self.subplot_offset = 0
		
		