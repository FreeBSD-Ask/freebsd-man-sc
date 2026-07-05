# rtentry.9

`rtentry` — 内核路由表中条目的结构

## 名称

`rtentry`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/socket.h>
```

```c
#include <net/route.h>
```

## 描述

内核提供了一个通用机制，所有协议都可以通过它从中央路由表中存储和检索条目。此机制的某些部分还用于通过 [route(4)](../man4/route.4.md) 伪协议族中的套接字与用户级进程交互。

```c
#include <net/route.h>
```

头文件定义了此设施中使用的结构和显式常量。

路由的基本结构由 `struct rtentry` 定义，包括以下字段：

**`struct radix_node rt_nodes[2]`** 由基数树例程使用的粘合。这些成员还在其子结构中包含创建路由时使用的键（即目的地址）和掩码。给定 `struct rtentry *`，可以使用 `rt_key(rt)` 和 `rt_mask(rt)` 宏提取此信息（以 `struct sockaddr *` 形式）。

**`struct sockaddr *rt_gateway`** 路由的“目标”，可以自身表示一个目的地（某些协议会在此放置链路层地址），也可以是前往该目的地途中的某个中间停靠点（如果设置了 `RTF_GATEWAY` 标志）。

**`int rt_flags`** 见下文。如果 `RTF_UP` 标志不存在，`rtfree` 函数将在最后一个引用丢弃时从基数树中删除该路由。

**`int rt_refcnt`** 路由条目是引用计数的；此字段指示外部（相对于基数树）引用的数量。

**`struct ifnet *rt_ifp`**

**`struct ifaddr *rt_ifa`** 这两个字段表示路由查找所提问题的“答案”，即它们命名了用于向此路由所代表的目的地或目的地集合发送数据包的接口和接口地址。

**`u_long rt_mtu`** 见下文 rmx_mtu 的描述。

**`u_long rt_weight`** 见下文 rmx_weight 的描述。

**`u_long rt_expire`** 见下文 rmx_expire 的描述。

**`counter64_t rt_pksent`** 见下文 rmx_pksent 的描述。

**`struct rtentry *rt_gwroute`** 此成员是对目的地为 `rt_gateway` 的路由的引用。仅用于 `RTF_GATEWAY` 路由。

**`struct mtx rt_mtx`** 用于锁定此路由条目的互斥锁。

定义了以下标志位：

**`RTF_UP`** 路由未被删除。

**`RTF_GATEWAY`** 路由指向中间目的地而非最终接收者；`rt_gateway` 和 `rt_gwroute` 字段命名该目的地。

**`RTF_HOST`** 这是主机路由。

**`RTF_REJECT`** 目的地当前不可达。这应导致输出例程返回 `EHOSTUNREACH` 错误。

**`RTF_DYNAMIC`** 此路由由 `rtredirect` 动态创建。

**`RTF_MODIFIED`** 此路由被 `rtredirect` 修改。

**`RTF_DONE`** 仅在 [route(4)](../man4/route.4.md) 协议中使用，指示请求已执行。

**`RTF_XRESOLVE`** 当此路由作为查找结果返回时，在 [route(4)](../man4/route.4.md) 接口上发送报告，请求外部进程执行此路由的解析。

**`RTF_STATIC`** 指示此路由是通过 [route(8)](../man8/route.8.md) 命令手动添加的。

**`RTF_BLACKHOLE`** 请求丢弃通过此路由发送的输出。

**`RTF_PROTO1`**

**`RTF_PROTO2`**

**`RTF_PROTO3`** 协议特定。

**`RTF_PINNED`** 指示此路由对路由协议不可变。

**`RTF_LOCAL`** 指示此路由的目的地是配置为属于此系统的地址。

**`RTF_BROADCAST`** 指示目的地是广播地址。

**`RTF_MULTICAST`** 指示目的地是多播地址。

几个度量值在 `struct rt_metrics` 中提供，通过 [route(4)](../man4/route.4.md) API 与路由控制消息一起传递。目前仅提供 `rmx_mtu`、`rmx_expire` 和 `rmx_pksent` 度量值。所有其他值都被忽略。

`struct rt_metrics` 定义了以下度量值：

**`u_long rmx_locks`** 标志位，指示内核不允许动态修改哪些度量值。

**`u_long rmx_mtu`** 此路径的 MTU。

**`u_long rmx_hopcount`** 到达此目的地路径上的中间系统数量。

**`u_long rmx_expire`** 此路由应过期的时间（类似于 time(3)），如果永不过期则为零。各个协议族有责任确保过期路由实际上被删除。

**`u_long rmx_recvpipe`** 名义上，从目的地到此系统路径的带宽延迟乘积。实际上，此值用于设置接收缓冲区的大小（从而设置 TCP 等滑动窗口协议中的窗口）。

**`u_long rmx_sendpipe`** 同上，但方向相反。

**`u_long rmx_ssthresh`** TCP 拥塞避免中使用的慢启动阈值。

**`u_long rmx_rtt`** 到此目的地的往返时间，以每秒 `RMX_RTTUNIT` 为单位。

**`u_long rmx_rttvar`** 到此目的地往返时间的平均偏差，以每秒 `RMX_RTTUNIT` 为单位。

**`u_long rmx_pksent`** 通过此路由成功发送的数据包计数。

**`u_long rmx_filler[4]`** 可用于协议特定信息的空余空间。

## 参见

[route(4)](../man4/route.4.md), [route(8)](../man8/route.8.md)

## 历史

`rtentry` 结构首次出现在 4.2BSD 中。路由表的基数树表示和 `rt_metrics` 结构首次出现在 4.3BSD 中。

## 作者

本手册页由 Garrett Wollman 编写。

## 缺陷

此接口中保留了许多历史遗迹。`rt_gateway` 和 `rmx_filler` 字段可以命名得更好。
