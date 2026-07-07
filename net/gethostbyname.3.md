# gethostbyname(3)

`gethostbyname` — 获取网络主机条目

## 名称

`gethostbyname`, `gethostbyname2`, `gethostbyaddr`, `gethostent`, `sethostent`, `endhostent`, `herror`, `hstrerror`, `gethostbyname_r`, `gethostbyname2_r`, `gethostbyaddr_r`

## 库

Lb libc

## 概要

`#include <netdb.h>`

`int h_errno; Ft struct hostent * Fn gethostbyname const char *name Ft struct hostent * Fn gethostbyname2 const char *name int af Ft struct hostent * Fn gethostbyaddr const void *addr socklen_t len int af Ft struct hostent * Fn gethostent void Ft void Fn sethostent int stayopen Ft void Fn endhostent void Ft void Fn herror const char *string Ft const char * Fn hstrerror int err Ft int Fn gethostbyname_r const char *name struct hostent *he char *buffer size_t buflen struct hostent **result int *h_errnop Ft int Fn gethostbyname2_r const char *name int af struct hostent *he char *buffer size_t buflen struct hostent **result int *h_errnop Ft int Fn gethostbyaddr_r const void *addr socklen_t len int af struct hostent *hp char *buf size_t buflen struct hostent **result int *h_errno p`

## 描述

推荐使用 [getaddrinfo(3)](getaddrinfo.3.md) 和 [getnameinfo(3)](getnameinfo.3.md) 函数，而不是 `gethostbyname`、`gethostbyname2` 和 `gethostbyaddr` 函数。

`gethostbyname`、`gethostbyname2` 和 `gethostbyaddr` 函数各自返回一个指针，指向具有以下结构、描述按名称或地址引用的互联网主机的对象。

传递给 `gethostbyname` 或 `gethostbyname2` 的 `name` 参数应指向以 `NUL` 结尾的主机名。传递给 `gethostbyaddr` 的 `addr` 参数应指向长度为 `len` 字节、二进制形式（即非人类可读 ASCII 形式的 IP 地址）的地址。`af` 参数指定该地址的地址族（例如 `AF_INET`、`AF_INET6` 等）。

返回的结构包含的信息可能来自名字服务器、**/etc/hosts** 中某行的分解字段，或由 [yp(8)](../man8/yp.8.md) 系统提供的数据库条目。查找顺序由 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 中的 `hosts` 条目控制。

```c
struct	hostent {
	char	*h_name;	/* 主机的官方名称 */
	char	**h_aliases;	/* 别名列表 */
	int	h_addrtype;	/* 主机地址类型 */
	int	h_length;	/* 地址长度 */
	char	**h_addr_list;	/* 来自名字服务器的地址列表 */
};
#define	h_addr  h_addr_list[0]	/* 地址，用于向后兼容 */
```

该结构的成员包括：

**`h_name`** 主机的官方名称。

**`h_aliases`** 以 `NULL` 结尾的主机别名数组。

**`h_addrtype`** 返回的地址类型；通常为 `AF_INET`。

**`h_length`** 地址的字节长度。

**`h_addr_list`** 以 `NULL` 结尾的主机网络地址数组。主机地址以网络字节顺序返回。

**`h_addr`** `h_addr_list` 中的第一个地址；用于向后兼容。

使用名字服务器时，`gethostbyname` 和 `gethostbyname2` 将在当前域及其父域中搜索命名主机，除非名称以点结尾。如果名称不包含点，且环境变量 `HOSTALIASES` 包含别名文件的名称，将首先在别名文件中搜索与输入名称匹配的别名。关于域搜索过程和别名文件格式，参见 [hostname(7)](../man7/hostname.7.md)。

`gethostbyname2` 函数是 `gethostbyname` 的演进版本，旨在允许在 `AF_INET` 以外的地址族（例如 `AF_INET6`）中进行查找。

`sethostent` 函数可用于请求使用已连接的 TCP 套接字进行查询。查询默认使用 UDP 数据报。如果 `stayopen` 标志非零，将使用与名字服务器的 TCP 连接。该连接在 `gethostbyname`、`gethostbyname2` 或 `gethostbyaddr` 调用完成后仍保持打开。

