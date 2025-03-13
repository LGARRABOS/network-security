# TP3 : Redondance et durcissement
## Network setup

Si besoin toute les configurations sont dans le fichier [conf.md](conf.md)


🌞 Insérer un serveur DHCP dans la topologie
(utilisation d'un routeur car buf avec l'ajout de VM)

```bash
interface fa1/0.30
 encapsulation dot1Q 30
ip address 10.3.30.251 255.255.255.0
ip dhcp excluded-address 10.3.30.251 10.3.30.254
ip dhcp pool VLAN30_POOL
 network 10.3.30.0 255.255.255.0
 default-router 10.3.30.251
 dns-server 8.8.8.8
exit
service dhcp
do write memory
```

🌞 Configurer le DHCP IP Helper sur les routeur
    
```bash
enable
configure terminal
interface fa1/0.10
 encapsulation dot1Q 10
 ip address 10.3.10.1 255.255.255.0
 ip helper-address 10.3.30.251
interface fa1/0.20
 encapsulation dot1Q 20
 ip address 10.3.20.1 255.255.255.0
 ip helper-address 10.3.30.251
exit
do write memory
```





## Part III : Harden this
### A. STP protections

Switch 5
```bash
enable
configure terminal
interface range e0/2 - 3
 spanning-tree portfast
 spanning-tree bpduguard enable
exit
do write memory
```

Switch 6
```bash
enable
configure terminal
interface e0/2
 spanning-tree portfast
 spanning-tree bpduguard enable
exit
do write memory
```

Switch 7
```bash
enable
configure terminal
interface e0/1
 spanning-tree portfast
 spanning-tree bpduguard enable
exit
do write memory
```

### B. DHCP protections

Sur tout les switchs
```bash
enable
configure terminal
ip dhcp snooping
ip dhcp snooping vlan 10 20
exit
do write memory
```

Sur le SWITCH 1 relier au routeur R1 qui sert de serveur dhcp
```bash
enable
configure terminal
interface e0/1
ip dhcp snooping trust
exit
do write memory
```

## C. ARP protections

Sur tout les switchs
```bash
enable
configure terminal
ip arp inspection vlan 10 20
exit
do write memory
```

Sur le SWITCH 1 relier au routeur R1 qui sert de serveur dhcp
```bash
interface e0/1
 ip arp inspection trust
exit
do write memory
```

Sur les switchs 5, 6 et 7
```bash
enable
configure terminal
interface range e0/0 # on change les ports en focntion des SWITCH
 ip arp inspection limit rate 10 # limiter le nombre de requête ARP et donc que personne ne se branche a la place d'un VPC
exit
do write memory
```

## 2. Protect L3
### A. ACL

Sur les deux routeurs
```bash
enable
configure terminal
ip access-list extended secure
 permit ip any host 10.3.30.67
 deny ip any 10.3.30.0 0.0.0.255
 permit ip any any
interface fa1/0.10
 ip access-group secure in
 interface fa1/0.20
 ip access-group secure in
 interface fa1/0.30
 ip access-group secure in
exit
do write memory
```

