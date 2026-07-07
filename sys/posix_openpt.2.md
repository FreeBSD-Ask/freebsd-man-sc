# posix_openpt(2)

`posix_openpt` — 打开伪终端设备

## 名称

`posix_openpt`

## 库

Lb libc

## 概要

```c
#include <fcntl.h>
#include <stdlib.h>

int
posix_openpt(int oflag);
```

## 描述

`posix_openpt()` 函数分配一个新的伪终端，并与其主设备建立连接。从设备将被创建在 **/dev/pts** 中。伪终端分配完成后，从设备在使用前应具有正确的权限（参见 [grantpt(3)](../stdlib/ptsname.3.md)）。从设备的名称可以通过调用 [ptsname(3)](../stdlib/ptsname.3.md) 来确定。

打开文件描述的文件状态标志和文件访问模式将根据 `oflag` 的值进行设置。`oflag` 的值由以下列表中定义的标志按位或构成：

```c
#include <fcntl.h>
```

**`O_RDWR`** 以读写方式打开。

**`O_NOCTTY`** 若设置，`posix_openpt()` 不会使终端设备成为该进程的控制终端。

**`O_CLOEXEC`** 为新文件描述符设置 close-on-exec 标志。

当 `oflag` 包含其他值时，`posix_openpt()` 函数将失败。

## 返回值

成功完成时，`posix_openpt()` 函数将分配一个新的伪终端设备，并返回一个表示文件描述符的非负整数，该描述符连接到其主设备。否则，返回 -1，并设置 errno 以指示错误。

## 错误

`posix_openpt()` 函数在以下情况下将失败：

**[ENFILE]** 系统文件表已满。

**[EINVAL]** `oflag` 的值无效。

**[EAGAIN]** 伪终端资源不足。

## 参见

[grantpt(3)](../stdlib/ptsname.3.md), [ptsname(3)](../stdlib/ptsname.3.md), [pts(4)](../man4/pts.4.md), [tty(4)](../man4/tty.4.md)

## 标准

`posix_openpt()` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。使用 `O_CLOEXEC` 的能力是对标准的扩展。

## 历史

`posix_openpt()` 函数首次出现于 FreeBSD 5.0。在 FreeBSD 8.0 中，该函数被改为系统调用。

## 注释

`O_NOCTTY` 标志是为了兼容性而保留的；在 FreeBSD 中，打开终端不会使其成为进程的控制终端。

## 作者

Ed Schouten <ed@FreeBSD.org>
