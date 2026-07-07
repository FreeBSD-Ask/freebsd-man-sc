# minherit(2)

`minherit` — 控制页面的继承

## 名称

`minherit`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
minherit(void *addr, size_t len, int inherit);
```

## 描述

`minherit()` 系统调用将指定页面更改为具有继承特性 `inherit`。并非所有实现都保证继承特性可按页面设置；更改的粒度可能大到整个区域。FreeBSD 能够按页面调整继承特性。继承仅影响由 `fork()` 创建的子进程。它对 `exec()` 没有影响。exec 的进程完全替换其地址空间。此系统调用对父进程的地址空间也没有影响（除了可能与其子进程共享地址空间）。

继承是一个相当深奥的功能，很大程度上已被 `mmap()` 的 `MAP_SHARED` 功能所取代。但是，可使用 `minherit()` 在已映射为 `MAP_PRIVATE` 的父进程和子进程之间共享一块内存。也就是说，父进程或子进程所做的修改会被共享，但原始底层文件保持不变。

**`INHERIT_SHARE`** 此选项使所讨论的地址空间在父进程和子进程之间共享。它对原始底层后备存储的映射方式没有影响。

**`INHERIT_NONE`** 此选项阻止所讨论的地址空间被继承。该地址空间将在子进程中取消映射。

**`INHERIT_COPY`** 此选项使子进程以写时复制方式继承地址空间。此选项还具有一个不幸的副作用：当父进程 fork 时，父进程地址空间也会变为写时复制。如果原始映射为 `MAP_SHARED`，在父进程 fork 之后，它将不再在父进程中被共享，且除非在父进程中取消映射并重新映射该地址空间，否则无法恢复先前的共享后备存储映射。

**`INHERIT_ZERO`** 此选项使所讨论的地址空间在子进程中映射为新的匿名页面，这些页面将初始化为全零字节。

## 返回值

成功完成后返回 0；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`minherit()` 系统调用将在以下情况下失败：

**[`EINVAL`]** 由 `addr` 和 `len` 参数指定的虚拟地址范围无效。

**[`EACCES`]** 由 `inherit` 参数指定的标志对由 `addr` 和 `len` 参数指定的页面无效。

## 参见

[fork(2)](fork.2.md), [madvise(2)](madvise.2.md), [mincore(2)](mincore.2.md), [mprotect(2)](mprotect.2.md), [msync(2)](msync.2.md), [munmap(2)](munmap.2.md), [rfork(2)](rfork.2.md)

## 历史

`minherit()` 系统调用首次出现于 OpenBSD，随后出现于 FreeBSD 2.2。

`INHERIT_ZERO` 支持首次出现于 OpenBSD 5.6，随后出现于 FreeBSD 12.0。

## 缺陷

一旦将继承设置为 `MAP_PRIVATE` 或 `MAP_SHARED`，除了取消映射并重新映射该区域外，无法恢复原始的写时复制语义。
