# -*- coding: utf-8 -*


from modules.common.Files import *
from modules.common.Errors import *
from modules.common.Tools import *

e = Errors()
f = Files(e)
t = Tools(e)

cols = []

f.open_file('data/test/test_file.txt')
while True:
	line = f.read_line()
	if line:
		cols = t.explode(line)	
	break
		
while not e.error_occured:
	line = f.read_line()
	if line:
		print(line)
		rec = t.line2rec(line, cols)
		print(rec)
		line = t.rec2line(rec, cols)
		print(line)
		
		
	else:
		break
	
f.close_file() 

if e.error_occured:
	e.print_errors()