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

