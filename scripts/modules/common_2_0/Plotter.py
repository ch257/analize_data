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
			
		curve_subplot = settings['curve_subplot']
		output = settings['output']
		subplot_height = settings['subplot_height']
		curve_subplot = settings['curve_subplot']
		curve_type = settings['curve_type']
		curve_width = settings['curve_width']
		curve_color = settings['curve_color']
		curve_alpha = settings['curve_alpha']
		
		# print(subplot_height)
		
		subplot_index = []
		curves = []
		subplot_heights = []
		for col in columns:
			if curve_subplot.get(col) != None:
				subp_i = int(curve_subplot[col])
				if subplot_height.get(curve_subplot[col]) != None:
					subp_h = int(subplot_height[curve_subplot[col]])
				else:
					subp_h = int(subplot_height['default'])
				inserted = False
				for i in range(len(subplot_index)):
					if subplot_index[i] > subp_i:
						m_subp_i = subplot_index[i]
						subplot_index[i] = subp_i
						subp_i = m_subp_i
					
						m_subp_h = subplot_height[i]
						subplot_height[i] = subp_h
						subp_h = m_subp_h
					
					elif subplot_index[i] == subp_i:
						inserted = True
						break
				
				if not inserted:
					subplot_index.append(subp_i)
					subplot_heights.append(subp_h)
					
				curves.append(col)
				
		# subplot_index.sort()
		print(subplot_index)
		print(subplot_heights)
		
		
		
		