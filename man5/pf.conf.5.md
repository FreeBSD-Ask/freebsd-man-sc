# pf.conf(5)

`pf.conf` — 包过滤器配置文件

## 名称

`pf.conf`

## 描述

[pf(4)](../man4/pf.4.md) 包过滤器根据 `pf.conf` 中指定的规则或定义来修改、丢弃或通过数据包。

## 语句顺序

`pf.conf` 中有八种类型的语句：

**`Macros`** 用户定义的变量可以定义后稍后使用，简化配置文件。宏必须在 `pf.conf` 中被引用之前定义。

**`Tables`** 表提供了一种机制，用于提高具有大量源或目标地址的规则的性能和灵活性。

**`Options`** 选项调整包过滤引擎的行为。

**`Ethernet Filtering`** 以太网过滤提供基于规则的以太网数据包阻止或通过。

**`Traffic Normalization`** `（例如` *scrub)* 流量规范化保护内部机器免受 Internet 协议和实现中的不一致性的影响。

**`Queueing`** 排队提供基于规则的带宽控制。

**`Translation`** `（各种形式的 NAT）` 转换规则指定如何将地址映射或重定向到其他地址。

**`Packet Filtering`** 包过滤提供基于规则的数据包阻止或通过。

除 `macros` 和 `tables` 外，各类语句应按上述顺序分组并出现在 `pf.conf` 中，这与底层包过滤引擎的操作相匹配。默认情况下，pfctl(8) 强制执行此顺序（参见下文的 `set require-order`）。

可以在文件中任何位置使用井号（‘#’）添加注释，并延伸到当前行尾。

可以使用 `include` 关键字包含其他配置文件，例如：

```sh
include "/etc/pf/sub.filter.conf"
```

## 宏

宏通过 `name`=`value` 形式的命令定义。宏 `name` 可以包含字母、数字和下划线，且不能是保留字（例如 `pass`、`in` 或 `out`）。在未加引号的参数中，字符串 $`name` 稍后会被展开为 `value`。在宏中使用且稍后将在列表中展开的网络地址范围必须用额外的单引号引起来。

例如，

```sh
ext_if = "kue0"
all_ifs = "{" $ext_if lo0 "}"
pass out on $ext_if from any to any
pass in  on $ext_if proto tcp from any to any port 25
usr_lan_range = "'192.0.2.0/24'"
srv_lan_range = "'198.51.100.0 - 198.51.100.255'"
nat_ranges = "{" $usr_lan_range $srv_lan_range "}"
nat on $ext_if from $nat_ranges to any -> ($ext_if)
```

## 表

表是命名的结构，可以保存一组地址和网络。在 [pf(4)](../man4/pf.4.md) 中对表的查找相对较快，使得在处理器使用率和内存消耗方面，使用表的单条规则比大量仅在 IP 地址上不同的规则（无论是显式创建还是通过规则展开自动创建）要高效得多。

表可用作过滤规则、`scrub` 规则或转换规则（如 `nat` 或 `rdr`）的源或目标（有关各种规则类型的详细信息，请参见下文）。表还可用于 `nat` 和 `rdr` 的重定向地址以及过滤规则的路由选项，但不能用于 `bitmask` 池。

表可以通过以下任何 pfctl(8) 机制来定义。与宏一样，保留字不能用作表名。

**`manually`** 持久表可以使用 pfctl(8) 的 `add` 或 `replace` 选项手动创建，可在规则集加载之前或之后。

**`pf.conf`** 表定义可以直接放在此文件中，与其他规则同时原子地加载。`pf.conf` 内的表定义使用 `table` 语句，对于定义非持久表特别有用。在加载 `pf.conf` 时，不带地址列表初始化的预存在表的内容不会被更改。使用空列表 `{ }` 初始化的表将在加载时被清空。

表可以使用以下属性定义：

**`persist`** `persist` 标志强制内核在没有规则引用表时仍保留该表。如果未设置此标志，当引用该表的最后一条规则被刷新时，内核将自动删除该表。

**`const`** `const` 标志防止用户在表创建后更改其内容。如果没有此标志，pfctl(8) 可用于随时向表添加或删除地址，即使在 securelevel(7) = 2 的情况下运行也是如此。

**`counters`** `counters` 标志启用每地址的数据包和字节计数器，可通过 pfctl(8) 显示。注意，此功能对于大型表会带来显著的内存开销。

例如，

```sh
table <private> const { 10/8, 172.16/12, 192.168/16 }
table <badhosts> persist
block on fxp0 from { <private>, <badhosts> } to any
```

创建一个名为 private 的表来保存 RFC 1918 私有网络块，以及一个名为 badhosts 的表，初始为空。设置了一条过滤规则来阻止来自任一表中列出的地址的所有流量。private 表无法更改其内容，而 badhosts 表即使在没有活动过滤规则引用它时也将存在。稍后可以向 badhosts 表添加地址，以便使用以下命令阻止来自这些主机的流量

```sh
# pfctl -t badhosts -Tadd 204.92.77.111
```

表还可以使用以下语法，用在一个或多个外部文件中指定的地址列表来初始化：

```sh
table <spam> persist file "/etc/spammers" file "/etc/openrelays"
block on fxp0 from <spam> to any
```

文件 **/etc/spammers** 和 **/etc/openrelays** 列出 IP 地址，每行一个。任何以 # 开头的行都被视为注释并被忽略。除了通过 IP 地址指定外，主机还可以通过其主机名指定。当调用解析器将主机名添加到表时，*所有* 生成的 IPv4 和 IPv6 地址都会被放入表中。还可以通过指定有效的接口名、有效的接口组或 *self* 关键字将 IP 地址输入到表中，在这种情况下，分配给该接口的所有地址都将被添加到表中。

## 选项

可以使用 `set` 命令针对各种情况调整 [pf(4)](../man4/pf.4.md)。

**`interval`** 清除过期状态和分片之间的间隔。

**`frag`** 未组装分片过期前的秒数。

**`src.track`** 在最后一条状态过期后保留源跟踪条目的时间长度。

**`tcp.first`** 第一个数据包后的状态。

**`tcp.opening`** 第二个数据包之后但两端都确认连接之前的状态。

**`tcp.tsdiff`** 符合 RFC 1323 的数据包时间戳之间允许的最大时间差。默认 30 秒。

**`tcp.established`** 完全建立的状态。

**`tcp.closing`** 发送第一个 FIN 后的状态。

**`tcp.finwait`** 双方都交换 FIN 且连接关闭后的状态。某些主机（尤其是 Solaris 上的 Web 服务器）在关闭连接后仍会发送 TCP 数据包。增加 `tcp.finwait`（可能还有 `tcp.closing`）可以防止此类数据包被阻止。

**`tcp.closed`** 一端发送 RST 后的状态。

**`sctp.first`** 第一个数据包后的状态。

**`sctp.opening`** 目标主机发送数据包之前的状态。

**`sctp.established`** 完全建立的状态。

**`sctp.closing`** 发送第一个 SHUTDOWN 块后的状态。

**`sctp.closed`** 交换 SHUTDOWN_ACK 且连接关闭后的状态。

**`udp.first`** 第一个数据包后的状态。

**`udp.single`** 源主机发送多个数据包但目标主机从未发送回数据包的状态。

**`udp.multiple`** 双方都已发送数据包的状态。

**`icmp.first`** 第一个数据包后的状态。

**`icmp.error`** 响应 ICMP 数据包返回 ICMP 错误后的状态。

**`other.first`**

**`other.single`**

**`other.multiple`**

**`adaptive.start`** 当状态条目数超过此值时，开始自适应缩放。所有超时值按因子（adaptive.end - 状态数）/（adaptive.end - adaptive.start）线性缩放。

**`adaptive.end`** 当达到此状态条目数时，所有超时值变为零，有效地立即清除所有状态条目。此值用于定义比例因子，不应实际达到（设置较低的状态限制，见下文）。

```sh
set timeout tcp.first 120
set timeout tcp.established 86400
set timeout { adaptive.start 60000, adaptive.end 120000 }
set limit states 100000
```

```sh
# pfctl -s info
```

```sh
set loginterface dc0
```

```sh
set loginterface none
```

**`states`** 设置状态表条目使用的内存池中的最大条目数（由不指定 `no state` 的 `pass` 规则生成的那些）。默认为 100000。

**`src-nodes`** 设置用于跟踪源 IP 地址的内存池中的最大条目数（由 `sticky-address` 和 `src.track` 选项生成）。默认为 10000。

**`table-entries`** 设置表中可存储的地址数。默认为 200000。

**`anchors`** 设置可存在的锚点数。默认为 512。

**`eth-anchors`** 设置可存在的锚点数。默认为 512。

```sh
set limit { states 20000, frags 2000, src-nodes 2000 }
```

- 删除重复规则
- 删除作为另一条规则子集的规则
- 在有利时将多条规则合并到一个表中
- 重新排序规则以提高评估性能

**`none`** 禁用规则集优化器。

**`basic`** 启用基本规则集优化。这是默认行为。基本规则集优化执行四项操作以提高规则集评估的性能：

**`profile`** 使用当前加载的规则集作为反馈配置文件，根据实际网络流量调整快速规则的顺序。

**`normal`** 正常网络环境。适用于几乎所有网络。

**`high-latency`** 高延迟环境（如卫星连接）。

**`satellite`** `high-latency` 的别名。

**`aggressive`** 激进地使连接过期。这可以大大减少防火墙的内存使用，但代价是过早丢弃空闲连接。

**`conservative`** 极其保守的设置。以更大的内存利用率（在繁忙网络上可能大得多）和略微增加的处理器利用率为代价，避免丢弃合法连接。

```sh
set optimization aggressive
```

**`drop`** 数据包被静默丢弃。

**`return`** 对被阻止的 TCP 数据包返回 TCP RST，对被阻止的 SCTP 数据包返回 SCTP ABORT 块，对被阻止的 UDP 数据包返回 ICMP UNREACHABLE，所有其他数据包被静默丢弃。

```sh
set block-policy return
```

**`drop`** 入站数据包被静默丢弃。

**`return`** 入站数据包被丢弃，对 TCP 数据包返回 TCP RST，对被阻止的 SCTP 数据包返回 SCTP ABORT 块，对 UDP 数据包返回 ICMP UNREACHABLE，对其他数据包不发送响应。

```sh
set fail-policy return
```

**`if-bound`** 状态绑定到接口。

**`floating`** 状态可以匹配任何接口上的数据包（默认）。

```sh
set state-policy if-bound
```

```sh
set syncookies adaptive (start 25%, end 12%)
```

**`never`** pf 永不发送 syncookie SYNACK（默认）。

**`always`** pf 始终发送 syncookie SYNACK。

**`adaptive`** 当状态表的给定百分比被半开 TCP 连接（即那些看到初始 SYN 但未完成三次握手的连接）耗尽时，pf 将启用 syncookie 模式。进入和离开 syncookie 模式的阈值可以使用

```sh
set state-defaults no-sync
```

```sh
set hostid 1
```

```sh
set fingerprints "/etc/pf.os.devel"
```

```sh
set skip on lo0
```

**`none`** 不生成调试消息。

**`urgent`** 仅针对严重错误生成调试消息。

**`misc`** 针对各种错误生成调试消息。

**`loud`** 针对常见情况生成调试消息。

**`set timeout`** 当数据包匹配有状态连接时，连接的生存秒数将更新为与连接状态对应的 `proto.modifier` 的值。匹配此状态的每个数据包都会重置 TTL。调整这些值可能会提高防火墙的性能，但有丢弃有效空闲连接的风险。或者，可以使用 `set optimization`（见上文）以适合特定环境的方式集体调整这些值。SCTP 超时的处理类似于 TCP，但有自己的一组状态：ICMP 和 UDP 的处理方式类似于 TCP，但状态集更有限：其他协议的处理类似于 UDP：随着状态表条目数的增长，超时值可以自适应减少。默认情况下启用自适应超时，adaptive.start 值等于状态限制的 60%，adaptive.end 值等于状态限制的 120%。可以通过将 adaptive.start 和 adaptive.end 都设置为 0 来禁用它们。自适应超时值可以全局定义，也可以为每条规则定义。在每条规则上使用时，这些值与该规则创建的状态数有关；否则与总状态数有关。例如：有 90000 个状态表条目时，超时值缩放为 50%（tcp.first 60，tcp.established 43200）。

**`set loginterface`** 启用为给定接口或接口组收集数据包和字节计数统计信息。这些统计信息可以使用在此示例中，[pf(4)](../man4/pf.4.md) 在名为 dc0 的接口上收集统计信息：可以使用以下命令禁用 loginterface：

**`set limit`** 设置包过滤器使用的内存池的硬限制。有关内存池的解释，请参见 [zone(9)](../man9/zone.9.md)。可以设置以下限制：多个限制可以合并在一行上：

**`set ruleset-optimization`** 重要的是要注意，规则集优化器会修改规则集以提高性能。规则集修改的一个副作用是每条规则的记账统计将具有与以前不同的含义。如果每条规则记账对于计费或其他目的很重要，则不应使用规则集优化器，或者应在所有记账规则中添加标签字段作为优化屏障。优化也可以作为 pfctl(8) 的命令行参数设置，覆盖 `pf.conf` 中的设置。

**`set optimization`** 为以下网络环境之一优化状态超时：例如：

**`set reassemble yes | no`** [`no-df`] `reassemble` 选项用于启用或禁用分片数据包的重组，可设置为 `yes` 或 `no`。如果还指定了 `no-df`，则设置了 “dont-fragment” 位的分片也会被重组，而不是被丢弃；重组后的数据包将清除 “dont-fragment” 位。默认值为 `no`。如果存在 FreeBSD 14 之前的 `scrub` 规则，则忽略此选项。

