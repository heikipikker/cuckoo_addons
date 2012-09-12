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

cuckoo_addons
=============

This package gives additional functionality to Cuckoo with the integration of: 
TOR Transparant Proxy for anonymous analysis, iNetsim for simulated internet components and NAT for the cowboys.
It contains two executable parts: prephost.py for preperation of your host and run.py --inetsim/--nat/--tor to run the desired service. 

This software is still in development and is meant for Debian/Ubuntu based distributions. (Yes. Ubuntu and Debian were pronounced in one sentence.)

To use this script you need to have:

* Installation of the TOR package with a _DEFAULT_ configuration file. (`tor' needs to be in your $PATH)

* A working installation of iNetsim from _SOURCE_, which is included in this script under src/ which will be extracted and configured when running prephost.py -si.

* A working installation of BIND, currently only works with the `named' binary (debian).

* iptables  

* Working Cuckoo framework >= 0.3.2

* uml-utilities installed to create a TAP/TUN interface

* install argparse python library



WARNING: ALWAYS PROPERLY CONFIGURE the config.py FILE BEFORE YOU START RUNNING PREPHOST.PY

WARNING: ALWAYS PROPERLY CONFIGURE the config.py FILE BEFORE YOU START RUNNING PREPHOST.PY

WARNING: ALWAYS PROPERLY CONFIGURE the config.py FILE BEFORE YOU START RUNNING PREPHOST.PY
if you don't, you'll probably end up with broken network configuration.



 What you need to do after you run prephost.py -si(setup inetsim), prephost -st(setup TAP) and -sd(setup dependencies:

* enable IP forwarding: echo 1 > /proc/sys/net/ipv4/ip_forward 

* Configure the created tapX interface in the VirtualBox VM as a _bridged_ interface

* Statisfy iNetsim depandencies when running ./inetsim from src/inetsimXXX/ with CPAN, currently there isn't a good .deb package for newer distributions.
  Dependancies can be found here if CPAN is not working: http://www.inetsim.org/requirements.html

* Edit lib/inetsim.conf to your needs, in most cases you only need to manually change the `dns_default_ip' to your TAP interface.
  Keep in mind that iNetsim is highly configurable, you can almost change all content that is being presented by the simulated services. 

* Static IP for your network interface inside you're VM (vmnic) that is configured to bridge with the created tapX interface (e.g.: 172.16.0.1 tapX on host, 172.16.0.25/16 on vmnic)

* DNS and gateway configured to the tap0 interface (e.g.: 172.16.0.1)

Now you are ready to go! just execute ./run.py with the desired service as parameter.



