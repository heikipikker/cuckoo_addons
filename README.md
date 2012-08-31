# Copyright (C) 2012 Serge van Namen <serge@se-cured.org>.

cuckoo_addons
=============

This is a script that gives additional functionality to Cuckoo with the integration of: 
TOR Transparant Proxy for anonymous analysis, iNetsim for simulated internet components and NAT for the cowboys.

This script is still in development and is meant for Debian/Ubuntu based distributions. (Yes. Ubuntu and Debian were pronounced in one sentence.)

To use this script you need to have:

* Installation of the TOR package with a _DEFAULT_ configuration file. (`tor' needs to be in your $PATH)

* A working installation of iNetsim from _SOURCE_, which is included in this script under src/ which will be extracted and configured when running prephost.py -si.

* A working installation of BIND, currently only works with the `named' binary(debian).

* iptables  

* Working Cuckoo framework >= 0.3.2

* uml-utilities installed to create a TAP/TUN interface

* install argparse python library



WARNING: ALWAYS PROPERLY CONFIGURE the config.py FILE BEFORE YOU START RUNNING PREPHOST.PY



 What you need to do after you run prephost.py -si(setup inetsim) and prephost -st(setup TAP),:

* enable IP forwarding: echo 1 > /proc/sys/net/ipv4/ip_forward 

* Configure the created tapX interface in the VirtualBox VM as a _bridged_ interface

* Statisfy iNetsim depandencies when running ./inetsim from src/inetsimXXX/ with CPAN, currently there isn't a good .deb package.
  Dependancies can be found here if CPAN is not working: http://www.inetsim.org/requirements.html

* edit lib/inetsim.conf to your needs, in most cases you only need to manually change the `dns_default_ip' to your TAP interface.

* Static IP for your network interface inside you're VM (vmnic) that is configured to bridge with the created tapX interface (e.g.: 172.16.0.1 tapX on host, 172.16.0.25/16 on vmnic)

* DNS and gateway configured to the tap0 interface (e.g.: 172.16.0.1)

Now you are ready to go! just execute ./run.py with the desired service as parameter.



