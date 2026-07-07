# buf_ring(9)

`buf_ring` — 多生产者、{单, 多}消费者无锁环形缓冲区

## 名称

`buf_ring`, `buf_ring_alloc`, `buf_ring_free`, `buf_ring_enqueue`, `buf_ring_dequeue_mc`, `buf_ring_dequeue_sc`, `buf_ring_count`, `buf_ring_empty`, `buf_ring_full`, `buf_ring_peek`

## 概要

```c
#include <sys/param.h>
#include <sys/buf_ring.h>

struct buf_ring *
buf_ring_alloc(int count, struct malloc_type *type, int flags,
    struct mtx *sc_lock)

void
buf_ring_free(struct buf_ring *br, struct malloc_type *type)

int
buf_ring_enqueue(struct buf_ring *br, void *buf)

void *
buf_ring_dequeue_mc(struct buf_ring *br)

void *
buf_ring_dequeue_sc(struct buf_ring *br)

int
buf_ring_count(struct buf_ring *br)

int
buf_ring_empty(struct buf_ring *br)

int
buf_ring_full(struct buf_ring *br)

void *
buf_ring_peek(struct buf_ring *br)
```

## 描述

buf_ring 函数提供无锁多生产者和无锁多消费者以及单消费者环形缓冲区。

`buf_ring_alloc` 函数用于分配具有 `count` 个槽位的 buf_ring 环形缓冲区，使用 malloc_type `type` 和内存标志 `flags`。单消费者接口由 `sc_lock` 保护。

`buf_ring_free` 函数用于释放 buf_ring。用户负责释放任何已入队的项。

`buf_ring_enqueue` 函数用于将缓冲区入队到 buf_ring。

`buf_ring_dequeue_mc` 函数是从 buf_ring 出队元素的多消费者安全方式。

`buf_ring_dequeue_sc` 函数是出队元素的单消费者接口，要求用户使用锁串行化访问。

`buf_ring_count` 函数返回 buf_ring 中的元素数量。

`buf_ring_empty` 函数在 buf_ring 为空时返回 `TRUE`，否则返回 `FALSE`。

`buf_ring_full` 函数在不能再入队更多项时返回 `TRUE`，否则返回 `FALSE`。

`buf_ring_peek` 函数在 buf_ring 不为空时返回指向 buf_ring 中最后一个元素的指针，否则返回 `NULL`。

## 返回值

`buf_ring_enqueue` 函数在 buf_ring 中没有可用槽位时返回 `ENOBUFS`。

## 历史

这些函数引入于 FreeBSD 8.0。
