# msync(2)

`msync` — 同步映射区域

## 名称

`msync`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
msync(void *addr, size_t len, int flags);
```

## 描述

`msync` 系统调用将所有已修改的页面写回文件系统，并更新文件修改时间。如果 `len` 为 0，将刷新包含 `addr` 的区域内的所有已修改页面；如果 `len` 非零，则仅检查包含 `addr` 及其后 `len-1` 个连续位置的页面。`flags` 参数可按如下指定：

**`MS_ASYNC`** 立即返回

**`MS_SYNC`** 执行同步写入

**`MS_INVALIDATE`** 使所有缓存数据失效

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`msync` 系统调用在以下情况下会失败：

**[`EBUSY`]** 指定区域中的部分或全部页面被锁定，且指定了 `MS_INVALIDATE`。

**[`EINVAL`]** `addr` 参数不是硬件页面大小的整数倍。

**[`ENOMEM`]** 从 `addr` 开始并延续 `len` 字节的范围内的地址超出了进程地址空间所允许的范围，或者指定了一个或多个未映射的页面。

**[`EINVAL`]** `flags` 参数同时为 MS_ASYNC 和 MS_INVALIDATE。仅允许使用其中之一。

**[`EIO`]** 在写入指定区域中至少一个页面时发生错误。

## 参见

[madvise(2)](madvise.2.md), [mincore(2)](mincore.2.md), [mlock(2)](mlock.2.md), [mprotect(2)](mprotect.2.md), [munmap(2)](munmap.2.md)

## 历史

`msync` 系统调用首次出现于 4.4BSD。

## 缺陷

`msync` 系统调用通常不需要，因为 BSD 实现了连贯的文件系统缓冲区缓存。然而，它可用于将脏 VM 页面与文件系统缓冲区关联，从而使其更快地被刷新到物理介质。
