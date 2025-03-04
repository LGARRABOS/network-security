# TP2 : Network protections
## Part I : Setup lab

🌞 Vous devez me rendre le show running-config de tous les équipements

Routeur1
```shell
Router(config)#do show running-config
Building configuration...

Current configuration : 1524 bytes

 Last configuration change at 11:09:56 UTC Tue Mar 4 2025

version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec

hostname Router

boot-start-marker
boot-end-marker

no aaa new-model


ip cef
no ipv6 cef


multilink bundle-name authenticated


interface FastEthernet0/0
 ip address 10.99.99.2 255.255.255.0
 ip nat outside
 duplex full

interface FastEthernet1/0
 no ip address
 ip nat inside
 duplex full

interface FastEthernet1/0.1
 ip nat inside

interface FastEthernet1/0.2
 ip nat inside

interface FastEthernet1/0.3
 ip nat inside

interface FastEthernet1/0.10
ip nat inside

interface FastEthernet1/0.10
 encapsulation dot1Q 10
 ip address 10.2.10.254 255.255.255.0
 ip nat inside

interface FastEthernet1/0.20
 encapsulation dot1Q 20
 ip address 10.2.20.254 255.255.255.0
 ip nat inside

interface FastEthernet1/0.30
 encapsulation dot1Q 30
 ip address 10.2.30.254 255.255.255.0
 ip nat inside

interface FastEthernet2/0
 no ip address
 shutdown
 duplex full

ip nat inside source list 1 interface FastEthernet0/0 overload
ip forward-protocol nd


ip forward-protocol nd


no ip http server
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 10.99.99.0
ip route 0.0.0.0 0.0.0.0 10.2.0.254
ip route 0.0.0.0 0.0.0.0 10.99.99.10

access-list 1 permit any
access-list 1 permit 10.2.10.0 0.0.0.255
access-list 1 permit 10.2.20.0 0.0.0.255
access-list 1 permit 10.2.30.0 0.0.0.255

control-plane


line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 login

no ip http server
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 10.99.99.0
ip route 0.0.0.0 0.0.0.0 10.2.0.254
ip route 0.0.0.0 0.0.0.0 10.99.99.10

access-list 1 permit any
access-list 1 permit 10.2.10.0 0.0.0.255
access-list 1 permit 10.2.20.0 0.0.0.255
access-list 1 permit 10.2.30.0 0.0.0.255

control-plane

line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 login


end
```

Core1
```shell
Switch(config)#do show running-config
Building configuration...

Current configuration : 963 bytes

 Last configuration change at 10:36:05 UTC Tue Mar 4 2025

version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config

hostname Switch

boot-start-marker
boot-end-marker



no aaa new-model
```

access1

```shell
Switch(config)#do show running-config
Building configuration...

Current configuration : 920 bytes

 Last configuration change at 10:33:10 UTC Tue Mar 4 2025

version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config

hostname Switch

boot-start-marker
boot-end-marker



no aaa new-model

```
access2
```shell
Switch(config)#do show running-config
Building configuration...

Current configuration : 994 bytes

 Last configuration change at 10:09:29 UTC Tue Mar 4 2025

version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config

hostname Switch

boot-start-marker
boot-end-marker



no aaa new-model

```

🌞 Ping 
```shell
VPCS> ping 10.2.30.1

84 bytes from 10.2.30.1 icmp_seq=1 ttl=63 time=30.971 ms
84 bytes from 10.2.30.1 icmp_seq=2 ttl=63 time=14.322 ms
84 bytes from 10.2.30.1 icmp_seq=3 ttl=63 time=19.818 ms
````
🌞 rePing 
```shell
VPCS> ping 8.8.8.8

84 bytes from 8.8.8.8 icmp_seq=1 ttl=253 time=34.180 ms
84 bytes from 8.8.8.8 icmp_seq=2 ttl=253 time=48.236 ms
84 bytes from 8.8.8.8 icmp_seq=3 ttl=253 time=37.783 ms
```

## Part II : Security

🌞 Ajouter des ACL sur le routeur

```shell
VPCS> ping 10.2.30.1

*10.2.10.254 icmp_seq=1 ttl=255 time=21.669 ms (ICMP type:3, code:13, Communication administratively prohibited)
*10.2.10.254 icmp_seq=2 ttl=255 time=4.186 ms (ICMP type:3, code:13, Communication administratively prohibited)
*10.2.10.254 icmp_seq=3 ttl=255 time=4.629 ms (ICMP type:3, code:13, Communication administratively prohibited)
*10.2.10.254 icmp_seq=4 ttl=255 time=9.570 ms (ICMP type:3, code:13, Communication administratively prohibited)
*10.2.10.254 icmp_seq=5 ttl=255 time=6.296 ms (ICMP type:3, code:13, Communication administratively prohibited)
```

🌞 Activer le DAI sur les switches

Core1
```shell

arp access-list ARP
permit ip host 10.2.10.1 mac host 00:50:79:66:68:03
permit ip host 10.2.20.1 mac host 00:50:79:66:68:07
permit ip host 10.2.10.2 mac host 00:50:79:66:68:06
permit ip host 10.2.20.2 mac host 00:50:79:66:68:08
permit ip host 10.2.30.1 mac host 00:50:79:66:68:09

