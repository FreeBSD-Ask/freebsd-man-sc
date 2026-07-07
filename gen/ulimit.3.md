# ulimit(3)

`ulimit` — 获取和设置进程限制

## 名称

`ulimit`

## 库

Lb libc

## 概要

```c
#include <ulimit.h>

long
ulimit(int cmd, ...);
```

## 描述

`ulimit` 函数用于获取和设置进程限制。目前仅限于最大文件大小。`cmd` 参数为以下之一：

`UL_GETFSIZE` 返回当前进程的最大文件大小，以 512 字节块为单位。

`UL_SETFSIZE` 尝试设置当前进程及其子进程的最大文件大小，第二个参数以 long 类型表示。

## 返回值

成功完成时，`ulimit` 返回所请求的值；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`ulimit` 函数在以下情况将失败：

**[`EINVAL`]** 指定的命令无效。

**[`EPERM`]** 传给 `ulimit` 的限制值会提高最大限制值，且调用者不是超级用户。

## 参见

[getrlimit(2)](../sys/getrlimit.2.md)

## 标准

`ulimit` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`ulimit` 函数首次出现于 FreeBSD 5.0。

## 缺陷

`ulimit` 函数在设置和获取进程限制时精度有限。如果需要比 `long` 类型所提供的更高精度，可考虑使用 [getrlimit(2)](../sys/getrlimit.2.md) 和 setrlimit(2) 函数。
