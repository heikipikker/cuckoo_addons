#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.


import sys
import os
import time
import config

def InetsimOn():
	print "\n Starting iNetsim..."
	os.system("iptables -t nat -A PREROUTING -i %s -j DNAT --to-destination %s" % (config.TAP_INTERFACE,config.TAP_IP))
	print "Enable IP forwarding..."
	os.system("sysctl -w net.ipv4.ip_forward=1")
	os.system("cd src/inetsim-1.2.2 && ./inetsim --bind-address=%s --config=../../lib/inetsim.conf" % (config.TAP_IP))

def InetsimOff():	
	print "\nStopping iNetsim..."
	os.system("pkill inetsim")
	print "\nFlushing iptables rules..."
	os.system("iptables -F; iptables -t nat -F")
	print "Disabled IP forwarding..."
	os.system("sysctl -w net.ipv4.ip_forward=0")
	print "\nDone."
	sys.exit()

