---
title: c 预处理器
date: 2023-04-14
categories:
  - programming
tags:
  - c-cpp
  - cheatsheet
---

#### 内置宏

```C
#include <stdio.h>

main()
{
   printf("File :%s\n", __FILE__ );
   printf("Date :%s\n", __DATE__ );
   printf("Time :%s\n", __TIME__ );
   printf("Line :%d\n", __LINE__ );
   printf("ANSI :%d\n", __STDC__ );

}
```

## 参考

-  [c预处理器](https://www.runoob.com/cprogramming/c-preprocessors.html)
