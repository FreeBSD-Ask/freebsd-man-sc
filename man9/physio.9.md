# physio.9

`physio` — 在原始设备上启动 I/O

## 名称

`physio`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/systm.h>
```

```c
#include <sys/bio.h>
```

```c
#include <sys/buf.h>
```

```c
int
physio(struct cdev *dev, struct uio *uio, int ioflag)
```

## 描述

`physio` 是一个辅助函数，通常从字符设备 `read` 和 `write` 例程中调用，以在用户进程缓冲区上启动 I/O。每次调用传输的最大数据量由 `dev->si_iosize_max` 确定。`physio` 调用将 I/O 请求转换为 `strategy` 请求，并将新请求传递给驱动程序的 `strategy` 例程进行处理。

由于 `uio` 通常描述用户空间地址，`physio` 需要将这些页面锁定到内存中。这是通过为相应的页面调用 `vmapbuf` 完成的。`physio` 总是等待整个请求传输完成后再返回，除非更早地检测到错误条件。

参数说明如下：

**`dev`** 标识要交互的设备的设备号。

**`uio`** 用户进程请求的整个传输的描述。目前，传递 `uio_segflg` 设置为 `UIO_USERSPACE` 以外值的 `uio` 结构的结果是未定义的。

**`ioflag`** 调用 `physio` 的 `read` 或 `write` 函数的 ioflag 参数。

## 返回值

如果成功，`physio` 返回 0。如果 `uio` 描述的地址范围无法被请求进程访问，则返回 EFAULT。`physio` 将通过检查 `B_ERROR` 缓冲区标志和 `b_error` 字段返回设备策略例程调用产生的任何错误。注意，如果设备发出“文件结束”条件信号，实际传输大小可能小于 `uio` 请求的大小。

## 参见

read(2), write(2)

## 历史

`physio` 手册页最初来自 NetBSD，为适用于 FreeBSD 进行了少量更改。

`physio` 调用已被完全重写，以提供更高的 I/O 和分页性能。
