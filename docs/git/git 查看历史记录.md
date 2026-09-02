---
title: git 查看历史记录
date: 2023-09-11
categories:
  - git
tags:
  - git
  - tool
---

```Shell
git log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
```

```Shell
git log --all --decorate --oneline --grap
```