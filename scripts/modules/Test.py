# -*- coding: utf-8 -*

from modules.common.Errors import *
from modules.common.IniParser import *
from modules.common.Tools import *
from modules.common.CSVParser import *
from modules.common.TableIterator import *
#######################
from modules.indicators.SMA import *
from modules.indicators.EquityA import *
from modules.trading.OrdersHolder import *
from modules.trading.OrdersExec import *
from modules.signals.ArbitrageSignals import *
from modules.trading.ArbitrageTrading import *


class Test:
	def __init__(self):
		self.errors = Errors()
		self.ini_encoding = 'utf-8'
		self.ini_parser = IniParser(self.errors)
		
		# self.settings = {}
	
	def read_settings(self, args):
		if len(args) < 2:
			self.errors.raise_error('no ini file path')
		else:
			encoding = self.ini_encoding
			if len(args) > 2:
				encoding = args[2]
				
			ini_file_path = args[1]
			self.ini_parser.read_ini(args[1], encoding)
	
	def main(self, args):
		self.read_settings(args)
		
		input_file_path = self.ini_parser.get_param('input', 'file_path')
		input_file_format = {}
		input_file_format_section = self.ini_parser.get_param('input', 'file_format')
		input_file_format['list_separator'] = self.ini_parser.get_param(input_file_format_section, 'list_separator', 'escape')
		input_file_format['decimal_symbol'] = self.ini_parser.get_param(input_file_format_section, 'decimal_symbol', 'escape')
		input_file_format['encoding'] = self.ini_parser.get_param(input_file_format_section, 'encoding')
		
		input_file_column_types_section = self.ini_parser.get_param(input_file_format_section, 'file_column_types')
		input_file_column_formats_section = self.ini_parser.get_param(input_file_format_section, 'file_column_formats')
		input_file_format['file_column_types'] = self.ini_parser.get_param(input_file_column_types_section)
		input_file_format['file_column_formats'] = self.ini_parser.get_param(input_file_column_formats_section)
		
		output_file_path = self.ini_parser.get_param('output', 'file_path')
		output_file_format = {}
		output_file_format_section = self.ini_parser.get_param('output', 'file_format')
		output_file_format['list_separator'] = self.ini_parser.get_param(output_file_format_section, 'list_separator', 'escape')
		output_file_format['decimal_symbol'] = self.ini_parser.get_param(output_file_format_section, 'decimal_symbol', 'escape')
		output_file_format['encoding'] = self.ini_parser.get_param(output_file_format_section, 'encoding')
		
		output_file_column_types_section = self.ini_parser.get_param(output_file_format_section, 'file_column_types')
		output_file_column_formats_section = self.ini_parser.get_param(output_file_format_section, 'file_column_formats')
		output_file_format['file_column_types'] = self.ini_parser.get_param(output_file_column_types_section)
		output_file_format['file_column_formats'] = self.ini_parser.get_param(output_file_column_formats_section)
		
		csv_parser = CSVParser(self.errors)
		table, columns = csv_parser.csv2table(input_file_path, input_file_format)
		
		tools = Tools(self.errors)
		adv_columns = ['<GAMMA>', '<GAMMA_AVG>', '<DELTA>']
		tools.add_columns(adv_columns, table, columns)
		
		order_holder = OrdersHolder()
		order_exec = OrdersExec(order_holder)
		
		N = 7
		sma_per = 21
		level = 100
		arb_sig = ArbitrageSignals(N, sma_per, level)
		arb_trd = ArbitrageTrading(order_exec)
		
		itr = TableIterator(self.errors, table, columns)
		while not itr.EOD:
			rec, rec_cnt = itr.get_next_rec()
			Si_C = rec.get('<Si_CLOSE>')
			Eu_C = rec.get('<Eu_CLOSE>')
			ED_C = rec.get('<ED_CLOSE>')
			
			order_exec.exec(Eu_C, Eu_C, Eu_C)
			open_long, open_short, close_long, close_short = arb_sig.calc(Si_C, Eu_C, ED_C)
			arb_trd.trade(open_long, open_short, close_long, close_short)
			
			tools.update_cells(adv_columns, arb_sig.log, rec_cnt, table)
		
		csv_parser.table2csv(table, columns, output_file_path, output_file_format)
		
		if self.errors.error_occured:
			self.errors.print_errors()
		else:
			print('OK\n')