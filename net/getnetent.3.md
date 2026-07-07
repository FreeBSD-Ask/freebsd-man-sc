# getnetent(3)

`getnetent` — 获取网络条目

## 名称

`getnetent`, `getnetbyaddr`, `getnetbyname`, `setnetent`, `endnetent`

## 库

Lb libc

## 概要

`#include <netdb.h>`

`Ft struct netent * Fn getnetent void Ft struct netent * Fn getnetbyname const char *name Ft struct netent * Fn getnetbyaddr uint32_t net int type Ft void Fn setnetent int stayopen Ft void Fn endnetent void Ft int Fn getnetent_r struct netent *ne char *buffer size_t buflen struct netent **result int *h_errnop Ft int Fn getnetbyaddr_r uint32_t net int type struct netent *ne char *buffer size_t buflen struct netent **result int *h_errorp" Ft int Fn getnetbyname_r const char *name struct netent *ne char *buffer size_t buflen struct netent **result int *h_errorp`

## 描述

`getnetent`、`getnetbyname` 和 `getnetbyaddr` 函数各自返回一个指针，指向具有以下结构、描述互联网网络的对象。该结构包含的信息可能来自名字服务器、**/etc/networks** 数据库中某行的分解字段，或由 [yp(8)](../man8/yp.8.md) 系统提供的条目。查找顺序由 [nsswitch.conf(5)](../man5/nsswitch.conf.5.md) 中的 `networks` 条目控制。

```c
struct netent {
	char		*n_name;	/* 网络的官方名称 */
	char		**n_aliases;	/* 别名列表 */
	int		n_addrtype;	/* 网络号类型 */
	uint32_t	n_net;		/* 网络号 */
};
```

该结构的成员包括：

**`n_name`** 网络的官方名称。

**`n_aliases`** 以零结尾的网络别名列表。

**`n_addrtype`** 返回的网络号类型；目前仅为 AF_INET。

**`n_net`** 网络号。网络号以机器字节顺序返回。

`getnetent` 函数读取文件的下一行，必要时打开文件。

`setnetent` 函数打开并回卷文件。如果 `stayopen` 标志非零，则在每次调用 `getnetbyname` 或 `getnetbyaddr` 之后，网络数据库不会被关闭。

`endnetent` 函数关闭文件。

`getnetbyname` 和 `getnetbyaddr` 函数从文件开头顺序搜索，直至找到匹配的网络名或网络地址和类型，或遇到 `EOF`。`type` 参数必须为 `AF_INET`。网络号以主机顺序提供。

带 *_r* 后缀的函数提供其对应函数的可重入版本。调用者必须提供五个额外参数：一个在成功时填充的 `struct netent` 变量、一个大小为 `buflen` 字节的 `buffer`、一个在成功时指向结果或在失败或未找到名称时设为 `NULL` 的 `struct netent` `result` 变量。`h_errnop` 变量在出错时填充错误代码。所有这些函数成功时返回 0。

## 文件

**/etc/networks**
**/etc/nsswitch.conf**
**/etc/resolv.conf**

## 诊断

遇到 `EOF` 或出错时返回空指针。

## 参见

[networks(5)](../man5/networks.5.md)

RFC 1101

## 历史

`getnetent`、`getnetbyaddr`、`getnetbyname`、`setnetent` 和 `endnetent` 函数出现于 4.2BSD。

## 缺陷

这些函数使用的数据空间是线程特定的；如果后续需要使用该数据，应在这些函数的后续调用覆盖它之前将其复制。目前仅支持 Internet 网络号。期望网络号不超过 32 位可能过于天真。
