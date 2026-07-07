# mbuf(9)

`mbuf` — 内核 IPC 子系统中的内存管理

## 名称

`mbuf`

## 概要

`#include <sys/param.h>`

`#include <sys/systm.h>`

`#include <sys/mbuf.h>`

### Mbuf 分配宏

`Fn MGET struct mbuf *mbuf int how short type Fn MGETHDR struct mbuf *mbuf int how short type Ft int Fn MCLGET struct mbuf *mbuf int how Fo MEXTADD struct mbuf *mbuf char *buf u_int size void (*free)(struct mbuf *) void *opt_arg1 void *opt_arg2 int flags int type Fc`

### Mbuf 工具宏

`Ft type Fn mtod struct mbuf *mbuf type Ft void * Fn mtodo struct mbuf *mbuf offset Fn M_ALIGN struct mbuf *mbuf u_int len Fn MH_ALIGN struct mbuf *mbuf u_int len Ft int Fn M_LEADINGSPACE struct mbuf *mbuf Ft int Fn M_TRAILINGSPACE struct mbuf *mbuf Fn M_MOVE_PKTHDR struct mbuf *to struct mbuf *from Fn M_PREPEND struct mbuf *mbuf int len int how Fn MCHTYPE struct mbuf *mbuf short type Ft int Fn M_WRITABLE struct mbuf *mbuf`

### Mbuf 分配函数

`Ft struct mbuf * Fn m_get int how short type Ft struct mbuf * Fn m_get2 int size int how short type int flags Ft struct mbuf * Fn m_get3 int size int how short type int flags Ft struct mbuf * Fn m_getm struct mbuf *orig int len int how short type Ft struct mbuf * Fn m_getjcl int how short type int flags int size Ft struct mbuf * Fn m_getcl int how short type int flags Ft struct mbuf * Fn m_gethdr int how short type Ft struct mbuf * Fn m_free struct mbuf *mbuf Ft void Fn m_freem struct mbuf *mbuf`

### Mbuf 工具函数

`Ft void Fn m_adj struct mbuf *mbuf int len Ft void Fn m_align struct mbuf *mbuf int len Ft int Fn m_append struct mbuf *mbuf int len c_caddr_t cp Ft struct mbuf * Fn m_prepend struct mbuf *mbuf int len int how Ft struct mbuf * Fn m_copyup struct mbuf *mbuf int len int dstoff Ft struct mbuf * Fn m_pullup struct mbuf *mbuf int len Ft struct mbuf * Fn m_pulldown struct mbuf *mbuf int offset int len int *offsetp Ft struct mbuf * Fn m_copym struct mbuf *mbuf int offset int len int how Ft struct mbuf * Fn m_copypacket struct mbuf *mbuf int how Ft struct mbuf * Fn m_dup const struct mbuf *mbuf int how Ft void Fn m_copydata const struct mbuf *mbuf int offset int len caddr_t buf Ft void Fn m_copyback struct mbuf *mbuf int offset int len caddr_t buf Ft struct mbuf * Fo m_devget char *buf int len int offset struct ifnet *ifp void (*copy)(char *from, caddr_t to, u_int len) Fc Ft void Fn m_cat struct mbuf *m struct mbuf *n Ft void Fn m_catpkt struct mbuf *m struct mbuf *n Ft u_int Fn m_fixhdr struct mbuf *mbuf Ft int Fn m_dup_pkthdr struct mbuf *to const struct mbuf *from int how Ft void Fn m_move_pkthdr struct mbuf *to struct mbuf *from Ft u_int Fn m_length struct mbuf *mbuf struct mbuf **last Ft struct mbuf * Fn m_split struct mbuf *mbuf int len int how Ft int Fn m_apply struct mbuf *mbuf int off int len int (*f)(void *arg, void *data, u_int len) void *arg Ft struct mbuf * Fn m_getptr struct mbuf *mbuf int loc int *off Ft struct mbuf * Fn m_defrag struct mbuf *m0 int how Ft struct mbuf * Fn m_collapse struct mbuf *m0 int how int maxfrags Ft struct mbuf * Fn m_unshare struct mbuf *m0 int how`

## 描述

