# io.4

`io` — I/O 特权文件

## 名称

`io`

## 概要

`device io`

`#include <sys/types.h>`

`#include <sys/ioctl.h>`

`#include <dev/io/iodev.h>`

`#include <machine/iodev.h>`

```sh
struct iodev_pio_req {
	u_int access;
	u_int port;
	u_int width;
	u_int val;
};
```

## 描述

特殊文件 **`/dev/io`** 是一个受控的安全漏洞，允许进程获取 I/O 特权（通常保留给内核内部代码使用）。这对于编写直接处理某些硬件的用户空间程序可能很有用。

对该设备的常规操作是通过 open(2) 接口打开它，并使用 ioctl(2) 系统调用向文件描述符发送 I/O 请求。

可用于 **`/dev/io`** 的 ioctl(2) 请求大多与平台相关，但也有一些是所有平台通用的。所有架构都使用 `IODEV_PIO` 来请求执行 I/O 操作。它接受一个必须事先设置好的 `struct iodev_pio_req` 参数。

`access` 成员指定所请求的操作类型。可以是：

**`IODEV_PIO_READ`** 操作为“in”类型。将从指定端口（从 `port` 成员获取）读取一个值，并将结果存储在 `val` 成员中。

**`IODEV_PIO_WRITE`** 操作为“out”类型。将从 `val` 成员获取值，并将其写入指定端口（由 `port` 成员定义）。

最后，`width` 成员指定要读/写的操作数大小，以字节为单位。

除对 **`/dev/io`** 的任何文件访问权限外，内核还强制要求只有超级用户才能打开此设备。

## 遗留

**`/dev/io`** 接口曾经是 i386 专用的，工作方式也不同。最初的实现只是在调用 open(2) 打开该设备时提升当前线程的 *IOPL*。当前实现中保留了此行为，作为对 i386 和 amd64 架构的遗留支持。

## 参见

close(2), i386_get_ioperm(2), i386_set_ioperm(2), ioctl(2), open(2), [mem(4)](mem.4.md)

## 历史

`io` 文件出现于 FreeBSD 1.0。
