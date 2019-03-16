# -*- coding: utf-8 -*

import numpy as np
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc 

class Plotter:
	def __init__(self, errors):
		self.errors = errors
		self.ax = []
		self.subplot_offset = 0
		
	def plot_series(self, table, columns, settings, fig_name):
		if self.errors.error_occured:
			return None
			
		print(settings)
		