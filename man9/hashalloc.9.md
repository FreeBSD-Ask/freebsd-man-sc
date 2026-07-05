# hashalloc.9

`hashalloc` — 分配和释放内核哈希表

## 名称

`hashalloc`, `hashfree`

## 概要

```c
#include <sys/malloc.h>
```

```c
#include <sys/hash.h>
```

```c
void *
hashalloc(struct hashalloc_args *args)
void
hashfree(void *table, struct hashalloc_args *args)
```

## 描述

`hashalloc` 和 `hashfree` 函数提供了灵活的内核编程接口 (KPI)，用于分配和释放具有可配置桶头的哈希表。

`hashalloc` 根据 `args` 结构中指定的参数为哈希表分配内存。它计算适当的桶数（根据请求的 `type` 调整 `args->size`），使用 [malloc(9)](malloc.9.md) 分配内存，初始化每个桶的队列头（例如 `LIST_HEAD`、`TAILQ_HEAD` 等），如果请求则初始化每桶锁。返回的内存分配可用作头结构数组，这些头结构以请求类型的已初始化列表头开始，后跟请求类型的已初始化锁。

`hashfree` 释放先前由 `hashalloc` 分配的哈希表。

这两个函数都要求调用者传递相同（或等效）的 `struct hashalloc_args`，该结构指定哈希表的所需配置，具有以下成员：

```c
struct hashalloc_args {
    /* 必需参数 */
    size_t  size;          /* 输入：所需桶数，输出：已分配 */
    int     mflags;            /* malloc(9) 标志 */
    struct malloc_type *mtype; /* malloc(9) 类型 */
    /* 可选参数 */
    size_t  hdrsize;            /* 桶头大小；0 = 自动 */
    enum {
        HASH_TYPE_POWER2,
        HASH_TYPE_PRIME,
    }       type;               /* 默认 HASH_TYPE_POWER2 */
    enum {
        HASH_HEAD_LIST,
        HASH_HEAD_CK_LIST,
        HASH_HEAD_SLIST,
        HASH_HEAD_CK_SLIST,
        HASH_HEAD_STAILQ,
        HASH_HEAD_CK_STAILQ,
        HASH_HEAD_TAILQ,
    }       head;               /* 默认 HASH_HEAD_LIST */
    enum {
        HASH_LOCK_NONE,
        HASH_LOCK_MTX,
        HASH_LOCK_RWLOCK,
        HASH_LOCK_SX,
        HASH_LOCK_RMLOCK,
        HASH_LOCK_RMSLOCK,
    }       lock;               /* 默认 HASH_LOCK_NONE */
    int     lopts;              /* 锁初始化选项 */
    const char *lname;          /* 锁名称 */
    int  (*ctor)(void *);	/* 桶构造函数 */
    void (*dtor)(void *);	/* 桶析构函数 */
    /* 返回参数 */
    int error;                  /* 失败时的错误代码 */
};
```

`hashalloc` 需要参数成员 `size`、`mflags` 和 `mtype`。`hashfree` 需要参数 `size`（由先前调用 `hashalloc` 填充）和 `mtype`。其余参数是可选的并具有合理的默认值。以非默认分配参数分配的哈希表应向 `hashfree` 传递相同的参数。该结构应使用稀疏 C99 初始化器初始化，因为它可能包含不透明的扩展成员。该结构可在调用者的栈上分配。

**`HASH_TYPE_POWER2`** 向上取整到小于或等于参数 `size` 的最大 2 的幂。

**`HASH_TYPE_PRIME`** 调整到小于或等于参数 `size` 的最大质数。

**`HASH_HEAD_LIST`** [queue(3)](../man3/queue.3.md) `LIST_HEAD`

**`HASH_HEAD_CK_LIST`** Concurrency-kit `CK_LIST_HEAD`

**`HASH_HEAD_SLIST`** [queue(3)](../man3/queue.3.md) `SLIST_HEAD`

**`HASH_HEAD_CK_SLIST`** Concurrency-kit `CK_SLIST_HEAD`

