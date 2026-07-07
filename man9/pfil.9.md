# pfil(9)

`pfil` — 包过滤接口

## 名称

`pfil`, `pfil_head_register`, `pfil_head_unregister`, `pfil_link`, `pfil_run_hooks`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/mbuf.h>
```

```c
#include <net/pfil.h>
```

```c
pfil_head_t
pfil_head_register(struct pfil_head_args *args)

void
pfil_head_unregister(struct pfil_head_t *head)

pfil_hook_t
pfil_add_hook(struct pfil_hook_args *)

void
pfil_remove_hook(pfil_hook_t)

int
pfil_link(struct pfil_link_args *args)

int
pfil_run_hooks(phil_head_t *, pfil_packet_t, struct ifnet *, int,
    struct inpcb *)
```

## 描述

`pfil_run_hooks` 框架允许为特定网络 I/O 流的每个传入或传出包调用指定的函数或函数列表。这些钩子可用于实现防火墙或执行包转换。

包过滤点，由于历史原因命名为 *head*，通过 `pfil_head_register` 注册。该函数接受一个特殊的带版本的 `struct pfil_head_args` 结构，该结构指定 head 的类型和功能以及人类可读的名称。如果过滤点要被销毁，创建它的子系统必须通过调用 `pfil_head_unregister` 注销它。

包过滤系统可以注册任意数量的过滤器，由于历史原因命名为 *hook*。要注册新钩子，需调用 `pfil_add_hook` 并传入特殊的带版本 `struct pfil_hook_args` 结构。该结构指定钩子的类型和功能、指向实际过滤函数的指针以及过滤模块的用户可读名称和规则集名称。之后可以使用 `pfil_remove_hook` 函数移除钩子。

要将现有 *hook* 连接到现有 *head*，应使用 `pfil_link` 函数。该函数接受带版本的 `struct pfil_link_args` 结构，该结构指定钩子和 head 的文字名称或指向它们的指针。通常 `pfil_link` 由过滤模块调用以自动注册其默认规则集和默认过滤点。它还在用户借助 pfilctl(8) 实用程序更改 `pfil_run_hooks` 配置时服务于 ioctl(2) 的内核侧。

对于通过 *head* 的每个包，后者应调用 `pfil_run_hooks`。该函数可以接受 `struct mbuf *` 指针或 `void *` 指针和长度。如果挂接的过滤模块无法理解 `void *` 指针，`pfil_run_hooks` 将为其提供一个假的指针。所有对 `pfil_run_hooks` 的调用都在网络 [epoch(9)](epoch.9.md) 中执行。

## HEAD（过滤点）

默认情况下，内核创建以下 head：

**inet** IPv4 包。

**inet6** IPv6 包。

**ethernet** 链路层包。

默认规则集自动链接到这些 head 以保持历史行为。

## 参见

ipfilter(4), ipfw(4), [pf(4)](../man4/pf.4.md), pfilctl(8)

## 历史

`pfil_run_hooks` 接口首次出现在 NetBSD 1.3 中。`pfil_run_hooks` 接口被引入 FreeBSD 5.2。在 FreeBSD 13.0 中，该接口被大幅重写。