`mbuf` 是内核 IPC 子系统中内存管理的基本单位。网络数据包和套接字缓冲区存储在 `mbuf` 中。一个网络数据包可能跨越多个 `mbuf`，这些 `mbuf` 排列成 `mbuf 链`（链表），这使得添加或修剪网络报头几乎没有开销。

虽然开发者在没有充分理由的情况下不应关心 `mbuf` 内部细节，以避免与未来更改不兼容，但了解 `mbuf` 的一般结构是有用的。

`mbuf` 由可变大小的头部和用于数据的小型内部缓冲区组成。`mbuf` 的总大小 `MSIZE` 是定义于以下位置的常量

`#include <sys/param.h>`

`mbuf` 头部包括：

**`m_next`** (`struct mbuf *`) 指向 `mbuf 链`中下一个 `mbuf` 的指针。

**`m_nextpkt`** (`struct mbuf *`) 指向队列中下一个 `mbuf 链`的指针。

**`m_data`** (`caddr_t`) 指向附加到此 `mbuf` 的数据的指针。

**`m_len`** (`int`) 数据的长度。

**`m_type`** (`short`) 数据的类型。

**`m_flags`** (`int`) `mbuf` 标志。

`mbuf` 标志位定义如下：

```c
#define	M_EXT		0x00000001 /* 具有关联的外部存储 */
#define	M_PKTHDR	0x00000002 /* 记录的开始 */
#define	M_EOR		0x00000004 /* 记录的结束 */
#define	M_RDONLY	0x00000008 /* 关联的数据标记为只读 */
#define	M_BCAST		0x00000010 /* 作为链路层广播发送/接收 */
#define	M_MCAST		0x00000020 /* 作为链路层多播发送/接收 */
#define	M_PROMISC	0x00000040 /* 数据包不是给我们的 */
#define	M_VLANTAG	0x00000080 /* ether_vtag 有效 */
#define	M_EXTPG		0x00000100 /* 具有未映射页面和 TLS 的数组 */
#define	M_NOFREE	0x00000200 /* 不要释放 mbuf，嵌入在集群中 */
#define	M_TSTMP		0x00000400 /* rcv_tstmp 字段有效 */
#define	M_TSTMP_HPREC	0x00000800 /* rcv_tstmp 是高精度，通常
				      在端口上硬件加盖（对 IEEE 1588
				      和 802.1AS 有用） */
#define	M_PROTO1	0x00001000 /* 协议特定 */
#define	M_PROTO2	0x00002000 /* 协议特定 */
#define	M_PROTO3	0x00004000 /* 协议特定 */
#define	M_PROTO4	0x00008000 /* 协议特定 */
#define	M_PROTO5	0x00010000 /* 协议特定 */
#define	M_PROTO6	0x00020000 /* 协议特定 */
#define	M_PROTO7	0x00040000 /* 协议特定 */
#define	M_PROTO8	0x00080000 /* 协议特定 */
#define	M_PROTO9	0x00100000 /* 协议特定 */
#define	M_PROTO10	0x00200000 /* 协议特定 */
#define	M_PROTO11	0x00400000 /* 协议特定 */
#define	M_PROTO12	0x00800000 /* 协议特定 */
```

可用的 `mbuf` 类型定义如下：

```c
#define	MT_DATA		1	/* 动态（数据）分配 */
#define	MT_HEADER	MT_DATA	/* 数据包头 */
#define	MT_VENDOR1	4	/* 供供应商内部使用 */
#define	MT_VENDOR2	5	/* 供供应商内部使用 */
#define	MT_VENDOR3	6	/* 供供应商内部使用 */
#define	MT_VENDOR4	7	/* 供供应商内部使用 */
#define	MT_SONAME	8	/* 套接字名称 */
#define	MT_EXP1		9	/* 供实验使用 */
#define	MT_EXP2		10	/* 供实验使用 */
#define	MT_EXP3		11	/* 供实验使用 */
#define	MT_EXP4		12	/* 供实验使用 */
#define	MT_CONTROL	14	/* 额外数据协议消息 */
#define	MT_EXTCONTROL	15	/* 具有外部化内容的控制消息 */
#define	MT_OOBDATA	16	/* 加急数据  */
```

可用的外部缓冲区类型定义如下：

