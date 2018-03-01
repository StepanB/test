#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os

for filename in os.listdir(os.getcwd()):
	if filename.endswith(".xhtml"):
		print(filename)

		with open(filename, "r", encoding="utf8") as file:
			
			data = file.read()

			print(data)
			p = re.compile(r'<span class="sup">[\*\+\±]</span>')

			i = 0
			
			for m in re.finditer(p, data):
				
				i = i+1

				helper = p.sub('<a class="sup" href="../Text/' + filename + '#ppc-' + str(i) + '" id="odkaz-' + str(i) + '">'+str(i)+'*</a>', m.group(0))
		
	
				m.group(0) = helper
				print(m)

			file = open(filename, "w", encoding="utf8")
			file.write(data)
			# file.write(data)
			file.close()
			print()
