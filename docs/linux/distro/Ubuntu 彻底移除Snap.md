---
title: Ubuntu 彻底移除Snap
date: 2023-04-18
categories:
  - linux
tags:
  - linux
---

### 彻底移除Snap

（1）删掉所有的已经安装的 Snap 软件。
```Shell
for p in $(snap list | awk '{print $1}'); do
  sudo snap remove $p
done
```
无法删除snapd,因为多版本
```Shell
snap list --all

sudo snap remove snapd --revision 13886

sudo apt autoremove --purge snapd
```
无法删除firefox[^1]
```Shell
sudo systemctl stop var-snap-firefox-common-host\\x2dhunspell.mount
sudo systemctl disable var-snap-firefox-common-host\\x2dhunspell.mount
snap remove --purge firefox
```


（2）删除 Snap 的 Core 文件。
```Shell
sudo systemctl stop snapd
sudo systemctl disable --now snapd.socket

for m in /snap/core/*; do
   sudo umount $m
done
```

（3）删除 Snap 的管理工具。
sudo apt autoremove --purge snapd
（4）删除 Snap 的目录。

```Shell
rm -rf ~/snap
sudo rm -rf /snap
sudo rm -rf /var/snap
sudo rm -rf /var/lib/snapd
sudo rm -rf /var/cache/snapd
```
（5）配置 APT 参数：禁止 apt 安装 snapd。([参看pt_preferences](https://manpages.ubuntu.com/manpages/focal/man5/apt_preferences.5.html))
```shell
sudo sh -c "cat > /etc/apt/preferences.d/no-snapd.pref" << EOL
Package: snapd
Pin: release a=*
Pin-Priority: -10
EOL
```
验证
```Shell
apt list snapd

sudo apt install snapd
```

禁用 snap Firefox 的更新（Server 版也可以配置）：
```Shell
sudo sh -c "cat > /etc/apt/preferences.d/no-firefox.pref" << EOL
Package: firefox
Pin: release a=*
Pin-Priority: -10
EOL
```
安装桌面环境
```Shell
sudo apt update
sudo apt install ubuntu-desktop
# or
sudo apt install ubuntu-desktop-minimal
# 安装 Gnome 软件商店
sudo apt install gnome-software

# 安装 DEB 格式的 Firefox
sudo add-apt-repository ppa:mozillateam/ppa

# 将 Firefox 官方 PPA 仓库中的 firefox 设为高优先级：
sudo sh -c "cat > /etc/apt/preferences.d/mozillateam-firefox.pref" << EOL
Package: firefox*
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 501
EOL

# 安装最新版的 deb 版 Firefox：
sudo apt update
apt list firefox  #现在已经不是 Snap firefox
sudo apt install firefox
# 或者 Firefox ESR
sudo apt install firefox-esr
```
### 恢复Snap 的方法
```Shell
sudo rm /etc/apt/preferences.d/no-snap.pref
sudo rm /etc/apt/preferences.d/no-firefox.pref
sudo rm /etc/apt/preferences.d/mozillateam-firefox.pref
sudo apt update
sudo snap install snap-store
sudo apt install firefox
```

## 参考

- [Completely remove firefox snap package](https://askubuntu.com/questions/1414173/completely-remove-firefox-snap-package)