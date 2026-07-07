# vm_page_alloc(9)

`vm_page_alloc` — 分配一页内存

## 名称

`vm_page_alloc`

## 概要

```c
#include <sys/param.h>
#include <vm/vm.h>
#include <vm/vm_page.h>

vm_page_t
vm_page_alloc(vm_object_t object, vm_pindex_t pindex, int req)

vm_page_t
vm_page_alloc_after(vm_object_t object, vm_pindex_t pindex, int req,
    vm_page_t mpred)

vm_page_t
vm_page_alloc_contig(vm_object_t object, vm_pindex_t pindex, int req,
    u_long npages, vm_paddr_t low, vm_paddr_t high, u_long alignment,
    vm_paddr_t boundary, vm_memattr_t memattr)

vm_page_t
vm_page_alloc_contig_domain(vm_object_t object, vm_pindex_t pindex,
    int req, u_long npages, vm_paddr_t low, vm_paddr_t high,
    u_long alignment, vm_paddr_t boundary, vm_memattr_t memattr)

vm_page_t
vm_page_alloc_domain(vm_object_t object, vm_pindex_t pindex, int domain,
    int req)

vm_page_t
vm_page_alloc_domain_after(vm_object_t object, vm_pindex_t pindex,
    int domain, int req, vm_page_t mpred)

vm_page_t
vm_page_alloc_noobj(int req)

vm_page_t
vm_page_alloc_noobj_contig(int req, u_long npages, vm_paddr_t low,
    vm_paddr_t high, u_long alignment, vm_paddr_t boundary,
    vm_memattr_t memattr)

vm_page_t
vm_page_alloc_noobj_contig_domain(int domain, int req, u_long npages,
    vm_paddr_t low, vm_paddr_t high, u_long alignment, vm_paddr_t boundary,
    vm_memattr_t memattr)

vm_page_t
vm_page_alloc_noobj_domain(int domain, int req)
```

## 描述

`vm_page_alloc` 系列函数分配一个或多个物理内存页。大多数内核代码不应直接调用这些函数，而应使用内核内存分配器（如 [malloc(9)](malloc.9.md) 或 [uma(9)](uma.9.md)），或使用页缓存的更高层接口（如 [vm_page_grab(9)](vm_page_grab.9.md)）。

所有函数都接受一个 `req` 参数，该参数编码了分配优先级和可选的修饰标志，如下所述。名称中不包含 "noobj" 的函数还会将起始索引为 `pindex` 的页面插入到 VM 对象 `object` 中。该对象必须处于写锁定状态，且在指定索引处不能已有驻留页面。名称中包含 "domain" 的函数通过从 `domain` 指定的 [numa(4)](../man4/numa.4.md) 域返回页面来支持 NUMA 感知分配。

`vm_page_alloc_after` 和 `vm_page_alloc_domain_after` 函数的行为分别与 `vm_page_alloc` 和 `vm_page_alloc_domain` 相同，区别在于它们接受一个额外的参数 `mpred`，该参数必须是驻留在 `object` 中且索引小于 `pindex` 的最大索引页面，如果不存在这样的页面则为 `NULL`。这些函数的存在是为了优化在对象中按连续索引分配多个页面的循环这一常见情况。

`vm_page_alloc_contig` 和 `vm_page_alloc_noobj_contig` 函数及其 NUMA 感知变体分配满足指定约束的 `npages` 页物理连续运行。`low` 和 `high` 参数指定从中分配运行的物理地址范围。`alignment` 参数指定运行中第一页的请求对齐方式，必须是 2 的幂。如果 `boundary` 参数非零，则构成运行的页面不会跨越是该参数值（必须是 2 的幂）倍数的物理地址。如果 `memattr` 不等于 `VM_MEMATTR_DEFAULT`，则由 [pmap_enter(9)](pmap_enter.9.md) 或 [pmap_qenter(9)](pmap_qenter.9.md) 等创建的返回页面映射将携带内存属性的机器相关编码。此外，页面的直接映射（如果有）将被更新以反映请求的内存属性。

## 请求标志

所有页面分配器函数接受一个 `req` 参数来控制函数行为的某些方面。

