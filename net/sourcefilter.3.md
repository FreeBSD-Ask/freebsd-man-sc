# sourcefilter.3

`sourcefilter` — 高级多播组成员资格 API

## 名称

`sourcefilter`

## 概要

`#include <sys/socket.h>`

`#include <netinet/in.h>`

```c
int
getipv4sourcefilter(int s, struct in_addr interface, struct in_addr group,
    uint32_t *fmode, uint32_t *numsrc, struct in_addr *slist);

int
getsourcefilter(int s, uint32_t interface, struct sockaddr *group,
    socklen_t grouplen, uint32_t *fmode, uint32_t *numsrc,
    struct sockaddr_storage *slist);

int
setipv4sourcefilter(int s, struct in_addr interface, struct in_addr group,
    uint32_t fmode, uint32_t numsrc, struct in_addr *slist);

int
setsourcefilter(int s, uint32_t interface, struct sockaddr *group,
    socklen_t grouplen, uint32_t fmode, uint32_t numsrc,
    struct sockaddr_storage *slist);
```

## 描述

`sourcefilter` 函数实现了 RFC 3678 中定义的高级、全状态多播 API。应用程序可使用这些函数原子地设置和检索与套接字 `s` 及多播 `group` 关联的多播源地址过滤器。

`getipv4sourcefilter` 和 `getsourcefilter` 函数允许应用程序发现现有组成员资格的过滤模式和源过滤条目。

内核始终会在 `*numsrc` 中返回该套接字上该组的源过滤条目数量。如果 `*numsrc` 参数非零，内核将尝试在 `slist` 所指向的数组中返回最多 `*numsrc` 个过滤条目。`*numsrc` 参数可设置为 0，此时 `slist` 参数将被忽略。

对于 `setipv4sourcefilter` 和 `setsourcefilter` 函数，`fmode` 参数可分别使用 `MCAST_INCLUDE` 或 `MCAST_EXCLUDE` 常量将套接字置于包含或排除组成员资格模式。`numsrc` 参数指定 `slist` 数组中的源条目数量。如果 `numsrc` 参数的值为 0，将从套接字移除所有源过滤器。从处于 `MCAST_INCLUDE` 过滤模式的成员资格中移除所有源过滤器将导致在该套接字上离开该组。

协议无关的 `setsourcefilter` 函数允许应用程序通过为 `interface` 参数传递其索引，在可能未分配协议地址的接口上加入多播组。

这些函数所做的任何更改都将适当地通知本地网络上的 IGMPv3 和/或 MLDv2 路由器。如果不存在 IGMPv3 或 MLDv2 路由器，这些函数对源过滤器列表所做的更改不会导致传输状态更改，但导致组被加入或离开的更改除外。无论链路上使用的 IGMP 或 MLD 版本如何，内核都将继续维护源过滤器状态。

## 实现说明

这些函数的 IPv4 特定版本是基于协议无关函数实现的。鼓励应用程序编写者使用协议无关函数，以提高效率并与 IPv6 网络前向兼容。

对于协议无关函数 `getsourcefilter` 和 `setsourcefilter`，`grouplen` 参数指定 `group` 所指向结构的大小。这是为了区分不同的地址族所必需的。

目前 FreeBSD 不支持 IPv4 协议族的源地址选择，因此*不推荐*在未编号的 IPv4 接口上使用多播 API。在所有情况下，接口上第一个分配的 IPv4 地址将用作 IGMP 控制流量的源地址。如果此地址被移除或更改，结果未定义。

## 返回值

`getsourcefilter`、`getipv4sourcefilter`、`setsourcefilter` 和 `setipv4sourcefilter` 函数在成功时返回 0，失败时返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`sourcefilter` 函数可能因以下原因失败：

**`[EADDRNOTAVAIL]`** `interface` 参数所引用的网络接口未在系统中配置，或者系统不是该 `group` 的成员。

**`[EAFNOSUPPORT]`** `group` 和/或一个或多个 `slist` 参数的地址族不被系统支持，或者 `group` 和 `slist` 参数的地址族不一致。

**`[EINVAL]`** `group` 参数不包含多播地址。`fmode` 参数无效；必须设置为 `MCAST_INCLUDE` 或 `MCAST_EXCLUDE`。`numsrc` 或 `slist` 参数未指定源列表。

**`[ENOMEM]`** 没有足够的内存来执行所请求的操作。

## 参见

[ip(4)](../man4/ip.4.md), [ip6(4)](../man4/ip6.4.md), [multicast(4)](../man4/multicast.4.md), ifmcstat(8)

> D. Thaler, B. Fenner, B. Quinn, "Socket Interface Extensions for Multicast Source Filters", RFC 3678, Jan 2004.

## 历史

`sourcefilter` 函数首次出现于 FreeBSD 7.0。

## 作者

Bruce M. Simpson <bms@FreeBSD.org>
