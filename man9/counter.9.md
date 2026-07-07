# counter(9)

`counter` — SMP 友好的内核计数器实现

## 名称

`counter`

## 概要

```c
#include <sys/types.h>
#include <sys/systm.h>
#include <sys/counter.h>

counter_u64_t
counter_u64_alloc(int wait)

void
counter_u64_free(counter_u64_t c)

void
counter_u64_add(counter_u64_t c, int64_t v)

void
counter_enter(void)

void
counter_exit(void)

void
counter_u64_add_protected(counter_u64_t c, int64_t v)

uint64_t
counter_u64_fetch(counter_u64_t c)

void
counter_u64_zero(counter_u64_t c)

struct counter_rate *
counter_rate_alloc(int flags, int period)

int64_t
counter_ratecheck(struct counter_rate *cr, int64_t limit)

uint64_t
counter_rate_get(struct counter_rate *cr)

void
counter_rate_free(struct counter_rate *cr)

COUNTER_U64_SYSINIT(counter_u64_t c)

COUNTER_U64_DEFINE_EARLY(counter_u64_t c)

#include <sys/sysctl.h>

SYSCTL_COUNTER_U64(parent, nbr, name, access, ptr, descr)

SYSCTL_ADD_COUNTER_U64(ctx, parent, nbr, name, access, ptr, descr)

SYSCTL_COUNTER_U64_ARRAY(parent, nbr, name, access, ptr, len, descr)

SYSCTL_ADD_COUNTER_U64_ARRAY(ctx, parent, nbr, name, access, ptr, len, descr)
```

## 描述

`counter` 是创建可用于任何目的（如收集统计数据）的计数器的通用工具。当多个内核线程同时更新时，`counter` 保证无损。但是，`counter` 不会阻塞调用线程，更新也不使用 [atomic(9)](atomic.9.md) 操作，因此计数器可在任何非中断上下文中使用。此外，`counter` 对 SMP 环境有特殊优化，使 `counter` 更新比简单地对全局变量进行算术运算更快。因此，`counter` 被认为适合在性能关键的代码路径中进行记账。

**`counter_u64_alloc(wait)`** 分配一个新的 64 位无符号计数器。`wait` 参数是 [malloc(9)](malloc.9.md) 等待标志，应为 `M_NOWAIT` 或 `M_WAITOK`。如果指定 `M_NOWAIT`，操作可能失败并返回 `NULL`。

**`counter_u64_free(c)`** 释放先前分配的计数器 `c`。可以安全地传递 `NULL`。

**`counter_u64_add(c, v)`** 将 `v` 加到 `c`。KPI 不保证对回绕的任何保护。

**`counter_enter()`** 进入允许通过 `counter_u64_add_protected` 安全更新多个计数器的模式。在某些机器上，这展开为 [critical(9)](critical.9.md) 节，而在其他机器上则是空操作。参见“实现说明”章节。

**`counter_exit()`** 退出更新多个计数器的模式。

**`counter_u64_add_protected(c, v)`** 与 `counter_u64_add` 相同，但应先调用 `counter_enter`。

**`counter_u64_fetch(c)`** 获取计数器 `c` 的快照。获得的数据不保证反映任何时刻的真实累积值。

**`counter_u64_zero(c)`** 清除计数器 `c` 并将其设为零。

**`counter_rate_alloc(flags, period)`** 分配新的 struct counter_rate。`flags` 传递给 [malloc(9)](malloc.9.md)。`period` 是检查速率的时间段。

**`counter_ratecheck(cr, limit)`** 该函数是 `ppsratecheck` 的多处理器友好版本，内部使用 `counter`。如果当前周期内尚未达到速率，返回非负值，否则返回负值。如果在前一个周期达到限制但刚刚重置为零，则 `counter_ratecheck` 返回自上次重置以来事件的数量。

**`counter_rate_get(cr)`** 当前周期内此检查的命中次数。

**`counter_rate_free(cr)`** 释放 `cr` 计数器。

