---
title: samba 用户管理
date: 2023-04-14
categories:
  - tools
tags:
  - linux
  - samba
  - tool
---

### ubuntu下共享文件夹密码设置和重置

设置账号密码和重置密码的方法如下：

```shell
 sudo smbpasswd -a user  
 New SMB password:  
 Retype new SMB password:
```

以下是 使账号 champwang 失效：
```shell
 sudo smbpasswd -d champwang
 [sudo] password for user:   
 Disabled user champwang.
```

去除添加的账号：
```shell
sudo smbpasswd -x champwang  
Deleted user champwang.
```

以下是 smbpasswd 的說明：
```shell
 smbpasswd -h
When run by root:
    smbpasswd [options] [username]
otherwise:
    smbpasswd [options]

options:
  -L                   local mode (must be first option)
  -h                   print this usage message
  -s                   use stdin for password prompt
  -c smb.conf file     Use the given path to the smb.conf file
  -D LEVEL             debug level
  -r MACHINE           remote machine
  -U USER              remote username (e.g. SAM/user)
extra options when run by root or in local mode:
  -a                   add user
  -d                   disable user
  -e                   enable user
  -i                   interdomain trust account
  -m                   machine trust account
  -n                   set no password
  -W                   use stdin ldap admin password
  -w PASSWORD          ldap admin password
  -x                   delete user
  -R ORDER             name resolve order
```

### linux及samba用户的查看与删除

查看samba服务器中已拥有哪些用户：

```shell
pdbedit -L
```

删除samba服务中的某个用户

```shell
smbpasswd -x   用户名
```

查看Linux中所有用户：

```shell
cat  /etc/passwd
```

查看Linux中添加了多少用户：

```shell
cat /etc/passwd|grep -v nologin|grep -v halt|grep -v shutdown|awk-F":" '{ print $1"|"$3"|"$4 }'|more
```

查看Linux中所有组：

```shell
cat  /etc/group
```

删除linux某个用户

```shell
userdel   用户名
```

删除linux中某个用户所有信息

```shell
userdel   -r  用户名
```

## 参考

- [原文链接](https://blog.csdn.net/qq_32693119/article/details/80016272)
