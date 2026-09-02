---
title: linux 中使用 ctrl+z 停止任务后如何恢复任务
date: 2024-06-26
categories:
  - linux
tags:
  - linux
---

# linux 中使用 ctrl+z 停止任务后如何恢复任务

ctrl+z的作用是停止任务，要恢复停止的任务要使用fg命令

```Shell
[root@localhost ~]# jobs
[1]+  已停止               top
[root@localhost ~]# fg 1
```

fg [任务序号]，直接用fg命令，恢复的是最新停止的一条任务

## 参考

[ Linux中使用ctrl+z停止任务后如何恢复任务](https://blog.csdn.net/qq_40572277/article/details/104990616#:~:text=ctrl%2Bz%E7%9A%84%E4%BD%9C%E7%94%A8%E6%98%AF%E5%81%9C%E6%AD%A2%E4%BB%BB%E5%8A%A1%EF%BC%8C%E8%A6%81%E6%81%A2%E5%A4%8D%E5%81%9C%E6%AD%A2%E7%9A%84%E4%BB%BB%E5%8A%A1%E8%A6%81%E4%BD%BF%E7%94%A8fg%E5%91%BD%E4%BB%A4%20%5B%20root%40localhost%20~%5D%20%23%20jobs%20%5B%201,%5B%20root%40localhost%20~%5D%20%23%20fg%201%20fg%20%5B%E4%BB%BB%E5%8A%A1%E5%BA%8F%E5%8F%B7%5D%EF%BC%8C%E7%9B%B4%E6%8E%A5%E7%94%A8fg%E5%91%BD%E4%BB%A4%EF%BC%8C%E6%81%A2%E5%A4%8D%E7%9A%84%E6%98%AF%E6%9C%80%E6%96%B0%E5%81%9C%E6%AD%A2%E7%9A%84%E4%B8%80%E6%9D%A1%E4%BB%BB%E5%8A%A1)