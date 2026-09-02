---
title: apt certificate verification failed
date: 2023-05-10
categories:
  - tools
tags:
  - apt
  - tool
---

```shell
touch /etc/apt/apt.conf.d/99verify-peer.conf \
&& echo >>/etc/apt/apt.conf.d/99verify-peer.conf "Acquire { https::Verify-Peer false }"

 apt-get -o Acquire::http::proxy="http://192.168.137.1:7890/" update

```

## 参考

- [apt-get update failed because certificate verification failed because handshake failed on nodesource](https://askubuntu.com/questions/1095266/apt-get-update-failed-because-certificate-verification-failed-because-handshake)