# sglist(9)

`sglist` — 管理物理内存地址的分散/聚集列表

## 名称

`sglist`, `sglist_alloc`, `sglist_append`, `sglist_append_bio`, `sglist_append_mbuf`, `sglist_append_mbuf_epg`, `sglist_append_phys`, `sglist_append_sglist`, `sglist_append_single_mbuf`, `sglist_append_uio`, `sglist_append_user`, `sglist_append_vmpages`, `sglist_build`, `sglist_clone`, `sglist_consume_uio`, `sglist_count`, `sglist_count_mbuf_epg`, `sglist_count_vmpages`, `sglist_free`, `sglist_hold`, `sglist_init`, `sglist_join`, `sglist_length`, `sglist_reset`, `sglist_slice`, `sglist_split`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/sglist.h>
```

```c
struct sglist *
sglist_alloc(int nsegs, int mflags)

int
sglist_append(struct sglist *sg, void *buf, size_t len)

int
sglist_append_bio(struct sglist *sg, struct bio *bp)

int
sglist_append_mbuf_epg(struct sglist *sg, struct mbuf *m, size_t offset, size_t len)

int
sglist_append_mbuf(struct sglist *sg, struct mbuf *m)

int
sglist_append_phys(struct sglist *sg, vm_paddr_t paddr, size_t len)

int
sglist_append_sglist(struct sglist *sg, struct sglist *source, size_t offset, size_t len)

int
sglist_append_single_mbuf(struct sglist *sg, struct mbuf *m)

int
sglist_append_uio(struct sglist *sg, struct uio *uio)

int
sglist_append_user(struct sglist *sg, void *buf, size_t len, struct thread *td)

int
sglist_append_vmpages(struct sglist *sg, vm_page_t *m, size_t pgoff, size_t len)

struct sglist *
sglist_build(void *buf, size_t len, int mflags)

struct sglist *
sglist_clone(struct sglist *sg, int mflags)

int
sglist_consume_uio(struct sglist *sg, struct uio *uio, size_t resid)

int
sglist_count(void *buf, size_t len)

int
sglist_count_mbuf_epg(struct mbuf *m, size_t offset, size_t len)

int
sglist_count_vmpages(vm_page_t *m, size_t pgoff, size_t len)

void
sglist_free(struct sglist *sg)

struct sglist *
sglist_hold(struct sglist *sg)

void
sglist_init(struct sglist *sg, int maxsegs, struct sglist_seg *segs)

int
sglist_join(struct sglist *first, struct sglist *second)

size_t
sglist_length(struct sglist *sg)

void
sglist_reset(struct sglist *sg)

int
sglist_slice(struct sglist *original, struct sglist **slice, size_t offset, size_t length, int mflags)

