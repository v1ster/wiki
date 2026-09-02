---
title: Ubuntu 没有网络连接
date: 2023-04-18
categories:
  - linux
tags:
  - linux
---

```Shell
sudo gedit /etc/NetworkManager/NetworkManager.conf
```
将 `managed` 的 ==false== 改为 ==true== ，最终修改为：
```Shell
sudo service network-manager stop
sudo rm /var/lib/NetworkManager/NetworkManager.state
sudo service network-manager start
```
重启网络服务:
```Shell
sudo service network-manager stop
sudo rm /var/lib/NetworkManager/NetworkManager.state
sudo service network-manager start
```