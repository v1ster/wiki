---
title: openvpn 局域网内分享网络
date: 2023-10-08
categories:
  - network
tags:
  - linux
  - proxy
---

# Brief

首先设置内网机器的流量请求路由到 vpn client

```Shell
ip route add 192.168.0.0/24 via 192.168.1.4
```

保存到文件夹中

```Shell
nano /etc/conf.d/net

routes_wlan1="192.168.0.0/24 via 192.168.1.4
    default via 192.168.1.1"

```

设置 vpn client 接收流量

```Shell
iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j SNAT --to-source 192.168.1.4
```

如果是openwrt 则设置防火墙区域,并设置NAT 转发
## 参考

- [Adding a permanent static route](https://wiki.gentoo.org/wiki/Static_routing)
- [使用openv屁恩实现办公室和IDC机房互通](https://www.cnblogs.com/huangweimin/articles/7712771.html)