int
sglist_split(struct sglist *original, struct sglist **head, size_t length, int mflags)
```

## 描述

`sglist` API 管理物理地址范围。每个列表包含一个或多个元素。每个元素包含一个起始物理地址和一个长度。分散/聚集列表在共享时是只读的。如果想更改现有的分散/聚集列表且不持有该列表的唯一引用，则应创建一个新列表而不是修改现有列表。

每个分散/聚集列表对象都包含一个引用计数。新列表以单个引用创建。通过调用 `sglist_hold` 获取新引用，通过调用 `sglist_free` 释放引用。

### 分配和初始化列表

每个 `sglist` 对象由一个头部结构和一个可变长度的分散/聚集列表元素数组组成。`sglist_alloc` 函数分配一个包含头部和 `nsegs` 个分散/聚集列表元素的新列表。`mflags` 参数可以设置为 `M_NOWAIT` 或 `M_WAITOK`。

`sglist_count` 函数返回描述由单个内核虚拟地址范围映射的物理地址范围所需的分散/聚集列表元素数量。内核虚拟地址范围从 `buf` 开始，长度为 `len` 字节。

`sglist_count_mbuf_epg` 函数返回描述外部多页 mbuf 缓冲区 `m` 所需的分散/聚集列表元素数量。范围从相对于缓冲区起始位置的 `offset` 偏移处开始，长度为 `len` 字节。

`sglist_count_vmpages` 函数返回描述由虚拟内存页数组 `m` 支撑的缓冲区的物理地址范围所需的分散/聚集列表元素数量。缓冲区从相对于第一页的 `pgoff` 字节偏移处开始，长度为 `len` 字节。

`sglist_build` 函数分配一个新的分散/聚集列表对象，描述由单个内核虚拟地址范围映射的物理地址范围。内核虚拟地址范围从 `buf` 开始，长度为 `len` 字节。`mflags` 参数可以设置为 `M_NOWAIT` 或 `M_WAITOK`。

`sglist_clone` 函数返回现有分散/聚集列表对象 `sg` 的副本。`mflags` 参数可以设置为 `M_NOWAIT` 或 `M_WAITOK`。这可用于在修改分散/聚集列表之前获取其私有副本。

`sglist_init` 函数初始化分散/聚集列表头部。头部由 `sg` 指向，被初始化为管理由 `segs` 指向的、包含 `maxsegs` 个分散/聚集列表元素的数组。这可用于初始化存储不由 `sglist_alloc` 提供的分散/聚集列表头部。在这种情况下，调用者不应调用 `sglist_free` 来释放自己的引用，并负责确保在释放 `sg` 和 `segs` 的存储之前，对该列表的所有其他引用都已释放。

### 构建分散/聚集列表

`sglist` API 提供了几个例程用于构建描述一个或多个对象的分散/聚集列表。具体来说，`sglist_append` 例程族可用于将对象描述的物理地址范围追加到分散/聚集列表的末尾。所有这些例程成功时返回 0，失败时返回错误。如果将地址范围追加到分散/聚集列表的请求失败，分散/聚集列表将保持不变。

`sglist_append` 函数将单个内核虚拟地址范围描述的物理地址范围追加到分散/聚集列表 `sg`。内核虚拟地址范围从 `buf` 开始，长度为 `len` 字节。

`sglist_append_bio` 函数将单个 bio `bp` 描述的物理地址范围追加到分散/聚集列表 `sg`。

`sglist_append_mbuf_epg` 函数将外部多页 [mbuf(9)](mbuf.9.md) 缓冲区 `ext_pgs` 描述的物理地址范围追加到分散/聚集列表 `sg`。物理地址范围从 `ext_pgs` 中的 `offset` 偏移处开始，持续 `len` 字节。注意，与 `sglist_append_mbuf` 不同，`sglist_append_mbuf_epg` 只为单个 mbuf 添加范围，而不是整个 mbuf 链。

`sglist_append_mbuf` 函数将整个 mbuf 链 `m` 描述的物理地址范围追加到分散/聚集列表 `sg`。

`sglist_append_single_mbuf` 函数将单个 mbuf `m` 描述的物理地址范围追加到分散/聚集列表 `sg`。

`sglist_append_phys` 函数将单个物理地址范围追加到分散/聚集列表 `sg`。物理地址范围从 `paddr` 开始，长度为 `len` 字节。

`sglist_append_sglist` 函数将分散/聚集列表 `source` 描述的物理地址范围追加到分散/聚集列表 `sg`。物理地址范围从 `source` 中的 `offset` 偏移处开始，持续 `len` 字节。

`sglist_append_uio` 函数将 [uio(9)](uio.9.md) 对象描述的物理地址范围追加到分散/聚集列表 `sg`。注意，调用者有责任确保支撑 I/O 请求的页面在 `sg` 的生命周期内被锁定。还应注意，此例程不修改 `uio`。

`sglist_append_user` 函数将单个用户虚拟地址范围描述的物理地址范围追加到分散/聚集列表 `sg`。用户虚拟地址范围相对于线程 `td` 的地址空间。它从 `buf` 开始，长度为 `len` 字节。注意，调用者有责任确保支撑用户缓冲区的页面在 `sg` 的生命周期内被锁定。

`sglist_append_vmpages` 函数追加由虚拟内存页数组 `m` 支撑的缓冲区的物理地址范围。缓冲区从相对于第一页的 `pgoff` 字节偏移处开始，长度为 `len` 字节。

`sglist_consume_uio` 函数是 `sglist_append_uio` 的变体。与 `sglist_append_uio` 一样，它将 `uio` 描述的物理地址范围追加到分散/聚集列表 `sg`。但与 `sglist_append_uio` 不同的是，`sglist_consume_uio` 会修改 I/O 请求，以指示已追加的地址范围已被处理，类似于调用 uiomove(9)。此例程只会追加描述总长度不超过 `resid` 字节的范围。如果在处理 `resid` 字节之前分散/聚集列表中的可用段已耗尽，则 `uio` 结构将被更新以反映实际处理的字节数，`sglist_consume_io` 将返回零以指示成功。实际上，此函数会执行部分读或写。调用者可以通过比较调用 `sglist_consume_uio` 前后 `uio` 的 `uio_resid` 成员来确定实际处理的字节数。

### 操作分散/聚集列表

`sglist_join` 函数将分散/聚集列表 `second` 中的物理地址范围追加到 `first`，然后将 `second` 重置为空列表。成功时返回零，失败时返回错误。

`sglist_split` 函数将现有的分散/聚集列表拆分为两个列表。列表 `original` 描述的前 `length` 字节被移动到新列表 `*head`。如果 `original` 描述的总地址范围小于 `length` 字节，则所有地址范围都将被移动到 `*head` 处的新列表，`original` 将成为空列表。调用者可以在 `*head` 中提供现有的分散/聚集列表。如果是这样，该列表必须为空。否则，调用者可以将 `*head` 设置为 `NULL`，在这种情况下将分配新的分散/聚集列表。此时，`mflags` 可以设置为 `M_NOWAIT` 或 `M_WAITOK`。注意，由于 `original` 列表会被此调用修改，它必须是一个没有其他引用的私有列表。`sglist_split` 函数成功时返回零，失败时返回错误。

`sglist_slice` 函数从现有分散/聚集列表 `original` 的子范围生成新的分散/聚集列表。要提取的子范围由 `offset` 和 `length` 参数指定。新的分散/聚集列表存储在 `*slice` 中。与 `sglist_join` 的 `head` 一样，调用者可以提供一个空的分散/聚集列表，也可以将 `*slice` 设置为 `NULL`，在这种情况下 `sglist_slice` 将根据 `mflags` 分配新列表。与 `sglist_split` 不同，`sglist_slice` 不修改 `original`，也不要求它是私有列表。`sglist_split` 函数成功时返回零，失败时返回错误。

### 杂项例程

`sglist_reset` 函数清除分散/聚集列表 `sg`，使其不再映射任何地址范围。这可以允许将单个分散/聚集列表对象重用于多个请求。

`sglist_length` 函数返回分散/聚集列表 `sg` 描述的物理地址范围的总长度。

## 返回值

`sglist_alloc`、`sglist_build` 和 `sglist_clone` 函数成功时返回新的分散/聚集列表，失败时返回 `NULL`。

`sglist_append` 函数族以及 `sglist_consume_uio`、`sglist_join`、`sglist_slice` 和 `sglist_split` 函数成功时返回零，失败时返回错误。

`sglist_count` 函数族返回分散/聚集列表元素的计数。

`sglist_length` 函数返回分散/聚集列表描述的地址空间计数（以字节为单位）。

## 错误

`sglist_append` 函数在以下情况失败时返回错误：

`[EINVAL]` 分散/聚集列表有零个段。

`[EFBIG]` 分散/聚集列表中没有足够的可用段来追加指定的物理地址范围。

`sglist_consume_uio` 函数在以下情况失败时返回错误：

`[EINVAL]` 分散/聚集列表有零个段。

`sglist_join` 函数在以下情况失败时返回错误：

`[EFBIG]` 分散/聚集列表 `first` 中没有足够的可用段来追加 `second` 的物理地址范围。

`sglist_slice` 函数在以下情况失败时返回错误：

`[EINVAL]` `original` 分散/聚集列表描述的地址空间不足以覆盖请求的子范围。

`[EINVAL]` `*slice` 中调用者提供的分散/聚集列表不为空。

`[ENOMEM]` 在 `mflags` 中设置 `M_NOWAIT` 时，分配新分散/聚集列表的尝试失败。

`[EFBIG]` `*slice` 中调用者提供的分散/聚集列表没有足够的可用段来描述请求的物理地址范围。

`sglist_split` 函数在以下情况失败时返回错误：

`[EDOOFUS]` `original` 分散/聚集列表有多个引用。

`[EINVAL]` `*head` 中调用者提供的分散/聚集列表不为空。

`[ENOMEM]` 在 `mflags` 中设置 `M_NOWAIT` 时，分配新分散/聚集列表的尝试失败。

`[EFBIG]` `*head` 中调用者提供的分散/聚集列表没有足够的可用段来描述请求的物理地址范围。

## 参见

[g_bio(9)](g_bio.9.md), [malloc(9)](malloc.9.md), [mbuf(9)](mbuf.9.md), [uio(9)](uio.9.md)

## 历史

此 API 首次引入于 FreeBSD 8.0。
