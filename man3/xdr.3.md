# xdr(3)

`xdr` — 外部数据表示的库例程

## 名称

`xdr`, `xdr_array`, `xdr_bool`, `xdr_bytes`, `xdr_char`, `xdr_destroy`, `xdr_double`, `xdr_enum`, `xdr_float`, `xdr_free`, `xdr_getpos`, `xdr_hyper`, `xdr_inline`, `xdr_int`, `xdr_long`, `xdr_longlong_t`, `xdrmem_create`, `xdr_opaque`, `xdr_pointer`, `xdrrec_create`, `xdrrec_endofrecord`, `xdrrec_eof`, `xdrrec_skiprecord`, `xdr_reference`, `xdr_setpos`, `xdr_short`, `xdr_sizeof`, `xdrstdio_create`, `xdr_string`, `xdr_u_char`, `xdr_u_hyper`, `xdr_u_int`, `xdr_u_long`, `xdr_u_longlong_t`, `xdr_u_short`, `xdr_union`, `xdr_vector`, `xdr_void`, `xdr_wrapstring`

## 库

Lb libc

## 概要

`#include <rpc/types.h>`

`#include <rpc/xdr.h>`

函数声明参见描述一节。

## 描述

这些例程允许 C 程序员以机器无关的方式描述任意数据结构。远程过程调用的数据使用这些例程传输。

```c
int
xdr_array(XDR *xdrs, char **arrp, u_int *sizep,
    u_int maxsize, u_int elsize, xdrproc_t elproc);
```

一种过滤器原语，用于在变长数组及其对应的外部表示之间进行转换。`arrp` 参数是指向数组指针的地址，`sizep` 参数是数组元素计数地址；该元素计数不能超过 `maxsize`。`elsize` 参数是每个数组元素的 `sizeof`，`elproc` 是一个 XDR 过滤器，用于在数组元素的 C 形式及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_bool(XDR *xdrs, bool_t *bp);
```

一种过滤器原语，用于在布尔值（C 整数）及其外部表示之间转换。编码数据时，此过滤器产生值 1 或 0。成功时返回 1，否则返回 0。

```c
int
xdr_bytes(XDR *xdrs, char **sp, u_int *sizep, u_int maxsize);
```

一种过滤器原语，用于在计数字节字符串及其外部表示之间转换。`sp` 参数是指向字符串指针的地址。字符串的长度位于地址 `sizep` 处；字符串长度不能超过 `maxsize`。成功时返回 1，否则返回 0。

```c
int
xdr_char(XDR *xdrs, char *cp);
```

一种过滤器原语，用于在 C 字符及其外部表示之间转换。成功时返回 1，否则返回 0。注意：编码后的字符不进行打包，每个字符占用 4 字节。对于字符数组，建议考虑 `xdr_bytes`、`xdr_opaque` 或 `xdr_string`。

```c
void
xdr_destroy(XDR *xdrs);
```

一个宏，调用与 XDR 流 `xdrs` 关联的销毁例程。销毁通常涉及释放与该流关联的私有数据结构。调用 `xdr_destroy` 之后使用 `xdrs` 的行为未定义。

```c
int
xdr_double(XDR *xdrs, double *dp);
```

一种过滤器原语，用于在 C `double` 精度数字及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_enum(XDR *xdrs, enum_t *ep);
```

一种过滤器原语，用于在 C `enum`（实际上是整数）及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_float(XDR *xdrs, float *fp);
```

一种过滤器原语，用于在 C `float` 及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
void
xdr_free(xdrproc_t proc, void *objp);
```

通用释放例程。第一个参数是所释放对象的 XDR 例程。第二个参数是指向对象本身的指针。注意：传递给此例程的指针*不会*被释放，但它所指向的内容*会*被（递归地）释放。

```c
u_int
xdr_getpos(XDR *xdrs);
```

一个宏，调用与 XDR 流 `xdrs` 关联的获取位置例程。该例程返回一个无符号整数，指示 XDR 字节流的位置。XDR 流的一个理想特性是简单的算术运算可以用于此数字，尽管 XDR 流实例不必保证这一点。

```c
int
xdr_hyper(XDR *xdrs, quad_t *llp);
```

