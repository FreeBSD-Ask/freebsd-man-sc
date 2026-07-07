# getnameinfo(3)

`getnameinfo` — 套接字地址结构转换为主机名和服务名

## 名称

`getnameinfo`

## 概要

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netdb.h>`

```c
int
getnameinfo(const struct sockaddr *sa, socklen_t salen, char *host,
    size_t hostlen, char *serv, size_t servlen, int flags);
```

## 描述

`getnameinfo` 函数用于将 `sockaddr` 结构转换为一对主机名和服务字符串。它是 gethostbyaddr(3) 和 getservbyport(3) 函数的替代品，并提供更大的灵活性，是 [getaddrinfo(3)](getaddrinfo.3.md) 函数的逆操作。

如果将链路层地址或 UNIX 域地址传递给 `getnameinfo`，其 ASCII 表示将存储在 `host` 中。如果 `serv` 非空，则其指向的字符串将设置为空字符串；`flags` 将始终被忽略。对于链路层地址，这可用作旧版 link_ntoa(3) 函数的替代。

`sockaddr` 结构 `sa` 应指向 `sockaddr_in`、`sockaddr_in6`、`sockaddr_dl` 或 `sockaddr_un` 结构（分别对应 IPv4、IPv6、链路层或 UNIX 域），长度为 `salen` 字节。如果 `salen` 短于指定地址族对应的长度或长于 `sizeof(struct sockaddr_storage)`，则返回 `EAI_FAMILY`。注意，`sa->sa_len` 应与 `salen` 一致，尽管 `sa->sa_len` 的值不直接在此函数中使用。

与 `sa` 关联的主机名和服务名存储在 `host` 和 `serv` 中，它们的长度参数分别为 `hostlen` 和 `servlen`。`hostlen` 的最大值为 `NI_MAXHOST`，`servlen` 的最大值为 `NI_MAXSERV`，由 <`netdb.h`> 定义。如果长度参数为零，则不会存储字符串。否则，必须提供足够的空间来存储主机名或服务字符串以及一个字节的 NUL 终止符。

`flags` 参数由以下值按位或组成：

**`NI_NOFQDN`** 本地主机不需要完全限定域名。返回完全限定域名的本地部分。

**`NI_NUMERICHOST`** 以数字形式返回地址，如同调用 inet_ntop(3)，而非主机名。

**`NI_NAMEREQD`** 需要名称。如果在 DNS 中找不到主机名且设置了此标志，则返回非零错误代码。如果未找到主机名且未设置此标志，则以数字形式返回地址。

**`NI_NUMERICSERV`** 服务名以表示端口号的数字字符串返回。

**`NI_NUMERICSCOPE`** 范围标识以数字字符串返回。

**`NI_DGRAM`** 指定要查找的服务是数据报服务，并使 getservbyport(3) 的第二个参数为“udp”而非默认的“tcp”。对于少数有不同 UDP 和 TCP 服务的端口（512-514）是必需的。

此实现允许带范围标识的数字 IPv6 地址表示法，如 RFC 4007 第 11 章所述。IPv6 链路本地地址将显示为类似“`fe80::1%ne0`”的字符串。更多信息参见 [getaddrinfo(3)](getaddrinfo.3.md)。

## 返回值

`getnameinfo` 成功时返回零，出错时返回 [gai_strerror(3)](gai_strerror.3.md) 中列出的错误代码之一。

## 实例

以下代码尝试获取给定套接字地址的数字主机名和服务名。注意，没有对特定地址族的硬编码引用。

```c
struct sockaddr *sa;	/* 输入 */
char hbuf[NI_MAXHOST], sbuf[NI_MAXSERV];
if (getnameinfo(sa, sa->sa_len, hbuf, sizeof(hbuf), sbuf,
    sizeof(sbuf), NI_NUMERICHOST | NI_NUMERICSERV)) {
	errx(1, "could not get numeric hostname");
	/* 不可到达 */
}
printf("host=%s, serv=%s\n", hbuf, sbuf);
```

以下版本检查套接字地址是否有反向地址映射：

```c
struct sockaddr *sa;	/* 输入 */
char hbuf[NI_MAXHOST];
if (getnameinfo(sa, sa->sa_len, hbuf, sizeof(hbuf), NULL, 0,
    NI_NAMEREQD)) {
	errx(1, "could not resolve hostname");
	/* 不可到达 */
}
printf("host=%s\n", hbuf);
```

## 参见

[gai_strerror(3)](gai_strerror.3.md), [getaddrinfo(3)](getaddrinfo.3.md), gethostbyaddr(3), getservbyport(3), inet_ntop(3), link_ntoa(3), [resolver(3)](resolver.3.md), [inet(4)](../man4/inet.4.md), [inet6(4)](../man4/inet6.4.md), [unix(4)](../man4/unix.4.md), [hosts(5)](../man5/hosts.5.md), resolv.conf(5), [services(5)](../man5/services.5.md), [hostname(7)](../man7/hostname.7.md)

> R. Gilligan, S. Thomson, J. Bound, J. McCann, W. Stevens, "Basic Socket Interface Extensions for IPv6", February 2003.

> S. Deering, B. Haberman, T. Jinmei, E. Nordmark, B. Zill, "IPv6 Scoped Address Architecture", March 2005.

> Craig Metz, "Protocol Independence Using the Sockets API", *Proceedings of the freenix track: 2000 USENIX annual technical conference*, June 2000.

## 标准

`getnameinfo` 函数由 IEEE Std 1003.1-2004（"POSIX.1"）规范定义，并记录在 RFC 3493“Basic Socket Interface Extensions for IPv6”中。

## 注意事项

`getnameinfo` 可以返回 `sa` 中指定地址的数字和 FQDN 两种形式。没有返回值指示 `host` 中返回的字符串是二进制到数字文本转换的结果（如 inet_ntop(3)），还是 DNS 反向查找的结果。因此，恶意方可以设置如下的 PTR 记录：

```c
1.0.0.127.in-addr.arpa. IN PTR  10.1.1.1
```

并欺骗 `getnameinfo` 的调用者相信 `sa` 是 `10.1.1.1`，而实际上它是 `127.0.0.1`。

为防止此类攻击，当 `getnameinfo` 的结果用于访问控制目的时，建议使用 `NI_NAMEREQD`：

```c
struct sockaddr *sa;
socklen_t salen;
char addr[NI_MAXHOST];
struct addrinfo hints, *res;
int error;
error = getnameinfo(sa, salen, addr, sizeof(addr),
    NULL, 0, NI_NAMEREQD);
if (error == 0) {
	memset(&hints, 0, sizeof(hints));
	hints.ai_socktype = SOCK_DGRAM;	/* 占位 */
	hints.ai_flags = AI_NUMERICHOST;
	if (getaddrinfo(addr, "0", &hints, &res) == 0) {
		/* 恶意 PTR 记录 */
		freeaddrinfo(res);
		printf("bogus PTR record\n");
		return -1;
	}
	/* addr 是 PTR 查找的 FQDN 结果 */
} else {
	/* addr 是数字字符串 */
	error = getnameinfo(sa, salen, addr, sizeof(addr),
	    NULL, 0, NI_NUMERICHOST);
}
```
