# TP4 : Maintien en conditions opérationnelles
## Part I : SSH sur les routeurs
### 1. Création d'utilisateur

🌞 Créer un utilisateur

```bash
enable
configure terminal
username toto privilege 15 secret toto
ip domain-name r1
hostname R1
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh pubkey-chain
username toto
key-string
AAAAB3NzaC1yc2EAAAADAQABAAABgQDbD4kM5jk4jf4vQTZBZ2EGadZ7dwxZX1wax06cQxmH
WCYdD8cexbebflUF0crT22ASpmusreRAbAK+FJMNhPUDWb+eq/TSYAWbBrbve2p+zUhdgROLr0wOV6Qq
5sdnr6onuPeAUmKq2USEjWaFE+MklL1A7k90VTqn/egmVNRu1E5o/LBombef9DvI6IX2W+x6dQ6Thljc
UeJJGL5nKX5WK4e6eH7XQmlZQmuRcufr5mkUym6CsrCWBEzoqIjN4vhE7VbGro9WWJjaLlKQgVY/3esb
3VcxaSFmkMODbLlOzs56DoLEQzohtWIycDF6ufcpZXdGjbh7dSHlxbHQQeGhle2jsoN0LWJcUoXbKoKL
N1Ie00f3nEiH1oNsepJOmjtI9A+Ww4aQFkjOhhidS7gvX59P86/xLp1rEAGvOpkE+Vfez6XUAi7fNETD
chIhY/eQj9+YB1Vv1X/QY0jgvnV3/9D4EmXj0FLyACP6yZ/u/lznm5gZiiyh7z3ux/bLehk=
exit
do wr
```
🌞 Activer le serveur SSH

```bash
enable
configure terminal
line vty 0 4
transport input ssh
login local
exit
exit
do wr
```
🌞 Prouvez que la connexion est fonctionnelle

Configuration ssh.conf
```bash
Host r1
    Hostname 10.3.30.252
        User toto
        KexAlgorithms +diffie-hellman-group1-sha1
        PubkeyAcceptedAlgorithms +ssh-rsa
        HostkeyAlgorithms +ssh-rsa
        Ciphers +aes256-cbc
        MACs hmac-sha1,hmac-md5
Host r2
    Hostname 10.3.30.253
        User toto
        KexAlgorithms +diffie-hellman-group1-sha1
        PubkeyAcceptedAlgorithms +ssh-rsa
        HostkeyAlgorithms +ssh-rsa
        Ciphers +aes256-cbc
        MACs hmac-sha1,hmac-md5
```
Teste de connexion sur R2
```bash
[toto@localhost ~]$ ssh toto@r2
R2#
R2#exit
Connection to 10.3.30.253 closed by remote host.
Connection to 10.3.30.253 closed.
```

## Part II : Bastion SSH

🌞 Config réseau

```bash
[toto@localhost ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:00:7a:31 brd ff:ff:ff:ff:ff:ff
    inet 10.3.30.100/24 brd 10.3.30.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe00:7a31/64 scope link
       valid_lft forever preferred_lft forever
[toto@localhost ~]$
```
🌞 Serveur SSH
    
```bash
[toto@Bastion ~]$ ss -tuln | grep ':22'
tcp   LISTEN 0      128          0.0.0.0:22        0.0.0.0:*
tcp   LISTEN 0      128             [::]:22           [::]:*

[toto@Bastion ~]$ systemctl status sshd
● sshd.service - OpenSSH server daemon
     Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: enabled)
     Active: active (running) since Wed 2025-03-26 11:18:29 CET; 2min 50s ago
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 704 (sshd)
      Tasks: 1 (limit: 4656)
     Memory: 6.4M
        CPU: 124ms
     CGroup: /system.slice/sshd.service
             └─704 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

Mar 26 11:18:28 Bastion systemd[1]: Starting OpenSSH server daemon...
Mar 26 11:18:29 Bastion sshd[704]: Server listening on 0.0.0.0 port 22.
Mar 26 11:18:29 Bastion sshd[704]: Server listening on :: port 22.
Mar 26 11:18:29 Bastion systemd[1]: Started OpenSSH server daemon.
Mar 26 11:20:25 Bastion sshd[1210]: Accepted password for toto from 10.3.30.1 port 53439 ssh2
Mar 26 11:20:25 Bastion sshd[1210]: pam_unix(sshd:session): session opened for user toto(uid=1000) by toto(uid=0)

[toto@Bastion ~]$ sudo firewall-cmd --list-services
[sudo] password for toto:
cockpit dhcpv6-client ssh
```
🌞 Connexion SSH
    
