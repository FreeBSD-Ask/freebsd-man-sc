# getuid(2)

`getuid` — 获取用户标识

## 名称

`getuid`, `geteuid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
uid_t
getuid(void);

uid_t
geteuid(void);
```

## 描述

`getuid()` 系统调用返回调用进程的实际用户 ID。`geteuid()` 系统调用返回调用进程的有效用户 ID。

实际用户 ID 是调用该程序的用户。由于有效用户 ID 在执行“*set-user-ID*”模式进程时为进程提供额外权限，因此使用 `getuid()` 来确定调用进程的实际用户 ID。

## 错误

`getuid()` 和 `geteuid()` 系统调用总是成功，没有保留任何返回值用于指示错误。

## 参见

[getgid(2)](getgid.2.md), [issetugid(2)](issetugid.2.md), [setgid(2)](setuid.2.md), [setreuid(2)](setreuid.2.md), [setuid(2)](setuid.2.md)

## 标准

`geteuid()` 和 `getuid()` 系统调用预期遵循 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`getuid()` 函数出现于 Version 1 AT&T UNIX。`geteuid()` 函数出现于 Version 4 AT&T UNIX。
