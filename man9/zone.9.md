# zone.9

`UMA` — 通用内核对象分配器

## 名称

`UMA` — 通用内核对象分配器

## 概要

```c
#include <sys/param.h>
#include <sys/queue.h>
#include <vm/uma.h>

typedef int (*uma_ctor)(void *mem, int size, void *arg, int flags);
typedef void (*uma_dtor)(void *mem, int size, void *arg);
typedef int (*uma_init)(void *mem, int size, int flags);
typedef void (*uma_fini)(void *mem, int size);
typedef int (*uma_import)(void *arg, void **store, int count, int domain,
    int flags);
typedef void (*uma_release)(void *arg, void **store, int count);
typedef void *(*uma_alloc)(uma_zone_t zone, vm_size_t size, int domain,
    uint8_t *pflag, int wait);
typedef void (*uma_free)(void *item, vm_size_t size, uint8_t pflag);

uma_zone_t
uma_zcreate(char *name, size_t size, uma_ctor ctor, uma_dtor dtor,
    uma_init zinit, uma_fini zfini, int align, uint16_t flags);

uma_zone_t
uma_zcache_create(char *name, int size, uma_ctor ctor, uma_dtor dtor,
    uma_init zinit, uma_fini zfini, uma_import zimport,
    uma_release zrelease, void *arg, int flags);

uma_zone_t
uma_zsecond_create(char *name, uma_ctor ctor, uma_dtor dtor,
    uma_init zinit, uma_fini zfini, uma_zone_t master);

void
uma_zdestroy(uma_zone_t zone);

void *
uma_zalloc(uma_zone_t zone, int flags);

void *
uma_zalloc_arg(uma_zone_t zone, void *arg, int flags);

void *
uma_zalloc_domain(uma_zone_t zone, void *arg, int domain, int flags);

void *
uma_zalloc_pcpu(uma_zone_t zone, int flags);

void *
uma_zalloc_pcpu_arg(uma_zone_t zone, void *arg, int flags);

void *
uma_zalloc_smr(uma_zone_t zone, int flags);

void
uma_zfree(uma_zone_t zone, void *item);

void
uma_zfree_arg(uma_zone_t zone, void *item, void *arg);

void
uma_zfree_pcpu(uma_zone_t zone, void *item);

void
uma_zfree_pcpu_arg(uma_zone_t zone, void *item, void *arg);

void
uma_zfree_smr(uma_zone_t zone, void *item);

void
uma_prealloc(uma_zone_t zone, int nitems);

void
uma_zone_reserve(uma_zone_t zone, int nitems);

void
uma_zone_reserve_kva(uma_zone_t zone, int nitems);

void
uma_reclaim(int req);

void
uma_reclaim_domain(int req, int domain);

void
uma_zone_reclaim(uma_zone_t zone, int req);

void
uma_zone_reclaim_domain(uma_zone_t zone, int req, int domain);

void
uma_zone_set_allocf(uma_zone_t zone, uma_alloc allocf);

void
uma_zone_set_freef(uma_zone_t zone, uma_free freef);

int
uma_zone_set_max(uma_zone_t zone, int nitems);

void
uma_zone_set_maxcache(uma_zone_t zone, int nitems);

int
uma_zone_get_max(uma_zone_t zone);

int
uma_zone_get_cur(uma_zone_t zone);

void
uma_zone_set_warning(uma_zone_t zone, const char *warning);

void
uma_zone_set_maxaction(uma_zone_t zone, void (*maxaction)(uma_zone_t));

smr_t
uma_zone_get_smr(uma_zone_t zone);

void
uma_zone_set_smr(uma_zone_t zone, smr_t smr);
```

```c
#include <sys/sysctl.h>

SYSCTL_UMA_MAX(parent, nbr, name, access, zone, descr);
SYSCTL_ADD_UMA_MAX(ctx, parent, nbr, name, access, zone, descr);
SYSCTL_UMA_CUR(parent, nbr, name, access, zone, descr);
SYSCTL_ADD_UMA_CUR(ctx, parent, nbr, name, access, zone, descr);
```

## 描述

UMA（Universal Memory Allocator，通用内存分配器）为管理由相同大小的项组成的动态大小集合（称为 zone）提供了高效接口。zone 会跟踪哪些项正在使用、哪些未被使用，UMA 提供了从 zone 中分配项以及将项释放回 zone 的函数，使其可用于后续的分配请求。zone 维护每 CPU 缓存，在 SMP 系统上具备线性可扩展性，并为 NUMA 系统提供轮询（round-robin）和首次触碰（first-touch）策略。每个 CPU 缓存的项数量有上限，此外每个 zone 还维护一个无界缓存，用于快速满足每 CPU 缓存分配未命中的请求。

