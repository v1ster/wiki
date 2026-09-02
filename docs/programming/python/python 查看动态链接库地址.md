---
title: python 查看动态链接库地址
date: 2023-04-28
categories:
  - programming
tags:
  - python
---

```shell
python3
>>>	import sys
# linux
>>>	sys.path
[''， '/usr/lib/python310.zip'， '/usr/lib/python3.10'， '/usr/Lib/python3.10/Lib-dynload'， '/usr/local/lib/python3.10/dist-packages'， '/usr/lib/python3/dist-packages']
# or windows
>>> sys.path
['D:\\Portable\\bin\\python-3.11.4-embed-amd64\\Lib\\site-packages', 'D:\\Portable\\bin\\python-3.11.4-embed-amd64\\python311.zip', 'D:\\Portable\\bin\\python-3.11.4-embed-amd64']
```
