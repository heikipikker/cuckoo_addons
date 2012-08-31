#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

import sys
import time
import argparse
import os
import config


# Enable ip forwarding
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
print "IP Forwarding Enabled\n"

# setup the tap/tun interface
os.system("tunctl -t %s" % (config.TAP_INTERFACE))
print "Created TAP interface %s\n" % (config.TAP_INTERFACE)

# configure ip address tap/tun interface
os.system("ifconfig %s %s netmask %s" % (config.TAP_INTERFACE,config.TAP_IP,config.TAP_NETMASK))
print "IP Address %s with netmask %s configured for %s\n" % (config.TAP_IP,config.TAP_NETMASK,config.TAP_INTERFACE)

# create a route so it _could_ communicate with the outside world
os.system("route add -net %s netmask %s gw %s %s" % (config.TAP_NETADDR,config.TAP_NETMASK,config.TAP_IP,config.TAP_INTERFACE))
print "Route added for subnet %s to gateway %s with IP %s\n" % (config.TAP_NETADDR,config.TAP_INTERFACE,config.TAP_IP)

# extract inetsim sources, run the inetsim setup script to correct persmissions and add inetsim group.
os.system("tar xvf src/inetsim-1.2.2.tar.gz -C src/ && cd src/inetsim-1.2.2 && ./setup.sh")
os.system("groupadd inetsim")
