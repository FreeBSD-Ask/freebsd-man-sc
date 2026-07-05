# gif.4

`gif` — 通用隧道接口

## 名称

`gif`

## 概要

`device gif`

## 描述

`gif` 接口是用于 IPv4 和 IPv6 的通用隧道设备。它可以在 IPv[46] 之上对 IPv[46] 流量进行隧道封装，因此共有四种可能的配置。`gif` 的行为主要基于 RFC2893 IPv6-over-IPv4 配置隧道。在 NetBSD 上，`gif` 还可以使用 EON 封装在 IPv[46] 之上对 ISO 流量进行隧道封装。注意，`gif` 不执行 GRE 封装；如需 GRE 封装，请使用 [gre(4)](gre.4.md)。

当与 if_bridge(4) 接口结合使用 EtherIP 协议时，`gif` 接口也可以在 IPv4 或 IPv6 之上对以太网流量进行隧道封装。详细设置请参见 if_bridge(4)。

每个 `gif` 接口都在运行时通过接口克隆创建。最简单的方法是使用“`ifconfig` `create`”命令，或在 [rc.conf(5)](../man5/rc.conf.5.md) 中使用 `ifconfig_`<`interface`> 变量。

要使用 `gif`，管理员需要配置用于外部头部的协议和地址。这可以通过 [ifconfig(8)](../man8/ifconfig.8.md) `tunnel` 或 `SIOCSIFPHYADDR` ioctl 来完成。管理员还需要使用 [ifconfig(8)](../man8/ifconfig.8.md) 配置内部头部的协议和地址。注意，IPv6 链路本地地址（以 `fe80::` 开头的地址）会在可能时自动配置。如果你想禁用 IPv6 作为内部头部（例如需要纯 IPv4-over-IPv6 隧道），可能需要使用 [ifconfig(8)](../man8/ifconfig.8.md) 手动删除 IPv6 链路本地地址。最后，必须修改路由表，使数据包通过 `gif` 接口路由。

### MTU 配置与路径 MTU 发现

`gif` 接口使用固定长度 `1280` 来判断是否对发出的 IPv6 数据包进行分片。这意味着当外部协议为 IPv6 时，接口上配置的 MTU 值将被忽略。当设置了 `NOCLAMP` 接口标志时，`gif` 使用与 IPv4 通信相同的已配置值。此行为可避免路径 MTU 小于接口 MTU 时可能出现的潜在问题。本节描述默认行为不同的原因。可以使用以下命令设置 `NOCLAMP` 接口标志：

```sh
ifconfig `gif0` `noclamp`
```

并使用以下命令清除该标志：

```sh
ifconfig `gif0` `-noclamp`
```

其中 `gif0` 是实际的接口名。

由于额外的头部，隧道接口的内部协议 MTU 总是隐式小于外部协议 MTU。注意，`gif` 接口上的接口 MTU（默认值为 `1280`）用作外部协议的 MTU。这意味着内部协议的 MTU 会根据外部协议头部长度而变化。如果到达 `gif` 接口准备封装的发出数据包大于内部协议 MTU，它将被分片。具体而言，如果 IPv4 用作外部协议，内部 MTU 比接口 MTU 小 20 字节。在默认接口 MTU `1280` 的情况下，大于 `1260` 的内部数据包将被分片。对于 IPv6，内部 MTU 比外部小 40 字节。

这种分片并无害处，但可能降低性能。注意，虽然增大 `gif` 接口上的 MTU 有助于缓解性能下降的问题，但同时也可能导致 IPv6 中两个通信端点之间最窄中间路径上的数据包丢失。IPv6 仅允许发送方分片，不允许通信路径上的路由器分片。较大的发出数据包会在 MTU 较小的路由器上被丢弃。

在正常的 IPv6 通信中，ICMPv6 Packet Too Big 错误会被回送给发送方，发送方可以调整数据包长度并重新发送。此过程在高于 L3 的上层协议（如 TCP）中执行，使数据包长度变短，从而让数据包无需分片即可通过路径。此行为称为路径 MTU 发现。

使用 `gif` 接口时，Packet Too Big 消息是为外部协议生成的。由于 `gif` 接口不会将此错误转换到内部协议，内部协议只会将其视为数据包丢失，无法获得用于调整后续数据包长度的有用信息。在这种情况下，路径 MTU 发现不起作用，内部协议的通信会陷入停滞。

