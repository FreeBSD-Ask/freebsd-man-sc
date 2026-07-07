# getifaddrs(3)

`getifaddrs` — 获取接口地址

## 名称

`getifaddrs`

## 概要

`#include <ifaddrs.h>`

```c
int
getifaddrs(struct ifaddrs **ifap);

void
freeifaddrs(struct ifaddrs *ifp);
```

## 描述

`getifaddrs` 函数将本地机器上网络接口链表的引用存储到 `ifap` 所引用的内存中。该链表由 `ifaddrs` 结构组成，定义于包含文件

`#include <ifaddrs.h>`

`ifaddrs` 结构至少包含以下条目：

```c
    struct ifaddrs   *ifa_next;         /* 指向下一个结构的指针 */
    char             *ifa_name;         /* 接口名 */
    u_int             ifa_flags;        /* 接口标志 */
    struct sockaddr  *ifa_addr;         /* 接口地址 */
    struct sockaddr  *ifa_netmask;      /* 接口子网掩码 */
    struct sockaddr  *ifa_broadaddr;    /* 接口广播地址 */
    struct sockaddr  *ifa_dstaddr;      /* P2P 接口目的地址 */
    void             *ifa_data;		/* 地址特定数据 */
```

`ifa_next` 字段包含指向链表中下一个结构的指针。此字段在链表最后一个结构中为 `NULL`。

`ifa_name` 字段包含接口名。

`ifa_flags` 字段包含接口标志，由 [ifconfig(8)](../man8/ifconfig.8.md) 工具设置。

`ifa_addr` 字段引用接口地址或接口的链路层地址（如果存在），否则为 NULL。（应查阅 `ifa_addr` 字段的 `sa_family` 字段以确定 `ifa_addr` 地址的格式。）

`ifa_netmask` 字段引用与 `ifa_addr` 关联的子网掩码（如果已设置），否则为 NULL。

`ifa_broadaddr` 字段应仅在非 P2P 接口上引用，引用与 `ifa_addr` 关联的广播地址（如果存在），否则为 NULL。

`ifa_dstaddr` 字段引用 P2P 接口上的目的地址（如果存在），否则为 NULL。

`ifa_data` 字段以指向 `struct if_data` 的指针引用地址族特定数据（定义于包含文件

`#include <net/if.h>`

对于 `AF_LINK` 地址，它包含各种接口属性和统计信息。对于所有其他地址族，它包含按地址的接口统计信息。

`getifaddrs` 返回的数据是动态分配的，不再需要时应使用 `freeifaddrs` 释放。

## 返回值

`getifaddrs` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getifaddrs` 可能失败并为库例程 [ioctl(2)](../sys/ioctl.2.md)、[socket(2)](../sys/socket.2.md)、malloc(3) 或 [sysctl(3)](../gen/sysctl.3.md) 所指定的任何错误设置 `errno`。

## 参见

[ioctl(2)](../sys/ioctl.2.md), [socket(2)](../sys/socket.2.md), [sysctl(3)](../gen/sysctl.3.md), networking(4), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`ifaddrs` 实现首次出现于 BSDi BSD/OS。

## 缺陷

如果同时包含

`#include <net/if.h>`

和

`#include <ifaddrs.h>`

则

`#include <net/if.h>`

*必须*在

`#include <ifaddrs.h>`

之前包含。
