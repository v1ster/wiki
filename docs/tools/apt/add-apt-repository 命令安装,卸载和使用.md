---
title: add-apt-repository 命令安装,卸载和使用
date: 2023-04-25
categories:
  - tools
tags:
  - apt
  - tool
---

### 安装

```shell
sudo:  add-apt-repository: command not found

sudo apt install software-properties-common
```

### 使用

```shell
sudo add-apt-repositry ppa:xxxxxxx
```

#### 移除不用的PPA

1. 使用software & update 移除
software & updates -> other software -> 选择PPA 仓库点击remove
2. 使用Terminal 删除
```shell
# 通常我们使用以下指令加入PPA :
sudo add-apt-repository "PPA_YOU_NEED"
# 要删除只需要后方接上remove 参数:
sudo add-apt-repository --remove "PPA_YOU_NEED"

# 手动删除PPA
# 首先显示安装的PPA
sudo ls /etc/apt/sources.list.d/ -l
总计 12
-rw-r--r-- 1 root root 154  4月 25 21:02 apandada1-ubuntu-foliate-jammy.list
-rw-r--r-- 1 root root 190  4月 25 21:02 google-chrome.list
-rw-r--r-- 1 root root 203  4月 25 21:02 vscode.list
# 删除foliate
sudo rm etc/apt/sources.list.d/apandada1-ubuntu-foliate-jammy.list
```
3.  使用ppa-purge 删除PPA和软件
```shell
# 安装ppa-purge
sudo apt install ppa-purge
# 使用ppa-purge 删除
sudo ppa-purge "PPA_YOU_WANT_TO_REMOVE"
# PPA url 可以通过software & updates -> other software 查看
# 使用例子
sudo ppa-purge http://ppa.launchpad.net/nginx/stable/ubuntu
```

## 参考

- [如何移除不要的 PPA 倉庫](https://clay-atlas.com/blog/2021/05/29/linux-cn-add-apt-repository-command-not-found/)
- [add-apt-repository: command not found](https://clay-atlas.com/blog/2021/05/29/linux-cn-add-apt-repository-command-not-found/)
- [如何在Ubuntu/Debian中添加Apt仓库](https://www.myfreax.com/how-to-add-apt-repository-in-ubuntu/)