`endhostent` 函数关闭 TCP 连接。

`herror` 函数向诊断输出写入消息，由字符串参数 `string`、常量字符串 ": " 和与 `h_errno` 值对应的消息组成。

`hstrerror` 函数返回一个字符串，即与 `err` 参数值对应的消息文本。

带 *_r* 后缀的函数提供其对应函数的可重入版本。调用者必须提供五个额外参数：一个在成功时填充的 `struct hostent` 变量、一个大小为 `buflen` 字节的 `buffer`、一个在成功时指向结果或在失败或未找到名称时设为 `NULL` 的 `struct hostent` `result` 变量。`h_errnop` 变量在出错时填充错误代码。所有这些函数成功时返回 0。

## 文件

**/etc/hosts**
**/etc/nsswitch.conf**
**/etc/resolv.conf**

## 实例

打印与特定 IP 地址关联的主机名：

```c
const char *ipstr = "127.0.0.1";
struct in_addr ip;
struct hostent *hp;
if (!inet_aton(ipstr, &ip))
	errx(1, "can't parse IP address %s", ipstr);
if ((hp = gethostbyaddr((const void *)&ip,
    sizeof ip, AF_INET)) == NULL)
	errx(1, "no name associated with %s", ipstr);
printf("name associated with %s is %s\n", ipstr, hp->h_name);
```

## 诊断

`gethostbyname`、`gethostbyname2` 和 `gethostbyaddr` 的错误返回状态通过返回 `NULL` 指针指示。然后可检查整数 `h_errno` 以查看这是临时故障还是无效或未知的主机。可使用 `herror` 例程打印描述故障的错误消息。如果其参数 `string` 非 `NULL`，将先打印该参数，后跟冒号和空格。错误消息以换行符结尾打印。

变量 `h_errno` 可能有以下值：

**`HOST_NOT_FOUND`** 未知此类主机。

**`TRY_AGAIN`** 这通常是临时错误，意味着本地服务器未收到来自权威服务器的响应。稍后重试可能会成功。

**`NO_RECOVERY`** 遇到某些意外的服务器故障。这是不可恢复的错误。

**`NO_DATA`** 请求的名称有效但没有 IP 地址；这不是临时错误。这意味着名字服务器知道该名称，但没有与该名称关联的地址。使用该域名的另一类对名字服务器的请求将获得应答；例如，可能为该域注册了邮件转发器。

## 参见

[getaddrinfo(3)](getaddrinfo.3.md), [getnameinfo(3)](getnameinfo.3.md), inet_aton(3), [resolver(3)](resolver.3.md), [hosts(5)](../man5/hosts.5.md), [hostname(7)](../man7/hostname.7.md)

## 历史

`herror` 函数出现于 4.3BSD。`endhostent`、`gethostbyaddr`、`gethostbyname`、`gethostent` 和 `sethostent` 函数出现于 4.2BSD。`gethostbyname2` 函数首次出现于 BIND 版本 4.9.4。`gethostbyname_r` 函数首次出现于 FreeBSD 6.2。

## 注意事项

当 Lb libc 构建为仅使用 **/etc/hosts** 中的查找例程而不使用名字服务器时，`gethostent` 函数被定义，`sethostent` 和 `endhostent` 被重定义。

`gethostent` 函数读取 **/etc/hosts** 的下一行，必要时打开文件。

`sethostent` 函数打开和/或回卷 **/etc/hosts** 文件。如果 `stayopen` 参数非零，在每次调用 `gethostbyname`、`gethostbyname2` 或 `gethostbyaddr` 之后，文件不会被关闭。

`endhostent` 函数关闭文件。

## 缺陷

这些函数使用线程特定的数据存储；如果后续需要使用该数据，应在后续调用覆盖它之前将其复制。

尽管这些函数是线程安全的，仍建议使用 [getaddrinfo(3)](getaddrinfo.3.md) 函数族。

目前仅支持 Internet 地址格式。
