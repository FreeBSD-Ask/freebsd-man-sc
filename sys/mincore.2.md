# mincore(2)

`mincore` — 确定内存页面的驻留状态

## 名称

`mincore`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
mincore(const void *addr, size_t len, char *vec);
```

## 描述

`mincore()` 系统调用根据 sysctl `vm.mincore_mapped` 的值，确定从 `addr` 开始、持续 `len` 字节的区域中每个页面是否驻留或已映射。状态通过 `vec` 数组返回，每个页面对应一个字符。如果页面未驻留，该字符为 0；否则为以下标志的组合（定义于

`#include <sys/mman.h>`

**`MINCORE_INCORE`** 页面在内存中（驻留）。

**`MINCORE_REFERENCED`** 页面已被本进程引用。

**`MINCORE_MODIFIED`** 页面已被本进程修改。

**`MINCORE_REFERENCED_OTHER`** 页面已被引用。

**`MINCORE_MODIFIED_OTHER`** 页面已被修改。

**`MINCORE_PSIND(i)`** 页面是大型（“超级”）页面的一部分，其大小由 [getpagesizes(3)](../sys-1/getpagesizes.3.md) 返回的数组中索引 `i` 处的值给出。

**`MINCORE_SUPER`** 有效的 `MINCORE_PSIND()` 值的掩码。如果此掩码中的任何位被设置，则该页面是大型（“超级”）页面的一部分。

`mincore()` 返回的信息在系统调用返回时可能已经过时。确保页面驻留的唯一方法是使用 [mlock(2)](mlock.2.md) 系统调用将其锁定在内存中。

如果 `vm.mincore_mapped` sysctl 设为非零值（默认值），仅检查当前进程在指定虚拟地址范围内的页面映射。这并不排除系统返回 `MINCORE_REFERENCED_OTHER` 和 `MINCORE_MODIFIED_OTHER` 状态。否则，如果 sysctl 值为零，则检查支持指定地址范围的所有驻留页面，无论映射状态如何。

## 实现说明

在 FreeBSD 13.0 引入 `MINCORE_PSIND()` 之前，`MINCORE_SUPER` 由等于 `MINCORE_PSIND(1)` 的单个位组成。特别是，使用旧版 `MINCORE_SUPER` 值编译的应用程序不会将大小索引为 2 的大型页面识别为大型页面。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`mincore()` 系统调用在以下情况下会失败：

**[`ENOMEM`]** `addr` 和 `len` 参数指定的虚拟地址范围未完全映射。

**[`EFAULT`]** `vec` 参数指向非法地址。

## 参见

[madvise(2)](madvise.2.md), [mlock(2)](mlock.2.md), [mprotect(2)](mprotect.2.md), [msync(2)](msync.2.md), [munmap(2)](munmap.2.md), [getpagesize(3)](../sys-1/getpagesize.3.md), [getpagesizes(3)](../sys-1/getpagesizes.3.md)

## 历史

`mincore()` 系统调用首次出现于 4.4BSD。
