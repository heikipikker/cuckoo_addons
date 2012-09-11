#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

import sys
import time
import argparse
import os
import config

# you _really_ have to be root, else there is no point in starting the script
# this could be a security issue but in most cases you are using this script on an isolated analysis box.

if os.geteuid() != 0:
    print "sorry, you need to run this as root"
    sys.exit(1)

parser = argparse.ArgumentParser("Cuckoo Sandbox Host preparation")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-si", "--setupinetsim", help="Extract and prepare iNetsim", action="store_true", required=False)
group.add_argument("-st", "--setuptapinterface", help="Setup the TAP interface and make it static in /etc/network/if-up.d for a reboot", action="store_true", required=False)
group.add_argument("-id", "--installdependancies", help="Install TOR all the dependancies", action="store_true", required=False)
args = parser.parse_args()

if args.dependancies:
        print "Installing TOR, uml-utilities and bind9 dns server.."
        os.system("apt-get install tor uml-utilities bind9")
        print "Installing Net::DNS cpanmodule"
        os.system("cpan Net::DNS")
        print "Installed the TOR package, uml-utilities and Perl module Net::DNS..."




if args.setupinetsim:

	# extract inetsim sources, run the inetsim setup script to correct persmissions and add inetsim group.
	os.system("groupadd inetsim")
	os.system("tar xvf src/inetsim-1.2.2.tar.gz -C src/ && cd src/inetsim-1.2.2 && ./setup.sh")


if args.setuptapinterface:

	os.system("tunctl -t %s" % (config.TAP_INTERFACE))
	print "Created TAP interface %s\n" % (config.TAP_INTERFACE)

	# configure ip address tap/tun interface
	os.system("ifconfig %s %s netmask %s" % (config.TAP_INTERFACE,config.TAP_IP,config.TAP_NETMASK))
	print "IP Address %s with netmask %s configured for %s\n" % (config.TAP_IP,config.TAP_NETMASK,config.TAP_INTERFACE)

	# create a route so it _could_ communicate with the outside world
	os.system("route add -net %s netmask %s gw %s %s" % (config.TAP_NETADDR,config.TAP_NETMASK,config.TAP_IP,config.TAP_INTERFACE))
	print "Route added for subnet %s to gateway %s with IP %s\n" % (config.TAP_NETADDR,config.TAP_INTERFACE,config.TAP_IP)



	if os.path.isfile("/etc/network/if-up.d/tap-cuckoo") != True:
        	        f = open("/etc/network/if-up.d/tap-cuckoo", "w")
                	try:
                        	f.write("#!/bin/bash\n")
                        	f.write("tunctl -t %s\n" % (config.TAP_INTERFACE))
                        	f.write("ifconfig %s %s netmask %s\n" % (config.TAP_INTERFACE,config.TAP_IP,config.TAP_NETMASK))
                        	f.write("route add -net %s netmask %s gw %s %s\n" % (config.TAP_NETADDR,config.TAP_NETMASK,config.TAP_IP,config.TAP_INTERFACE))
                	finally:
                        	f.close()
				os.system("chmod +x /etc/network/if-up.d/tap-cuckoo")
                        	print "\n Making configuration static, /etc/network/if-up.d/tap-cuckoo written with the TAP configuration"
 
