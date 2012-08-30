#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

import sys
import time
import argparse
import os
import config

# This is going to be installation script for setting up your host.
# NEED TO CHECK ROUTE
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("tunctl -t %s" % (config.TAP_INTERFACE))
os.system("ifconfig %s %s netmask %s" % (config.TAP_INTERFACE,config.TAP_IP,config.TAP_NETMASK))
os.system("route add -net %s netmask %s gw %s %s" % (config.TAP_NETADDR,config.TAP_NETMASK,config.TAP_IP,config.TAP_INTERFACE))



