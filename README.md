cuckoo_addons
=============
#!/usr/bin/python
# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.



This is a script that give additional functionality to Cuckoo with the intergration of: 
TOR Transparant Proxy for anonymous analysis, iNetsim for simulated internet and NAT for the cowboys.

To use this script you need to have:

* Installation of the TOR package with a _DEFAULT_ configuration file.
* A working installation of iNetsim from _SOURCE_
* A working installation of BIND, currently only works with the `named' binary.
* iptables  
* Cuckoo >= 0.3.2
* uml-utilities installed to create a TAP/TUN interface
* ipv4 forwarding enabled
* route from the TAP interface to you're outgoing interface (e.g. eth0)

This script does al the magic for the TOR Transparant Proxy, just fill in the right listning addresses in config.py.