```bash
PS C:\Users\garra> ssh toto@10.3.30.100
Last login: Wed Mar 26 11:20:25 2025 from 10.3.30.1
[toto@Bastion ~]$
```
🌞 Fichier SSH config
    
```bash
Host bastion
  Hostname 10.3.30.100
  User toto
  IdentityFile C:\Users\garra\.ssh\id_ed25519
```

🌞 Proof !

```bash
PS C:\Users\garra> ssh bastion
The authenticity of host '10.3.30.100 (10.3.30.100)' can't be established.
ED25519 key fingerprint is SHA256:O6Ws9QyCTYBJAw6a+bCtGZYhfUh94rU17ZeP8zVDe/8.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.3.30.100' (ED25519) to the list of known hosts.
Last login: Wed Mar 26 11:35:56 2025 from 10.3.30.1
[toto@Bastion ~]$
```

🌞 Mettre à jour la clé publique déposées sur les routeurs
    
```bash
en
conf t
crypto key zeroize rsa
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh pubkey-chain
username toto
key-string

```

## Part III : SNMP
### 1. Activer le serveur SNMP

🌞 Activer le service SNMP

```bash
enable
configure terminal
snmp-server community tp4 RO
do wr
```

🌞 Vérifier l'état du service SNMP

```bash
R1#show snmp community

Community name: ILMI
Community Index: ILMI
Community SecurityName: ILMI
storage-type: read-only  active


Community name: tp4
Community Index: tp4
Community SecurityName: tp4
storage-type: nonvolatile        active
```
### 2. Requêter SNMP

🌞 Sur votre bastion

```bash
[toto@Bastion ~]$ snmpwalk -v
snmpwalk: option requires an argument -- 'v'
USAGE: snmpwalk [OPTIONS] AGENT [OID]

  Version:  5.9.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net
```
```bash	
[toto@Bastion ~]$ snmpwalk -v2c -c tp4 10.3.30.252
SNMPv2-MIB::sysDescr.0 = STRING: Cisco IOS Software, 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)S6, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Fri 08-Aug-14 04:05 by prod_rel_team
SNMPv2-MIB::sysObjectID.0 = OID: SNMPv2-SMI::enterprises.9.1.222
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (97920) 0:16:19.20
SNMPv2-MIB::sysContact.0 = STRING:
SNMPv2-MIB::sysName.0 = STRING: R1.r1
SNMPv2-MIB::sysLocation.0 = STRING:
SNMPv2-MIB::sysServices.0 = INTEGER: 78
SNMPv2-MIB::sysORLastChange.0 = Timeticks: (0) 0:00:00.00
IF-MIB::ifNumber.0 = INTEGER: 6
IF-MIB::ifIndex.1 = INTEGER: 1
IF-MIB::ifIndex.2 = INTEGER: 2
IF-MIB::ifIndex.3 = INTEGER: 3
IF-MIB::ifIndex.4 = INTEGER: 4
```
🌞 Trouvez une commande

```bash	
[toto@Bastion ~]$ snmpwalk -v2c -c tp4 10.3.30.252 1.3.6.1.2.1.2.2.1.2
IF-MIB::ifDescr.1 = STRING: FastEthernet0/0
IF-MIB::ifDescr.2 = STRING: FastEthernet1/0
IF-MIB::ifDescr.3 = STRING: Null0
IF-MIB::ifDescr.4 = STRING: FastEthernet1/0.10
IF-MIB::ifDescr.5 = STRING: FastEthernet1/0.20
IF-MIB::ifDescr.6 = STRING: FastEthernet1/0.30
```
[snmp.pcap](/snmp.pcap)

### 3. Un peu de visualisation

🌞 Installer Netdata sur votre bastion
