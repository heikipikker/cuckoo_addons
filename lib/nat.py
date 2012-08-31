#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

import sys
import os
import time
import config

def NatOn():

	print "Starting BIND DNS server..."
	os.system("named")
	time.sleep(1)
	print "\nAdding iptables rules for NAT..."
	os.system("iptables -A FORWARD -i %s -o %s -m state --state RELATED,ESTABLISHED -j ACCEPT" % (config.INTERNET_INTERFACE,config.TAP_INTERFACE))
	os.system("iptables -A FORWARD -i %s -o %s -j ACCEPT" % (config.TAP_INTERFACE,config.INTERNET_INTERFACE))
	os.system("iptables -t nat -A POSTROUTING -o %s -j MASQUERADE" % (config.INTERNET_INTERFACE))	
	time.sleep(1)
	print "\nDone, NAT running from %s to the internet." % (config.INTERNET_INTERFACE)


def NatOff():

	print "\nStopping BIND DNS server..."
	os.system("pkill named")
	print "\nFlushing iptables..."
	os.system("iptables -F; iptables -t nat -F")
	time.sleep(1)
	print "\nDone."
