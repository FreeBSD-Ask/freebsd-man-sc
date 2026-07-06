# mbuf_tags.9

`mbuf_tags` — 通用数据包属性框架

## 名称

`mbuf_tags`

## 概要

`#include <sys/mbuf.h>`

`Ft struct m_tag * Fn m_tag_alloc uint32_t cookie uint16_t type int len int wait Ft struct m_tag * Fn m_tag_copy struct m_tag *t int how Ft int Fn m_tag_copy_chain struct mbuf *to const struct mbuf *from int how Ft void Fn m_tag_delete struct mbuf *m struct m_tag *t Ft void Fn m_tag_delete_chain struct mbuf *m struct m_tag *t Ft void Fn m_tag_delete_nonpersistent struct mbuf *m Ft struct m_tag * Fn m_tag_find struct mbuf *m uint16_t type struct m_tag *start Ft struct m_tag * Fn m_tag_first struct mbuf *m Ft void Fn m_tag_free struct m_tag *t Ft struct m_tag * Fn m_tag_get uint16_t type int len int wait Ft void Fn m_tag_init struct mbuf *m Ft struct m_tag * Fn m_tag_locate struct mbuf *m uint32_t cookie uint16_t type struct m_tag *t Ft struct m_tag * Fn m_tag_next struct mbuf *m struct m_tag *t Ft void Fn m_tag_prepend struct mbuf *m struct m_tag *t Ft void Fn m_tag_unlink struct mbuf *m struct m_tag *t`

## 描述

Mbuf 标签允许通过提供一种将额外内核内存标记到数据包头 mbuf 上的机制，将额外的元数据与传输中的数据包相关联。标签在 [mbuf(9)](mbuf.9.md) 头部的链中维护，并使用一系列 API 调用来分配、搜索和删除标签。标签使用唯一标识一类标记到数据包上的数据的 ID 和 cookie 来标识，并且可以包含任意数量的额外存储。mbuf 标签的典型用途包括 [mac(9)](mac.9.md) 中描述的强制访问控制（MAC）标签、[ipsec(4)](../man4/ipsec.4.md) 中描述的 IPsec 策略信息以及 [pf(4)](../man4/pf.4.md) 使用的数据包过滤器标签。

标签会在各种操作中维护，包括使用 `M_COPY_PKTHDR` 和 `M_MOVE_PKTHDR` 等工具复制数据包头。与 mbuf 头部相关联的任何标签将在 mbuf 释放时自动释放，尽管某些子系统希望在此之前删除标签。

不同的内核 API 使用数据包标签来跟踪对数据包已完成或计划执行的操作。每个数据包标签可以通过其类型和 cookie 来区分。cookie 用于标识特定的模块或 API。数据包标签附加到 mbuf 数据包头。

标签的前 `sizeof(struct m_tag)` 字节包含一个 `struct m_tag`：

```c
struct m_tag {
	SLIST_ENTRY(m_tag)	m_tag_link;	/* 数据包标签列表 */
	uint16_t		m_tag_id;	/* 标签 ID */
	uint16_t		m_tag_len;	/* 数据长度 */
	uint32_t		m_tag_cookie;	/* ABI/模块 ID */
	void			(*m_tag_free)(struct m_tag *);
};
```

`m_tag_link` 字段用于将标签链接在一起（详见 [queue(3)](../man3/queue.3.md)）。`m_tag_id`、`m_tag_len` 和 `m_tag_cookie` 字段分别设置为类型、长度和 cookie。`m_tag_free` 指向 `m_tag_free_default`。在此结构之后是 `m_tag_len` 字节的空间，可用于存储标签特定信息。寻址此数据区域可能有些棘手。一种安全的方法是将 `struct m_tag` 嵌入到私有数据结构中，如下所示：

```c
struct foo {
	struct m_tag	tag;
	...
};
struct foo *p = (struct foo *)m_tag_alloc(...);
struct m_tag *mtag = &p->tag;
```

注意，OpenBSD 不支持 cookie，它需要 `m_tag_id` 全局唯一。为了与 OpenBSD 保持兼容，提供了 cookie `MTAG_ABI_COMPAT` 以及一些兼容性函数。编写 OpenBSD 兼容代码时，应注意不要使用已使用的标签类型。标签类型定义于

`#include <sys/mbuf.h>`

### 数据包标签操作函数

**`m_tag_alloc(cookie, type, len, wait)`** 分配一个类型为 `type`、cookie 为 `cookie` 的新标签，标签头之后有 `len` 字节的空间。`wait` 参数直接传递给 [malloc(9)](malloc.9.md)。如果成功，`m_tag_alloc` 返回一个 (`len` + `sizeof(struct m_tag)`) 字节的内存缓冲区。否则，返回 `NULL`。还提供了一个兼容函数 `m_tag_get`。

**`m_tag_copy(tag, how)`** 分配 `tag` 的副本。`how` 参数直接传递给 `m_tag_alloc`。返回值与 `m_tag_alloc` 中的相同。

**`m_tag_copy_chain(tombuf, frommbuf, how)`** 分配并将 mbuf `frommbuf` 的所有标签复制到 mbuf `tombuf`。成功时返回 1，失败时返回 0。在后一种情况下，mbuf `tombuf` 将丢失其所有标签，甚至包括之前存在的标签。

**`m_tag_delete(mbuf, tag)`** 从 `mbuf` 的列表中删除 `tag` 并释放它。

**`m_tag_delete_chain(mbuf, tag)`** 从 `tag` 开始删除并释放数据包标签链。如果 `tag` 为 `NULL`，则删除所有标签。

**`m_tag_delete_nonpersistent(mbuf)`** 遍历 `mbuf` 的标签并删除那些未设置 `MTAG_PERSISTENT` 标志的标签。

**`m_tag_first(mbuf)`** 返回与 `mbuf` 相关联的第一个标签。

**`m_tag_free(tag)`** 使用其 `m_tag_free` 方法释放 `tag`。默认使用 `m_tag_free_default` 函数。

**`m_tag_init(mbuf)`** 为数据包 `mbuf` 初始化标签存储。

**`m_tag_locate(mbuf, cookie, type, tag)`** 在 `mbuf` 中搜索由 `type` 和 `cookie` 定义的标签，从 `tag` 指定的位置开始。如果后者为 `NULL`，则搜索整个列表。成功时，返回指向第一个找到的标签的指针。在任何情况下，都返回 `NULL`。还提供了一个兼容函数 `m_tag_find`。

**`m_tag_next(mbuf, tag)`** 返回 `mbuf` 中 `tag` 之后的标签。如果不存在，则返回 `NULL`。

**`m_tag_prepend(mbuf, tag)`** 将新标签 `tag` 添加到数据包 `mbuf` 的标签列表的头部。

**`m_tag_unlink(mbuf, tag)`** 从数据包 `mbuf` 的标签列表中删除标签 `tag`。

## 代码参考

标签操作代码包含在文件 `sys/kern/uipc_mbuf2.c` 中。内联函数定义于

`#include <sys/mbuf.h>`

## 参见

[queue(3)](../man3/queue.3.md), [mbuf(9)](mbuf.9.md)

## 历史

数据包标签首次出现于 OpenBSD 2.9，由 Angelos D. Keromytis <angelos@openbsd.org> 编写。