```c
#define	EXT_CLUSTER	1	/* mbuf 集群 */
#define	EXT_SFBUF	2	/* sendfile(2) 的 sf_bufs */
#define	EXT_JUMBOP	3	/* jumbo 集群 4096 字节 */
#define	EXT_JUMBO9	4	/* jumbo 集群 9216 字节 */
#define	EXT_JUMBO16	5	/* jumbo 集群 16184 字节 */
#define	EXT_PACKET	6	/* 来自 packet 区域的 mbuf+集群 */
#define	EXT_MBUF	7	/* 外部 mbuf 引用 */
#define	EXT_RXRING	8	/* NIC 接收环中的数据 */
#define	EXT_PGS		9	/* 未映射页面的数组 */
#define	EXT_VENDOR1	224	/* 供供应商内部使用 */
#define	EXT_VENDOR2	225	/* 供供应商内部使用 */
#define	EXT_VENDOR3	226	/* 供供应商内部使用 */
#define	EXT_VENDOR4	227	/* 供供应商内部使用 */
#define	EXT_EXP1	244	/* 供实验使用 */
#define	EXT_EXP2	245	/* 供实验使用 */
#define	EXT_EXP3	246	/* 供实验使用 */
#define	EXT_EXP4	247	/* 供实验使用 */
#define	EXT_NET_DRV	252	/* 由网络驱动程序提供的自定义 ext_buf */
#define	EXT_MOD_TYPE	253	/* 自定义模块的 ext_buf 类型 */
#define	EXT_DISPOSABLE	254	/* 可以通过页面翻转丢弃此缓冲区 */
#define	EXT_EXTREF	255	/* 具有外部维护的 ref_cnt 指针 */
```

如果设置了 `M_PKTHDR` 标志，则会将 `struct pkthdr` `m_pkthdr` 添加到 `mbuf` 头部。它包含指向接收数据包的接口的指针（`struct ifnet` `*rcvif`）以及数据包的总长度（`int` `len`）。可选地，它还可能包含附加的数据包标签列表（`struct m_tag`）。详见 [mbuf_tags(9)](mbuf_tags.9.md)。用于将校验和计算卸载到硬件的字段也保存在 `m_pkthdr` 中。详见硬件辅助校验和计算小节。

如果数据足够小，则存储在 `mbuf` 的内部数据缓冲区中。如果数据足够大，则可以向 `mbuf 链`中添加另一个 `mbuf`，或者将外部存储与 `mbuf` 关联。设置了 `M_PKTHDR` 标志的 `mbuf` 可以容纳 `MHLEN` 字节的数据，否则可以容纳 `MLEN` 字节。

如果将外部存储与 `mbuf` 关联，则会添加 `m_ext` 头部，代价是丢失内部数据缓冲区。它包括指向外部存储的指针、存储的大小、指向用于释放存储的函数的指针、指向可传递给该函数的可选参数的指针，以及指向引用计数器的指针。使用外部存储的 `mbuf` 设置了 `M_EXT` 标志。

系统提供了一个用于分配所需外部存储缓冲区的宏 `MEXTADD`。

引用计数器的分配和管理由子系统处理。

系统还提供了一种默认类型的外部存储缓冲区，称为 `mbuf 集群`。可以使用 `MCLGET` 宏分配和配置 `mbuf 集群`。每个 `mbuf 集群` 的大小为 `MCLBYTES`，其中 MCLBYTES 是与机器相关的常量。系统定义了一个建议性宏 `MINCLSIZE`，它是要放入 `mbuf 集群` 的最小数据量。它等于 `MHLEN` 加一。如果大小允许，通常最好将数据存储在 `mbuf` 的数据区域中，而不是分配单独的 `mbuf 集群` 来容纳相同的数据。

### 宏和函数

有许多预定义的宏和函数为开发者提供常用工具。

**`mtod(mbuf, type)`** 将 `mbuf` 指针转换为数据指针。该宏展开为转换为指定 `type` 的数据指针。**注意：** 建议确保 `mbuf` 中有足够的连续数据。详见 `m_pullup`。

**`mtodo(mbuf, offset)`** 返回 `mbuf` 附加数据中偏移量（以字节为单位）处的数据指针。返回 `void *` 指针。**注意：** 调用者必须确保偏移量在附加数据的范围内。

