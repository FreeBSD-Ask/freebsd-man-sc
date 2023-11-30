  PING(8)  

PING(8)

FreeBSD System Manager's Manual

PING(8)

[名称](#__u540D___u79F0_)
=======================

`ping` —

向网络主机发送 ICMP 或 ICMPv6 ECHO\_REQUEST 数据包

[概要](#__u6982___u8981_)
=======================

`ping` \[`-4AaDdfHnoQqRrv`\] \[`-C` pcp\] \[`-c` count\] \[`-G` sweepmaxsize\] \[`-g` sweepminsize\] \[`-h` sweepincrsize\] \[`-i` wait\] \[`-l` preload\] \[`-M` `mask` | `time`\] \[`-m` ttl\] \[`-P` policy\] \[`-p` pattern\] \[`-S` src\_addr\] \[`-s` packetsize\] \[`-t` timeout\] \[`-W` waittime\] \[`-z` tos\] IPv4-host `ping` \[`-4AaDdfHLnoQqRrv`\] \[`-C` pcp\] \[`-c` count\] \[`-I` iface\] \[`-i` wait\] \[`-l` preload\] \[`-M` `mask` | `time`\] \[`-m` ttl\] \[`-P` policy\] \[`-p` pattern\] \[`-S` src\_addr\] \[`-s` packetsize\] \[`-T` ttl\] \[`-t` timeout\] \[`-W` waittime\] \[`-z` tos\] IPv4-mcast-group `ping` \[`-6AaDdEfHNnOoquvYyZ`\] \[`-b` bufsiz\] \[`-c` count\] \[`-e` gateway\] \[`-I` interface\] \[`-i` wait\] \[`-k` addrtype\] \[`-l` preload\] \[`-m` hoplimit\] \[`-P` policy\] \[`-p` pattern\] \[`-S` sourceaddr\] \[`-s` packetsize\] \[`-t` timeout\] \[`-W` waittime\] \[IPv6-hops ...\] IPv6-host

[描述](#__u63CF___u8FF0_)
=======================

(IPv4-host or IPv4-mcast-group) 调用的 `ping` 实用程序使用 ICMP protocol's mandatory ECHO\_REQUEST 数据报从主机或网关引发 ICMP ECHO\_RESPONSE 。 ECHO\_REQUEST 数据报 (“pings”) 有一个 IP 和 ICMP 报头，后跟一个 “struct timeval” ，然后是用于填充数据包的任意数量的 “pad” 字节。

当使用 IPv6 目标 (IPv6-host)调用时，它使用 ICMPv6 协议的强制 ICMP6\_ECHO\_REQUEST 数据报来引发 ICMP6\_ECHO\_REPLY 。 ICMP6\_ECHO\_REQUEST 数据报有一个 IPv6 标头和 ICMPv6 标头，其格式如 RFC 2463 中所述。

当使用主机名调用时，将使用首先解析目标的版本。在这种情况下，使用的选项和参数必须对特定 IP 版本有效，否则 `ping` 退出并出现错误。如果目标被解析为 IPv4 和 IPv6，则可以分别通过 `-4` 或 `-6` 选项请求特定的 IP 版本。为了向后兼容，也可以通过将二进制文件调用为 `ping6` 来选择 ICMPv6。

[IPv4 和 IPv6 目标通用的选项](#IPv4___u548C__IPv6___u76EE___u6807___u901A___u7528___u7684___u9009___u9879_)
---------------------------------------------------------------------------------------------------

[`-A`](#A)

听得见。如果在传输下一个数据包之前没有接收到数据包，则输出一个响铃 (ASCII 0x07) 字符。为了满足比传输间隔更长的往返时间，只有在未接收数据包的最大数量增加时，进一步丢失的数据包才会导致响铃。

[`-a`](#a)

听得见。接收到任何数据包时，在输出中包含一个响铃 (ASCII 0x07) 字符。

[`-C`](#C) pcp

发送数据包时添加 802.1p 以太网优先级代码点。0..7 使用特定的 PCP，-1 使用接口默认 PCP（或无）。

[`-c`](#c) count

在发送（和接收） count ECHO\_RESPONSE 数据包后停止。如果未指定此选项，则 `ping` 将一直运行直到中断。

对于 IPv4 目标，如果此选项与 ping 扫描一起指定，则每次扫描将包含 count 数据包。

[`-D`](#D)

禁用碎片。

[`-d`](#d)

在正在使用的套接字上设置 `SO_DEBUG` 选项。

[`-f`](#f)

洪水平。以返回数据包的速度或每秒一百次（以较大者为准）输出数据包。对于每个 ECHO\_REQUEST 发送一个句点 “.” 被打印，而对于每个收到的 ECHO\_REPLY 都会打印一个退格键。这可以快速显示有多少数据包被丢弃。只有超级用户可以使用此选项。

这在网络上可能非常困难，应谨慎使用。

[`-H`](#H)

主机名输出。在显示地址时尝试进行反向 DNS 查找。这与 `-n` 选项相反。

[`-I`](#I) iface

对于 IPv4 目标， iface 是一个 IP 地址，用于标识将发送数据包的接口。仅当 ping 目标是多播地址时，此标志才适用。

对于 IPv6 目标， iface 是从其发送数据包的接口名称（例如“em0”）。如果 ping 目标是多播地址或链路本地/站点本地单播地址，则此标志适用。

[`-i`](#i) wait

在发送 _每个数据包之间_ 等待 wait 几秒钟。默认是在每个数据包之间等待一秒钟。等待时间可以是分数，但只有超级用户可以指定小于 1 秒的值。此选项与 `-f` 选项不兼容。

[`-l`](#l) preload

如果指定了 preload ，则 `ping` 会在进入其正常行为模式之前尽可能快地发送那么多数据包。只有超级用户可以使用此选项。

[`-m`](#m) ttl

对于 IPv4 目标，为传出数据包设置 IP 生存时间。如果未指定，内核将使用 net.inet.ip.ttl MIB 变量的值。

对于 IPv6 目标，设置 IPv6 hoplimit。

[`-n`](#n)

仅限数字输出。不会尝试查找主机地址的符号名称。这与 `-H` 相反，它是默认行为。

[`-o`](#o)

收到一个回复包后成功退出。

[`-P`](#P) policy

policy 为 ping 会话指定 IPsec 策略。详细信息请参考 ipsec(4) 和 ipsec\_set\_policy(3) 。

[`-p`](#p) pattern

可以指定最多 16 个 “pad” 字节来填写您发送的数据包。这对于诊断网络中的数据相关问题很有用。例如， “`-p ff`” 将导致发送的数据包被全部填充。

[`-q`](#q)

安静的输出。除了启动时和完成时的摘要行外，什么都不会显示。

[`-S`](#S) src\_addr

使用以下 IP 地址作为传出数据包的源地址。在具有多个 IP 地址的主机上，此选项可用于强制源地址不是发送探测包的接口的 IP 地址。

对于 IPv4，如果 IP 地址不是本机的接口地址之一，则会返回错误并且不发送任何内容。

对于 IPv6，源地址必须是发送节点的单播地址之一，并且必须是数字。

[`-s`](#s) packetsize

指定要发送的数据字节数。默认值为 56，当与 8 字节的 ICMP 报头数据组合时，它转换为 64 个 ICMP 数据字节。

对于 IPv4，只有超级用户可以指定超过默认值的值。此选项不能与 ping 扫描一起使用。

对于 IPv6，您可能还需要指定 `-b` 以扩展套接字缓冲区大小。

[`-t`](#t) timeout

在 ping 退出之前指定超时（以秒为单位），无论已收到多少数据包。

[`-v`](#v)

详细输出。列出了收到的 ECHO\_RESPONSE 以外的 ICMP 数据包。

[`-W`](#W) waittime

等待每个发送数据包回复的时间（以毫秒为单位）。如果稍后收到回复，则该数据包不会打印为已回复，而是在计算统计信息时视为已回复。

[仅适用于 IPv4 目标的选项](#__u4EC5___u9002___u7528___u4E8E__IPv4___u76EE___u6807___u7684___u9009___u9879_)
--------------------------------------------------------------------------------------------------

[`-4`](#4)

无论目标是如何解析的，都使用 IPv4。

[`-G`](#G) sweepmaxsize

指定发送扫描 ping 时 ICMP 有效负载的最大大小。ping 扫描需要此选项。

[`-g`](#g) sweepminsize

指定发送扫描 ping 时要开始的 ICMP 有效负载的大小。默认值为 0。

[`-h`](#h) sweepincrsize

在发送扫描 ping 时，指定每次扫描后增加 ICMP 有效负载大小的字节数。默认值为 1。

[`-L`](#L)

抑制组播数据包的环回。仅当 ping 目标是多播地址时，此标志才适用。

[`-M`](#M) `mask` | [`time`](#time)

使用 `ICMP_MASKREQ` 或 `ICMP_TSTAMP` 而不是 `ICMP_ECHO` 。对于 `mask` ，打印远程机器的网络掩码。如果要覆盖响应中的网络掩码，请设置 net.inet.icmp.maskrepl 变量以启用 `ICMP_MASKREPLY` 和 net.inet.icmp.maskfake 。对于 `time` ，打印发起、接收和传输时间戳。设置 net.inet.icmp.tstamprepl MIB 变量以启用或禁用 `ICMP_TSTAMPREPLY` 。

[`-Q`](#Q)

有点安静的输出。 Don't 显示响应我们查询消息的 ICMP 错误消息。最初，需要 `-v` 标志来显示此类错误，但 `-v` 会显示所有 ICMP 错误消息。在一台繁忙的机器上，这个输出可能是霸道的。如果没有 `-Q` 标志， `ping` 会打印出由它自己的 ECHO\_REQUEST 消息引起的任何 ICMP 错误消息。

[`-R`](#R)

记录路线。 在 ECHO\_REQUEST 数据包中包含 RECORD\_ROUTE 选项，并在返回的数据包上显示路由缓冲区。 请注意，IP 标头仅足以容纳九个此类路由； traceroute(8) 命令通常更擅长确定数据包到特定目的地的路由。 如果返回的路由多于应有的路由，例如由于非法欺骗数据包，ping 将打印路由列表，然后在正确的位置截断它。 许多主机忽略或丢弃 RECORD\_ROUTE 选项。

[`-r`](#r)

绕过正常的路由表并直接发送到连接网络上的主机。 如果主机不在直连网络上，则返回错误。 此选项可用于通过没有路由的接口 ping 本地主机（例如，在接口被 routed(8) 删除后）。

[`-T`](#T) ttl

为多播数据包设置 IP 生存时间。 仅当 ping 目标是多播地址时，此标志才适用。

[`-z`](#z) tos

使用指定类型的服务。

IPv4-host

最终目标节点的主机名或 IPv4 地址。

IPv4-mcast-group

最终目标节点的 IPv4 多播地址。

[仅适用于 IPv6 目标的选项](#__u4EC5___u9002___u7528___u4E8E__IPv6___u76EE___u6807___u7684___u9009___u9879_)
--------------------------------------------------------------------------------------------------

[`-6`](#6)

无论目标如何解析，都使用 IPv6。

[`-b`](#b) bufsiz

设置套接字缓冲区大小。

[`-e`](#e) gateway

指定使用 gateway 作为到达目的地的下一跳。网关必须是发送节点的邻居。

[`-k`](#k) addrtype

生成 ICMPv6 节点信息节点地址查询，而不是回显请求。 addrtype 必须是由以下字符构成的字符串。

[`a`](#a_2)

从所有响应者的接口请求单播地址。 如果省略该字符，则只有那些属于具有响应者地址的接口的地址才是请求。

[`c`](#c_2)

请求响应者的 IPv4 兼容地址和 IPv4 映射地址。

[`g`](#g_2)

请求响应者的全局范围地址。

[`s`](#s_2)

请求响应者的站点本地地址。

[`l`](#l_2)

请求响应者的链接本地地址。

[`A`](#A_2)

请求响应者的任播地址。如果没有这个字符，响应者将只返回单播地址。 使用此字符，响应者将仅返回任播地址。 请注意，规范没有指定如何获取响应者的任播地址。 这是一个实验选项。

[`-N`](#N)

探测节点信息组播组地址 (`ff02::2:ffxx:xxxx`) 。 host 必须是目标的字符串主机名（不能是数字 IPv6 地址）。 节点信息组播组将根据给定的 host 计算，并将用作最终目的地。 由于节点信息组播组是链路本地组播组，因此需要通过 `-I` 选项指定出接口。

当指定两次时，将使用地址 (`ff02::2:xxxx:xxxx`) 。 前者在 RFC 4620 中，后者在旧 Internet Draft Draft-ietf-ipngwg-icmp-name-lookup 中。 请注意，包括 FreeBSD 在内的 KAME 派生实现使用后者。

[`-O`](#O)

生成 ICMPv6 节点信息支持的查询类型查询，而不是回显请求。 如果指定了 `-O` ，则 `-s` 无效。

[`-u`](#u)

默认情况下， `ping` 要求内核对数据包进行分段以适应最小 IPv6 MTU。 `-u` 选项将抑制以下两个级别的行为：当指定一次该选项时，将对单播数据包禁用该行为。 当该选项不止一次时，它将对单播和多播数据包都禁用。

[`-Y`](#Y)

与 `-y` 相同，但使用基于 03 草案的旧数据包格式。 存在此选项是为了向后兼容。 如果指定了 `-y` ，则 `-s` 无效。

[`-y`](#y)

生成 ICMPv6 节点信息 DNS 名称查询，而不是 echo-request。 如果指定了 `-y` ，则 `-s` 无效。

IPv6-hops

中间节点的 IPv6 地址，将被放入类型 0 路由标头中。

IPv6-host

最终目标节点的 IPv6 地址。

[仅适用于 IPv6 目标的实验选项](#__u4EC5___u9002___u7528___u4E8E__IPv6___u76EE___u6807___u7684___u5B9E___u9A8C___u9009___u9879_)
--------------------------------------------------------------------------------------------------------------------

[`-E`](#E)

启用传输模式 IPsec 封装的安全负载。

[`-Z`](#Z)

启用传输模式 IPsec 身份验证标头。

使用 `ping` 进行故障隔离时，应首先在本地主机上运行，以验证本地网络接口是否已启动并运行。 然后，应该 “ping” 越来越远的主机和网关。 计算往返时间和丢包统计。 如果接收到重复的数据包，则它们不包括在数据包丢失计算中，尽管这些数据包的往返时间用于计算往返时间统计信息。 当指定数量的数据包已发送（和接收）或程序以 `SIGINT` 终止时，将显示简短摘要，显示发送和接收的数据包数量，以及最小、平均、最大和标准偏差往返时间。

如果 `ping` 收到 `SIGINFO` （参见 stty(1) 的 `status` 参数）信号，则当前发送和接收的数据包数，以及往返时间的最小、平均、最大和标准偏差将写入标准输出。

该程序旨在用于网络测试、测量和管理。 由于它可能对网络施加负载，因此在正常操作期间或从自动脚本中使用 `ping` 是不明智的。

[ICMP 数据包详细信息](#ICMP___u6570___u636E___u5305___u8BE6___u7EC6___u4FE1___u606F_)
==============================================================================

没有选项的 IP 标头为 20 个字节。 一个 ICMP ECHO\_REQUEST 数据包包含一个额外的 8 字节的 ICMP 标头，后跟任意数量的数据。 当给定 packetsize 大小时，这表示该额外数据的大小（默认值为 56）。 因此，在 ICMP ECHO\_REPLY 类型的 IP 数据包内接收的数据量将始终比请求的数据空间（ ICMP ）多 8 个字节。

如果数据空间至少有 8 个字节大，则 `ping` 使用该空间的前 8 个字节来包含一个时间戳，用于计算往返时间。 如果指定的填充字节少于 8 个字节，则不给出往返时间。

[重复和损坏的数据包](#__u91CD___u590D___u548C___u635F___u574F___u7684___u6570___u636E___u5305_)
======================================================================================

`ping` 实用程序将报告重复和损坏的数据包。 ping 单播地址时永远不会出现重复的数据包，这似乎是由不适当的链路级重传引起的。 重复可能在许多情况下发生，并且很少（如果有的话）是一个好兆头，尽管存在低水平的重复可能并不总是引起警报。 ping 广播或多播地址时会出现重复，因为它们并不是真正的重复，而是来自不同主机对同一请求的回复。

损坏的数据包显然是引起警报的严重原因，并且通常表明 `ping` 数据包路径（网络或主机中）某处的硬件损坏。

[尝试不同的数据模式](#__u5C1D___u8BD5___u4E0D___u540C___u7684___u6570___u636E___u6A21___u5F0F_)
======================================================================================

（间）网络层不应该根据数据部分中包含的数据来区别对待数据包。 不幸的是，众所周知，与数据相关的问题会潜入网络并在很长一段时间内未被发现。 在许多情况下，会出现问题的特定模式是没有足够 “transitions” 的东西，例如全 1 或全零，或者位于边缘的模式，例如几乎全零。 在命令行上指定全零的数据模式（例如）并不一定足够，因为感兴趣的模式在数据链路级别，并且您键入的内容与控制器传输的内容之间的关系可能很复杂。

这意味着，如果您遇到与数据相关的问题，您可能需要进行大量测试才能找到它。 如果幸运的话，您可能会设法找到一个文件，该文件要么无法通过网络发送，要么传输时间比其他类似长度的文件要长得多。 然后，您可以检查此文件是否有重复的模式，您可以使用 `ping` 的 `-p` 选项对其进行测试。

[IPv4 TTL 详细信息](#IPv4_TTL___u8BE6___u7EC6___u4FE1___u606F_)
===========================================================

IP 数据包的 TTL 值表示数据包在被丢弃之前可以通过的 IP 路由器的最大数量。 在当前实践中，您可以期望 Internet 中的每个路由器都将 TTL 字段减一。

TCP/IP 规范建议将 IP 数据包的 TTL 字段设置为 64，但许多系统使用较小的值 (4.3BSD 使用 30, 4.2BSD 使用 15)。

该字段的最大可能值为 255，大多数 UNIX 系统将 ICMP ECHO\_REQUEST 数据包的 TTL 字段设置为 255。 这就是为什么您会发现您可以 “ping” 一些主机，但无法使用 telnet(1) 或 ftp(1) 访问它们。

在正常操作中， `ping` 它收到的数据包中打印出 ttl 值。 当远程系统接收到 ping 数据包时，它可以在响应中使用 TTL 字段执行以下三种操作之一：

*   不改变它；这是 BSD 系统在 4.3BSD-Tahoe 发布之前所做的。 在这种情况下，接收到的数据包中的 TTL 值将是 255 减去往返路径中的路由器数量。
*   将其设置为 255；这就是当前 BSD 系统所做的。 在这种情况下，接收到的数据包中的 TTL 值将是 255 减去 _from_ 远程系统 _to_ `ping`_ing_ 主机的路径中的路由器数量。
*   将其设置为其他值。 有些机器对 ICMP 数据包使用与 TCP 数据包相同的值，例如 30 或 60。 其他人可能会使用完全疯狂的值。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

`ping` 实用程序以下列值之一退出：

0

至少从指定的 host 听到了一个响应。

2

传输成功，但未收到任何响应。

any other value

发生错误。

[实例](#__u5B9E___u4F8B_)
=======================

以下将向 `dst.foo.com` 发送 ICMPv6 回显请求。

ping -6 -n dst.foo.com 

以下将探测连接到 `wi0` 接口的网络链接上所有节点的主机名。 地址 `ff02::1` 被命名为链路本地全节点多播地址，数据包将到达网络链路上的每个节点。

ping -6 -y ff02::1%wi0 

下面将探测分配给目标节点 `dst.foo.com` 的地址。

ping -6 -k agl dst.foo.com 

[参见](#__u53C2___u89C1_)
=======================

netstat(1), icmp(4), icmp6(4), inet6(4), ip6(4), ifconfig(8), routed(8), traceroute(8), traceroute6(8) A. Conta and S. Deering, Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6) Specification, RFC 2463, December 1998. Matt Crawford, IPv6 Node Information Queries, draft-ietf-ipngwg-icmp-name-lookups-09.txt, May 2002, work in progress material.

[历史](#__u5386___u53F2_)
=======================

`ping` 实用程序出现在 4.3BSD 中。 支持 IPv6 的 `ping6` 实用程序首次出现在 WIDE Hydrangea IPv6 协议栈套件中。

基于 KAME 项目 (http://www.kame.net/) 堆栈的 IPv6 和 IPsec 支持最初集成到 FreeBSD 4.0 中。

`ping6` 实用程序已在 Google Summer of Code 2019 中合并到 `ping` 。

[作者](#__u4F5C___u8005_)
=======================

最初的 `ping` 实用程序是由 Mike Muuss 在美国陆军弹道研究实验室编写的。

[缺陷](#__u7F3A___u9677_)
=======================

许多主机和网关忽略 IPv4 RECORD\_ROUTE 选项。

对于像 RECORD\_ROUTE 这样的选项来说，最大 IP 标头长度太小而不能完全有用。 然而，对此无能为力。

一般不建议使用泛洪 ping，并且只能在非常受控的条件下进行泛洪 ping 广播地址。

`-v` 选项在繁忙的主机上没有多大价值。

November 26, 2020

FreeBSD 13.1-RELEASE