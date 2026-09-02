---
title: ubuntu 设置虚拟显示器输出
date: 2023-04-18
categories:
  - linux
tags:
  - linux
---

### 安装程序

```Shell
$ sudo apt-get install  xserver-xorg-core-hwe-18.04
$ sudo apt-get install  xserver-xorg-video-dummy-hwe-18.04  --fix-missing
```

### 创建配置文件

~~Section "Device"
    Identifier  "Configured Video Device"
    Driver      "dummy"
EndSection
Section "Monitor"
    Identifier  "Configured Monitor"
    HorizSync 31.5-48.5
    VertRefresh 50-70
EndSection
Section "Screen"
    Identifier  "Default Screen"
    Monitor     "Configured Monitor"
    Device      "Configured Video Device"
    DefaultDepth 24
    SubSection "Display"
    Depth 24
    Modes "1920x1080"
    EndSubSection
EndSection~~

```
$ sudo nano /etc/X11/xorg.conf.d/xorg.conf

Section "Monitor"
	Identifier "Monitor0"
	HorizSync 28.0-80.0
	VertRefresh 48.0-75.0
	# https://arachnoid.com/modelines/
	# 1920x1080 @ 60.00 Hz (GTF) hsync: 67.08 kHz; pclk: 172.80 MHz
	Modeline "1920x1080_60.00" 172.80 1920 2040 2248 2576 1080 1081 1084 1118 -HSync +Vsync
EndSection
Section "Device"
	Identifier "Card0"
	Driver "dummy"
	VideoRam 256000
EndSection
Section "Screen"
	DefaultDepth 24
	Identifier "Screen0"
	Device "Card0"
	Monitor "Monitor0"
	SubSection "Display"
		Depth 24
		Modes "1920x1080_60.00"
	EndSubSection
EndSection


```

### 配置文件存储位置

```
/etc/X11/xorg.conf.d/xorg.conf
/usr/share/X11/xorg.conf.d/xorg.conf
```

## 参考

[ubuntu18.04安装虚拟显示器，不接显示器可远程桌面_AIchiNiurou的博客-CSDN博客_xrandr 不接显示器](https://blog.csdn.net/weixin_44523062/article/details/105405019)
[Ubuntu 20.04 虚拟显示器 1080P 配置](https://blog.csdn.net/zml66666/article/details/110434167)
[archlinux 显示器设置](https://wiki.archlinuxcn.org/wiki/Xorg#:~:text=Display%22%0A%20%20%20%20%20%20%20%20EndSubSection%0AEndSection-,%E5%A4%9A%E4%B8%AA%E6%98%BE%E7%A4%BA%E5%99%A8,-%5B%E7%BC%96%E8%BE%91%20%7C)
[archlinux nvidia](https://wiki.archlinuxcn.org/wiki/NVIDIA)
