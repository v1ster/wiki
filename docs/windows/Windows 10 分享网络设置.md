---
title: Windows 10 分享网络设置
date: 2023-11-09
categories:
  - windows
tags:
  - windows
---

# windows

打开控制面板中的网络连接，切换到共享标签，将“允许其它网络用户通过此计算机的Internet连接来连接”，然后选择需要共享至的网卡。

选中之后，系统会将目标网卡的IP地址自动设置为“192.168.137.1”，这样服务端就配置好了。然后你需要在不能上网的客户机上，填入一个同网段的IP地址，如：192.168.137.10 掩码地址填写为：55.255.255.0 网关为：192.168.137.1，这样我们客户端就可以通过服务端的网络上网了。

值得注意的是，Windows在重新启动后，共享的设置虽然还在，但实际不能上网了，这应该是微软的一个bug。我们做如下处理：

使用Win + R快捷键调出运行窗口，输入regedit,打开注册表编辑器，依次定位到如下位置：

```text
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\SharedAccess
在空白处右击鼠标，新建"DWORD（32位）值（D），名称叫做"EnableRebootPersistConnection"，将数值数据改为1。
```

保存后重启计算机，下次重启就会自动开启连接了。

## 参考

* [快速的网络共享方法?](https://zhuanlan.zhihu.com/p/489160128)