# contigmalloc(9)

`contigmalloc` — 管理连续内核物理内存

## 名称

`contigmalloc`

## 概要

```c
#include <sys/types.h>
#include <sys/malloc.h>

void *
contigmalloc(unsigned long size, struct malloc_type *type, int flags,
    vm_paddr_t low, vm_paddr_t high, unsigned long alignment,
    vm_paddr_t boundary)

#include <sys/param.h>
#include <sys/domainset.h>

void *
contigmalloc_domainset(unsigned long size, struct malloc_type *type,
    struct domainset *ds, int flags, vm_paddr_t low, vm_paddr_t high,
    unsigned long alignment, vm_paddr_t boundary)
```

## 描述

`contigmalloc` 函数分配 `size` 字节的连续物理内存，对齐到 `alignment` 字节，且不跨越 `boundary` 字节的边界。如果成功，分配将位于物理地址 `low` 和 `high` 之间。返回的指针指向从内核虚拟地址（KVA）映射分配的 `size` 字节有线内核虚拟地址范围。

`contigmalloc_domainset` 变体允许调用者额外指定 [numa(4)](../man4/numa.4.md) 域选择策略。示例策略参见 [domainset(9)](domainset.9.md)。

`flags` 参数按以下方式修改 `contigmalloc` 的行为：

**`M_ZERO`** 使分配的物理内存被零填充。

**`M_NOWAIT`** 如果由于资源不足无法立即满足请求，使 `contigmalloc` 返回 `NULL`。

其他标志（如果存在）将被忽略。

`contigfree` 函数已弃用。请改用 [free(9)](free.9.md)。

## 实现说明

`contigmalloc` 函数不会睡眠等待内存资源被释放，而是在放弃之前主动回收页面。但是，除非指定 `M_NOWAIT`，否则它可能选择一个必须先写入后备存储的页面进行回收，从而导致睡眠。

## 返回值

`contigmalloc` 函数成功分配时返回内核虚拟地址，否则返回 `NULL`。

## 实例

```c
void *p;
p = contigmalloc(8192, M_DEVBUF, M_ZERO, 0, (1L << 22),
    32 * 1024, 1024 * 1024);
```

请求 8192 字节的零填充内存，位于物理地址 0 到 4194303（含）之间，对齐到 32K 边界，且不跨越 1M 地址边界。

## 诊断

如果 `size` 为零，或 `alignment` 或 `boundary` 不是 2 的幂，`contigmalloc` 函数将触发 panic。

## 参见

[malloc(9)](malloc.9.md), [memguard(9)](memguard.9.md)
