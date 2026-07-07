# ping(8)

`ping` — 向网络主机发送 ICMP 或 ICMPv6 ECHO_REQUEST 数据包

## 名称

`ping`

## 概要

`ping [-4AaDdfHnoQqRrv] [-.chars] [-C pcp] [-c count] [-G sweepmaxsize] [-g sweepminsize] [-h sweepincrsize] [-i wait] [-l preload] [-M mask | time] [-m ttl] [-P policy] [-p pattern] [-S src_addr] [-s packetsize] [-t timeout] [-W waittime] [-z tos] IPv4-host` `ping [-4AaDdfHLnoQqRrv] [-.chars] [-C pcp] [-c count] [-I iface] [-i wait] [-l preload] [-M mask | time] [-m ttl] [-P policy] [-p pattern] [-S src_addr] [-s packetsize] [-T ttl] [-t timeout] [-W waittime] [-z tos] IPv4-mcast-group` `ping [-6AaDdEfHNnOoquvYyZ] [-.chars] [-b bufsiz] [-C pcp] [-c count] [-e gateway] [-I interface] [-i wait] [-k addrtype] [-l preload] [-m hoplimit] [-P policy] [-p pattern] [-S sourceaddr] [-s packetsize] [-t timeout] [-W waittime] [IPv6-hops ...] IPv6-host`

## 描述

以 IPv4 目标（`IPv4-host` 或 `IPv4-mcast-group`）调用时，`ping` 工具使用 ICMP 协议的强制 ECHO_REQUEST 数据报来引导主机或网关返回 ICMP ECHO_RESPONSE。ECHO_REQUEST 数据报（"ping"）包含 IP 和 ICMP 头，其后是一个“struct timeval”，然后是用于填充数据包的任意数量的“pad”字节。

以 IPv6 目标（`IPv6-host`）调用时，它使用 ICMPv6 协议的强制 ICMP6_ECHO_REQUEST 数据报来引导返回 ICMP6_ECHO_REPLY。ICMP6_ECHO_REQUEST 数据报包含 IPv6 头和 ICMPv6 头，格式如 RFC 2463 中所述。

以主机名调用时，使用目标首先解析到的版本。在这种情况下，所使用的选项和参数必须对该特定 IP 版本有效，否则 `ping` 将出错退出。如果目标同时解析为 IPv4 和 IPv6，可分别通过 `-4` 或 `-6` 选项请求特定的 IP 版本。为向后兼容，也可以通过以 `ping6` 名字调用该程序来选择 ICMPv6。

### IPv4 和 IPv6 目标的通用选项

```sh
ping -.0123456789 freebsd.org
```

**`-.`** `chars` 默认情况下，每发送一个 ECHO_REQUEST 打印一个句点“.”，而每接收到一个 ECHO_REPLY 打印一个退格符。此选项接受一个可选的字符串参数，列出将按所给顺序逐一打印的字符，以替代默认的句点。示例用法：

**`-A`** 可听提示。在下一个数据包发送之前未收到任何数据包时，输出一个响铃（ASCII 0x07）字符。为适应比发送间隔更长的往返时间，仅当未接收数据包的最大数量增加时，后续丢失的数据包才会触发响铃。

**`-a`** 可听提示。接收到任何数据包时，在输出中包含一个响铃（ASCII 0x07）字符。

**`-C`** `pcp` 发送数据包时添加 802.1p 以太网优先级代码点（Priority Code Point）。0..7 使用该特定 PCP，-1 使用接口默认 PCP（或无）。

**`-c`** `count` 在发送（并接收）`count` 个 ECHO_RESPONSE 数据包后停止。如果未指定此选项，`ping` 将持续运行直至被中断。对于 IPv4 目标，如果此选项与 ping 扫描一起指定，每次扫描将包含 `count` 个数据包。

**`-D`** 禁用分片。

**`-d`** 在所使用的套接字上设置 `SO_DEBUG` 选项。

