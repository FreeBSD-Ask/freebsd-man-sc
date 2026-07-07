# ether_gen_addr(9)

`ether_gen_addr` — 生成供使用的任意 MAC 地址

## 名称

`ether_gen_addr`

## 概要

```c
#include <sys/types.h>
#include <sys/socket.h>
#include <net/if.h>
#include <net/if_var.h>
#include <net/ethernet.h>
```

```c
void
ether_gen_addr(struct ifnet *ifp, struct ether_addr *hwaddr)
```

## 描述

`ether_gen_addr` 函数为没有分配地址的以太网接口生成一个任意 MAC 地址供使用。

默认情况下，`ether_gen_addr` 尝试使用 `ifp` 被添加到的 jail 的 hostid 生成一个稳定的 MAC 地址。在启动早期，尚未填充 `/etc/hostid` 的机器或不使用 [loader(8)](../man8/loader.8.md) 的机器上，hostid 可能尚未设置。

由于内存分配失败或 hostid 尚未填充，`ether_gen_addr` 可能无法派生出 MAC 地址。在这些情况下，将随机生成一个本地管理的单播 MAC 地址并通过 `hwaddr` 参数返回。

如果 `ether_gen_addr` 成功，则通过 `hwaddr` 参数返回一个属于 FreeBSD Foundation OUI "58:9c:fc" 的 MAC 地址。

## 作者

本手册页由 Kyle Evans <kevans@FreeBSD.org> 编写。
