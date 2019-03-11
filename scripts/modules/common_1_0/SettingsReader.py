# -*- coding: utf-8 -*

from modules.common_1_0.IniParser import *

class SettingsReader:
	def __init__(self, errors):
		self._errors = errors
		self._ini_encoding = 'utf-8'
		self._default_settings_file_path = 'settings/default.ini'
		self._settings = {}
		
	def read_settings(self, args):
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
		self._settings['output_file'] = {}
		
		self._settings['input_file']['path'] = user_ini_parser.get_param('input_file', 'path')
		input_file_format_section = user_ini_parser.get_param('input_file', 'format')
		self._settings['input_file']['format'] = {
			'list_separator': user_ini_parser.get_param(input_file_format_section, 'list_separator', 'escape')
		}
		
		# input_file_path = self.ini_parser.get_param('input', 'file_path')
		# input_file_format = {}
		# input_file_format_section = self.ini_parser.get_param('input', 'file_format')
		# input_file_format['list_separator'] = self.ini_parser.get_param(input_file_format_section, 'list_separator', 'escape')
		# input_file_format['decimal_symbol'] = self.ini_parser.get_param(input_file_format_section, 'decimal_symbol', 'escape')
		# input_file_format['encoding'] = self.ini_parser.get_param(input_file_format_section, 'encoding')
		
		# input_file_column_types_section = self.ini_parser.get_param(input_file_format_section, 'file_column_types')
		# input_file_column_formats_section = self.ini_parser.get_param(input_file_format_section, 'file_column_formats')
		# input_file_format['file_column_types'] = self.ini_parser.get_param(input_file_column_types_section)
		# input_file_format['file_column_formats'] = self.ini_parser.get_param(input_file_column_formats_section)
		
		# output_file_path = self.ini_parser.get_param('output', 'file_path')
		# output_file_format = {}
		# output_file_format_section = self.ini_parser.get_param('output', 'file_format')
		# output_file_format['list_separator'] = self.ini_parser.get_param(output_file_format_section, 'list_separator', 'escape')
		# output_file_format['decimal_symbol'] = self.ini_parser.get_param(output_file_format_section, 'decimal_symbol', 'escape')
		# output_file_format['encoding'] = self.ini_parser.get_param(output_file_format_section, 'encoding')
		
		# output_file_column_types_section = self.ini_parser.get_param(output_file_format_section, 'file_column_types')
		# output_file_column_formats_section = self.ini_parser.get_param(output_file_format_section, 'file_column_formats')
		# output_file_format['file_column_types'] = self.ini_parser.get_param(output_file_column_types_section)
		# output_file_format['file_column_formats'] = self.ini_parser.get_param(output_file_column_formats_section)
		
		return self._settings
