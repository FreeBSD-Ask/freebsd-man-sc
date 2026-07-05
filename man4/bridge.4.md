# bridge.4

`if_bridge` — 网络桥接设备

## 名称

`if_bridge`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device if_bridge

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_bridge_load="YES"
bridgestp_load="YES"
```

## 描述

`if_bridge` 驱动在两个或多个使用相同（或“足够相似”）帧格式的 IEEE 802 网络之间创建逻辑链路。例如，可以将以太网和 802.11 网络桥接在一起，但不能将以太网和令牌环网桥接在一起。

每个 `if_bridge` 接口在运行时通过接口克隆创建。最简单的方法是使用 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令，或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `cloned_interfaces` 变量。

创建时，`if_bridge` 接口会通过对主机 UUID、jail 名和接口名进行哈希，在 FreeBSD 基金会保留的通用管理地址范围内获得一个链路（MAC）地址。如果此操作失败，则生成一个随机的本地管理地址。此地址仅在本地机器上的所有 `if_bridge` 接口之间保证唯一。因此，理论上你可以在不同机器上拥有两个具有相同链路地址的桥接。可以使用 [ifconfig(8)](../man8/ifconfig.8.md) 分配所需的链路地址来更改此地址。

如果 [sysctl(8)](../man8/sysctl.8.md) 节点 `net.link.bridge.inherit_mac` 具有非零值，则新创建的桥接将从其第一个成员继承 MAC 地址，而不是选择随机的链路层地址。这将在无需任何额外配置的情况下提供更可预测的桥接 MAC 地址，但目前已知此功能会破坏某些 L2 协议，例如由 [ng_pppoe(4)](ng_pppoe.4.md) 和 ppp(8) 提供的 PPPoE。目前此功能被视为实验性功能，默认关闭。

桥接可用于提供多种服务，例如为无线主机提供简单的 802.11 到以太网桥接，或流量隔离。

桥接的工作方式类似交换机，将流量从一个接口转发到另一个接口。多播和广播数据包始终转发到作为桥接一部分的所有接口。对于单播流量，桥接学习哪些 MAC 地址与哪些接口关联，并选择性地转发流量。

默认情况下，桥接将 MAC 地址端口翻动记录到 syslog(3)。可以通过将 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.bridge.log_mac_flap` 设置为 `0` 来禁用此行为。

所有桥接成员接口都需要处于 up 状态才能传递网络流量。可以使用 [ifconfig(8)](../man8/ifconfig.8.md) 或 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `ifconfig_`<`interface` >`="up"`> 来启用它们。

添加的第一个成员接口的 MTU 用作桥接 MTU。所有其他成员的 MTU 将被更改为匹配。如果在创建后更改了桥接的 MTU，所有成员接口的 MTU 也会更改为匹配。

如果添加到桥接的任何接口不支持/未启用 TOE、TSO、TXCSUM 和 TXCSUM6 功能，则所有接口上的这些功能都会被禁用。LRO 功能始终被禁用。当接口从桥接中移除时，所有功能都会恢复。在运行时更改功能可能导致 NIC 重新初始化和链路翻动。

桥接支持“监视模式”，其中数据包在 [bpf(4)](bpf.4.md) 处理之后被丢弃，不再被进一步处理或转发。这可用于将两个或多个接口的输入多路复用到单个 [bpf(4)](bpf.4.md) 流中。这对于重构通过两个独立接口发送 RX/TX 信号的网络分接器的流量很有用。

