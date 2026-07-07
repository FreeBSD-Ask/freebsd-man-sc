# pim(4)

`pim` — 协议无关多播

## 名称

`pim`

## 概要

`options MROUTING`

`#include <sys/types.h>`

`#include <sys/socket.h>`

`#include <netinet/in.h>`

`#include <netinet/ip_mroute.h>`

`#include <netinet/pim.h>`

`Ft int Fn getsockopt int s IPPROTO_IP MRT_PIM void *optval socklen_t *optlen Ft int Fn setsockopt int s IPPROTO_IP MRT_PIM const void *optval socklen_t optlen Ft int Fn getsockopt int s IPPROTO_IPV6 MRT6_PIM void *optval socklen_t *optlen Ft int Fn setsockopt int s IPPROTO_IPV6 MRT6_PIM const void *optval socklen_t optlen`

## 描述

PIM 是两种多播路由协议的通用名称：协议无关多播 - 稀疏模式（PIM-SM）和协议无关多播 - 密集模式（PIM-DM）。

PIM-SM 是一种多播路由协议，可使用底层单播路由信息库或单独的支持多播的路由信息库。它构建以每个组的会合点（RP）为根的单向共享树，并可选择为每个源创建最短路径树。

PIM-DM 是一种多播路由协议，使用底层单播路由信息库将多播数据报文泛洪给所有多播路由器。Prune 消息用于防止未来的数据报文传播到没有组成员信息的路由器。

PIM-SM 和 PIM-DM 都是相当复杂的协议，但 PIM-SM 要复杂得多。要在路由器中启用 PIM-SM 或 PIM-DM 多播路由，用户必须在内核中启用多播路由和 PIM 处理（参见 Sx SYNOPSIS 关于内核配置选项），并运行支持 PIM-SM 或 PIM-DM 的用户级进程。从开发者的角度来看，应使用 Sx Programming Guide 部分中描述的编程指南来控制内核中的 PIM 处理。

### 编程指南

在打开多播路由套接字并在内核中启用多播转发之后（参见 [multicast(4)](multicast.4.md)），应使用以下套接字选项之一来启用或禁用内核中的 PIM 处理。注意，这些选项需要特定特权（即 root 特权）：

```sh
/* IPv4 */
int v = 1;        /* 1 启用，或 0 禁用 */
setsockopt(mrouter_s4, IPPROTO_IP, MRT_PIM, (void *)&v, sizeof(v));
```

```sh
/* IPv6 */
int v = 1;        /* 1 启用，或 0 禁用 */
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_PIM, (void *)&v, sizeof(v));
```

启用 PIM 处理后，应添加支持多播的接口（参见 [multicast(4)](multicast.4.md)）。在 PIM-SM 的情况下，还必须添加 PIM-Register 虚拟接口。可使用以下选项完成：

```sh
/* IPv4 */
struct vifctl vc;
memset(&vc, 0, sizeof(vc));
/* 按需赋值所有 vifctl 字段 */
...
if (is_pim_register_vif)
    vc.vifc_flags |= VIFF_REGISTER;
setsockopt(mrouter_s4, IPPROTO_IP, MRT_ADD_VIF, (void *)&vc,
           sizeof(vc));
```

```sh
/* IPv6 */
struct mif6ctl mc;
memset(&mc, 0, sizeof(mc));
/* 按需赋值所有 mif6ctl 字段 */
...
if (is_pim_register_vif)
    mc.mif6c_flags |= MIFF_REGISTER;
setsockopt(mrouter_s6, IPPROTO_IPV6, MRT6_ADD_MIF, (void *)&mc,
           sizeof(mc));
```

发送或接收 PIM 包可通过先打开“原始套接字”（参见 socket(2)），并使用 `IPPROTO_PIM` 协议值来完成：

```sh
/* IPv4 */
int pim_s4;
pim_s4 = socket(AF_INET, SOCK_RAW, IPPROTO_PIM);
```

```sh
/* IPv6 */
int pim_s6;
pim_s6 = socket(AF_INET6, SOCK_RAW, IPPROTO_PIM);
```

然后，可使用以下系统调用来发送或接收 PIM 包：sendto(2)、sendmsg(2)、recvfrom(2)、recvmsg(2)。

## 参见

getsockopt(2), recvfrom(2), recvmsg(2), sendmsg(2), sendto(2), setsockopt(2), socket(2), [inet(4)](inet.4.md), [intro(4)](intro.4.md), [ip(4)](ip.4.md), [multicast(4)](multicast.4.md)

## 标准

PIM-SM 协议在 RFC 2362 中规定（将被 draft-ietf-pim-sm-v2-new-*取代）。PIM-DM 协议在 draft-ietf-pim-dm-new-v2-* 中规定。

## 作者

IRIX 和 SunOS-4.x 的原始 IPv4 PIM 内核支持由 Ahmed Helmy（USC 和 SGI）实现。后来，代码被移植到各种 BSD 变体并由 George Edmond Eddy (Rusty)（ISI）、Hitoshi Asaeda（WIDE 项目）和 Pavlin Radoslavov（USC/ISI 和 ICSI）修改。IPv6 PIM 内核支持由 KAME 项目（`https://www.kame.net`）实现，并基于 IPv4 PIM 内核支持。

本手册页由 Pavlin Radoslavov (ICSI) 编写。
