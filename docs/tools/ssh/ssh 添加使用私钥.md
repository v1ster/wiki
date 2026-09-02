---
title: ssh 添加使用私钥
date: 2023-07-08
categories:
  - tools
tags:
  - ssh
  - tool
---

# brief

添加和使用私钥,ssh有权限要求.
.ssh 目录权限设置700
id_rsa,authiruzed_keys 权限设置600
id_rsa.pub, known_hosts 权限设置644

```Shell
# 查看私钥是否可用
ssh-add ~/.ssh/mars_rsa

# 如果出现下面提示修改权限即可
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions **0744** for '**/home/<_username_>/.ssh/id_rsa**' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.

sudo chown -R mars ~/.ssh
sudo chmod 700 ~/.ssh

sudo chmod 600  ~/.ssh/id_rsa
sudo chmod 600 ~/.ssh/mars_rsa

```

## 参考

- [ssh密钥文件的权限](https://blog.51cto.com/merrycheng/1340280)
- [Signing Failed: Agent Refused Operation](https://www.shellhacks.com/signing-failed-agent-refused-operation-solved/)