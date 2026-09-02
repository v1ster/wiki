---
title: Yocoto 调试总结
date: 2025-04-25
categories:
  - embedded
tags:
  - linux
  - yocto
---

添加设备树编译, 修改文件 `sources/meta-nxp-harpoon/conf/layer.conf` 
```
KERNEL_DEVICETREE:append:imx8mm-lpddr4-evk = " \
                                              freescale/imx8mm-evk-harpoon.dtb \
                                              freescale/imx8mm-evk-harpoon-avb.dtb \
                                              freescale/imx8mm-evk-harpoon-industrial.dtb \
                                              freescale/imx8mm-evk-harpoon-virtio-net.dtb \
+++
                                              freescale/sdp-dante.dtb \
```

添加 defconfig 配置, 修改文件 `sources/meta-nxp-harpoon/recipes-kernel/linux/linux-imx_%.bbappend`
```
DELTA_KERNEL_DEFCONFIG:append:mx8mm-nxp-bsp = "imx_ch1_defconfig"
```

patch 文件生效, 修改文件  `sources/meta-nxp-harpoon/recipes-kernel/linux/linux-imx_%.bbappend`
patch 文件需要存储在 `sources/meta-nxp-harpoon/recipes-kernel/linux/files` 路径下
```
 `sources/meta-nxp-harpoon/recipes-kernel/linux/linux-imx_%.bbappend`
```

## 其他的一些常用命令
```Shell
# 获取源码
https://variwiki.com/index.php?title=Yocto_Customizing_U-Boot
bitbake -c unpack virtual/kernel
bitbake -c unpack virtual/bootloader
cp -a tmp/work/imx8mm_lpddr4_evk-poky-linux/u-boot-imx/2023.04/git/. ..local_repos/uboot-imx
cp -r tmp/work-shared/${MACHINE}/kernel-source ../local_repos/

# 还有一种方法，就是展开yocto扩展变量的值，可以通过检查bitbake -e命令的输出来检查变量的值 　
 
bitbake -e virtual/kernel | grep ^S=
　
# 如果您已经构建了主线版本，则可能需要使用以下方法重置构建目录
 
bitbake -c clean virtual/kernel virtual/bootloader
 
source setup-environment build
  
bitbake-layers  show-layers

bitbake-layers create-layer ../sources/meta-ch1

bitbake-layers add-layer ../sources/meta-ch1/

bitbake -c cleansstate # recipes

bitbake virtual/kernel

bitbake -c compile -f linux-imx

dtc -I dtb -O dts *.dtb > my.dts


export  CROSS_COMPILE=/home/dewey/workspace/platin-ch1/out/yinfan_huazhu-ch1/host/bin/aarch64-buildroot-linux-gnu-
export ARCH=arm64
make defconfig imx.config

export ARCH=arm64
export CROSS_COMPILE=aarch64-none-linux-gnu-
 make imx_v8_defconfig
 
# 使用 make modules_install INSTALL_MOD_PATH=<路径> , 如,
$ make modules_install INSTALL_MOD_PATH=/home/jello/kernel_modules

//获取当前内核配置
 zcat /proc/config.gz || cat /boot/{config,config-$(uname -r)}
```