**`-f`** 洪泛 ping。以数据包返回的速度或每秒一百次（取较大者）输出数据包。隐含 `-.`，即为每个发送的 ECHO_REQUEST 打印句点，为每个接收到的 ECHO_REPLY 打印退格符。这提供了有多少数据包被丢弃的快速显示。仅超级用户可使用此选项。这可能对网络造成很大负担，应谨慎使用。

**`-H`** 主机名输出。显示地址时尝试进行反向 DNS 查询。这与 `-n` 选项相反。

**`-I`** `iface` 对于 IPv4 目标，`iface` 是标识发送数据包所用接口的 IP 地址。此标志仅在 ping 目标为多播地址时适用。对于 IPv6 目标，`iface` 是发送数据包所用接口的名称（例如 `em0`）。此标志在 ping 目标为多播地址或链路本地/站点本地单播地址时适用。

**`-i`** `wait` 在 *每次发送数据包之间* 等待 `wait` 秒。默认为每个数据包之间等待 1 秒。等待时间可以是小数，但仅超级用户可指定小于 1 秒的值。此选项与 `-f` 选项不兼容。

**`-l`** `preload` 如果指定了 `preload`，`ping` 会在进入正常行为模式之前尽快发送那么多数据包。仅超级用户可使用此选项。

**`-m`** `ttl` 对于 IPv4 目标，设置传出数据包的 IP 生存时间（Time To Live）。如果未指定，内核使用 `net.inet.ip.ttl` MIB 变量的值。对于 IPv6 目标，设置 IPv6 跳数限制。

**`-n`** 仅数字输出。不尝试查找主机地址的符号名称。这与 `-H` 相反，并且是默认行为。

**`-o`** 接收到一个回复数据包后成功退出。

**`-P`** `policy` `policy` 为 ping 会话指定 IPsec 策略。详情请参见 [ipsec(4)](../man4/ipsec.4.md) 和 ipsec_set_policy(3)。

**`-p`** `pattern` 你最多可以指定 16 个“pad”字节来填充所发送的数据包。这有助于诊断网络中依赖于数据的问题。例如，“`-p ff`”将使发送的数据包被全 1 填充。

**`-q`** 静默输出。除启动时和完成时的摘要行外，不显示任何内容。

**`-S`** `src_addr` 使用以下 IP 地址作为传出数据包的源地址。在具有多个 IP 地址的主机上，此选项可用于强制将源地址设为探测数据包发送接口的 IP 地址以外的其他地址。对于 IPv4，如果该 IP 地址不是本机接口地址之一，将返回错误且不发送任何内容。对于 IPv6，源地址必须是发送节点的单播地址之一，且必须为数字形式。

**`-s`** `packetsize` 指定要发送的数据字节数。默认为 56，与 8 字节的 ICMP 头数据合并后转换为 64 字节的 ICMP 数据。对于 IPv4，仅超级用户可指定超过默认值的值。此选项不能与 ping 扫描一起使用。对于 IPv6，你可能还需要指定 `-b` 以扩展套接字缓冲区大小。

**`-t`** `timeout` 指定超时时间（秒），无论已接收到多少数据包，ping 都将在超时后退出。

**`-v`** 详细输出。列出接收到的 ECHO_RESPONSE 以外的 ICMP 数据包。

**`-W`** `waittime` 为每个发送的数据包等待回复的时间（毫秒）。如果回复稍后到达，该数据包不会显示为已回复，但在计算统计信息时会视为已回复。

### 仅适用于 IPv4 目标的选项

**`-4`** 无论目标如何解析，均使用 IPv4。

**`-G`** `sweepmaxsize` 指定发送扫描 ping 时 ICMP 负载的最大大小。ping 扫描需要此选项。

**`-g`** `sweepminsize` 指定发送扫描 ping 时起始 ICMP 负载的大小。默认值为 0。

**`-h`** `sweepincrsize` 指定发送扫描 ping 时每次扫描后 ICMP 负载大小的递增字节数。默认值为 1。