**`COUNTER_U64_SYSINIT(c)`** 为全局计数器 `c` 定义 [SYSINIT(9)](sysinit.9.md) 初始化程序。

**`COUNTER_U64_DEFINE_EARLY(c)`** 定义并初始化全局计数器 `c`。递增 `c` 始终安全，但在 `SI_SUB_COUNTER` [SYSINIT(9)](sysinit.9.md) 事件之前的更新会丢失。

**`SYSCTL_COUNTER_U64(parent, nbr, name, access, ptr, descr)`** 声明一个表示 `counter` 的静态 [sysctl(9)](sysctl.9.md) oid。`ptr` 参数应是指向已分配 `counter_u64_t` 的指针。读取 oid 返回通过 `counter_u64_fetch` 获取的值。任何对 oid 的写入都会将其清零。

**`SYSCTL_ADD_COUNTER_U64(ctx, parent, nbr, name, access, ptr, descr)`** 创建一个表示 `counter` 的 [sysctl(9)](sysctl.9.md) oid。`ptr` 参数应是指向已分配 `counter_u64_t` 的指针。读取 oid 返回通过 `counter_u64_fetch` 获取的值。任何对 oid 的写入都会将其清零。

**`SYSCTL_COUNTER_U64_ARRAY(parent, nbr, name, access, ptr, len, descr)`** 声明一个表示 `counter` 数组的静态 [sysctl(9)](sysctl.9.md) oid。`ptr` 参数应是指向已分配 `counter_u64_t` 数组的指针。`len` 参数应指定数组中的元素数量。读取 oid 返回通过 `counter_u64_fetch` 获取的 `uint64_t` 值的 len 大小数组。任何对 oid 的写入都会将所有数组元素清零。

**`SYSCTL_ADD_COUNTER_U64_ARRAY(ctx, parent, nbr, name, access, ptr, len, descr)`** 创建一个表示 `counter` 数组的 [sysctl(9)](sysctl.9.md) oid。`ptr` 参数应是指向已分配 `counter_u64_t` 数组的指针。`len` 参数应指定数组中的元素数量。读取 oid 返回通过 `counter_u64_fetch` 获取的 `uint64_t` 值的 len 大小数组。任何对 oid 的写入都会将所有数组元素清零。

## 实现说明

在所有架构上，`counter` 使用在内存中特殊对齐的每 CPU 数据字段实现，以避免由于 CPU 之间共享变量而导致的 CPU 间总线流量。这些字段使用 `UMA_ZONE_PCPU` [uma(9)](uma.9.md) 区分配。更新操作仅触及当前 CPU 私有的字段。获取操作遍历所有每 CPU 字段并获取所有字段快照总和。

在 amd64 上，`counter` 更新实现为不带锁语义的单条指令，对当前 CPU 的私有数据操作，对抢占和中断安全。

在 i386 架构上，当机器支持 cmpxchg8 指令时，使用此指令。多指令序列提供与 amd64 单指令实现相同的保证。

在某些架构上，更新计数器需要 [critical(9)](critical.9.md) 节。

## 实例

以下示例创建一个通过 sysctl 导出到用户空间的静态计数器数组：

```c
#define MY_SIZE 8
static counter_u64_t array[MY_SIZE];
SYSCTL_COUNTER_U64_ARRAY(_debug, OID_AUTO, counter_array, CTLFLAG_RW,
    &array[0], MY_SIZE, "Test counter array");
```

## 参见

[atomic(9)](atomic.9.md), [critical(9)](critical.9.md), [locking(9)](locking.9.md), [malloc(9)](malloc.9.md), [ratecheck(9)](ratecheck.9.md), [sysctl(9)](sysctl.9.md), [SYSINIT(9)](sysinit.9.md), [uma(9)](uma.9.md)

## 历史

`counter` 工具首次出现于 FreeBSD 10.0。

## 作者

`counter` 工具由 Gleb Smirnoff 和 Konstantin Belousov 编写。
