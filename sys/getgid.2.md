# getgid(2)

`getgid` — 获取组进程标识

## 名称

`getgid`, `getegid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
gid_t
getgid(void);

gid_t
getegid(void);
```

## 描述

`getgid()` 系统调用返回调用进程的实际组 ID，`getegid()` 返回调用进程的有效组 ID。

实际组 ID 在登录时指定。

实际组 ID 是调用该程序的用户的组。由于有效组 ID 在执行“*set-group-ID*”模式进程期间赋予进程额外的权限，因此 `getgid()` 用于确定调用进程的实际用户 ID。

## 错误

`getgid()` 和 `getegid()` 系统调用总是成功，不保留任何返回值用于指示错误。

## 参见

[getuid(2)](getuid.2.md), [issetugid(2)](issetugid.2.md), [setgid(2)](setuid.2.md), [setregid(2)](setregid.2.md)

## 标准

`getgid()` 和 `getegid()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`getgid()` 函数出现于 Version 4 AT&T UNIX。