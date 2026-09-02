---
title: ssh 端口转发
date: 2023-06-08
categories:
  - tools
tags:
  - ssh
  - tool
---

# 1. SSH 端口转发

1. 本地端口转发
```shell
ssh -fgN -L 本机端口:目标地址:目标端口 本机端口
# example:
ssh -fgN -L 8080:192.168.0.48:80 192.168.137.1
```
2. 远程端口转发
```Shell
ssh -fgN -R 2222:目标地址:目标端口 localhost
```
3. 动态转发
```Shell
ssh -fgN -D 12345 root@目标地址
```


## 参考

- [Linux端口转发的几种常用方法](https://cloud.tencent.com/developer/article/1688152)
