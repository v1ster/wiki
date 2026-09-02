---
title: OpenWrt 使用记录
date: 2023-05-28
categories:
  - embedded
tags:
  - linux
  - yocto
---

# 1. 安装PVE 配置网络

## 1.1 下载& 安装PVE

- 下载[PVE 下载地址](https://pve.proxmox.com/wiki/Downloads#Proxmox_Virtual_Environment_7.4_.28ISO_Image.29)
-  使用 [Ventoy](https://www.ventoy.net/en/index.html)安装PVE

## 1.2 配置PVE网络

经过多次配置网口,发现使用有网络的PVE网络端口设置为控制端口最好,不然网络不好配置.例如:

| Name | Ports | description |
|:-------:|:------:|:----------:|
| vmbr0 | enp1s0| enp1s0 连接路由器|
| vmbr1 | eno1, enp2s0,enp4s| eno1 为半双工,其他为全双工|

vmbr0 设置ip, gateway和DNS,vmbr1不用设置.

# 2. 安装 OpenWrt

## 2.1 下载& 安装 OpenWrt

- ImmortWrt 下载地址
- [配置虚拟机]()
- 添加镜像到虚拟机硬盘
```Shell
qm importdisk 102 /var/lib/vz/template/iso//immortalwrt-x86-64-generic-ext4-combined-efi.img local-lvm
```

## 2.1.1 配置OpenWrt 网络

1. 修改IP 地址



3. 打开网络接口,配置

## 2.2 下载最新的OpenClash

- [OpenClash下载地址](https://github.com/vernesong/OpenClash/)

## 2.3 [WIP]使用网络共享硬盘

https://zhucebaike.com/samba-on-openwrt/
https://bbs.shumeipan.com/topic/144
### 2.3.1 导入硬盘

https://www.cnblogs.com/aozhejin/p/15863016.html

```Shell

ls /dev/disk/by-id

qm set 102 --sata1 /dev/disk/by-id/ata-SanDisk_SSD_PLUS_1000GB_23115L800072-part5
```

### 2.3.2 创建系统用户

### 2.3.3 创建Smaba 用户

```Shell
# 安装用户工具
opkg install shadow-groupmod shadow-useradd
# 创建用户并设置密码
useradd -m smbusers && passwd smbusers
# 修改用户所属组名称（创建用户同时会创建同名用户组。Windows 使用环境不允许用户和组使用相同名称）
groupmod -n smbgroups smbusers

smbpasswd -a smbusers

```

### 2.3.4 Smaba 参数配置

### 2.3.5 添加共享目录


## 2.4 [WIP]使用Aria2 配置下载文件

https://opclash.com/luyou/159.html

1. aria2总是“未运行”
核对配置文件路径和默认下载路径,==默认下载路径==需要添加反斜杠`/mnt/share/download/`
2. 附加选项添加,下载BT 磁力链接强制保存
```
force-save=true
seed-ratio=0.0
```
3. aria2下载，提示RPC服务未连接
需要开6800端口
```
nano /etc/config/aria2

config aria2 'main'
	option bt_enable_lpd 'true'
	option enable_dht 'true'
	option follow_torrent 'true'
	option file_allocation 'none'
	option save_session_interval '30'
	list header ''
	list extra_settings ''
	option enabled '1'
	option rpc_listen_port '6800'
	option config_dir '/mnt/sda3/aria2'  这个路径按自己的改一下
	option dir '/mnt/sda3/download'  这个路径按自己的改一下
	option enable_log 'true'
	option log_level 'debug'
	option rpc_auth_method 'none'
	option user 'root'
```
4. openwrt 关于网页设置Aria2出现一个或多个必选项值为空
默认验证方式为账户密码验证方式,修改设置`option rpc_auth_method 'none'`
```Shell
nano /etc/config/aria2

config aria2 'main'
	option bt_enable_lpd 'true'
	option enable_dht 'true'
	option follow_torrent 'true'
	option file_allocation 'none'
	option save_session_interval '30'
	list header ''
	list extra_settings ''
	option enabled '1'
	option rpc_listen_port '6800'
	option config_dir '/mnt/sda3/aria2'
	option dir '/mnt/sda3/download'
	option enable_log 'true'
	option log_level 'debug'
	option rpc_auth_method 'none'
	option user 'root'
```

## 参考

- [关于aria2最完整的一篇](http://ivo-wang.github.io/2019/04/18/%E5%85%B3%E4%BA%8Earia2%E6%9C%80%E5%AE%8C%E6%95%B4%E7%9A%84%E4%B8%80%E7%AF%87/)
- [OpenWrt 安装配置 Samba 实现网络文件共享](https://zhucebaike.com/samba-on-openwrt/)
- [openwrt 关于网页设置Aria2出现一个或多个必选项值为空](https://blog.csdn.net/popuui123/article/details/111399587)
- [OpenWrt 安装及配置 Aria2 远程下载教程](https://opclash.com/luyou/159.html)
- [linux磁盘分区fdisk命令操作（实践）](https://www.cnblogs.com/aozhejin/p/15863016.html)
- [用这些 OpenWRT 插件来武装你的路由器](https://zhuanlan.zhihu.com/p/103121214)
- [在PVE中，给虚拟机挂载独立的硬盘](https://bbs.shumeipan.com/topic/144)
- [PVE虚拟机的安装](https://www.benzhu.xyz/pve/)
- [OpenWrt搭建文件共享服务——基于samba](https://blog.csdn.net/a791693310/article/details/84584680)