为避免此问题，即使接口 MTU 配置为大于 1280，`gif` 接口也会静默地将超过 1240 字节的数据包分片，使外部协议数据包等于或短于 1280 字节。注意，此情况仅在外部协议为 IPv6 时发生。`1280` 是 IPv6 中最小的 MTU，可保证中间路由器不发生数据包丢失。

如前所述，如果实际路径 MTU 大于 `1280`，性能并非最优。一个典型的令人困惑的场景如下：`gif` 接口可以将以太网（其 MTU 通常为 1500）作为内部协议。这称为 EtherIP 隧道，可以通过将 `gif` 接口添加为 if_bridge(4) 接口的成员来配置。if_bridge(4) 接口会强制将 `gif` 接口的 MTU 更改为其他成员接口的 MTU，很可能为 1500。这种情况下，会出现 `gif` 接口 MTU 为 1500 但始终以 1280 字节分片的情况。

默认行为最为保守，可避免令人困惑的数据包丢失。根据网络配置，启用 `NOCLAMP` 接口标志可能有助于提升性能。启用此标志时，确保路径 MTU 等于或大于接口 MTU 至关重要。

### 对 ECN 友好的行为

`gif` 设备可配置为对 ECN 友好，如 `draft-ietf-ipsec-ecn-02.txt` 所述。默认关闭，可通过 `IFF_LINK1` 接口标志开启。

不带 `IFF_LINK1` 时，`gif` 将显示 RFC2893 中描述的正常行为。可总结如下：

**入口** 将外部 TOS 位设置为 `0`。

**出口** 丢弃外部 TOS 位。

带 `IFF_LINK1` 时，`gif` 会在出口和入口复制 ECN 位（IPv4 TOS 字节或 IPv6 流量类别字节上的 `0x02` 和 `0x01`），如下所示：

**入口** 从内部到外部复制除 ECN CE 以外的 TOS 位（以 `0xfe` 屏蔽）。将 ECN CE 位设置为 `0`。

**出口** 使用内部 TOS 位并做某些更改。如果外部 ECN CE 位为 `1`，则在内部启用 ECN CE 位。

注意，对 ECN 友好的行为违反 RFC2893。应在与对端达成一致后使用。

### 安全

恶意方可能尝试通过隧道数据包绕过安全过滤。为提供更好的保护，`gif` 在出口对外部源地址执行 martian 和入口过滤。注意，martian/入口过滤器并不完整。你可能需要使用包过滤器来保护节点。入口过滤可能在非对称路由网络中破坏隧道操作。可通过 `IFF_LINK2` 位关闭。

### 杂项

默认情况下，`gif` 隧道不能嵌套。可在运行时通过将 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.gif.max_nesting` 设置为所需的嵌套级别来修改此行为。

## 参见

[gre(4)](gre.4.md), if_bridge(4), [inet(4)](inet.4.md), [inet6(4)](inet6.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> R. Gilligan, E. Nordmark, "Transition Mechanisms for IPv6 Hosts and Routers", *RFC2893*, August 2000.

> Sally Floyd, David L. Black, K. K. Ramakrishnan, "IPsec Interactions with ECN", December 1999, draft-ietf-ipsec-ecn-02.txt.

> R. Housley, S. Hollenbeck, "EtherIP: Tunneling Ethernet Frames in IP Datagrams", September 2002.

## 历史

`gif` 设备首次出现于 WIDE hydrangea IPv6 kit。

## 缺陷

存在许多隧道协议规范，彼此定义各不相同。`gif` 设备可能无法与基于不同规范的对端互操作，并且对外部头部字段较为挑剔。例如，通常无法使用 `gif` 与使用 IPsec 隧道模式的 IPsec 设备通信。

如果外部协议为 IPv4，`gif` 不会尝试为封装后的数据包执行路径 MTU 发现（DF 位设置为 0）。

如果外部协议为 IPv6，封装后数据包的路径 MTU 发现可能影响通过该接口的通信。第一个大于 pmtu 的数据包可能丢失。为避免此问题，当外部头部为 IPv6 且内部头部为 IPv4 时，你可能希望将 `gif` 的接口 MTU 设置为 1240 或更小。

`gif` 设备不会将外部头部的 ICMP 消息转换为内部头部。

过去，`gif` 具有可通过 `NOCLAMP` 标志配置的多目的地行为。此行为已过时，不再受支持。此标志现在用于确定当外部协议为 IPv6 时是否执行分片。
