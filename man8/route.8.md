  ROUTE(8)  

ROUTE(8)

FreeBSD System Manager's Manual

ROUTE(8)

[名称](#__u540D___u79F0_)
=======================

`route` —

手动操作路由表

[概要](#__u6982___u8981_)
=======================

`route` \[`-dnqtv`\] command \[\[modifiers\] args\]

[描述](#__u63CF___u8FF0_)
=======================

`route` 实用程序用于手动操作网络路由表。 通常不需要它，因为系统路由表管理守护进程，例如 routed(8), 应该倾向于这个任务。

`route` 实用程序支持有限数量的通用选项，但支持丰富的命令语言，使用户能够指定任何可以通过 route(4) 中讨论的编程接口传递的任意请求。

可以使用以下选项：

[`-4`](#4)

指定 `inet` 地址族作为子命令的族提示。

[`-6`](#6)

指定 `inet6` 地址族作为子命令的族提示。

[`-d`](#d)

在仅调试模式下运行，即不实际修改路由表。

[`-n`](#n)

在报告操作时绕过以符号方式打印主机和网络名称的尝试。 （符号名称和数字等价物之间的转换过程可能非常耗时，并且可能需要网络的正确操作；因此忘记这一点可能是有利的，尤其是在尝试修复网络操作时）。

[`-t`](#t)

在仅测试模式下运行。 使用 /dev/null 代替套接字。

[`-v`](#v)

（详细）打印更多详细信息。

[`-q`](#q)

禁止 `add`, `change`, `delete` 和 `flush` 命令的所有输出。

`route` 实用程序提供以下命令：

[`add`](#add)

添加路线。

[`flush`](#flush)

删除所有路线。

[`delete`](#delete)

删除特定路线。

[`del`](#del)

[`delete`](#delete_2) 命令的另一个名称。

[`change`](#change)

更改路由的各个方面（例如其网关）。

[`get`](#get)

查找并显示目的地的路线。

[`monitor`](#monitor)

持续报告对路由信息库的任何更改、路由查找未命中或可疑的网络分区。

[`show`](#show)

[`get`](#get_2) 命令的另一个名称。

monitor 命令的语法如下：

`route` \[`-n`\] `monitor` \[`-fib` number\]

flush 命令的语法如下：

`route` \[`-n`\] `flush` \[family\] \[`-fib` number\]

如果指定了 `flush` 命令， `route` 将“刷新”所有网关条目的路由表。 当地址族可以由 `-osi`, `-xns`, `-inet6` 或 `-inet` 修饰符中的任何一个指定时，只有目的地地址在所描绘的族中的路由才会被删除。 此外， `-4` 或 `-6` 可用作 `-inet` 和 `-inet6` 修饰符的别名。 当指定 `-fib` 选项时，该操作将应用于指定的 FIB (routing table) 。

add 命令的语法如下：

`route` \[`-n`\] `add` \[`-net` | `-host`\] destination gateway \[netmask\] \[`-fib` number\]

其他命令具有以下语法：

`route` \[`-n`\] command \[`-net` | `-host`\] destination \[gateway \[netmask\]\] \[`-fib` number\]

其中 destination 是目标主机或网络， gateway 是路由数据包的下一跳中介。 通过解释指定为 destination 参数的 Internet 地址，可以将到特定主机的路由与到网络的路由区分开来。 可选修饰符 `-net` 和 `-host` 分别强制将目标解释为网络或主机。 否则，如果 destination 具有 INADDR\_ANY (`0.0.0.0`) 的 “local address part” ，或者如果 destination 是网络的符号名称，则假定路由到网络；否则，假定它是到主机的路由。 或者，也可以以 net/bits 格式指定 destination 。

例如， `128.32` 被解释为 `-host` `128.0.0.32`; `128.32.130` 被解释为 `-host` `128.32.0.130`; `-net` `128.32` 被解释为 `128.32.0.0;` `-net` `128.32.130` 被解释为 `128.32.130.0;` and `192.168.64/20` 被解释为 `-net` `192.168.64` `-netmask` `255.255.240.0` 。

default destination 是默认路由的同义词。对于 `IPv4` ，它是 `-net` `-inet` `0.0.0.0`, 对于 `IPv6` ,它是 `-net` `-inet6` `::` 。

如果可以通过不需要中间系统充当网关的接口直接到达目的地，则应指定 `-interface` 修饰符；给定的网关是该主机在公共网络上的地址，表示要用于传输的接口。或者，如果接口是点对点的，则可以给出接口本身的名称，在这种情况下，即使本地或远程地址发生变化，路由仍然有效。

可选修饰符 `-xns`, `-osi` 和 `-link` 指定所有后续地址都在 XNS 或 OSI 地址族中，或者指定为链接级地址，并且名称必须是数字规范而不是符号名称。

可选的 `-netmask` 修饰符旨在使用 netmask 选项实现 OSI ESIS 重定向的效果，或手动添加具有不同于隐含网络接口的网络掩码的子网路由（否则将使用 OSPF 或 ISIS 路由协议进行通信）。 一个指定一个附加的后续地址参数（被解释为网络掩码）。 通过确保此选项遵循目标参数，可以覆盖在 AF\_INET 案例中生成的隐式网络掩码。

对于 `AF_INET6`, 可用 `-prefixlen` 限定符代替 `-mask` 限定符，因为 IPv6 中不允许使用非连续掩码。 例如， `-prefixlen` `32` 指定将使用网络掩码 `ffff:ffff:0000:0000:0000:0000:0000:0000` 。 默认前缀长度为 64。 但是，如果为 destination 指定了 `default` ，则假定为 0。 请注意，限定符仅适用于 `AF_INET6` 地址族。

当发送到与路由匹配的目的地时，路由具有影响协议操作的相关标志。 可以通过指示以下相应的修饰符来设置（或有时清除）这些标志：

\-xresolve RTF\_XRESOLVE - 在使用时发出消息（用于外部查找） -iface ~RTF\_GATEWAY - 目的地可直接到达 -static RTF\_STATIC - 手动添加路由 -nostatic ~RTF\_STATIC - 内核或守护进程添加的假装路由 -reject RTF\_REJECT - 匹配时发出无法访问的 ICMP -blackhole RTF\_BLACKHOLE - 静默丢弃 pkts（在更新期间） -proto1 RTF\_PROTO1 - 设置协议特定的路由标志 #1 -proto2 RTF\_PROTO2 - 设置协议特定的路由标志 #2 

可选修饰符 `-rtt`, `-rttvar`, `-sendpipe`, `-recvpipe`, `-mtu`, `-hopcount`, `-expire` 和 `-ssthresh` 为传输层协议（如 TCP 或 TP4）在路由条目中维护的数量提供初始值。 这些可以通过在每个要被 `-lock` 元修饰符锁定的修饰符之前单独锁定，或者可以指定所有随后的度量都可以由 `-lockrest` 元修饰符锁定。

请注意， `-expire` 接受路由的过期时间作为自 Epoch 以来的秒数（请参阅 (see time(3)) ）。 当数字的第一个字符是 “+” 或 “-” 时，它被解释为相对于当前时间的值。

可选修饰符 `-fib` number 数字指定该命令将应用于非默认 FIB。 该 number 必须小于 net.fibs sysctl(8) MIB。 当未指定此修饰符或指定负数时，将使用 net.my\_fibnum sysctl(8) MIB 中显示的默认 FIB。

该 number 允许通过逗号分隔的列表和/或范围规范进行多个 FIB。 “`-fib` `2,4,6`” 表示 FIB 编号 2、4 和 6。 “`-fib` `1,3-5,6`” 表示 1、3、4、5 和 6。

在目标和网关不足以指定路由的 `change` 或 `add` 命令中（如在 ISO 情况下，多个接口可能具有相同的地址）， `-ifp` 或 `-ifa` 修饰符可用于确定接口或接口地址。

为 destination 或 gateway 指定的所有符号名称首先使用 gethostbyname(3) 作为主机名查找。 如果此查找失败，则使用 getnetbyname(3) 将名称解释为网络的名称。

`route` 实用程序使用路由套接字和新的消息类型 `RTM_ADD`, `RTM_DELETE`, `RTM_GET` 和 `RTM_CHANGE` 。 因此，只有超级用户可以修改路由表。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `route` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

将默认路由添加到网络路由表。 这会将路由表中不可用的目的地的所有数据包发送到默认网关 192.168.1.1：

`route add -net 0.0.0.0/0 192.168.1.1`

添加默认路由的较短版本也可以写成：

`route add default 192.168.1.1`

通过 172.16.1.1 网关添加到 172.16.10.0/24 网络的静态路由：

`route add -net 172.16.10.0/24 172.16.1.1`

更改路由表中已建立的静态路由的网关：

`route change -net 172.16.10.0/24 172.16.1.2`

显示目标网络的路由：

`route show 172.16.10.0`

从路由表中删除静态路由：

`route delete -net 172.16.10.0/24 172.16.1.2`

从路由表中删除所有路由：

`route flush`

[诊断](#__u8BCA___u65AD_)
=======================

add \[host | network \] %s: gateway %s flags %x

正在将指定的路线添加到表中。 打印的值来自 ioctl(2) 调用中提供的路由表条目。 如果使用的网关地址不是网关的主地址（ gethostbyname(3) 返回的第一个地址），则网关地址以数字和符号形式打印。

delete \[ host | network \] %s: gateway %s flags %x

如上所述，但在删除条目时。

%s %s done

当指定了 `flush` 命令时，每个被删除的路由表条目都用这种形式的消息来指示。

Network is unreachable

尝试添加路由失败，因为列出的网关不在直接连接的网络上。 必须给出下一跳网关。

not in table

尝试对表中不存在的条目执行删除操作。

routing table overflow

尝试了添加操作，但系统资源不足，无法分配内存来创建新条目。

gateway uses the same route

[`change`](#change_2) 操作导致路由的网关使用与被更改的路由相同的路由。 下一跳网关应该可以通过不同的路由到达。

[参见](#__u53C2___u89C1_)
=======================

netintro(4), route(4), arp(8), routed(8)

[历史](#__u5386___u53F2_)
=======================

`route` 实用程序出现在 4.2BSD 中。

[缺陷](#__u7F3A___u9677_)
=======================

第一段可能稍微夸大了 routed(8) 的能力。

目前，设置了 `RTF_BLACKHOLE` 标志的路由需要使用 `-iface` 选项将网关设置为 lo(4) 驱动程序的实例，才能使该标志生效；除非启用了 IP 快速转发，在这种情况下，标志的含义将始终得到尊重。

January 9, 2019

FreeBSD 13.1-RELEASE