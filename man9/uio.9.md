# uio(9)

`uio` — 设备驱动程序 I/O 例程

## 名称

`uio`, `uiomove`, `uiomove_frombuf`, `uiomove_fromphys`, `uiomove_nofault`

## 概要

`#include <sys/types.h>`

`#include <sys/uio.h>`

```c
struct uio {
	struct iovec	*uio_iov;	/* 分散/聚集列表 */
	int		 uio_iovcnt;	/* 分散/聚集列表长度 */
	off_t		 uio_offset;	/* 在目标对象中的偏移量 */
	ssize_t		 uio_resid;	/* 剩余待处理字节数 */
	enum uio_seg	 uio_segflg;	/* 地址空间 */
	enum uio_rw	 uio_rw;	/* 操作 */
	struct thread	*uio_td;	/* 所有者 */
};
```

`int uiomove(void *buf, int howmuch, struct uio *uiop)`

`int uiomove_frombuf(void *buf, int howmuch, struct uio *uiop)`

`int uiomove_fromphys(vm_page_t ma[], vm_offset_t offset, int howmuch, struct uio *uiop)`

`int uiomove_nofault(void *buf, int howmuch, struct uio *uiop)`

## 描述

`uiomove()`、`uiomove_frombuf()`、`uiomove_fromphys()` 和 `uiomove_nofault()` 函数用于在缓冲区和可能跨越用户/内核空间边界的 I/O 向量之间传输数据。

作为传递给字符设备驱动程序的任何 read(2)、write(2)、readv(2) 或 writev(2) 系统调用的结果，将调用相应的驱动程序 `d_read` 或 `d_write` 入口，并传入指向 `struct uio` 的指针。传输请求编码在此结构中。驱动程序本身应使用 `uiomove()` 或 `uiomove_nofault()` 来访问此结构中的数据。

`uio` 结构中的字段如下：

**`UIO_USERSPACE`** I/O 向量指向进程的地址空间。

**`UIO_SYSSPACE`** I/O 向量指向内核地址空间。

**`UIO_NOCOPY`** 不复制，已在对象中。

**`UIO_READ`** 将数据从缓冲区传输到 I/O 向量。

**`UIO_WRITE`** 将数据从 I/O 向量传输到缓冲区。

**`uio_iov`** 待处理的 I/O 向量数组。在分散/聚集 I/O 的情况下，将有多个向量。

**`uio_iovcnt`** 存在的 I/O 向量数量。

**`uio_offset`** 设备中的偏移量。

**`uio_resid`** 剩余待处理的字节数，在传输后更新。

**`uio_segflg`** 以下标志之一：

**`uio_rw`** 所需传输的方向。支持的标志有：

**`uio_td`** 指向关联线程的 `struct thread` 的指针；如果 `uio_segflg` 指示传输要从/向进程地址空间进行，则使用此字段。

`uiomove_nofault()` 函数要求缓冲区和 I/O 向量可在不引发页错误的情况下访问。源地址和目标地址必须分别物理映射以进行读写访问，且源地址和目标地址都不可分页。因此，`uiomove_nofault()` 函数可从禁止获取虚拟内存系统锁或睡眠的上下文中调用。

`uiomove_frombuf()` 函数是 `uiomove()` 的便捷封装，适用于服务完全包含在内存中现有缓冲区内的数据的驱动程序。它根据现有缓冲区的大小验证 `uio_offset` 和 `uio_resid` 值，在请求部分重叠缓冲区时处理短传输。当 `uio_offset` 大于或等于缓冲区大小时，结果为成功但不传输任何字节，有效地发出 EOF 信号。

`uiomove_fromphys()` 函数提供了一种与机器无关的方式，用于在物理地址空间之间复制内存。`ma[]` 参数是物理页数组。数组中的每个物理页地址提供一个页大小的物理空间块。`offset` 参数是 `ma[]` 数组中的偏移量。特别是，偏移量不必位于第一页内。

## 返回值

成功时 `uiomove()`、`uiomove_frombuf()`、`uiomove_fromphys()` 和 `uiomove_nofault()` 将返回 0；出错时将返回适当的错误代码。

## 实例

其思路是驱动程序为其数据维护一个私有缓冲区，并以最大不超过此缓冲区大小的块处理请求。注意，下面的缓冲区处理非常简化，不会工作（在部分读取时缓冲区指针不会前进），此处仅用于演示 `uiomove_nofault` 处理。

```c
/* MIN() 可在此处找到： */
#include <sys/param.h>
#define BUFSIZE 512
static char buffer[BUFSIZE];
static int data_available;	/* 可读取的数据量 */
static int
fooread(struct cdev *dev, struct uio *uio, int flag)
{
	int rv, amnt;
	rv = 0;
	while (uio->uio_resid > 0) {
		if (data_available > 0) {
			amnt = MIN(uio->uio_resid, data_available);
			rv = uiomove(buffer, amnt, uio);
			if (rv != 0)
				break;
			data_available -= amnt;
		} else
			tsleep(...);	/* 等待更好的时机 */
	}
	if (rv != 0) {
		/* 在此处进行错误清理 */
	}
	return (rv);
}
```

## 错误

`uiomove()`、`uiomove_fromphys()` 和 `uiomove_nofault()` 在以下情况下将失败并返回以下错误代码：

**[`EFAULT`]** 调用的 copyin(9) 或 copyout(9) 返回 `EFAULT`。

此外，`uiomove_nofault()` 在以下情况下将失败并返回以下错误代码：

**[`EFAULT`]** 发生页错误。

## 参见

read(2), readv(2), write(2), writev(2), copyin(9), copyout(9), [sleep(9)](sleep.9.md)

## 历史

`uiomove_nofault` 机制出现在 UNIX 的某个早期版本中。

## 作者

本手册页由 J(:org Wunsch 编写。