**`MGET(mbuf, how, type)`** 分配一个 `mbuf` 并将其初始化为包含内部数据。成功时，`mbuf` 将指向已分配的 `mbuf`，失败时设置为 `NULL`。`how` 参数应设置为 `M_WAITOK` 或 `M_NOWAIT`。它指定调用者是否愿意在必要时阻塞。许多其他与 `mbuf` 相关的函数和宏都有此参数，因为它们在某些时候可能需要分配新的 `mbuf`。

**`MGETHDR(mbuf, how, type)`** 分配一个 `mbuf` 并将其初始化为包含数据包头和内部数据。详见 `MGET`。

**`MEXTADD(mbuf, buf, size, free, opt_arg1, opt_arg2, flags, type)`** 将外部管理的数据与 `mbuf` 关联。mbuf 中包含的任何内部数据将被丢弃，并将设置 `M_EXT` 标志。`buf` 和 `size` 参数分别是数据的地址和长度。`free` 参数指向一个函数，该函数将在 mbuf 释放时被调用以释放数据；仅在 `type` 为 `EXT_EXTREF` 时使用。`opt_arg1` 和 `opt_arg2` 参数将保存在 mbuf 的 `struct m_ext` 的 `ext_arg1` 和 `ext_arg2` 字段中。`flags` 参数指定额外的 `mbuf` 标志；不必指定 `M_EXT`。最后，`type` 参数指定外部数据的类型，它控制 `mbuf` 释放时如何处理数据。在大多数情况下，正确的值为 `EXT_EXTREF`。

**`MCLGET(mbuf, how)`** 分配一个 `mbuf 集群` 并将其附加到 `mbuf`。成功时返回非零值；否则返回 0。从历史上看，使用者通过测试 mbuf 上的 `M_EXT` 标志来检查是否成功，但现在不鼓励这样做，以避免在协议栈和设备驱动程序中不必要地了解外部存储的实现。

**`M_ALIGN(mbuf, len)`** 设置指针 `mbuf->m_data`，以将大小为 `len` 的对象放置在 `mbuf` 内部数据区域的末尾，按长字对齐。仅适用于通过 `MGET` 或 `m_get` 新分配的 `mbuf`。

**`MH_ALIGN(mbuf, len)`** 与 `M_ALIGN` 具有相同的目的，但仅适用于通过 `MGETHDR` 或 `m_gethdr` 新分配的 `mbuf`，或由 `m_dup_pkthdr` 或 `m_move_pkthdr` 初始化的 `mbuf`。

**`m_align(mbuf, len)`** 与 `M_ALIGN` 具有相同的目的，但处理任何类型的 mbuf。

**`M_LEADINGSPACE(mbuf)`** 返回 `mbuf` 中数据开始之前可用的字节数。

**`M_TRAILINGSPACE(mbuf)`** 返回 `mbuf` 中数据结束之后可用的字节数。

**`M_PREPEND(mbuf, len, how)`** 此宏对 `mbuf 链` 进行操作。它是 `m_prepend` 的优化包装器，可以利用数据之前可能的空闲空间（例如，修剪链路层报头后留下的空间）。调用后，新的 `mbuf 链` 指针或 `NULL` 在 `mbuf` 中。

**`M_MOVE_PKTHDR(to, from)`** 使用此宏等价于调用 `m_move_pkthdr(to, from)`。

**`M_WRITABLE(mbuf)`** 如果 `mbuf` 未标记为 `M_RDONLY`，并且 `mbuf` 不包含外部存储，或者如果包含外部存储但存储的引用计数不大于 1，则此宏将评估为真。可以在 `mbuf->m_flags` 中设置 `M_RDONLY` 标志。这可以在设置外部存储期间通过将 `M_RDONLY` 位作为 `flags` 参数传递给 `MEXTADD` 宏来实现，或者可以直接在单个 `mbuf` 中设置。

**`MCHTYPE(mbuf, type)`** 将 `mbuf` 的类型更改为 `type`。这是一个相对昂贵的操作，应避免使用。

函数有：

**`m_get(how, type)`** 用于非关键路径的 `MGET` 函数版本。

