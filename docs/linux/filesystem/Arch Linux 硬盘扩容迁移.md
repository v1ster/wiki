---
title: Arch Linux 硬盘扩容
date: 2024-02-25
categories:
  - linux
tags:
  - filesystem
  - linux
---

正常分区后,使用rsync 同步分区内容

```Shell
rsync -a /src/* /dst/*
```

windows 引导丢失,使用命令重建
```CMD

diskpart
list disk
select disk *     // 选择你要重建EFI分区的盘的编号，以数字代替*
list partition
create partition efi size = 260     // 260M，分配给EFI分区的容量format quick fs = fat32
exit
bcdboot C:\Windows                  // 注意盘符

```

arch linux 引导丢失.重建
在 archiso 环境中
```shell
mount /dev/_root_partition /mnt
mount --mkdir /dev/_efi_system_partition /mnt/boot
swapon /dev/_swap_partition

pacstrap -K /mnt base linux-lts nvid linux-firmware amd-ucode

genfstab -U /mnt >> /mnt/etc/fstab
rch-chroot /mnt
mkinitcpio -P

bootctl --esp-path=/boot --boot-path=/boot install
```

The loader configuration is stored in the file `_esp_/loader/loader.conf`. See [loader.conf(5) § OPTIONS](https://man.archlinux.org/man/loader.conf.5#OPTIONS) for details.
```
_esp_/loader/loader.conf

default  arch.conf
timeout  4
console-mode max
editor   no
```

```
_esp_/loader/entries/arch.conf

title   Arch Linux
linux   /vmlinuz-linux
initrd  /intel-ucode.img
initrd  /initramfs-linux.img
options root=UUID=_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx_ rw
```

## 参考

- # [迁移linux系统到新硬盘](https://zhuanlan.zhihu.com/p/33341983?#)
- # [Windows下误删EFI分区重建引导简单教程](https://blog.csdn.net/Rookie_tong/article/details/84455527#:~:text=%E9%87%8D%E5%BB%BAEFI%E5%88%86%E5%8C%BA%EF%BC%8C%E9%A6%96%E5%85%88%E9%9C%80%E8%A6%81%E4%B8%80%E4%B8%AAU%E7%9B%98%E3%80%82%20%E7%94%A8%E4%BA%8E%E5%88%B6%E4%BD%9CPE%E7%B3%BB%E7%BB%9F%E7%9B%98%EF%BC%8C%E4%BD%BF%E7%94%A8%E8%80%81%E6%AF%9B%E6%A1%83%E5%88%B6%E4%BD%9C%E5%8D%B3%E5%8F%AF%E3%80%82%20%E4%BD%BF%E7%94%A8PE%E7%B3%BB%E7%BB%9F%E7%9B%98%E8%BF%9B%E5%85%A5%E7%B3%BB%E7%BB%9F%EF%BC%8C%E6%89%93%E5%BC%80%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%95%8C%E9%9D%A2%EF%BC%8C%E5%A6%82%E6%9E%9CEFI%E5%88%86%E5%8C%BA%E8%BF%98%E5%9C%A8%E7%9A%84%E8%AF%9D%EF%BC%8C%E7%9B%B4%E6%8E%A5%E4%BD%BF%E7%94%A8%E5%A6%82%E4%B8%8B%E5%91%BD%E4%BB%A4%E5%8D%B3%E5%8F%AF%EF%BC%8C%E5%85%B6%E4%B8%AD)
- # [systemd-boot](https://wiki.archlinux.org/title/Systemd-boot)
- # [Installation](https://wiki.archlinux.org/title/installation_guide)
