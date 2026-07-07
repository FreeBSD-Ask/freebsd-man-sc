# mbchain(9)

`mbchain` — 用于从各种数据类型构建 mbuf 链的一组函数

## 名称

`mbchain`, `mb_init`, `mb_initm`, `mb_done`, `mb_detach`, `mb_fixhdr`, `mb_reserve`, `mb_put_uint8`, `mb_put_uint16be`, `mb_put_uint16le`, `mb_put_uint32be`, `mb_put_uint32le`, `mb_put_int64be`, `mb_put_int64le`, `mb_put_mem`, `mb_put_mbuf`, `mb_put_uio`

## 概要

`options LIBMCHAIN kldload libmchain`

`#include <sys/param.h>`

`#include <sys/uio.h>`

`#include <sys/mchain.h>`

`Ft int Fn mb_init struct mbchain *mbp Ft void Fn mb_initm struct mbchain *mbp struct mbuf *m Ft void Fn mb_done struct mbchain *mbp Ft struct mbuf * Fn mb_detach struct mbchain *mbp Ft int Fn mb_fixhdr struct mbchain *mbp Ft caddr_t Fn mb_reserve struct mbchain *mbp int size Ft int Fn mb_put_uint8 struct mbchain *mbp uint8_t x Ft int Fn mb_put_uint16be struct mbchain *mbp uint16_t x Ft int Fn mb_put_uint16le struct mbchain *mbp uint16_t x Ft int Fn mb_put_uint32be struct mbchain *mbp uint32_t x Ft int Fn mb_put_uint32le struct mbchain *mbp uint32_t x Ft int Fn mb_put_int64be struct mbchain *mbp int64_t x Ft int Fn mb_put_int64le struct mbchain *mbp int64_t x Ft int Fn mb_put_mem struct mbchain *mbp c_caddr_t source int size int type Ft int Fn mb_put_mbuf struct mbchain *mbp struct mbuf *m Ft int Fn mb_put_uio struct mbchain *mbp struct uio *uiop int size`

## 描述

这些函数用于从各种数据类型组合 mbuf 链。`mbchain` 结构用作工作上下文，应通过调用 `mb_init` 或 `mb_initm` 进行初始化。它具有以下字段：

**`mb_top`** (`struct mbuf *`) 指向已构建 mbuf 链顶部的指针。

**`mb_cur`** (`struct mbuf *`) 指向当前正在填充的 mbuf 的指针。

**`mb_mleft`** (`int`) 当前 mbuf 中剩余的字节数。

**`mb_count`** (`int`) 放入 mbuf 链的总字节数。

**`mb_copy`** (`mb_copy_t *`) 用户定义的用于执行复制到 mbuf 的函数；在需要任何异常数据转换时很有用。

**`mb_udata`** (`void *`) 用户提供的、可在 `mb_copy` 函数中使用的数据。

`mb_done` 函数释放由 `mbp->mb_top` 字段指向的 mbuf 链，并将该字段设置为 `NULL`。

`mb_detach` 函数返回 `mbp->mb_top` 字段的值，并将其值设置为 `NULL`。

`mb_fixhdr` 重新计算 mbuf 链的长度，并更新链中第一个 mbuf 的 `m_pkthdr.len` 字段。它返回计算出的长度。

`mb_reserve` 确保由 `size` 参数指定长度的对象能够放入当前 mbuf（必要时执行 mbuf 分配），并推进所有指针，就像放置了真实数据一样。返回值将指向保留空间的开头。注意，对象的大小不应超过 `MLEN` 字节。

所有 `mb_put_*` 函数都执行将数据实际复制到 mbuf 链的操作。带有 `le` 或 `be` 后缀的函数将执行到小端或大端数据格式的转换。

`mb_put_mem` 函数将 `source` 参数指定的 `size` 字节数据复制到 mbuf 链。`type` 参数指定执行复制的方法，可以是以下之一：

**`MB_MSYSTEM`** 使用 `bcopy` 函数。

**`MB_MUSER`** 使用 copyin(9) 函数。

**`MB_MINLINE`** 使用不调用任何函数的"内联"循环。

**`MB_MZERO`** 不复制任何数据，只是用零字节填充目标。

**`MB_MCUSTOM`** 调用由 `mbp->mb_copy` 字段指定的函数。

## 返回值

除 `mb_fixhdr` 外，所有 `int` 函数如果成功则返回零，否则返回错误代码。

*注意：* 任何函数失败后，mbuf 链都会处于损坏状态，只有 `mb_done` 函数可以安全地调用以销毁它。

## 实例

```c
struct mbchain *mbp;
struct mbuf *m;
mb_init(mbp);
mb_put_uint8(mbp, 33);
mb_put_uint16le(mbp, length);
m = m_copym(mbp->mb_top, 0, M_COPYALL, M_WAIT);
send(m);
mb_done(mbp);
```

## 参见

[mbuf(9)](mbuf.9.md), [mdchain(9)](mdchain.9.md)

## 作者

本手册页由 Boris Popov <bp@FreeBSD.org> 编写。