**`m_get2(size, how, type, flags)`** 分配一个具有足够空间容纳指定数据量的 `mbuf`。如果大小大于 `MJUMPAGESIZE`，则返回 `NULL`。

**`m_get3(size, how, type, flags)`** 分配一个具有足够空间容纳指定数据量的 `mbuf`。如果大小大于 `MJUM16BYTES`，则返回 `NULL`。

**`m_getm(orig, len, how, type)`** 分配 `len` 字节的 `mbuf` 和 `mbuf 集群`（如有必要），并将生成的已分配 `mbuf 链` 附加到 `mbuf 链` `orig`（如果非 `NULL`）。如果在任何时候分配失败，则释放已分配的所有内容并返回 `NULL`。如果 `orig` 非 `NULL`，则不会释放它。可以使用 `m_getm` 将 `len` 字节附加到现有的 `mbuf` 或 `mbuf 链`（例如，可能位于预分配环中的 `mbuf` 或 `mbuf 链`），或简单地执行全有或全无的 `mbuf` 和 `mbuf 集群` 分配。

**`m_gethdr(how, type)`** 用于非关键路径的 `MGETHDR` 函数版本。

**`m_getcl(how, type, flags)`** 获取一个附加了 `mbuf 集群` 的 `mbuf`。如果其中任何一个分配失败，整个分配都会失败。此例程是同时获取 `mbuf` 和 `mbuf 集群` 的首选方式，因为它避免了在分配之间进行解锁/重新锁定。失败时返回 `NULL`。

**`m_getjcl(how, type, flags, size)`** 类似于 `m_getcl`，但要分配的集群的指定 `size` 必须是 `MCLBYTES`、`MJUMPAGESIZE`、`MJUM9BYTES` 或 `MJUM16BYTES` 之一。

**`m_free(mbuf)`** 释放 `mbuf`。返回已释放 `mbuf` 的 `m_next`。

以下函数对 `mbuf 链` 进行操作。

**`m_freem(mbuf)`** 释放整个 `mbuf 链`，包括任何外部存储。

**`m_adj(mbuf, len)`** 如果 `len` 为正，则从 `mbuf 链` 的头部修剪 `len` 字节，否则从尾部修剪。

**`m_append(mbuf, len, cp)`** 将 `len` 字节的数据 `cp` 附加到 `mbuf 链`。如果新数据不适合现有空间，则扩展 mbuf 链。

**`m_prepend(mbuf, len, how)`** 分配一个新的 `mbuf` 并将其前置于 `mbuf 链`，正确处理 `M_PKTHDR`。**注意：** 它不分配任何 `mbuf 集群`，因此 `len` 必须小于 `MLEN` 或 `MHLEN`，具体取决于 `M_PKTHDR` 标志的设置。

**`m_copyup(mbuf, len, dstoff)`** 类似于 `m_pullup`，但将 `len` 字节的数据复制到 mbuf 中 `dstoff` 字节处的新 mbuf 中。`dstoff` 参数对齐数据并为链路层报头留出空间。成功时返回新的 `mbuf 链`，失败时释放 `mbuf 链` 并返回 `NULL`。**注意：** 该函数不分配 `mbuf 集群`，因此 `len + dstoff` 必须小于 `MHLEN`。

**`m_pullup(mbuf, len)`** 安排 `mbuf 链` 的前 `len` 字节是连续的，并位于 `mbuf` 的数据区域中，以便可以使用 `mtod(mbuf, type)` 访问它们。重要的是要记住，这可能涉及重新分配一些 mbuf 并移动数据，因此必须重新计算或使引用旧 mbuf 链中数据的所有指针无效。成功时返回新的 `mbuf 链`，失败时返回 `NULL`（在这种情况下 `mbuf 链` 被释放）。**注意：** 它不分配任何 `mbuf 集群`，因此 `len` 必须小于或等于 `MHLEN`。

