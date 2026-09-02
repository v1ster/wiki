---
title: Linux 内核开发
date: 2023-10-31
categories:
  - embedded
tags:
  - kernel
---

* ## 查看linux 内核驱动

`cat /lib/modules/$(uname -r)/modules.builtin`

* ## linux 查看设备和驱动安装信息

* `lsmod` 命令可以列出当前系统中所有已经加载了的模块/驱动

* modinfo命令可以单看指定的模块/驱动的信息，其中alias指的是这个模块/驱动所支持的硬件的型号

* 使用modprobe或者insmod命令可以加载驱动，使用rmmod可以删除一个模块/驱动

* # Linux 内核管理

Linux 中所有的模块都存放在 /lib/modules/2.6.32-279.el6.i686/modules.dep 文件中，在安装模块时，依赖这个文件査找所有的模块，所以不需要指定模块所在位置的绝对路径，而且也依靠这个文件来解决模块的依赖性。

如果这个文件丢失了怎么办？不用担心，使用 depmod 命令会自动扫描系统中已有的模块，并生成 modules.dep 文件。命令格式如下：

```
[root@localhost ~]# depmod [选项]
#不加选项，depmod命令会扫描系统中的内核模块，并写入modules.dep文件

选项：

  -a：扫描所有模块；
  -A：扫描新模块，只有有新模块时，才会更新modules.dep文件；
  -n：把扫描结果不写入modules.dep文件，而是输出到屏幕上；
```

## 参考

[如何查看Linux 内核内置驱动](https://blog.csdn.net/dongshibo12/article/details/106921535)
[linux 查看设备信息和驱动](https://blog.csdn.net/gx19862005/article/details/48622767)
[Linux 内核模块管理(查看\添加和删除)](https://c.biancheng.net/view/1039.html)
