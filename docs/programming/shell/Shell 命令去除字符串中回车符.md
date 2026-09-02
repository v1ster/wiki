---
title: Shell 命令去除字符串中回车符
date: 2025-01-11
categories:
  - programming
tags:
  - linux
  - shell
---

# Shell 命令去除字符串中回车符

在 Shell 中，你可以使用 `tr` 或 `sed` 命令来去除字符串中的 `'\r'` 字符。以下是两种方法的示例：

### 使用 `tr` 命令

```bash
echo -e "Hello\rWorld\r!" | tr -d '\r'
```

### 使用 `sed` 命令

```bash
echo -e "Hello\rWorld\r!" | sed 's/\r//g'
```


这两种方法都会输出：

```code
HelloWorld!
```

你可以将 `echo -e "Hello \r World \r!"` 替换为你实际的字符串或文件内容。
