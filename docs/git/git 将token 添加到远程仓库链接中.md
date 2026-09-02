---
title: git 将token 添加到远程仓库链接中
date: 2023-04-19
categories:
  - git
tags:
  - git
  - tool
---

将token 添加到远程仓库链接中

```Shell
git remote set-url origin https://<your_token>@github.com/<USERNAME>/<REPO>.git
```

-   `<your_token>`：换成你自己得到的token
-   `<USERNAME>`:是你自己github的用户名
-   `<REPO>`：是你的仓库名称

## 参考

- [Github使用基于令牌的身份验证](https://zhuanlan.zhihu.com/p/401978754)