**`set block-policy`** `block-policy` 选项设置数据包 `block` 操作的默认行为：默认值为 `drop`。例如：

**`set fail-policy`** `fail-policy` 选项设置应该通过数据包但无法通过的规则的行为。当 nat 或 route-to 规则使用空表作为目标列表，或者规则无法创建状态或源节点时，可能会发生这种情况。可能的 `block` 操作如下：例如：

**`set state-policy`** `state-policy` 选项设置状态的默认行为：例如：

**`set syncookies never | always | adaptive`** 当 `syncookies` 激活时，pf 将使用 syncookie SYNACK 应答每个传入的 TCP SYN，而不分配任何资源。在收到客户端对 syncookie SYNACK 的 ACK 响应后，pf 将评估规则集，如果规则集允许则创建状态，与目标主机完成三次握手，并在 synproxy 就位的情况下继续连接。这使 pf 能够抵御大型 synflood 攻击，否则这些攻击会使状态表达到其限制。由于对每个传入 SYN 的盲目应答，syncookies 共享 synproxy 的注意事项，即似乎接受稍后将丢弃的连接。

**`set state-defaults`** `state-defaults` 选项为没有显式 `keep state` 的规则创建的状态设置状态选项。例如：

**`set hostid`** 32 位 `hostid` 向 [pfsync(4)](../man4/pfsync.4.md) 故障转移集群中的其他防火墙标识此防火墙的状态表条目。默认情况下，hostid 设置为伪随机值，但可能需要手动配置它，例如更容易地识别状态表条目的来源。hostid 可以用十进制或十六进制指定。

**`set require-order`** 默认情况下，pfctl(8) 强制规则集中语句类型的顺序为：*options,* *normalization,* *queueing,* *translation,* *filtering.* 将此选项设置为 `no` 可禁用此强制。无序规则集可能存在重要且不明显的隐患。在禁用顺序强制之前请仔细考虑。

**`set fingerprints`** 从给定文件名加载已知操作系统的指纹。默认情况下，已知操作系统的指纹自动从 **/etc** 中的 [pf.os(5)](pf.os.5.md) 加载，但可以通过此选项覆盖。设置此选项可能会留下短暂的时间段，在此期间当前活动规则集引用的指纹与新规则集完成加载之前不一致。指纹的默认位置是 **/etc/pf.os**。例如：

**`set skip on`** <`ifspec`> 列出不应过滤数据包的接口。在此类接口上进出的数据包就像 pf 被禁用一样通过，即 pf 不会以任何方式处理它们。这在回环和其他虚拟接口上很有用，当不需要包过滤时，可能会有意外效果。例如：

**`set debug`** 将调试 `level` 设置为以下之一：

**`set keepcounters`** 在规则更新时保留规则计数器。通常在每次更新规则集时将规则计数器重置为零。设置 `keepcounters` 后，pf 将尝试在旧规则集和新规则集之间找到匹配的规则并保留规则计数器。

## 以太网过滤

[pf(4)](../man4/pf.4.md) 能够根据其以太网（第 2 层）头的属性 `block` 和 `pass` 数据包。

每次包过滤器处理的数据包进入或离开接口时，过滤规则按顺序从第一条到最后一条进行评估。最后匹配的规则决定采取什么操作。如果没有规则匹配该数据包，默认操作是不创建状态地通过该数据包。

以下操作可在过滤器中使用：

**`block`** 数据包被阻止。与第 3 层流量不同，数据包始终被静默丢弃。

**`pass`** 数据包通过；不为第 2 层流量创建状态。

### 适用于第 2 层规则的参数

规则参数指定规则适用于哪些数据包。数据包总是从某个接口进入或通过某个接口离开。大多数参数是可选的。如果指定了参数，则该规则仅适用于具有匹配属性的数据包。某些参数的匹配可以使用 `!` 运算符反转。某些参数可以表示为列表，在这种情况下，pfctl(8) 会生成所有需要的规则组合。

**`in`** 或 `out` 此规则适用于传入或传出数据包。如果未指定 `in` 或 `out`，规则将匹配双向数据包。

**`quick`** 如果数据包匹配设置了 `quick` 选项的规则，此规则被视为最后匹配的规则，并跳过对后续规则的评估。

**`on`** <`ifspec`> 此规则仅适用于从该特定接口或接口组进入或离开的数据包。有关接口组的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md) 中的 `group` 关键字。`any` 将匹配除回环接口外的任何现有接口。

**`bridge-to`** <interface> 匹配此规则的数据包将从指定接口发出，无需进一步处理。

**`proto`** <`protocol`> 此规则仅适用于此协议的数据包。注意，以太网协议号与 [ip(4)](../man4/ip.4.md) 和 [ip6(4)](../man4/ip6.4.md) 中使用的不同。

**Xo** `from` <`source`> `to` <`dest`> Xc 此规则仅适用于具有指定源和目标 MAC 地址的数据包。

**Xo** `queue` <`queue`> Xc 匹配此规则的数据包将分配到指定队列。设置详情请参见 Sx QUEUEING。

**`tag`** <`string`> 匹配此规则的数据包将用指定字符串标记。标记充当内部标记，可用于稍后识别这些数据包。例如，这可用于在接口之间提供信任，以及确定数据包是否已被转换规则处理。标记是 “粘性的”，意味着即使该规则不是最后匹配的规则，数据包也将被标记。进一步的匹配规则可以用新标记替换标记，但不会删除之前应用的标记。一个数据包一次只能分配一个标记。

**`tagged`** <`string`> 用于指定数据包必须已经用给定标记标记才能匹配规则。也可以通过在 tagged 关键字之前指定 ! 运算符来进行反向标记匹配。

## 流量规范化

流量规范化是一个广义的统称，涵盖包过滤器中处理验证数据包、数据包分片、欺骗流量和其他异常情况的各个方面。

### Scrub

Scrub 涉及以消除接收方数据包解释中的歧义的方式清理数据包内容。它通过 `scrub` 选项调用，添加到过滤规则中。

参数在括号中指定。必须至少指定以下参数之一：

**ttl** 不允许连接的任一方减少其 IP TTL。攻击者可能发送这样的数据包，使其到达防火墙、影响防火墙状态，并在到达目标主机之前过期。`reassemble tcp` 会将所有数据包的 TTL 提升到连接上看到的最高值。

**timestamp** 调制 现代 TCP 栈会在每个 TCP 数据包上发送时间戳，并将另一端的时间戳回显给它们。许多操作系统在首次启动时仅从零开始时间戳，并每秒递增几次。可以通过读取时间戳并乘以常数来推断主机的正常运行时间。此外，观察几个不同的时间戳可用于统计 NAT 设备后面的主机数。向连接中欺骗 TCP 数据包需要知道或猜测有效的时间戳。时间戳只需单调递增，不源自可猜测的基准时间。`reassemble tcp` 会使 `scrub` 用随机数调制 TCP 时间戳。

**extended** PAWS 检查 在长肥管道上 TCP 存在一个问题，即数据包可能被延迟的时间超过连接绕过其 32 位序列空间所需的时间。在这种情况下，旧数据包将无法与新数据包区分，并会被当作新数据包接受。解决此问题的方法称为 PAWS：防止序列号回绕。它通过确保每个数据包上的时间戳不会倒退来防止此类情况。`reassemble tcp` 还确保数据包上的时间戳不会超过 RFC 允许的值。通过这样做，当主机使用适当随机化的时间戳时，[pf(4)](../man4/pf.4.md) 人为地将 TCP 序列号的安全性扩展了 10 到 18 位，因为盲目攻击者还必须猜测时间戳。

**`no-df`** 从匹配的 IP 数据包中清除 `dont-fragment` 位。已知某些操作系统会生成设置了 `dont-fragment` 位的分片数据包。NFS 尤其如此。除非指定了 `no-df`，否则 `Scrub` 将丢弃此类分片的 `dont-fragment` 数据包。不幸的是，某些操作系统还生成 IP 标识字段为零的 `dont-fragment` 数据包。如果上游路由器稍后对数据包进行分片，则清除 IP ID 为零的数据包上的 `dont-fragment` 位可能会导致不良结果。建议将 `random-id` 修饰符（见下文）与 `no-df` 修饰符结合使用，以确保唯一的 IP 标识符。

**`min-ttl`** <`number`> 对匹配的 IP 数据包强制执行最小 TTL。

**`max-mss`** <`number`> 将 TCP SYN 数据包上的最大段大小（MSS）减少到不大于 `number`。在 TCP 连接的两个端点无法承载相似大小数据包的情况下，有时需要这样做，由此产生的不匹配可能导致数据包分片或丢失。注意，以这种方式设置 MSS 可能会有不良影响，例如干扰 [pf(4)](../man4/pf.4.md) 的 OS 检测功能。

