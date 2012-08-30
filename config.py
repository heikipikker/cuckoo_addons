#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

# The path to your cuckoo installation
CUCKOO_PATH="~/src/cuckoo/"

# The path to your source dir of inetsim
INETSIM_PATH="/opt/inetsim-1.2.2/"

# name of your created tap interface, don't forget to bridge this with you VM
TAP_INTERFACE="tap0"

# ipaddress of the tap interface
TAP_IP="172.16.0.1"
TAP_NETADDR="172.16.0.0"
TAP_NETMASK="255.255.0.0"

# you're internet interface
INTERNET_INTERFACE="eth0"
