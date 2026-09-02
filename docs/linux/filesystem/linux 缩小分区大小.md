---
title: linux 缩小分区大小
date: 2023-10-09
categories:
  - linux
tags:
  - filesystem
  - linux
---

重启到 `LiveCD`

```Shell
# 查看分区 或者使用 fdisk -l
lsblk
# 检查调整的分区
e2fsck -f /dev/sda1
# 分区调整到前100G空间
resize2fs /dev/sda1 100G
删除sda1 分区并重新新建sda1 分区为缩小后的大小,w保存
fdisk /dev/sda
# 再次检查分区
e2fsck -f /dev/sda1
```
## 参考

[无损调整EXT4分区大小](https://blog.pinkd.moe/linux/2018/01/31/resize-a-ext4-partiton-safely "无损调整EXT4分区大小")
[ 在终端下调整ext4文件系统的大小](https://blog.colorfulshark.net/2019/12/29/how-to-resize-ext4-filesystem.html)
[ProxmoxVE(PVE) 减小缩减虚拟机硬盘设置的空间大小](https://mayanpeng.cn/archives/158.html)
[Resize disks](https://pve.proxmox.com/wiki/Resize_disks)
