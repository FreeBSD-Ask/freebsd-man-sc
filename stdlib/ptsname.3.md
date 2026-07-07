# ptsname.3

`grantpt` — 伪终端访问函数

## 名称

`grantpt`, `ptsname`, `ptsname_r`, `unlockpt`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
grantpt(int fildes);

char *
ptsname(int fildes);

int
ptsname_r(int fildes, char *buffer, size_t buflen);

int
unlockpt(int fildes);
```

## 描述

`grantpt`、`ptsname` 和 `unlockpt` 函数允许访问伪终端设备。这三个函数接受一个引用伪终端对主端的文件描述符。该文件描述符通过 [posix_openpt(2)](../sys/posix_openpt.2.md) 创建。

`grantpt` 函数用于建立与 `fildes` 所指定主设备对应的从设备的属主和权限。从设备的属主设置为调用进程的实际用户 ID，权限设置为用户可读写且组可写。从设备的组属主还设置为“`tty`”组。

`ptsname` 函数返回与 `fildes` 所指定主设备对应的从设备的完整路径名。在调用 [posix_openpt(2)](../sys/posix_openpt.2.md) 和 `grantpt` 之后，可使用此值随后打开相应的从设备。

`ptsname_r` 函数是 `ptsname` 的线程安全版本。调用者必须在 `buffer` 和 `bufsize` 参数中为从设备完整路径名的结果提供存储空间。

`unlockpt` 函数清除对 `fildes` 所指定主设备的伪终端对所持有的锁。

## 返回值

`grantpt` 和 `unlockpt` 函数成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

`ptsname` 函数成功时返回指向从设备名称的指针；否则返回 `NULL` 指针。

`ptsname_r` 函数成功时返回值 0；否则返回非零值，并设置全局变量 `errno` 以指示错误。注意：`ptsname_r` 以前文档记录为出错时返回 -1。将来会改为返回错误号，以兼容 POSIX。因此，调用者不应检查 -1。

## 错误

`grantpt`、`ptsname`、`ptsname_r` 和 `unlockpt` 函数可能失败并设置 `errno` 为：

**[`EBADF`]** `fildes` 不是有效的已打开文件描述符。

**[`EINVAL`]** `fildes` 不是主伪终端设备。

此外，`ptsname_r` 函数可能设置 `errno` 为：

**[`ERANGE`]** 缓冲区太小。

此外，`grantpt` 函数可能设置 `errno` 为：

**[`EACCES`]** 无法访问从伪终端设备。

## 参见

[posix_openpt(2)](../sys/posix_openpt.2.md), [pts(4)](../man4/pts.4.md), [tty(4)](../man4/tty.4.md)

## 标准

`ptsname` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

此 `grantpt` 和 `unlockpt` 的实现不遵循 IEEE Std 1003.1-2008 ("POSIX.1")，因为它依赖 [posix_openpt(2)](../sys/posix_openpt.2.md) 创建带有适当权限的伪终端设备。它仅验证 `fildes` 是否为有效的伪终端主设备。如 Austin Group 所述，未来的规范修订可能会允许此行为。

## 历史

`grantpt`、`ptsname` 和 `unlockpt` 函数出现于 FreeBSD 5.0。
