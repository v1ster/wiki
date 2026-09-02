---
title: cloudflared 内网代理
date: 2023-04-13
categories:
  - network
tags:
  - linux
  - proxy
  - tool
---

## cloudflared故障解决

```Shell
sudo sysctl -w net.ipv4.ping_group_range='0 100'
sudo nano /proc/sys/net/ipv4/ping_group_range
```

## ssh代理

## 参考

1. [HOW TO: Remote access a Raspberry Pi using a Cloudflare tunnel (node-red and ssh).](https://www.youtube.com/watch?v=Z6b3l1z0N7w)
2. [Cloudflare Docs](https://developers.cloudflare.com/cloudflare-one/setup/)
3. [用 Cloudflare Tunnel 进行内网穿透](https://blog.outv.im/2021/cloudflared-tunnel/)

