# getrpcent(3)

`getrpcent` — 获取 RPC 条目

## 名称

`getrpcent`, `getrpcbyname`, `getrpcbynumber`, `endrpcent`, `setrpcent`

## 库

Lb libc

## 概要

`#include <rpc/rpc.h>`

```c
struct rpcent *
getrpcent(void);

struct rpcent *
getrpcbyname(const char *name);

struct rpcent *
getrpcbynumber(int number);

void
setrpcent(int stayopen);

void
endrpcent(void);
```

## 描述

`getrpcent`、`getrpcbyname` 和 `getrpcbynumber` 函数各自返回一个指向某对象的指针，该对象具有以下结构，包含 rpc 程序号数据库 **/etc/rpc** 中某一行分解后的字段：

```c
struct rpcent {
	char	*r_name;	/* 此 rpc 程序的服务器名称 */
	char	**r_aliases;	/* 别名列表 */
	long	r_number;	/* rpc 程序号 */
};
```

该结构的成员包括：

**`r_name`** 此 rpc 程序的服务器名称。

**`r_aliases`** 此 rpc 程序的备用名称列表，以零结尾。

**`r_number`** 此服务的 rpc 程序号。

`getrpcent` 函数读取文件的下一行，必要时打开文件。

`setrpcent` 函数打开并回绕文件。如果 `stayopen` 标志非零，则在每次调用 `getrpcent`（无论是直接调用还是通过其他 “getrpc” 调用间接调用）之后，net 数据库不会被关闭。

`endrpcent` 函数关闭文件。

`getrpcbyname` 和 `getrpcbynumber` 函数从文件开头顺序搜索，直到找到匹配的 rpc 程序名或程序号，或者到达文件末尾。

## 文件

**/etc/rpc**

## 诊断

遇到 `EOF` 或错误时返回 `NULL` 指针。

## 参见

rpc(5), rpcinfo(8), ypserv(8)

## 缺陷

所有信息都包含在静态区域中，因此如果要保存，必须进行复制。
