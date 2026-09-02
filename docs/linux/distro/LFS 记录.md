---
title: LFS 记录
date: 2025-08-31
categories:
  - linux
tags:
  - linux
---

# LFS 记录

#### 1) 看当前目录总大小（人类可读）

```bash
du -sh .
```

#### 备份

```Shell
tar -cJpf $HOME/lfs-temp-tools-12.3.tar.xz .
```

#### 还原

```
cd $LFS
rm -rf ./*
tar -xpf $HOME/lfs-temp-tools-12.3.tar.xz
```

####  Entering the Chroot Environment

```
sudo chroot "$LFS" /usr/bin/env -i   \
    HOME=/root                  \
    TERM="$TERM"                \
    PS1='(lfs chroot) \u:\w\$ ' \
    PATH=/usr/bin:/usr/sbin     \
    MAKEFLAGS="-j$(nproc)"      \
    TESTSUITEFLAGS="-j$(nproc)" \
    /bin/bash --login
```

#### Preparing Virtual Kernel File Systems
```
sudo mount -v --bind /dev $LFS/dev

sudo mount -vt devpts devpts -o gid=5,mode=0620 $LFS/dev/pts
sudo mount -vt proc proc $LFS/proc
sudo mount -vt sysfs sysfs $LFS/sys
sudo mount -vt tmpfs tmpfs $LFS/run

if [ -h $LFS/dev/shm ]; then
  sudo install -v -d -m 1777 $LFS$(realpath /dev/shm)
else
  sudo mount -vt tmpfs -o nosuid,nodev tmpfs $LFS/dev/shm
fi
```