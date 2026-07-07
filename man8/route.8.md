# route(8)

`route` — 手动操作路由表

## 名称

`route`

## 概要

`route [-j jail] [-dnqtv] command [[modifiers] args]`

## 描述

`route` 工具用于手动操作网络路由表。通常不需要使用它，因为系统路由表管理守护进程（如 [routed(8)](routed.8.md)）会负责此项任务。

`route` 工具支持数量有限的一般选项，但拥有丰富的命令语言，使用户能够指定可通过 [route(4)](../man4/route.4.md) 中讨论的编程接口传递的任意请求。

可用选项如下：

**`-4`** 指定 `inet` 地址族作为子命令的地址族提示。

**`-6`** 指定 `inet6` 地址族作为子命令的地址族提示。

**`-d`** 仅在调试模式下运行，即不实际修改路由表。

**`-n`** 在报告操作时，跳过以符号方式打印主机和网络名称的尝试。（在符号名称和数值之间转换的过程可能相当耗时，并且可能需要网络正常运作；因此忘记这一点可能更为实际，特别是在尝试修复网络操作时。）

**`-t`** 仅在测试模式下运行。使用 **/dev/null** 代替套接字。

**`-v`** （详细模式）打印附加细节。

**`-q`** 抑制 `add`、`change`、`delete` 和 `flush` 命令的所有输出。

**`-j`** `jail` 在 jail 中运行。

`route` 工具提供以下命令：

**`add`** 添加路由。
**`flush`** 删除所有路由。
**`delete`** 删除特定路由。
**`del`** `delete` 命令的另一个名称。
**`change`** 更改路由的某些方面（如网关）。
**`get`** 查找并显示到某个目的地的路由。
**`monitor`** 持续报告路由信息库的任何更改、路由查找未命中或可疑的网络分区。
**`show`** `get` 命令的另一个名称。

monitor 命令的语法：

```
route [-n] monitor [-fib number]
```

flush 命令的语法：

```
route [-n] flush [family] [-fib number]
```

如果指定 `flush` 命令，`route` 将“清空”路由表中所有网关条目。当通过 `-inet6` 或 `-inet` 修饰符指定地址族时，仅删除具有该族地址的目的地的路由。此外，`-4` 或 `-6` 可分别用作 `-inet` 和 `-inet6` 修饰符的别名。指定 `-fib` 选项时，操作将应用于指定的 FIB（路由表）。

add 命令的语法：

```
route [-n] add [-net | -host] destination gateway [netmask] [-fib number]
```

其他命令的语法：

```
route [-n] command [-net | -host] destination [gateway [netmask]] [-fib number]
```

其中 `destination` 是目的主机或网络，`gateway` 是数据包应通过其路由的下一跳中介。通过解释作为 `destination` 参数指定的 Internet 地址，可以区分到特定主机的路由和到网络的路由。可选修饰符 `-net` 和 `-host` 分别强制将目的地解释为网络或主机。否则，如果 `destination` 的“本地地址部分”为 `INADDR_ANY`（`0.0.0.0`），或者 `destination` 是网络的符号名称，则假定该路由是到网络的；否则，假定为到主机的路由。此外，`destination` 还可以用 `net`/`bits` 格式指定。

例如，`128.32` 被解释为 `-host` `128.0.0.32`；`128.32.130` 被解释为 `-host` `128.32.0.130`；`-net` `128.32` 被解释为 `128.32.0.0`；`-net` `128.32.130` 被解释为 `128.32.130.0`；`192.168.64/20` 被解释为 `-net` `192.168.64` `-netmask` `255.255.240.0`。

`default` 作为 `destination` 是默认路由的同义词。对于 `IPv4`，它是 `-net` `-inet` `0.0.0.0`；对于 `IPv6`，它是 `-net` `-inet6` `::`。

如果目的地可通过不需要中介系统作为网关的接口直接到达，则应指定 `-interface` 修饰符；给定的网关是此主机在公共网络上的地址，指示用于传输的接口。或者，如果接口是点对点的，则可以给出接口名称本身，在这种情况下，即使本地或远程地址发生变化，路由仍然有效。

