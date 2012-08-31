#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

import os


# name of your created tap interface, don't forget to bridge this with your VM's in Cuckoo
TAP_INTERFACE="tap0"

# ip address of the tap interface
TAP_IP="172.16.0.1"
TAP_NETADDR="172.16.0.0"
TAP_NETMASK="255.255.0.0"

# you're internet interface
INTERNET_INTERFACE="eth0"