**Xo** `set-tos` <`string`> *(Ba <`number`> Xc 对匹配的 IP 数据包强制执行 *TOS*。*TOS* 可以作为 `critical`、`inetcontrol`、`lowdelay`、`netcontrol`、`throughput`、`reliability` 之一，或 DiffServ 代码点之一：`ef`、`va`、`af11` ... `af43`、`cs0` ... `cs7`；或十六进制或十进制。

**`random-id`** 用随机值替换 IP 标识字段，以补偿许多主机生成的可预测值。此选项仅适用于可选分片重组后未分片的数据包。

**`reassemble tcp`** 有状态地规范化 TCP 连接。`reassemble tcp` 执行以下规范化：

例如，

```sh
match in all scrub (no-df random-id max-mss 1440)
```

### Scrub 规则集（FreeBSD 14 之前）

为了保持与旧版 FreeBSD 的兼容性，`scrub` 规则也可以在它们自己的规则集中指定。在这种情况下，它们通过 `scrub` 指令调用。如果存在此类规则，它们确定数据包重组行为。当不存在此类规则时，选项 `set reassembly` 优先。`scrub` 规则可以采用上面为过滤规则的 `scrub` 选项指定的所有参数，以及另外 2 个控制分片重组的参数：

**`fragment reassemble`** 使用 `scrub` 规则，可以通过规范化重组分片。在这种情况下，分片被缓冲直到它们形成完整的数据包，只有完整的数据包被传递给过滤器。优点是过滤规则只需处理完整的数据包，可以忽略分片。缓存分片的缺点是额外的内存成本。除非未指定分片重组，否则这是默认行为。

**`no fragment reassemble`** 不重组分片。

例如，

```sh
scrub in on $ext_if all fragment reassemble
```

在 scrub 规则前加 `no` 选项会使匹配的数据包保持未被 scrub 处理，方式与 `drop quick` 在包过滤器中的工作方式类似（见下文）。当需要从更广泛的 scrub 规则中排除特定数据包时，应使用此机制。

`scrub` 规则集中的 `scrub` 规则在有状态过滤之前对每个数据包进行评估。这意味着过度使用它们会导致性能损失。`scrub reassemble tcp` 规则不得指定方向（in/out）。

## 使用 ALTQ 排队

ALTQ 系统目前在 GENERIC 内核中不可用，也不能作为可加载模块。要使用此处及下文所述的排队选项，必须使用自定义构建的内核。有关相关内核选项，请参阅 [altq(4)](../man4/altq.4.md)。

可以出于带宽控制的目的将数据包分配到队列。配置队列至少需要两个声明，稍后任何包过滤规则都可以通过名称引用定义的队列。在 `pf.conf` 的过滤组件中，最后引用的 `queue` 名称是 `pass` 规则中任何数据包将排队的地方，而对于 `block` 规则，它指定任何由此产生的 ICMP 或 TCP RST 数据包应排队的地方。`scheduler` 定义用于决定哪些数据包被延迟、丢弃或立即发送的算法。目前支持三种 `scheduler`。

**`cbq`** 基于类的排队。附加到接口的 `Queues` 构建一棵树，因此每个 `queue` 可以有进一步的子 `queues`。每个队列可以分配 `priority` 和 `bandwidth`。`Priority` 主要控制数据包发送的时间，而 `bandwidth` 主要影响吞吐量。`cbq` 通过层次结构化的类实现链路带宽的分区和共享。每个类有自己的 `queue` 并分配其 `bandwidth` 份额。只要有剩余带宽可用，子类就可以从其父类借用带宽（参见下文的 `borrow` 选项）。

**`priq`** 优先级排队。`Queues` 平面地附加到接口，因此 `queues` 不能有进一步的子 `queues`。每个 `queue` 分配唯一的 `priority`，范围从 0 到 15。具有最高 `priority` 的 `queue` 中的数据包首先被处理。

**`hfsc`** 层次化公平服务曲线。附加到接口的 `Queues` 构建一棵树，因此每个 `queue` 可以有进一步的子 `queues`。每个队列可以分配 `priority` 和 `bandwidth`。`Priority` 主要控制数据包发送的时间，而 `bandwidth` 主要影响吞吐量。`hfsc` 支持链路共享和保证实时服务。它采用基于服务曲线的 QoS 模型，其独特功能是能够解耦 `delay` 和 `bandwidth` 分配。

应使用 `altq on` 声明来声明应激活排队的接口。`altq on` 具有以下关键字：

**<`interface`>** 在命名接口上启用排队。

**<`scheduler`>** 指定要使用的排队调度器。当前支持的值为 `cbq`（基于类的排队）、`priq`（优先级排队）和 `hfsc`（层次化公平服务曲线调度器）。

**`bandwidth`** <`bw`> 可以使用 `bandwidth` 关键字指定接口上所有队列的最大比特率。该值可以指定为绝对值或接口带宽的百分比。使用绝对值时，后缀 `b`、`Kb`、`Mb` 和 `Gb` 分别表示比特/秒、千比特/秒、兆比特/秒和吉比特/秒。该值不得超过接口带宽。如果未指定 `bandwidth`，则使用接口带宽（但请注意，某些接口不知道其带宽，或可以调整其带宽速率）。

**`qlimit`** <`limit`> 队列中保存的最大数据包数。默认为 50。

**`tbrsize`** <`size`> 调整令牌桶调节器的大小（以字节为单位）。如果未指定，则使用基于接口带宽的启发式方法来确定大小。

**`queue`** <`list`> 定义要在接口上创建的子队列列表。

在以下示例中，接口 dc0 应使用基于类的排队在四个二级队列中排队高达 5Mbps。这四个队列将在后面的示例中展示。

```sh
altq on dc0 cbq bandwidth 5Mb queue { std, http, mail, ssh }
```

一旦使用 `altq` 指令激活接口排队，就可以定义一系列 `queue` 指令。与 `queue` 关联的名称必须匹配 `altq` 指令中定义的队列（例如 mail），或者除 `priq` `scheduler` 外，在父 `queue` 声明中。可以使用以下关键字：

**`on`** <`interface`> 指定队列操作的接口。如果未给出，则在所有匹配的接口上操作。

**`bandwidth`** <`bw`> 指定队列要处理的最大比特率。此值不得超过父 `queue` 的值，可以指定为绝对值或父队列带宽的百分比。如果未指定，默认为父队列带宽的 100%。`priq` 调度器不支持带宽规范。

**`priority`** <`level`> 队列之间可以设置优先级。对于 `cbq` 和 `hfsc`，范围为 0 到 7，对于 `priq`，范围为 0 到 15。所有默认值为 1。具有更高优先级的 `Priq` 队列始终首先被服务。在过载情况下，具有更高优先级的 `Cbq` 和 `Hfsc` 队列被优先处理。

**`qlimit`** <`limit`> 队列中保存的最大数据包数。默认为 50。

`scheduler` 可以通过 Xo <`scheduler`> (<`parameters`>)> 获取附加参数。参数如下：

**`default`** 未被另一队列匹配的数据包分配到此队列。需要一个默认队列。

**`red`** 在此队列上启用 RED（随机早期检测）。RED 以与平均队列长度成正比的概率丢弃数据包。

**`rio`** 在此队列上启用 RIO。RIO 是带有 IN/OUT 的 RED，因此运行 RED 两次的效果与 RIO 相同。GENERIC 内核当前不支持 RIO。

**`ecn`** 在此队列上启用 ECN（显式拥塞通知）。ECN 隐含 RED。

`cbq` `scheduler` 支持一个附加选项：

**`borrow`** 队列可以从父级借用带宽。

`hfsc` `scheduler` 支持一些附加选项：

**`realtime`** <`sc`> 队列所需的最小带宽。

**`upperlimit`** <`sc`> 队列允许的最大带宽。

**`linkshare`** <`sc`> 积压队列的带宽份额。

<`sc`> 是 `service curve` 的首字母缩写。

服务曲线规范的格式为 `( m1 , d , m2 )`。`m2` 控制分配给队列的带宽。`m1` 和 `d` 是可选的，可用于控制初始带宽分配。对于前 `d` 毫秒，队列获得作为 `m1` 给出的带宽，之后获得 `m2` 中给出的值。

此外，对于 `cbq` 和 `hfsc`，子队列可以在 `altq` 声明中指定，从而使用父级带宽的一部分构建队列树。

可以使用 `queue` 关键字基于过滤规则将数据包分配到队列。通常只指定一个 `queue`；当指定第二个时，它将用于具有 *lowdelay* 的 *TOS* 和没有数据负载的 TCP ACK 的数据包。

继续前面的示例，以下示例将指定四个引用的队列，加上几个子队列。交互式 [ssh(1)](../man1/ssh.1.md) 会话的优先级高于 [scp(1)](../man1/scp.1.md) 和 [sftp(1)](../man1/sftp.1.md) 等批量传输。然后可以通过过滤规则引用这些队列（参见下文的 Sx PACKET FILTERING）。

```sh
queue std bandwidth 10% cbq(default)
queue http bandwidth 60% priority 2 cbq(borrow red) \
      { employees, developers }
queue  developers bandwidth 75% cbq(borrow)
queue  employees bandwidth 15%
queue mail bandwidth 10% priority 0 cbq(borrow ecn)
queue ssh bandwidth 20% cbq(borrow) { ssh_interactive, ssh_bulk }
queue  ssh_interactive bandwidth 50% priority 7 cbq(borrow)
queue  ssh_bulk bandwidth 50% priority 0 cbq(borrow)
block return out on dc0 inet all queue std
pass out on dc0 inet proto tcp from $developerhosts to any port 80 \
      queue developers
pass out on dc0 inet proto tcp from $employeehosts to any port 80 \
      queue employees
pass out on dc0 inet proto tcp from any to any port 22 \
      queue(ssh_bulk, ssh_interactive)
pass out on dc0 inet proto tcp from any to any port 25 \
      queue mail
```

## 使用 dummynet 排队

排队也可以使用 [dummynet(4)](../man4/dummynet.4.md) 完成。可以使用 dnctl(8) 创建队列和管道。

可以分别使用 `dnqueue` 和 `dnpipe` 将数据包分配到队列和管道。

`dnqueue` 和 `dnpipe` 都接受单个管道或队列号或两个数字作为参数。第一个管道或队列号将用于在规则方向上整形流量，第二个将用于在反方向上整形流量。如果规则未指定方向，则创建状态的第一个数据包将根据第一个号码进行整形，响应流量根据第二个号码。

如果未加载 [dummynet(4)](../man4/dummynet.4.md) 模块，则发送到队列或管道的任何流量都将被丢弃。

## 转换

转换选项修改与有状态连接关联的数据包的源或目标地址和端口。[pf(4)](../man4/pf.4.md) 修改数据包中指定的地址和/或端口，并根据需要重新计算 IP、TCP 和 UDP 校验和。

如果在 `match` 规则上指定，后续规则将看到数据包在地址和端口被转换后的样子。因此，这些规则必须基于转换后的地址和端口号进行过滤。

创建的状态条目允许 [pf(4)](../man4/pf.4.md) 跟踪与该状态关联的流量的原始地址，并正确引导该连接的返回流量。

pf 可以进行各种类型的转换：

```sh
pass in inet af-to inet6 from 2001:db8::1 to 2001:db8::/96
pass in inet af-to inet6 from 2001:db8::1
```

```sh
pass in inet6 from any to 64:ff9b::/96 af-to inet \
       from 198.51.100.1 to 0.0.0.0/0
pass in inet6 from any to 64:ff9b::/96 af-to inet \
       from 198.51.100.1
```

```sh
10.0.0.0 - 10.255.255.255 (all of net 10.0.0.0, i.e., 10.0.0.0/8)
172.16.0.0 - 172.31.255.255 (i.e., 172.16.0.0/12)
192.168.0.0 - 192.168.255.255 (i.e., 192.168.0.0/16)
```

```sh
match in ... port 2000:2999 rdr-to ... port 4000
```

```sh
match in ... port 2000:2999 rdr-to ... port 4000:*
```

**`af-to`** 不同地址族之间的转换（NAT64）使用 `af-to` 规则处理。由于地址族转换覆盖路由表，因此只能在入站规则上使用 `af-to`，并且必须始终指定结果转换的源地址。可选的第二个参数是原始地址被转换到的目标主机或子网。原始目标地址的最低位根据指定子网形成新目标地址的主机部分。可以使用 /96 或更小的网络前缀将完整的 IPv4 地址嵌入到 IPv6 地址中。当未指定目标地址时，假定主机部分为 32 位长。对于 IPv6 到 IPv4 转换，这意味着仅使用原始 IPv6 目标地址的低 32 位。对于 IPv4 到 IPv6 转换，目标子网默认为前缀长度为 /96 的新 IPv6 源地址的子网。有关前缀如何确定目标地址编码的详细信息，请参见 RFC 6052 第 2.2 节。例如，以下规则是相同的：在上述示例中，匹配的 IPv4 数据包将被修改为具有源地址 2001:db8::1，目标地址将加上 2001:db8::/96 前缀，例如 198.51.100.100 将被转换为 2001:db8::c633:6464。在反向情况下，以下规则是相同的：假定目标 IPv4 地址嵌入在原始 IPv6 目标地址中，例如 64:ff9b::c633:6464 将被转换为 198.51.100.100。当前实现仅从具有 /96 及更大前缀长度的 IPv6 地址中提取 IPv4 地址。

**`binat-to`** `binat-to` 规则指定外部 IP 网络块和内部 IP 网络块之间的双向映射。它展开为出站 `nat-to` 规则和入站 `rdr-to` 规则。

**`nat-to`** `nat-to` 选项指定在数据包通过给定接口时要更改 IP 地址。此技术允许转换主机上的一个或多个 IP 地址为 “内部” 网络上更大范围的机器支持网络流量。虽然在理论上内部可以使用任何 IP 地址，但强烈建议使用 RFC 1918 定义的一个地址范围。这些网络块是：`nat-to` 通常出站应用。如果入站应用，不支持 nat-to 到本地 IP 地址。

**`rdr-to`** 数据包被重定向到另一个目标，可能是不同的端口。`rdr-to` 可以可选地指定端口范围而不是单个端口。例如：将端口 2000 到 2999（含）重定向到端口 4000。将端口 2000 重定向到 4000、2001 重定向到 4001、...、2999 重定向到 4999。

`rdr-to` 通常入站应用。如果出站应用，不支持 rdr-to 到本地 IP 地址。除了修改地址外，某些转换规则可能会修改 [tcp(4)](../man4/tcp.4.md) 或 [udp(4)](../man4/udp.4.md) 连接的源或目标端口；在 `nat-to` 选项的情况下是隐式的，在 `rdr-to` 选项的情况下既是隐式的也是显式的。如果这样做可以避免与现有连接冲突，`rdr-to` 选项可能会导致源端口被修改。在这种情况下，选择 50001-65535 范围内的随机源端口。使用 `binat-to` 选项时，端口号永远不会被转换。

注意，将外部传入连接重定向到回环地址，如

```sh
pass in on egress proto tcp from any to any port smtp \
      rdr-to 127.0.0.1 port spamd
```

将有效地允许外部主机连接到仅绑定到回环地址的守护进程，绕过传统上在真实接口上对此类连接的阻止。除非期望此效果，否则应使用任何本地非回环地址作为重定向目标，这仅允许外部连接到绑定到此地址或未绑定到任何地址的守护进程。

参见下文的 Sx TRANSLATION EXAMPLES。

### NAT 规则集（FreeBSD 15 之前）

为了保持与旧版 FreeBSD 的兼容性，`NAT` 规则也可以在它们自己的规则集中指定。只要数据包未被 `pf.conf` 的过滤部分阻止，就会自动创建有状态连接来跟踪匹配此类规则的数据包。由于转换发生在过滤之前，过滤引擎将看到数据包在地址和端口被转换后的样子。因此，过滤规则必须基于转换后的地址和端口号进行过滤。仅当给出 `pass` 修饰符时，匹配转换规则的数据包才会自动通过，否则仍受 `block` 和 `pass` 规则约束。

NAT 规则集中可以定义以下规则：`binat`、`nat` 和 `rdr`。它们与过滤规则的 `binat-to`、`nat-to` 和 `rdr-to` 选项具有相同效果。

转换规则前加 `no` 选项会使数据包保持未转换状态，方式与 `drop quick` 在包过滤器中的工作方式类似。如果没有规则匹配数据包，则将其未修改地传递给过滤引擎。

转换规则的评估顺序取决于转换规则的类型和数据包的方向。`binat` 规则始终首先评估。然后在入站数据包上评估 `rdr` 规则，或在出站数据包上评估 `nat` 规则。相同类型的规则按它们在规则集中出现的相同顺序评估。第一条匹配规则决定采取什么操作。

转换规则仅适用于通过指定接口的数据包，如果未指定接口，则转换应用于所有接口上的数据包。例如，将外部接口上的端口 80 重定向到内部 Web 服务器仅对来自外部的连接有效。从本地主机到外部接口地址的连接不会被重定向，因为此类数据包实际上并未通过外部接口。重定向不能将数据包反射回它们到达的接口，只能重定向到连接到不同接口的主机或防火墙本身。

参见下文的 Sx COMPATIBILITY TRANSLATION EXAMPLES。

## 包过滤

[pf(4)](../man4/pf.4.md) 能够根据其第 3 层（参见 [ip(4)](../man4/ip.4.md) 和 [ip6(4)](../man4/ip6.4.md)）和第 4 层（参见 [icmp(4)](../man4/icmp.4.md)、[icmp6(4)](../man4/icmp6.4.md)、[tcp(4)](../man4/tcp.4.md)、[sctp(4)](../man4/sctp.4.md)、[udp(4)](../man4/udp.4.md)）头的属性 `block`、`pass` 和 `match` 数据包。此外，数据包还可以出于带宽控制的目的分配到队列。

对于包过滤器处理的每个数据包，过滤规则按顺序从第一条到最后一条进行评估。对于 `block` 和 `pass`，最后匹配的规则决定采取什么操作。对于 `match`，规则每次匹配时都会被评估；数据包的通过/阻止状态保持不变。如果没有规则匹配数据包，默认操作是通过数据包。

以下操作可在过滤器中使用：

**`drop`** 数据包被静默丢弃。

**`return-rst`** 这仅适用于 [tcp(4)](../man4/tcp.4.md) 数据包，发出关闭连接的 TCP RST。

**`return-icmp`**

**`return-icmp6`** 这会导致为匹配规则的数据包返回 ICMP 消息。默认情况下这是 ICMP UNREACHABLE 消息，但是可以通过将消息指定为代码或数字来覆盖。

**`return`** 这会导致对 [tcp(4)](../man4/tcp.4.md) 数据包返回 TCP RST，对 SCTP 返回 SCTP ABORT，对 UDP 和其他数据包返回 ICMP UNREACHABLE。

```sh
block all
```

**`block`** 数据包被阻止。`block` 规则在阻止数据包时有多种行为方式。默认行为是静默 `drop` 数据包，但是可以通过设置 `block-policy` 选项全局覆盖或使其显式，或者使用以下选项之一按规则覆盖：如果 [pf(4)](../man4/pf.4.md) 在 if_bridge(4) 上操作，则返回 ICMP 数据包的选项当前无效，因为支持此功能的代码尚未实现。默认阻止所有内容并仅通过匹配显式规则的数据包的最简单机制是指定第一条过滤规则为：

**`match`** 数据包被匹配。此机制用于提供细粒度过滤而不更改数据包的阻止/通过状态。`match` 规则与 `block` 和 `pass` 规则的不同之处在于，参数是为数据包匹配的每条规则设置的，而不仅仅是最后匹配的规则。对于以下参数，这意味着参数实际上变得 “粘性”，直到被显式覆盖：`nat-to`、`binat-to`、`rdr-to`、`queue`、`dnpipe`、`dnqueue`、`rtable`、`scrub`

**`pass`** 数据包通过；除非指定了 `no state` 选项，否则创建状态。

默认情况下，[pf(4)](../man4/pf.4.md) 有状态地过滤数据包；数据包首次匹配 `pass` 规则时创建状态条目；对于后续数据包，过滤器检查数据包是否匹配任何状态。如果匹配，则数据包通过而不评估任何规则。连接关闭或超时后，状态条目会自动删除。

这有几个优点。对于 TCP 连接，将数据包与状态进行比较涉及检查其序列号，以及如果 `scrub reassemble tcp` 规则适用于连接，还包括 TCP 时间戳。如果这些值超出预期值的窄窗口，数据包将被丢弃。这可以防止欺骗攻击，例如攻击者发送具有伪造源地址/端口但不知道连接序列号的数据包。类似地，[pf(4)](../man4/pf.4.md) 知道如何将 ICMP 回复匹配到状态。例如，

```sh
pass out inet proto icmp all icmp-type echoreq
```

允许回显请求（如 [ping(8)](../man8/ping.8.md) 创建的那些）有状态地发出，并正确将传入的回显回复匹配到状态。

此外，查找状态通常比评估规则更快。

此外，正确处理 ICMP 错误消息对许多协议（特别是 TCP）至关重要。[pf(4)](../man4/pf.4.md) 将 ICMP 错误消息匹配到正确的连接，根据连接参数检查它们，并在适当时通过它们。例如，如果引用有状态 TCP 连接的 ICMP 源抑制消息到达，它将被匹配到状态并被通过。

最后，`nat , binat` 和 `rdr` 规则需要状态跟踪，以便跟踪地址和端口转换并在返回数据包上反转转换。

[pf(4)](../man4/pf.4.md) 还将为本质上无状态的其他协议创建状态。UDP 数据包仅使用主机地址和端口匹配到状态，其他协议仅使用主机地址匹配到状态。

如果需要对单个数据包进行无状态过滤，可以使用 `no state` 关键字指定如果这是最后匹配的规则则不创建状态。还可以设置许多参数来影响 [pf(4)](../man4/pf.4.md) 处理状态跟踪的方式。有关更多详细信息，请参见下文的 Sx STATEFUL TRACKING OPTIONS。

### 参数

规则参数指定规则适用于哪些数据包。数据包总是从某个接口进入或通过某个接口离开。大多数参数是可选的。如果指定了参数，则该规则仅适用于具有匹配属性的数据包。某些参数可以表示为列表，在这种情况下，pfctl(8) 会生成所有需要的规则组合。

**`any`** 任何地址。

**`no-route`** 当前不可路由的任何地址。

**`urpf-failed`** 任何未通过单播反向路径转发（URPF）检查的源地址，即从与持有到数据包源地址路由的接口不同的接口进入的数据包。

**`self`** 展开为分配给所有接口的所有地址。

**<`table`>** 匹配给定表的任何地址。

**`:network`** 转换为附加到接口的网络。

**`:broadcast`** 转换为接口的广播地址。

**`:peer`** 转换为点到点接口的对端地址。

**`:0`** 不包括接口别名。

```sh
=	(等于)
!=	(不等于)
<	(小于)
<=	(小于或等于)
>	(大于)
>=	(大于或等于)
:	(包括边界的范围)
><	(不包括边界的范围)
<>	(范围之外)
```

**`port 2000:2004`** 表示 “所有 >= 2000 且 <= 2004 的端口”，即端口 2000、2001、2002、2003 和 2004。

**`port 2000 >< 2004`** 表示 “所有 > 2000 且 < 2004 的端口”，即端口 2001、2002 和 2003。

**`port 2000 <> 2004`** 表示 “所有 < 2000 或 > 2004 的端口”，即端口 1-1999 和 2005-65535。

```sh
pass in all
pass in from any to any
pass in proto tcp from any port < 1024 to any
pass in proto tcp from any to any port 25
pass in proto tcp from 10.0.0.0/8 port >= 1024 \
      to ! 10.1.2.3 port != ssh
pass in proto tcp from any os "OpenBSD"
```

```sh
block out proto { tcp, udp } all
pass  out proto { tcp, udp } all user { < 1000, dhartmei }
```

```sh
block out proto tcp all
pass  out proto tcp from self user { 999 >< 1501 }
```

**`flags S/S`** 设置了 SYN 标志。其他标志被忽略。

**`flags S/SA`** 这是有状态连接的默认设置。在 SYN 和 ACK 中，正好可以设置 SYN。SYN、SYN+PSH 和 SYN+RST 匹配，但 SYN+ACK、ACK 和 ACK+RST 不匹配。这比前面的示例更具限制性。

**`flags /SFRA`** 如果未指定第一组，则默认为无。SYN、FIN、RST 和 ACK 必须全部未设置。

```sh
pass all tos lowdelay
pass all tos 0x10
pass all tos 16
```

**`$if`** 接口。

**`$srcaddr`** 源 IP 地址。

**`$dstaddr`** 目标 IP 地址。

**`$srcport`** 源端口规范。

**`$dstport`** 目标端口规范。

**`$proto`** 协议名称。

**`$nr`** 规则编号。

```sh
ips = "{ 1.2.3.4, 1.2.3.5 }"
pass in proto tcp from any to $ips \
      port > 1023 label "$dstaddr:$dstport"
```

```sh
pass in inet proto tcp from any to 1.2.3.4 \
      port > 1023 label "1.2.3.4:>1023"
pass in inet proto tcp from any to 1.2.3.5 \
      port > 1023 label "1.2.3.5:>1023"
```

```sh
block in proto icmp
pass in proto icmp max-pkt-rate 100/10
```

```sh
pass in proto tcp to port 25 queue mail
pass in proto tcp to port 22 queue(ssh_bulk, ssh_prio)
```

```sh
pass in proto tcp to port 25 set prio 2
pass in proto tcp to port 22 set prio (2, 5)
```

```sh
block in proto icmp probability 20%
```

**`in`** 或 `out` 此规则适用于传入或传出数据包。如果未指定 `in` 或 `out`，规则将匹配双向数据包。

**`log`** (`all | matches | to` <`interface` >`user`>) 除了指定的任何操作外，还记录数据包。仅建立状态的数据包被记录，除非指定了 `no state` 选项。记录的数据包发送到 [pflog(4)](../man4/pflog.4.md) 接口，默认为 pflog0；pflog0 由 pflogd(8) 日志守护进程监控，该守护进程以 pcap(3) 二进制格式记录到文件 **/var/log/pflog**。关键字 `all , matches , to` 和 `user` 是可选的，可以使用逗号组合，但如果给出，必须用括号括起来。使用 `all` 强制记录连接的所有数据包。当显式指定 `no state` 时，这不是必需的。如果指定了 `matches`，它会在所有后续匹配规则上记录数据包。它通常与 `to` <`interface`> 结合使用，以避免向默认日志文件添加噪声。关键字 `user` 记录拥有套接字的 UNIX 用户 ID 和具有打开套接字的进程的 PID，数据包来自或发往该套接字（取决于哪个套接字是本地的）。这是除记录的正常信息之外的附加信息。使用有状态匹配时，只有通过 `log (all, user)` 记录的第一个数据包才会记录用户凭据。要指定 pflog0 之外的日志记录接口，使用语法 `to` <`interface`>。

**`quick`** 如果数据包匹配设置了 `quick` 选项的规则，此规则被视为最后匹配的规则，并跳过对后续规则的评估。

**`on`** <`interface`> 此规则仅适用于从该特定接口或接口组进入或离开的数据包。有关接口组的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md) 中的 `group` 关键字。`any` 将匹配除回环接口外的任何现有接口。

