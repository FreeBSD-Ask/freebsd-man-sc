# getdtablesize(2)

`getdtablesize` — 获取文件描述符上限

## 名称

`getdtablesize`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
getdtablesize(void);
```

## 描述

`getdtablesize()` 系统调用返回当前进程可打开的最大文件描述符数。系统可分配的最大文件描述符号为返回值减一。如果在打开文件描述符之后降低了限制，则现有文件描述符号可能更高。

## 参见

[close(2)](close.2.md), [closefrom(2)](closefrom.2.md), [dup(2)](dup.2.md), [getrlimit(2)](getrlimit.2.md), [sysconf(3)](../gen/sysconf.3.md)

## 历史

`getdtablesize()` 系统调用出现于 4.2BSD。