可选的 `-netmask` 修饰符旨在实现带 netmask 选项的 OSI ESIS 重定向效果，或手动添加与隐含网络接口掩码不同的子网路由（否则将使用 OSPF 或 ISIS 路由协议进行传递）。需要指定一个额外的后续地址参数（解释为网络掩码）。通过确保此选项跟在 `destination` 参数之后，可以覆盖 AF_INET 情况下生成的隐式网络掩码。

对于 `AF_INET6`，可使用 `-prefixlen` 限定符代替 `-mask` 限定符，因为 IPv6 不允许非连续掩码。例如，`-prefixlen` `32` 指定使用网络掩码 `ffff:ffff:0000:0000:0000:0000:0000:0000`。默认 prefixlen 为 64。但是，如果为 `destination` 指定了 `default`，则假定 prefixlen 为 0。注意，该限定符仅适用于 `AF_INET6` 地址族。

对于 `ECMP` 路由，可使用 `-weight` 修饰符影响下一跳选择。例如，一个具有两个下一跳“`-gateway` `3fff::1` `-weight` `100`”和“`-gateway` `3fff::2` `-weight` `200`”的目的地，会使下一跳 3fff::2 被选中的概率是 3fff::1 的两倍。

`-metric` 选项设置与路由下一跳关联的数值成本。始终优先选择最低 metric，仅在较低 metric 路由不可用时才使用较高 metric 值的路由。这允许路由建立主下一跳和备份下一跳，而无需删除主下一跳。未指定时 `-metric` 的默认值为 1。当到同一目的地的多个路由具有相同 metric 时，`-weight` 选项确定 ECMP 选择哪个下一跳。

例如，一个具有两个下一跳“`-gateway` `3fff::1` `-metric` `1`”和“`-gateway` `3fff::2` `-metric` `2`”的目的地，将导致选择下一跳 3fff::1。

路由具有关联的标志，这些标志影响协议在向路由匹配的目的地发送数据时的操作。可通过指示以下相应修饰符来设置（或有时清除）这些标志：

```
-xresolve  RTF_XRESOLVE   - 使用时发出消息（用于外部查找）
-iface    ~RTF_GATEWAY    - 目的地可直接到达
-static    RTF_STATIC     - 手动添加的路由
-nostatic ~RTF_STATIC     - 假装路由由内核或守护进程添加
-reject    RTF_REJECT     - 匹配时发出 ICMP 不可达
-blackhole RTF_BLACKHOLE  - 静默丢弃数据包（在更新期间）
-proto1    RTF_PROTO1     - 设置协议特定的路由标志 #1
-proto2    RTF_PROTO2     - 设置协议特定的路由标志 #2
```

可选修饰符 `-rtt`、`-rttvar`、`-sendpipe`、`-recvpipe`、`-mtu`、`-hopcount`、`-expire` 和 `-ssthresh` 为传输层协议（如 TCP 或 TP4）在路由条目中维护的量提供初始值。可以通过在每个要锁定的修饰符前加上 `-lock` 元修饰符来单独锁定，也可以使用 `-lockrest` 元修饰符指定锁定所有后续度量值。

注意，`-expire` 接受路由的过期时间，以自 Epoch 以来的秒数表示（参见 time(3)）。当数字的第一个字符为“+”或“-”时，解释为相对于当前时间的值。

可选修饰符 `-fib` `number` 指定命令将应用于非默认 FIB。`number` 必须小于 `net.fibs` [sysctl(8)](sysctl.8.md) MIB。未指定此修饰符或指定负数时，将使用 `net.my_fibnum` [sysctl(8)](sysctl.8.md) MIB 中显示的默认 FIB。

`number` 允许通过逗号分隔列表和/或范围指定多个 FIB。“`-fib` `2,4,6`”表示 FIB 编号 2、4 和 6。“`-fib` `1,3-5,6`”表示 1、3、4、5 和 6。

在 `change` 或 `add` 命令中，当目的地和网关不足以指定路由时（如 ISO 情况下，多个接口可能具有相同地址），可使用 `-ifp` 或 `-ifa` 修饰符来确定接口或接口地址。

为 `destination` 或 `gateway` 指定的所有符号名称首先使用 gethostbyname(3) 作为主机名查找。如果此查找失败，则使用 getnetbyname(3) 将名称解释为网络名。

`route` 工具使用路由套接字和新的消息类型 `RTM_ADD`、`RTM_DELETE`、`RTM_GET` 和 `RTM_CHANGE`。因此，仅超级用户可修改路由表。