存在两种类型的 zone：常规 zone 和缓存 zone。在常规 zone 中，项从 slab 分配，slab 是从内核页面分配器分配的一个或多个虚拟连续内存页。在内部，slab 由 UMA keg 管理，keg 负责分配 slab 并跟踪一个或多个 zone 对其的使用情况。在典型用法中，每个 zone 对应一个 keg，因此 slab 不会在多个 zone 之间共享。

普通 zone 从 keg 导入项，并在需要时将项释放回该 keg。缓存 zone 没有 keg，而是使用自定义的导入和释放方法。例如，某些内核对象集合在引导时静态分配，且集合大小不再改变。缓存 zone 可用于为这类集合中的对象实现高效的分配器。

`uma_zcreate` 和 `uma_zcache_create` 函数分别用于创建新的常规 zone 和缓存 zone。`uma_zsecond_create` 函数创建一个常规 zone，该 zone 共享由 `master` 参数指定的 zone 的 keg。`name` 参数是 zone 的文本名称，用于调试和统计；在 zone 被释放之前，不应释放此内存。

`ctor` 和 `dtor` 参数是回调函数，分别在调用 `uma_zalloc` 和 `uma_zfree` 时由 UMA 子系统调用。其目的是为资源分配或释放时需要执行的初始化或销毁操作提供钩子。`ctor` 和 `dtor` 回调的一个良好用法是初始化嵌入在项中的数据结构，例如 [queue(3)](../man3/queue.3.md) 头。

`zinit` 和 `zfini` 参数用于优化 zone 中项的分配。当 UMA 子系统需要分配或释放项以满足请求或应对内存压力时，会调用它们。`zinit` 和 `zfini` 回调的一个良好用法是初始化和销毁项中包含的互斥锁。这样可以避免在每次项被释放和重新分配时销毁并重新初始化互斥锁。它们并非在每次调用 `uma_zalloc` 和 `uma_zfree` 时都被调用，而是在项被导入到 zone 的缓存时、以及 zone 将项释放给 slab 分配器时（通常作为对内存压力的响应）被调用。

对于 `uma_zcache_create`，`zimport` 和 `zrelease` 函数分别用于将项导入 zone 和从 zone 释放项。`zimport` 函数应将指向项的指针存储在 `store` 数组中，该数组最多包含 `count` 个条目。该函数必须返回导入的项数量，该数量可以小于最大值。类似地，传递给 `zrelease` 函数的 `store` 参数包含一个由 `count` 个指向项的指针组成的数组。传递给 `uma_zcache_create` 的 `arg` 参数会被提供给导入和释放函数。`zimport` 的 `domain` 参数指定分配所请求的 [numa(4)](../man4/numa.4.md) 域。它要么是一个 NUMA 域编号，要么是特殊值 `UMA_ANYDOMAIN`。

`uma_zcreate` 和 `uma_zcache_create` 的 `flags` 参数是以下标志的子集：

**`UMA_ZONE_NOFREE`**  
分配给 zone 的 keg 的 slab 永远不会被释放。

**`UMA_ZONE_NODUMP`**  
属于该 zone 的页面不会被包含在 minidump 中。

**`UMA_ZONE_PCPU`**  
从该 zone 的分配将拥有 `mp_ncpu` 个影子副本，这些副本被私下分配给各 CPU。CPU 可以使用分配基地址加上当前 CPU ID 与 `sizeof(struct pcpu)` 的乘积来寻址其私有副本：

```c
foo_zone = uma_zcreate(..., UMA_ZONE_PCPU);
 ...
foo_base = uma_zalloc(foo_zone, ...);
 ...
critical_enter();
foo_pcpu = (foo_t *)zpcpu_get(foo_base);
/* 使用 foo_pcpu 做一些操作 */
critical_exit();
```

注意，从 PCPU zone 分配项时不能使用 `M_ZERO`。要从 PCPU zone 获取零填充内存，请改用 `uma_zalloc_pcpu` 函数及其变体，并传入 `M_ZERO`。

**`UMA_ZONE_NOTOUCH`**  
UMA 子系统不能直接触碰（即读取或写入）slab 内存。否则，默认情况下，slab 中项的簿记可能在 slab 页面本身完成，`INVARIANTS` 内核也可能通过访问 slab 内存来进行释放后使用检查。

**`UMA_ZONE_ZINIT`**  
该 zone 的 `uma_init` 方法将被设置为内部方法，该方法将新分配的 slab 初始化为全零。不要将 `uma_init` 方法与 `uma_ctor` 混淆。带有 `UMA_ZONE_ZINIT` 标志的 zone 不会在每次 `uma_zalloc` 时都返回零填充内存。

