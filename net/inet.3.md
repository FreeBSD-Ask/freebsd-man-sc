# inet(3)

`inet_aton` — Internet 地址操作例程

## 名称

`inet_aton`, `inet_addr`, `inet_network`, `inet_ntoa`, `inet_ntoa_r`, `inet_ntop`, `inet_pton`, `inet_makeaddr`, `inet_lnaof`, `inet_netof`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <arpa/inet.h>`

```c
int
inet_aton(const char *cp, struct in_addr *pin);

in_addr_t
inet_addr(const char *cp);

in_addr_t
inet_network(const char *cp);

char *
inet_ntoa(struct in_addr in);

char *
inet_ntoa_r(struct in_addr in, char *buf, socklen_t size);

const char *
inet_ntop(int af, const void * restrict src, char * restrict dst,
    socklen_t size);

int
inet_pton(int af, const char * restrict src, void * restrict dst);

struct in_addr
inet_makeaddr(in_addr_t net, in_addr_t lna);

in_addr_t
inet_lnaof(struct in_addr in);

in_addr_t
inet_netof(struct in_addr in);
```

## 描述

`inet_aton`、`inet_addr` 和 `inet_network` 例程解释以 Internet 标准 `.` 表示法表示数字的字符串。

`inet_pton` 函数将呈现格式地址（即保存在字符串中的可打印形式）转换为网络格式（通常是 `struct in_addr` 或某种其他内部二进制表示，采用网络字节顺序）。如果地址对于指定的地址族有效，它返回 1；如果地址在指定地址族中无法解析，返回 0；如果发生某些系统错误，返回 -1（此时 `errno` 将被设置）。此函数目前对 `AF_INET` 和 `AF_INET6` 有效。

`inet_aton` 例程将指定字符串解释为 Internet 地址，将该地址放入所提供的结构中。如果字符串被成功解释，它返回 1；如果字符串无效，返回 0。`inet_addr` 和 `inet_network` 函数分别返回适合用作 Internet 地址和 Internet 网络号的数字。

`inet_ntop` 函数将地址 `*src` 从网络格式（通常是 `struct in_addr` 或某种其他二进制形式，采用网络字节顺序）转换为呈现格式（适合外部显示用途）。`size` 参数指定缓冲区 `*dst` 的大小（以字节为单位）。`INET_ADDRSTRLEN` 和 `INET6_ADDRSTRLEN` 定义了转换相应类型地址所需的最大大小。如果发生系统错误，它返回 `NULL`（此时 `errno` 将被设置），或者返回指向目标字符串的指针。此函数目前对 `AF_INET` 和 `AF_INET6` 有效。

`inet_ntoa` 例程接受一个 Internet 地址，返回以 `.` 表示法表示该地址的 ASCII 字符串。`inet_ntoa_r` 例程是 `inet_ntoa` 的可重入版本。已弃用的 `inet_makeaddr` 例程接受一个 Internet 网络号和该网络上的本地主机地址，并据此构造一个 Internet 地址。仅应假定它适用于历史上的 A/B/C 类网络。已弃用的 `inet_netof` 和 `inet_lnaof` 例程拆分 Internet 主机地址，分别返回网络号和本地主机地址部分，假定使用历史上的 A/B/C 类网络掩码。

所有 Internet 地址以网络顺序返回（字节从左到右排序）。所有网络号和本地地址部分以机器字节顺序整数值返回。

## Internet 地址（IP 版本 4）

`inet_aton` 和 `inet_addr` 函数接受使用 `.` 表示法以下列形式之一指定的 IPv4 值：

```sh
a.b.c.d
a.b.c
a.b
a
```

当指定四个部分时，每个部分被解释为一个字节的数据，从左到右分配给 Internet 地址的四个字节。

当指定三部分地址时，最后一部分被解释为 16 位量，放置在网络地址的两个最低有效字节中。

当提供两部分地址时，最后一部分被解释为 24 位量，放置在网络地址的三个最低有效字节中。

当仅给出一个部分时，该值直接存储在网络地址中，不进行任何字节重排。

以 `.` 表示法作为"部分"提供的所有数字可以是十进制、八进制或十六进制，如 C 语言所指定（即前导 0x 或 0X 表示十六进制；否则前导 0 表示八进制；否则该数字被解释为十进制）。

注意，`inet_pton` 不接受 1、2 或 3 部分的点分地址；必须指定全部四个部分，且仅解释为十进制值。这比 `inet_aton` 所接受的输入集合更窄。

## 诊断

对于格式错误的请求，`inet_addr` 和 `inet_network` 返回常量 `INADDR_NONE`。

## 错误

`inet_ntop` 调用在以下情况失败：

**[ENOSPC]** `size` 不足以存储地址的呈现形式。

**[EAFNOSUPPORT]** `*src` 不是 `AF_INET` 或 `AF_INET6` 族地址。

## 参见

[byteorder(3)](byteorder.3.md), [getaddrinfo(3)](getaddrinfo.3.md), [gethostbyname(3)](gethostbyname.3.md), [getnameinfo(3)](getnameinfo.3.md), [getnetent(3)](getnetent.3.md), [inet_net(3)](inet_net.3.md), [hosts(5)](../man5/hosts.5.md), [networks(5)](../man5/networks.5.md)

> "IP Version 6 Addressing Architecture", 2373, July 1998.

## 标准

`inet_ntop` 和 `inet_pton` 函数遵循 XNS 5.2。

## 历史

这些函数出现于 4.2BSD。

## 缺陷

值 `INADDR_NONE`（0xffffffff）是一个有效的广播地址，但 `inet_addr` 无法在不指示失败的情况下返回该值。较新的 `inet_aton` 函数不存在此问题。主机字节顺序与网络字节顺序的问题容易令人混淆。`inet_ntoa` 返回的字符串位于静态内存区中。

`inet_addr` 函数应返回一个 `struct in_addr`。
