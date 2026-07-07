# getaddrinfo(3)

`getaddrinfo` — 套接字地址结构与主机和服务名的转换

## 名称

`getaddrinfo`, `freeaddrinfo`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netdb.h>`

```c
int
getaddrinfo(const char *hostname, const char *servname,
    const struct addrinfo *hints, struct addrinfo **res);

void
freeaddrinfo(struct addrinfo *ai);
```

## 描述

`getaddrinfo` 函数用于获取主机 `hostname` 和服务 `servname` 的地址和端口号列表。它是 [gethostbyname(3)](gethostbyname.3.md) 和 getservbyname(3) 函数的替代品，并提供更大的灵活性。

`hostname` 和 `servname` 参数要么是指向以 NUL 结尾的字符串的指针，要么是空指针。`hostname` 的可接受值可以是有效的主机名或由点分十进制 IPv4 地址、IPv6 地址或 UNIX 域地址组成的数字主机地址字符串。`servname` 可以是十进制端口号或 [services(5)](../man5/services.5.md) 中列出的服务名。`hostname` 和 `servname` 中至少有一个必须非空。

`hints` 是一个可选指针，指向 `struct addrinfo`，由 <`netdb.h`> 定义：

```c
struct addrinfo {
        int     ai_flags;       /* AI_PASSIVE, AI_CANONNAME, .. */
        int     ai_family;      /* AF_xxx */
        int     ai_socktype;    /* SOCK_xxx */
        int     ai_protocol;    /* 0 或 IPv4 和 IPv6 的 IPPROTO_xxx */
        socklen_t ai_addrlen;   /* ai_addr 的长度 */
        char    *ai_canonname;  /* 主机的规范名称 */
        struct  sockaddr *ai_addr;      /* 二进制地址 */
        struct  addrinfo *ai_next;      /* 链表中的下一个结构 */
};
```

此结构可用于提供有关调用者支持或希望使用的套接字类型的提示。调用者可以在 `hints` 中提供以下结构元素：

**`AI_ADDRCONFIG`** 如果设置了 `AI_ADDRCONFIG` 位，则仅当本地系统上配置了 IPv4 地址时才返回 IPv4 地址，仅当本地系统上配置了 IPv6 地址时才返回 IPv6 地址。

**`AI_ALL`** 如果 `AI_ALL` 标志与 `AI_V4MAPPED` 标志一起使用，则 `getaddrinfo` 将返回所有匹配的 IPv6 和 IPv4 地址。例如，使用 DNS 时，将同时查询 AAAA 记录和 A 记录，`getaddrinfo` 返回两个查询的组合结果。找到的任何 IPv4 地址将作为 IPv4 映射的 IPv6 地址返回。不带 `AI_V4MAPPED` 标志的 `AI_ALL` 标志将被忽略。

**`AI_CANONNAME`** 如果设置了 `AI_CANONNAME` 位，则对 `getaddrinfo` 的成功调用将在返回的第一个 `addrinfo` 结构的 `ai_canonname` 元素中返回包含指定主机名规范名称的以 NUL 结尾的字符串。

**`AI_NUMERICHOST`** 如果设置了 `AI_NUMERICHOST` 位，则表示 `hostname` 应被视为定义 IPv4 或 IPv6 地址的数字字符串，不应尝试名称解析。

**`AI_NUMERICSERV`** 如果设置了 `AI_NUMERICSERV` 位，则提供的非空 `servname` 字符串应为数字端口字符串。否则，将返回 `EAI_NONAME` 错误。此位将阻止调用任何类型的名称解析服务（例如 NIS+）。

**`AI_PASSIVE`** 如果设置了 `AI_PASSIVE` 位，则表示返回的套接字地址结构旨在用于 [bind(2)](../sys/bind.2.md) 调用。在这种情况下，如果 `hostname` 参数是空指针，则套接字地址结构的 IP 地址部分对于 IPv4 地址将设置为 `INADDR_ANY`，对于 IPv6 地址将设置为 `IN6ADDR_ANY_INIT`。如果未设置 `AI_PASSIVE` 位，则返回的套接字地址结构将准备好用于面向连接协议的 [connect(2)](../sys/connect.2.md) 调用，或如果选择了无连接协议则用于 [connect(2)](../sys/connect.2.md)、sendto(2) 或 sendmsg(2)。如果 `hostname` 是空指针且未设置 `AI_PASSIVE`，则套接字地址结构的 IP 地址部分将设置为回环地址。

**`AI_V4MAPPED`** 如果指定了 `AI_V4MAPPED` 标志且 ai_family 为 `AF_INET6`，则 `getaddrinfo` 在找不到匹配的 IPv6 地址时将返回 IPv4 映射的 IPv6 地址（`ai_addrlen` 将为 16）。例如，使用 DNS 时，如果未找到 AAAA 记录，则查询 A 记录，找到的任何记录将作为 IPv4 映射的 IPv6 地址返回。除非 `ai_family` 等于 `AF_INET6`，否则 `AI_V4MAPPED` 标志将被忽略。

**`ai_family`** 应使用的地址族。当 `ai_family` 设置为 `AF_UNSPEC` 时，表示调用者将接受操作系统支持的任何地址族。

**`ai_socktype`** 表示所需的套接字类型：`SOCK_STREAM`、`SOCK_DGRAM`、`SOCK_SEQPACKET` 或 `SOCK_RAW`。当 `ai_socktype` 为零时，调用者将接受任何套接字类型。

**`ai_protocol`** 表示所需的传输协议：`IPPROTO_UDP`、`IPPROTO_TCP`、`IPPROTO_SCTP` 或 `IPPROTO_UDPLITE`。如果 `ai_protocol` 为零，调用者将接受任何协议。

**`ai_flags`** `hints` 参数指向的 `ai_flags` 字段应设置为零，或为 `AI_ADDRCONFIG`、`AI_ALL`、`AI_CANONNAME`、`AI_NUMERICHOST`、`AI_NUMERICSERV`、`AI_PASSIVE` 和 `AI_V4MAPPED` 中一个或多个值的按位或。对于 UNIX 域地址，`ai_flags` 被忽略。

通过 `hints` 传递的 `addrinfo` 结构的所有其他元素必须为零或空指针。

如果 `hints` 是空指针，`getaddrinfo` 的行为如同调用者提供了一个 `struct addrinfo`，其中 `ai_family` 设置为 `AF_UNSPEC`，所有其他元素设置为零或 `NULL`。

成功调用 `getaddrinfo` 后，`*res` 是指向一个或多个 `addrinfo` 结构链表的指针。可以通过跟随每个 `addrinfo` 结构中的 `ai_next` 指针遍历列表，直到遇到空指针。每个返回的 `addrinfo` 结构包含三个适合 [socket(2)](../sys/socket.2.md) 调用的成员：`ai_family`、`ai_socktype` 和 `ai_protocol`。对于列表中的每个 `addrinfo` 结构，`ai_addr` 成员指向一个长度为 `ai_addrlen` 的已填充套接字地址结构。

此 `getaddrinfo` 实现允许带范围标识的数字 IPv6 地址表示法，如 RFC 4007 第 11 章所述。通过在地址后附加百分号和范围标识，可以填充地址的 `sin6_scope_id` 字段。这使得范围地址的管理更加容易，并允许范围地址的剪切和粘贴输入。

目前代码仅支持使用此格式的链路本地地址。范围标识被硬编码为与链路关联的硬件接口的名称（如 `ne0`）。例如“`fe80::1%ne0`”，表示“与 `ne0` 接口关联的链路上的 `fe80::1`”。

当前实现假设接口与链路之间存在一对一关系，但规范中并不一定如此。

`getaddrinfo` 返回的所有信息都是动态分配的：`addrinfo` 结构本身以及 `addrinfo` 结构中包含的套接字地址结构和规范主机名字符串。

成功调用 `getaddrinfo` 创建的动态分配结构的内存由 `freeaddrinfo` 函数释放。`ai` 指针应为通过调用 `getaddrinfo` 创建的 `addrinfo` 结构。

## 实现注释

`freeaddrinfo(NULL)` 的行为在 -susv4 和 `RFC 3493` 中均未指定。当前实现忽略 `NULL` 参数，以兼容依赖其他操作系统实现细节的程序。

## 返回值

`getaddrinfo` 成功时返回零，出错时返回 [gai_strerror(3)](gai_strerror.3.md) 中列出的错误代码之一。

## 实例

以下代码尝试通过流式套接字连接到“`www.kame.net`”的“`http`”服务。它遍历所有可用的地址，而不考虑地址族。如果目标解析为 IPv4 地址，将使用 `AF_INET` 套接字。类似地，如果解析为 IPv6，将使用 `AF_INET6` 套接字。注意，没有对特定地址族的硬编码引用。即使 `getaddrinfo` 返回非 IPv4/v6 的地址，代码也能工作。

```c
struct addrinfo hints, *res, *res0;
int error;
int s;
const char *cause = NULL;
memset(&hints, 0, sizeof(hints));
hints.ai_family = AF_UNSPEC;
hints.ai_socktype = SOCK_STREAM;
error = getaddrinfo("www.kame.net", "http", &hints, &res0);
if (error) {
	errx(1, "%s", gai_strerror(error));
	/* 不可到达 */
}
s = -1;
for (res = res0; res; res = res->ai_next) {
	s = socket(res->ai_family, res->ai_socktype,
	    res->ai_protocol);
	if (s < 0) {
		cause = "socket";
		continue;
	}
	if (connect(s, res->ai_addr, res->ai_addrlen) < 0) {
		cause = "connect";
		close(s);
		s = -1;
		continue;
	}
	break;	/* 成功获取一个 */
}
if (s < 0) {
	err(1, "%s", cause);
	/* 不可到达 */
}
freeaddrinfo(res0);
```

以下示例尝试为所有可用的地址族打开通配监听套接字，用于“`http`”服务。

```c
struct addrinfo hints, *res, *res0;
int error;
int s[MAXSOCK];
int nsock;
const char *cause = NULL;
memset(&hints, 0, sizeof(hints));
hints.ai_family = AF_UNSPEC;
hints.ai_socktype = SOCK_STREAM;
hints.ai_flags = AI_PASSIVE;
error = getaddrinfo(NULL, "http", &hints, &res0);
if (error) {
	errx(1, "%s", gai_strerror(error));
	/* 不可到达 */
}
nsock = 0;
for (res = res0; res && nsock < MAXSOCK; res = res->ai_next) {
	s[nsock] = socket(res->ai_family, res->ai_socktype,
	    res->ai_protocol);
	if (s[nsock] < 0) {
		cause = "socket";
		continue;
	}
	if (bind(s[nsock], res->ai_addr, res->ai_addrlen) < 0) {
		cause = "bind";
		close(s[nsock]);
		continue;
	}
	(void) listen(s[nsock], 5);
	nsock++;
}
if (nsock == 0) {
	err(1, "%s", cause);
	/* 不可到达 */
}
freeaddrinfo(res0);
```

## 参见

[bind(2)](../sys/bind.2.md), [connect(2)](../sys/connect.2.md), [send(2)](../sys/send.2.md), [socket(2)](../sys/socket.2.md), [gai_strerror(3)](gai_strerror.3.md), [gethostbyname(3)](gethostbyname.3.md), [getnameinfo(3)](getnameinfo.3.md), getservbyname(3), [resolver(3)](resolver.3.md), [inet(4)](../man4/inet.4.md), [inet6(4)](../man4/inet6.4.md), [unix(4)](../man4/unix.4.md), [hosts(5)](../man5/hosts.5.md), resolv.conf(5), [services(5)](../man5/services.5.md), [hostname(7)](../man7/hostname.7.md), ip6addrctl(8)

> R. Gilligan, S. Thomson, J. Bound, J. McCann, W. Stevens, "Basic Socket Interface Extensions for IPv6", February 2003.

> S. Deering, B. Haberman, T. Jinmei, E. Nordmark, B. Zill, "IPv6 Scoped Address Architecture", March 2005.

> Craig Metz, "Protocol Independence Using the Sockets API", *Proceedings of the freenix track: 2000 USENIX annual technical conference*, June 2000.

## 标准

`getaddrinfo` 函数由 IEEE Std 1003.1-2004（"POSIX.1"）规范定义，并记录在 `RFC 3493`“Basic Socket Interface Extensions for IPv6”中。
