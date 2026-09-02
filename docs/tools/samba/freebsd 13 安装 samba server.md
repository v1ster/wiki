---
title: freebsd 13 安装 samba server
date: 2024-04-11
categories:
  - tools
tags:
  - samba
  - tool
---

# freebsd 13 安装 samba server

## 内核优化

 Edit `/etc/sysctl.conf`

```
kern.maxfiles=25600
kern.maxfilesperproc=16384
net.inet.tcp.sendspace=65536
net.inet.tcp.recvspace=65536
```

enable asynchronous I/O.This can be accomplished by adding the following line to the file `/boot/loader.conf`:

```
aio_load="YES"
```

To get it working without restarting, additionally execute the following command:

```bash
kldload aio
```

## Installation

```
pkg search samba4
samba413-4.13.17_8             Free SMB/CIFS and AD/DC server and client for Unix
samba416-4.16.11_2             Free SMB/CIFS and AD/DC server and client for Unix
sudo pkg install samba416
```

## Config

create a file called `/usr/local/etc/smb4.conf`

```
[global]
    workgroup = MYGROUP
    realm = mygroup.local
    netbios name = NAS

[davd data]
    path = /home/davd
    public = no
    writable = yes
    printable = no
    guest ok = no
    valid users = davd
```

Then just enable Samba and start it:

```bash
sysrc samba_server_enable=YES
service samba_server start
```

## User creation

Now that the server is running, you can’t still access your files because you got no credentials to log in with. By default Samba relies on system users, so after you created your system user using `adduser`, enable it for Samba:

```bash
pdbedit -a -u davd
```

You are prompted to enter a password which will be used to authenticate against Samba.

## 参考

[Samba fileserver on FreeBSD (Update FreeBSD 12)](https://www.davd.io/samba-fileserver-on-freebsd/)
[How-To: Setup NFS and Samba on FreeBSD 13](https://blog.vulnifo.com/2021/09/17/how-to-setup-nfs-and-samba-on-freebsd-13/)
