# mpool(3)

`mpool` — 共享内存缓冲池

## 名称

`mpool`

## 概要

`#include <db.h>`

`#include <mpool.h>`

`Ft MPOOL * Fn mpool_open void *key int fd pgno_t pagesize pgno_t maxcache Ft void Fo mpool_filter MPOOL *mp void (*pgin)(void *, pgno_t, void *) void (*pgout)(void *, pgno_t, void *) void *pgcookie Fc Ft void * Fn mpool_new MPOOL *mp pgno_t *pgnoaddr u_int flags Ft int Fn mpool_delete MPOOL *mp void *page Ft void * Fn mpool_get MPOOL *mp pgno_t pgno u_int flags Ft int Fn mpool_put MPOOL *mp void *pgaddr u_int flags Ft int Fn mpool_sync MPOOL *mp Ft int Fn mpool_close MPOOL *mp`

## 描述

`mpool` 库接口旨在提供面向页面的文件缓冲管理。

`mpool_open` 函数初始化一个内存池。`key` 参数目前被忽略。`fd` 参数是底层文件的文件描述符，该文件必须支持寻址。

`pagesize` 参数是文件被划分成的页面的字节大小。`maxcache` 参数是任意时刻从底层文件缓存的最大页面数。此值与共享文件缓冲的进程数无关，而是共享该文件的任何进程所指定的最大值。

`mpool_filter` 函数旨在实现对页面的透明输入和输出处理。如果指定了 `pgin` 函数，每次从后备文件将缓冲读入内存池时都会调用它。如果指定了 `pgout` 函数，每次将缓冲写入后备文件时都会调用它。这两个函数在调用时都会传入 `pgcookie` 指针、页面号以及指向正在读取或写入的页面的指针。

`mpool_new` 函数以一个 `MPOOL` 指针、一个地址和一组标志作为参数。如果可以分配新页面，则返回指向该页面的指针，并将页面号存入 `pgnoaddr` 地址。否则，返回 `NULL` 并设置 `errno`。flags 值由以下值按位或构成：

**`MPOOL_PAGE_REQUEST`** 分配一个具有特定页面号的新页面。

**`MPOOL_PAGE_NEXT`** 分配具有下一个页面号的新页面。

`mpool_delete` 函数从池中删除指定页面并释放该页面。它以一个 `MPOOL` 指针和一个页面作为参数。该页面必须是由 `mpool_new` 生成的。

`mpool_get` 函数以一个 `MPOOL` 指针和一个页面号作为参数。如果页面存在，返回指向该页面的指针。否则，返回 `NULL` 并设置 `errno`。`flags` 参数由以下任意值按位或指定：

**`MPOOL_IGNOREPIN`** 返回的页面未被钉住；否则页面在返回时将被钉住。

`mpool_put` 函数解除由 `pgaddr` 所引用页面的钉住状态。`pgaddr` 参数必须是先前由 `mpool_get` 或 `mpool_new` 返回的地址。`flags` 参数由以下任意值按位或指定：

**`MPOOL_DIRTY`** 该页面已被修改，需要写入后备文件。

`mpool_put` 函数成功时返回 0，出错时返回 -1。

`mpool_sync` 函数将与 `MPOOL` 指针关联的所有已修改页面写入后备文件。`mpool_sync` 函数成功时返回 0，出错时返回 -1。

`mpool_close` 函数释放与内存池 cookie 关联的所有已分配内存。已修改页面*不会*被写入后备文件。`mpool_close` 函数成功时返回 0，出错时返回 -1。

## 错误

`mpool_open` 函数可能失败并为库例程 malloc(3) 所指定的任何错误设置 `errno`。

`mpool_get` 函数可能失败并为以下情况设置 `errno`：

**[Er** EINVAL] 所请求的记录不存在。

`mpool_new` 和 `mpool_get` 函数可能失败并为库例程 read(2)、[write(2)](../sys/write.2.md) 和 malloc(3) 所指定的任何错误设置 `errno`。

`mpool_sync` 函数可能失败并为库例程 [write(2)](../sys/write.2.md) 所指定的任何错误设置 `errno`。

`mpool_close` 函数可能失败并为库例程 free(3) 所指定的任何错误设置 `errno`。

## 参见

btree(3), dbopen(3), hash(3), recno(3)
