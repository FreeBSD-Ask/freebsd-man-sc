# bpf(9)

`bpf` — Berkeley 数据包过滤器

## 名称

`bpf`

## 概要

```c
#include <net/bpf.h>

void
bpfattach(struct ifnet *ifp, u_int dlt, u_int hdrlen)

void
bpfattach2(struct ifnet *ifp, u_int dlt, u_int hdrlen,
    struct bpf_if **driverp)

void
bpfdetach(struct ifnet *ifp)

void
bpf_tap(struct ifnet *ifp, u_char *pkt, u_int *pktlen)

void
bpf_mtap(struct ifnet *ifp, struct mbuf *m)

void
bpf_mtap2(struct bpf_if *bp, void *data, u_int dlen, struct mbuf *m)

u_int
bpf_filter(const struct bpf_insn *pc, u_char *pkt, u_int wirelen,
    u_int buflen)

int
bpf_validate(const struct bpf_insn *fcode, int flen)
```

## 描述

Berkeley 数据包过滤器（BPF）为数据链路层提供了与协议无关的原始接口。它允许网络上的所有数据包（包括发往其他主机的数据包）从网络接口传递到用户程序。每个程序可以指定一个过滤器，以 `bpf` 过滤机程序的形式。[bpf(4)](../man4/bpf.4.md) 手册页描述了用户程序使用的接口。本手册页描述接口用于将数据包传递给 `bpf` 的函数，以及用于测试和运行 `bpf` 过滤机程序的函数。

`bpfattach` 函数将网络接口附加到 `bpf`。`ifp` 参数是指向定义要附加到接口的结构体的指针。`dlt` 参数是数据链路层类型：`DLT_NULL`（无链路层封装）、`DLT_EN10MB`（以太网）、`DLT_IEEE802_11`（802.11 无线网络）等。其余链路层类型可在

```c
#include <net/bpf.h>
```

中找到。`hdrlen` 参数是链路头的固定大小；目前不支持可变长度头。`bpf` 系统将持有指向 `ifp->if_bpf` 的指针。当 `bpf` 需要使用下面的函数从该接口抽取数据包时，此变量将设置为非 `NULL` 值。

`bpfattach2` 函数允许将多个 `bpf` 实例附加到单个接口，方法是注册显式的 `if_bpf` 而非使用 `ifp->if_bpf`。这样就可以在该接口上对任何附加的数据链路层类型运行 [tcpdump(1)](../man1/tcpdump.1.md)。

`bpfdetach` 函数从 `ifp` 指定的接口分离 `bpf` 实例。对于每个附加的 `bpf` 实例，应调用一次 `bpfdetach` 函数。

`bpf_tap` 函数由接口用于将数据包传递给 `bpf`。`pkt` 所指向的数据包数据（包括链路头）长度为 `pktlen`，必须是连续缓冲区。`ifp` 参数是指向定义要抽取的接口的结构体的指针。数据包由每个进程的过滤器解析，如果被接受，则缓冲以供进程读取。

`bpf_mtap` 函数类似于 `bpf_tap`，不同之处在于它用于抽取 `mbuf` 链 `m` 中的数据包。`ifp` 参数是指向定义要抽取的接口的结构体的指针。与 `bpf_tap` 一样，`bpf_mtap` 需要为指定的数据链路层类型提供链路头。注意，`bpf` 只从 `mbuf` 链读取，不会释放它或保持指向它的指针。这意味着如果需要，可以将包含链路头的 `mbuf` 前置到链中。`bpf_mtap2` 提供了实现此功能的更简洁接口。

`bpf_mtap2` 函数允许用户独立于包含数据包的 `mbuf` `m` 传递长度为 `dlen` 的链路头 `data`。这简化了某些链路头的传递。

`bpf_filter` 函数在数据包 `pkt` 上执行从 `pc` 开始的过滤程序。`wirelen` 参数是原始数据包的长度，`buflen` 是存在的数据量。`buflen` 值为 0 是特殊情况；它表示 `pkt` 实际上是指向 mbuf 链的指针（`struct mbuf *`）。

`bpf_validate` 函数检查长度为 `flen` 的过滤代码 `fcode` 是否有效。

## 返回值

`bpf_filter` 函数在没有过滤器时返回 -1（转换为无符号整数）。否则，返回过滤程序的结果。

`bpf_validate` 函数在程序不是有效的过滤程序时返回 0。

## 事件处理程序

`bpf` 每次监听器附加到或从接口分离时都会调用 `bpf_track` [EVENTHANDLER(9)](eventhandler.9.md) 事件。指向（`struct ifnet *`）的指针作为第一个参数传递，接口的 `dlt` 紧随其后。最后一个参数指示监听器是附加（1）还是分离（0）。注意，处理程序在持有 `bpf` 全局锁时调用，这意味着在 [EVENTHANDLER(9)](eventhandler.9.md) 分发器内部有限制睡眠和调用 `bpf` 子系统。注意，对于只写监听器不会调用处理程序。

## 参见

[tcpdump(1)](../man1/tcpdump.1.md), [bpf(4)](../man4/bpf.4.md), [EVENTHANDLER(9)](eventhandler.9.md)

## 历史

Enet 数据包过滤器由 Carnegie-Mellon 大学的 Mike Accetta 和 Rick Rashid 于 1980 年创建。Stanford 的 Jeffrey Mogul 将代码移植到 BSD 并从 1983 年起继续其开发。此后，它演变为 DEC 的 Ultrix 数据包过滤器、SunOS 4.1 下的 STREAMS NIT 模块以及 BPF。

## 作者

BPF 由 Lawrence Berkeley 实验室的 Steven McCanne 在 1990 年夏天实现。大部分设计归功于 Van Jacobson。本手册页由 Orla McGann 编写。