**`m_pulldown(mbuf, offset, len, offsetp)`** 安排 `mbuf 链` 中 `offset` 和 `offset + len` 之间的 `len` 字节是连续的，并位于 `mbuf` 的数据区域中，以便可以使用 `mtod` 或 `mtodo` 访问它们。`len` 必须小于或等于 `mbuf 集群` 的大小。返回指向链中包含请求区域的中间 `mbuf` 的指针；返回的 mbuf 中包含的数据在 `mbuf 链` 数据区域中的偏移量存储在 `*offsetp` 中。如果 `offsetp` 为 NULL，则可以使用 `mtod(mbuf, type)` 或 `mtodo(mbuf, 0)` 访问该区域。如果 `offsetp` 为非 NULL，则可以使用 `mtodo(mbuf, *offsetp)` 访问该区域。mbuf 链开头和 `offset` 之间的区域不会被修改，因此在调用 `m_pulldown` 之前持有指向该区域内数据的指针是安全的。

**`m_copym(mbuf, offset, len, how)`** 从开头开始 `offset` 字节处复制 `mbuf 链`，持续 `len` 字节。如果 `len` 为 `M_COPYALL`，则复制到 `mbuf 链` 的末尾。**注意：** 副本是只读的，因为 `mbuf 集群` 未被复制，只是增加其引用计数。

**`m_copypacket(mbuf, how)`** 复制整个数据包包括报头（必须存在）。这是常见情况 `m_copym(mbuf, 0, M_COPYALL, how)` 的优化版本。**注意：** 副本是只读的，因为 `mbuf 集群` 未被复制，只是增加其引用计数。

**`m_dup(mbuf, how)`** 将数据包头 `mbuf 链` 复制为一个全新的 `mbuf 链`，包括复制任何 `mbuf 集群`。当需要 `mbuf 链` 的可写副本时，请使用此函数而不是 `m_copypacket`。

**`m_copydata(mbuf, offset, len, buf)`** 从 `mbuf 链` 开头 `off` 字节处开始复制 `len` 字节的数据到指定的缓冲区 `buf`。

**`m_copyback(mbuf, offset, len, buf)`** 将缓冲区 `buf` 中的 `len` 字节复制回指定的 `mbuf 链`，从 `mbuf 链` 开头 `offset` 字节处开始，如有必要则扩展 `mbuf 链`。**注意：** 它不分配任何 `mbuf 集群`，只是将 `mbuf` 添加到 `mbuf 链`。可以安全地将 `offset` 设置为超出当前 `mbuf 链` 末尾：将分配清零的 `mbuf` 来填充空间。

**`m_length(mbuf, last)`** 返回 `mbuf 链` 的长度，以及可选的指向最后一个 `mbuf` 的指针。

**`m_dup_pkthdr(to, from, how)`** 在函数完成时，`mbuf` `to` 将包含 `from->m_pkthdr` 和 `mbuf 链` `from` 中找到的每个数据包属性的相同副本。`mbuf` `from` 最初必须设置 `M_PKTHDR` 标志，`to` 在进入时必须为空。

**`m_move_pkthdr(to, from)`** 将 `m_pkthdr` 和每个数据包属性从 `mbuf 链` `from` 移动到 `mbuf` `to`。`mbuf` `from` 最初必须设置 `M_PKTHDR` 标志，`to` 在进入时必须为空。函数完成时，`from` 将清除 `M_PKTHDR` 标志和每个数据包属性。

**`m_fixhdr(mbuf)`** 将数据包头长度设置为 `mbuf 链` 的长度。

**`m_devget(buf, len, offset, ifp, copy)`** 将 `buf` 指向的设备本地内存中的数据复制到 `mbuf 链`。使用指定的复制例程 `copy` 进行复制，如果 `copy` 为 `NULL` 则使用 `bcopy`。

**`m_cat(m, n)`** 将 `n` 连接到 `m`。两个 `mbuf 链` 必须是相同类型。`m_cat` 返回后，`n` 不保证有效。`m_cat` 不更新任何数据包头字段或释放 mbuf 标签。

**`m_catpkt(m, n)`** `m_cat` 的一个变体，对数据包进行操作。`m` 和 `n` 都必须包含数据包头。`m_catpkt` 返回后，`n` 不保证有效。

**`m_split(mbuf, len, how)`** 将 `mbuf 链` 分成两部分，返回尾部：除前 `len` 字节以外的所有内容。如果失败，它返回 `NULL` 并尝试将 `mbuf 链` 恢复到原始状态。

