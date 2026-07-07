# drbr(9)

`drbr` — 网络驱动到 buf_ring 的接口

## 名称

`drbr`, `drbr_free`, `drbr_enqueue`, `drbr_dequeue`, `drbr_dequeue_cond`, `drbr_flush`, `drbr_empty`, `drbr_inuse`

## 概要

```c
#include <sys/param.h>
#include <net/if.h>
#include <net/if_var.h>
```

```c
void
drbr_free(struct buf_ring *br, struct malloc_type *type)

int
drbr_enqueue(struct ifnet *ifp, struct buf_ring *br, struct mbuf *m)

struct mbuf *
drbr_dequeue(struct ifnet *ifp, struct buf_ring *br)

struct mbuf *
drbr_dequeue_cond(struct ifnet *ifp, struct buf_ring *br,
    int (*func)(struct mbuf *, void *), void *arg)

void
drbr_flush(struct ifnet *ifp, struct buf_ring *br)

int
drbr_empty(struct ifnet *ifp, struct buf_ring *br)

int
drbr_inuse(struct ifnet *ifp, struct buf_ring *br)
```

## 描述

`drbr_inuse` 系列函数为网络驱动提供使用 [buf_ring(9)](buf_ring.9.md) 进行数据包入队和出队的 API。它旨在替代用于数据包排队的 IFQ 接口。它允许使用单个原子操作将数据包入队，并且在驱动 tx 队列锁的保护下进行数据包出队时无需任何每包原子操作。如果启用了 `INVARIANTS`，调用 `drbr_dequeue` 时会断言已持有 tx 队列锁。

`drbr_free` 函数释放所有入队的 mbuf，然后释放 buf_ring。

`drbr_enqueue` 函数用于将 mbuf 入队到 buf_ring，如果启用了 ALTQ(4) 则回退到 ifnet 的 IFQ。

`drbr_dequeue` 函数用于从 buf_ring 中出队一个 mbuf，如果启用了 ALTQ(4) 则从 ifnet 的 IFQ 出队。

`drbr_dequeue_cond` 函数用于根据 `func` 返回 `TRUE` 或 `FALSE` 有条件地从 buf_ring 中出队一个 mbuf。

`drbr_flush` 函数释放所有入队到 buf_ring 和 ifnet IFQ 中的 mbuf。

`drbr_empty` 函数在没有入队 mbuf 时返回 `TRUE`，否则返回 `FALSE`。

`drbr_inuse` 函数返回已入队的 mbuf 数量。请注意，这本质上存在竞态条件，因为无法保证在实际调用 `drbr_dequeue` 时不会有更多 mbuf。只要持有 tx 队列锁，已入队的 mbuf 数量不会更少。

## 返回值

`drbr_enqueue` 函数在 buf_ring 中无可用槽位时返回 `ENOBUFS`，成功时返回 `0`。

`drbr_dequeue` 和 `drbr_dequeue_cond` 函数成功时返回一个 mbuf，buf_ring 为空时返回 `NULL`。

## 历史

这些函数引入于 FreeBSD 8.0。
