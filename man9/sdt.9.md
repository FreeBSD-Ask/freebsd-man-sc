# SDT(9)

`SDT` — 用于添加静态定义追踪探针的 DTrace 框架

## 名称

`SDT`

## 概要

```c
#include <sys/param.h>
#include <sys/queue.h>
#include <sys/sdt.h>

SDT_PROVIDER_DECLARE(prov)
SDT_PROVIDER_DEFINE(prov)
SDT_PROBE_DECLARE(prov, mod, func, name)
SDT_PROBE_DEFINE(prov, mod, func, name)
SDT_PROBE_DEFINE0(prov, mod, func, name)
SDT_PROBE_DEFINE1(prov, mod, func, name, arg0)
SDT_PROBE_DEFINE2(prov, mod, func, name, arg0, arg1)
SDT_PROBE_DEFINE3(prov, mod, func, name, arg0, arg1, arg2)
SDT_PROBE_DEFINE4(prov, mod, func, name, arg0, arg1, arg2, arg3)
SDT_PROBE_DEFINE5(prov, mod, func, name, arg0, arg1, arg2, arg3, arg4)
SDT_PROBE_DEFINE6(prov, mod, func, name, arg0, arg1, arg2, arg3, arg4, arg5)
SDT_PROBE_DEFINE7(prov, mod, func, name, arg0, arg1, arg2, arg3, arg4, arg5,
    arg6)
SDT_PROBE_DEFINE0_XLATE(prov, mod, func, name)
SDT_PROBE_DEFINE1_XLATE(prov, mod, func, name, arg0, xarg0)
SDT_PROBE_DEFINE2_XLATE(prov, mod, func, name, arg0, xarg0, arg1, xarg1)
SDT_PROBE_DEFINE3_XLATE(prov, mod, func, name, arg0, xarg0, arg1, xarg1,
    arg2, xarg2)
SDT_PROBE_DEFINE4_XLATE(prov, mod, func, name, arg0, xarg0, arg1, xarg1,
    arg2, xarg2, arg3, xarg3)
SDT_PROBE_DEFINE5_XLATE(prov, mod, func, name, arg0, xarg0, arg1, xarg1,
    arg2, xarg2, arg3, xarg3, arg4, xarg4)
SDT_PROBE_DEFINE6_XLATE(prov, mod, func, name, arg0, xarg0, arg1, xarg1,
    arg2, xarg2, arg3, xarg3, arg4, xarg4, arg5, xarg5)
SDT_PROBE_DEFINE7_XLATE(prov, mod, func, name, arg0, xarg0, arg1, xarg1,
    arg2, xarg2, arg3, xarg3, arg4, xarg4, arg5, xarg5, arg6, xarg6)
SDT_PROBE0(prov, mod, func, name)
SDT_PROBE1(prov, mod, func, name, arg0)
SDT_PROBE2(prov, mod, func, name, arg0, arg1)
SDT_PROBE3(prov, mod, func, name, arg0, arg1, arg2)
SDT_PROBE4(prov, mod, func, name, arg0, arg1, arg2, arg3)
SDT_PROBE5(prov, mod, func, name, arg0, arg1, arg2, arg3, arg4)
SDT_PROBE6(prov, mod, func, name, arg0, arg1, arg2, arg3, arg4, arg5)
SDT_PROBE7(prov, mod, func, name, arg0, arg1, arg2, arg3, arg4, arg5, arg6)
```

## 描述

`SDT` 宏允许程序员在内核代码中定义静态追踪点。这些追踪点由 `SDT` 框架用于创建 DTrace 探针，从而可以使用 [dtrace(1)](../man1/dtrace.1.md) 对代码进行插桩。默认情况下，`SDT` 追踪点被禁用，对周围代码没有影响。当与给定追踪点对应的 DTrace 探针被启用时，执行该追踪点的线程将调用处理程序并触发探针。此外，追踪点可以接受参数，使得在启用的探针触发时能够将数据传递给 DTrace 框架。

多个追踪点可以对应单个 DTrace 探针，这允许程序员创建对应于逻辑系统事件而非绑定到特定代码执行路径的 DTrace 探针。例如，对应 IP 数据包到达网络栈的 DTrace 探针可以使用两个 `SDT` 追踪点来定义：一个用于 IPv4 数据包，一个用于 IPv6 数据包。

除了定义 DTrace 探针外，`SDT` 宏还允许程序员定义新的 DTrace 提供者，从而可以对逻辑相关的探针进行命名空间隔离。一个例子是 FreeBSD 的 sctp 提供者，其中包含 FreeBSD [sctp(4)](../man4/sctp.4.md) 实现的 `SDT` 探针。

`SDT_PROVIDER_DECLARE` 和 `SDT_PROVIDER_DEFINE` 宏分别用于声明和定义名为 `prov` 的 DTrace 提供者。提供者只需定义一次；但是，在定义属于该提供者的任何 `SDT` 探针之前，必须先声明该提供者。

类似地，`SDT_PROBE_DECLARE` 和 `SDT_PROBE_DEFINE*` 宏用于使用 `SDT` 框架声明和定义 DTrace 探针。探针一旦定义，就可以将探针的追踪点添加到内核代码中。DTrace 探针标识符由提供者、模块、函数和名称组成，所有这些都可以在 `SDT` 探针定义中指定。注意，探针不应指定模块名称：探针的模块名称用于确定在卸载内核模块时是否应销毁该探针。参见缺陷部分。特别要注意，探针不得跨多个内核模块定义。

如果探针名称中需要 `-` 字符（连字符），则在传递给各种 `SDT_*` 宏的探针 `name` 参数中应表示为 `__`（双下划线），这是出于技术原因（连字符在 C 标识符中无效）。

