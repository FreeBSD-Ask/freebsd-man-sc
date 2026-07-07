# gethostname.3

`gethostname` — 获取/设置当前主机的名称

## 名称

`gethostname`, `sethostname`

## 库

Lb libc

## 概要

`#include <unistd.h>`

`Ft int Fn gethostname char *name size_t namelen Ft int Fn sethostname const char *name int namelen`

## 描述

`gethostname` 函数返回当前处理器的标准主机名，该主机名此前由 `sethostname` 设置。`namelen` 参数指定 `name` 数组的大小。除非提供的空间不足，否则返回的名称以 null 结尾。

`sethostname` 函数将主机的名称设置为 `name`，其长度为 `namelen`。此调用仅限超级用户使用，通常仅在系统引导时使用。

应用程序应使用 `sysconf(_SC_HOST_NAME_MAX)` 来查找主机名的最大长度（不包括终止 null）。

## 返回值

Rv -std

## 错误

这些调用可能返回以下错误：

**[Er** EFAULT] `name` 或 `namelen` 参数给出了无效地址。

**[Er** ENAMETOOLONG] 当前主机名长于 `namelen`。（仅适用于 `gethostname`。）

**[Er** EPERM] 调用者试图设置主机名且不是超级用户。

## 参见

[sysconf(3)](sysconf.3.md), [sysctl(3)](sysctl.3.md)

## 标准

`gethostname` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。调用者应注意 {`HOST_NAME_MAX`} 可能是可变的或无限的，但保证不小于 {`_POSIX_HOST_NAME_MAX`}。在较旧的系统中，此限制定义于非标准头文件

`#include <sys/param.h>`

中，名称为 `MAXHOSTNAMELEN`，且计入终止 null。`sethostname` 函数和 `gethostname` 的错误返回未标准化。

## 历史

`gethostname` 函数出现于 4.2BSD。在 FreeBSD 5.2 中，`gethostname` 的 `namelen` 参数改为 `size_t` 类型，以与 IEEE Std 1003.1-2001 ("POSIX.1") 保持一致。
