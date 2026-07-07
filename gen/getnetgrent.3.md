# getnetgrent(3)

`getnetgrent` — 网络组数据库操作

## 名称

`getnetgrent`, `getnetgrent_r`, `innetgr`, `setnetgrent`, `endnetgrent`

## 库

Lb libc

## 概要

```c
#include <netdb.h>

int
getnetgrent(char **host, char **user, char **domain);

int
getnetgrent_r(char **host, char **user, char **domain,
    char *buf, size_t bufsize);

int
innetgr(const char *netgroup, const char *host,
    const char *user, const char *domain);

void
setnetgrent(const char *netgroup);

void
endnetgrent(void);
```

## 描述

这些函数操作于 **/etc/netgroup** 网络组数据库文件，该文件在 netgroup(5) 中描述。该数据库定义了一组网络组，每个网络组由一个或多个三元组组成：

```sh
(host, user, domain)
```

定义了主机、用户和域的组合。三个字段中的任何一个都可以指定为匹配任意字符串的“通配符”。

`getnetgrent()` 函数将三个指针参数设置为当前网络组中下一个成员的字符串。如果任何一个字符串指针为 `NULL`，则该字段被视为通配符。

`setnetgrent()` 和 `endnetgrent()` 函数分别设置当前网络组和终止当前网络组。如果 `setnetgrent()` 调用时使用的网络组与上一次调用不同，则隐含执行了 `endnetgrent()`。`setnetgrent()` 函数还将偏移量设置到网络组的第一个成员。

`innetgr()` 函数在指定组内搜索所有字段的匹配项。如果 **host**、**user** 或 **domain** 参数中的任何一个为 `NULL`，则这些字段将匹配网络组成员中的任何字符串值。

## 返回值

`getnetgrent()` 函数在没有更多网络组成员时返回 0，否则返回 1。`innetgr()` 函数在成功匹配时返回 1，否则返回 0。`setnetgrent()` 和 `endnetgrent()` 函数没有返回值。

## 文件

**/etc/netgroup** 网络组数据库文件

## 兼容性

网络组成员有三个字符串字段以保持与其他厂商实现的兼容性，但在 BSD 中 **domain** 字符串的用途并不明显。

## 参见

netgroup(5)

## 缺陷

`getnetgrent()` 函数返回指向动态分配数据区域的指针，当调用 `endnetgrent()` 函数时这些区域会被释放。