**`UMA_ZONE_NOTPAGE`**  
将通过 `uma_zone_set_allocf` 提供分配器函数，且其返回的内存可能不是由页面数组中 VM 页面支持的内核虚拟内存。

**`UMA_ZONE_MALLOC`**  
该 zone 用于 [malloc(9)](malloc.9.md) 子系统。

**`UMA_ZONE_VM`**  
该 zone 用于 VM 子系统。

**`UMA_ZONE_CONTIG`**  
该 zone 中的项在物理地址空间中必须是连续的。项遵循正常的对齐约束，并且可以跨越具有连续物理地址的页面之间的边界。

**`UMA_ZONE_UNMANAGED`**  
默认情况下，UMA zone 缓存会被收缩以帮助缓解空闲页面短缺。长时间未使用的缓存项也可能从 zone 中被释放。设置此标志后，系统不会从该 zone 的缓存中回收内存。

**`UMA_ZONE_SMR`**  
创建一个其项将使用 [smr(9)](smr.9.md) 机制进行同步的 zone。创建时，该 zone 将关联一个 `smr_t` 结构，可通过 `uma_zone_get_smr` 获取。

可以使用 `uma_zdestroy` 销毁 zone，释放该 zone 中缓存的所有内存。在安全销毁 zone 之前，必须将从该 zone 分配的所有项释放回该 zone。

要从 zone 分配项，只需调用 `uma_zalloc` 并传入指向该 zone 的指针，同时将 `flags` 参数设置为 [malloc(9)](malloc.9.md) 中记录的所选标志。如果成功，它将返回指向项的指针；在 zone 中所有项都在使用且分配器无法扩展 zone 且指定了 `M_NOWAIT` 的罕见情况下，返回 `NULL`。

通过调用 `uma_zfree` 并传入指向 zone 的指针和指向项的指针，将项释放回分配它的 zone。如果 `item` 为 `NULL`，则 `uma_zfree` 不执行任何操作。

`uma_zalloc_arg` 和 `uma_zfree_arg` 变体允许调用者分别为 zone 的 `ctor` 和 `dtor` 函数指定参数。`uma_zalloc_pcpu` 和 `uma_zfree_pcpu` 变体分配和释放 `mp_ncpu` 个影子副本，如 `UMA_ZONE_PCPU` 中所述。如果 `item` 为 `NULL`，则 `uma_zfree_pcpu` 不执行任何操作。

`uma_zalloc_smr` 和 `uma_zfree_smr` 函数分配和释放来自启用 SMR 的 zone 的项，即使用 `UMA_ZONE_SMR` 创建的 zone 或已调用过 `uma_zone_set_smr` 的 zone。

`uma_zalloc_domain` 函数允许调用者指定固定的 [numa(4)](../man4/numa.4.md) 域进行分配。这使用了分配器中一条有保证但较慢的路径，该路径会降低并发性。

`uma_prealloc` 函数为所请求数量的项分配 slab，通常在 zone 初始创建之后调用。后续从该 zone 的分配将使用预分配的 slab 来满足。注意，slab 分配使用 `M_WAITOK` 标志执行，因此 `uma_prealloc` 可能会休眠。

`uma_zone_reserve` 函数设置 zone 的保留项数量。`uma_zalloc` 及其变体将确保 zone 包含至少所保留数量的空闲项。可以通过在分配请求标志中指定 `M_USE_RESERVE` 来分配保留项。`uma_zone_reserve` 本身不执行任何预分配。

`uma_zone_reserve_kva` 函数为所请求数量的项预分配内核虚拟地址空间。后续从该 zone 的分配将使用预分配的地址空间来满足。注意，与 `uma_zone_reserve` 不同，`uma_zone_reserve_kva` 不将预分配的使用限制为 `M_USE_RESERVE` 请求。

`uma_reclaim` 和 `uma_zone_reclaim` 函数从 UMA zone 回收缓存项，释放未使用的内存。`uma_reclaim` 函数从所有常规 zone 回收项，而 `uma_zone_reclaim` 仅从指定 zone 回收项。`req` 参数必须是以下三个值之一，指定回收项的激进程度：

**`UMA_RECLAIM_TRIM`**  
仅回收超出 zone 估计工作集大小的项。工作集大小会定期更新，并跟踪 zone 使用情况的近期历史。

**`UMA_RECLAIM_DRAIN`**  
从无界缓存中回收所有项。每 CPU 缓存中的空闲项保持不变。

**`UMA_RECLAIM_DRAIN_CPU`**  
回收所有缓存项。

