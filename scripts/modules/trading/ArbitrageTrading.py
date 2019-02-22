# -*- coding: utf-8 -*

from modules.indicators.Buffer import *

class ArbitrageTrading:
	
	def __init__(self, order_exec):
		self.order_exec = order_exec
		self.order_holder = order_exec.order_holder
		self.allow_once = True
		self.log = []
		self.cnt = 1
			
	def orders_state(self):
		BuyState, SellState, HasStopLoss, HasTakeProfit = False, False, False, False
		if self.order_holder.open_lots_balance > 0:
			BuyState = True
		elif self.order_holder.open_lots_balance < 0:
			SellState = True
			
		return BuyState, SellState, HasStopLoss, HasTakeProfit
		
	def trade(self, open_long, open_short, close_long, close_short, market_price):
		BuyState, SellState, HasStopLoss, HasTakeProfit = self.orders_state()
		
		if self.cnt == 40:
			self.order_exec.BuyMarket(1)
		# if self.cnt == 50:
			# self.order_exec.SellMarket(1)
			
		# if self.cnt == 60:
			# self.order_exec.SellMarket(1)
		# if self.cnt == 70:
			# self.order_exec.BuyMarket(1)
		
		# if close_long:
			# if self.order_holder.open_lots_balance > 0:
				# pass
			# if self.order_holder.buy_limit_lots_balance > 0:
				# self.order_exec.CancelBuyLimits()
		# if close_short:
			# if self.order_holder.open_lots_balance < 0:
				# pass
			# if self.order_holder.sell_limit_lots_balance > 0:
				# self.order_exec.CancelSellLimits()

		# if (self.order_exec.order_holder.open_lots_balance > 0
			# and self.order_exec.order_holder.sell_limit_order_cnt == 0):
			# pass
		# if (self.order_exec.order_holder.open_lots_balance < 0
			# and self.order_exec.order_holder.buy_limit_order_cnt == 0):
			# pass
		
		# if (self.order_holder.open_lots_balance == 0
			# and self.order_holder.buy_limit_lots_balance == 0
			# and self.order_holder.sell_limit_lots_balance == 0):	
			# if open_long:
				# self.order_exec.BuyLimit(1, market_price - 10)
				# self.order_exec.SellStop(1, market_price - 40)
			# if open_short:
				# self.order_exec.SellLimit(1, market_price + 10)
				# self.order_exec.BuyStop(1, market_price + 40)
		
		self.log = []
		self.cnt += 1
		