要允许主机与桥接成员通信，IP 地址应分配给 `if_bridge` 接口本身，而不是桥接的成员接口。尝试将 IP 地址分配给桥接成员接口，或将具有已分配 IP 地址的成员接口添加到桥接，将返回 `EINVAL` “(Invalid argument”) 错误。为了与允许此操作的旧版本兼容，将 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.bridge.member_ifaddrs` 设置为 1 将允许此配置。此 sysctl 变量将在 FreeBSD 16.0 中移除。

## IPV6 支持

`if_bridge` 在桥接接口上支持 `AF_INET6` 地址族。以下 [rc.conf(5)](../man5/rc.conf.5.md) 变量在 `bridge0` 接口上配置 IPv6 链路本地地址：

```sh
ifconfig_bridge0_ipv6="inet6 auto_linklocal"
```

然而，`AF_INET6` 地址族具有作用域区域的概念。桥接多个接口会更改区域配置，因为多个链路相互合并形成一个新的单一链路，而成员接口仍单独工作。这意味着每个成员接口仍具有单独的链路本地作用域区域，同时 `if_bridge` 接口具有另一个单一的聚合链路本地作用域区域。这种情况明显违反了 RFC 4007 第 5 节中“相同作用域的区域不能重叠”的描述。虽然它在大多数情况下有效，但当 `if_bridge` 接口和某个成员接口都具有 IPv6 地址且应用程序同时使用两者时，在某些边缘情况下可能导致一些反直觉或不良行为。

为防止这种情况，`if_bridge` 检查要添加的成员接口和 `if_bridge` 接口上是否配置了链路本地作用域的 IPv6 地址。当 `if_bridge` 接口具有 IPv6 地址时，在添加接口之前会自动删除成员接口上的 IPv6 地址。

可以通过将 [sysctl(8)](../man8/sysctl.8.md) 变量 `net.link.bridge.allow_llz_overlap` 设置为 `1` 来禁用此行为。

注意，即使将 `net.inet6.ip6.accept_rtadv` 和/或 `net.inet6.ip6.auto_linklocal` 设置为 `1`，`if_bridge` 接口上默认也不启用 `ACCEPT_RTADV` 和 `AUTO_LINKLOCAL` 接口标志。

## 生成树

`if_bridge` 驱动实现了快速生成树协议（RSTP 或 802.1w），与旧版生成树协议（STP）向后兼容。生成树用于检测和删除网络拓扑中的环路。

RSTP 提供比旧版 STP 更快的生成树收敛，该协议与相邻交换机交换信息以快速转换到转发状态而不产生环路。

代码默认使用 RSTP 模式，但会将连接到旧版 STP 网络的任何端口降级，因此完全向后兼容。可通过 [ifconfig(8)](../man8/ifconfig.8.md) 中的 `proto` 命令强制桥接在不进行快速状态转换的 STP 模式下运行。

通过使用 [sysctl(8)](../man8/sysctl.8.md) 设置 `net.link.bridge.log_stp` 节点，桥接可以将 STP 端口更改记录到 syslog(3)。

## VLAN 支持

虚拟局域网（VLAN）在 IEEE 802.1Q 标准中定义，允许将桥接上的流量分隔为不能相互通信的独立逻辑网络。例如，VLAN 10 中的两个接口能够相互通信，但不能与 VLAN 20 中的另一个接口通信。

每个 VLAN 由 1 到 4094（含）之间的数字标识。默认情况下，桥接上的所有流量分配给“VLAN 0”，这是一个用于历史兼容性的伪 VLAN。在桥接上使用 VLAN 时，建议将所有流量显式分配给某个 VLAN，而不是使用 VLAN 0。

桥接实现独立 VLAN 学习（IVL），意味着主机地址是按每个 VLAN 单独学习的，同一主机地址可能存在于不同 VLAN 中的多个不同端口上。

如果在某个接口上配置了 [vlan(4)](vlan.4.md) 接口，而该接口同时是 `if_bridge` 成员接口，则所有带标记的帧将由 [vlan(4)](vlan.4.md) 接口处理，对桥接不可见。不推荐此配置，未来版本可能不支持。

### 带标记和无标记流量

成员接口上的传入帧可以是带标记的或无标记的。带标记的帧包含一个 802.1Q 头部，指示该帧属于哪个 VLAN，而无标记的帧不包含。收到带标记的帧时，该帧会自动分配给标记中的 VLAN（受任何已配置的 VLAN 访问列表约束），而无标记的帧分配给接口已配置的端口 VLAN ID（PVID），或在没有配置 PVID 时分配给 VLAN 0。

### 将接口分配到 VLAN

接口的 PVID 可使用 [ifconfig(8)](../man8/ifconfig.8.md) `ifuntagged` 命令配置：

```sh
ifconfig bridge0 ifuntagged ix0 10
```

或通过使用 `addm` 的 `untagged` 选项：

```sh
ifconfig bridge0 addm ix0 untagged 10
```

这会将接口上接收的所有无标记流量分配给指定 VLAN，并且此 VLAN 中接口上传输的任何流量都将删除其 VLAN 标记（如果存在）。反之，在不同 VLAN 中接口上传输的任何流量都将添加标记，以允许远程系统将流量分配给适当的 VLAN。

### VLAN 中的主机通信

有时允许主机本身在 VLAN 中通信很有用，例如为 VLAN 中的其他主机提供路由。为此，在 `if_bridge` 接口之上创建一个具有适当 VLAN 标记的 [vlan(4)](vlan.4.md) 接口。例如，要允许主机在 VLAN 10 中通信：

```sh
ifconfig bridge0.10 create inet6 2001:db8::1/64
```

### 配置 VLAN 访问列表（VLAN 过滤）

由于历史原因，默认的 `if_bridge` 配置允许所有接口为任何 VLAN 发送带标记的流量，这意味着 VLAN 不提供安全隔离。要限制哪些接口可以在哪些 VLAN 中通信，在桥接上启用 VLAN 过滤：

```sh
ifconfig bridge0 vlanfilter
```

这对桥接成员有以下影响：

- 除非接口配置了 PVID，否则不会接受来自成员接口的无标记帧。
- 除非 VLAN 标识符存在于接口的 VLAN 访问列表中，否则不会接受来自成员接口的带标记帧。
- 除非已为该成员配置了 `qinq` 选项（见下文），否则不会接受来自成员接口的堆叠标记（Q-in-Q）帧。

要配置 VLAN 访问列表，请使用 [ifconfig(8)](../man8/ifconfig.8.md) `iftagged`、`+iftagged` 或 `-iftagged` 命令。例如，要允许接口在 VLAN 10、20 以及从 100 到 199 的任何 VLAN 中通信：

```sh
ifconfig bridge0 iftagged ix0 10,20,100-199
```

### IEEE 802.1ad (Q-in-Q) 配置

IEEE 802.1ad，也称为 Q-in-Q 或“标记堆叠”，允许单个以太网帧包含多个标记。这允许一个以太网网络使用其自己的 VLAN 标记在端点之间传输流量，而不干扰任何预先存在的标记，常用于服务提供商网络中提供“虚拟线”以太网服务。

启用 VLAN 过滤时，`if_bridge` 不允许成员接口发送 Q-in-Q 帧，因为在某些配置中这允许对桥接进行“VLAN 跳跃”攻击。例如，考虑一个桥接，端口 ix0 配置为 VLAN 10 中的带标记端口，端口 ix1 配置为 VLAN 10 中的无标记端口和 VLAN 20 中的带标记端口。如果允许 ix0 发送 Q-in-Q 帧，则它可以发送一个带有两个标记的帧：一个用于 VLAN 10，后跟一个用于 VLAN 20。当桥接将帧转发给 ix1 时，它将剥离 VLAN 10 的标记，然后将帧转发给 ix1，VLAN 20 的标记保持不变，实际上允许 ix1 在 VLAN 20 上发送流量，即使桥接配置不应允许这样做。

要允许接口发送 Q-in-Q 帧，在接口上设置 [ifconfig(8)](../man8/ifconfig.8.md) `qinq` 标志。这仅在将发送 Q-in-Q 帧的接口上需要，而不在接收帧的接口上需要。

或者，在桥接本身上设置 `defqinq` 标志，以默认为所有新添加的接口启用 Q-in-Q。

## 数据包过滤

数据包过滤可与任何通过 [pfil(9)](../man9/pfil.9.md) 框架挂钩的防火墙软件包一起使用。启用过滤时，桥接的数据包将在 originating 接口上的入站、桥接接口上以及相应接口上的出站通过过滤器。任一阶段都可禁用。过滤行为可使用 [sysctl(8)](../man8/sysctl.8.md) 控制：

**`net.link.bridge.pfil_onlyip`** 控制对未传递给 [pfil(9)](../man9/pfil.9.md) 的非 IP 数据包的处理。设置为 `1` 仅允许 IP 数据包通过（受防火墙规则约束），设置为 `0` 无条件传递所有非 IP 以太网帧。

**`net.link.bridge.pfil_member`** 设置为 `1` 在传入和传出的成员接口上启用过滤，设置为 `0` 禁用。

**`net.link.bridge.pfil_bridge`** 设置为 `1` 在桥接接口上启用过滤，设置为 `0` 禁用。

**`net.link.bridge.pfil_local_phys`** 设置为 `1` 额外对本地目标数据包在物理接口上进行过滤。设置为 `0` 禁用此功能。

**`net.link.bridge.ipfw`** 设置为 `1` 以使用 [ipfirewall(4)](ipfirewall.4.md) 启用第 2 层过滤，设置为 `0` 禁用。需要启用此项以支持 [dummynet(4)](dummynet.4.md)。当启用 `ipfw` 时，`pfil_bridge` 和 `pfil_member` 将被禁用，以免 IPFW 运行两次；如果需要，可重新启用。

**`net.link.bridge.ipfw_arp`** 设置为 `1` 以使用 [ipfirewall(4)](ipfirewall.4.md) 启用第 2 层 ARP 过滤，设置为 `0` 禁用。需要启用 `ipfw`。

ARP 和 REVARP 数据包在不被过滤的情况下转发，启用 `pfil_onlyip` 时其他非 IP 和非 IPv6 数据包不会被转发。IPFW 可以使用 `mac-type` 过滤以太网类型，因此所有数据包都会传递给过滤器进行处理。

来自桥接主机的数据包将在路由表中查找的接口上被过滤器看到。

发往桥接主机的数据包将在 MAC 地址等于数据包目的 MAC 的接口上被过滤器看到。在某些情况下，某些桥接成员共享相同的 MAC 地址（例如 [vlan(4)](vlan.4.md) 接口：它们当前共享父物理接口的 MAC 地址）。无法使用其 MAC 地址区分这些接口，除非数据包的目的 MAC 地址等于数据包进入系统的接口的 MAC 地址。在这种情况下，过滤器将在此接口上看到传入数据包。在所有其他情况下，数据包过滤器看到的接口从具有相同 MAC 地址的桥接成员列表中选择，结果很大程度上取决于成员添加顺序和 `if_bridge` 的实际实现。不建议依赖当前 `if_bridge` 实现所选择的顺序，因为它可能在未来发生变化。

上一段最好用以下图示说明。设

- 传入数据包的目的 MAC 地址为 `nn:nn:nn:nn:nn:nn`，
- 数据包进入系统的接口为 `ifX`，
- `ifX` 的 MAC 地址为 `xx:xx:xx:xx:xx:xx`，
- 可能存在具有相同 MAC 地址 `xx:xx:xx:xx:xx:xx` 的其他桥接成员，
- 桥接具有多个共享相同 MAC 地址 `yy:yy:yy:yy:yy:yy` 的接口；我们将它们称为 `vlanY1`、`vlanY2` 等。

如果 MAC 地址 `nn:nn:nn:nn:nn:nn` 等于 `xx:xx:xx:xx:xx:xx`，则无论是否有任何其他桥接成员具有相同的 MAC 地址，过滤器都将在接口 `ifX` 上看到该数据包。但如果 MAC 地址 `nn:nn:nn:nn:nn:nn` 等于 `yy:yy:yy:yy:yy:yy`，则过滤器将看到的接口是 `vlanYn` 之一。在没有系统状态和 `vlanYn` 实现细节的知识的情况下，无法预测实际接口的名称。

此问题对于共享相同 MAC 地址的任何桥接成员都存在，不仅限于 [vlan(4)](vlan.4.md) 的成员：它们只是作为这种情况的示例。因此，如果想根据接口名称过滤本地目标数据包，应意识到此影响。所述情况至少会出现在执行 IP 转发的过滤桥接上；在某些此类情况下，最好仅将 IP 地址分配给 `vlanYn` 接口，而不是桥接成员。启用 `net.link.bridge.pfil_local_phys` 将允许你在物理接口上进行额外过滤。

## NETMAP

[netmap(4)](netmap.4.md) 应用程序可以以模拟模式打开桥接接口。netmap 应用程序将接收来自成员接口的所有数据包。特别是，原本会转发到另一个成员接口的数据包将被 netmap 应用程序接收。

当 [netmap(4)](netmap.4.md) 应用程序通过桥接接口将数据包传输到主机栈时，`vlanYn` 接收它并尝试通过在接口的学习表中查找源 MAC 地址来确定其 `source` 接口。未找到匹配源接口的数据包将被丢弃，输入错误计数器递增。如果找到匹配的源接口，`vlanYn` 会将该数据包视为来自相应接口并正常处理，而不将数据包传回 [netmap(4)](netmap.4.md)。

## 实例

将以下内容放入 **/etc/rc.conf** 文件中将导致创建名为“`bridge0`”的桥接，将接口“`wlan0`”和“`fxp0`”添加到桥接中，然后启用数据包转发。这样的配置可用于实现简单的 802.11 到以太网桥接（假设 802.11 接口处于 ad-hoc 模式）。

```sh
cloned_interfaces="bridge0"
ifconfig_bridge0="addm wlan0 addm fxp0 up"
```

要使桥接转发数据包，所有成员接口和桥接都需要处于 up 状态。上述示例还需要：

```sh
create_args_wlan0="wlanmode hostap"
ifconfig_wlan0="up ssid my_ap mode 11g"
ifconfig_fxp0="up"
```

以下命令将创建一个具有两个 VLAN（10 和 20）的桥接，其中“`em`”接口只能在其分配的 VLAN 中通信，而“`ix0`”是可以在任一 VLAN 中通信的 trunk 端口：

```sh
cloned_interfaces="bridge0"
ifconfig_bridge0="vlanfilter e
	addm em0 untagged 10 e
	addm em1 untagged 10 e
	addm em2 untagged 20 e
	addm em3 untagged 20 e
	addm ix0 tagged 10,20"
