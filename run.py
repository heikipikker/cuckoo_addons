#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

import os
import sys
import argparse
import config
import time
from lib import nat
from lib import tor
from lib import inetsim
from lib import service


# you _really_ have to be root, else there is no point in starting the script
# this could be a security issue but in most cases you are using this script on an isolated analysis box.

if os.geteuid() != 0:
    print "sorry, you need to run this as root"
    sys.exit(1)

parser = argparse.ArgumentParser("Cuckoo Sandbox Addons")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--tor", help="Enable TOR Transparant Proxy", action="store_true", required=False)
group.add_argument("-i", "--inetsim", help="Enable iNetsim", action="store_true", required=False)
group.add_argument("-n", "--nat", help="Enable NAT", action="store_true", required=False)
group.add_argument("-R", "--reset", help="This command is for flushing iptables and disabling IP forwarding, in case something goes wrong", action="store_true", required=False)
args = parser.parse_args()


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
