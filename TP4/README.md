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