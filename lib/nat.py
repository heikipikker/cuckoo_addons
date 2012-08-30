#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.


import sys
import os
import time
import config

def Nat():
	print "Starting BIND DNS server..."
	os.system("named")
	time.sleep(1)
	print "\nAdding iptables rules for NAT..."
	time.sleep(1)
	os.system("iptables -A FORWARD -i %s -o %s -m state --state RELATED,ESTABLISHED -j ACCEPT" % (config.INTERNET_INTERFACE,config.TAP_INTERFACE))
	os.system("iptables -A FORWARD -i %s -o %s -j ACCEPT" % (config.TAP_INTERFACE,config.INTERNET_INTERFACE))
	os.system("iptables -t nat -A POSTROUTING -o %s -j MASQUERADE" % (config.INTERNET_INTERFACE))	
	print "\nDone, NAT running for %s to the internet." % (config.INTERNET_INTERFACE)

	while True:
		try:
			time.sleep(1)
			
		except KeyboardInterrupt:
			print "\nStopping BIND DNS server..."
			os.system("pkill named")
			time.sleep(1)
			print "\nFlushing iptables rules..."
			time.sleep(1)
			os.system("iptables -t nat -F; iptables -F")
			print "\nDone."
			sys.exit()
