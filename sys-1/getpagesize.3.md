# getpagesize(3)

`getpagesize` — 获取系统页面大小

## 名称

`getpagesize`

## 库

libc

## 概要

```c
#include <unistd.h>

int
getpagesize(void);
```

## 描述

`getpagesize` 函数返回一个页面中的字节数。页面粒度是许多内存管理调用的粒度。

此处的页面大小是系统页面大小，可能与底层硬件页面大小不同。

IEEE Std 1003.1-2001 ("POSIX.1") 移除了 `getpagesize`。可移植的应用程序应改用 `sysconf(_SC_PAGESIZE)`。

## 参见

[pagesize(1)](../man1/pagesize.1.md), sbrk(2), [getpagesizes(3)](getpagesizes.3.md), sysconf(3)

## 历史

`getpagesize` 函数出现于 4.2BSD。
