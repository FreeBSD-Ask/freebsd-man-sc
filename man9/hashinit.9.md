# hashinit.9

`hashinit` — 管理内核哈希表

## 名称

`hashinit`

## 概要

```c
#include <sys/malloc.h>
```

```c
#include <sys/systm.h>
```

```c
#include <sys/queue.h>
```

```c
void *
hashinit(int nelements, struct malloc_type *type, u_long *hashmask)
void
hashinit_flags(int nelements, struct malloc_type *type, u_long *hashmask,
    int flags)
void
hashdestroy(void *hashtbl, struct malloc_type *type, u_long hashmask)
void *
phashinit(int nelements, struct malloc_type *type, u_long *nentries)
phashinit_flags(int nelements, struct malloc_type *type, u_long *nentries,
    int flags)
```

## 警告

此 KPI 已弃用，计划在 FreeBSD 17 中移除。请改用 [hashalloc(9)](hashalloc.9.md)。

## 描述

`hashinit`、`hashinit_flags`、`phashinit` 和 `phashinit_flags` 函数为大小由参数 `nelements` 给定的哈希表分配空间。

`hashinit` 函数分配大小为小于或等于参数 `nelements` 的最大 2 的幂的哈希表。`phashinit` 函数分配大小为小于或等于参数 `nelements` 的最大质数的哈希表。`hashinit_flags` 函数操作类似于 `hashinit`，但还接受额外参数 `flags`，控制分配期间的各种选项。`phashinit_flags` 函数操作类似于 `phashinit`，但还接受额外参数 `flags`，控制分配期间的各种选项。分配的哈希表是 LIST_HEAD(3) 条目的连续数组，使用 [malloc(9)](malloc.9.md) 分配，使用 LIST_INIT(3) 初始化。用于分配的 malloc 区域由参数 `type` 指向。

`hashdestroy` 函数释放参数 `hashtbl` 所指向的哈希表占用的空间。参数 `type` 确定释放空间时要使用的 malloc 区域。参数 `hashmask` 应为分配哈希表的 `hashinit` 调用返回的位掩码。参数 `flags` 必须使用以下值之一。

**`HASH_NOWAIT`** `hashinit_flags` 和 `phashinit_flags` 函数执行的任何 malloc 都不允许等待，因此可能失败。

**`HASH_WAITOK`** `hashinit_flags` 和 `phashinit_flags` 函数执行的任何 malloc 都允许等待内存。这也是 `hashinit` 和 `phashinit` 的行为。

## 实现说明

`phashinit` 选择的最大质数哈希值为 32749。

## 返回值

`hashinit` 函数返回指向已分配哈希表的指针，并将 `hashmask` 所指向的位置设置为用于计算哈希表中正确槽位的位掩码。

`phashinit` 函数返回指向已分配哈希表的指针，并将 `nentries` 所指向的位置设置为哈希表中的行数。

## 实例

典型示例如下：

```c
...
static LIST_HEAD(foo, foo) *footable;
static u_long foomask;
...
footable = hashinit(32, M_FOO, &foomask);
```

这里我们从 `M_FOO` 所指向的 malloc 区域分配具有 32 个条目的哈希表。分配的哈希表的掩码返回在 `foomask` 中。随后调用 `hashdestroy` 使用 `foomask` 中的值：

```c
...
hashdestroy(footable, M_FOO, foomask);
```

## 诊断

`hashinit` 和 `phashinit` 函数在参数 `nelements` 小于或等于零时将引发 panic。

`hashdestroy` 函数在 `hashtbl` 所指向的哈希表不为空时将引发 panic。

## 参见

[hashalloc(9)](hashalloc.9.md), LIST_HEAD(3), [malloc(9)](malloc.9.md)

## 缺陷

没有 `phashdestroy` 函数，使用 `hashdestroy` 释放由 `phashinit` 分配的哈希表通常会产生严重后果。