**`HASH_HEAD_STAILQ`** [queue(3)](../man3/queue.3.md) `STAILQ_HEAD`

**`HASH_HEAD_CK_STAILQ`** Concurrency-kit `CK_STAILQ_HEAD`

**`HASH_HEAD_TAILQ`** [queue(3)](../man3/queue.3.md) `TAILQ_HEAD`

**`HASH_LOCK_NONE`** 无每桶锁。

**`HASH_LOCK_MTX`** 每桶 [mutex(9)](mutex.9.md)。

**`HASH_LOCK_RWLOCK`** 每桶 [rwlock(9)](rwlock.9.md)。

**`HASH_LOCK_SX`** 每桶 [sx(9)](sx.9.md)。

**`HASH_LOCK_RMLOCK`** 每桶 [rmlock(9)](rmlock.9.md)。

**`HASH_LOCK_RMSLOCK`** 每桶可休眠 (rms) [rmlock(9)](rmlock.9.md)。

**`size`** `hashalloc` 所需的桶数。成功返回时，`hashalloc` 将此成员设置为实际分配的数量（可能向上取整到 2 的幂或最近的质数）。`hashalloc` 返回的值应随后提供给 `hashfree`。

**`mflags`**, `mtype` 直接传递给 [malloc(9)](malloc.9.md)。

**`hdrsize`** 允许调用者设置不同（增大）桶头大小的可选成员。

**`type`** 桶计数策略：默认为 `HASH_TYPE_POWER2`。

**`head`** 每个桶的队列头类型，[queue(3)](../man3/queue.3.md) 或 Concurrency-kit (CK) 类型。默认为 `HASH_HEAD_LIST`。

**`lock`** 同步：默认为 `HASH_LOCK_NONE`。

**`lopts`** 传递给 mtx_init(9)、rw_init(9)、sx_init(9)、rm_init(9) 或 rms_init(9) 的选项（如果启用了锁定）。

**`lname`** 锁名称。除非 `lock` 为 `HASH_LOCK_NONE`，否则此成员是必需的。

**`ctor`** 可选构造函数，由 `hashalloc` 在列表头和锁初始化后为每个桶调用。可能因错误代码失败，导致 `hashalloc` 失败。

**`dtor`** 可选析构函数，由 `hashfree` 在锁析构函数和列表空检查之前为每个桶调用。

## 返回值

`hashalloc` 成功时返回指向已分配并初始化的哈希表的指针，内存分配失败或构造函数失败时返回 `NULL`。`args` 的 `error` 成员设置为适当的错误代码。当 `args` 中的 `mflags` 包含 `M_WAITOK` 标志且 `ctor` 为 NULL 或从不失败时，`hashalloc` 从不失败。

## 实例

使用 TAILQ 桶的简单互斥锁保护哈希表：

```c
struct bucket {
    TAILQ_HEAD(, foo)   head;
    struct mtx          lock;
} *table;
struct hashalloc_args args = {
    .size    = 9000,
    .mflags  = M_WAITOK,
    .mtype   = M_FOO,
    .head    = HASH_HEAD_TAILQ,
    .lock    = HASH_LOCK_MTX,
    .lopts   = MTX_DEF,
    .lname   = "bucket of foo",
};
table = hashalloc(&args);
/* 将 table 用作 struct bucket 数组 ... */
mtx_lock(&table[hash].lock);
TAILQ_INSERT_HEAD(&table[hash].head, foo, next);
/* 稍后 */
hashfree(table, &args);
```

## 参见

[malloc(9)](malloc.9.md), [mutex(9)](mutex.9.md), [rmlock(9)](rmlock.9.md), [rwlock(9)](rwlock.9.md), [sx(9)](sx.9.md), [queue(3)](../man3/queue.3.md)

## 历史

`hashfree` KPI 首次出现于 FreeBSD 16.0。它取代了自 4.4BSD 以来可用的旧接口 `hashinit`，通过提供对哈希表结构和锁定策略的更大控制。

## 作者

Gleb Smirnoff <glebius@FreeBSD.org>
