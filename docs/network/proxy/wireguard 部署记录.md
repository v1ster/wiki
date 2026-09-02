---
title: wireguard 部署记录
date: 2023-09-17
categories:
  - network
tags:
  - linux
  - proxy
---

# wireguard 部署记录

## 网络类型

NAT0: OpenInternet，没有经过NAT[地址转换](https://so.csdn.net/so/search?q=%E5%9C%B0%E5%9D%80%E8%BD%AC%E6%8D%A2&spm=1001.2101.3001.7020)，公网IP

NAT1: Full Cone NAT，动态家宽可以达到最优的状态，[外网](https://so.csdn.net/so/search?q=%E5%A4%96%E7%BD%91&spm=1001.2101.3001.7020)设备可以主动发信息给NAT1网络内的设备。

NAT2: Address-Restricted Cone NAT，只有内网设备(地址:任意端口)主动发过信息给外网设备，外网设备才能主动连接NAT2的该设备的地址(地址:任意端口)
NAT3: Port-Restricted Cone NAT，只有内网设备(地址:指定端口)主动发过信息给外网设备，外网设备才能主动连接NAT3的该设备的地址(地址:指定端口)，限制为通信过的端口

NAT4: Symmetric NAT，只能和NAT0设备通讯

## 参考

- [使用 Phantun 将 WireGuard 的 UDP 流量伪装成 TCP](https://icloudnative.io/posts/wireguard-over-tcp-using-phantun/)
- [How to install PhantomJS on Ubuntu](https://gist.github.com/julionc/7476620)
- [OpenWRT路由环境下使用Cloudflare的动态DNS（DDNS）服务](https://www.qxwa.com/dynamic-dns-services-using-cloudflare-in-an-openwrt-routed-environment.html)
- [WireGuard Endpoint Discovery and NAT Traversal using DNS-SD](https://www.jordanwhited.com/posts/wireguard-endpoint-discovery-nat-traversal/)
- [P2P技术详解(一)：NAT详解——详细原理、P2P简介](http://www.52im.net/thread-50-1-1.html)
- [Open source STUN server software](https://www.stunprotocol.org/)
- [WireGuard 的搭建使用与配置详解](https://www.llmgo.cn/post/wireguard-docs-practice/)
- [peertopeer_behind_nat](https://www.reddit.com/r/WireGuard/comments/it4tkw/peertopeer_behind_nat/?rdt=57046&onetap_auto=true)
- [Wireguard 体验](https://zdyxry.github.io/2019/03/23/Wireguard-%E4%BD%93%E9%AA%8C/)
- [如何快速判断自己的网络NAT类型](https://blog.csdn.net/D3_3109/article/details/119875626)
- [Wireguard：新一代魔法上网工具](https://lqingcloud.cn/post/network-01/)
- [tool n2n](https://github.com/ntop/n2n)