---
title: google chrome 强制启用 secure dns
date: 2026-04-07
tags:
  - windows
category:
  - windows
---
# google chrome 强制启用 secure dns

regedit 打开注册表

```
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome
新建
DnsOverHttpsMode REG_SZ secure
DnsOverHttpsTemplates REG_ZS https://dns.google/dns-query{?dns}
```

自定义DoH服务包括：

Cloudflare：https://1.1.1.1/dns-query

阿里巴巴：https://dns.alidns.com/dns-query

百度：https://dns.baidu.com/dns-query

360：https://doh.360.cn/dns-query

114DNS：https://doh.pub/dns-query

DNS 加密检测 :
	https://www.browserscan.net/zh/dns-leak
# 参考

- [如何在谷歌浏览器中启用安全DNS](https://chrome.xahuapu.net/help/534.html)
