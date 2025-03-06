# liste des conf

agrégat de lien LACP
```bash
# Switch 1
en
conf t
interface range ethernet 1/0 - 1
channel-group 1 mode active
exit
interface port-channel 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 10,20,30
exit
do wr
```

```bash
# Switch 2
en
conf t
interface range ethernet 1/0 - 1
channel-group 1 mode passive
exit
interface port-channel 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 10,20,30
exit
do wr
```
Vlan 10,20,30

```bash
# Switch 1
en
conf t
vlan 10
name client
exit
vlan 20
name admin
exit
vlan 30
name serveur
exit
interface range ethernet 1/2
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet 0/1 - 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface port-channel 1
switchport trunk allowed vlan add 10,20,30
do wr
```

```bash
# Switch 2
en
conf t
vlan 10
name client
exit
vlan 20
name admin
exit
vlan 30
name serveur
exit
interface range ethernet 1/2
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet 0/1 - 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface port-channel 1
switchport trunk allowed vlan add 10,20,30
do wr
```

```bash
# Switch 3
en
conf t
vlan 10
name client
exit
vlan 20
name admin
exit
vlan 30
name serveur
exit
interface range ethernet0/0 - 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet0/1 - 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
exit
do wr
```

```bash
# Switch 4
en
conf t
vlan 10
name client
exit
vlan 20
name admin
exit
vlan 30
name serveur
exit
interface range ethernet0/0 - 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet0/1 - 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
exit
do wr
```

```bash
# Switch 5
en
conf t
vlan 10
name client
exit
vlan 20
name admin
exit
interface range ethernet0/0 - 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet0/2
switchport mode access
switchport access vlan 10
interface range ethernet0/3
switchport mode access
switchport access vlan 20
exit
do wr
```

```bash
# Switch 6
en
conf t
vlan 20
name admin
exit
interface range ethernet0/0 - 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet0/2
switchport mode access
switchport access vlan 20
exit
do wr
```

```bash
# Switch 7
en
conf t
vlan 30
name serveur
exit
interface range ethernet0/0
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet0/2
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 10,20,30
interface range ethernet0/1
switchport mode access
switchport access vlan 30
exit
do wr
```

Configuration des routeurs

```bash
# Routeur 1
en
conf t
interface fa 1/0.10
encapsulation dot1Q 10
ip address 10.3.10.252 255.255.255.0
standby 10 ip 10.3.10.254 
standby 10 priority 150
standby 10 preempt
no sh
exit
interface fa 1/0.20
encapsulation dot1Q 20
ip address 10.3.20.252 255.255.255.0
standby 20 ip 10.3.20.254 
standby 20 priority 150
standby 20 preempt
no sh
exit
interface fa 1/0.30
encapsulation dot1Q 30
ip address 10.3.30.252 255.255.255.0
standby 30 ip 10.3.30.254 
standby 30 priority 100
no sh
interface fastEthernet 1/0
no sh
exit
do wr
```

```bash
# Routeur 2
en
conf t
interface fa 1/0.10
encapsulation dot1Q 10
ip address 10.3.10.253 255.255.255.0
standby 10 ip 10.3.10.254 
standby 10 priority 100
no sh
exit
interface fa 1/0.20
encapsulation dot1Q 20
ip address 10.3.20.253 255.255.255.0
standby 20 ip 10.3.20.254 
standby 20 priority 100
no sh
exit
interface fa 1/0.30
encapsulation dot1Q 30
ip address 10.3.30.253 255.255.255.0
standby 30 ip 10.3.30.254 
standby 30 priority 150
standby 30 preempt
no sh
interface fastEthernet 1/0
no sh
exit
do wr
```
Config NAT sur les deux routeurs

```bash
# Routeur 1
en
conf t
interface fastEthernet 0/0
ip address 10.88.88.20 255.255.255.0
ip nat outside
no sh
exit
interface fastEthernet 1/0.10
ip nat inside
exit
interface fastEthernet 1/0.20
ip nat inside
exit
interface fastEthernet 1/0.30
ip nat inside
exit
access-list 1 permit any
ip nat inside source list 1 interface fastEthernet 0/0 overload
ip route 0.0.0.0 0.0.0.0 10.88.88.10
do wr
```

```bash
# Routeur 2
en
conf t
interface fastEthernet 0/0
ip address 10.99.99.20 255.255.255.0
ip nat outside
no sh
exit
interface fastEthernet 1/0.10
ip nat inside
exit
interface fastEthernet 1/0.20
ip nat inside
exit
interface fastEthernet 1/0.30
ip nat inside
exit
access-list 1 permit any
ip nat inside source list 1 interface fastEthernet 0/0 overload
ip route 0.0.0.0 0.0.0.0 10.99.99.10
do wr
```


```bash