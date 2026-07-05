# mdchain.9

`mdchain` — 一组将 mbuf 链拆解为各种数据类型的函数

## 名称

`mdchain`, `md_initm`, `md_done`, `md_append_record`, `md_next_record`, `md_get_uint8`, `md_get_uint16`, `md_get_uint16be`, `md_get_uint16le`, `md_get_uint32`, `md_get_uint32be`, `md_get_uint32le`, `md_get_int64`, `md_get_int64be`, `md_get_int64le`, `md_get_mem`, `md_get_mbuf`, `md_get_uio`

## 概要

```c
options LIBMCHAIN
kldload libmchain
```

```c
#include <sys/param.h>
```

```c
#include <sys/uio.h>
```

```c
#include <sys/mchain.h>
```

```c
void
md_initm(struct mdchain *mdp, struct mbuf *m)

void
md_done(struct mdchain *mdp)

void
md_append_record(struct mdchain *mdp, struct mbuf *top)

int
md_next_record(struct mdchain *mdp)

int
md_get_uint8(struct mdchain *mdp, uint8_t *x)

int
md_get_uint16(struct mdchain *mdp, uint16_t *x)

int
md_get_uint16be(struct mdchain *mdp, uint16_t *x)

int
md_get_uint16le(struct mdchain *mdp, uint16_t *x)

int
md_get_uint32(struct mdchain *mdp, uint32_t *x)

int
md_get_uint32be(struct mdchain *mdp, uint32_t *x)

int
md_get_uint32le(struct mdchain *mdp, uint32_t *x)

int
md_get_int64(struct mdchain *mdp, int64_t *x)

int
md_get_int64be(struct mdchain *mdp, int64_t *x)

int
md_get_int64le(struct mdchain *mdp, int64_t *x)

int
md_get_mem(struct mdchain *mdp, caddr_t target, int size, int type)

int
md_get_mbuf(struct mdchain *mdp, int size, struct mbuf **m)

int
md_get_uio(struct mdchain *mdp, struct uio *uiop, int size)
```

## 描述

这些函数用于将 mbuf 链拆解为各种数据类型。`mdchain` 结构用作工作上下文，应通过调用 `mb_initm` 函数进行初始化。它包含以下字段：

**`md_top`**（`struct mbuf *`）指向所解析 mbuf 链顶部的指针。

**`md_cur`**（`struct mbuf *`）指向当前正在解析的 mbuf 的指针。

**`md_pas`**（`int`）当前 mbuf 中的偏移量。

`md_done` 函数释放由 `mdp->md_top` 字段指向的 mbuf 链，并将该字段设为 `NULL`。

`md_append_record` 使用 `m_nextpkt` 字段追加新的 mbuf 链，形成 mbuf 链的单链表。如果 `mdp->md_top` 字段为 `NULL`，则此函数的行为与 `md_initm` 函数完全相同。

`md_next_record` 函数提取下一个 mbuf 链并释放当前链（如果存在）。对于新的 mbuf 链，它调用 `md_initm` 函数。如果没有剩余数据，函数返回 `ENOENT`。

所有 `md_get_*` 函数执行从 mbuf 链实际复制数据的操作。带有 `le` 或 `be` 后缀的函数将执行到小端或大端数据格式的转换。

`md_get_mem` 函数从 mbuf 链中复制由 `source` 参数指定的 `size` 字节数据。`type` 参数指定执行复制所用的方法，可为以下之一：

**`MB_MSYSTEM`** 使用 `bcopy` 函数。

**`MB_MUSER`** 使用 copyin(9) 函数。

**`MB_MINLINE`** 使用不调用任何函数的“内联”循环。

如果 `target` 为 `NULL`，则不执行实际复制，函数仅跳过给定数量的字节。

## 返回值

所有 `int` 函数成功时返回零，否则返回错误码。

*注意：* 任一函数失败后，mbuf 链将处于损坏状态，只有 `md_done` 函数可以安全地调用以销毁它。

## 实例

```c
struct mdchain *mdp;
struct mbuf *m;
uint16_t length;
uint8_t byte;
receive(so, &m);
md_initm(mdp, m);
if (md_get_uint8(mdp, &byte) != 0 ||
    md_get_uint16le(mdp, &length) != 0)
	error = EBADRPC;
mb_done(mdp);
```

## 参见

[mbchain(9)](mbchain.9.md), [mbuf(9)](mbuf.9.md)

## 作者

本手册页由 Boris Popov <bp@FreeBSD.org> 编写。
