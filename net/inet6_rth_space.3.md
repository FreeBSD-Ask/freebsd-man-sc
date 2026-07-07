# inet6_rth_space(3)

`inet6_rth_space` — IPv6 路由头选项操作

## 名称

`inet6_rth_space`, `inet6_rth_init`, `inet6_rth_add`, `inet6_rth_reverse`, `inet6_rth_segments`, `inet6_rth_getaddr`

## 概要

`#include <netinet/in.h>`

```c
socklen_t
inet6_rth_space(int, int);

void *
inet6_rth_init(void *, socklen_t, int, int);

int
inet6_rth_add(void *, const struct in6_addr *);

int
inet6_rth_reverse(const void *, void *);

int
inet6_rth_segments(const void *);

struct in6_addr *
inet6_rth_getaddr(const void *, int);
```

## 描述

IPv6 高级 API（RFC 3542）定义了应用程序调用以构建和检查 IPv6 路由头的函数。路由头用于在 IPv6 网络中执行源路由。RFC 使用"segments"（段）一词来描述地址，此处也采用该术语。所有函数都定义在

`#include <netinet/in.h>`

头文件中。本手册页中描述的所有函数都操作于

`#include <netinet/ip6.h>`

中定义的路由头结构，但不应在此 API 的使用之外对其进行修改。路由头结构的大小和形状可能发生变化，因此使用这些 API 是更具可移植性的长期解决方案。

API 中的函数分为两组：构建路由头的函数和解析接收到的路由头的函数。下面先描述构建函数，再描述解析函数。

### inet6_rth_space

`inet6_rth_space` 函数返回存放 `type` 参数指定的类型、且包含 `segments` 参数指定数量地址的路由头所需的字节数。当类型为 `IPV6_RTHDR_TYPE_0` 时，段数必须为 0 到 127。`IPV6_RTHDR_TYPE_2` 类型的路由头仅包含一个段，且仅用于移动 IPv6。此函数的返回值是存储路由头所需的字节数。如果返回值为 0，则表示路由头类型未被识别或发生了其他错误。

### inet6_rth_init

`inet6_rth_init` 函数将 `bp` 所指向的预分配缓冲区初始化为包含指定类型的路由头。`bp_len` 参数用于验证缓冲区是否足够大。调用者必须分配 `bp` 所指向的缓冲区。所需的缓冲区大小应通过调用前面描述的 `inet6_rth_space` 来确定。

`inet6_rth_init` 函数成功时返回指向 `bp` 的指针，出错时返回 `NULL`。

### inet6_rth_add

`inet6_rth_add` 函数将 `addr` 所指向的 IPv6 地址添加到正在构建的路由头的末尾。

添加成功时函数返回 0，否则返回 -1。

### inet6_rth_reverse

`inet6_rth_reverse` 函数接受 `in` 参数所指向的路由头，并将新的路由头写入 `out` 所指向的参数中。该路由头使数据报沿着原路由的反向路径发送。两个参数都允许指向同一缓冲区，意味着反转操作可以就地完成。

函数成功时返回 0，出错时返回 -1。

下一组函数操作于应用程序想要解析的路由头。在通常情况下，此类路由头是从网络接收的，但这些函数也可用于应用程序自身创建的路由头。

### inet6_rth_segments

`inet6_rth_segments` 函数返回 `bp` 所指向的路由头中包含的段数。返回值为路由头中包含的段数，出错时返回 -1。返回 0 不是错误，因为路由头可以包含 0 个段。

### inet6_rth_getaddr

`inet6_rth_getaddr` 函数用于从路由头中检索单个地址。`index` 是应用程序想要从路由头中检索地址的位置。`index` 参数的值必须在 0 与路由头中存在的段数减一之间。应使用上一节描述的 `inet6_rth_segments` 函数来确定路由头中的总段数。`inet6_rth_getaddr` 函数成功时返回指向 IPv6 地址的指针，出错时返回 `NULL`。

## 实例

RFC 3542 第 21 节附录 B 给出了大量示例。

KAME 也在其套件的 `advapitest` 目录中提供了示例。

## 诊断

`inet6_rth_space` 和 `inet6_rth_getaddr` 函数出错时返回 0。

`inet6_rthdr_init` 函数出错时返回 `NULL`。`inet6_rth_add` 和 `inet6_rth_reverse` 函数成功时返回 0，出错时返回 -1。

## 参见

> W. Stevens, M. Thomas, E. Nordmark, T. Jinmei, "Advanced Sockets API for IPv6", RFC 3542, May 2003.

> S. Deering, R. Hinden, "Internet Protocol, Version 6 (IPv6) Specification", RFC2460, December 1998.

## 历史

该实现首次出现于 KAME 高级网络套件。
