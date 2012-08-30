#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.


import time
import sys
import os
import config

def Tor():	
	print "Starting TOR Transparant proxy listning on %s with IP: %s" % (config.TAP_INTERFACE,config.TAP_IP) 
	os.system("tor VirtualAddrNetwork 10.192.0.0/10 AutomapHostsOnResolve 1 TransPort 9040 TransListenAddress %s DNSPort 53 DNSListenAddress %s" % (config.TAP_IP,config.TAP_IP))
	os.system("iptables -t nat -A PREROUTING -i %s -p udp -m udp --dport 53 -j REDIRECT --to-ports 53" % (config.TAP_INTERFACE))
	os.system("iptables -t nat -A PREROUTING -i %s -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 9040" % (config.TAP_INTERFACE))
	time.sleep(5)

	while True:
		try:
			time.sleep(1)

		except KeyboardInterrupt:
			print "Stopping TOR Transparant Proxy..."
			os.system("pkill tor")
			time.sleep(5)
			print "Flushing iptables rules..."
			os.system("iptables -t nat -F; iptables -F")
			print "\nDone."
			sys.exit()
