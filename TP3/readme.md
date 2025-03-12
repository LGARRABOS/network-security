# TP3 : Redondance et durcissement
## Network setup

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