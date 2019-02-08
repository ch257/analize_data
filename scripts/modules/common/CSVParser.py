# -*- coding: utf-8 -*

from modules.common.Files import *
from modules.common.Tools import *

class CSVParser:
	def __init__(self, errors):
		self.errors = errors
		self.settings = {}
		self.tools = Tools(self.errors)
	

