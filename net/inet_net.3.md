# inet_net(3)

`inet_net_ntop` — Internet 网络号操作例程

## 名称

`inet_net_ntop`, `inet_net_pton`

## 库

libc

## 概要

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <arpa/inet.h>`

```c
char *
inet_net_ntop(int af, const void *src, int bits, char *dst, size_t size);

int
inet_net_pton(int af, const char *src, void *dst, size_t size);
```

## 描述

`inet_net_ntop` 函数将 Internet 网络号从网络格式（通常是 `struct in_addr` 或某种其他二进制形式，采用网络字节顺序）转换为 CIDR 呈现格式（适合外部显示用途）。`bits` 参数是 `src` 中作为网络号的位数。如果发生系统错误，它返回 `NULL`（此时 `errno` 将被设置），或者返回指向目标字符串的指针。

`inet_net_pton` 函数将呈现格式的 Internet 网络号（即保存在字符串中的可打印形式）转换为网络格式（通常是 `struct in_addr` 或某种其他内部二进制表示，采用网络字节顺序）。它返回位数（基于类别计算，或用 /CIDR 指定），或 -1 表示失败（此时 `errno` 将被设置。如果 Internet 网络号无效，它将被设置为 `ENOENT`）。

`af` 当前支持的值为 `AF_INET` 和 `AF_INET6`。`size` 参数是结果缓冲区 `dst` 的大小。

## 网络号（IP 版本 4）

Internet 网络号可以以下列形式之一指定：

```sh
a.b.c.d/bits
a.b.c.d
a.b.c
a.b
a
```

当指定四个部分时，每个部分被解释为一个字节的数据，从左到右分配给 Internet 网络号的四个字节。注意，当 Internet 网络号在使用小端字节顺序的系统（如 Intel 386、486 和 Pentium 处理器）上被视为 32 位整数量时，上述字节显示为 "`d.c.b.a`"。即小端字节从右到左排序。

当指定三部分数字时，最后一部分被解释为 16 位量，放置在 Internet 网络号的两个最低有效字节中。

当提供两部分数字时，最后一部分被解释为 24 位量，放置在 Internet 网络号的三个最低有效字节中。

当仅给出一个部分时，该值直接存储在 Internet 网络号中，不进行任何字节重排。

以 `.` 表示法作为"部分"提供的所有数字可以是十进制、八进制或十六进制，如 C 语言所指定（即前导 0x 或 0X 表示十六进制；否则前导 0 表示八进制；否则该数字被解释为十进制）。

## 参见

[byteorder(3)](byteorder.3.md), [inet(3)](inet.3.md), [networks(5)](../man5/networks.5.md)

## 历史

`inet_net_ntop` 和 `inet_net_pton` 函数出现于 BIND 4.9.4。
