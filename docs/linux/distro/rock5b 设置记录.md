---
title: rock5b 设置记录
date: 2023-05-29
categories:
  - linux
tags:
  - linux
---

1. 设置用户自动登陆桌面
```Shell
sudo  vi  /etc/lightdm/lightdm.conf

---
#autologin-user=
+++
autologin-user=USER
```

2. 修改密码
```Shell
sudo su
passwd rock
```

3.  设置imx219 获取全分辨率
```Shell
media-ctl -d /dev/media0 --set-v4l2 '"m00_b_imx219 3-0010":0[fmt:SRGGB10_1X10/3280x2464]'

# media-ctl -d /dev/media0 --set-v4l2 '"rockchip-csi2-dphy0":0[fmt:SRGGB10_1X10/3280x2464]'

media-ctl -d /dev/media1 --set-v4l2 '"rkisp-isp-subdev":0[fmt:SRGGB10_1X10/3280x2464]'

media-ctl -d /dev/media1 --set-v4l2 '"rkisp-isp-subdev":2[fmt:SRGGB10_1X10/3280x2464]'

media-ctl -d /dev/media1 --set-v4l2 '"rkisp-isp-subdev":0[crop:(0,0)/3280x2464]'

media-ctl -d /dev/media1 --set-v4l2 '"rkisp-isp-subdev":2[crop:(0,0)/3280x2464]'
```

4. 查看拓扑结构
```Shell
media-ctl -p -d 0
```

5. 设置时间
```
sudo date -s "2023-08-17 14:22:00"
sudo hwclock -w
```

6. 设置网络

7. 配置source code
```Shell
git clone -b dev-rkr3.4 http://192.168.137.1:8080/test/rk3588-kernel.git kernel
git clone -b master https://github.com/radxa/rkbin.git rkbin
git clone -b dev http://192.168.137.1:808
0/rockchip/rk3588-build.git build
```

8. 设置git 代理
```Shell
git config --global http.https://github.com.proxy http://192.168.137.1:7890
```

## 参考

- [debian10怎么设置开机自动登录到桌面](https://t.rock-chips.com/forum.php?mod=viewthread&tid=1948)
- [debian系统之修改时间与时区](https://blog.51cto.com/zhujiangtao/1554976)