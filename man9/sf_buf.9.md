# sf\_buf.9

`sf_buf` — 管理内存页面的临时内核地址空间映射

## 名称

`sf_buf`

## 概要

```c
#include <sys/sf_buf.h>
```

```c
struct sf_buf *
sf_buf_alloc(struct vm_page *m, int flags)

void
sf_buf_free(struct sf_buf *sf)

vm_offset_t
sf_buf_kva(struct sf_buf *sf)

struct vm_page *
sf_buf_page(struct sf_buf *sf)
```

## 描述

`sf_buf` 接口，历史上称为 sendfile(2) 缓冲区接口，允许内核子系统管理物理内存页面的临时内核地址空间映射。在具有直接内存映射区域（允许所有物理页面始终在内核地址空间中可见）的系统上，`struct sf_buf` 将指向直接映射区域中的地址；在没有直接内存映射区域的系统上，`struct sf_buf` 将管理在 `struct sf_buf` 生命周期内有效的临时内核地址空间映射。

调用 `sf_buf_alloc` 为物理内存页面分配 `struct sf_buf`。`sf_buf_alloc` 不负责安排页面存在于物理内存中；调用者应已安排页面被锁定，即通过调用 [vm_page_wire(9)](vm_page_wire.9.md)。可以向 `sf_buf_alloc` 传递几个标志：

**`SFB_CATCH`** 使 `sf_buf_alloc` 在等待 `struct sf_buf` 变为可用时收到信号时中止并返回 `NULL`。

**`SFB_NOWAIT`** 使 `sf_buf_alloc` 在 `struct sf_buf` 不能立即可用时返回 `NULL` 而不是休眠。

**`SFB_CPUPRIVATE`** 使 `sf_buf_alloc` 仅安排临时映射在当前 CPU 上有效，避免对一次只会在单个 CPU 上访问的映射进行不必要的 TLB 击落。调用者必须确保对虚拟地址的访问仅发生在调用 `sf_buf_alloc` 的 CPU 上，或许可以使用 `sched_pin`。

调用 `sf_buf_kva` 返回该页面的内核映射地址。

调用 `sf_buf_page` 返回最初传递给 `sf_buf_alloc` 的页面指针。

调用 `sf_buf_free` 释放 `struct sf_buf` 引用。调用者负责释放他们先前在物理页面上获取的任何锁定；`sf_buf_free` 仅释放临时内核地址空间映射，而不释放页面本身。

此接口的用途包括管理从用户内存借用的页面的映射（例如在零复制套接字 I/O 中），或来自缓冲区缓存的、由 sendfile(2) 的 mbuf 外部存储引用的内存页面。

## 参见

[sendfile(2)](../man2/sendfile.2.md), [vm_page_wire(9)](vm_page_wire.9.md)

## 作者

`struct sf_buf` API 由 Alan L. Cox 设计和实现。本手册页由 Robert N. M. Watson 编写。
