#!/usr/bin/python

#derp
# Install argparse module trough PIP or install manually

import argparse
from lib import nat
from lib import tor
#from lib import inetsim

#subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward")
#subprocess.call("route add blaat")


parser = argparse.ArgumentParser("Cuckoo Sandbox Additions")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--tor", help="Enable TOR Transparant Proxy", action="store_true", required=False)
group.add_argument("-i", "--inetsim", help="Enable iNetsim", action="store_true", required=False)
group.add_argument("-n", "--nat", help="Enable NAT", action="store_true", required=False)
args = parser.parse_args()

if args.nat:	
	nat.Nat()

if args.tor:
	tor.Tor()


# Rare loop om er voor te zorgen dat proces blijft draaien, kan waarschijnlijk netter.
# Zodra deze gestopt wordt zal alles weer normaal worden.

#while True:
#	try:
#		time.sleep(1)
#
#	except KeyboardInterrupt:
#		print "\nBack to defaults"
#		subprocess.call(["echo", "STOP ALLE SERVICES"])
#		sys.exit()
