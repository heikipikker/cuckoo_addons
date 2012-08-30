import time
import sys
import os

def Tor():	
	os.system("tor VirtualAddrNetwork 10.192.0.0/10 AutomapHostsOnResolve 1 TransPort 9040 TransListenAddress 172.16.0.1 DNSPort 53 DNSListenAddress 172.16.0.1")
	os.system("iptables -t nat -A PREROUTING -i tap0 -p udp -m udp --dport 53 -j REDIRECT --to-ports 53")
	os.system("iptables -t nat -A PREROUTING -i tap0 -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 9040")

	while True:
		try:
			time.sleep(1)

		except KeyboardInterrupt:
			# Kill TOR Transparant Proxy
			os.system("pkill tor")
			# clear iptables rules
			os.system("iptables -t nat -D PREROUTING -i tap0 -p udp -m udp --dport 53 -j REDIRECT --to-ports 53")
			os.system("iptables -t nat -D PREROUTING -i tap0 -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 9040")
			print "\nTOR Transparant Proxy disabled, clearing added iptables rules"
			sys.exit()
