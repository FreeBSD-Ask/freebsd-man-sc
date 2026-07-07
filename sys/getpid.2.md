# getpid(2)

`getpid` — 获取父进程或调用进程的标识

## 名称

`getpid`, `getppid`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
getpid(void);

pid_t
getppid(void);
```

## 描述

`getpid()` 系统调用返回调用进程的进程 ID。尽管该 ID 保证唯一，但出于安全原因，*不应*使用它来构造临时文件名；请参见 mkstemp(3)。

`getppid()` 系统调用返回调用进程的父进程的进程 ID。

## 错误

`getpid()` 和 `getppid()` 系统调用总是成功，没有保留返回值用于指示错误。

## 参见

[fork(2)](fork.2.md), [getpgrp(2)](getpgrp.2.md), [kill(2)](kill.2.md), [setpgid(2)](setpgid.2.md), [setsid(2)](setsid.2.md), [exec(3)](../gen/exec.3.md)

## 标准

`getpid()` 和 `getppid()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1") 规范。

## 历史

`getpid()` 函数出现于 Version 7 AT&T UNIX。
