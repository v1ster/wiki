---
title: linux 用户使用
date: 2023-06-19
categories:
  - linux
tags:
  - linux
---

### 查看用户组

```Shell
groups
rock sudo audio video
groups rock
rock : rock sudo audio video xrdp
```

添加用户追加到组

```shell
sudo usermod -a -G group user
```