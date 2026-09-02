---
title: openocd 使用
date: 2024-11-03
categories:
  - embedded
tags:
  - hardware
  - linux
---

# openocd 使用

## 安装openocd 

```Shell
apt-get install libhidapi-dev libhidapi-libusb0  libgpiod-dev # CMSIS-DAP 必需要安装HIDAPI
apt install openocd
```

## CMSIS-DAP 连接

 - 查看 usb 信息

```Shell
$ lsusb  
[...]  
Bus 001 Device 007: ID 03eb:2111 Atmel Corp.  
[...]  
  
~$ lsusb -v -s 001:007 | grep "iSerial"  
iSerial 3 ATML1803040200001055
```

- 添加udev 规则

```Shell
 sudo vim /etc/udev/rules.d/49-cmsis-dap.rules <<EOF
SUBSYSTEMS=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2111", MODE:="0666", OWNER="user"
EOF
```

使用 CMSIS-DAP 连接MCU

```Shell
openocd -f interface/cmsis-dap.cfg -f target/stm32f1x.cfg

Open On-Chip Debugger 0.10.0
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
Info : auto-selecting first available session transport "swd". To override use 'transport select '.        
adapter speed: 1000 kHz
adapter_nsrst_delay: 100
none separate
cortex_m reset_config sysresetreq
Info : CMSIS-DAP: SWD  Supported
Info : CMSIS-DAP: Interface Initialised (SWD)
Info : CMSIS-DAP: FW Version = 2.2.1R
Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 0
Info : CMSIS-DAP: Interface ready
Info : clock speed 1000 kHz
Info : SWD DPIDR 0x1ba01477
Info : stm32f1x.cpu: hardware has 6 breakpoints, 4 watchpoints
Error: stm32f1x.cpu -- clearing lockup after double fault
Polling target stm32f1x.cpu failed, trying to reexamine
Info : stm32f1x.cpu: hardware has 6 breakpoints, 4 watchpoints
...
```

## 附录

- 更新udev,创建一个openocd 连接配置文件

```
~$ sudo udevadm trigger  
~$ cat atmel_sam4s_xplained_pro.cfg  
interface cmsis-dap  
cmsis_dap_vid_pid 0x03eb 0x2111  
cmsis_dap_serial ATML1803040200001055  
set CHIPNAME ATSAM4SD32C  
source [find board/atmel_sam4s_xplained_pro.cfg]  
  
~$ openocd -f atmel_sam4s_xplained_pro.cfg
```