ifconfig_em0="up"
ifconfig_em1="up"
ifconfig_em2="up"
ifconfig_em3="up"
ifconfig_ix0="up"
```

可以扩展前面的示例以允许主机在 VLAN 10 和 20 中通信：

```sh
vlans_bridge0="10 20"
ifconfig_bridge0_10_ipv6="inet6 2001:db8:0:10::1/64"
ifconfig_bridge0_20_ipv6="inet6 2001:db8:0:20::1/64"
```

考虑一个具有两块 4 端口以太网卡的系统。以下命令将创建一个由所有 8 个端口组成并启用快速生成树的桥接：

```sh
ifconfig bridge0 create
ifconfig bridge0 e
    addm fxp0 stp fxp0 e
    addm fxp1 stp fxp1 e
    addm fxp2 stp fxp2 e
    addm fxp3 stp fxp3 e
    addm fxp4 stp fxp4 e
    addm fxp5 stp fxp5 e
    addm fxp6 stp fxp6 e
    addm fxp7 stp fxp7 e
    up
```

桥接可以在其成员端口之间桥接的同时用作常规主机接口。在此示例中，桥接连接 em0 和 em1，并通过 DHCP 获取其 IP 地址：

```sh
cloned_interfaces="bridge0"
ifconfig_bridge0="addm em0 addm em1 DHCP"
ifconfig_em0="up"
ifconfig_em1="up"
```

桥接可以使用 EtherIP 协议通过 IP 互联网隧道传输以太网。这可与 [ipsec(4)](ipsec.4.md) 结合以提供加密连接。创建一个 [gif(4)](gif.4.md) 接口并设置隧道的本地和远程 IP 地址，这些在远程桥接上是相反的。

```sh
ifconfig gif0 create
ifconfig gif0 tunnel 1.2.3.4 5.6.7.8 up
ifconfig bridge0 create
ifconfig bridge0 addm fxp0 addm gif0 up
```

## 参见

[gif(4)](gif.4.md), ipf(4), ipfw(4), [netmap(4)](netmap.4.md), [pf(4)](pf.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`vlanYn` 驱动首次出现于 FreeBSD 6.0。

## 作者

`bridge` 驱动最初由 Jason L. Wright <jason@thought.net> 编写，作为北卡罗来纳大学格林斯博罗分校本科独立研究的一部分。

此版本的 `bridge` 驱动已从原始版本由 Jason R. Thorpe <thorpej@wasabisystems.com> 大幅修改。

快速生成树协议（RSTP）支持由 Andrew Thompson <thompsa@FreeBSD.org> 添加。

## 缺陷

`bridge` 驱动当前仅支持以太网和类以太网（例如 802.11）网络设备，这些设备可以配置与桥接设备相同的 MTU 大小。
