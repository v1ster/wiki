---
title: repo 初始化仓库
date: 2024-08-13
categories:
  - embedded
tags:
  - buildroot
  - linux
---

# repo 拉取仓库

```Shell
repo init --repo-url=ssh://gerrit/tools/python2-repo -u ssh://gerrit/xpert/platform/manifest -m platin-ch-1.xml
```

### 同步仓库
```Shell
repo sync --force-sync
```


