# malloc.9

`malloc` — 内核内存管理例程

## 名称

`malloc`, `mallocarray`, `free`, `zfree`, `realloc`, `reallocf`, `malloc_usable_size`, `malloc_aligned`, `malloc_exec`, `MALLOC_DECLARE`, `MALLOC_DEFINE`, `malloc_domainset`, `malloc_domainset_aligned`, `malloc_domainset_exec`, `mallocarray_domainset`

## 概要

`#include <sys/types.h>`

`#include <sys/malloc.h>`

`Ft void * Fn malloc size_t size struct malloc_type *type int flags Ft void * Fn mallocarray size_t nmemb size_t size struct malloc_type *type int flags Ft void Fn free void *addr struct malloc_type *type Ft void Fn zfree void *addr struct malloc_type *type Ft void * Fn realloc void *addr size_t size struct malloc_type *type int flags Ft void * Fn reallocf void *addr size_t size struct malloc_type *type int flags Ft size_t Fn malloc_usable_size const void *addr Ft void * Fo malloc_aligned size_t size size_t align struct malloc_type *type int flags Fc Ft void * Fn malloc_exec size_t size struct malloc_type *type int flags Fn MALLOC_DECLARE type`

`#include <sys/param.h>`

`#include <sys/malloc.h>`

`#include <sys/kernel.h>`

`Fn MALLOC_DEFINE type shortdesc longdesc`

`#include <sys/param.h>`

`#include <sys/domainset.h>`

`#include <sys/malloc.h>`

`Ft void * Fn malloc_domainset size_t size struct malloc_type *type struct domainset *ds int flags Ft void * Fo malloc_domainset_aligned size_t size size_t align struct malloc_type *type struct domainset *ds int flags Fc Ft void * Fn malloc_domainset_exec size_t size struct malloc_type *type struct domainset *ds int flags Ft void * Fn mallocarray_domainset size_t nmemb size_t size struct malloc_type *type struct domainset *ds int flags`

## 描述

`malloc` 函数在内核地址空间中为大小由 `size` 指定的对象分配未初始化的内存。

`malloc_domainset` 变体使用指定的域选择策略从特定的 [numa(4)](../man4/numa.4.md) 域分配内存。有关一些示例策略，请参见 [domainset(9)](domainset.9.md)。

`malloc_aligned` 和 `malloc_domainset_aligned` 变体返回按 `align` 指定的对齐方式的分配，`align` 必须非零、为 2 的幂且小于或等于页面大小。

`malloc_exec` 和 `malloc_domainset_exec` 都可用于返回可执行内存。并非所有平台都强制区分可执行和不可执行内存。

`mallocarray` 函数在内核地址空间中为 `nmemb` 个元素的数组分配未初始化的内存，每个元素的大小由 `size` 指定。

`mallocarray_domainset` 变体使用指定的域选择策略从特定的 [numa(4)](../man4/numa.4.md) 域分配内存。有关一些示例策略，请参见 [domainset(9)](domainset.9.md)。

`free` 函数释放先前由 `malloc` 分配的地址 `addr` 处的内存以供重用。内存不会被清零。如果 `addr` 为 `NULL`，则 `free` 不执行任何操作。

与 `free` 一样，`zfree` 函数释放先前由 `malloc` 分配的地址 `addr` 处的内存以供重用。但是，`zfree` 会在释放内存之前将其清零。

`realloc` 函数将 `addr` 引用的先前分配的内存大小更改为 `size` 字节。内存的内容在新旧大小中较小者之前保持不变。注意，返回值可能与 `addr` 不同。如果无法分配请求的内存，则返回 `NULL`，并且 `addr` 引用的内存有效且未更改。如果 `addr` 为 `NULL`，则 `realloc` 函数对于指定大小的行为与 `malloc` 完全相同。

`reallocf` 函数与 `realloc` 相同，只是在无法分配请求的内存时会释放传递的指针。

`malloc_usable_size` 函数返回 `addr` 所指向分配的可用大小。返回值可能大于分配期间请求的大小。

与其标准 C 库对应物 malloc(3) 不同，内核版本需要两个额外的参数。`flags` 参数进一步限定 `malloc` 的操作特性，如下所示：

