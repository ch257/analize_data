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
			
		for section in settings:
			print(section)
			
		curve_subplot = settings['curve_subplot']
		output = settings['output']
		subplot_height = settings['subplot_height']
		curve_subplot = settings['curve_subplot']
		curve_type = settings['curve_type']
		curve_width = settings['curve_width']
		curve_color = settings['curve_color']
		curve_alpha = settings['curve_alpha']
		
		subplot_index = []
		for col in columns:
			if curve_subplot.get(col) != None:
				if not curve_subplot[col] in subplot_index:
					subplot_index.append(curve_subplot[col])
				
		subplot_index.sort()
		print(subplot_index)