一种过滤器原语，用于在 ANSI C `long long` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
long *
xdr_inline(XDR *xdrs, int len);
```

一个宏，调用与 XDR 流 `xdrs` 关联的内联例程。该例程返回指向流缓冲区中连续块的指针；`len` 是所需缓冲区的字节长度。注意：指针被转换为 `long *`。警告：如果无法分配连续的缓冲区块，`xdr_inline` 可能返回 `NULL`（0）。因此，不同流实例的行为可能不同；它的存在是为了提高效率。

```c
int
xdr_int(XDR *xdrs, int *ip);
```

一种过滤器原语，用于在 C 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_long(XDR *xdrs, long *lp);
```

一种过滤器原语，用于在 C `long` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_longlong_t(XDR *xdrs, quad_t *llp);
```

一种过滤器原语，用于在 ANSI C `long long` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
void
xdrmem_create(XDR *xdrs, char *addr, u_int size, enum xdr_op op);
```

此例程初始化 `xdrs` 所指向的 XDR 流对象。流的数据写入到或读取自位于 `addr` 的一块内存，其长度不超过 `size` 字节。`op` 参数决定 XDR 流的方向（`XDR_ENCODE`、`XDR_DECODE` 或 `XDR_FREE`）。

```c
int
xdr_opaque(XDR *xdrs, char *cp, u_int cnt);
```

一种过滤器原语，用于在固定大小的不透明数据及其外部表示之间转换。`cp` 参数是不透明对象的地址，`cnt` 是其字节大小。成功时返回 1，否则返回 0。

```c
int
xdr_pointer(XDR *xdrs, char **objpp, u_int objsize,
    xdrproc_t xdrobj);
```

类似于 `xdr_reference`，不同之处在于它可以序列化 `NULL` 指针，而 `xdr_reference` 不能。因此，`xdr_pointer` 可以表示递归数据结构，如二叉树或链表。

```c
void
xdrrec_create(XDR *xdrs, u_int sendsize, u_int recvsize,
    void *handle, int (*readit)(void *, void *, int),
    int (*writeit)(void *, void *, int));
```

此例程初始化 `xdrs` 所指向的 XDR 流对象。流的数据写入大小为 `sendsize` 的缓冲区；值为零表示系统应使用合适的默认值。流的数据从大小为 `recvsize` 的缓冲区读取；同样可以通过传递零值来设置为合适的默认值。当流的输出缓冲区满时，调用 `writeit`。类似地，当流的输入缓冲区为空时，调用 `readit`。这两个例程的行为类似于系统调用 [read(2)](../sys/read.2.md) 和 [write(2)](../sys/write.2.md)，不同之处在于 `handle` 作为第一个参数传递给前述例程。注意：XDR 流的 `op` 字段必须由调用者设置。警告：此 XDR 流实现了中间记录流。因此流中有额外的字节用于提供记录边界信息。

```c
int
xdrrec_endofrecord(XDR *xdrs, int sendnow);
```

此例程只能在由 `xdrrec_create` 创建的流上调用。输出缓冲区中的数据被标记为一条完整的记录，如果 `sendnow` 非零，则可选地写出输出缓冲区。成功时返回 1，否则返回 0。

```c
int
xdrrec_eof(XDR *xdrs);
```

此例程只能在由 `xdrrec_create` 创建的流上调用。消耗流中当前记录的剩余部分后，如果流没有更多输入，此例程返回 1，否则返回 0。

```c
int
xdrrec_skiprecord(XDR *xdrs);
```

此例程只能在由 `xdrrec_create` 创建的流上调用。它告知 XDR 实现应丢弃流的输入缓冲区中当前记录的剩余部分。成功时返回 1，否则返回 0。

```c
int
xdr_reference(XDR *xdrs, char **pp, u_int size, xdrproc_t proc);
```

一种在结构内提供指针追踪的原语。`pp` 参数是指针的地址；`size` 是 `*pp` 所指向结构的 `sizeof`；`proc` 是一个 XDR 过程，用于在结构的 C 形式及其外部表示之间进行过滤。成功时返回 1，否则返回 0。警告：此例程不理解 `NULL` 指针。请改用 `xdr_pointer`。

```c
int
xdr_setpos(XDR *xdrs, u_int pos);
```

一个宏，调用与 XDR 流 `xdrs` 关联的设置位置例程。`pos` 参数是从 `xdr_getpos` 获取的位置值。如果 XDR 流可以重新定位，此例程返回 1，否则返回 0。警告：某些类型的 XDR 流难以重新定位，因此此例程可能对一种类型的流失败而对另一种成功。