**`M_ZERO`** 导致分配的内存被设置为全零。

**`M_NODUMP`** 对于大于页面大小的分配，导致分配的内存被排除在内核核心转储之外。

**`M_NOWAIT`** 如果由于资源短缺无法立即满足请求，则导致 `malloc`、`realloc` 和 `reallocf` 返回 `NULL`。注意，在中断上下文中运行时需要 `M_NOWAIT`。

**`M_WAITOK`** 表示可以等待资源。如果无法立即满足请求，则当前进程将被置于睡眠状态，等待其他进程释放资源。如果指定了 `M_WAITOK`，则 `malloc`、`mallocarray`、`realloc` 和 `reallocf` 函数不能返回 `NULL`。如果 `nmemb` 和 `size` 的乘积会导致整数溢出，则 `mallocarray` 函数会引发 panic。

**`M_USE_RESERVE`** 表示系统可以使用其内存储备来满足请求。此选项仅应与 `M_NOWAIT` 结合使用，且仅当调用者无法容忍分配失败且对系统有灾难性影响时。

**`M_NEVERFREED`** 这是 uma(9) 分配器使用的内部标志，不应在常规 `malloc` 调用中使用。有关更多详细信息，请参见 [vm_page_alloc(9)](vm_page_alloc.9.md) 中 VM_ALLOC_NOFREE 的描述。

必须指定 `M_WAITOK` 或 `M_NOWAIT` 中的一个。

`type` 参数用于执行内存使用统计和基本完整性检查。它可用于标识多个分配。可以通过 ‘vmstat -m’ 检查统计信息。

`type` 通过 `MALLOC_DECLARE` 和 `MALLOC_DEFINE` 宏使用 `struct malloc_type` 定义。

```c
/* sys/something/foo_extern.h */
MALLOC_DECLARE(M_FOOBUF);
/* sys/something/foo_main.c */
MALLOC_DEFINE(M_FOOBUF, "foobuffers", "Buffers to foo data into the ether");
/* sys/something/foo_subr.c */
...
buf = malloc(sizeof(*buf), M_FOOBUF, M_NOWAIT);
```

为了使用 `MALLOC_DEFINE`，必须包含

`#include <sys/param.h>`

（而不是

`#include <sys/types.h>`

和

`#include <sys/kernel.h>`

## 上下文

`malloc`、`realloc` 和 `reallocf` 不能从快速中断处理程序中调用。从线程化中断调用时，`flags` 必须包含 `M_NOWAIT`。

`malloc`、`realloc` 和 `reallocf` 在以 `M_WAITOK` 调用时可能会睡眠。`free` 从不睡眠。但是，`malloc`、`realloc`、`reallocf` 和 `free` 不能在临界区或持有自旋锁时调用。

在持有 [vnode(9)](vnode.9.md) 互锁时调用 `malloc`（即使使用 `M_NOWAIT`）或 `free` 会由于 VM 对象和 Vnode 的交织而导致 LOR（锁顺序反转）。

## 实现说明

内存分配器以大小为 2 的幂的块为单位分配内存，用于不超过一页内存大小的请求。对于更大的请求，则分配一个或多个页面。虽然不应依赖此信息，但它可能对优化内存使用效率有用。

## 返回值

`malloc`、`realloc` 和 `reallocf` 函数返回一个适合存储任何类型对象的适当对齐的内核虚拟地址，如果无法满足请求（意味着设置了 `M_NOWAIT`），则返回 `NULL`。

## 诊断

使用 `INVARIANTS` 配置选项编译的内核会尝试检测由诸如写入分配区域之外以及对 `malloc` 和 `free` 函数的不平衡调用之类的事情导致的内存损坏。一致性检查失败将导致 panic 或系统控制台消息。

## 参见

[dtrace_dtmalloc(4)](../man4/dtrace_dtmalloc.4.md), [numa(4)](../man4/numa.4.md), [vmstat(8)](../man8/vmstat.8.md), [contigmalloc(9)](contigmalloc.9.md), [domainset(9)](domainset.9.md), [memguard(9)](memguard.9.md), [vnode(9)](vnode.9.md)

## 历史

`zfree` 首次出现于 FreeBSD 13.0。
