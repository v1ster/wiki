---
title: v2ray一键脚本收集整理
date: 2018-03-06
categories:
  - network
tags:
  - linux
  - proxy
---

> 本文主要收集网络上的v2ray脚本，该页面的脚本都经过本人验证使用没问题。

> 最后更新时间：2018-03-06


#### V2Ray 基于 Nginx 的 vmess+ws+tls 一键安装脚本
> from: [https://github.com/wulabing/V2Ray_ws-tls_bash_onekey](https://github.com/wulabing/V2Ray_ws-tls_bash_onekey)

##### 安装方式
```
git clone https://github.com/wulabing/V2Ray_ws-tls_bash_onekey.git temp && cd temp && bash install.sh | tee v2log.txt
```

##### V2ray core 更新方式
```
执行： bash <(curl -L -s https://install.direct/go.sh)
```

##### 启动方式
```
启动 V2ray：systemctl start v2ray
启动 Nginx：systemctl start nginx
```

---

#### V2RAY 基于 NGINX 的 VMESS+WS+TLS+Website(Use Host)

> from: [https://github.com/dylanbai8/V2Ray_ws-tls_Website_onekey](https://github.com/dylanbai8/V2Ray_ws-tls_Website_onekey)

```
bash <(curl https://raw.githubusercontent.com/dylanbai8/V2Ray_ws-tls_Website_onekey/master/install.sh)
```
尽量使用 Debian8 , 如果需要修改配置，运行脚本重新安装一次即可。


---
#### 最好用的 V2Ray 一键安装脚本 & 管理脚本

##### 安装
```
bash <(curl -s -L https://233blog.com/v2ray.sh)
```

##### 快速管理
```
v2ray info 查看 V2Ray 配置信息
v2ray config 修改 V2Ray 配置
v2ray link 生成 V2Ray 配置文件链接
v2ray infolink 生成 V2Ray 配置信息链接
v2ray qr 生成 V2Ray 配置二维码链接
v2ray ss 修改 Shadowsocks 配置
v2ray ssinfo 查看 Shadowsocks 配置信息
v2ray ssqr 生成 Shadowsocks 配置二维码链接
v2ray status 查看 V2Ray 运行状态
v2ray start 启动 V2Ray
v2ray stop 停止 V2Ray
v2ray restart 重启 V2Ray
v2ray log 查看 V2Ray 运行日志
v2ray update 更新 V2Ray
v2ray update.sh 更新 V2Ray 管理脚本
v2ray uninstall 卸载 V2Ray
```

##### 配置文件路径

> from： [https://233blog.com/post/16](https://233blog.com/post/16)

```
V2Ray 配置文件路径：/etc/v2ray/config.json
Caddy 配置文件路径：/etc/caddy/Caddyfile
脚本配置文件路径: /etc/v2ray/233blog_v2ray_backup.txt
```

##### 备注

V2Ray 客户端配置文件解压密码为 233blog.com，SOCKS 监听端口为 2333， HTTP 监听端口为 6666
可能某些 V2Ray 客户端的选项或描述略有不同，但事实上，此脚本显示的 V2Ray 配置信息已经足够详细，由于客户端的不同，请对号入座。

## 参考

-  [v2ray一键脚本收集整理](https://github.com/sharkyzh/MyBlogResources/blob/2088fcb923e93f5e50a58f0da854fe09965be4d4/source/_posts/v2ray%E4%B8%80%E9%94%AE%E8%84%9A%E6%9C%AC%E6%94%B6%E9%9B%86%E6%95%B4%E7%90%86.md)