---
title: git 修改配置文件
date: 2023-04-14
categories:
  - git
tags:
  - git
  - tool
---

```Shell
# 查看git配置
git config --list --show-origin

# 编辑配置
git config --global --edit

# 添加配置
[core]
	editor = code --wait  --new-window
	# editor = nano -w
[diff]
    tool = vscode-diff
[difftool]
    prompt = false
[difftool "vscode-diff"]
    cmd = code --wait --diff $LOCAL $REMOTE
[merge]
    tool = vscode-merge
[mergetool "vscode-merge"]
    cmd = code --wait $MERGED
```

## 参考

-  [Git查看和编辑配置并设置默认编辑器为VSCode](https://blog.csdn.net/subtitle_/article/details/127832897?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EAD_ESQUERY%7Eyljh-1-127832897-blog-57966303.pc_relevant_landingrelevant&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EAD_ESQUERY%7Eyljh-1-127832897-blog-57966303.pc_relevant_landingrelevant&utm_relevant_index=2)
- [A3.1 Appendix C: Git Commands - Setup and Config](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config)
