---
title: ssh 设置代理
date: 2023-07-17
categories:
  - tools
tags:
  - ssh
  - tool
---

```Shell
nano ~/.ssh/config

Host *
  ProxyCommand /usr/bin/nc -X connect -x <PROXY_HOST>:<PROXY_PORT> %h %p

Host github.com
    User git
    ProxyCommand nc -v -x 192.168.137.1:7890 %h %p

```

	1. bash: /usr/bin/nc: No such file or directory
```Shell
apt install netcat
```