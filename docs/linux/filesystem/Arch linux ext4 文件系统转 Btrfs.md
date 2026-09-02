---
title: Arch linux ext4 文件系统转 Btrfs
date: 2024-04-14
categories:
  - linux
tags:
  - filesystem
  - linux
---

# ext4 文件系统转为 Btrfs

> 注意所有操作在LiveCD 环境下进行操作

1. 检查文件系统保证现有分区没有问题
```Shell
fsck.ext4 /dev/nvme0n1p3
```
2. 文件系统转换
```Shell
btrfs-convert /dev/nvme0n1p3
```
3. 挂载分区并修改fstab
```Shell
mount /dev/nvme0n1p3 /mnt
mount /dev/nvme0n1p4 /mnt/home
mount /dev/nvme0n1p1 /mnt/boot
sweapon /dev/nvme0n1p2

mount -t proc none /mnt/proc
mount -t sysfs none /mnt/sys
mount -o bind /dev /mnt/dev

genfstab -U /mnt > /mnt/etc/fstab

```
4. 使用 `pacstrap` 脚本安装基础包：
```Shell

arch-chroot /mnt
pacstrap /mnt base base-devel linux linux-firmware btrfs-progs
# 如果使用btrfs文件系统，额外安装一个btrfs-progs包
pacstrap /mnt networkmanager vim sudo zsh zsh-completions

mkinitcpio -P

exit
```
5. 启用透明压缩
```Shell
btrfs filesystem defragment -r -v -czstd /mnt
```
6. 使用balance 来回收数据
```Shell
btrfs subvolume delete /mnt/ext2_saved
btrfs balance start /mnt
btrfs balance status /mnt
```
# 根目录文件迁移到子卷

1. 创建子卷
```Shell
sudo btrfs subvolume create /mnt/@
sudo btrfs subvolume create /mnt/@home
sudo btrfs subvol list /mnt
ID 256 gen 3500 top level 5 path @
ID 258 gen 3500 top level 5 path @home
```
2. 同步子区文件
```Shell
rsync -a /mnt /mnt/@
rsync -a /mnt/home /mnt/@home
```
3. 挂载分区并修改fstab
> 这里要注意重新挂载其他的分区
```Shell
mount -t btrfs -o subvol=/@,compress=zstd /dev//dev/nvme0n1p3 /mnt
mount -t btrfs -o subvol=/@home,compress=zstd /dev//dev/nvme0n1p3 /mnt/home

genfstab -U /mnt > /mnt/etc/fstab
```
4. 修改systemd-boot 引导
```Shell
sudo blkid -p /dev/nvme0n1p3

ls /dev/disk/by-partuuid -la
total 0
drwxr-xr-x 2 root root 160 Apr 14 16:07 .
drwxr-xr-x 8 root root 160 Apr 14 16:07 ..
lrwxrwxrwx 1 root root  15 Apr 14 16:07 1f52178e-ace5-43c8-a25a-666b6975533a -> ../../nvme1n1p2
lrwxrwxrwx 1 root root  15 Apr 14 16:07 73d99787-e061-4aef-a610-278463f96cf6 -> ../../nvme0n1p3
lrwxrwxrwx 1 root root  15 Apr 14 16:07 99ef2922-a9df-49e1-a193-d48b7fc9a40a -> ../../nvme0n1p2
lrwxrwxrwx 1 root root  15 Apr 14 16:07 b339edf8-ea40-459e-b26d-dd70d49064b4 -> ../../nvme1n1p3
lrwxrwxrwx 1 root root  15 Apr 14 16:07 be3bb32f-6193-472d-be7d-1a4f9f5d682e -> ../../nvme0n1p1
lrwxrwxrwx 1 root root  15 Apr 14 16:07 c84bac03-8a3a-4f9e-a121-3a00d9187be3 -> ../../nvme1n1p1

vim /boot/loader/entries/arch.conf  
title   Arch Linux
linux   /vmlinuz-linux
initrd  /amd-ucode.img
initrd  /initramfs-linux.img
options root=PARTUUID=73d99787-e061-4aef-a610-278463f96cf6 rw rootflags=subvol=/@
```

# 修改分区大小
```Shell
[mars@mapc ~]$ sudo fdisk /dev/nvme0n1               

Welcome to fdisk (util-linux 2.40).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.


Command (m for help): e
Partition number (1-3, default 3):  

New <size>{K,M,G,T,P} in bytes or <size>S in sectors (default 915G):  

Partition 3 has been resized.

Command (m for help): w
The partition table has been altered.
Syncing disks.
[mars@mapc ~]$ df -h                   
Filesystem      Size  Used Avail Use% Mounted on
dev             7.5G     0  7.5G   0% /dev
run             7.5G  1.9M  7.5G   1% /run
efivarfs        148K  126K   18K  88% /sys/firmware/efi/efivars
/dev/nvme0n1p3  512G   40G  471G   8% /
tmpfs           7.5G  169M  7.4G   3% /dev/shm
/dev/nvme0n1p3  512G   40G  471G   8% /home
/dev/nvme0n1p1  511M  297M  215M  59% /boot
tmpfs           7.5G   29M  7.5G   1% /tmp
tmpfs           1.5G   76K  1.5G   1% /run/user/1000
/dev/nvme0n1p3  512G   40G  471G   8% /mnt
[mars@mapc ~]$ sudo btrfs filesystem resize max /mnt
Resize device id 1 (/dev/nvme0n1p3) from 512.00GiB to max
[mars@mapc ~]$ df -h                                 
Filesystem      Size  Used Avail Use% Mounted on
dev             7.5G     0  7.5G   0% /dev
run             7.5G  1.9M  7.5G   1% /run
efivarfs        148K  126K   18K  88% /sys/firmware/efi/efivars
/dev/nvme0n1p3  916G   40G  874G   5% /
tmpfs           7.5G  169M  7.4G   3% /dev/shm
/dev/nvme0n1p3  916G   40G  874G   5% /home
/dev/nvme0n1p1  511M  297M  215M  59% /boot
tmpfs           7.5G   29M  7.5G   1% /tmp
tmpfs           1.5G   76K  1.5G   1% /run/user/1000
/dev/nvme0n1p3  916G   40G  874G   5% /mnt
```

## 参考

[Btrfs：认识、从 Ext4 迁移与快照方案](https://blog.kaaass.net/archives/1748)
[archlinux 基础安装​](https://arch.icekylin.online/guide/rookie/basic-install#archlinux-%E5%9F%BA%E7%A1%80%E5%AE%89%E8%A3%85)
[TLP](https://wiki.archlinux.org/title/TLP)
[将 Arch Linux 内核从 stable 更换为 LTS 的办法与案例](https://zhuanlan.zhihu.com/p/385843857)
[Kernel](https://wiki.archlinux.org/title/Kernel)
[Linux ext4 文件系统转 Btrfs](https://blog.samchu.cn/posts/linux-ext4-to-btrfs/)