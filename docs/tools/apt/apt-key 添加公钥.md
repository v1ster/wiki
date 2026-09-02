---
title: apt-key 添加公钥
date: 2023-04-14
categories:
  - tools
tags:
  - apt
  - tool
---

检索 key 并添加 key :
```Shell
curl -s URL | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/NAME.gpg --import

cat URL.pub | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/NAME.gpg --import

apt-key export BE1229CF|sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/microsoft.gpg
```

授权用户 _apt :
```Shell
sudo chown _apt /etc/apt/trusted.gpg.d/NAME.gpg
```

## 参考

1. [linux-警告:apt-key is deprecated.](https://www.coder.work/article/7771966)
2. [Warning: apt-key is deprecated (SOLVED)](https://suay.site/?p=526)