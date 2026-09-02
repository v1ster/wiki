---
title: 设置静态 IP 地址
date: 2023-05-06
categories:
  - linux
tags:
  - linux
---

# 使用终端 设置静态IP

#### 查看可用的网络接口

```shell
ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enP4p65s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:e0:4c:68:02:0e brd ff:ff:ff:ff:ff:ff
```

#### 使用nano 编辑 `/etc/network/interfaces` 文件

```shell
cat /etc/network/interfaces
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
source /etc/network/interfaces.d/*
```

如果看到interfaces 文件内容如上所示, 可以在`/etc/network/interfaces.d/` 文件夹下新建配置文件
```
sudo nano  /etc/network/interfaces.d/enP4p65s0.conf

# 文件内填写
auto enP4p65s0
iface enP4p65s0 inet static
address 192.168.137.110
netmask 255.255.255.0
gateway 192.168.137.1
dns-nameservers 192.168.137.1 114.114.114.114

#保存并退出,重启服务
sudo systemctl restart NetworkManager
```

## 参考

- [如何在 Debian 11 上设置一个静态 IP 地址](https://juejin.cn/post/7124495623914520589)