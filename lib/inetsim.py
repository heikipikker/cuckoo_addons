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

def InetsimOn():
	print "\n Starting iNetsim..."
	os.system("iptables -t nat -A PREROUTING -i %s -j DNAT --to-destination %s" % (config.TAP_INTERFACE,config.TAP_IP))
#	print "Enable IP forwarding..."
#	os.system("sysctl -w net.ipv4.ip_forward=1")
	os.system("cd src/inetsim-1.2.2 && ./inetsim --bind-address=%s --config=../../lib/inetsim.conf" % (config.TAP_IP))

def InetsimOff():	
	print "\nStopping iNetsim..."
	os.system("pkill inetsim")	
	time.sleep(1)
	print "\nFlushing iptables rules..."
	os.system("iptables -F; iptables -t nat -F")
	time.sleep(1)
#	print "Disabled IP forwarding..."
#	os.system("sysctl -w net.ipv4.ip_forward=0")
	print "\nDone."
	sys.exit()

