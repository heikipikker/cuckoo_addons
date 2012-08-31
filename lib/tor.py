#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.


import time
import sys
import os
import config

def Tor():	
	print "Starting TOR Transparant proxy listening on %s with IP: %s ...\n" % (config.TAP_INTERFACE,config.TAP_IP) 
	os.system("tor VirtualAddrNetwork 10.192.0.0/10 AutomapHostsOnResolve 1 TransPort 9040 TransListenAddress %s DNSPort 53 DNSListenAddress %s" % (config.TAP_IP,config.TAP_IP))
	print "Adding iptables rules for TOR Transparant Proxying..."
	os.system("iptables -t nat -A PREROUTING -i %s -p udp -m udp --dport 53 -j REDIRECT --to-ports 53" % (config.TAP_INTERFACE))
	os.system("iptables -t nat -A PREROUTING -i %s -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 9040" % (config.TAP_INTERFACE))
	print "TOR Transparant Proxy listening, all traffic from %s is being forwarded to the TOR network..." % (config.TAP_INTERFACE)

	while True:
		try:
			time.sleep(50000)

		except KeyboardInterrupt: 
			print "\nStopping TOR Transparant Proxy..."
			os.system("pkill tor")
			time.sleep(5)
			print "\nFlushing iptables rules..."
			time.sleep(5)
			os.system("iptables -t nat -F; iptables -F")
			print "\nDone."
			sys.exit()
