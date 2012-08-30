#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.


import sys
import os
import time

def Nat():
	os.system("named")
	os.system("iptables -A FORWARD -i eth0 -o tap0 -m state --state RELATED,ESTABLISHED -j ACCEPT")
	os.system("iptables -A FORWARD -i tap0 -o eth0 -j ACCEPT")
	os.system("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")	
	print "NAT Enabled, adding firewall rules and BIND DNS server started"


	while True:
		try:
			time.sleep(1)
	
		except KeyboardInterrupt:
			# clear all iptables rules
	        	os.system("iptables -D FORWARD -i eth0 -o tap0 -m state --state RELATED,ESTABLISHED -j ACCEPT")
        		os.system("iptables -D FORWARD -i tap0 -o eth0 -j ACCEPT")
        		os.system("iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE")	
			os.system("pkill named")
			print "\nNAT Disabled, clearing firewall rules and BIND DNS server killed"	
			sys.exit()
