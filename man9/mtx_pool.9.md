# mtx_pool.9.md

`mtx_pool` — 互斥锁池例程

## 名称

`mtx_pool`, `mtx_pool_alloc`, `mtx_pool_find`, `mtx_pool_lock`, `mtx_pool_lock_spin`, `mtx_pool_unlock`, `mtx_pool_unlock_spin`, `mtx_pool_create`, `mtx_pool_destroy`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/lock.h>
```

```c
#include <sys/mutex.h>
```

```c
struct mtx *
mtx_pool_alloc(struct mtx_pool *pool)

struct mtx *
mtx_pool_find(struct mtx_pool *pool, void *ptr)

void
mtx_pool_lock(struct mtx_pool *pool, void *ptr)

void
mtx_pool_lock_spin(struct mtx_pool *pool, void *ptr)

void
mtx_pool_unlock(struct mtx_pool *pool, void *ptr)

void
mtx_pool_unlock_spin(struct mtx_pool *pool, void *ptr)

struct mtx_pool *
mtx_pool_create(const char *mtx_name, int pool_size, int opts)

void
mtx_pool_destroy(struct mtx_pool **poolp)
```

## 描述

互斥锁池旨在用作短期叶互斥锁；即在调用 mtx_sleep(9) 之前可能获取的最后一个互斥锁。它们使用一个共享的互斥锁池进行操作。可以根据提供的指针从池中选择一个互斥锁，该指针可以指向有效的内容，也可以不指向任何有效内容；或者调用者可以从池中分配一个任意的共享互斥锁，并保存返回的互斥锁指针以供以后使用。

默认创建的 `mtxpool_sleep` 互斥锁池中的共享互斥锁是标准的、非递归的、可阻塞的互斥锁，只应在适当的场合使用。`mtxpool_lockbuilder` 互斥锁池中的互斥锁类似，区别在于它们使用 MTX_NOWITNESS 标志初始化，以便可用于构建更高层级的锁。还可以创建包含具有不同属性（如自旋互斥锁）的互斥锁的其他互斥锁池。

调用者可以对池例程返回的互斥锁进行加锁和解锁，但由于这些互斥锁是共享的，调用者不应试图销毁它们或修改其特性。虽然池互斥锁通常是叶互斥锁（意味着获取一个之后无法依赖任何排序保证），但在仔细控制的情况下仍然可以获取其他互斥锁。具体而言，如果调用者拥有一个私有互斥锁（由调用者分配并初始化的），在仔细考虑排序问题后，可以在获取池互斥锁之后获取该私有互斥锁。在这些情况下，私有互斥锁最终成为真正的叶互斥锁。

池互斥锁具有以下优点：

- 无结构性开销；即可以与某个结构关联而不会使其变得臃肿。
- 可以为无效指针获取互斥锁，这在使用互斥锁来互锁析构操作时非常有用。
- 无初始化或销毁开销。
- 可与 mtx_sleep(9) 一起使用。

以及以下缺点：

- 通常只应作为叶互斥锁使用。
- 无法保证池/池之间的依赖排序。
- CPU 之间可能发生 L1 缓存主权争用。

`mtx_pool_alloc` 从指定的池中获取一个共享互斥锁。该例程使用一个简单的轮询器来选择由 `mtx_pool_destroy` 子系统管理的共享互斥锁之一。

`mtx_pool_find` 返回与指定地址关联的共享互斥锁。该例程会对传入的指针进行哈希计算，并根据该哈希值从指定的池中选择一个共享互斥锁。该指针不需要指向任何实际内容。

`mtx_pool_lock`、`mtx_pool_lock_spin`、`mtx_pool_unlock` 和 `mtx_pool_unlock_spin` 对指定池中与指定地址关联的共享互斥锁进行加锁和解锁；它们分别是 `mtx_pool_find` 与 mtx_lock(9)、mtx_lock_spin(9)、mtx_unlock(9) 和 mtx_unlock_spin(9) 的组合。由于这些例程必须先找到要操作的互斥锁，因此不如直接使用先前调用 `mtx_pool_find` 或 `mtx_pool_alloc` 返回的互斥锁指针来得快。

`mtx_pool_create` 分配并初始化指定大小的新互斥锁池。池大小必须是 2 的幂。`opts` 参数传递给 mtx_init(9) 以设置池中每个互斥锁的选项。

`mtx_pool_destroy` 对指定池中的每个互斥锁调用 mtx_destroy(9)，释放与池关联的内存，并将池指针赋值为 NULL。

## 参见

[locking(9)](locking.9.md), [mutex(9)](mutex.9.md)

## 历史

这些例程首次出现于 FreeBSD 5.0。
