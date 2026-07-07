# getbootfile(3)

`getbootfile` — 获取内核启动文件名

## 名称

`getbootfile`

## 库

Lb libc

## 概要

`#include <paths.h>`

```c
const char *
getbootfile(void);
```

## 描述

`getbootfile` 函数检索当前内核加载时所用的文件的完整路径名，并返回指向该名称的静态指针。通过 [sysctl(3)](sysctl.3.md) MIB 变量"`kern.bootfile`"可获得此信息的读写接口。

## 返回值

如果调用成功，返回给出路径名的字符串。如果失败，返回空指针，并在全局位置 `errno` 中放置错误代码。

## 参见

[sysctl(3)](sysctl.3.md)

## 历史

`getbootfile` 函数出现于 FreeBSD 2.0。

## 缺陷

如果启动块未被修改以在引导时将此信息传递给内核，则返回静态字符串"**/boot/kernel/kernel**"而不是真实的启动文件。
