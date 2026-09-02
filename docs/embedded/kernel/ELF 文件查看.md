---
title: ELF 文件查看
date: 2025-04-25
categories:
  - embedded
tags:
  - kernel
  - linux
---

# ELF 文件查看 

(1) file：判断文件类型

```
$ file /bin/ls
```

(2) readelf：查看ELF文件的所有信息

```
$ readelf -a /bin/ls  # 显示全部信息
```

(3) objdump：反汇编 ELF 文件

```
$ objdump -d /bin/ls  # 反汇编代码段
```

(4) nm：列出符号表

```
$ nm /bin/ls  # 显示符号（函数、变量）
```

(5) ldd：查看动态依赖

```
$ ldd /bin/ls  # 显示依赖的共享库
```

(6) strings：提取文件中的字符串

```
$ strings /bin/ls | grep"GNU"# 查找包含"GNU"的字符串
```

(7) strip：移除ELF文件中的符号表和调试信息

```
$ strip -s program  # 减小文件体积
```

(8) patchelf：修改 ELF 文件的属性

```
$ patchelf --set-interpreter /lib64/ld-custom.so program  # 修改解释器
```

# 参考

[五分钟彻底搞懂 Linux ELF 文件](https://mp.weixin.qq.com/s/Rz44RG9NQJeaIh71ZC3cvA)
