#!/usr/bin/python

# This package gives additional functionality to Cuckoo with
# the intergration of TOR Transparant Proxy, 
# iNetsim and NAT during analysis.
#
# Copyright (C) 2012  Serge van Namen <serge@se-cured.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
	print "Enabled IP forwarding..."
	os.system("sysctl -w net.ipv4.ip_forward=1")
	time.sleep(1)
	print "\nDone, NAT running from %s to the internet." % (config.INTERNET_INTERFACE)


def NatOff():

	print "\nStopping BIND DNS server..."
	os.system("pkill named")
	time.sleep(1)
	print "\nFlushing iptables..."
	os.system("iptables -F; iptables -t nat -F")
	time.sleep(1)
	print "Disabled IP forwarding..."
	os.system("sysctl -w net.ipv4.ip_forward=0")
	time.sleep(1)
	print "\nDone."
