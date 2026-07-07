# posix_fadvise(2)

`posix_fadvise` — 提供关于文件数据使用的建议

## 名称

`posix_fadvise`

## 库

Lb libc

## 概要

`#include <fcntl.h>`

```c
int
posix_fadvise(int fd, off_t offset, off_t len, int advice);
```

## 描述

`posix_fadvise()` 系统调用允许进程向系统描述其对打开文件描述符 `fd` 的数据访问行为。该建议覆盖从偏移量 `offset` 开始、持续 `len` 字节的数据。如果 `len` 为零，则覆盖从 `offset` 到文件末尾的所有数据。

行为由 `advice` 参数指定，可以是以下值之一：

**`POSIX_FADV_NORMAL`** 告知系统恢复默认的数据访问行为。

**`POSIX_FADV_RANDOM`** 提示文件数据将被随机访问，预取可能没有益处。

**`POSIX_FADV_SEQUENTIAL`** 告知系统文件数据将被顺序访问。目前这不起作用，因为默认行为使用启发式方法来检测顺序行为。

**`POSIX_FADV_WILLNEED`** 告知系统指定的数据将在不久后被访问。如果数据尚未存在于内存中，系统可以发起对该数据的异步读取。

**`POSIX_FADV_DONTNEED`** 告知系统指定的数据在不久的将来不会被访问。系统可以降低指定范围内干净数据在内存中的优先级，未来访问该数据可能需要读操作。

**`POSIX_FADV_NOREUSE`** 告知系统指定的数据只会被访问一次，之后不再重用。系统可以在数据被读取或写入后降低其在内存中的优先级。未来访问该数据可能需要读操作。

## 返回值

成功时，`posix_fadvise()` 返回零。失败时返回一个错误码，不设置 `errno`。

## 错误

可能的失败情况：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`EINVAL`]** `advice` 参数无效。

**[`EINVAL`]** `offset` 或 `len` 参数为负，或者 `offset` + `len` 大于最大文件大小。

**[`ENODEV`]** `fd` 参数不引用常规文件。

**[`ESPIPE`]** `fd` 参数与管道或 FIFO 相关联。

**[`EIO`]** 在读取或写入文件系统时发生 I/O 错误。

**[`EINTEGRITY`]** 在读取文件系统时检测到数据损坏。

## 参见

[madvise(2)](madvise.2.md)

## 标准

`posix_fadvise()` 接口遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`posix_fadvise()` 系统调用首次出现于 FreeBSD 9.1。