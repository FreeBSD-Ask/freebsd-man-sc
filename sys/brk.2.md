# brk(2)

`brk` — 更改数据段大小

## 名称

`brk`, `sbrk`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
brk(const void *addr);

void *
sbrk(intptr_t incr);
```

## 描述

`brk()` 和 `sbrk()` 函数是现代虚拟内存管理出现之前的遗留接口。它们已弃用，且在 arm64 或 riscv 架构上不存在。应改用 [mmap(2)](mmap.2.md) 接口来分配页面。

`brk()` 和 `sbrk()` 函数用于更改进程数据段中所分配的内存量。它们通过移动“break”的位置来实现这一点。break 是进程未初始化数据段（也称为“BSS”）结束后的第一个地址。

`brk()` 函数将 break 设置为 `addr`。

`sbrk()` 函数将 break 提高 `incr` 字节，从而在数据段中分配至少 `incr` 字节的新内存。如果 `incr` 为负数，break 将降低 `incr` 字节。

## 注释

虽然内核维护的实际进程数据段大小只能按页大小增长或缩小，但这些函数允许将 break 设置为未对齐的值（即它可以指向数据段最后一页内的任何地址）。

程序的当前 break 值可以通过调用 `sbrk(0)` 来确定。另请参见 [end(3)](../man3/end.3.md)。

可以使用 [getrlimit(2)](getrlimit.2.md) 系统调用来确定数据段的最大允许大小。无法将 break 设置为超过“`etext` + `rlim.rlim_max`”，其中 `rlim.rlim_max` 的值由调用 `getrlimit(RLIMIT_DATA, &rlim)` 返回。（`etext` 的定义请参见 [end(3)](../man3/end.3.md)）。

## 返回值

`brk()` 函数成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

`sbrk()` 函数成功时返回先前的 break 值；否则返回值 (`void *`)-1，并设置全局变量 `errno` 以指示错误。

## 错误

`brk()` 和 `sbrk()` 函数在以下情况下会失败：

**[`EINVAL`]** 请求的 break 值超出数据段的起始位置。

**[`ENOMEM`]** 超过了由 setrlimit(2) 设置的数据段大小限制。

**[`ENOMEM`]** 交换区中空间不足，无法支持数据段的扩展。

## 参见

[execve(2)](execve.2.md), [getrlimit(2)](getrlimit.2.md), [mmap(2)](mmap.2.md), [end(3)](../man3/end.3.md), free(3), malloc(3)

## 历史

`brk()` 函数出现于 Version 7 AT&T UNIX。FreeBSD 11.0 引入了不支持 `brk()` 或 `sbrk()` 的 arm64 和 riscv 架构。

## 缺陷

将 `brk()` 或 `sbrk()` 与 malloc(3)、free(3) 或类似函数混用会导致不可移植的程序行为。

由于交换空间临时不足，设置 break 可能会失败。如果不参考 [getrlimit(2)](getrlimit.2.md)，无法将这种情况与因超过数据段最大大小而导致的失败区分开来。

`sbrk()` 有时被用于通过传入参数 0 来监视堆使用情况。在与基于 [mmap(2)](mmap.2.md) 的 malloc 结合使用时，其结果不太可能反映实际使用情况。

`brk()` 和 `sbrk()` 不是线程安全的。
