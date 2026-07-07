# fspacectl(2)

`fspacectl` — 文件中的空间管理

## 名称

`fspacectl`

## 库

Lb libc

## 概要

`#include <fcntl.h>`

```c
int
fspacectl(int fd, int cmd, const struct spacectl_range *rqsr, int flags,
    struct spacectl_range *rmsr);
```

## 描述

`fspacectl` 是一个对文件执行空间管理的系统调用。`fd` 参数指定由 `cmd` 参数所操作的文件描述符。`rqsr` 参数指向一个 `spacectl_range` 结构，其中包含请求的操作范围。`flags` 参数控制要执行的操作的行为。如果 `rmsr` 参数非 NULL，则其所指向的 `spacectl_range` 结构会被更新，以包含系统调用返回后未处理的操作范围。

对于在请求操作范围内没有未处理部分的成功完成，`rmsr->r_len` 被更新为值 0，`rmsr->r_offset` 被更新为 `rqsr->r_offset` 加上在文件结束之前被清零的字节数。系统调用不使用也不修改文件描述符的文件偏移量。`rqsr` 和 `rmsr` 参数可以指向同一结构。

`spacectl_range` 结构定义如下：

```c
struct spacectl_range {
	off_t r_offset;
	off_t r_len;
};
```

由 `cmd` 参数指定的操作可以是以下之一：

**`SPACECTL_DEALLOC`** 将由 `rqsr` 参数指定的文件中的某个区域清零。`rqsr->r_offset` 必须是大于或等于 0 的值，`rqsr->r_len` 必须是大于 0 的值。如果文件系统支持打洞（hole-punching），可以在给定区域执行文件系统空间释放。

`flags` 参数当前必须为值 0。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置 `errno` 以指示错误。

## 错误

可能的失败条件：

**[`EBADF`]** `fd` 参数不是有效的文件描述符。

**[`EBADF`]** `fd` 参数引用了一个打开时没有写权限的文件。

**[`EINTR`]** 执行过程中捕获到信号。

**[`EINVAL`]** `cmd` 参数无效。

**[`EINVAL`]** 如果 `cmd` 参数为 `SPACECTL_DEALLOC`，则 `rqsr->r_offset` 参数小于零，或 `rqsr->r_len` 参数小于或等于零。

**[`EINVAL`]** `rqsr->r_offset + rqsr->r_len` 的值大于 `OFF_MAX`。

**[`EINVAL`]** `flags` 中包含无效或不支持的标志。

**[`EINVAL`]** `flags` 中包含的标志不被 `cmd` 参数指定的操作所支持。

**[`EFAULT`]** `rqsr` 或非 NULL 的 `rmsr` 参数指向进程已分配地址空间之外。

**[`EIO`]** 在对文件系统进行读取或写入时发生 I/O 错误。

**[`EINTEGRITY`]** 在从文件系统读取时检测到损坏的数据。

**[`ENODEV`]** `fd` 参数不引用支持 `fspacectl` 的文件。

**[`ENOSPC`]** 文件系统存储介质上剩余的可用空间不足。

**[`ENOTCAPABLE`]** 文件描述符 `fd` 的权限不足。

**[`ESPIPE`]** `fd` 参数与管道或 FIFO 关联。

## 参见

[creat(2)](creat.2.md), [ftruncate(2)](truncate.2.md), [open(2)](open.2.md), [unlink(2)](unlink.2.md)

## 历史

`fspacectl` 系统调用出现于 FreeBSD 14.0。

## 作者

`fspacectl` 及本手册页由 Ka Ho Ng <khng@FreeBSD.org> 在 FreeBSD Foundation 的赞助下编写。
