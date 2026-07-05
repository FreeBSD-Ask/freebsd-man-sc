# crypto_buffer.9

`crypto_buffer` — 对称密码学请求缓冲区

## 名称

`crypto_buffer`

## 概要

```c
#include <opencrypto/cryptodev.h>

int
crypto_apply(struct cryptop *crp, int off, int len,
    int (*f)(void *, void *, u_int), void *arg)

int
crypto_apply_buf(struct crypto_buffer *cb, int off, int len,
    int (*f)(void *, void *, u_int), void *arg)

void *
crypto_buffer_contiguous_subsegment(struct crypto_buffer *cb,
    size_t skip, size_t len)

size_t
crypto_buffer_len(struct crypto_buffer *cb)

void *
crypto_contiguous_subsegment(struct cryptop *crp, size_t skip,
    size_t len)

void
crypto_cursor_init(struct crypto_buffer_cursor *cc,
    const struct crypto_buffer *cb)

void
crypto_cursor_advance(struct crypto_buffer_cursor *cc, size_t amount)

void
crypto_cursor_copyback(struct crypto_buffer_cursor *cc, int size,
    const void *src)

void
crypto_cursor_copydata(struct crypto_buffer_cursor *cc, int size,
    void *dst)

void
crypto_cursor_copydata_noadv(struct crypto_buffer_cursor *cc,
    int size, void *dst)

void *
crypto_cursor_segment(struct crypto_buffer_cursor *cc, size_t *len)

void
crypto_cursor_copy(const struct crypto_buffer_cursor *fromc,
    struct crypto_buffer_cursor *toc)

bool
CRYPTO_HAS_OUTPUT_BUFFER(struct cryptop *crp)
```

## 描述

对称密码学请求使用数据缓冲区来描述要修改的数据。请求可以指定单个数据缓冲区，其内容被原地修改；或者请求可以为输入和输出指定各自的数据缓冲区。`struct crypto_buffer` 提供了一种抽象，允许密码学请求操作不同类型的缓冲区。`struct crypto_cursor` 允许密码学驱动程序遍历数据缓冲区。

`CRYPTO_HAS_OUTPUT_BUFFER` 在 `crp` 为输入和输出使用各自独立的缓冲区时返回真，在 `crp` 使用单个缓冲区时返回假。

`crypto_buffer_len` 返回数据缓冲区 `cb` 的字节长度。

`crypto_apply_buf` 对数据缓冲区 `cb` 的某个区域调用调用者提供的函数。函数 `f` 会被调用一次或多次。对于每次调用，`f` 的第一个参数是传递给 `crypto_apply_buf` 的 `arg` 的值。`f` 的第二个和第三个参数是指向映射到内核中的一个缓冲区段的指针和长度。该函数会被调用足够多次，以覆盖从偏移量 `off` 开始、长度为 `len` 字节的数据缓冲区。如果 `f` 的某次调用返回非零值，`crypto_apply_buf` 会立即返回该值，而不再对该区域的任何剩余段调用 `f`；否则 `crypto_apply_buf` 返回最后一次调用 `f` 的返回值。`crypto_apply` 对 `crp` 的输入数据缓冲区中的某个区域调用回调函数 `f`。

`crypto_buffer_contiguous_subsegment` 尝试在数据缓冲区 `cb` 中定位单个虚拟连续的段。该段必须长度为 `len` 字节，且从偏移量 `skip` 字节处开始。如果找到这样的段，返回指向该段起始处的指针。否则返回 `NULL`。`crypto_contiguous_subsegment` 尝试在 `crp` 的输入数据缓冲区中定位单个虚拟连续的段。

### 数据缓冲区

数据缓冲区由 `struct crypto_buffer` 的实例描述。`cb_type` 成员包含数据缓冲区的类型。支持以下类型：

**`CRYPTO_BUF_NONE`** 无效缓冲区。用于在密码学请求使用单个数据缓冲区时标记输出缓冲区。

**`CRYPTO_BUF_CONTIG`** 映射到内核地址空间的字节数组。