```c
int
xdr_short(XDR *xdrs, short *sp);
```

一种过滤器原语，用于在 C `short` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
unsigned long
xdr_sizeof(xdrproc_t func, void *data);
```

此例程返回使用过滤器 `func` 编码 `data` 所需的内存量。

```c
#ifdef _STDIO_H_
/* 使用 stdio 库的 XDR */
void
xdrstdio_create(XDR *xdrs, FILE *file, enum xdr_op op);
#endif
```

此例程初始化 `xdrs` 所指向的 XDR 流对象。XDR 流数据写入到或读取自标准 I/O 流 `file`。`op` 参数决定 XDR 流的方向（`XDR_ENCODE`、`XDR_DECODE` 或 `XDR_FREE`）。警告：与此类 XDR 流关联的销毁例程会对 `file` 流调用 [fflush(3)](../stdio/fflush.3.md)，但从不调用 [fclose(3)](../stdio/fclose.3.md)。

```c
int
xdr_string(XDR *xdrs, char **sp, u_int maxsize);
```

一种过滤器原语，用于在 C 字符串及其对应的外部表示之间转换。字符串长度不能超过 `maxsize`。注意：`sp` 是字符串指针的地址。成功时返回 1，否则返回 0。

```c
int
xdr_u_char(XDR *xdrs, unsigned char *ucp);
```

一种过滤器原语，用于在 `unsigned` C 字符及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_u_hyper(XDR *xdrs, u_quad_t *ullp);
```

一种过滤器原语，用于在 `unsigned` ANSI C `long long` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_u_int(XDR *xdrs, unsigned *up);
```

一种过滤器原语，用于在 C `unsigned` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_u_long(XDR *xdrs, unsigned long *ulp);
```

一种过滤器原语，用于在 C `unsigned long` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_u_longlong_t(XDR *xdrs, u_quad_t *ullp);
```

一种过滤器原语，用于在 `unsigned` ANSI C `long long` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_u_short(XDR *xdrs, unsigned short *usp);
```

一种过滤器原语，用于在 C `unsigned short` 整数及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_union(XDR *xdrs, enum_t *dscmp, char *unp,
    const struct xdr_discrim *choices, xdrproc_t defaultarm);
```

一种过滤器原语，用于在判别式 C `union` 及其对应的外部表示之间转换。它首先转换位于 `dscmp` 处的联合的判别式。此判别式始终是 `enum_t`。接下来转换位于 `unp` 处的联合。`choices` 参数是指向 `xdr_discrim` 结构数组的指针。每个结构包含一个有序对 [`value`, `proc`]。如果联合的判别式等于关联的 `value`，则调用 `proc` 来转换联合。`xdr_discrim` 结构数组的末尾由值为 `NULL` 的例程表示。如果在 `choices` 数组中未找到判别式，则调用 `defaultarm` 过程（如果它不是 `NULL`）。成功时返回 1，否则返回 0。

```c
int
xdr_vector(XDR *xdrs, char *arrp, u_int size,
    u_int elsize, xdrproc_t elproc);
```

一种过滤器原语，用于在定长数组及其对应的外部表示之间转换。`arrp` 参数是指向数组指针的地址，`size` 是数组的元素计数。`elsize` 参数是每个数组元素的 `sizeof`，`elproc` 是一个 XDR 过滤器，用于在数组元素的 C 形式及其外部表示之间转换。成功时返回 1，否则返回 0。

```c
int
xdr_void(void);
```

此例程始终返回 1。可传递给需要函数参数的 RPC 例程，此时无需执行任何操作。

```c
int
xdr_wrapstring(XDR *xdrs, char **sp);
```

一种原语，调用 `xdr_string(xdrs, sp, MAXUN.UNSIGNED)`；其中 `MAXUN.UNSIGNED` 是无符号整数的最大值。`xdr_wrapstring` 函数很方便，因为 RPC 包最多传递两个 XDR 例程作为参数，而 `xdr_string` 作为最常用的原语之一需要三个参数。成功时返回 1，否则返回 0。

## 参见

[rpc(3)](../rpc/rpc.3.md)

> "eXternal Data Representation Standard: Protocol Specification".

> "eXternal Data Representation: Sun Technical Notes".

> "XDR: External Data Representation Standard", RFC1014.

## 历史

`xdr_sizeof` 函数首次出现于 FreeBSD 9.0。