FreeBSD 提供对可扩展多路径路由的支持。默认激活，但可通过将 `net.route.multipath` [sysctl(8)](sysctl.8.md) MIB 设置为 0 来关闭。

有多种可用的路由查找算法。可通过设置 IPv4 的 `net.route.algo.inet.algo` 和 IPv6 的 `net.route.algo.inet6.algo` [sysctl(8)](sysctl.8.md) MIB 来配置。

可通过访问以下 [sysctl(8)](sysctl.8.md) MIB 获取可用算法列表：IPv4 的 `net.route.algo.inet.algo_list` 和 IPv6 的 `net.route.algo.inet6.algo_list`。

可用算法如下：

**radix** 基本系统 radix 后端。

**bsearch** 在特殊 IP 数组中的无锁二分搜索，专为少于 16 条路由的小型 FIB 量身定制。此算法仅适用于 IPv4。

**radix_lockless** 无锁不可变 radix，在每次 rtable 更改时重新创建，专为少于 1000 条路由的小型 FIB 量身定制。

**dpdk_lpm** 基于 DPDK DIR24-8 的查找，无锁数据结构，针对大型 FIB 优化。DIR24-8 依赖一个大型平面查找表（IPv4 为 64 MB），通过查找键的较高有效部分直接索引。要使用 dpdk_lpm 算法，必须通过 loader.conf(5) 加载以下一个或两个内核模块：

- `dpdk_lpm4.ko` DPDK 的 IPv4 实现。
- `dpdk_lpm6.ko` DPDK 的 IPv6 实现。

**dxr** 仅适用于 IPv4，无锁压缩查找结构（对于大型 BGP FIB，每个 IPv4 前缀低于 2.5 字节），可轻松适应现代 CPU 缓存层次结构，查找吞吐量随 CPU 核心数线性扩展。可在运行时作为内核模块加载，或通过 loader.conf(5) 加载：

- `fib_dxr.ko`

算法根据系统路由表的大小自动选择。可以更改，但并非每种算法在每种 FIB 大小下都表现最佳。

## 退出状态

`route` 工具成功时退出代码为 0，发生错误时大于 0。

## 实例

向网络路由表添加默认路由。这会将路由表中不可用的目的地的所有数据包发送到默认网关 192.168.1.1：

```sh
route add -net 0.0.0.0/0 192.168.1.1
```

添加默认路由的更简短写法：

```sh
route add default 192.168.1.1
```

通过 172.16.1.1 网关向 172.16.10.0/24 网络添加静态路由：

```sh
route add -net 172.16.10.0/24 172.16.1.1
```

更改路由表中已建立的静态路由的网关：

```sh
route change -net 172.16.10.0/24 172.16.1.2
```

显示到目的地网络的路由：

```sh
route show 172.16.10.0
```

从路由表中删除静态路由：

```sh
route delete -net 172.16.10.0/24 172.16.1.2
```

从路由表中删除所有路由：

```sh
route flush
```

可使用 [netstat(1)](../man1/netstat.1.md) 列出路由表。

## 诊断

- `add [host | network ] %s: gateway %s flags %x` 指定的路由正在被添加到表中。打印的值来自 ioctl(2) 调用中提供的路由表条目。如果使用的网关地址不是该网关的主地址（gethostbyname(3) 返回的第一个地址），则网关地址会以数字和符号两种形式打印。
- `delete [ host | network ] %s: gateway %s flags %x` 同上，但用于删除条目时。
- `%s %s done` 指定 `flush` 命令时，每个被删除的路由表条目以此形式的消息指示。
- `Network is unreachable` 添加路由的尝试失败，因为列出的网关不在直接连接的网络上。必须提供下一跳网关。
- `not in table` 尝试对表中不存在的条目执行删除操作。
- `routing table overflow` 尝试执行添加操作，但系统资源不足，无法分配内存来创建新条目。
- `gateway uses the same route` `change` 操作导致路由的网关使用与被更改路由相同的路由。下一跳网关应通过不同的路由可达。

## 参见

[netstat(1)](../man1/netstat.1.md), [netintro(4)](../man4/netintro.4.md), [route(4)](../man4/route.4.md), loader.conf(5), arp(8), [routed(8)](routed.8.md)

## 历史

`route` 工具出现于 4.2BSD。
