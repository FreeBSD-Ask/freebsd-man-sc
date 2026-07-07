# getservent(3)

`getservent` — 获取服务条目

## 名称

`getservent`, `getservbyport`, `getservbyname`, `setservent`, `endservent`

## 库

Lb libc

## 概要

`#include <netdb.h>`

`Ft struct servent * Fn getservent Ft struct servent * Fn getservbyname const char *name const char *proto Ft struct servent * Fn getservbyport int port const char *proto Ft void Fn setservent int stayopen Ft void Fn endservent void`

## 描述

`getservent`、`getservbyname` 和 `getservbyport` 函数各自返回一个指针，指向具有以下结构的对象，该结构包含网络服务数据库 **/etc/services** 中某行的分解字段。

```c
struct servent {
	char	*s_name;	/* 服务的官方名称 */
	char	**s_aliases;	/* 别名列表 */
	int	s_port;		/* 服务所在的端口 */
	char	*s_proto;	/* 使用的协议 */
};
```

该结构的成员包括：

**`s_name`** 服务的官方名称。

**`s_aliases`** 以零结尾的服务别名列表。

**`s_port`** 服务所在的端口号。端口号以网络字节顺序返回。

**`s_proto`** 联系该服务时使用的协议名称。

`getservent` 函数读取文件的下一行，必要时打开文件。

`setservent` 函数打开并回卷文件。如果 `stayopen` 标志非零，则在每次调用 `getservbyname` 或 `getservbyport` 之后，网络数据库不会被关闭。

`endservent` 函数关闭文件。

`getservbyname` 和 `getservbyport` 函数从文件开头顺序搜索，直至找到匹配的协议名或端口号（必须以网络字节顺序指定），或遇到 `EOF`。如果同时提供了协议名（非 `NULL`），搜索还必须匹配该协议。

## 文件

**/etc/services**
**/var/db/services.db**

## 诊断

遇到 `EOF` 或出错时返回空指针。

## 参见

[getprotoent(3)](getprotoent.3.md), [services(5)](../man5/services.5.md), services_mkdb(8)

## 历史

`getservent`、`getservbyport`、`getservbyname`、`setservent` 和 `endservent` 函数出现于 4.2BSD。

## 缺陷

这些函数使用线程特定的数据存储；如果后续需要使用该数据，应在后续调用覆盖它之前将其复制。期望端口号适合 32 位量可能过于天真。
