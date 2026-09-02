---
title: 手把手解析ELF文件格式：从Hello World到二进制奥秘
date: 2025-04-25
categories:
  - embedded
tags:
  - kernel
  - linux
---

# 手把手解析ELF文件格式：从Hello World到二进制奥秘

大伙应该都知道无论是Linux下的可执行程序，还是共享库（`.so`）、核心转储文件（`core`），它们的底层格式都是 ELF（Executable and Linkable Format）。理解ELF文件，能让你获得哪些能力呢？我想应该有如下几点  
  

• 逆向分析：破解程序逻辑，分析恶意代码。

• 调试定位：通过崩溃的core文件快速定位问题。

• 性能优化：分析内存布局和函数调用关系。

  

本文将以一个包含 全局变量、局部变量、字符串常量 的“Hello World”程序为例，生成ELF文件，并逐字节解析其结构！

**第一步：生成示例ELF文件**  
  

我们编写一个包含多种数据类型的程序，确保生成丰富的ELF段（section）。

**1. 示例代码**

```
// hello_elf.c#include <stdio.h>int global_init = 42;           // 初始化的全局变量（.data段）int global_uninit;              // 未初始化的全局变量（.bss段）constchar *str = "Hello ELF!"; // 字符串常量（.rodata段）int main() {    int local_var = 100;        // 局部变量（栈中，ELF不直接存储）    staticint static_var = 0;  // 静态变量（.data或.bss段）    printf("%s\n", str);    return0;}
```

**2. 编译生成ELF文件**

```
gcc -g -no-pie hello_elf.c -o hello_elf  # -g生成调试信息，-no-pie禁用地址随机化
```

**第二步：ELF文件全景速览**  
  

使用工具快速查看ELF文件结构：

```
file hello_elf               # 查看文件类型readelf -h hello_elf         # 查看ELF头readelf -l hello_elf         # 查看程序头表（加载信息）readelf -S hello_elf         # 查看节头表（段信息）objdump -d hello_elf         # 反汇编代码段
```

**第三步：逐字节解析ELF文件结构**  
  

我们将从二进制层面解析ELF文件，重点关注以下部分：

1. ELF头（ELF Header）
    
2. 程序头表（Program Header Table）
    
3. 代码段（.text）
    
4. 数据段（.data、.bss、.rodata）
    
5. 符号表（.symtab）
    
6. 调试信息（.debug_*）
    

---

**1. ELF头（ELF Header）**  
  

ELF头位于文件起始位置（0x0~0x40字节），描述文件基本信息。

```
hexdump -C hello_elf -n 64  # 查看ELF头（前64字节）
```

输出示例：

```
00000000  7f 45 4c 46 02 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|00000010  02 00 3e 00 01 00 00 00  a0 04 40 00 00 00 00 00  |..>.......@.....|00000020  40 00 00 00 00 00 00 00  10 3e 00 00 00 00 00 00  |@........>......|00000030  00 00 00 00 40 00 38 00  09 00 40 00 1f 00 1c 00  |....@.8...@.....|
```

  

关键字段解析：  
• Magic：`7F 45 4C 46`（`0x7F`+`ELF`）。

• Class：`02`表示64位文件。

• Type：`01 00`（`0x0001`）表示可执行文件（`ET_EXEC`）。

• Machine：`3e 00`（`0x003e`）表示x86-64架构。

• Entry point：`a0 04 40 00`（`0x4004a0`），程序入口地址。

• Start of program headers：`40 00`（`0x40`），程序头表起始位置。

---

**2. 程序头表（Program Header Table）**  
  

程序头表指导操作系统如何加载程序到内存。

```
readelf -l hello_elf
```

输出示例：

```
Program Headers:  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align  LOAD           0x000000 0x0000000000400000 0x0000000000400000 0x0006b4 0x0006b4 R E 0x200000  LOAD           0x000e00 0x0000000000600e00 0x0000000000600e00 0x000228 0x000230 RW  0x200000  DYNAMIC        0x000e18 0x0000000000600e18 0x0000000000600e18 0x0001d0 0x0001d0 RW  0x8
```

• LOAD段：

• 第一个`LOAD`段为代码段（`.text`），权限`R E`（可读可执行）。

• 第二个`LOAD`段为数据段（`.data`、`.bss`），权限`RW`（可读可写）。

---

**3. 代码段（.text）**  
  

代码段存放可执行指令，对应`main`函数和库函数调用。

```
objdump -d hello_elf
```

反汇编输出：

