# -*- coding: utf-8 -*

from modules.indicators.Buffer import *
from modules.indicators.SMA import *
from modules.indicators.EquityA import *

class ArbitrageSignals:
	
	def __init__(self, N, sma_per, level):
		self.log = []
		self.N = N
		self.level = level
		self.sma = SMA(sma_per)
		self.Si_eqv = EquityA()
		self.Eu_eqv = EquityA()
		self.ED_eqv = EquityA()
		self.lots = 1
	
	def calc(self, Si_C, Eu_C, ED_C):
		open_long, open_short, close_long, close_short = False, False, False, False
		
		Si_eqv_val = self.Si_eqv.calc_by_lots(Si_C, self.lots)
		Eu_eqv_val = self.Eu_eqv.calc_by_lots(Eu_C, self.lots)
		ED_eqv_val = self.ED_eqv.calc_by_lots(ED_C, self.lots)
		
		gamma = (Eu_eqv_val - Si_eqv_val - ED_eqv_val * Si_C) * self.N - Si_eqv_val
		gamma_avg = self.sma.calc(gamma)
		delta = None
		if gamma_avg != None:
			delta = gamma - gamma_avg
			if delta > self.level:
				open_short = True
			elif delta < -self.level:
				open_long = True
			
			if delta > 0:
				close_long = True
			elif delta < 0:
				close_short = True
			
		self.log = [gamma, gamma_avg, delta]
		self.lots = 0
		return open_long, open_short, close_long, close_short