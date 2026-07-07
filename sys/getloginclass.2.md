# getloginclass(2)

`getloginclass` — 获取/设置登录类

## 名称

`getloginclass`, `setloginclass`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
getloginclass(char *name, size_t len);

int
setloginclass(const char *name);
```

## 描述

`getloginclass()` 例程返回与调用进程关联的登录类名称，该名称此前由 `setloginclass()` 设置。调用者必须提供长度为 `len` 字节的缓冲区 `name` 来存放结果。该缓冲区的长度应至少为 `MAXLOGNAME` 字节。

`setloginclass()` 系统调用将调用进程的登录类设置为 `name`。此系统调用仅限超级用户使用，通常仅在代表命名用户创建新会话时使用（例如，在登录时，或调用远程 shell 时）。进程从其父进程继承登录类。

## 返回值

`getloginclass()` 和 `setloginclass()` 系统调用在成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

这些调用可能返回以下错误：

**[`EFAULT`]** `name` 参数给出了无效地址。

**[`EINVAL`]** `name` 参数指向的字符串过长。登录类名称限制为 `MAXLOGNAME`（来自 `<sys/param.h>`）个字符，目前包括 null 终止符在内为 33 个。

**[`EPERM`]** 调用者试图设置登录类，但不是超级用户。

**[`ENAMETOOLONG`]** 缓冲区大小小于要返回的结果。

## 参见

[ps(1)](../man1/ps.1.md), setusercontext(3), [login.conf(5)](../man5/login.conf.5.md), [rctl(8)](../man8/rctl.8.md)

## 历史

`getloginclass()` 和 `setloginclass()` 系统调用首次出现于 FreeBSD 9.0。
