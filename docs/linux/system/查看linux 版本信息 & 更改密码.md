---
title: 查看linux 版本信息 & 更改密码
date: 2023-04-28
categories:
  - linux
tags:
  - linux
---

## 查看linux 内容信息

```Shell
# 当前系统的内核版本号及系统名称
$ cat /proc/version
Linux version 5.15.32-v7l+ (dom@buildbot) (arm-linux-gnueabihf-gcc-8 (Ubuntu/Linaro 8.4.0-3ubuntu1) 8.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #1538 SMP Thu Mar 31 19:39:41 BST 2022
$ uname -a
Linux raspberrypi 5.15.32-v7l+ #1538 SMP Thu Mar 31 19:39:41 BST 2022 armv7l GNU/Linux
# 查看硬件
$ cat /proc/cpuinfo
Hardware	: BCM2711
Revision	: d03114
Serial		: 100000002019bf00
Model		: Raspberry Pi 4 Model B Rev 1.4
```

## Ubuntu更改密码

1. 进入Ubuntu，打开一个终端，输入 sudo su转为root用户。 注意，必须先转为root用户！！！
2.  sudo passwd user(user 是对应的用户名)
3. 输入新密码，确认密码。
4. 修改密码成功，重启，输入新密码进入Ubuntu。