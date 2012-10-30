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

import time
import sys
import os
import config

def TorOn():	
	print "Starting TOR Transparant proxy listening on %s with IP: %s ...\n" % (config.TAP_INTERFACE,config.TAP_IP) 
	os.system("tor VirtualAddrNetwork 10.192.0.0/10 AutomapHostsOnResolve 1 TransPort 9040 TransListenAddress %s DNSPort 53 DNSListenAddress %s" % (config.TAP_IP,config.TAP_IP))
	time.sleep(1)
	print "Adding iptables rules for TOR Transparant Proxying..."
	os.system("iptables -A FORWARD -i %s -p udp -m udp -j DROP" % (config.TAP_INTERFACE))
	os.system("iptables -A FORWARD -i %s -p tcp -m tcp -j DROP" % (config.TAP_INTERFACE))
	os.system("iptables -t nat -A PREROUTING -i %s -p udp -m udp --dport 53 -j REDIRECT --to-ports 53" % (config.TAP_INTERFACE))
	os.system("iptables -t nat -A PREROUTING -i %s -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 9040" % (config.TAP_INTERFACE))
	time.sleep(1)
	print "Disabled IP forwarding..."
	os.system("sysctl -w net.ipv4.ip_forward=0")
	time.sleep(1)
	print "TOR Transparant Proxy listening, all traffic from %s is being forwarded to the TOR network..." % (config.TAP_INTERFACE)	

def TorOff():
	print "\nStopping TOR Transparant Proxy..."
	os.system("pkill tor")
	time.sleep(1)
	print "\nFlushing iptables rules..."
	os.system("iptables -t nat -F; iptables -F")
	time.sleep(1)
	print "\nDone."
	sys.exit()