**`CRYPTO_BUF_UIO`** 如 [uio(9)](uio.9.md) 中所述的内核缓冲区的分散/聚集列表。

**`CRYPTO_BUF_MBUF`** 如 [mbuf(9)](mbuf.9.md) 中所述的网络内存缓冲区链。

**`CRYPTO_BUF_SINGLE_MBUF`** 如 [mbuf(9)](mbuf.9.md) 中所述的单个网络内存缓冲区。

**`CRYPTO_BUF_VMPAGE`** 描述内核地址空间中各页的 `vm_page_t` 结构的分散/聚集列表。仅当 `CRYPTO_HAS_VMPAGE` 为真时此缓冲区类型才可用。

该结构还包含以下特定于类型的字段：

**`cb_buf`** 指向 `CRYPTO_BUF_CONTIG` 数据缓冲区起始处的指针。

**`cb_buf_len`** `CRYPTO_BUF_CONTIG` 数据缓冲区的长度。

**`cb_mbuf`** 指向用于 `CRYPTO_BUF_MBUF` 和 `CRYPTO_BUF_SINGLE_MBUF` 的 `struct mbuf` 的指针。

**`cb_uio`** 指向用于 `CRYPTO_BUF_UIO` 的 `struct uio` 的指针。

**`cb_vm_page`** 指向用于 `CRYPTO_BUF_VMPAGE` 的 `struct vm_page` 数组的指针。

**`cb_vm_page_len`** `cb_vm_page` 数组中包含的数据总量，以字节为单位。

**`cb_vm_page_offset`** `cb_vm_page` 第一页中有效数据起始处的偏移量，以字节为单位。

### 游标

游标提供了一种遍历数据缓冲区的机制。它们主要用于通过虚拟地址访问数据缓冲区的软件驱动程序。

`crypto_cursor_init` 初始化游标 `cc`，使其引用数据缓冲区 `cb` 的起始处。

`crypto_cursor_advance` 将游标在数据缓冲区中向前推进 `amount` 字节。

`crypto_cursor_copyback` 将 `src` 所指向的本地缓冲区中的 `size` 字节复制到与 `cc` 关联的数据缓冲区中。字节写入到 `cc` 的当前位置，然后游标前进 `size` 字节。

`crypto_cursor_copydata` 将与 `cc` 关联的数据缓冲区中的 `size` 字节复制到 `dst` 所指向的本地缓冲区中。字节从 `cc` 的当前位置读取，然后游标前进 `size` 字节。

`crypto_cursor_copydata_noadv` 类似于 `crypto_cursor_copydata`，但它不改变 `cc` 的当前位置。

`crypto_cursor_segment` 返回 `cc` 当前位置处虚拟连续段的起始处。该段的长度存储在 `len` 中。

## 返回值

`crypto_apply` 和 `crypto_apply_buf` 返回调用者提供的回调函数的返回值。

`crypto_buffer_contiguous_subsegment`、`crypto_contiguous_subsegment` 和 `crypto_cursor_segment` 返回指向连续段的指针或 `NULL`。

`crypto_buffer_len` 返回缓冲区的字节长度。

`crypto_cursor_seglen` 返回连续段的字节长度。

`crypto_cursor_copy` 对游标 `fromc` 进行深拷贝。两份拷贝不共享任何状态，因此可以独立使用。

`CRYPTO_HAS_OUTPUT_BUFFER` 在请求使用独立的输出缓冲区时返回真。

## 参见

[ipsec(4)](../man4/ipsec.4.md), [crypto(7)](../man7/crypto.7.md), [bus_dma(9)](bus_dma.9.md), [crypto(9)](crypto.9.md), [crypto_driver(9)](crypto_driver.9.md), [crypto_request(9)](crypto_request.9.md), [crypto_session(9)](crypto_session.9.md), [mbuf(9)](mbuf.9.md), [uio(9)](uio.9.md)

## 历史

`crypto_buffer` 函数首次出现于 FreeBSD 13。

## 作者

`crypto_buffer` 函数及本手册页由 John Baldwin <jhb@FreeBSD.org> 编写。