**`-L`** 抑制多播数据包的环回。此标志仅在 ping 目标为多播地址时适用。

**`-M`** `mask | time` 使用 `ICMP_MASKREQ` 或 `ICMP_TSTAMP` 替代 `ICMP_ECHO`。对于 `mask`，打印远程机器的网络掩码。设置 `net.inet.icmp.maskrepl` MIB 变量以启用 `ICMP_MASKREPLY`，如需覆盖响应中的网络掩码则设置 `net.inet.icmp.maskfake`。对于 `time`，打印发起、接收和传输时间戳。设置 `net.inet.icmp.tstamprepl` MIB 变量以启用或禁用 `ICMP_TSTAMPREPLY`。

**`-Q`** 略微静默输出。不显示响应我们查询消息的 ICMP 错误消息。最初需要 `-v` 标志来显示此类错误，但 `-v` 会显示所有 ICMP 错误消息。在繁忙的机器上，此输出可能过于繁杂。未指定 `-Q` 标志时，`ping` 会打印由其自身 ECHO_REQUEST 消息引起的任何 ICMP 错误消息。

**`-R`** 记录路由。在 ECHO_REQUEST 数据包中包含 RECORD_ROUTE 选项，并在返回的数据包上显示路由缓冲区。注意，IP 头仅足够容纳九个此类路由；traceroute(8) 命令通常更能确定数据包到达特定目的地所走的路由。如果返回的路由多于应有数量（例如由于非法伪造的数据包），ping 将打印路由列表，然后在正确的位置截断。许多主机忽略或丢弃 RECORD_ROUTE 选项。

**`-r`** 绕过正常的路由表，直接发送给所连接网络上的主机。如果主机不在直接连接的网络上，将返回错误。此选项可用于通过没有路由的接口 ping 本地主机（例如在该接口被 [routed(8)](routed.8.md) 丢弃之后）。

**`-T`** `ttl` 设置多播数据包的 IP 生存时间。此标志仅在 ping 目标为多播地址时适用。

**`-z`** `tos` 使用指定的服务类型。

**`IPv4-host`** 最终目标节点的主机名或 IPv4 地址。

**`IPv4-mcast-group`** 最终目标节点的 IPv4 多播地址。

### 仅适用于 IPv6 目标的选项

**`a`** 请求来自响应者所有接口的单播地址。如果省略该字符，则仅请求属于拥有响应者地址的接口的地址。
**`c`** 请求响应者的 IPv4 兼容和 IPv4 映射地址。
**`g`** 请求响应者的全局范围地址。
**`s`** 请求响应者的站点本地地址。
**`l`** 请求响应者的链路本地地址。
**`A`** 请求响应者的任播地址。不带此字符时，响应者将仅返回单播地址。带此字符时，响应者将仅返回任播地址。注意，规范并未说明如何获取响应者的任播地址。这是一个实验性选项。

**`-6`** 无论目标如何解析，均使用 IPv6。

**`-b`** `bufsiz` 设置套接字缓冲区大小。

**`-e`** `gateway` 指定使用 `gateway` 作为通往目标的下一跳。网关必须是发送节点的邻居。

**`-k`** `addrtype` 生成 ICMPv6 节点信息节点地址查询，而非回显请求。`addrtype` 必须是由以下字符构成的字符串。

**`-N`** 探测节点信息多播组地址（`ff02::2:ffxx:xxxx`）。`host` 必须是目标的主机名字符串（不能是数字形式的 IPv6 地址）。节点信息多播组将根据给定的 `host` 计算，并用作最终目标。由于节点信息多播组是链路本地多播组，需要通过 `-I` 选项指定传出接口。指定两次时，改用地址（`ff02::2:xxxx:xxxx`）。前者见于 RFC 4620，后者见于旧 Internet 草案 draft-ietf-ipngwg-icmp-name-lookup。注意，包括 FreeBSD 在内的 KAME 派生实现使用后者。

