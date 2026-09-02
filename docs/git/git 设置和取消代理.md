---
title: git 设置和取消代理
date: 2023-04-14
categories:
  - git
tags:
  - git
  - tool
---

```Shell
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy http://127.0.0.1:1080

git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'

git config --global --unset http.proxy
git config --global --unset https.proxy

#只对github.com
git config --global http.https://github.com.proxy http://192.168.137.1:7890
#取消代理
git config --global --unset http.https://github.com.proxy)
```


## 参考

1. [git设置和取消代理](https://gist.github.com/laispace/666dd7b27e9116faece6)