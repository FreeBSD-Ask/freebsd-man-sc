# mprotect(2)

`mprotect` — 控制页面的保护

## 名称

`mprotect`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
mprotect(void *addr, size_t len, int prot);
```

## 描述

`mprotect()` 系统调用将指定页面更改为具有保护 `prot`。

`prot` 参数应为 `PROT_NONE`（无任何权限）或以下一个或多个值的按位*或*：

**`PROT_READ`** 页面可读。

**`PROT_WRITE`** 页面可写。

**`PROT_EXEC`** 页面可执行。

除了这些标准保护标志外，FreeBSD 的 `mprotect()` 实现还提供了设置区域最大保护的能力（防止 `mprotect` 以后增加权限）。这通过将包装在 `PROT_MAX()` 宏中的一个或多个 `PROT_` 值按位*或*到 `prot` 参数中来实现。

## 返回值

成功完成后返回 0；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`mprotect()` 系统调用将在以下情况下失败：

**[`EACCES`]** 不允许调用进程将保护更改为 `prot` 参数指定的值。

**[`EINVAL`]** 由 `addr` 和 `len` 参数指定的虚拟地址范围无效。

**[`EINVAL`]** `prot` 参数包含未处理的位。

**[`ENOTSUP`]** `prot` 参数包含的权限不是指定最大权限的子集。

## 参见

[madvise(2)](madvise.2.md), [mincore(2)](mincore.2.md), [msync(2)](msync.2.md), [munmap(2)](munmap.2.md)

## 历史

`mprotect()` 系统调用首次在 4.2BSD 中文档化，首次出现于 4.4BSD。

`PROT_MAX` 功能引入于 FreeBSD 13。
