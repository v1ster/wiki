---
title: git cherry-pick 代码片段
date: 2025-09-12
categories:
    - git
tags:
  - git
---

```bash
#!/usr/bin/env bash
# cherry-tag.sh  <tag>

set -euo pipefail

# ---------- 1. 参数检查 ----------
if [ $# -ne 1 ]; then
  echo "用法: $0 <tag>"
  exit 1
fi
TAG=$1

# 判断是否为本地已存在的 tag
if ! git rev-parse --verify "refs/tags/$TAG" >/dev/null 2>&1; then
  echo "错误: '$TAG' 不是当前仓库的有效 tag"
  exit 2
fi

COMMIT=$(git rev-parse "refs/tags/$TAG")

# ---------- 2. cherry-pick（冲突时自动取 incoming） ----------
git cherry-pick -X theirs "$COMMIT"

# ---------- 3. 删除 diff 出来的文件 ----------
# 比较 tag 与当前 HEAD 的差异文件（tag→HEAD）
git diff --name-only "$COMMIT" HEAD | xargs -r -d '\n' rm -v

# ---------- 4. 把删完后的状态并入刚才的 cherry-pick 提交 ----------
git add -A .
git commit --amend --no-edit

# ---------- 5. 在当前新提交上重新打 tag ----------
# 若同名 tag 已存在则强制移动
git tag -f "v$TAG" HEAD

echo "完成：已拣选提交、清理文件、修正提交并移动 tag '$TAG' 到最新提交。"

```