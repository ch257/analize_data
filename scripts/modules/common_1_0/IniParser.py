# -*- coding: utf-8 -*

from modules.common.Files import *
from modules.common.Tools import *

class IniParser:
	def __init__(self, errors):
		self._errors = errors
		self._tools = Tools(self._errors)
		self._ini_file_path = ''
		self.settings = {}
		
	
	def _exlude_non_data(self, line):
		line = line.rstrip('\n')
		line = line.rstrip('\r')
		start_comment_pos = line.find(';')
		if start_comment_pos > -1:
			line = line[0:start_comment_pos]
		line = line.replace('\t', '')
		line = line.replace(' ', '')
		return line
		
	def _parse_line(self, line):
		section = None
		param = None
		value = None
		if line[0:1] == '[' and line[-1:] == ']':
			section = line[1:-1]
		else:
			eq_smb = line.find('=')
			param = line[0:eq_smb]
			value = line[eq_smb + 1:]
		return section, param, value
		
	def read_ini(self, ini_file_path, encoding):
		if self._errors.error_occured:
			return None
		
		ini_file = Files(self._errors)
		ini_file.open_file(ini_file_path, 'r', encoding)
		last_section = None
		while not self._errors.error_occured:
			line = ini_file.read_line()
			if line:
				line = self._exlude_non_data(line)
				section, param, value = self._parse_line(line)
				if section:
					self.settings[section] = {}
					last_section = section
				if last_section  and param:
					self.settings[last_section][param] = value
				
			else:
				break
		ini_file.close_file()
		self._ini_file_path = ini_file_path
		return self.settings
	
	def get_param(self, section, param=None, param_type='str', error_ignoring=False, default_param_value=None):
		if self._errors.error_occured:
			if param:
				return ''
			else:
				return {}
		
		if self.settings.get(section):
			if param:
				if self.settings[section].get(param):
					return self._tools.str2type(self.settings[section][param], param_type)
				else:
					if not error_ignoring:
						self._errors.raise_error('No parameter [' + section + '][' + param + '] in ini file ' + self._ini_file_path)
						return ''
					else:
						return self._tools.str2type(default_param_value, param_type)
					
			else:
				return self.settings[section]
		else:
			if not error_ignoring:
				self._errors.raise_error('No section [' + section + '] in ini file ' + self._ini_file_path)
				return {}