permit ip host 10.2.10.254 mac host ffff.ffff.ffff
permit ip host 10.2.20.254 mac host ffff.ffff.ffff
permit ip host 10.2.30.254 mac host ffff.ffff.ffff
exit

ip arp inspection filter ARP vlan 10,20,30

interface ethernet 0/0
no ip arp inspection trust

interface ethernet 0/1
no ip arp inspection trust

interface ethernet 0/2
no ip arp inspection trust
```
Switch1
```shell

arp access-list ARP
permit ip host 10.2.10.1 mac host 00:50:79:66:68:03
permit ip host 10.2.20.1 mac host 00:50:79:66:68:07
permit ip host 10.2.10.2 mac host 00:50:79:66:68:06
permit ip host 10.2.20.2 mac host 00:50:79:66:68:08
permit ip host 10.2.30.1 mac host 00:50:79:66:68:09

permit ip host 10.2.10.254 mac host ffff.ffff.ffff
permit ip host 10.2.20.254 mac host ffff.ffff.ffff
permit ip host 10.2.30.254 mac host ffff.ffff.ffff
exit

ip arp inspection filter ARP vlan 10,20,30

interface ethernet 0/2
no ip arp inspection trust
```	
Switch2
```shell

arp access-list ARP
permit ip host 10.2.10.1 mac host 00:50:79:66:68:03
permit ip host 10.2.20.1 mac host 00:50:79:66:68:07
permit ip host 10.2.10.2 mac host 00:50:79:66:68:06
permit ip host 10.2.20.2 mac host 00:50:79:66:68:08
permit ip host 10.2.30.1 mac host 00:50:79:66:68:09

permit ip host 10.2.10.254 mac host ffff.ffff.ffff
permit ip host 10.2.20.254 mac host ffff.ffff.ffff
permit ip host 10.2.30.254 mac host ffff.ffff.ffff
exit

ip arp inspection filter ARP vlan 10,20,30

interface ethernet 0/1
no ip arp inspection trust
```

🌞 Activer BPDUGuard sur vos switches

Core1
```shell
enable
configure terminal
spanning-tree portfast bpduguard default

interface ethernet 0/1
 no spanning-tree bpduguard enable
exit

interface ethernet 0/2
 no spanning-tree bpduguard enable
exit

interface ethernet 0/3
 no spanning-tree bpduguard enable
exit
```
Switch1
```shell
enable
configure terminal
spanning-tree portfast bpduguard default

interface ethernet 0/2
 no spanning-tree bpduguard enable
exit
```	
Switch2
```shell
enable
configure terminal
spanning-tree portfast bpduguard default

interface ethernet 0/1
 no spanning-tree bpduguard enable
exit
```
🌞 La running-config des 4 équipements réseau

Router
```shell
Router(config)#do show running-config
Building configuration...

Current configuration : 1680 bytes

 Last configuration change at 12:51:43 UTC Tue Mar 4 2025

version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec

hostname Router

boot-start-marker
boot-end-marker


no aaa new-model

ip cef
no ipv6 cef


multilink bundle-name authenticated

interface FastEthernet0/0
 ip address 10.99.99.2 255.255.255.0
 ip nat outside
 duplex full

interface FastEthernet1/0
 no ip address
 ip access-group 100 in
 ip nat inside
 duplex full

interface FastEthernet1/0.1
 ip nat inside

interface FastEthernet1/0.2
 ip nat inside

interface FastEthernet1/0.3
 ip nat inside

interface FastEthernet1/0.3
 ip nat inside

interface FastEthernet1/0.10
 encapsulation dot1Q 10
 ip address 10.2.10.254 255.255.255.0
 ip access-group 100 in
 ip nat inside

interface FastEthernet1/0.20
 encapsulation dot1Q 20
 ip address 10.2.20.254 255.255.255.0
 ip access-group 100 in
 ip nat inside

interface FastEthernet1/0.30
 encapsulation dot1Q 30
 ip address 10.2.30.254 255.255.255.0
 ip nat inside

interface FastEthernet2/0
 no ip address
 shutdown
 duplex full

ip nat inside source list 1 interface FastEthernet0/0 overload
 duplex full

ip nat inside source list 1 interface FastEthernet0/0 overload
ip forward-protocol nd


no ip http server
no ip http secure-server
ip route 0.0.0.0 0.0.0.0 10.99.99.0
ip route 0.0.0.0 0.0.0.0 10.2.0.254
ip route 0.0.0.0 0.0.0.0 10.99.99.10

access-list 1 permit any
access-list 1 permit 10.2.10.0 0.0.0.255
access-list 1 permit 10.2.20.0 0.0.0.255
access-list 1 permit 10.2.30.0 0.0.0.255
access-list 100 deny   ip any 10.2.30.0 0.0.0.255
access-list 100 permit ip any any

control-plane

line con 0
 stopbits 1
 ip route 0.0.0.0 0.0.0.0 10.99.99.0
ip route 0.0.0.0 0.0.0.0 10.2.0.254
ip route 0.0.0.0 0.0.0.0 10.99.99.10

access-list 1 permit any
access-list 1 permit 10.2.10.0 0.0.0.255
access-list 1 permit 10.2.20.0 0.0.0.255
access-list 1 permit 10.2.30.0 0.0.0.255
access-list 100 deny   ip any 10.2.30.0 0.0.0.255
access-list 100 permit ip any any

control-plane

line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 login

end
```
