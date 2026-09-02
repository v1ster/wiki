---
title: git diff 生成patch 并应用
date: 2023-04-14
categories:
  - git
tags:
  - git
  - tool
---

```Shell
git diff lwdev:ipa_c master > dev1201.patch

git apply --directory=ipa_c --stat  dev1201.patch
git apply --directory=ipa_c --check  dev1201.patch
git apply --directory=ipa_c dev1201.patch
```

###  修复尾随空白

``` Shell
git apply --reject --whitespace=fix  *.patch
```

### 通过commit 生成patch

``` Shell
 git format-patch 064c076cff2896e0a2bbb6af57415d74c055eff2 //HEAD~n commit
```