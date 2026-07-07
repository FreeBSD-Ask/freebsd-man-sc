# umask(2)

`umask` — 设置文件创建模式掩码

## 名称

`umask`

## 库

Lb libc

## 概要

```c
#include <sys/stat.h>

mode_t
umask(mode_t numask);
```

## 描述

`umask()` 例程将进程的文件模式创建掩码设置为 `numask`，并返回该掩码的前一个值。`numask` 的低 9 位访问权限位被系统调用使用，包括 [open(2)](open.2.md)、[mkdir(2)](mkdir.2.md) 和 [mkfifo(2)](mkfifo.2.md)，用于关闭文件模式中请求的对应位。（参见 [chmod(2)](chmod.2.md)。）这种清除操作允许每个用户限制对其文件的默认访问。

默认的掩码值为 S_IWGRP|S_IWOTH（022，仅所有者有写权限）。子进程继承调用进程的掩码。

## 返回值

调用返回文件模式掩码的前一个值。

## 错误

`umask()` 系统调用总是成功。

## 参见

[chmod(2)](chmod.2.md), [mkfifo(2)](mkfifo.2.md), [mknod(2)](mknod.2.md), [open(2)](open.2.md)

## 标准

`umask()` 系统调用预期符合 IEEE Std 1003.1-1990 ("POSIX.1")。

## 历史

`umask()` 函数出现于 Version 7 AT&T UNIX。