**<`af`>** 此规则仅适用于此地址族的数据包。支持的值为 `inet` 和 `inet6`。

**`proto`** <`protocol`> 此规则仅适用于此协议的数据包。常见协议有 [icmp(4)](../man4/icmp.4.md)、[icmp6(4)](../man4/icmp6.4.md)、[tcp(4)](../man4/tcp.4.md)、[sctp(4)](../man4/sctp.4.md) 和 [udp(4)](../man4/udp.4.md)。有关 pfctl(8) 使用的所有协议名到编号的映射列表，请参见文件 **/etc/protocols**。

**Xo** `from` <`source`> `port` <`source`> `os` <`source`> `to` <`dest`> `port` <`dest`> Xc 此规则仅适用于具有指定源和目标地址和端口的数据包。地址可以用 CIDR 表示法（匹配网络块）、符号主机名、接口名或接口组名，或以下任何关键字指定：地址范围使用 ‘-’ 运算符指定。例如：“10.1.1.10 - 10.1.1.12” 表示从 10.1.1.10 到 10.1.1.12 的所有地址，即地址 10.1.1.10、10.1.1.11 和 10.1.1.12。接口名和接口组名，以及 `self` 可以附加修饰符：主机名也可以附加 `:0` 选项，以将名称解析限制为找到的第一个 v4 和非链路本地 v6 地址。主机名解析和接口到地址的转换在规则集加载时完成。当接口（或主机名）的地址更改时（例如在 DHCP 或 PPP 下），必须重新加载规则集才能在内核中反映更改。将接口名（和可选修饰符）用括号括起来会更改此行为。当接口名用括号括起来时，每当接口更改其地址时，规则会自动更新。无需重新加载规则集。这在 `nat` 中特别有用。端口可以按编号或名称指定。例如，端口 80 可以指定为 *www.* 有关 pfctl(8) 使用的所有端口名到编号的映射列表，请参见文件 **/etc/services**。端口和端口范围使用以下运算符指定：‘><’、‘<>’ 和 ‘:’ 是二元运算符（它们接受两个参数）。例如：在 TCP 规则的情况下，可以使用 `OS` 修饰符指定源主机的操作系统。更多信息请参见 Sx OPERATING SYSTEM FINGERPRINTING 部分。主机、端口和 OS 规范是可选的，如以下示例所示：

**`all`** 这等同于 “from any to any”。

**`group`** <`group`> 类似于 `user`，此规则仅适用于由指定组拥有的套接字的数据包。

**`user`** <`user`> 此规则仅适用于由指定用户拥有的套接字的数据包。对于从防火墙发起的传出连接，这是打开连接的用户。对于到防火墙本身的传入连接，这是在目标端口上监听的用户。对于转发的连接，其中防火墙不是连接端点，用户和组是 *unknown.* 一个连接的所有数据包（传出和传入）都与同一用户和组关联。只有 TCP 和 UDP 数据包可以与用户关联；对于其他协议，这些参数被忽略。如果套接字由 setuid/setgid 进程创建，则用户和组引用有效（而非实际）ID。创建套接字时存储用户和组 ID；当进程以 root 身份创建监听套接字（例如通过绑定到特权端口）并随后更改为另一个用户 ID（以放弃权限）时，凭据将保持为 root。用户和组 ID 可以指定为数字或名称。语法类似于端口的语法。值 *unknown* 匹配转发连接的数据包。*unknown* 只能与运算符 `=` 和 `!=` 一起使用。其他构造如 `user *(Ge unknown` 无效。具有未知用户和组 ID 的转发数据包仅匹配使用 `=` 或 `!=` 运算符与 *unknown* 显式比较的规则。例如 `user *(Ge 0` 不匹配转发数据包。以下示例仅允许选定用户打开传出连接：以下示例允许 uid 在 1000 和 1500 之间的用户打开连接：用于端口号匹配的 ‘:’ 运算符不适用于 `user` 和 `group` 匹配。