**`-O`** 生成 ICMPv6 节点信息支持的查询类型查询，而非回显请求。如果指定了 `-O`，`-s` 无效。

**`-u`** 默认情况下，`ping` 要求内核对数据包进行分片以适应最小 IPv6 MTU。`-u` 选项将在以下两个级别上抑制该行为：当选项指定一次时，对单播数据包禁用该行为；当选项指定多次时，对单播和多播数据包均禁用该行为。

**`-Y`** 与 `-y` 相同，但使用基于 03 草案的旧数据包格式。此选项用于向后兼容。如果指定了 `-y`，`-s` 无效。

**`-y`** 生成 ICMPv6 节点信息 DNS 名称查询，而非回显请求。如果指定了 `-y`，`-s` 无效。

**`IPv6-hops`** 中间节点的 IPv6 地址，将放入类型 0 路由头中。

**`IPv6-host`** 最终目标节点的 IPv6 地址。

### 仅适用于 IPv6 目标的实验性选项

**`-E`** 启用传输模式 IPsec 封装安全载荷。

**`-Z`** 启用传输模式 IPsec 认证头。

使用 `ping` 进行故障隔离时，应首先在本地主机上运行，以验证本地网络接口是否正常工作。然后，应对越来越远的主机和网关进行“ping”。系统会计算往返时间和丢包统计信息。如果接收到重复数据包，它们不计入丢包计算，但这些数据包的往返时间会用于计算往返时间统计信息。当已发送（并接收）指定数量的数据包，或程序被 `SIGINT` 终止时，将显示简要摘要，包括发送和接收的数据包数量，以及往返时间的最小值、平均值、最大值和标准差。

如果 `ping` 接收到 `SIGINFO` 信号（参见 stty(1) 的 `status` 参数），当前已发送和接收的数据包数量，以及往返时间的最小值、平均值、最大值和标准差将被写入标准输出。

此程序用于网络测试、测量和管理。由于它可能给网络带来负载，不建议在正常操作中或从自动化脚本中使用 `ping`。

## ICMP 数据包细节

不含选项的 IP 头为 20 字节。ICMP ECHO_REQUEST 数据包包含额外的 8 字节 ICMP 头，其后是任意数量的数据。当给定 `packetsize` 时，它指示这块额外数据的大小（默认为 56）。因此，ICMP ECHO_REPLY 类型的 IP 数据包内接收到的数据量将始终比所请求的数据空间（ICMP 头）多 8 字节。

如果数据空间至少为 8 字节，`ping` 使用该空间的前 8 字节包含一个时间戳，用于计算往返时间。如果指定的填充少于 8 字节，则不提供往返时间。

## 重复和损坏的数据包

`ping` 工具会报告重复和损坏的数据包。ping 单播地址时不应该出现重复数据包，这似乎是由不当的链路层重传引起的。重复可能在许多情况下出现，且很少（如果有的话）是好兆头，尽管低水平的重复不一定总是引起警报。ping 广播或多播地址时会出现重复，因为它们并非真正的重复，而是不同主机对同一请求的回复。

损坏的数据包显然是引起警报的严重原因，通常表明 `ping` 数据包路径上某处（网络中或主机中）存在损坏的硬件。

## 尝试不同的数据模式

（互连）网络层不应根据数据部分中包含的数据对数据包进行区别对待。不幸的是，已知依赖于数据的问题会潜入网络并长时间未被发现。在许多情况下，会出现问题的特定模式是没有足够“转换”的内容，例如全 1 或全 0，或处于边缘的模式，例如几乎全 0。在命令行上指定全 0（例如）的数据模式不一定足够，因为感兴趣的模式处于数据链路层，而你所键入的内容与控制器所传输内容之间的关系可能很复杂。

