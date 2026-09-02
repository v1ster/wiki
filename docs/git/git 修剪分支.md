---
title: git 修剪分支
date: 2023-04-19
categories:
  - git
tags:
  - git
  - tool
---

```Shell
# 修剪不存在 远程分支
git fetch --prune
# 查看远程仓库地址
git remote -v
# 删除远程分支
git push <remote> --delete <branch>
# 推送本地分支到远程
git checkout -b feature-branch
git push origin feature-branch:origin-branch
# 拉去远程分支到本地
git checkout -b feature-branch origin/feature-branch
```

