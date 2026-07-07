# getipnodebyname(3)

`getipnodebyname` — 节点名到地址以及地址到节点名的转换

## 名称

`getipnodebyname`, `getipnodebyaddr`, `freehostent`

## 库

libc

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netdb.h>`

```c
struct hostent *
getipnodebyname(const char *name, int af, int flags, int *error_num);

struct hostent *
getipnodebyaddr(const void *src, size_t len, int af, int *error_num);

void
freehostent(struct hostent *ptr);
```

## 描述

`getipnodebyname` 和 `getipnodebyaddr` 函数与 [gethostbyname(3)](gethostbyname.3.md)、gethostbyname2(3) 和 gethostbyaddr(3) 非常相似。这些函数涵盖了旧函数提供的所有功能，并为程序员提供了更好的接口。这些函数需要额外的参数 `af` 和 `flags`，用于指定地址族和操作模式。这些额外参数允许程序员获取特定地址族（如 `AF_INET` 或 `AF_INET6`）的节点名地址。这些函数还需要一个额外的指针参数 `error_num` 来返回适当的错误代码，以支持线程安全的错误代码返回。

返回值的类型和用法 `struct hostent` 在 [gethostbyname(3)](gethostbyname.3.md) 中描述。

对于 `getipnodebyname`，`name` 参数可以是节点名或数字地址字符串（即点分十进制 IPv4 地址或 IPv6 十六进制地址）。`af` 参数指定地址族，为 `AF_INET` 或 `AF_INET6`。`flags` 参数指定要搜索的地址类型和返回的地址类型。我们注意到，特殊的 flags 值 `AI_DEFAULT`（定义见下文）应能满足大多数应用程序的需求。也就是说，将简单应用程序移植为使用 IPv6 只需将调用

```c
hptr = gethostbyname(name);
```

替换为

```c
hptr = getipnodebyname(name, AF_INET6, AI_DEFAULT, &error_num);
```

希望对搜索和返回的地址类型进行更精细控制的应用程序，可以指定 `flags` 参数的其他组合。

`flags` 为 `0` 时表示严格解释 `af` 参数：

- 如果 `flags` 为 0 且 `af` 为 `AF_INET`，则调用者只需要 IPv4 地址。将查询 `A` 记录。如果成功，返回 IPv4 地址且 `hostent` 结构的 `h_length` 成员为 4，否则函数返回 `NULL` 指针。
- 如果 `flags` 为 0 且 `af` 为 `AF_INET6`，则调用者只需要 IPv6 地址。将查询 `AAAA` 记录。如果成功，返回 IPv6 地址且 `hostent` 结构的 `h_length` 成员为 16，否则函数返回 `NULL` 指针。

其他常量可以逻辑或到 `flags` 参数中，以修改函数的行为。

- 如果指定了 `AI_V4MAPPED` 标志且 `af` 为 `AF_INET6`，则调用者将接受 IPv4 映射的 IPv6 地址。也就是说，如果未找到 `AAAA` 记录，则查询 `A` 记录，找到的记录作为 IPv4 映射的 IPv6 地址返回（`h_length` 为 16）。除非 `af` 等于 `AF_INET6`，否则忽略 `AI_V4MAPPED` 标志。
- `AI_V4MAPPED_CFG` 标志仅在内核支持 IPv4 映射 IPv6 地址时与 `AI_V4MAPPED` 标志完全相同。
- `AI_ALL` 标志与 `AI_V4MAPPED` 标志配合使用，且仅用于 IPv6 地址族。当 `AI_ALL` 与 `AI_V4MAPPED` 标志逻辑或时，调用者想要所有地址：IPv6 和 IPv4 映射的 IPv6。首先查询 `AAAA` 记录，如果成功则返回 IPv6 地址。然后查询 `A` 记录，找到的记录作为 IPv4 映射的 IPv6 地址返回。`h_length` 将为 16。只有当两次查询都失败时，函数才返回 `NULL` 指针。除非 af 等于 AF_INET6，否则忽略此标志。如果同时指定了 `AI_ALL` 和 `AI_V4MAPPED`，`AI_ALL` 优先。
- `AI_ADDRCONFIG` 标志指定仅当节点配置了至少一个 IPv6 源地址时才查询 `AAAA` 记录，仅当节点配置了至少一个 IPv4 源地址时才查询 `A` 记录。例如，如果节点未配置 IPv6 源地址，且 `af` 等于 AF_INET6，且所查找的节点名同时具有 `AAAA` 和 `A` 记录，则：(a) 如果仅指定了 `AI_ADDRCONFIG`，函数返回 `NULL` 指针；(b) 如果指定了 `AI_ADDRCONFIG` | `AI_V4MAPPED`，则 `A` 记录作为 IPv4 映射的 IPv6 地址返回；

特殊的 flags 值 `AI_DEFAULT` 定义为

```c
#define  AI_DEFAULT  (AI_V4MAPPED_CFG | AI_ADDRCONFIG)
```

我们注意到 `getipnodebyname` 函数必须允许 `name` 参数为节点名或字面地址字符串（即点分十进制 IPv4 地址或 IPv6 十六进制地址）。这使应用程序无需调用 inet_pton(3) 来处理字面地址字符串。当 `name` 参数为字面地址字符串时，`flags` 参数始终被忽略。

根据字面地址字符串的类型和 `af` 参数的值，有四种情况。两种简单情况是：`name` 为点分十进制 IPv4 地址且 `af` 等于 `AF_INET`，或 `name` 为 IPv6 十六进制地址且 `af` 等于 `AF_INET6`。返回的 hostent 结构的成员为：`h_name` 指向 `name` 参数的副本，`h_aliases` 为 `NULL` 指针，`h_addrtype` 为 `af` 参数的副本，`h_length` 为 4（对于 `AF_INET`）或 16（对于 `AF_INET6`），`h_addr_list[0]` 是指向 4 字节或 16 字节二进制地址的指针，`h_addr_list[1]` 为 `NULL` 指针。

当 `name` 为点分十进制 IPv4 地址且 `af` 等于 `AF_INET6`，并指定了 `AI_V4MAPPED` 时，返回 IPv4 映射的 IPv6 地址：`h_name` 指向包含该 IPv4 映射 IPv6 地址的 IPv6 十六进制地址，`h_aliases` 为 `NULL` 指针，`h_addrtype` 为 `AF_INET6`，`h_length` 为 16，`h_addr_list[0]` 是指向 16 字节二进制地址的指针，`h_addr_list[1]` 为 `NULL` 指针。

当 `name` 为 IPv6 十六进制地址且 `af` 等于 `AF_INET` 时为错误。函数的返回值为 `NULL` 指针，`error_num` 所指向的值等于 `HOST_NOT_FOUND`。

`getipnodebyaddr` 函数的参数与 gethostbyaddr(3) 几乎相同，但增加了一个用于返回错误号的指针。此外，它还能处理 IPv4 映射的 IPv6 地址和 IPv4 兼容的 IPv6 地址。

`getipnodebyname` 和 `getipnodebyaddr` 函数动态分配返回给调用者的结构。`freehostent` 函数回收由 `getipnodebyname` 或 `getipnodebyaddr` 分配并返回的内存区域。

## 文件

**/etc/hosts**
**/etc/nsswitch.conf**
**/etc/resolv.conf**

## 诊断

`getipnodebyname` 和 `getipnodebyaddr` 函数出错时返回 `NULL`。然后可检查 `error_num` 所指向的整数值，以确定这是临时故障还是无效或未知的主机。每个错误代码的含义在 [gethostbyname(3)](gethostbyname.3.md) 中描述。

## 参见

[getaddrinfo(3)](getaddrinfo.3.md), gethostbyaddr(3), [gethostbyname(3)](gethostbyname.3.md), [getnameinfo(3)](getnameinfo.3.md), [hosts(5)](../man5/hosts.5.md), [nsswitch.conf(5)](../man5/nsswitch.conf.5.md), [services(5)](../man5/services.5.md), [hostname(7)](../man7/hostname.7.md)

> R. Gilligan, S. Thomson, J. Bound, W. Stevens, "Basic Socket Interface Extensions for IPv6", March 1999.

## 标准

`getipnodebyname` 和 `getipnodebyaddr` 函数记录于 "Basic Socket Interface Extensions for IPv6"（RFC2553）。

## 历史

该实现首次出现于 KAME 高级网络套件。

## 缺陷

`getipnodebyname` 和 `getipnodebyaddr` 函数不能正确处理作用域 IPv6 地址。如果使用这些函数，你的程序将无法处理作用域 IPv6 地址。对于 IPv6 地址操作，推荐使用 [getaddrinfo(3)](getaddrinfo.3.md) 和 [getnameinfo(3)](getnameinfo.3.md)。
