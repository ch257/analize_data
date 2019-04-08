# -*- coding: utf-8 -*

from modules.common_2_0.IniParser import *

class SettingsReader:
	def __init__(self, errors):
		self._errors = errors
		self._ini_encoding = 'utf-8'
		self._default_settings_file_path = 'settings/default/default.ini'
		self._settings = {}
		
	def read(self, args):
		if self._errors.error_occured:
			return None
		
		if len(args) > 1:
			encoding = self._ini_encoding
			user_ini_file_path = self._default_settings_file_path
			
			if len(args) == 2:
				user_ini_file_path = args[1]
			else:
				user_ini_file_path = args[1]
				encoding = args[2]
				
			user_ini_parser = IniParser(self._errors)
			user_settings = user_ini_parser.read_ini(user_ini_file_path, encoding)
			default_ini_parser = IniParser(self._errors)
			default_settings = default_ini_parser.read_ini(self._default_settings_file_path, self._ini_encoding)
			for section in default_settings:
				if not user_settings.get(section):	
					user_settings[section] = {}
				
				for param in default_settings[section]:
					if not user_settings[section].get(param):
						user_settings[section][param] = default_settings[section][param]
		else:
			default_ini_parser = IniParser(self._errors)
			user_settings = default_ini_parser.read_ini(self._default_settings_file_path, self._ini_encoding)
			
		self._settings['input_file'] = {}
		self._settings['input_file']['path'] = user_ini_parser.get_param('input_file', 'path')
		input_file_format_section = user_ini_parser.get_param('input_file', 'format')
		input_file_column_types_section = user_ini_parser.get_param(input_file_format_section, 'column_types')
		input_file_column_formats_section = user_ini_parser.get_param(input_file_format_section, 'column_formats')
		self._settings['input_file']['format'] = {
			'list_separator': user_ini_parser.get_param(input_file_format_section, 'list_separator', 'escape'),
			'decimal_symbol': user_ini_parser.get_param(input_file_format_section, 'decimal_symbol', 'escape'),
			'encoding': user_ini_parser.get_param(input_file_format_section, 'encoding'),
			'column_types': user_ini_parser.get_param(input_file_column_types_section),
			'column_formats': user_ini_parser.get_param(input_file_column_formats_section)
		}
		self._settings['input_folder'] = {}
		self._settings['input_folder']['path'] = user_ini_parser.get_param('input_folder', 'path')

		self._settings['output_file'] = {}
		self._settings['output_file']['path'] = user_ini_parser.get_param('output_file', 'path')
		output_file_format_section = user_ini_parser.get_param('output_file', 'format')
		output_file_column_types_section = user_ini_parser.get_param(output_file_format_section, 'column_types')
		output_file_column_formats_section = user_ini_parser.get_param(output_file_format_section, 'column_formats')
		self._settings['output_file']['format'] = {
			'list_separator': user_ini_parser.get_param(output_file_format_section, 'list_separator', 'escape'),
			'decimal_symbol': user_ini_parser.get_param(output_file_format_section, 'decimal_symbol', 'escape'),
			'encoding': user_ini_parser.get_param(output_file_format_section, 'encoding'),
			'column_types': user_ini_parser.get_param(output_file_column_types_section),
			'column_formats': user_ini_parser.get_param(output_file_column_formats_section)
		}
		self._settings['output_folder'] = {}
		self._settings['output_folder']['path'] = user_ini_parser.get_param('output_folder', 'path')
		
		self._settings['plotter'] = {}
		output_section = user_ini_parser.get_param('plotter', 'output')
		subplot_height_section = user_ini_parser.get_param('plotter', 'subplot_height')
		curve_subplot_section = user_ini_parser.get_param('plotter', 'curve_subplot')
		curve_type_section = user_ini_parser.get_param('plotter', 'curve_type')
		curve_width_section = user_ini_parser.get_param('plotter', 'curve_width')
		curve_color_section = user_ini_parser.get_param('plotter', 'curve_color')
		curve_alpha_section = user_ini_parser.get_param('plotter', 'curve_alpha')
		self._settings['plotter'] = {
			'output': user_ini_parser.get_param(output_section),
			'subplot_height': user_ini_parser.get_param(subplot_height_section),
			'curve_subplot': user_ini_parser.get_param(curve_subplot_section),
			'curve_type': user_ini_parser.get_param(curve_type_section),
			'curve_width': user_ini_parser.get_param(curve_width_section),
			'curve_color': user_ini_parser.get_param(curve_color_section),
			'curve_alpha': user_ini_parser.get_param(curve_alpha_section)
		}
		
		self._settings['usd_rate'] = {}
		self._settings['usd_rate'] = user_ini_parser.get_param('usd_rate')
		
		self._settings['contracts'] = {}
		self._settings['contracts']['tickers'] = user_ini_parser.get_param('contracts', 'tickers', 'str_array')
		self._settings['contracts']['header'] = user_ini_parser.get_param('contracts', 'header')
		
		return self._settings