`SDT_PROBE_DEFINE*` 宏还允许程序员声明传递给探针的参数类型。这是可选的；如果省略了参数类型（通过使用 `SDT_PROBE_DEFINE` 宏），希望使用这些参数的用户将不得不在其 D 脚本中手动将它们转换为正确的类型。强烈建议探针定义包含其参数类型的声明。

`SDT_PROBE_DEFINE*_XLATE` 宏用于参数类型要动态转换为相应 `xarg` 参数指定类型的探针。这主要用于从其他操作系统移植探针定义。如 [dtrace(1)](../man1/dtrace.1.md) 所见，使用这些宏定义的探针参数将具有与探针定义中的 `xarg` 类型匹配的类型。但是，在追踪点传入的参数将具有与探针定义中的原生参数类型匹配的类型，因此原生类型会被动态转换为转换后的类型。只要在 **`/usr/lib/dtrace`** 中定义了适当的转换器，使用该探针的脚本无需关心给定 `SDT` 探针参数的底层类型。

`SDT_PROBE*` 宏用于创建 `SDT` 追踪点。它们用于添加到可执行代码中，可用于对其调用所在的代码进行插桩。

## 提供者

有许多内核 DTrace 提供者可用。通常，这些提供者定义了稳定的接口，应如此对待：如果重命名探针或修改其参数，可能会破坏现有的 D 脚本。但是，定义临时 `SDT` 探针来调试子系统或驱动程序通常很有用。类似地，开发者可能希望提供一组 `SDT` 探针而不承诺其未来稳定性。此类探针应添加到 `sdt` 提供者中，而不是定义新的提供者。

## 实例

可以使用以下命令列出当前系统上可用的 DTrace 提供者：

```sh
dtrace -l | sed 1d | awk '{print $2}' | sort -u
```

通过使用 `-P` 标志指定提供者，可以获取该提供者提供的探针的详细列表。例如，要查看 `sched` 提供者的探针和参数类型，运行：

```sh
dtrace -lv -P sched
```

以下探针定义将创建一个名为 `icmp:::receive-unreachable` 的 DTrace 探针，该探针在内核收到类型为目标不可达的 ICMP 数据包时触发：

```c
SDT_PROVIDER_DECLARE(icmp);
SDT_PROBE_DEFINE1(icmp, , , receive__unreachable,
    "struct icmp *");
```

此特定探针接受一个参数：指向包含该数据包 ICMP 头的结构的指针。注意，未指定此探针的模块名称。

考虑一个在网络栈收到 IP 数据包时触发的 DTrace 探针。这样的探针将由多个追踪点定义：

```c
SDT_PROBE_DEFINE3(ip, , , receive, "struct ifnet *",
    "struct ip *", "struct ip6_hdr *");
int
ip_input(struct mbuf *m)
{
	struct ip *ip;
	...
	ip = mtod(m, struct ip *);
	SDT_PROBE3(ip, , , receive, m->m_pkthdr.rcvif, ip, NULL);
	...
}
int
ip6_input(struct mbuf *m)
{
	struct ip6_hdr *ip6;
	...
	ip6 = mtod(m, struct ip6_hdr *);
	SDT_PROBE3(ip, , , receive, m->m_pkthdr.rcvif, NULL, ip6);
	...
}
```

特别是，该探针应在内核收到 IPv4 或 IPv6 数据包时触发。

考虑上面讨论的 ICMP 探针。注意其第二个参数的类型为 `struct icmp`，这是 FreeBSD 内核中定义的用于表示 ICMP 数据包 ICMP 头的类型，定义于 RFC 792。Linux 有一个对应的类型 `struct icmphdr`，用于相同目的，但其字段名称与 FreeBSD 的 `struct icmp` 不同。类似地，illumos 定义了 `icmph_t` 类型，同样具有不同的字段名称。即使所有三个操作系统中都定义了 `icmp:::pkt-receive` 探针，仍然需要编写特定于操作系统的脚本来从 ICMP 头参数中提取给定字段。动态转换类型解决了这个问题：可以定义一个与操作系统无关的 [c(7)](../man7/c.7.md) 结构来表示 ICMP 头，例如 `struct icmp_hdr_dt`，并在 [dtrace(1)](../man1/dtrace.1.md) 库路径中定义从三种操作系统特定类型到 `struct icmp_hdr_dt` 的转换器。然后上面的 FreeBSD 探针可以定义为：

```c
SDT_PROBE_DEFINE1_XLATE(ip, , , receive, "struct icmp *",
    "struct icmp_hdr_dt *");
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_io(4)](../man4/dtrace_io.4.md), [dtrace_ip(4)](../man4/dtrace_ip.4.md), [dtrace_proc(4)](../man4/dtrace_proc.4.md), [dtrace_sched(4)](../man4/dtrace_sched.4.md), [dtrace_tcp(4)](../man4/dtrace_tcp.4.md), [dtrace_udp(4)](../man4/dtrace_udp.4.md)

## 作者

DTrace 和 `SDT` 框架最初由 John Birrell <jb@FreeBSD.org> 从 Solaris 移植到 FreeBSD。本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。

## 缺陷

`SDT` 宏允许将探针的模块和函数名称作为探针定义的一部分指定。DTrace 框架使用探针的模块名称来确定在卸载内核模块时应销毁哪些探针，因此探针的模块名称应与其定义所在模块的名称匹配。如果在探针定义中未指定模块名称，`SDT` 会正确设置模块名称；参见实例部分。

原始 `SDT` 实现（以及 FreeBSD 移植版）的目标之一是非活动的 `SDT` 探针不应产生性能影响。但不幸的是，情况并非如此；`SDT` 追踪点会向其定义所在的代码添加少量但非零的延迟。更复杂的探针实现将有助于缓解此问题。
