---
title: ssh 如何向服务器添加公钥
date: 2023-04-28
categories:
  - tools
tags:
  - ssh
  - tool
---

### 如何向服务器添加 ssh 公钥 : 

#### wondows传输pub

```cmd
type %USERPROFILE%\.ssh\id_rsa.pub | ssh ubuntu@192.168.1.8 “cat >> .ssh/authorized_keys”
```

```powershell
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh root@192.168.30.31 "cat >> .ssh/authorized_keys"
```
#### linux
```shell
ssh-copy-id -i ~/.ssh/id_rsa.pub YOUR_USER_NAME@IP_ADDRESS_OF_THE_SERVER
```

#### linux 手动添加

```Shell
mkdir -p /home/user_name/.ssh && touch /home/user_name/.ssh/authorized_keys
vim /home/user_name/.ssh/authorized_keys
# 为文件设置权限
chmod 700 /home/user_name/.ssh && chmod 600 /home/user_name/.ssh/authorized_keys
# 由于我们使用 root 或我们自己的管理员帐户为其他用户创建了这些文件，所以需要更改用户的所有权：
chown -R username:username /home/username/.ssh

```

### SSH 保持长连接

#### 客户端主动保持连接

编辑`/etc/ssh/ssh_config` 或者`~/.ssh/config`，追加以下内容
```shell
TCPKeepAlive=yes 
# Client每隔 180 秒发送一次KeepAlive请求给Server，然后Server响应从而保持连接 
ServerAliveInterval 180 
# Client发出请求后，服务器端未响应次数达到3，就自动断开连接。正常情况下，Server基本会响应。 
ServerAliveCountMax 3
```

#### 服务的主动保持连接

- 编辑`/etc/ssh/sshd_config`，追加以下内容
```shell
# Server每隔 180 秒发送一次心跳数据包给Client，然后Client响应从而保持连接 
ClientAliveInterval 180 
# Server发出请求后，客户端未响应次数达到10，就自动断开连接。正常情况下，Client基本会响应 
ClientAliveCountMax 10
```

- **重启ssh服务**以使配置生效
```shell
systemctl restart sshd
```

### scp 传输文件
```Shell
scp -r ./codespace/repos/tof_demo pi@192.168.0.68:~/
```

## 参考

- [如何向服务器添加 ssh 公钥](https://www.51cto.com/article/749011.html)
- [SSH保持长连接](https://qgrain.github.io/2020/03/27/SSH%E4%BF%9D%E6%8C%81%E9%95%BF%E8%BF%9E%E6%8E%A5/)