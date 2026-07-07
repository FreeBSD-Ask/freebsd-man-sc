# getifmaddrs(3)

`getifmaddrs` — 获取多播组成员关系

## 名称

`getifmaddrs`

## 概要

`#include <ifaddrs.h>`

```c
int
getifmaddrs(struct ifmaddrs **ifmap);

void
freeifmaddrs(struct ifmaddrs *ifmp);
```

## 描述

`getifmaddrs` 函数将本地机器上多播成员关系链表的引用存储到 `ifmap` 所引用的内存中。该链表由 `ifmaddrs` 结构组成，定义于包含文件

`#include <ifaddrs.h>`

`ifmaddrs` 结构至少包含以下条目：

```c
    struct ifmaddrs   *ifma_next;     /* 指向下一个结构的指针 */
    struct sockaddr   *ifma_name;     /* 接口名（AF_LINK） */
    struct sockaddr   *ifma_addr;     /* 多播地址 */
    struct sockaddr   *ifma_lladdr;   /* 链路层转换（如果有） */
```

`ifma_next` 字段包含指向链表中下一个结构的指针。此字段在链表最后一个结构中为 `NULL`。

`ifma_name` 字段引用一个 `AF_LINK` 地址结构，包含成员关系所在接口的名称。

`ifma_addr` 引用此成员关系所对应的地址。

`ifma_lladdr` 字段引用 `ifma_addr` 中协议层地址的链路层转换（如果已设置），否则为 `NULL`。

`getifmaddrs` 返回的数据是动态分配的，不再需要时应使用 `freeifmaddrs` 释放。

## 返回值

`getifmaddrs` 函数成功时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getifmaddrs` 可能失败并为库例程 malloc(3) 或 [sysctl(3)](../gen/sysctl.3.md) 所指定的任何错误设置 `errno`。

## 参见

[sysctl(3)](../gen/sysctl.3.md), networking(4), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`getifmaddrs` 函数首次出现于 FreeBSD 5.2。

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
