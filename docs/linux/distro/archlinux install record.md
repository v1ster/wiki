---
title: archlinux install record
date: 2023-07-08
categories:
  - linux
tags:
  - system
---

# archlinux install record

## 1. 分区

## 2. 安装 & 配置环境


```Shell

ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc

pacman -S --needed base-devel vim dhcpcd
pacman -S --overwrite amd-ucode

ln -s /usr/bin/vim /usr/bin/vi

useradd -m -G wheel mars
passwd mars
pacman -S sudo
visudo

pacman -S networkmanager

#安装中文字体
sudo pacman -S noto-fonts-cjk

```

# 安装桌面

安装桌面需要安装 显示服务(xorg 或 wayland),安装显卡驱动和桌面应用

## Display server

**`qt5-wayland` 和 `glfw-wayland` 分别为 QT5 和 [GLFW](https://www.glfw.org/) 提供 Wayland 兼容 API**
```Shell
sudo pacman -S --needed wayland \
		xorg-xwayland libxcb egl-wayland \
		glfw-wayland qt5-wayland qt6-wayland gtk3 gtk4 \
		xorg-xlsclients
```

**用 `xlsclients` 检测 XWayland**
```Shell
$ xlsclients
mapc  gsd-xsettings
mapc  ibus-x11
mapc  google-chrome
mapc  electron
mapc  mutter-x11-frames
```

## 安装显卡驱动

```Shell
sudo pacman -S --needed xf86-video-amdgpu nvidia-lts
```

**查看使用驱动**
```Shell
$ lspci -k | grep -E "VGA|3D"  -A 3
01:00.0 VGA compatible controller: NVIDIA Corporation TU106M [GeForce RTX 2060 Mobile] (rev a1)
	Subsystem: Lenovo TU106M [GeForce RTX 2060 Mobile]
	Kernel driver in use: nvidia
	Kernel modules: nouveau, nvidia_drm, nvidia
--
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev c6)
	Subsystem: Lenovo Renoir
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```

- [can't start wayland session](https://bbs.archlinux.org/viewtopic.php?id=283597)

**查看完整系统日志**
```Shell
sudo journalctl -b | curl -F 'file=@-' 0x0.st
```

**gnome 强制启用 wayland**
```Shell
7月 08 13:56:50 mapc systemd[1406]: Reached target GNOME Session Manager is ready.
7月 08 13:56:50 mapc systemd[1406]: Starting GNOME Shell on Wayland...
7月 08 13:56:50 mapc systemd[1406]: Starting GNOME Shell on X11...
7月 08 13:56:50 mapc systemd[1406]: org.gnome.Shell@wayland.service: Skipped due to 'exec-condition'.
7月 08 13:56:50 mapc systemd[1406]: Condition check resulted in GNOME Shell on Wayland being skipped.

# /etc/udev/rules.d/ override those in /usr/lib/udev/rules.d/
sudo ln -s /dev/null /etc/udev/rules.d/61-gdm.rules
```


# 安装桌面软件

# 配置

**驱动早启动**
```Shell
sudo vi

```

**多屏幕**
```Shell
sudo vi /etc/X11/xorg.conf

Section "Device"
    Identifier    "Device0"
    Driver        "nvidia"
    VendorName    "NVIDIA Corporation"
    BusID         "PCI:1:0:0"
EndSection

Section "Device"
    Identifier   "Device1"
    Driver       "amdgpu"
    BusID        "PCI:6:0:0"
EndSection
```

**自动登录**
```Shell
sudo vi /etc/gdm/custom.conf

# GDM configuration storage

[daemon]
# Uncomment the line below to force the login screen to use Xorg
#WaylandEnable=false

AutomaticLoginEnable=True
AutomaticLogin=mars

[security]

[xdmcp]

[chooser]

[debug]
# Uncomment the line below to turn on debugging
#Enable=true
```

## 参考

- [arch wiki](https://wiki.archlinux.org/)
- [arch gdm wiki](https://wiki.archlinux.org/title/GDM#Wayland_and_the_proprietary_NVIDIA_driver)
-  [Use Wayland with proprietary NVIDIA drivers](https://forum.manjaro.org/t/howto-use-wayland-with-proprietary-nvidia-drivers/36130)