```
00000000004004a0 <main>:  4004a0:   55                      push   %rbp  4004a1:   48 89 e5                mov    %rsp,%rbp  4004a4:   48 83 ec 10             sub    $0x10,%rsp  4004a8:   c7 45 fc 64 00 00 00    movl   $0x64,-0x4(%rbp)  # local_var=100  4004af:   48 8b 05 6a 0b 20 00    mov    0x200b6a(%rip),%rax # 601020 <str>  4004b6:   48 89 c7                mov    %rax,%rdi  4004b9:   e8 92 fe ff ff          call   400350 <puts@plt>  4004be:   b8 00 00 00 00          mov    $0x0,%eax  4004c3:   c9                      leave    4004c4:   c3                      ret    
```

• 机器码：如`55 48 89 e5`对应`push %rbp; mov %rsp, %rbp`。

• 函数调用：`call 400350`跳转到`puts@plt`（动态链接库函数）。

---

**4. 数据段（.data、.bss、.rodata）**  

**（1）.data段**  
存储已初始化的全局变量和静态变量。

```
readelf -x .data hello_elf  # 查看.data段
```

输出示例：

```
Hex dump of section '.data':  0x00601020 00000000 00000000 20064000 00000000 ........ .@.....  0x00601030 2a000000                             *...            
```

• `0x2a`（十进制42）对应`global_init = 42`。

• `0x20064000`是字符串`"Hello ELF!"`的地址（在.rodata段）。

**（2）.rodata段**  
存储只读数据（如字符串常量）。

```
readelf -x .rodata hello_elf
```

输出示例：

```
Hex dump of section '.rodata':  0x004005e0 01000200 48656c6c 6f20454c 462100    ....Hello ELF!.
```

• 字符串`"Hello ELF!"`以ASCII形式存储。

**（3）.bss段**  
存储未初始化的全局变量（程序加载时初始化为0）。

```
readelf -x .bss hello_elf
```

输出示例：

```
Hex dump of section '.bss':  0x00601038 00000000 00000000                   ........        
```

• `global_uninit`在此段，初始值为0。

---

**5. 符号表（.symtab）**  
  

记录函数和变量的地址和类型。

```
readelf -s hello_elf
```

输出示例：

```
Symbol table '.symtab' contains 64 entries:   Num:    Value          Size Type    Bind   Vis      Ndx Name     1: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS hello_elf.c     8: 0000000000601038     4 OBJECT  GLOBAL DEFAULT   23 global_uninit     9: 0000000000601020     8 OBJECT  GLOBAL DEFAULT   21 str    10: 0000000000601028     4 OBJECT  GLOBAL DEFAULT   21 global_init    15: 00000000004004a0    37 FUNC    GLOBAL DEFAULT   13 main
```

• `main`函数地址为`0x4004a0`。

• `str`变量地址为`0x601020`，对应.rodata段的字符串地址。

---

**6. 调试信息（.debug_*）**  
  

编译时添加`-g`选项会生成调试信息，用于关联源代码和二进制指令。

```
readelf -S hello_elf | grep debug  # 查看调试段
```

输出示例：

```
  [27] .debug_aranges    PROGBITS        0000000000000000 000010a0  [28] .debug_info       PROGBITS        0000000000000000 000010d0  [29] .debug_abbrev     PROGBITS        0000000000000000 000013a0
```

• .debug_info：记录变量类型、函数参数等源码级信息。

---

**第四步：动手实验——修改ELF文件**  
  

通过修改ELF文件，直观感受其结构：

1. 修改字符串常量：
    
    ```
    printf "Hello HACK!" | dd of=hello_elf bs=1 seek=$((0x4005e4)) conv=notrunc
    ```
    
    运行程序，输出将变为`Hello HACK!`。
    
2. 修改全局变量：
    
    ```
    printf "\x2b\x00\x00\x00" | dd of=hello_elf bs=1 seek=$((0x601028)) conv=notrunc
    ```
    
    `global_init`的值从42（0x2a）变为43（0x2b）。
    

---

**第五步：ELF文件结构总结**

|结构|作用|
|---|---|
|ELF头|标识文件类型、架构、入口点、程序头表位置。|
|程序头表|指导操作系统加载段到内存。|
|.text段|存储可执行指令（如`main`函数）。|
|.data段|存储已初始化的全局变量和静态变量。|
|.bss段|存储未初始化的全局变量（程序加载时初始化为0）。|
|.rodata段|存储只读数据（如字符串常量）。|
|.symtab段|符号表，记录函数和变量的地址。|
|.debug_*段|调试信息，关联源代码和二进制指令。|

---

好了，简单介绍到这里吧，一旦掌握ELF文件的核心结构。无论是调试崩溃的程序，还是逆向分析二进制文件，ELF文件都是你的“地图”