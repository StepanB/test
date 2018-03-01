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

			i = 1
			data = p.sub('<a class="sup" href="../Text/' + filename + '#ppc-' + str(i) + '" id="odkaz-' + str(i) + '">'+str(i)+'*</a>', data)
							# <a class="sup" href="../Text/Investor-01-3.xhtml#ppc-1" id="odkaz-1">1*</a>
			m = re.findall(p, data)

			print(m)
			file = open(filename, "w", encoding="utf8")
			file.write(data)
			# file.write(data)
			file.close()
			print()
