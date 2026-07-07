# getprotoent(3)

`getprotoent` — 获取协议条目

## 名称

`getprotoent`, `getprotobynumber`, `getprotobyname`, `setprotoent`, `endprotoent`

## 库

Lb libc

## 概要

`#include <netdb.h>`

`Ft struct protoent * Fn getprotoent void Ft struct protoent * Fn getprotobyname const char *name Ft struct protoent * Fn getprotobynumber int proto Ft void Fn setprotoent int stayopen Ft void Fn endprotoent void`

## 描述

`getprotoent`、`getprotobyname` 和 `getprotobynumber` 函数各自返回一个指针，指向具有以下结构的对象，该结构包含网络协议数据库 **/etc/protocols** 中某行的分解字段。

```c
struct protoent {
	char	*p_name;	/* 协议的官方名称 */
	char	**p_aliases;	/* 别名列表 */
	int	p_proto;	/* 协议号 */
};
```

该结构的成员包括：

**`p_name`** 协议的官方名称。

**`p_aliases`** 以零结尾的协议别名列表。

**`p_proto`** 协议号。

`getprotoent` 函数读取文件的下一行，必要时打开文件。

`setprotoent` 函数打开并回卷文件。如果 `stayopen` 标志非零，则在每次调用 `getprotobyname` 或 `getprotobynumber` 之后，网络数据库不会被关闭。

`endprotoent` 函数关闭文件。

`getprotobyname` 和 `getprotobynumber` 函数从文件开头顺序搜索，直至找到匹配的协议名或协议号，或遇到 `EOF`。

## 返回值

遇到 `EOF` 或出错时返回空指针。

## 文件

**/etc/protocols**

## 参见

[protocols(5)](../man5/protocols.5.md)

## 历史

`getprotoent`、`getprotobynumber`、`getprotobyname`、`setprotoent` 和 `endprotoent` 函数出现于 4.2BSD。

## 缺陷

这些函数使用线程特定的数据空间；如果后续需要使用该数据，应在后续调用覆盖它之前将其复制。目前仅支持 Internet 协议。
