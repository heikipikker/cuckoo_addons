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

import os
import sys
import argparse
import config
import time
from lib import nat
from lib import tor
from lib import inetsim
from lib import service

if platform.uname() != "debian":
    print "This script only runs on Debian (based) linux distributions."
    quit()

parser = argparse.ArgumentParser("Cuckoo Sandbox Addons")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--tor", help="Enable TOR Transparant Proxy", action="store_true", required=False)
group.add_argument("-i", "--inetsim", help="Enable iNetsim", action="store_true", required=False)
group.add_argument("-n", "--nat", help="Enable NAT", action="store_true", required=False)
group.add_argument("-R", "--reset", help="This command is for flushing iptables and disabling IP forwarding, in case something goes wrong", action="store_true", required=False)
args = parser.parse_args()

# you _really_ have to be root, else there is no point in starting the script
# this could be a security issue but in most cases you are using this script on an isolated analysis box.

if os.geteuid() != 0:
    print "sorry, you need to run this as root"
    sys.exit(1)


# Call the Cuckoo Addons magic.
if args.nat:	
	nat.NatOn()
	service.Service()
	nat.NatOff()

if args.tor:
	tor.TorOn()
	service.Service()
	tor.TorOff()
	

if args.inetsim:
	inetsim.InetsimOn()	
	service.Service()
	inetsim.InetsimOff()

if args.reset:
	print "Flushing IP tables.."
	os.system("iptables -t nat -F; iptables -F")
	print "Disabling IP forwarding..."
	os.system("sysctl -w net.ipv4.ip_forward=0")
	print "Trying to gracefully kill all daemons..."
	os.system("pkill tor")
	os.system("pkill named")
	os.system("pkill inetsim")
	time.sleep(5)
	print "Done."
