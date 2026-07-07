# munmap(2)

`munmap` — 删除映射

## 名称

`munmap`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
munmap(void *addr, size_t len);
```

## 描述

`munmap()` 系统调用删除指定地址范围的映射和保护区，并使对该范围内地址的进一步引用生成无效内存引用。

## 返回值

成功完成时，`munmap()` 函数返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`munmap()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `len` 参数为零，或要取消映射区域的某部分超出进程的有效地址范围。

## 参见

[madvise(2)](madvise.2.md), [mincore(2)](mincore.2.md), [mmap(2)](mmap.2.md), [mprotect(2)](mprotect.2.md), [msync(2)](msync.2.md), [getpagesize(3)](../man3/getpagesize.3.md)

## 标准

`munmap()` 系统调用遵循 -p1003.1-2024。可移植程序应确保 `addr` 是 [sysconf(3)](../man3/sysconf.3.md) 返回的页大小的倍数。

## 历史

`munmap()` 系统调用首次出现于 4.4BSD。