**`m_apply(mbuf, off, len, f, arg)`** 在 `mbuf 链` 上偏移 `off` 处，长度 `len` 字节应用一个函数。通常用于避免调用 `m_pullup`，否则这些调用将是不必要或不可取的。`arg` 是一个便利参数，传递给回调函数 `f`。每次调用 `f` 时，它将传递 `arg`、指向当前 mbuf 中 `data` 的指针以及应该应用函数的此 mbuf 中数据的长度 `len`。函数应返回零以表示成功；否则，如果指示错误，则 `m_apply` 将返回错误并停止遍历 `mbuf 链`。

**`m_getptr(mbuf, loc, off)`** 返回指向包含位于 `mbuf 链` 开头 `loc` 字节处数据的 mbuf 的指针。相应的 mbuf 内偏移量将存储在 `*off` 中。

**`m_defrag(m0, how)`** 对 mbuf 链进行碎片整理，返回尽可能短的 mbuf 和集群链。如果分配失败且无法完成，则返回 `NULL` 并且原始链保持不变。成功时，原始链将被释放并返回新链。`how` 应为 `M_WAITOK` 或 `M_NOWAIT`，具体取决于调用者的偏好。此函数在网络驱动程序中特别有用，其中某些长 mbuf 链在添加到 TX 描述符列表之前必须缩短。

**`m_collapse(m0, how, maxfrags)`** 对 mbuf 链进行碎片整理，返回最多 `maxfrags` 个 mbuf 和集群的链。如果分配失败或链无法按请求折叠，则返回 `NULL`，原始链可能被修改。与 `m_defrag` 一样，`how` 应为 `M_WAITOK` 或 `M_NOWAIT` 之一。

**`m_unshare(m0, how)`** 创建指定 mbuf 链的一个版本，其内容可以安全修改而不会影响其他用户。如果分配失败且无法完成此操作，则返回 `NULL`。原始 mbuf 链始终被回收，并且任何共享 mbuf 集群的引用计数都会减少。`how` 应为 `M_WAITOK` 或 `M_NOWAIT`，具体取决于调用者的偏好。作为此过程的副作用，返回的 mbuf 链可能会被压缩。此函数在网络代码的发送路径中特别有用，当数据在发送之前必须加密或以其他方式更改时。

## 硬件辅助校验和计算

本节目前仅适用于 IP 上的 SCTP、TCP 和 UDP。为了节省主机 CPU 资源，如果可能，校验和计算会卸载到网络接口硬件。数据包的前导 `mbuf` 的 `m_pkthdr` 成员包含用于此目的的两个字段：`int` `csum_flags` 和 `int` `csum_data`。这些字段的含义取决于数据包是否被分片。此后，数据包的 `csum_flags` 或 `csum_data` 将表示包含数据包的 `mbuf 链` 中前导 `mbuf` 的 `m_pkthdr` 成员的相应字段。

当数据包由 SCTP、TCP 或 UDP 发送时，校验和的计算会延迟到确定数据包的输出接口之后。IP 会查询接口特定字段 `ifnet.if_data.ifi_hwassist`（参见 [ifnet(9)](ifnet.9.md)）以了解为输出选择的网络接口的能力，以协助计算校验和。数据包头的 `csum_flags` 字段被设置为指示接口应该对其执行的操作。网络接口不支持的操作在将数据包传递给接口驱动程序之前在软件中完成；此类操作永远不会通过 `csum_flags` 请求。

要求接口执行特定操作的标志如下：

**`CSUM_IP`** 将计算 IP 头校验和并存储在数据包的相应字段中。期望硬件知道 IP 头的格式以确定 IP 校验和字段的偏移量。

**`CSUM_SCTP`** 将计算 SCTP 校验和。（见下文。）

**`CSUM_TCP`** 将计算 TCP 校验和。（见下文。）

**`CSUM_UDP`** 将计算 UDP 校验和。（见下文。）

如果 SCTP、TCP 或 UDP 校验和被卸载到硬件，则 `csum_data` 字段将包含校验和字段相对于 IP 头末尾的字节偏移量。对于 TCP 或 UDP，校验和字段最初将由 TCP 或 UDP 实现设置为 TCP 和 UDP 规范定义的伪头校验和。对于 SCTP，校验和字段最初将由 SCTP 实现设置为 0。

