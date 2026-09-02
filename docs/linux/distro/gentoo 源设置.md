---
title: gentoo 源设置
date: 2023-08-06
categories:
  - linux
tags:
  - linux
---

在`/etc/portage/make.conf` 中添加:
```
...

GENTOO_MIRRORS="https://mirrors.ustc.edu.cn/gentoo"

```


网易
	Portage: 已失效
	Distfiles: [http://mirrors.163.com/gentoo/](http://mirrors.163.com/gentoo/)

搜狐
	Portage: 不提供
	Distfiles: [http://mirrors.sohu.com/gentoo/](http://mirrors.sohu.com/gentoo/)

阿里云
	Portage：不提供
	Distfiles: [http://mirrors.aliyun.com/gentoo/](http://mirrors.aliyun.com/gentoo/)

[*]中国科学技术大学（USTC）
	Portage: [http://mirrors.ustc.edu.cn/gentoo/](http://mirrors.ustc.edu.cn/gentoo/)
	Distfiles: rsync://rsync.mirrors.ustc.edu.cn/gentoo-portage/

厦门大学
	Portage: 不提供
	Distfiles: [http://mirrors.xmu.edu.cn/gentoo/](http://mirrors.xmu.edu.cn/gentoo/)

日本北陆尖端科学技术大学院大学（JAIST）
	Portage: 不提供
	Distfiles: [http://ftp.iij.ad.jp/pub/linux/gentoo/](http://ftp.iij.ad.jp/pub/linux/gentoo/)

## 参考

- [国内真的是没多少用gentoo了吗？](https://bbs.archlinuxcn.org/viewtopic.php?id=4479)
