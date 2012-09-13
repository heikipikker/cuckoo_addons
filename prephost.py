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
import time
import argparse
import os
import config

# you _really_ have to be root, else there is no point in starting the script
# this could be a security issue but in most cases you are using this script on an isolated analysis box.

parser = argparse.ArgumentParser("Cuckoo Sandbox Host preparation")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-si", "--setupinetsim", help="Extract and prepare iNetsim", action="store_true", required=False)
group.add_argument("-st", "--setuptapinterface", help="Setup the TAP interface and make it static in /etc/network/if-up.d for a reboot", action="store_true", required=False)
group.add_argument("-id", "--installdependencies", help="Install TOR all the dependencies", action="store_true", required=False)
args = parser.parse_args()

if os.geteuid() != 0:
    print "sorry, you need to run this as root"
    sys.exit(1)


if args.installdependencies:
        print "Installing TOR, uml-utilities, Perl dependencies and bind9 DNS server.."
        os.system("apt-get install tor uml-utilities bind9 perl perl-base perl-modules libnet-server-perl libnet-dns-perl libipc-shareable-perl libdigest-sha1-perl libio-socket-ssl-perl libiptables-ipv4-ipqueue-perl")

	print "Disabling BIND9 to automatically start at boot.."
	os.system("update-rc.d bind9 disable")

	print "Disabling TOR to automatically start at boot.."
	os.system("update-rc.d tor disable")

#        print "Installing Net::DNS cpan module"
#        os.system("cpan -i Net::DNS")
#        os.system("cpan -i Digest::SHA1")

	print "\n\nDone."
	print "If you encounter problems running iNetsim please statisfy the Perl dependencies manually through CPAN.."
	

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
 
