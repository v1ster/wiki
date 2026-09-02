---
title: 搭建clash 并且分享网络
date: 2023-04-12
categories:
  - network
tags:
  - linux
  - proxy
  - tool
---

### 下载&安装clash

```Shell
sudo apt install git iproute2 iptables nftables jq -y
sudo git clone  https://github.com/Kr328/clash-premium-installer
cd clash-premium-installer/
sudo wget https://github.com/Dreamacro/clash/releases/download/v1.11.4/clash-linux-amd64-v3-v1.11.4.gz
sudo gzip -d clash-linux-amd64-v3-v1.11.4.gz
sudo mv clash-linux-amd64-v3-v1.11.4 clash
sudo chmod 775 clash
sudo cp clash /usr/bin
sudo ./installer.sh  install
sudo cp config.yaml  /srv/clash/config.yaml

systemctl start clash
systemctl status clash
systemctl enable clash
```

### 搭建clash-dashboard

```Shell
sudo git clone -b gh-pages --depth 1 https://github.com/Dreamacro/clash-dashboard ~/app/clash-dashboard
sudo /srv/clash/config.yaml # 编辑clash配置文件
```

#### 在文中修改或增加以下内容

```
external-controller: 0.0.0.0:9090 # 修改ip地址和端口
external-ui: /etc/clash/clash-dashboard # clash-dashboard的路径
secret:'112233' # 112233是连接的密钥，自行设置
```

 **重启**
```Shell
systemctl restart clash
```

### iptable 设置端口转发共享网络

#### Linux:

```Shell
echo "1" > /proc/sys/net/ipv4/ip_forward
iptables -F  #清空规则
iptables -P INPUT ACCEPT
#iptables -P INPUT -i eth1 -j ACCEPT
iptables -P FORWARD ACCEPT
#eth0 为有网络的端口
iptables -t nat -A POSTROUTING -s 192.168.*.0/24 -o eth0 -j MASQUERADE
```

#### Windows:

 手动设置IP地址和网关设置为linux主机的IP
 手动设置DNS 114.114.114.114 8.8.8.8 4.4.4.4

## 参考

- [clash 安装](https://zhuanlan.zhihu.com/p/545734974)
- [iptables实现网络数据转发和网络数据共享功能](https://blog.csdn.net/li_wen01/article/details/86714176)
- [iptable语法](https://wiki.centos.org/HowTos/Network/IPTables)
- [Debian 部署 Clash Web 管理页](https://www.modb.pro/db/399645)
- [设置IP地址、网关、DNS](https://www.osyunwei.com/archives/2199.html)