`VM_ALLOC_WAITOK`、`VM_ALLOC_WAITFAIL` 和 `VM_ALLOC_NOWAIT` 标志指定在无法立即分配空闲页面时分配器的行为。`VM_ALLOC_WAITOK` 标志只能与 "noobj" 变体一起使用。如果指定了 `VM_ALLOC_NOWAIT`，则分配器放弃并返回 `NULL`。如果请求中没有任何标志，则隐式指定 `VM_ALLOC_NOWAIT`。如果指定了 `VM_ALLOC_WAITOK` 或 `VM_ALLOC_WAITFAIL`，分配器会将调用线程置于睡眠状态，直到有足够的空闲页面可用。此时，如果指定了 `VM_ALLOC_WAITFAIL`，分配器将返回 `NULL`；如果指定了 `VM_ALLOC_WAITOK`，分配器将重试分配。在失败的 `VM_ALLOC_WAITFAIL` 分配返回后，VM 对象（如果有）在线程睡眠期间已被解锁。在这种情况下，函数调用返回前将重新获取 VM 对象写锁。

`req` 还编码了分配请求优先级。默认情况下，分配的页面没有特殊处理。如果可用空闲页数低于某个水位线，分配将失败或分配线程将睡眠，具体取决于指定的等待标志。该水位线在引导时计算，对应于系统总物理内存的一小部分（不到百分之一）。要更积极地分配内存，可以指定以下标志之一：

**`VM_ALLOC_SYSTEM`** 如果空闲页数高于中断保留水位线，则可以分配页面。此标志仅在系统确实需要该页面时使用。

**`VM_ALLOC_INTERRUPT`** 仅在可用空闲页为零时分配才失败。此标志仅在分配失败后果比让系统没有空闲内存更严重时使用。例如，在分配内核页表页时使用此标志，此时分配失败会触发内核恐慌。

以下可选标志可以进一步修改分配器行为：

**`VM_ALLOC_SBUSY`** 返回的页面将为共享忙碌状态。此标志仅在 VM 对象中分配页面时指定。

**`VM_ALLOC_NOBUSY`** 返回的页面不会处于忙碌状态。在没有 VM 对象的情况下分配页面时，此标志是隐式的。在 VM 对象中分配页面时，如果未指定 `VM_ALLOC_SBUSY` 和 `VM_ALLOC_NOBUSY`，则返回的页面将以独占方式忙碌。

**`VM_ALLOC_NODUMP`** 无论是否映射到 KVA，返回的页面都不会包含在任何内核核心转储中。

**`VM_ALLOC_WIRED`** 返回的页面将被锁定。

**`VM_ALLOC_ZERO`** 如果指定此标志，"noobj" 变体将返回已清零的页面。其他分配器接口忽略此标志。

**`VM_ALLOC_NORECLAIM`** 如果指定此标志且请求无法立即满足，分配器不会尝试打破超级页预留来满足分配。当扫描预留队列的开销超过分配失败的成本时，这可能有用。此标志只能与 "contig" 变体一起使用，并且不得与 `VM_ALLOC_WAITOK` 组合指定。

**`VM_ALLOC_COUNT(n)`** 提示调用者在不久的将来将至少分配 `n` 页。`n` 不得超过 65535。如果系统缺少空闲页，此提示可能导致内核比其他方式更积极地回收内存。

**`VM_ALLOC_NOFREE`** 调用者断言返回的页面永远不会被释放。如果指定此标志，分配器将尝试从特殊的每域 arena 中获取页面，以抑制长期物理内存碎片。

## 返回值

如果分配成功，返回指向对应于已分配页面的 `struct vm_page` 的指针。如果分配请求指定了多个页面，返回的指针指向构成运行的 `struct vm_page` 数组。失败时返回 `NULL`。无论分配成功还是失败，VM 对象 `object` 在返回时都处于写锁定状态。

## 参见

[numa(4)](../man4/numa.4.md), [malloc(9)](malloc.9.md), [uma(9)](uma.9.md), [vm_page_grab(9)](vm_page_grab.9.md), [vm_page_sbusy(9)](vm_page_sbusy.9.md)

## 作者

本手册页由 Chad David <davidc@acns.ab.ca> 编写。
