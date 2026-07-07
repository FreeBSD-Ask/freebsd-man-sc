# ioctl(2)

`ioctl` — 控制设备

## 名称

`ioctl`

## 库

Lb libc

## 概要

`#include <sys/ioctl.h>`

```c
int
ioctl(int fd, unsigned long request, ...);
```

## 描述

`ioctl()` 系统调用操作特殊文件的底层设备参数。特别是，字符特殊文件（例如终端）的许多操作特性可以通过 `ioctl()` 请求来控制。`fd` 参数必须是一个打开的文件描述符。

`ioctl()` 的第三个参数传统上命名为 `char *argp`。然而，`ioctl()` 的大多数用途要求第三个参数为 `caddr_t` 或 `int`。

`ioctl()` 的 `request` 中编码了参数是“in”参数还是“out”参数，以及参数 `argp` 的大小（以字节为单位）。用于指定 ioctl `request` 的宏和定义位于文件

`#include <sys/ioctl.h>`

## 通用 ioctl

某些通用 ioctl 并未对所有类型的文件描述符实现。包括：

**`FIONREAD int`** 获取立即可供读取的字节数。

**`FIONWRITE int`** 获取描述符发送队列中的字节数。这些字节是已写入描述符但被内核保留以供进一步处理的数据。所需处理的性质取决于底层设备。对于 TCP 套接字，这些字节尚未被连接的另一端确认。

**`FIONSPACE int`** 获取描述符发送队列中的可用空间。此值为发送队列大小减去队列中保留的字节数。注意：虽然此值表示可添加到队列的字节数，但其他资源限制可能导致小于发送队列空间的写入被阻塞。其中一个限制可能是由于网络缓冲区不足而无法写入网络连接。

## 返回值

如果发生错误，返回值 -1，并设置 `errno` 以指示错误。

## 错误

`ioctl()` 系统调用在以下情况下会失败：

**[`EACCES`]** 进程无权调用此 `ioctl`。

**[`EBADF`]** `fd` 参数不是有效的描述符。

**[`ENOTTY`]** `fd` 参数未与字符特殊设备关联。

**[`ENOTTY`]** 指定的请求不适用于描述符 `fd` 所引用的对象类型。

**[`EINVAL`]** `request` 或 `argp` 参数无效。

**[`EFAULT`]** `argp` 参数指向进程所分配地址空间之外。

## 参见

[execve(2)](execve.2.md), [fcntl(2)](fcntl.2.md), [intro(4)](../man4/intro.4.md), [tty(4)](../man4/tty.4.md)

## 历史

`ioctl()` 函数出现于 Version 7 AT&T UNIX。
