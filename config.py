#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

import os

# The FULL path to your cuckoo installation
CUCKOO_PATH="~/src/cuckoo/"

# a user to run components of this script for security reasons
CUCKOO_USER=""

# The RELATIVE path to your source dir of inetsim
INETSIM_PATH="src/inetsim-1.2.2/"

# The path to the tor binary, default the scripts uses the system's $PATH to locate the binary
TOR_PATH="src/tor-0.2.2.38/"

# name of your created tap interface, don't forget to bridge this with your VM's in Cuckoo
TAP_INTERFACE="tap0"

# ip address of the tap interface
TAP_IP="172.16.0.1"
TAP_NETADDR="172.16.0.0"
TAP_NETMASK="255.255.0.0"

# you're internet interface
INTERNET_INTERFACE="eth0"

