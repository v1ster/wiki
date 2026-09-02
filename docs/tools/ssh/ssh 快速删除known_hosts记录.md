---
title: ssh 快速删除known_hosts记录
date: 2024-01-10
categories:
  - tools
tags:
  - ssh
  - tool
---

```
ssh-keygen -R 192.168.0.10

ssh-keygen -R [hostname]

ssh-keygen -R [ip_address]

ssh-keygen -R [hostname],[ip_address]

ssh-keyscan -t rsa [hostname],[ip_address] >> ~/.ssh/known_hosts

ssh-keyscan -t rsa [ip_address] >> ~/.ssh/known_hosts

ssh-keyscan -t rsa [hostname] >> ~/.ssh/known_hosts

```

## 参考

[KNOWN_HOSTS处理](https://developer.aliyun.com/article/6827)