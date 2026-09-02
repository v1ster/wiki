---
title: windows 中添加右键菜单 - 在vscode 中打开
date: 2024-01-04
categories:
  - windows
tags:
  - tool
---

1. `win+r` 输入regedit, 打开注册表
2. 打开文件夹, 找到 `HKEY_CLASSES_ROOT\Directory\shell` 目录
	1. 右键Shell 新建vscode 目录, 新建 -> 项
	2. 修改 default 值 -> `vscode 中打开` , 该项为右键菜单名
	3. 添加图标,新建 -> 字符串值, 数值名称 Icon, 数值数据  `"C:\Program Files\VSCodium\VSCodium.exe"` 
	5. 新建command 目录, 新建-> 项
	6. 修改command 目录默认值, `"C:\Program Files\VSCodium\VSCodium.exe" "%1"` 
3.  打开文件, 找到 `HKEY_CLASSES_ROOT\*\shell` 目录, 操作同上