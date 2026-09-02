---
title: git 合并commit
date: 2023-04-19
categories:
  - git
tags:
  - git
  - tool
---

```Shell
# 使用rebase 操作来合并commit
git rebase -i <after-this-commit>
# 从HEAD版本开始往过去数3个版本
git rebase -i HEAD~3
# 输入rebase命令之后会打开一个编辑器 参考下面来修改文本:
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
#         create a merge commit using the original merge commit's
#         message (or the oneline, if no original merge commit was
#         specified); use -c <commit> to reword the commit message
# u, update-ref <ref> = track a placeholder for the <ref> to be updated
#                       to this position in the new commits. The <ref> is
#                       updated at the end of the rebase
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.

# 推荐使用fixup 合并commit 和使用reword 来修改提交信息
```

## 参考

-   [Git-rebase-合并多个commit](https://swumao.github.io/swumao/update/git/rebase/pick/edit/reword/drop/squash/fixup/2016/08/31/Git-rebase-%E5%90%88%E5%B9%B6%E5%A4%9A%E4%B8%AAcommit.html)
-   [Git 合并多个 commit，保持历史简洁](https://cloud.tencent.com/developer/article/1690638)