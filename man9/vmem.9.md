# vmem.9

`vmem` — 通用资源分配器

## 名称

`vmem`

## 概要

```c
#include <sys/vmem.h>

vmem_t *
vmem_create(const char *name, vmem_addr_t base, vmem_size_t size,
    vmem_size_t quantum, vmem_size_t qcache_max, int flags)

int
vmem_add(vmem_t *vm, vmem_addr_t addr, vmem_size_t size, int flags)

int
vmem_xalloc(vmem_t *vm, const vmem_size_t size, vmem_size_t align,
    const vmem_size_t phase, const vmem_size_t nocross,
    const vmem_addr_t minaddr, const vmem_addr_t maxaddr, int flags,
    vmem_addr_t *addrp)

void
vmem_xfree(vmem_t *vm, vmem_addr_t addr, vmem_size_t size)

int
vmem_alloc(vmem_t *vm, vmem_size_t size, int flags, vmem_addr_t *addrp)

void
vmem_free(vmem_t *vm, vmem_addr_t addr, vmem_size_t size)

void
vmem_destroy(vmem_t *vm)
```

## 描述

`vmem` 是一个通用资源分配器。尽管其名称如此，它可用于虚拟内存以外的任意资源。

`vmem_create` 创建一个新的 vmem arena。

**`name`** 描述 vmem 的字符串。

**`base`** 初始跨度的起始地址。如果不需要初始跨度，传入 `0`。

**`size`** 初始跨度的大小。如果不需要初始跨度，传入 `0`。

**`quantum`** 最小分配单位。

**`qcache_max`** 量子缓存可服务的最大分配大小。它只是一个提示，可以忽略。

**`flags`** [malloc(9)](malloc.9.md) 等待标志。

`vmem_add` 将从 `addr` 开始、大小为 `size` 的跨度添加到 arena。成功返回 0，失败返回 `ENOMEM`。`flags` 是 [malloc(9)](malloc.9.md) 等待标志。

`vmem_xalloc` 从 arena 分配资源。

**`vm`** 从中分配的 arena。

**`size`** 指定分配的大小。

**`align`** 如果为零，不关心分配的对齐。否则，请求从 `align` 对齐边界偏移 `phase` 处开始的资源段。

**`phase`** 参见上面 `align` 的描述。如果 `align` 为零，`phase` 应为零。否则，`phase` 应小于 `align`。

**`nocross`** 请求不跨越 `nocross` 对齐边界的资源。

**`minaddr`** 指定可分配的最小地址，如果调用者不关心则使用 `VMEM_ADDR_MIN`。

**`maxaddr`** 指定可分配的最大地址，如果调用者不关心则使用 `VMEM_ADDR_MAX`。

**`flags`** 分配策略和 [malloc(9)](malloc.9.md) 等待标志的按位或。分配策略为以下之一：

**`M_FIRSTFIT`** 优先分配性能。

**`M_BESTFIT`** 优先空间效率。

**`M_NEXTFIT`** 从上次搜索结束处开始执行地址有序的空闲地址搜索。

**`addrp`** 成功时，如果 `addrp` 不为 `NULL`，`vmem_xalloc` 用已分配跨度的起始地址覆盖它。

`vmem_xfree` 将 `vmem_xalloc` 分配的资源释放到 arena。

**`vm`** 释放到的 arena。

**`addr`** 被释放的资源。它必须是 `vmem_xalloc` 返回的。特别是，它不能是 `vmem_alloc` 返回的。否则，行为未定义。

**`size`** 被释放资源的大小。它必须与 `vmem_xalloc` 使用的 `size` 参数相同。

`vmem_alloc` 从 arena 分配资源。

**`vm`** 从中分配的 arena。

**`size`** 指定分配的大小。

**`flags`** `vmem` 分配策略标志（见上文）和 [malloc(9)](malloc.9.md) 睡眠标志的按位或。

**`addrp`** 成功时，如果 `addrp` 不为 `NULL`，`vmem_alloc` 用已分配跨度的起始地址覆盖它。

`vmem_free` 将 `vmem_alloc` 分配的资源释放到 arena。

**`vm`** 释放到的 arena。

**`addr`** 被释放的资源。它必须是 `vmem_alloc` 返回的。特别是，它不能是 `vmem_xalloc` 返回的。否则，行为未定义。

**`size`** 被释放资源的大小。它必须与 `vmem_alloc` 使用的 `size` 参数相同。

`vmem_destroy` 销毁一个 vmem arena。

**`vm`** 被销毁的 vmem arena。调用者应确保不再有人使用它。

## 返回值

`vmem_create` 返回指向新分配的 vmem_t 的指针。否则返回 `NULL`。

成功时，`vmem_xalloc` 和 `vmem_alloc` 返回 0。否则返回 `ENOMEM`。

## 代码参考

`vmem` 子系统在文件 **sys/kern/subr_vmem.c** 中实现。

## 参见

[malloc(9)](malloc.9.md)

libuvmem(3) 提供该分配器的用户空间移植。

Jeff Bonwick 和 Jonathan Adams，《Magazines and Vmem: Extending the Slab Allocator to Many CPUs and Arbitrary Resources》，2001 USENIX 年度技术会议，2001 年。

## 历史

`vmem` 分配器最初在 NetBSD 中实现。它在 FreeBSD 10.0 中引入。

## 作者

`vmem` 的原始实现由 YAMAMOTO Takashi 编写。FreeBSD 移植由 Jeff Roberson 完成。

## 缺陷

`vmem` 依赖 [malloc(9)](malloc.9.md)，因此不能在系统引导早期使用。
