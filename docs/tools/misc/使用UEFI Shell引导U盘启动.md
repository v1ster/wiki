---
title: 使用UEFI Shell引导U盘启动
date: 2023-08-06
categories:
  - tools
tags:
  - tool
---

首先确认你的主板集成的UEFI自带Shell模式，一般开机时按F2即可进入Shell模式，或者在bios中选择引导，待出现”shell”提示符时即表明你已进入efi shell环境中。
此时我们可以尝试使用命令行手动加载启动文件，一般UEFI启动分区是硬盘最前端的FAT分区。因此首先我们要找到存放启动文件的分区，依次输入下列命令：

```Shell
fs0:（ufeshell使用fs:x方式表示驱动器，序号从0开始）fs_:(记得冒号)

ls（查看文件结构，确保其中有EFI目录，如果没有则重新选择其他fs驱动器）

cd EFI\Boot（进入引导目录，查看引导文件）

BOOTX64.efi（直接运行uefi可执行程序）
```

## 参考

- [使用UEFI Shell引导U盘启动](https://blog.csdn.net/asxcdfv/article/details/104950248)