当接口接收到数据包时，它通过在与此数据包关联的 `csum_flags` 中设置以下一个或多个标志来指示它已对数据包执行的操作：

**`CSUM_IP_CHECKED`** 已计算 IP 头校验和。

**`CSUM_IP_VALID`** IP 头具有有效的校验和。此标志只能与 `CSUM_IP_CHECKED` 组合出现。

**`CSUM_DATA_VALID`** 已计算 IP 数据包数据部分的校验和并以网络字节顺序存储在字段 `csum_data` 中。

**`CSUM_PSEUDO_HDR`** 只能与 `CSUM_DATA_VALID` 一起设置，以指示 `csum_data` 中找到的 IP 数据校验和允许 TCP 和 UDP 规范定义的伪头。否则，伪头的校验和必须由主机 CPU 计算并添加到 `csum_data` 中，以获得用于 TCP 或 UDP 验证的最终校验和。

如果特定网络接口仅指示 SCTP、TCP 或 UDP 校验和验证的成功或失败，而不向主机 CPU 返回校验和的精确值，则其驱动程序可以在 `csum_flags` 中标记 `CSUM_DATA_VALID`，对于 TCP 和 UDP 还可以标记 `CSUM_PSEUDO_HDR`，并将 `csum_data` 设置为十六进制 `0xFFFF` 以指示有效的校验和。这是所用算法的一个特性，只要包含原始校验和字段，对任何有效数据包计算的互联网校验和都将是 `0xFFFF`。注意，对于 SCTP，`csum_data` 的值不相关，`csum_flags` 中的 `CSUM_PSEUDO_HDR` 也未设置，因为 SCTP 不使用伪头校验和。

如果 IP 将 `csum_flags` 中设置了 `CSUM_IP`、`CSUM_SCTP`、`CSUM_TCP` 或 `CSUM_UDP` 标志的数据包传递给本地 IP、SCTP、TCP 或 UDP 栈，则将处理数据包而不计算或验证校验和，因为数据包未在线上传输。如果数据包由虚拟接口（如 [tap(4)](../man4/tap.4.md) 或 [epair(4)](../man4/epair.4.md)）处理，则可能发生这种情况。

## 压力测试

运行使用 `MBUF_STRESS_TEST` 选项编译的内核时，可以使用以下由 [sysctl(8)](../man8/sysctl.8.md) 控制的选项来创建各种故障/极端情况，用于测试网络驱动程序和依赖 `mbuf` 的内核其他部分。

**`net.inet.ip.mbuf_frag_size`** 导致 `ip_output` 将传出 `mbuf 链` 分片为指定大小的分片。将此变量设置为 1 是测试网络驱动程序处理长 `mbuf 链` 能力的绝佳方式。

**`kern.ipc.m_defragrandomfailures`** 导致函数 `m_defrag` 随机失败并返回 `NULL`。使用 `m_defrag` 的任何代码都应使用此功能进行测试。

## 返回值

见上文。

## 参见

[ifnet(9)](ifnet.9.md), [mbuf_tags(9)](mbuf_tags.9.md)

> S. J. Leffler, W. N. Joy, R. S. Fabry, M. J. Karels, "Networking Implementation Notes", *4.4BSD System Manager's Manual (SMM)*.

## 历史

`Mbufs` 出现在 BSD 的早期版本中。除了用于网络数据包外，它们还用于存储各种动态结构，如路由表条目、接口地址、协议控制块等。在最近的 FreeBSD 中，`mbuf` 的使用几乎完全限于数据包存储，uma(9) 区域直接用于存储其他与网络相关的内存。

从历史上看，`mbuf` 分配器是一个专用内存分配器，能够在中断上下文中运行并从特殊的内核地址空间映射中分配。从 FreeBSD 5.3 开始，`mbuf` 分配器是 uma(9) 的包装器，允许在每 CPU 缓存中缓存 `mbuf`、集群和 `mbuf` + 集群对，以及带来 slab 分配的其他好处。

## 作者

原始 `mbuf` 手册页由 Yar Tikhiy 编写。uma(9) `mbuf` 分配器由 Bosko Milekic 编写。
