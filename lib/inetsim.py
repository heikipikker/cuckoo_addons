#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.


import sys
import os
import time
import config

def Inetsim():
	print "\n Starting iNetsim"
	os.system("cd src/inetsim-1.2.2 && ./inetsim --bind-address=%s --config=../../lib/inetsim.conf" % (config.TAP_IP))
	
	while True:
		try:
			time.sleep(2000)

		except KeyboardInterrupt:	
			print "Stopping iNetsim"
			os.system("pkill inetsim")
			sys.exit()

