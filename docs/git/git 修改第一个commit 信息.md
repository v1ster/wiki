---
title: git 修改第一个commit 信息
date: 2023-08-22
categories:
  - git
tags:
  - git
  - tool
---

| 修改 commit 提交信息场景| 操作命令 |
|------------------------------|------------|
| 修改最新 commit 的提交信息| `git commit --amend`
| 修改某历史 commit 的提交信息 | `git rebase -i father_commitId` |
| 修改第一个 commit 的提交信息 | `git rebase -i --root` |

## 参考

[如何修改第一个 commit 的提交信息](https://www.jianshu.com/p/12c98eb74aaf)
