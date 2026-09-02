---
title: 查看python所支持的wheel包
date: 2023-08-03
categories:
  - tools
tags:
  - tool
---

``` shell
pi@testpi2:~ $ python
Python 3.9.2 (default, Mar 12 2021, 04:06:34)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pip._internal.utils.compatibility_tags import get_supported
>>> print(get_supported())
[<cp39-cp39-linux_armv6l @ 3058276136>, <cp39-abi3-linux_armv6l @ 3058276200>, <cp39-none-linux_armv6l @ 3058276552>, <cp38-abi3-linux_armv6l @ 3058275912>, <cp37-abi3-linux_armv6l @ 3058276648>, <cp36-abi3-linux_armv6l @ 3058276712>, <cp35-abi3-linux_armv6l @ 3058276808>, <cp34-abi3-linux_armv6l @ 3058276904>, <cp33-abi3-linux_armv6l @ 3058277000>, <cp32-abi3-linux_armv6l @ 3058277096>, <py39-none-linux_armv6l @ 3058277320>, <py3-none-linux_armv6l @ 3058275976>, <py38-none-linux_armv6l @ 3058277352>, <py37-none-linux_armv6l @ 3058277480>, <py36-none-linux_armv6l @ 3058277544>, <py35-none-linux_armv6l @ 3058277640>, <py34-none-linux_armv6l @ 3058277736>, <py33-none-linux_armv6l @ 3058277832>, <py32-none-linux_armv6l @ 3058277928>, <py31-none-linux_armv6l @ 3058278024>, <py30-none-linux_armv6l @ 3058278120>, <cp39-none-any @ 3058278312>, <py39-none-any @ 3058278216>, <py3-none-any @ 3058315368>, <py38-none-any @ 3058315528>, <py37-none-any @ 3058315624>, <py36-none-any @ 3058315752>, <py35-none-any @ 3058315880>, <py34-none-any @ 3058316008>, <py33-none-any @ 3058316136>, <py32-none-any @ 3058316264>, <py31-none-any @ 3058316392>, <py30-none-any @ 3058316520>]
>>>
```


## 参考

- [python的wheel](https://www.cnblogs.com/chenyujie/p/16722641.html)
