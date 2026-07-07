# netisr(9)

`netisr` — 内核网络分发服务

## 名称

`netisr`

## 概要

```c
#include <net/netisr.h>
```

```c
void
netisr_register(const struct netisr_handler *nhp)

void
netisr_unregister(const struct netisr_handler *nhp)

int
netisr_dispatch(u_int proto, struct mbuf *m)

int
netisr_dispatch_src(u_int proto, uintptr_t source, struct mbuf *m)

int
netisr_queue(u_int proto, struct mbuf *m)

int
netisr_queue_src(u_int proto, uintptr_t source, struct mbuf *m)

void
netisr_clearqdrops(const struct netisr_handler *nhp)

void
netisr_getqdrops(const struct netisr_handler *nhp, uint64_t *qdropsp)

void
netisr_getqlimit(const struct netisr_handler *nhp, u_int *qlimitp)

int
netisr_setqlimit(const struct netisr_handler *nhp, u_int qlimit)

u_int
netisr_default_flow2cpu(u_int flowid)

u_int
netisr_get_cpucount(void)

u_int
netisr_get_cpuid(u_int cpunumber)
```

通过以下内核编译选项启用可选的虚拟网络栈支持：

> options VIMAGE

```c
void
netisr_register_vnet(const struct netisr_handler *nhp)

void
netisr_unregister_vnet(const struct netisr_handler *nhp)
```

## 描述

`netisr` 内核接口套件允许设备驱动程序（及其他包源）将包定向到协议以进行直接分发或延迟处理。可以使用 [netstat(1)](../man1/netstat.1.md) 监控协议注册和工作流统计信息。

### 协议注册

协议使用 `netisr_register` 和 `netisr_unregister` 注册和注销处理程序，还可以使用 `netisr_clearqdrops`、`netisr_getqdrops`、`netisr_getqlimit` 和 `netisr_setqlimit` 管理队列限制和统计信息。

在 VIMAGE 内核中，每个非默认基础系统网络栈的虚拟网络栈（vnet）调用 `netisr_register_vnet` 和 `netisr_unregister_vnet` 来启用或禁用 `netisr` 对每个协议的包处理。禁用还将清除协议队列中的任何未处理包。

`netisr` 支持处理程序的多处理器执行，并依靠源排序和协议特定的排序及工作放置策略的组合来决定如何在一个或多个工作线程之间分配工作。注册协议将声明三种策略之一：

**`NETISR_POLICY_SOURCE`** `netisr` 应在没有协议建议的情况下维护源排序。`netisr` 将忽略 `mbuf` 头部上存在的任何流 ID 用于工作放置。

**`NETISR_POLICY_FLOW`** `netisr` 应维护由 `mbuf` 头部流 ID 字段定义的流排序。如果协议实现了 `nh_m2flow`，则当 `mbuf` 没有流 ID 时，`netisr` 将查询协议，回退到源排序。

**NETISR_POLICY_CPU** `netisr` 将完全委托所有工作放置决策给协议，为每个包查询 `nh_m2cpuid`。

注册使用 `struct netisr_handler` 声明，其字段定义如下：

**`const char *`** `nh_name` 协议的唯一字符串名称，可能包含在 sysctl(3) MIB 名称中，因此不应包含空格。

**`netisr_handler_t`** `nh_handler` 协议处理程序函数，在为该协议接收到的每个包上被调用。

**`netisr_m2flow_t`** `nh_m2flow` 可选的协议函数，用于为 `M_HASHTYPE_GET(m)` 等于 `M_HASHTYPE_NONE` 进入 `netisr` 的包生成流 ID 并设置有效的 hashtype。仅在 `NETISR_POLICY_FLOW` 时使用。

**`netisr_m2cpuid_t`** `nh_m2cpuid` 协议函数，用于确定包应在哪个 CPU 上处理。仅在 `NETISR_POLICY_CPU` 时使用。

**`netisr_drainedcpu_t`** `nh_drainedcpu` 可选的回调函数，在每个 CPU 队列被排空时被调用。对于直接分发的包从不触发。除非完全理解，否则不应使用此特殊用途函数。

**`u_int`** `nh_proto` 协议号，协议用于向 `netisr` 标识自身，包源用于选择将使用哪个处理程序来处理包。支持的协议号表见下文。由于实现原因，目前不支持大于 15 的协议号。

**`u_int`** `nh_qlimit` 协议的每 CPU 最大队列深度；由于内部实现细节，有效队列深度可能高达此数值的两倍。

**`u_int`** `nh_policy` 协议的排序和工作放置策略，如前所述。

### 包源接口

包源（如网络接口）可以使用 `netisr_dispatch` 和 `netisr_queue` 接口请求协议处理。两者都接受协议号和 `mbuf` 参数，但 `netisr_queue` 将始终在延迟上下文中异步执行协议处理程序，而 `netisr_dispatch` 在全局和每协议策略允许时将可选地直接分发。

为了提供额外的负载均衡和流信息，包源还可以使用 `netisr_dispatch_src` 和 `netisr_queue_src` 变体指定一个不透明的源标识符，实际上它可能是网络接口号或套接字指针。

### 协议号常量

当前定义了以下协议号：

**`NETISR_IP`** IPv4

**`NETISR_IGMP`** IGMPv3 回环

**`NETISR_ROUTE`** 路由套接字回环

**`NETISR_ARP`** ARP

**`NETISR_IPV6`** IPv6

## 作者

本手册页和 `netisr` 实现由 Robert N. M. Watson 编写。