这意味着，如果你遇到依赖于数据的问题，可能需要进行大量测试才能找到它。如果幸运的话，你可能会找到一个无法通过网络发送或传输时间比其他相似长度文件长得多的文件。然后你可以检查此文件中是否存在重复模式，并使用 `ping` 的 `-p` 选项进行测试。

## IPv4 TTL 细节

IP 数据包的 TTL 值表示数据包在被丢弃前最多可以经过的 IP 路由器数量。在当前实践中，可以预期互联网中的每个路由器将 TTL 字段恰好减一。

TCP/IP 规范建议将 IP 数据包的 TTL 字段设置为 64。

此字段的最大可能值为 255，一些 UNIX 系统将 ICMP ECHO_REQUEST 数据包的 TTL 字段设置为 255。这就是为什么你会发现可以“ping”通某些主机，但无法通过 [telnet(1)](../man1/telnet.1.md) 或 [ftp(1)](../man1/ftp.1.md) 访问它们的原因。

在正常操作中，`ping` 打印所接收数据包的 ttl 值。当远程系统接收到 ping 数据包时，它可以对其响应中的 TTL 字段执行以下三种操作之一：

- 不更改它；这是 BSD 系统在 4.3BSD 版本之前所做的。在这种情况下，接收数据包中的 TTL 值将为 255 减去往返路径上的路由器数量。
- 将其设置为 64；这是当前 FreeBSD 系统所做的。在这种情况下，接收数据包中的 TTL 值将为 64 减去 *从* 远程系统 *到* 执行 `ping` 的主机的路径上的路由器数量。
- 将其设置为其他值。某些机器对 ICMP 数据包使用与 TCP 数据包相同的值，例如 30 或 60。其他机器可能使用完全离奇的值。

## 退出状态

`ping` 工具以以下值之一退出：

**0** 从指定的 `host` 至少听到一个响应。

**2** 传输成功但未收到任何响应。

**任何其他值** 发生错误。

## 实例

以下命令将向 `dst.example.com` 发送 ICMPv6 回显请求。

```sh
ping -6 -n dst.example.com
```

以下命令将探测连接到 `wi0` 接口的网络链路上所有节点的主机名。地址 **ff02::1** 称为链路本地所有节点多播地址，该数据包将到达网络链路上的每个节点。

```sh
ping -6 -y ff02::1%wi0
```

以下命令将探测分配给目标节点 `dst.example.com` 的地址。

```sh
ping -6 -k agl dst.example.com
```

## 参见

[netstat(1)](../man1/netstat.1.md), [icmp(4)](../man4/icmp.4.md), [icmp6(4)](../man4/icmp6.4.md), [inet6(4)](../man4/inet6.4.md), [ip6(4)](../man4/ip6.4.md), [ifconfig(8)](ifconfig.8.md), [routed(8)](routed.8.md), traceroute(8), traceroute6(8)

> A. Conta, S. Deering, "Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6) Specification", RFC 2463, December 1998.

> Matt Crawford, "IPv6 Node Information Queries", draft-ietf-ipngwg-icmp-name-lookups-09.txt, May 2002, work in progress material.

## 历史

`ping` 工具出现在 4.3BSD 中。支持 IPv6 的 `ping6` 工具首次出现在 WIDE Hydrangea IPv6 协议栈工具包中。

基于 KAME 项目（`https://www.kame.net/`）栈的 IPv6 和 IPsec 支持最初集成到 FreeBSD 4.0 中。

`ping6` 工具在 2019 年 Google Summer of Code 中被合并到 `ping` 中。

## 作者

原始 `ping` 工具由 Mike Muuss 在美国陆军弹道研究实验室工作时编写。

## 缺陷

许多主机和网关忽略 IPv4 RECORD_ROUTE 选项。

最大 IP 头长度对于 RECORD_ROUTE 等选项而言太小，无法完全发挥作用。然而，对此无能为力。

一般不建议洪泛 ping，洪泛广播地址的 ping 应仅在非常受控的条件下进行。

`-v` 选项在繁忙的主机上意义不大。