`uma_reclaim_domain` 和 `uma_zone_reclaim_domain` 函数仅应用于从指定域分配的项。对于使用轮询 NUMA 策略的域，来自所有域的缓存项都会被释放给 keg，但只有来自特定域的 slab 会被释放。

`uma_zone_set_allocf` 和 `uma_zone_set_freef` 函数允许覆盖 zone 的默认 slab 分配和释放函数。如果必须使用具有特殊约束（如属性、对齐或地址范围）的内存，这很有用。

`uma_zone_set_max` 函数限制可以分配给 `zone` 的项数量（以及相应的内存）。`nitems` 参数指定所请求的项数量上限。有效上限会返回给调用者，因为由于实现会向上取整以确保分配给 zone 的所有内存页都被充分利用，最终上限可能高于请求值。该限制适用于 zone 中项的总数，包括已分配的项、空闲项和每 CPU 缓存中的空闲项。在多于一个 CPU 的系统上，即使没有内存短缺，也可能无法分配指定数量的项，因为当达到限制时，所有剩余的空闲项可能都在其他 CPU 的缓存中。

`uma_zone_set_maxcache` 函数限制 zone 中可以缓存的空闲项数量。此限制同时适用于每 CPU 缓存和空闲桶缓存。

`uma_zone_get_max` 函数返回 zone 的有效项数量上限。

`uma_zone_get_cur` 函数返回当前从 zone 分配的项数量的近似值。返回的值是近似的，因为实现未执行适当的同步来确定精确值。这确保了低开销，但代价是计算中可能使用了过时的数据。

`uma_zone_set_warning` 函数设置一个警告，当给定 zone 已满且分配项失败时，该警告将打印到系统控制台。警告的打印频率不超过每五分钟一次。通过将 `vm.zone_warnings` sysctl 可调参数设置为 `0`，可以全局关闭警告。

`uma_zone_set_maxaction` 函数设置一个函数，当给定 zone 已满且分配项失败时将调用该函数。调用该函数时 zone 处于锁定状态。此外，调用分配函数的函数可能持有额外的锁。因此，该函数应做非常少的工作（类似于信号处理程序）。

`uma_zone_set_smr` 函数将现有的 [smr(9)](smr.9.md) 结构与 UMA zone 关联。其效果类似于使用 `UMA_ZONE_SMR` 标志创建 zone，区别在于不会创建新的 SMR 结构。必须在从 zone 执行任何分配之前调用此函数。

`SYSCTL_UMA_MAX(parent, nbr, name, access, zone, descr)` 宏声明一个静态 [sysctl(9)](sysctl.9.md) oid，用于导出 zone 的有效项数量上限。`zone` 参数应为指向 `uma_zone_t` 的指针。读取该 oid 返回通过 `uma_zone_get_max` 获取的值。写入该 oid 通过 `uma_zone_set_max` 设置新值。提供 `SYSCTL_ADD_UMA_MAX(ctx, parent, nbr, name, access, zone, descr)` 宏用于动态创建此类 oid。

`SYSCTL_UMA_CUR(parent, nbr, name, access, zone, descr)` 宏声明一个静态只读 [sysctl(9)](sysctl.9.md) oid，用于导出 zone 的近似当前占用率。`zone` 参数应为指向 `uma_zone_t` 的指针。读取该 oid 返回通过 `uma_zone_get_cur` 获取的值。提供 `SYSCTL_ADD_UMA_CUR(ctx, parent, nbr, name, access, zone, descr)` 宏用于动态创建此类 oid。

## 实现说明

这些分配调用返回的内存不可执行。`uma_zalloc` 函数不支持 `M_EXEC` 标志来分配可执行内存。并非所有平台都强制区分可执行内存和不可执行内存。

## 参见

[numa(4)](../man4/numa.4.md), [vmstat(8)](../man8/vmstat.8.md), [malloc(9)](malloc.9.md), [smr(9)](smr.9.md)

> Jeff Bonwick, "The Slab Allocator: An Object-Caching Kernel Memory Allocator", 1994.

## 历史

zone 分配器首次出现在 FreeBSD 3.0 中。在 FreeBSD 5.0 中经过了根本性改动，以作为 slab 分配器运行。

## 作者

zone 分配器由 John S. Dyson 编写。zone 分配器的大部分由 Jeff Roberson <jeff@FreeBSD.org> 重写，以作为 slab 分配器运行。

本手册页由 Dag-Erling Smørgrav <des@FreeBSD.org> 编写。UMA 相关更改由 Jeroen Ruigrok van der Werven <asmodai@FreeBSD.org> 完成。