**Xo** `flags` <`a`> /<`b`> *(Ba /<`b`> *(Ba any Xc 此规则仅适用于在集合 <`b`> 中设置了标志 <`a`> 的 TCP 数据包。未在 <`b`> 中指定的标志被忽略。对于有状态连接，默认为 `flags S/SA`。要表示根本不检查标志，指定 `flags any`。标志有：(F)IN、(S)YN、(R)ST、(P)USH、(A)CK、(U)RG、(E)CE 和 C(W)R。由于默认应用 `flags S/SA`（除非指定 `no state`），TCP 握手的初始 SYN 数据包才会为 TCP 连接创建状态。可以通过指定 `flags any` 来放宽限制，允许从中间（非 SYN）数据包创建状态。这将导致 [pf(4)](../man4/pf.4.md) 同步到现有连接，例如如果刷新了状态表。但是，从此类中间数据包创建的状态可能缺少连接详细信息，如 TCP 窗口缩放因子。修改数据包流的状态，如受 `af-to`、`nat`、`binat or` `rdr` 规则、`modulate` 或 `synproxy state` 选项影响的状态，或使用 `reassemble tcp` 进行清理的状态，也将无法从中间数据包恢复。此类连接将停滞并超时。

**Xo** `icmp-type` <`type`> `file` [code <`code`>] Xc

**Xo** `icmp6-type` <`type`> `file` [code <`code`>] Xc 此规则仅适用于具有指定类型和代码的 ICMP 或 ICMPv6 数据包。ICMP 类型和代码的文本名称列在 [icmp(4)](../man4/icmp.4.md) 和 [icmp6(4)](../man4/icmp6.4.md) 中。此参数仅对涵盖协议 ICMP 或 ICMP6 的规则有效。协议和 ICMP 类型指示符（`icmp-type` 或 `icmp6-type`）必须匹配。

**Xo** `tos` <`string`> *(Ba <`number`> Xc 此规则适用于设置了指定 *TOS* 位的数据包。*TOS* 可以作为 `critical`、`inetcontrol`、`lowdelay`、`netcontrol`、`throughput`、`reliability` 之一，或 DiffServ 代码点之一：`ef`、`va`、`af11` ... `af43`、`cs0` ... `cs7`；或十六进制或十进制。例如，以下规则是相同的：

**`allow-opts`** 默认情况下，带有 IPv4 选项或 IPv6 逐跳或目标选项头的数据包被阻止。当为 `pass` 规则指定 `allow-opts` 时，基于该规则（最后匹配）通过过滤的数据包即使包含选项也会通过。对于匹配状态的数据包，使用最初创建状态的规则。当数据包不匹配任何规则时使用的隐式 `pass` 规则不允许 IP 选项或选项头。注意，具有类型 0 路由头的 IPv6 数据包始终被丢弃。

**`label`** <`string`> 为规则添加标签（名称），可用于标识规则。例如，pfctl -s labels 显示具有标签的规则的每条规则统计。以下宏可用于标签中：例如：展开为 `label` 指令的宏展开仅在配置文件解析时发生，不在运行期间。

**`ridentifier`** <`number`> 为规则添加标识符（数字），可用于将规则与 pflog 条目相关联，即使在规则集更新后也是如此。

**`max-pkt-rate`** `number`/`seconds` 测量匹配规则及其创建的状态的数据包速率。当超过指定速率时，规则停止匹配。仅考虑创建状态方向上的数据包，因此通常只计算请求而不计算回复。例如，每 10 秒最多通过 100 个 ICMP 数据包：当超过速率时，所有 ICMP 被阻止，直到速率再次降到每 10 秒 100 以下。

**`max-pkt-size`** <`number`> 限制每个数据包不超过指定的字节数。这包括 IP 头，但不包括任何第 2 层头。

**`once`** 创建一次性规则。第一个匹配数据包将规则标记为过期。过期规则被跳过并隐藏，除非 pfctl(8) 在调试或详细模式下使用。

**Xo** `queue` <`queue`> *(Ba ( <`queue`>, <`queue`>) Xc 匹配此规则的数据包将分配到指定队列。如果给出两个队列，具有 *lowdelay* 的 *TOS* 和没有数据负载的 TCP ACK 的数据包将分配到第二个队列。设置详情请参见 Sx QUEUEING。例如：

**`set prio`** `priority |` (`priority , priority`) 匹配此规则的数据包将分配特定的排队优先级。优先级指定为 0 到 7 的整数。如果数据包在 [vlan(4)](../man4/vlan.4.md) 接口上传输，排队优先级将写入 802.1Q VLAN 头中的优先级代码点。如果给出两个优先级，没有数据负载的 TCP ACK 和具有 `lowdelay` 的 TOS 的数据包将分配到第二个优先级。例如：

**[`!`** ]`received-on` `interface`] 仅匹配在指定 `interface`（或接口组）上接收的数据包。`any` 将匹配除回环接口外的任何现有接口。

**`tag`** <`string`> 匹配此规则的数据包将用指定字符串标记。标记充当内部标记，可用于稍后识别这些数据包。例如，这可用于在接口之间提供信任，以及确定数据包是否已被转换规则处理。标记是 “粘性的”，意味着即使该规则不是最后匹配的规则，数据包也将被标记。进一步的匹配规则可以用新标记替换标记，但不会删除之前应用的标记。一个数据包一次只能分配一个标记。数据包标记可以在 `nat`、`rdr`、`binat` 或 `ether` 规则以及过滤规则中完成。标记采用与标签相同的宏（见上文）。

**`tagged`** <`string`> 与过滤、转换或 scrub 规则一起使用，指定数据包必须已经用给定标记标记才能匹配规则。

**`rtable`** <`number`> 用于为路由查找选择备用路由表。仅在路由查找发生之前有效，即过滤入站时。

**Xo** `divert-to` <`host`> `port` <`port`> Xc 用于将数据包 [divert(4)](../man4/divert.4.md) 到给定的 divert `port`。历史上 OpenBSD pf FreeBSD pf 使用此语法支持 [divert(4)](../man4/divert.4.md) `host` 没有意义，可以设置为 127.0.0.1 之类的任何值。如果数据包被重新注入且方向不变，则不会被重新 divert。

**`divert-reply`** 在 FreeBSD pf 中没有意义。

**`probability`** <`number`> 可以将概率属性附加到规则，值设置在 0 和 1 之间，不包括边界。在这种情况下，规则仅使用给定的概率值被遵守。例如，以下规则将丢弃 20% 的传入 ICMP 数据包：

**`state limiter`** `name` [`(limiter options)` ]] 使用指定的状态限制器限制此规则创建的状态。默认情况下，如果没有可用容量，数据包被阻止并且规则集评估停止。使用 `no-match` 选项更改默认行为，此类规则被忽略，规则集评估继续下一条规则。更多信息请参见 Sx State Limiters 部分。

**`source limiter`** `name` [`(limiter options)` ]] 使用指定的源限制器限制此规则创建的状态。默认情况下，如果没有可用容量，数据包被阻止并且规则集评估停止。使用 `no-match` 选项更改默认行为，此类规则被忽略，规则集评估继续下一条规则。更多信息请参见 Sx Source Limiters 部分。

**`prio`** <`number`> 仅匹配已分配给定排队优先级的数据包。

## 路由

如果数据包匹配设置了路由选项的规则，包过滤器将根据路由选项的类型路由数据包。当此类规则创建状态时，路由选项也应用于匹配同一连接的所有数据包。

**`route-to`** `route-to` 选项将数据包路由到指定接口的下一跳地址。当 `route-to` 规则创建状态时，只有与过滤规则指定方向相同的数据包才会以这种方式路由。相反方向的数据包（回复）不受影响，正常路由。

**`reply-to`** `reply-to` 选项类似于 `route-to`，但将相反方向（回复）的数据包路由到指定接口。相反方向仅在状态条目的上下文中定义，`reply-to` 仅在创建状态的规则中有用。它可用于具有多个外部连接的系统，通过连接到达的接口路由连接的所有传出数据包（对称路由强制）。

**`dup-to`** `dup-to` 选项创建数据包的副本并像 `route-to` 一样路由它。原始数据包按正常方式路由。

与内核的正常转发路径不同，路由选项转发路径在输出接口被路由选项覆盖时不会丢弃广播或多播流量。如果 `route-to`、`reply-to` 或 `dup-to` 规则匹配发往广播地址（有限广播或子网定向广播）或 IPv4/IPv6 多播地址的流量，数据包将从指定接口转发，这可能跨越广播域。

使用 `route-to`、`reply-to` 或 `dup-to` 且具有宽松目标（例如 `from any to any`）的规则集可以使用路由选项目标接口上的显式 `block out` 规则堵塞此泄漏。为避免阻止路由器自身的广播或多播流量，使用 `received-on any` 限定符将阻止规则范围限定为转发的数据包。例如，假设 `$wan` 是 `route-to` 目标接口：

```sh
block out quick on $wan inet  from any to 255.255.255.255  received-on any
block out quick on $wan inet  from any to ($wan:broadcast) received-on any
block out quick on $wan inet  from any to 224.0.0.0/4      received-on any
block out quick on $wan inet6 from any to ff00::/8         received-on any
```

每个可能用作路由选项目标的接口需要一组阻止出站规则。

## 池选项

对于 `nat` 和 `rdr` 规则（以及 `route-to`、`reply-to` 和 `dup-to` 规则选项），如果只有一个重定向地址且子网掩码小于 32（IPv4）或 128（IPv6）（多于一个 IP 地址），可以使用多种不同的方法来分配此地址：

```sh
nat on $gif_mape_if from $int_if:network to any \
      -> $ipv4_mape_src map-e-portset 6/8/0x34
```

**`bitmask`** `bitmask` 选项将重定向地址的网络部分应用于要修改的地址（`nat` 的源，`rdr` 的目标）。

**`random`** `random` 选项在定义的地址块内随机选择一个地址。

**`source-hash`** `source-hash` 选项使用源地址的哈希来确定重定向地址，确保对于给定源，重定向地址始终相同。可以在此关键字之后以十六进制或字符串形式指定可选密钥；默认情况下，pfctl(8) 每次重新加载规则集时为 source-hash 随机生成密钥。

**`round-robin`** `round-robin` 选项循环遍历重定向地址。当指定多个重定向地址时，不允许将 `bitmask` 作为池类型。

**`static-port`** 对于 `nat` 规则，`static-port` 选项阻止 [pf(4)](../man4/pf.4.md) 修改 TCP 和 UDP 数据包上的源端口。

**Xo** `map-e-portset` <`psid-offset`> / <`psid-len`> / <`psid`> Xc 对于 `nat` 规则，`map-e-portset` 选项启用 MAP-E（RFC 7597）客户边缘的源端口转换。要使主机充当 MAP-E 客户边缘，除了 map-e-portset nat 规则外，还需要设置隧道接口和封装数据包的通过规则。例如：设置 PSID 偏移 6、PSID 长度 8、PSID 0x34。

**`endpoint-independent`** 对于 `nat` 规则，`endpoint-independent` 选项使 [pf(4)](../man4/pf.4.md) 始终将来自 UDP 源地址和端口的连接映射到相同的 NAT 地址和端口。此功能实现 “full-cone” NAT 行为。

此外，可以指定选项 `sticky-address` 和 `prefer-ipv6-nexthop` 来影响从池中选择的 IP 地址。

可以指定 `sticky-address` 选项以帮助确保来自同一源的多个连接映射到同一重定向地址。此选项可与 `random` 和 `round-robin` 池选项一起使用。注意，默认情况下，一旦不再有引用它们的状态，这些关联就会被销毁；要使映射持续超出状态的生命周期，请使用 `set timeout src.track` 增加全局选项。有关控制源跟踪的更多方法，请参见 Sx STATEFUL TRACKING OPTIONS。

`prefer-ipv6-nexthop` 选项允许将 IPv6 地址用作使用 `route-to` 规则选项路由的 IPv4 数据包的下一跳。如果表使用 IPv4 和 IPv6 地址，则首先以轮询方式使用 IPv6 地址，然后使用 IPv4 地址。

## 状态调制

TCP 衍生的大部分安全性归功于初始序列号（ISN）的选择。一些流行的栈实现选择 *非常* 差的 ISN，因此通常容易受到 ISN 预测攻击。通过将 `modulate state` 规则应用于 TCP 连接，[pf(4)](../man4/pf.4.md) 将为每个连接端点创建高质量的随机序列号。

`modulate state` 指令隐式地在规则上保持状态，仅适用于 TCP 连接。

例如：

```sh
block all
pass out proto tcp from any to any modulate state
pass in  proto tcp from any to any port 25 flags S/SFRA modulate state
```

注意，当状态表丢失（防火墙重启、刷新状态表等）时，调制连接不会恢复。状态表刷新连接的调制器后，[pf(4)](../man4/pf.4.md) 无法再次推断连接。状态丢失时，连接可能会悬挂，直到各自端点超时该连接。在快速本地网络上，端点在调制器丢失后尝试重新同步时可能引发 ACK 风暴。应在 `modulate state` 规则上使用默认 `flags` 设置（或更严格的等效设置）以防止 ACK 风暴。

注意，有替代方法可用于防止状态表丢失并允许防火墙故障转移。更多信息请参见 [carp(4)](../man4/carp.4.md) 和 [pfsync(4)](../man4/pfsync.4.md)。

## SYN 代理

默认情况下，[pf(4)](../man4/pf.4.md) 通过端点之间 [tcp(4)](../man4/tcp.4.md) 握手的数据包。`synproxy state` 选项可用于使 [pf(4)](../man4/pf.4.md) 本身完成与主动端点的握手，与被动端点执行握手，然后在端点之间转发数据包。

在主动端点完成握手之前，不会向被动端点发送数据包，因此具有伪造源地址的所谓 SYN 泛滥不会到达被动端点，因为发送方无法完成握手。

代理对两个端点都是透明的，它们各自看到来自/到另一端点的单个连接。[pf(4)](../man4/pf.4.md) 为两个握手选择随机初始序列号。握手完成后，序列号调制器（见上一节）用于转换连接的后续数据包。`synproxy state` 包括 `modulate state`。

如果 [pf(4)](../man4/pf.4.md) 在 [bridge(4)](../man4/bridge.4.md) 上操作，则带有 `synproxy` 的规则不起作用。它们也仅作用于传入的 SYN 数据包。

示例：

```sh
pass in proto tcp from any to any port www synproxy state
```

### 状态限制器

状态限制器提供了一种机制，用于限制一组规则创建的状态数或状态创建速率。状态限制器与主规则集一起配置和加载，但可被任何锚点中的规则使用。状态总数仍受 `set limit states` 设置的限制，但规则子集创建的状态数可由状态限制器提供。

状态限制器使用以下语句配置：

**`state limiter`** `name` 每个状态限制器由唯一名称标识。

状态限制器支持以下配置：

**`id`** `number` 1 到 255 之间的唯一标识符。此配置是必需的。

**`limit`** `number` 指定最大状态数。此配置是必需的。

**`rate`** `number`/`seconds` 限制在时间间隔内可以创建状态的速率。连接速率是作为移动平均值计算的近似值。

通过规则可以使用 `state limiter` `name` 选项指定状态限制器。如果允许的状态数已达到限制，通过规则不匹配，规则集评估继续超过它。

状态限制器的一个示例用例是限制可通过多种协议访问的服务允许的连接数，例如可通过 TCP 和 UDP 端口 53、TCP 端口 853 上的 DNS-over-TLS 和 TCP 端口 443 上的 DNS-over-HTTPS 访问的 DNS 服务器可限制为 1000 个并发连接：

state limiter "dns-server" id 1 limit 1000
pass in proto { tcp udp } to port domain state limiter "dns-server"
pass in proto tcp to port { 853 443 } state limiter "dns-server"

### 源限制器

源限制器对来自一组规则的源地址或网络的连接应用状态数或状态创建速率限制。源限制器与主规则集一起配置和加载，但可被任何锚点中的规则使用。状态总数仍受 `set limit states` 设置的限制，但源地址子集和规则子集的状态限制可由源限制器提供。

源池中的源地址条目按需创建，并用于统计为每个源地址或网络创建的状态。源限制器指定它将跟踪的最大源地址条目数，并可配置为在网络前缀中掩码位，以便在需要时使源条目覆盖更大的地址空间部分。

源限制器使用以下语句配置：

**`source limiter`** `name` 每个源限制器由指定名称唯一标识。

源限制器支持以下配置：

**`id`** `number` 1 到 255 之间的唯一标识符。此配置是必需的。

**`entries`** `number` 指定最大源地址条目数。此配置是必需的。

**`limit`** `number` 指定每个源地址条目的最大状态数。此配置是必需的。

**`rate`** `number`/`seconds` 限制每个源地址条目在时间间隔内可以创建状态的速率。连接速率是作为移动平均值计算的近似值。

**`inet mask`** `prefixlen` 创建地址条目时使用 `prefixlen` 指定的前缀长度掩码 IPv4 源地址。默认 IPv4 前缀长度为 32 位。

**`inet6 mask`** `prefixlen` 创建地址条目时使用 `prefixlen` 指定的前缀长度掩码 IPv6 源地址。默认 IPv6 前缀长度为 128 位。

**`table <`** `table`> `above` `hwm` [`below` `lwm`] 当状态数超过 `hwm` 高水位线时将地址添加到指定 `table`。当状态数降至 `lwm` 低水位线以下时，地址将从表中删除。默认低水位线为 0。

通过规则可以使用 `source limiter` `name` 选项指定源限制器。

源限制器的一个示例用途是缓解网络外部网络或端口扫描导致防火墙资源耗尽的拒绝服务。任何一台扫描仪从任何一个源地址创建的状态可以被限制，以避免影响其他源。下面，外部网络中最多 10000 个 IPv4 主机和 IPv6 /64 网络各自限制为最多 1000 个连接，并且限制为在 10 秒间隔内创建 100 个状态：

source limiter "internet" id 1 entries 10000 \
       limit 1000 rate 100/10 \
       inet6 mask 64
block in on egress
pass in on egress source limiter "internet"

## 有状态跟踪选项

许多与有状态跟踪相关的选项可在每条规则上应用。`keep state`、`modulate state` 和 `synproxy state` 支持这些选项，必须显式指定 `keep state` 才能将选项应用于规则。

**`max`** <`number`> 限制规则可创建的并发状态数。达到此限制时，将进一步创建状态的数据包丢弃，直到现有状态超时。

**`no-sync`** 阻止此规则创建的状态的状态更改出现在 [pfsync(4)](../man4/pfsync.4.md) 接口上。

**Xo** <`timeout`> <`seconds`> Xc 更改此规则创建的状态使用的超时值。有关所有有效超时名称的列表，请参见上文的 Sx OPTIONS。

**`sloppy`** 使用完全不检查序列号的松散 TCP 连接跟踪器，这使插入和 ICMP 拆除攻击更容易。这适用于看不到连接所有数据包的情况，例如在非对称路由情况下。不能与 modulate 或 synproxy state 一起使用。

**`pflow`** 此规则创建的状态在 [pflow(4)](../man4/pflow.4.md) 接口上导出。

**`allow-related`** 自动允许与此连接相关的连接，无论可能影响它们的其他规则。目前仅适用于 SCTP 多宿主连接。

可以指定多个选项，用逗号分隔：

```sh
pass in proto tcp from any to any \
      port www keep state \
      (max 100, source-track rule, max-src-nodes 75, \
      max-src-states 3, tcp.established 60, tcp.closing 5)
```

当指定 `source-track` 关键字时，跟踪每个源 IP 的状态数。

**`source-track rule`** 此规则创建的最大状态数受规则的 `max-src-nodes` 和 `max-src-states` 选项限制。只有此特定规则创建的状态条目计入规则的限制。

**`source-track global`** 限制使用此选项的所有规则创建的状态数。每条规则可以指定不同的 `max-src-nodes` 和 `max-src-states` 选项，但任何参与规则创建的状态条目都计入每条单独规则的限制。

可以设置以下限制：

**`max-src-nodes`** <`number`> 限制可同时具有状态表条目的最大源地址数。

**`max-src-states`** <`number`> 限制单个源地址可使用此规则创建的最大并发状态条目数。

对于有状态 TCP 连接，每个源 IP 还可以强制执行已建立连接（已完成 TCP 三次握手的连接）的限制。

**`max-src-conn`** <`number`> 限制单个主机可以建立的最大并发 TCP 连接数（已完成三次握手）。

**Xo** `max-src-conn-rate` <`number`> / <`seconds`> Xc 限制时间间隔内的新连接速率。连接速率是作为移动平均值计算的近似值。

当达到这些限制之一时，将进一步创建状态的数据包丢弃，直到现有状态超时。

由于三次握手确保源地址未被欺骗，可以基于这些限制采取更激进的行动。使用 `overload` <`table`> 状态选项，达到已建立连接任一限制的源 IP 地址将被添加到命名表中。此表可用于规则集中以阻止来自违规主机的进一步活动、将其重定向到 tarpit 进程或限制其带宽。

可选的 `flush` 关键字杀死由匹配规则创建的源自超过这些限制的主机的所有状态。flush 命令的 `global` 修饰符杀死源自违规主机的所有状态，无论哪条规则创建了状态。

例如，以下规则将保护 Web 服务器免受在 10 秒内建立超过 100 个连接的主机的攻击。任何连接速度快于此速率的主机将其地址添加到 <bad_hosts> 表中，并刷新源自它的所有状态。来自此主机的任何新数据包将被阻止规则无条件丢弃。

```sh
block quick from <bad_hosts>
pass in on $ext_if proto tcp to $webserver port www keep state \
	(max-src-conn-rate 100/10, overload <bad_hosts> flush global)
```

## 操作系统指纹识别

被动 OS 指纹识别是一种检查 TCP 连接初始 SYN 数据包细微差别并猜测主机操作系统的机制。不幸的是，这些细微差别很容易被攻击者欺骗，因此指纹对于做出安全决策没有用。但指纹通常足够准确，可以据此做出策略决策。

指纹可以按操作系统类别、版本或子类型/补丁级别指定。操作系统的类别通常是供应商或类型，对于 [pf(4)](../man4/pf.4.md) 防火墙本身，将是 OpenBSD。主 FTP 站点上最旧的可用 OpenBSD 版本将是 2.6，指纹将写为

```sh
"OpenBSD 2.6"
```

操作系统的子类型通常用于描述补丁级别（如果该补丁导致 TCP 栈行为更改）。对于 OpenBSD，唯一的子类型是用于被 `no-df` scrub 选项规范化的指纹，将指定为

```sh
"OpenBSD 3.3 no-df"
```

大多数流行操作系统的指纹由 [pf.os(5)](pf.os.5.md) 提供。一旦 [pf(4)](../man4/pf.4.md) 运行，可以通过运行以下命令列出已知操作系统指纹的完整列表：

```sh
# pfctl -so
```

过滤规则可以在操作系统规范的任何级别强制执行策略，前提是存在指纹。策略可以将流量限制为已批准的操作系统，甚至禁止来自非最新服务包的主机的流量。

`unknown` 类也可用作指纹，它将匹配没有已知操作系统指纹的数据包。

示例：

```sh
pass  out proto tcp from any os OpenBSD
block out proto tcp from any os Doors
block out proto tcp from any os "Doors PT"
block out proto tcp from any os "Doors PT SP3"
block out from any os "unknown"
pass on lo0 proto tcp from any os "OpenBSD 3.3 lo0"
```

操作系统指纹识别仅限于 TCP SYN 数据包。这意味着它不适用于其他协议，也不会匹配当前已建立的连接。

注意事项：操作系统指纹偶尔会出错。存在三个问题：攻击者可以轻松地制作数据包使其看起来像任何操作系统；操作系统补丁可能更改栈行为，在数据库更新之前没有指纹会匹配它；多个操作系统可能具有相同的指纹。

## 阻止欺骗流量

“欺骗” 是 IP 地址的伪造，通常用于恶意目的。`antispoof` 指令展开为一组过滤规则，这些规则将阻止来自直接连接到指定接口的网络（们）的源 IP 的所有流量通过任何其他接口进入系统。

例如，行

```sh
antispoof for lo0
```

展开为

```sh
block drop in on ! lo0 inet from 127.0.0.1/8 to any
block drop in on ! lo0 inet6 from ::1 to any
```

对于非回环接口，还有额外的规则来阻止源 IP 地址与接口 IP（们）相同的传入数据包。例如，假设接口 wi0 的 IP 地址为 10.0.0.1，子网掩码为 255.255.255.0，行

```sh
antispoof for wi0 inet
```

展开为

```sh
block drop in on ! wi0 inet from 10.0.0.0/24 to any
block drop in inet from 10.0.0.1 to any
```

注意事项：由 `antispoof` 指令创建的规则会干扰通过回环接口发送到本地地址的数据包。应显式通过这些数据包。

## 分片处理

IP 数据报（数据包）的大小可能显著大于网络的最大传输单元（MTU）。在需要或更高效地发送此类大数据包的情况下，大数据包将被分片为多个较小的数据包，每个都能放入网络线路。不幸的是，对于防火墙设备，只有第一个逻辑分片包含允许 [pf(4)](../man4/pf.4.md) 过滤 TCP 端口等内容或执行 NAT 的子协议所需的头信息。

除了使用上文中 Sx TRAFFIC NORMALIZATION 描述的 `set reassemble` 选项或 `scrub` 规则外，包过滤器中还有三个处理分片的选项。

一种替代方法是使用过滤规则过滤单个分片。如果没有 `scrub` 规则适用于分片或将 `set reassemble` 设置为 `no`，则将其传递给过滤器。具有匹配 IP 头参数的过滤规则决定分片是通过还是阻止，方式与过滤完整数据包相同。在没有重组的情况下，分片只能基于 IP 头字段（源/目标地址、协议）进行过滤，因为子协议头字段不可用（TCP/UDP 端口号、ICMP 代码/类型）。`fragment` 选项可用于将过滤规则限制为仅适用于分片，而不适用于完整数据包。未指定 `fragment` 选项的过滤规则如果仅指定 IP 头字段，仍适用于分片。例如，规则

```sh
pass in proto tcp from any to any port 80
```

从不适用于分片，即使分片是目标端口为 80 的 TCP 数据包的一部分，因为在没有重组的情况下，此信息对每个分片不可用。这也意味着分片无法创建新的或匹配现有的状态表条目，这使得分片的有状态过滤和地址转换（NAT、重定向）不可能。

还可以通过在 `scrub` 规则中将源或目标地址或协议指定为参数来仅重组某些分片。

在大多数情况下，重组的好处超过额外的内存成本，建议使用 `set reassemble` 选项或带有 `fragment reassemble` 修饰符的 `scrub` 规则来重组所有分片。

用于分片缓存的内存可以使用 pfctl(8) 进行限制。一旦达到此限制，必须缓存的分片将被丢弃，直到其他条目超时。超时值也可以调整。

当转发重组的 IPv6 数据包时，pf 使用原始最大分片大小对其进行重新分片。这允许发送方通过路径 MTU 发现确定最佳分片大小。

## 锚点

除了主规则集外，pfctl(8) 还可以将规则集加载到 `anchor` 附加点。`anchor` 是一个可以容纳规则、地址表和其他锚点的容器。

锚点有一个名称，指定了 pfctl(8) 可用于访问锚点以对其执行操作的路径，例如将子锚点附加到它或向其加载规则。锚点可以嵌套，组件以 ‘/’ 字符分隔，类似于文件系统层次结构的布局。主规则集实际上是默认锚点，因此过滤和转换规则等也可以包含在任何锚点中。

锚点可以使用以下类型的规则引用另一个 `anchor` 附加点：

**`nat-anchor`** <`name`> 评估指定 `anchor` 中的 `nat` 规则。

**`rdr-anchor`** <`name`> 评估指定 `anchor` 中的 `rdr` 规则。

**`binat-anchor`** <`name`> 评估指定 `anchor` 中的 `binat` 规则。

**`anchor`** <`name`> 评估指定 `anchor` 中的过滤规则。

**Xo** `load anchor` <`name`> `from` <`file`> Xc 将指定文件中的规则加载到锚点 `name` 中。

当主规则集的评估到达 `anchor` 规则时，[pf(4)](../man4/pf.4.md) 将继续评估该锚点中指定的所有规则。

标记有 `quick` 选项的匹配过滤和转换规则是最终的，并中止其他锚点和主规则集中规则的评估。如果 `anchor` 本身标记有 `quick` 选项，则当锚点退出时，如果数据包被锚点内的任何规则匹配，规则集评估将终止。

`anchor` 规则相对于包含它们的锚点进行评估。例如，主规则集中指定的所有 `anchor` 规则将引用主规则集下的锚点附加点，而从 `load anchor` 规则加载的文件中指定的 `anchor` 规则将附加在该锚点下。

当主规则集加载时，规则可以包含在不包含任何规则的 `anchor` 附加点中，稍后可以通过 pfctl(8) 操作此类锚点，而无需重新加载主规则集或其他锚点。例如，

```sh
ext_if = "kue0"
block on $ext_if all
anchor spam
pass out on $ext_if all
pass in on $ext_if proto tcp from any \
      to $ext_if port smtp
```

默认阻止外部接口上的所有数据包，然后评估名为 “spam” 的 `anchor` 中的所有规则，最后通过所有传出连接和到端口 25 的传入连接。

```sh
# echo "block in quick from 1.2.3.4 to any" | \
      pfctl -a spam -f -
```

这会将单个规则加载到 `anchor` 中，该规则阻止来自特定地址的所有数据包。

还可以通过在 `anchor` 规则之后添加 `load anchor` 规则来填充锚点：

```sh
anchor spam
load anchor spam from "/etc/pf-spam.conf"
```

当 pfctl(8) 加载 `pf.conf` 时，它还将从文件 **/etc/pf-spam.conf** 加载所有规则到锚点中。

可选地，`anchor` 规则可以使用与过滤规则相同的语法指定包过滤参数。使用参数时，`anchor` 规则仅针对匹配的数据包进行评估。这允许有条件地评估锚点，如：

```sh
block on $ext_if all
anchor spam proto tcp from any to any port smtp
pass out on $ext_if all
pass in on $ext_if proto tcp from any to $ext_if port smtp
```

`anchor` spam 内的规则仅针对目标端口为 25 的 `tcp` 数据包进行评估。因此，

```sh
# echo "block in quick from 1.2.3.4 to any" | \
      pfctl -a spam -f -
```

仅阻止从 1.2.3.4 到端口 25 的连接。

锚点可以以星号（‘*’）字符结尾，这表示应按锚点名称的字母顺序评估在该点附加的所有锚点。例如，

```sh
anchor "spam/*"
```

将评估附加到 `spam` 锚点的每个锚点中的每条规则。注意，它仅评估直接附加到 `spam` 锚点的锚点，不会递归下降评估锚点。

由于锚点相对于包含它们的锚点进行评估，因此有一种机制可以访问给定锚点的父级和祖先锚点。类似于文件系统路径名解析，如果序列 “..” 作为锚点路径组件出现，则路径评估中该点的当前锚点的父锚点将成为新的当前锚点。例如，考虑以下：

```sh
# echo ' anchor "spam/allowed" ' | pfctl -f -
# echo -e ' anchor "../banned" \n pass' | \
      pfctl -a spam/allowed -f -
```

主规则集的评估将引导到 `spam/allowed` 锚点，该锚点将评估 `spam/banned` 锚点中的规则（如果有），然后最终评估 `pass` 规则。

`anchor` 规则还可以在花括号分隔的块中包含过滤规则集。在这种情况下，不需要单独将规则加载到锚点中。花括号分隔的块可以包含规则或其他花括号分隔的块。以这种方式填充锚点时，锚点名称变为可选。

```sh
anchor "external" on $ext_if {
	block
	anchor out {
		pass proto tcp from any to port { 25, 80, 443 }
	}
	pass in proto tcp to any port 22
}
```

由于锚点名称的解析器规范是字符串，因此对包含 ‘/’ 字符的锚点名称的任何引用都需要在锚点名称周围使用双引号（‘"’）字符。

## SCTP 注意事项

[pf(4)](../man4/pf.4.md) 支持 [sctp(4)](../man4/sctp.4.md) 连接。它可以匹配端口、跟踪状态和 NAT SCTP 流量。但是，它不会在 nat 或 rdr 转换期间更改端口号。这样做会破坏 SCTP 多宿主。

## 转换实例

此示例将端口 80 上的传入请求映射到端口 8080，守护进程在该端口上运行（例如，因为它不以 root 身份运行，因此没有权限绑定到端口 80）。

```sh
# 使用宏定义接口名，以便轻松更改
ext_if = "ne3"
# 将 8080 上的守护进程映射为看起来在 80 上
match in on $ext_if proto tcp from any to any port 80 \
      rdr-to 127.0.0.1 port 8080
```

如果 `pass` 规则与 `quick` 修饰符一起使用，匹配转换规则的数据包通过而不检查后续过滤规则：

```sh
pass in quick on $ext_if proto tcp from any to any port 80 \
      rdr-to 127.0.0.1 port 8080
```

在下面的示例中，vlan12 配置为 192.168.168.1；机器将来自 192.168.168.0/24 的所有数据包在通过除 vlan12 之外的任何接口外出时转换为 204.92.77.111。这具有使来自 192.168.168.0/24 网络的流量对路由器上除 vlan12 上的节点之外的任何接口后面的节点显示为 Internet 可路由地址 204.92.77.111 的净效果。（因此，192.168.168.1 可以与 192.168.168.0/24 节点通信。）

```sh
match out on ! vlan12 from 192.168.168.0/24 to any nat-to 204.92.77.111
```

此更长的示例同时使用 NAT 和重定向。外部接口的地址为 157.161.48.183。在本地主机上，我们运行 [ftp-proxy(8)](../man8/ftp-proxy.8.md)，等待 FTP 会话被重定向到它。[ftp-proxy(8)](../man8/ftp-proxy.8.md) 的三个必需锚点在此示例中省略；参见 [ftp-proxy(8)](../man8/ftp-proxy.8.md) 手册页。

```sh
# NAT
# 转换传出数据包的源地址（任何协议）。
# 在这种情况下，除网关外部地址之外的任何地址都被映射。
pass out on $ext_if inet from ! ($ext_if) to any nat-to ($ext_if)
# NAT 代理
# 将传出数据包的源端口映射到分配的代理端口，而不是
# 任意端口。
# 在这种情况下，代理传出 isakmp 在网关上使用端口 500。
pass out on $ext_if inet proto udp from any port = isakmp to any \
      nat-to ($ext_if) port 500
# BINAT
# 转换传出数据包的源地址（任何协议）。
# 将传入数据包的目标地址转换为内部机器
# （双向）。
pass on $ext_if from 10.1.2.150 to any binat-to $ext_if
# 转换到达 $peer_if 上寻址到 172.22.16.0/20 的数据包
# 到 172.21.16.0/20 中的相应地址（双向）。
pass on $peer_if from 172.21.16.0/20 to any binat-to 172.22.16.0/20
# RDR
# 转换传入数据包的目标地址。
# 例如，将 TCP 和 UDP 端口重定向到内部机器。
pass in on $ext_if inet proto tcp from any to ($ext_if) port 8080 \
      rdr-to 10.1.2.151 port 22
pass in on $ext_if inet proto udp from any to ($ext_if) port 8080 \
      rdr-to 10.1.2.151 port 53
# RDR
# 转换传出 ftp 控制连接以将其发送到本地主机
# 以便与在端口 8021 上运行的 ftp-proxy(8) 代理。
pass in on $int_if proto tcp from any to any port 21 \
      rdr-to 127.0.0.1 port 8021
```

在此示例中，设置了 NAT 网关以使用公共地址池（192.0.2.16/28）转换内部地址，并将传入的 Web 服务器连接重定向到内部网络上的 Web 服务器组。

```sh
# NAT 负载平衡
# 使用地址池转换传出数据包的源地址。
# 通过使用 source-hash 关键字，给定源地址始终转换为
# 相同的池地址。
pass out on $ext_if inet from any to any nat-to 192.0.2.16/28 source-hash
# RDR 轮询
# 将传入的 Web 服务器连接转换到内部网络上的
# 一组 Web 服务器。
pass in on $ext_if proto tcp from any to any port 80 \
      rdr-to { 10.1.2.155, 10.1.2.160, 10.1.2.161 } round-robin
```

## 兼容性转换实例

在下面的示例中，机器位于伪造的内部 144.19.74.* 网络和可路由的外部 IP 204.92.77.100 之间。`no nat` 规则排除协议 AH 被转换。

```sh
# NAT
no nat on $ext_if proto ah from 144.19.74.0/24 to any
nat on $ext_if from 144.19.74.0/24 to any -> 204.92.77.100
```

在下面的示例中，绑定到一个特定服务器的数据包以及系统管理员生成的数据包不被代理；所有其他连接都被代理。

```sh
# RDR
no rdr on $int_if proto { tcp, udp } from any to $server port 80
no rdr on $int_if proto { tcp, udp } from $sysadmins to any port 80
rdr on $int_if proto { tcp, udp } from any to any port 80 \
      -> 127.0.0.1 port 80
```

## 过滤实例

```sh
# 外部接口是 kue0
# (157.161.48.183，唯一的可路由地址)
# 专用网络是 10.0.0.0/8，我们正在为其进行 NAT。
# 重组传入流量
set reassemble yes
# 使用宏定义接口名，以便轻松更改
ext_if = "kue0"
# 默认阻止并记录所有内容
block return log on $ext_if all
# 阻止来自我们没有返回路由的源的所有内容
block in from no-route to any
# 阻止其入口接口与到其源地址的路由中的接口不匹配的数据包
block in from urpf-failed to any
# 阻止并记录不具有我们地址作为源的传出数据包，
# 它们要么被欺骗，要么配置错误（例如 NAT 被禁用），
# 我们希望友好，不发垃圾。
block out log quick on $ext_if from ! 157.161.48.183 to any
# 静默丢弃广播（电缆调制解调器噪声）
block in quick on $ext_if from any to 255.255.255.255
# 阻止并记录来自保留地址空间和无效地址的传入数据包，
# 它们要么被欺骗，要么配置错误，我们无论如何都无法回复
# （因此不返回 rst）。
block in log quick on $ext_if from { 10.0.0.0/8, 172.16.0.0/12, \
      192.168.0.0/16, 255.255.255.255/32 } to any
# ICMP
# 通过某些 ICMP 查询并保持状态 (ping)
# 状态匹配基于主机地址和 ICMP id（不是类型/代码），
# 因此回复（如 8/0 的 0/0）将匹配查询
# ICMP 错误消息（始终引用 TCP/UDP 数据包）由
# TCP/UDP 状态处理
pass on $ext_if inet proto icmp all icmp-type 8 code 0
# UDP
# 通过所有 UDP 连接并保持状态
pass out on $ext_if proto udp all
# 通过某些 UDP 连接并保持状态 (DNS)
pass in on $ext_if proto udp from any to any port domain
# TCP
# 通过所有 TCP 连接并调制状态
pass out on $ext_if proto tcp all modulate state
# 通过某些 TCP 连接并保持状态 (SSH, SMTP, DNS, IDENT)
pass in on $ext_if proto tcp from any to any port { ssh, smtp, domain, \
      auth }
# 不允许 Windows 9x SMTP 连接，因为它们通常是
# 病毒蠕虫。或者我们可以将这些 OS 限制为每个 1 个连接。
block in on $ext_if proto tcp from any os {"Windows 95", "Windows 98"} \
      to any port smtp
# IPv6
# 通过所有 IPv6 流量：注意，我们必须以两种不同的方式启用此功能，
# 在我们的物理接口和我们的隧道上
pass quick on gif0 inet6
pass quick on $ext_if proto ipv6
# 数据包标记
# 三个接口：$int_if、$ext_if 和 $wifi_if（无线）。NAT 在 $ext_if 上对所有传出数据包进行。
# 标记 $int_if 上的传入数据包，并在 $ext_if 上通过这些标记的数据包。
# 所有其他传出数据包（即来自无线网络的数据包）仅允许访问端口 80。
pass in on $int_if from any to any tag INTNET
pass in on $wifi_if from any to any
block out on $ext_if from any to any
pass out quick on $ext_if tagged INTNET
pass out on $ext_if proto tcp from any to any port 80
# 标记传入数据包，因为它们被重定向到 spamd(8)。使用标记
# 通过包过滤器传递这些数据包。
rdr on $ext_if inet proto tcp from <spammers> to port smtp \
	tag SPAMD -> 127.0.0.1 port spamd
block in on $ext_if
pass in on $ext_if inet proto tcp tagged SPAMD
```

在下面的示例中，处理两个地址族的路由器使用众所周知的 64:ff9b::/96 前缀将内部 IPv4 子网转换为 IPv6：

```sh
pass in on $v4_if inet af-to inet6 from ($v6_if) to 64:ff9b::/96
```

与上面的示例配对，下面的示例可在另一个处理两个地址族的路由器上使用以转换回 IPv4：

```sh
pass in on $v6_if inet6 to 64:ff9b::/96 af-to inet from ($v4_if)
```

## 语法

`pf.conf` 的 BNF 语法：

```sh
line           = ( option | ether-rule | pf-rule | nat-rule | binat-rule |
                 rdr-rule | antispoof-rule | altq-rule | queue-rule |
                 trans-anchors | anchor-rule | anchor-close | load-anchor |
                 table-rule | include )
option         = "set" ( [ "timeout" ( timeout | "{" timeout-list "}" ) ] |
                 [ "ruleset-optimization" [ "none" | "basic" | "profile" ]] |
                 [ "optimization" [ "default" | "normal" |
                 "high-latency" | "satellite" |
                 "aggressive" | "conservative" ] ]
                 [ "limit" ( limit-item | "{" limit-list "}" ) ] |
                 [ "loginterface" ( interface-name | "none" ) ] |
                 [ "block-policy" ( "drop" | "return" ) ] |
                 [ "state-policy" ( "if-bound" | "floating" ) ]
                 [ "state-defaults" state-opts ]
                 [ "require-order" ( "yes" | "no" ) ]
                 [ "fingerprints" filename ] |
                 [ "skip on" ifspec ] |
                 [ "debug" ( "none" | "urgent" | "misc" | "loud" ) ]
                 [ "keepcounters" ] )
ether-rule     = "ether" etheraction [ ( "in" | "out" ) ]
                 [ "quick" ] [ "on" ifspec ] [ "bridge-to" interface-name ]
                 [ etherprotospec ] [ etherhosts ] [ "l3" hosts ]
                 [ etherfilteropt-list ]
pf-rule        = action [ ( "in" | "out" ) ]
                 [ "log" [ "(" logopts ")"] ] [ "quick" ]
                 [ "on" ifspec ] [ route ] [ af ] [ protospec ]
                 [ hosts ] [ filteropt-list ]
logopts        = logopt [ "," logopts ]
logopt         = "all" | "matches" | "user" | "to" interface-name
etherfilteropt-list = etherfilteropt-list etherfilteropt | etherfilteropt
etherfilteropt = "tag" string | "tagged" string | "queue" ( string ) |
                 "ridentifier" number | "label" string
filteropt-list = filteropt-list filteropt | filteropt
filteropt      = user | group | flags | icmp-type | icmp6-type | "tos" tos |
                 "af-to" af "from" ( redirhost | "{" redirhost-list "}" )
                 [ "to" ( redirhost | "{" redirhost-list "}" ) ] |
                 ( "no" | "keep" | "modulate" | "synproxy" ) "state"
                 [ "(" state-opts ")" ] |
                 "fragment" | "no-df" | "min-ttl" number | "set-tos" tos |
                 "max-mss" number | "random-id" | "reassemble tcp" |
                 fragmentation | "allow-opts" | "once" |
                 "label" string | "tag" string | [ "!" ] "tagged" string |
                 "max-pkt-rate" number "/" seconds |
                 "set prio" ( number | "(" number [ [ "," ] number ] ")" ) |
                 "max-pkt-size" number |
                 "queue" ( string | "(" string [ [ "," ] string ] ")" ) |
                 "rtable" number | "probability" number"%" | "prio" number |
                 "state limiter" name |
                 "state limiter" name "(" limiter-opts ")" |
                 "source limiter" name |
                 "source limiter" name "(" limiter-opts ")" | "prio" number |
                 "dnpipe" ( number | "(" number "," number ")" ) |
                 "dnqueue" ( number | "(" number "," number ")" ) |
                 "ridentifier" number |
                 "binat-to" ( redirhost | "{" redirhost-list "}" )
                 [ portspec ] [ pooltype ] |
                 "rdr-to" ( redirhost | "{" redirhost-list "}" )
                 [ portspec ] [ pooltype ] |
                 "nat-to" ( redirhost | "{" redirhost-list "}" )
                 [ portspec ] [ pooltype ] [ "static-port" ] |
                 [ ! ] "received-on" ( interface-name | interface-group )
nat-rule       = [ "no" ] "nat" [ "pass" [ "log" [ "(" logopts ")" ] ] ]
                 [ "on" ifspec ] [ af ]
                 [ protospec ] hosts [ "tag" string ] [ "tagged" string ]
                 [ "->" ( redirhost | "{" redirhost-list "}" )
                 [ portspec ] [ pooltype ] [ "static-port" ]
                 [ "map-e-portset" number "/" number "/" number ] ]
binat-rule     = [ "no" ] "binat" [ "pass" [ "log" [ "(" logopts ")" ] ] ]
                 [ "on" interface-name ] [ af ]
                 [ "proto" ( proto-name | proto-number ) ]
                 "from" address [ "/" mask-bits ] "to" ipspec
                 [ "tag" string ] [ "tagged" string ]
                 [ "->" address [ "/" mask-bits ] ]
rdr-rule       = [ "no" ] "rdr" [ "pass" [ "log" [ "(" logopts ")" ] ] ]
                 [ "on" ifspec ] [ af ]
                 [ protospec ] hosts [ "tag" string ] [ "tagged" string ]
                 [ "->" ( redirhost | "{" redirhost-list "}" )
                 [ portspec ] [ pooltype ] ]
antispoof-rule = "antispoof" [ "log" ] [ "quick" ]
                 "for" ifspec [ af ] [ "label" string ]
                 [ "ridentifier" number ]
table-rule     = "table" "<" string ">" [ tableopts-list ]
tableopts-list = tableopts-list tableopts | tableopts
tableopts      = "persist" | "const" | "counters" | "file" string |
                 "{" [ tableaddr-list ] "}"
tableaddr-list = tableaddr-list [ "," ] tableaddr-spec | tableaddr-spec
tableaddr-spec = [ "!" ] tableaddr [ "/" mask-bits ]
tableaddr      = hostname | ifspec | "self" |
                 ipv4-dotted-quad | ipv6-coloned-hex
altq-rule      = "altq on" interface-name queueopts-list
                 "queue" subqueue
queue-rule     = "queue" string [ "on" interface-name ] queueopts-list
                 subqueue
anchor-rule    = "anchor" [ string ] [ ( "in" | "out" ) ] [ "on" ifspec ]
                 [ af ] [ protospec ] [ hosts ] [ filteropt-list ] [ "{" ]
anchor-close   = "}"
trans-anchors  = ( "nat-anchor" | "rdr-anchor" | "binat-anchor" ) string
                 [ "on" ifspec ] [ af ] [ "proto" ] [ protospec ] [ hosts ]
load-anchor    = "load anchor" string "from" filename
queueopts-list = queueopts-list queueopts | queueopts
queueopts      = [ "bandwidth" bandwidth-spec ] |
                 [ "qlimit" number ] | [ "tbrsize" number ] |
                 [ "priority" number ] | [ schedulers ]
schedulers     = ( cbq-def | priq-def | hfsc-def )
bandwidth-spec = "number" ( "b" | "Kb" | "Mb" | "Gb" | "%" )
etheraction    = "pass" | "block"
action         = "pass" | "match" | "block" [ return ] | [ "no" ] "scrub"
return         = "drop" | "return" | "return-rst" [ "( ttl" number ")" ] |
                 "return-icmp" [ "(" icmpcode [ [ "," ] icmp6code ] ")" ] |
                 "return-icmp6" [ "(" icmp6code ")" ]
icmpcode       = ( icmp-code-name | icmp-code-number )
icmp6code      = ( icmp6-code-name | icmp6-code-number )
ifspec         = ( [ "!" ] ( interface-name | interface-group ) ) |
                 "{" interface-list "}"
interface-list = [ "!" ] ( interface-name | interface-group )
                 [ [ "," ] interface-list ]
route          = ( "route-to" | "reply-to" | "dup-to" )
                 ( routehost | "{" routehost-list "}" )
                 [ pooltype ]
af             = "inet" | "inet6"
etherprotospec = "proto" ( proto-number | "{" etherproto-list "}" )
etherproto-list	= proto-number [ [ "," ] etherproto-list ]
protospec      = "proto" ( proto-name | proto-number |
                 "{" proto-list "}" )
proto-list     = ( proto-name | proto-number ) [ [ "," ] proto-list ]
etherhosts     = "from" macaddress "to" macaddress
macaddress     = mac | mac "/" masklen | mac "&" mask
hosts          = "all" |
                 "from" ( "any" | "no-route" | "urpf-failed" | "self" | host |
                 "{" host-list "}" ) [ port ] [ os ]
                 "to"   ( "any" | "no-route" | "self" | host |
                 "{" host-list "}" ) [ port ]
ipspec         = "any" | host | "{" host-list "}"
host           = [ "!" ] ( address [ "/" mask-bits ] | "<" string ">" )
redirhost      = address [ "/" mask-bits ]
routehost      = "(" interface-name address [ "/" mask-bits ] ")"
address        = ( interface-name | interface-group |
                 "(" ( interface-name | interface-group ) ")" |
                 hostname | ipv4-dotted-quad | ipv6-coloned-hex )
host-list      = host [ [ "," ] host-list ]
redirhost-list = redirhost [ [ "," ] redirhost-list ]
routehost-list = routehost [ [ "," ] routehost-list ]
port           = "port" ( unary-op | binary-op | "{" op-list "}" )
portspec       = "port" ( number | name ) [ ":" ( "*" | number | name ) ]
os             = "os"  ( os-name | "{" os-list "}" )
user           = "user" ( unary-op | binary-op | "{" op-list "}" )
group          = "group" ( unary-op | binary-op | "{" op-list "}" )
unary-op       = [ "=" | "!=" | "<" | "<=" | ">" | ">=" ]
                 ( name | number )
binary-op      = number ( "<>" | "><" | ":" ) number
op-list        = ( unary-op | binary-op ) [ [ "," ] op-list ]
os-name        = operating-system-name
os-list        = os-name [ [ "," ] os-list ]
flags          = "flags" ( [ flag-set ] "/"  flag-set | "any" )
flag-set       = [ "F" ] [ "S" ] [ "R" ] [ "P" ] [ "A" ] [ "U" ] [ "E" ]
                 [ "W" ]
icmp-type      = "icmp-type" ( icmp-type-code | "{" icmp-list "}" )
icmp6-type     = "icmp6-type" ( icmp-type-code | "{" icmp-list "}" )
icmp-type-code = ( icmp-type-name | icmp-type-number )
                 [ "code" ( icmp-code-name | icmp-code-number ) ]
icmp-list      = icmp-type-code [ [ "," ] icmp-list ]
tos            = ( "lowdelay" | "throughput" | "reliability" |
                 [ "0x" ] number )
state-opts     = state-opt [ [ "," ] state-opts ]
state-opt      = ( "max" number | "no-sync" | timeout | "sloppy" |
                 "source-track" [ ( "rule" | "global" ) ] |
                 "max-src-nodes" number | "max-src-states" number |
                 "max-src-conn" number |
                 "max-src-conn-rate" number "/" number |
                 "overload" "<" string ">" [ "flush" ] |
                 "if-bound" | "floating" | "pflow" )
fragmentation  = [ "fragment reassemble" ]
timeout-list   = timeout [ [ "," ] timeout-list ]
timeout        = ( "tcp.first" | "tcp.opening" | "tcp.established" |
                 "tcp.closing" | "tcp.finwait" | "tcp.closed" | "tcp.tsdiff" |
                 "sctp.first" | "sctp.opening" | "sctp.established" |
                 "sctp.closing" | "sctp.closed" |
                 "udp.first" | "udp.single" | "udp.multiple" |
                 "icmp.first" | "icmp.error" |
                 "other.first" | "other.single" | "other.multiple" |
                 "frag" | "interval" | "src.track" |
                 "adaptive.start" | "adaptive.end" ) number
limit-list     = limit-item [ [ "," ] limit-list ]
limit-item     = ( "states" | "frags" | "src-nodes" ) number
pooltype       = ( "bitmask" | "random" |
                 "source-hash" [ ( hex-key | string-key ) ] |
                 "round-robin" ) [ sticky-address | prefer-ipv6-nexthop ]
subqueue       = string | "{" queue-list "}"
queue-list     = string [ [ "," ] string ]
cbq-def        = "cbq" [ "(" cbq-opt [ [ "," ] cbq-opt ] ")" ]
priq-def       = "priq" [ "(" priq-opt [ [ "," ] priq-opt ] ")" ]
hfsc-def       = "hfsc" [ "(" hfsc-opt [ [ "," ] hfsc-opt ] ")" ]
cbq-opt        = ( "default" | "borrow" | "red" | "ecn" | "rio" )
priq-opt       = ( "default" | "red" | "ecn" | "rio" )
hfsc-opt       = ( "default" | "red" | "ecn" | "rio" |
                 linkshare-sc | realtime-sc | upperlimit-sc )
linkshare-sc   = "linkshare" sc-spec
realtime-sc    = "realtime" sc-spec
upperlimit-sc  = "upperlimit" sc-spec
sc-spec        = ( bandwidth-spec |
                 "(" bandwidth-spec number bandwidth-spec ")" )
limiter-opts   = "block" | "no-match"
include        = "include" filename
```

## 文件

**/etc/hosts** 主机名数据库。

**/etc/pf.conf** 规则集文件的默认位置。该文件必须手动创建，因为标准安装不会安装它。

**/etc/pf.os** OS 指纹的默认位置。

**/etc/protocols** 协议名数据库。

**/etc/services** 服务名数据库。

## 参见

[altq(4)](../man4/altq.4.md), [carp(4)](../man4/carp.4.md), [icmp(4)](../man4/icmp.4.md), [icmp6(4)](../man4/icmp6.4.md), [ip(4)](../man4/ip.4.md), [ip6(4)](../man4/ip6.4.md), [pf(4)](../man4/pf.4.md), [pflow(4)](../man4/pflow.4.md), [pfsync(4)](../man4/pfsync.4.md), [sctp(4)](../man4/sctp.4.md), [tcp(4)](../man4/tcp.4.md), [udp(4)](../man4/udp.4.md), [hosts(5)](hosts.5.md), [pf.os(5)](pf.os.5.md), [protocols(5)](protocols.5.md), [services(5)](services.5.md), [ftp-proxy(8)](../man8/ftp-proxy.8.md), pfctl(8), pflogd(8)

## 历史

`pf.conf` 文件格式首次出现在 OpenBSD 3.0 中。
