#!/usr/bin/python

import sys
import time
import argparse
import subprocess

parser = argparse.ArgumentParser("Cuckoo Sandbox Additions")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--tor", help="Enable TOR Transparant Proxy", action="store_true", required=False)
group.add_argument("-i", "--inetsim", help="Enable iNetsim", action="store_true", required=False)
group.add_argument("-n", "--nat", help="Enable NAT", action="store_true", required=False)
args = parser.parse_args()

if args.tor:	
	print "Enable TOR"
	subprocess.call(["echo", "start TOR"])

# Rare loop om er voor te zorgen dat proces blijft draaien, kan waarschijnlijk netter.
# Zodra deze gestopt wordt zal alles weer normaal worden.

while True:
	try:
		time.sleep(1)

	except KeyboardInterrupt:
		print "\nBack to defaults"
		subprocess.call(["echo", "STOP ALLE SERVICES"])
		sys.exit()
