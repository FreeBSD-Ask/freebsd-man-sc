  IFCONFIG(8)  

IFCONFIG(8)

FreeBSD System Manager's Manual

IFCONFIG(8)

[名称](#__u540D___u79F0_)
=======================

`ifconfig` —

配置网络接口参数

[概要](#__u6982___u8981_)
=======================

`ifconfig` \[`-f` type`:`format\[`,`type:format ...\]\] \[`-L`\] \[`-k`\] \[`-m`\] \[`-n`\] interface \[`create`\] address\_family \[address \[dest\_address\]\] \[parameters\] `ifconfig` interface `destroy` `ifconfig` `-a` \[`-L`\] \[`-d`\] \[`-[gG]` groupname\] \[`-m`\] \[`-u`\] \[`-v`\] \[address\_family\] `ifconfig` `-l` \[`-d`\] \[`-u`\] \[address\_family\] `ifconfig` \[`-L`\] \[`-d`\] \[`-k`\] \[`-m`\] \[`-u`\] \[`-v`\] \[`-C`\] `ifconfig` \[`-g` groupname\]

[描述](#__u63CF___u8FF0_)
=======================

`ifconfig` 实用程序用于分配地址到网络接口和/或配置网络接口参数。 必须在引导时使用 `ifconfig` 实用程序来定义机器上每个接口的网络地址；它也可以在以后用于重新定义接口的地址或其他操作参数。

可以使用以下选项：

address

对于 DARPA-Internet 系列，地址可以是主机名数据库 hosts(5) 中的主机名，也可以是以 Internet 标准 “dot notation” 表示的 DARPA Internet 地址。

It is also possible to use the CIDR notation 也可以使用 CIDR 表示法（也称为斜线表示法）来包含网络掩码。 也就是说，可以指定一个像 `192.168.0.1/16` 这样的地址。

对于 “inet6” 系列，还可以使用斜杠表示法指定前缀长度，例如 `::1/128` 。 有关详细信息，请参阅下面的 `prefixlen` 参数。

链接级 (“link”) 地址被指定为一系列以冒号分隔的十六进制数字。 例如，这可用于在以太网接口上设置新的 MAC 地址，尽管使用的机制不是以太网特定的。 使用 (“random”) 关键字设置随机生成的 MAC 地址。 随机生成的 MAC 地址可能与网络中已在使用的 MAC 地址相同。 这种重复是极不可能的。 如果在使用此选项时接口已经启动，它将短暂关闭，然后再次启动，以确保底层以太网硬件中的接收过滤器被正确重新编程。

address\_family

指定影响其余参数解释的地址族。 由于接口可以接收具有不同命名方案的不同协议的传输，因此建议指定地址族。 当前支持的地址或协议族有 “inet”, “inet6” 和 “link” 。 如果可用，默认值为 “inet” 或 “link” 。 “ether” 和 “lladdr” 是 “link” 的同义词。 使用 `-l` 标志时， “ether” 地址族具有特殊含义，不再与 “link” 或 “lladdr” 同义。 指定 `-l` “ether” 将仅列出以太网接口，不包括所有其他接口类型，包括环回接口。

dest\_address

指定点对点链接另一端的通信者地址。

interface

该参数为 “name unit” 形式的字符串，例如 “`em0`” 。

groupname

列出给定组中的接口。

`ifconfig` 的输出格式可以使用 `-f` 标志或 `IFCONFIG_FORMAT` 环境变量来控制。 格式指定为以逗号分隔的 **type:format** 对列表。 有关详细信息，请参阅 [实例](#__u5B9E___u4F8B_) 部分。 **types** 及其关联的 **format** 字符串有：

**addr**

调整 inet 和 inet6 地址的显示

**default**

格式显示 inet 和 inet6 地址， **numeric**

**fqdn**

将 inet 和 inet6 地址显示为完全限定域名 (FQDN)

**host**

将 inet 和 inet6 地址显示为非限定主机名

**numeric**

以数字格式显示 inet 和 inet6 地址

**ether**

链路级以太网 (MAC) 地址

**colon**

用冒号分隔地址段

**dash**

用破折号分隔地址段

**default**

以默认格式显示以太网地址， **colon**

**inet**

调整 inet 地址子网掩码的显示：

**cidr**

以 CIDR 表示法显示子网掩码，例如：-
10.0.0.0/8 or 203.0.113.224/26

**default**

以默认格式显示子网掩码, **hex**

**dotted**

以点分四进制显示子网掩码，例如：-
255.255.0.0 or 255.255.255.192

**hex**

以十六进制显示子网掩码，例如：-
0xffff0000 or 0xffffffc0

**inet6**

调整 inet6 地址前缀的显示（子网掩码):

**cidr**

以 CIDR 表示法显示子网前缀，例如-
::1/128 or fe80::1%lo0/64

**default**

以默认格式显示子网前缀 **numeric**

**numeric**

以整数格式显示子网前缀，例如：-
prefixlen 64

可以使用 `ifconfig` 设置以下参数：

[`add`](#add)

[`alias`](#alias) 参数的另一个名称。 为与 BSD/OS 兼容而引入。

[`alias`](#alias_2)

为此接口建立一个额外的网络地址。 这在更改网络号时有时很有用，并且希望接受寻址到旧接口的数据包。 如果地址与此接口的第一个网络地址位于同一子网上，则必须提供不冲突的网络掩码。 通常 `0xffffffff` 是最合适的。

[`-alias`](#alias_3)

删除指定的网络地址。 如果您错误地指定了别名，或者不再需要它，则将使用它。 如果您错误地设置了具有指定主机部分的副作用的 NS 地址，则删除所有 NS 地址将允许您重新指定主机部分。

[`anycast`](#anycast)

（仅限 Inet6。）指定配置的地址是任播地址。 根据当前规范，只有路由器可以配置任播地址。 Anycast 地址不会用作任何传出 IPv6 数据包的源地址。

[`arp`](#arp)

在网络级地址和链路级地址之间的映射中启用地址解析协议 ( (arp(4)) )（默认）。 这目前用于 DARPA 互联网地址和 IEEE 802 48 位 MAC 地址（以太网、FDDI 和令牌环地址）之间的映射。

[`-arp`](#arp_2)

禁用地址解析协议 ( (arp(4)) )。

[`staticarp`](#staticarp)

如果启用了地址解析协议，主机将只回复对其地址的请求，并且永远不会发送任何请求。

[`-staticarp`](#staticarp_2)

如果启用了地址解析协议，主机将正常执行，发送请求并监听回复。

[`broadcast`](#broadcast)

（仅限 Inet。）指定用于表示网络广播的地址。 默认广播地址是主机部分全为 1 的地址。

[`debug`](#debug)

启用依赖于驱动程序的调试代码；通常，这会打开额外的控制台错误日志记录。

[`-debug`](#debug_2)

禁用依赖于驱动程序的调试代码。

[`promisc`](#promisc)

将界面置于永久混杂模式。

[`-promisc`](#promisc_2)

永久禁用混杂模式。

[`delete`](#delete)

[`-alias`](#alias_4) 参数的另一个名称。

[`description`](#description) value, `descr` value

指定接口的描述。 这可用于在可能难以区分的情况下标记接口。

[`-description`](#-description), `-descr`

清除接口描述。

[`down`](#down)

将接口标记为 “down” 。 当接口标记为 “down” 时，系统将不会尝试通过该接口传输消息。 如果可能，接口也将被重置以禁用接收。 此操作不会自动禁用使用该接口的路由。

[`group`](#group) groupname

将接口分配给 “group” 。 任何接口都可以在多个组中。

默认情况下，克隆的接口是其接口系列组的成员。 例如，PPP 接口（如 _ppp0_ ）是 PPP 接口系列组 _ppp_ 的成员。

[`-group`](#-group) groupname

从给定的 “group” 中删除接口。

[`eui64`](#eui64)

（仅限 Inet6。）自动填充接口索引（IPv6 地址的最低 64 位）。

[`fib`](#fib) fib\_number

指定接口 FIB。 fib\_number 分配给在该接口上接收的所有帧或数据包。 FIB 不是继承的，例如，vlan 或其他子接口将使用默认的 FIB (0)，而与父接口的 FIB 无关。 需要使用 ROUTETABLES 内核配置选项或 net.fibs 可调参数来调整内核以支持比默认 FIB 更多的功能。

[`tunnelfib`](#tunnelfib) fib\_number

指定隧道 FIB。 FIB fib\_number 分配给隧道接口封装的所有数据包，例如 gif(4) 和 gre(4) 。

[`maclabel`](#maclabel) label

如果在内核中启用了强制访问控制支持，请将 MAC 标签设置为 label 。

[`media`](#media) type

如果驱动支持媒体选择系统，设置接口的媒体类型为 type 。 一些接口支持互斥使用几种不同的物理媒体连接器之一。 例如，10Mbit/s 以太网接口可能支持使用 AUI 或双绞线连接器。 将媒体类型设置为 `10base5/AUI` 会将当前活动的连接器更改为 AUI 端口。 将其设置为 `10baseT/UTP` 将激活双绞线。 有关可用类型的完整列表，请参阅接口的驱动程序特定文档或手册页。

[`mediaopt`](#mediaopt) opts

如果驱动支持媒体选择系统，在界面上设置指定的媒体选项。 opts 参数是应用于接口的选项的逗号分隔列表。 有关可用选项的完整列表，请参阅接口的驱动程序特定手册页。

[`-mediaopt`](#mediaopt_2) opts

如果驱动程序支持媒体选择系统，则禁用界面上指定的媒体选项。

[`mode`](#mode) mode

如果驱动支持媒体选择系统，将界面上指定的操作模式设置为 mode 。 对于支持多种操作模式的 IEEE 802.11 无线接口，此指令用于在 (`11a`), 802.11b (`11b`), and 802.11g (`11g`) 操作模式之间进行选择。

[`txrtlmt`](#txrtlmt)

设置驱动程序是否支持 TX 速率限制。

[`inst`](#inst) minst, `instance` minst

将媒体实例设置为 minst 。 这对于具有多个物理层接口 (PHY) 的设备很有用。

[`name`](#name) name

设置接口名称为 name 。

[`rxcsum`](#rxcsum), `txcsum`, `rxcsum6`, `txcsum6`

如果驱动程序支持用户可配置的校验和卸载，则在接口上启用接收（或发送）校验和卸载。 该功能可以根据协议系列有选择地打开。 将 `rxcsum6`, `txcsum6` 用于 ip6(4) 或 `rxcsum`, `txcsum` 否则。 一些驱动程序可能无法独立启用这些标志，因此设置一个也可能设置另一个。 驱动程序将卸载尽可能多的校验和工作，因为它可以可靠地支持，卸载的确切级别因驱动程序而异。

[`-rxcsum`](#rxcsum_2), `-txcsum`, `-rxcsum6`, `-txcsum6`

如果驱动程序支持用户可配置的校验和卸载，则禁用接口上的接收（或发送）校验和卸载。 可以根据协议系列有选择地关闭该功能。 对 ip6(4) 使用 `-rxcsum6`, `-txcsum6` 或 `-rxcsum`, `-txcsum` 否则。 这些设置可能并不总是相互独立。

[`tso`](#tso)

如果驱动程序支持 tcp(4) 分段卸载，请在接口上启用 TSO。 某些驱动程序可能无法支持 ip(4) 和 ip6(4)-
数据包的 TSO，因此它们可能只启用其中一个。

[`-tso`](#tso_2)

如果驱动程序支持 tcp(4) 分段卸载，请在接口上禁用 TSO。 它将始终禁用 ip(4) 和 ip6(4) 的 TSO。

[`tso6`](#tso6), `tso4`

如果驱动程序支持 ip6(4) 或 ip(4) 的 tcp(4) 分段卸载，请使用其中之一来选择性地仅为一个协议系列启用它。

[`-tso6`](#tso6_2), `-tso4`

如果驱动程序支持 ip6(4) 或 ip(4) 的 tcp(4) 分段卸载，请使用其中之一来选择性地仅为一个协议系列禁用它。

[`lro`](#lro)

如果驱动程序支持 tcp(4) 大接收卸载，请在接口上启用 LRO。

[`-lro`](#lro_2)

如果驱动程序支持 tcp(4) 大接收卸载，请在接口上禁用 LRO。

[`txtls`](#txtls)

传输 TLS 卸载加密传输层安全 (TLS) 记录并将加密记录分段为一个或多个通过 ip(4) 或 ip6(4) 的 tcp(4) 段。 如果驱动程序支持传输 TLS 卸载，请在接口上启用传输 TLS 卸载。 某些驱动程序可能无法支持 ip(4) 和 ip6(4) 数据包的传输 TLS 卸载，因此它们可能仅启用其中一个。

[`-txtls`](#txtls_2)

如果驱动程序支持传输 TLS 卸载，请在接口上禁用传输 TLS 卸载。 它将始终禁用 ip(4) 和 ip6(4) 的 TLS。

[`txtlsrtlmt`](#txtlsrtlmt)

启用对 TLS 卸载的速率限制（数据包调步）。

[`-txtlsrtlmt`](#txtlsrtlmt_2)

禁用 TLS 卸载的速率限制。

[`nomap`](#nomap)

如果驱动程序支持未映射的网络缓冲区，请在接口上启用它们。

[`-nomap`](#nomap_2)

如果驱动程序支持未映射的网络缓冲区，请在接口上禁用它们。

[`wol`](#wol), `wol_ucast`, `wol_mcast`, `wol_magic`

WOL 是一种可以唤醒处于低功率状态的机器以响应接收到的数据包的设施。 有三种类型的数据包可以唤醒系统：ucast（仅定向到机器的 mac 地址）、mcast（定向到广播或多播地址）或魔术（具有“神奇内容”的单播或多播帧） . 并非所有设备都支持 WOL，那些确实表明它们在其功能中支持的机制的设备。 `wol` 是启用所有可用 WOL 机制的同义词。 要禁用 WOL，请使用 `-wol` 。

[`vlanmtu`](#vlanmtu), `vlanhwtag`, `vlanhwfilter`, `vlanhwcsum`, `vlanhwtso`

如果驱动程序提供用户可配置的 VLAN 支持，则分别启用扩展帧的接收、硬件中的标记处理、硬件中的帧过滤、校验和卸载或 VLAN 上的 TSO。 请注意，这必须在与 vlan(4) 关联的物理接口上配置，而不是在 vlan(4) 接口本身上配置。

[`-vlanmtu`](#vlanmtu_2), `-vlanhwtag`, `-vlanhwfilter`, `-vlanhwtso`

如果驱动程序提供用户可配置的 VLAN 支持，则分别禁用扩展帧的接收、硬件中的标记处理、硬件中的帧过滤或 VLAN 上的 TSO。

[`vxlanhwcsum`](#vxlanhwcsum), `vxlanhwtso`

如果驱动程序提供用户可配置的 VXLAN 支持，请分别在 VXLAN 上启用内部校验和卸载（接收和传输）或 TSO。 请注意，这必须在与 vxlan(4) 关联的物理接口上配置，而不是在 vxlan(4) 接口本身上配置。 物理接口可以是指定为 vxlandev 的接口，也可以是托管 vxlanlocal 地址的接口。 驱动程序将卸载尽可能多的校验和工作和 TSO，因为它可以可靠地支持，卸载的确切级别可能因驱动程序而异。

[`-vxlanhwcsum`](#vxlanhwcsum_2), `-vxlanhwtso`

如果驱动程序提供用户可配置的 VXLAN 支持，请分别禁用 VXLAN 上的校验和卸载（接收和传输）或 TSO。

[`vnet`](#vnet) jail

将接口移动到由名称或 JID 指定的 jail(8) 。 如果监狱有一个虚拟网络堆栈，该接口将从当前环境中消失，并对监狱可见。

[`-vnet`](#vnet_2) jail

从 jail(8) 中回收接口，由名称或JID 指定。 如果监狱有一个虚拟网络堆栈，该接口将从监狱中消失，并对当前网络环境可见。

[`polling`](#polling)

如果驱动程序支持此模式，请打开 polling(4) 功能并禁用接口上的中断。

[`-polling`](#polling_2)

关闭 polling(4) 功能并在接口上启用中断模式。

[`create`](#create)

创建指定的网络伪设备。 如果给出的接口没有单元号，请尝试创建一个具有任意单元号的新设备。 如果任意设备的创建成功，则新设备名称将打印到标准输出，除非该接口在同一次 `ifconfig` 调用中被重命名或销毁。

[`destroy`](#destroy)

销毁指定的网络伪设备。

[`plumb`](#plumb)

[`create`](#create_2) 参数的另一个名称。 包括用于 Solaris 兼容性。

[`unplumb`](#unplumb)

[`destroy`](#destroy_2) 参数的另一个名称。 包括用于 Solaris 兼容性。

[`metric`](#metric) n

将接口的路由度量设置为 n ，默认为0。 路由度量由路由协议（ (routed(8)) ）使用。 更高的指标会使路线变得不那么有利；指标被计为到目标网络或主机的额外跃点。

[`mtu`](#mtu) n

设置接口的最大传输单元为 n ，默认为接口特定。 MTU 用于限制在接口上传输的数据包的大小。 并非所有接口都支持设置 MTU，部分接口有范围限制。

[`netmask`](#netmask) mask

（仅限 Inet。）指定为将网络细分为子网络而保留的地址量。 掩码包括本地地址的网络部分和子网部分，子网部分取自地址的主机字段。 掩码可以指定为单个十六进制数字，带有前导 ‘`0x`’ ，带有点表示法的 Internet 地址，或网络表 networks(5) 中列出的伪网络名称。 掩码包含 1 表示 32 位地址中用于网络和子网部分的位位置，而 0 表示主机部分。 掩码应至少包含标准网络部分，子网字段应与网络部分连续。

网络掩码也可以在地址后面以 CIDR 表示法指定。 有关详细信息，请参阅上面的 address 选项。

[`prefixlen`](#prefixlen) len

（仅限 Inet6。）指定 len 位保留用于将网络细分为子网络。 len 必须是整数，出于语法原因，它必须介于 0 到 128 之间 。根据当前的 IPv6 分配规则，它几乎总是 64。如果省略该参数，则使用 64。

前缀也可以在地址后使用斜线表示法指定。 有关详细信息，请参阅上面的 address 选项。

[`remove`](#remove)

[`-alias`](#alias_5) 参数的另一个名称。 为与 BSD/OS 兼容而引入。

[`link`](#link)\[`0`\-`2`\]

启用接口链接级别的特殊处理。 这三个选项实际上是界面特定的，但一般用于选择特殊的操作模式。 例如，启用 SLIP 压缩，或为某些以太网卡选择连接器类型。 有关详细信息，请参阅特定驱动程序的手册页。

[`-link`](#link_2)\[`0`\-`2`\]

在指定接口的链接级别禁用特殊处理。

[`monitor`](#monitor)

将接口置于监控模式。 没有数据包被发送，接收到的数据包在 bpf(4) 处理后被丢弃。

[`-monitor`](#monitor_2)

使接口退出监控模式。

[`pcp`](#pcp) priority\_code\_point

优先级代码点 (`PCP`) 是一个 3 位字段，它引用 IEEE 802.1p 服务类别并映射到帧优先级。

[`-pcp`](#pcp_2)

停止在带有优先级代码点的接口上标记数据包。

[`up`](#up)

将接口标记为 “up” 。 这可用于在 “`ifconfig` `down`” 之后启用接口。 在接口上设置第一个地址时会自动发生。 如果接口在先前标记为关闭时被重置，则硬件将重新初始化。

以下参数适用于 ICMPv6 邻居发现协议。 请注意，它们需要地址族关键字 “`inet6`” :

[`accept_rtadv`](#accept_rtadv)

设置一个标志以启用接受 ICMPv6 路由器广告消息。 sysctl(8) 变量 net.inet6.ip6.accept\_rtadv 控制是否默认设置此标志。

[`-accept_rtadv`](#-accept_rtadv)

清除标志 `accept_rtadv` 。

[`no_radr`](#no_radr)

设置一个标志来控制系统接受路由器通告消息的路由器是否被添加到默认路由器列表中。 当 `accept_rtadv` 标志被禁用时，此标志无效。 sysctl(8) 变量 net.inet6.ip6.no\_radr 控制是否默认设置此标志。

[`-no_radr`](#-no_radr)

清除标志 `no_radr` 。

[`auto_linklocal`](#auto_linklocal)

设置一个标志以在接口可用时执行自动链路本地地址配置。 sysctl(8) 变量 net.inet6.ip6.auto\_linklocal 控制是否默认设置此标志。

[`-auto_linklocal`](#-auto_linklocal)

清除标志 `auto_linklocal` 。

[`defaultif`](#defaultif)

当没有默认路由器时，将指定接口设置为默认路由。

[`-defaultif`](#-defaultif)

清除标志 `defaultif` 。

[`ifdisabled`](#ifdisabled)

ifdisabled 设置一个标志以禁用指定接口上的所有 IPv6 网络通信。 请注意，如果该接口上已经配置了 IPv6 地址，则所有这些地址都标记为 “tentative” ，并且在清除该标志时将执行 DAD。

[`-ifdisabled`](#-ifdisabled)

清除标志 `ifdisabled` 。 当此标志被清除并启用 `auto_linklocal` 标志时，将执行链接本地地址的自动配置。

[`nud`](#nud)

设置一个标志以启用邻居不可达检测。

[`-nud`](#-nud)

清除一个标志 `nud` 。

[`no_prefer_iface`](#no_prefer_iface)

设置一个标志以不遵守 RFC 3484 中的源地址选择规则 5。 实际上，这意味着传出接口上的地址将不被首选，有效地将决定交给地址选择策略表，可使用 ip6addrctl(8) 进行配置。

[`-no_prefer_iface`](#-no_prefer_iface)

清除标志 `no_prefer_iface` 。

[`no_dad`](#no_dad)

设置一个标志以禁用重复地址检测。

[`-no_dad`](#-no_dad)

清除标志 `no_dad` 。

以下参数特定于 IPv6 地址。 请注意，它们需要地址族关键字 “`inet6`” :

[`autoconf`](#autoconf)

设置 IPv6 自动配置地址位。

[`-autoconf`](#autoconf_2)

清除 IPv6 自动配置地址位。

[`deprecated`](#deprecated)

设置 IPv6 不推荐使用的地址位。

[`-deprecated`](#deprecated_2)

清除 IPv6 不推荐使用的地址位。

[`pltime`](#pltime) n

设置地址的首选生存期。

[`prefer_source`](#prefer_source)

设置一个标志以首选地址作为传出数据包的源地址的候选者。

[`-prefer_source`](#-prefer_source)

清除标志 `prefer_source` 。

[`vltime`](#vltime) n

设置地址的有效生命周期。

以下参数特定于使用 `create` 请求克隆 IEEE 802.11 无线接口：

[`wlandev`](#wlandev) device

使用 device 作为克隆设备的父级。

[`wlanmode`](#wlanmode) mode

指定此克隆设备的操作模式。 mode 是 `sta`, `ahdemo` (或 `adhoc-demo`), `ibss` (或 `adhoc`), `ap` (或 `hostap`), `wds`, `tdma`, `mesh` 和 `monitor` 之一。 克隆接口的工作模式不能更改。 `tdma` 模式实际上是作为具有特殊属性的 `adhoc-demo` 接口实现的。

[`wlanbssid`](#wlanbssid) bssid

用于 bssid 的 802.11 mac 地址。 这必须在创建旧 `wds` 设备时指定。

[`wlanaddr`](#wlanaddr) address

本地 MAC 地址。 如果未指定，则 mac 地址将自动分配给克隆设备。 通常，此地址与父设备的地址相同，但如果指定了 `bssid` 参数，则驱动程序将为设备制作一个唯一地址（如果支持）。

[`wdslegacy`](#wdslegacy)

将 `wds` 设备标记为以 \`\`legacy mode'' 运行。传统 `wds` 设备具有固定的对等关系，例如，如果它们的对等停止通信，则不会漫游。 为了完整起见，动态 WDS (DWDS) 接口可以标记为 `-wdslegacy` 。

[`bssid`](#bssid)

为克隆设备请求一个唯一的本地 MAC 地址。 仅当设备支持多个 mac 地址时，这才有可能。 要强制使用父 MAC 地址，请使用 `-bssid` 。

[`beacons`](#beacons)

将克隆的接口标记为取决于硬件支持以跟踪接收到的信标。 要在软件中跟踪信标，请使用 `-beacons` 。 对于 `hostap` 模式 `-beacons` 也可用于指示不应传输信标；这在创建 WDS 配置时很有用，但 `wds` 接口只能创建为接入点的伴侣。

以下参数特定于使用 `create` 操作克隆的 IEEE 802.11 无线接口：

[`ampdu`](#ampdu)

在使用 802.11n 时启用发送和接收 AMPDU 帧（默认）。 802.11n 规范规定兼容站必须能够接收 AMPDU 帧，但传输是可选的。 使用 `-ampdu` 禁用 AMPDU 与 802.11n 的所有使用。 为了测试和/或解决互操作性问题，可以使用 `ampdutx` 和 `ampdurx` 来控制 AMPDU 在一个方向上的使用。

[`ampdudensity`](#ampdudensity) density

设置使用 802.11n 操作时使用的 AMPDU 密度参数。 此参数控制 AMPDU 帧的包间间隙。 发送设备通常控制此设置，但接收站可能会要求更大的间隙。 密度的 density 为 0、0.25、0.5、1、2、4、8 和 16（微秒）。 `-` 值与 0 相同。

[`ampdulimit`](#ampdulimit) limit

设置使用 802.11n 操作时接收 AMPDU 帧的数据包大小限制。 limit 的合法值为 8192、16384、32768 和 65536，但也可以仅指定唯一前缀：8、16、32、64。 请注意，发送方可能会将 AMPDU 帧的大小限制为小于接收站指定的最大值。

[`amsdu`](#amsdu)

在使用 802.11n 时启用发送和接收 AMSDU 帧。 默认情况下，接收但不发送 AMSDU。 使用 `-amsdu` 禁用对 802.11n 的所有 AMSDU 使用。 为了测试和/或解决互操作性问题，可以使用 `amsdutx` 和 `amsdurx` 来控制 AMSDU 在一个方向上的使用。

[`amsdulimit`](#amsdulimit) limit

设置使用 802.11n 操作时发送和接收 AMSDU 帧的数据包大小限制。 limit 的合法值为 7935 和 3839（字节）。 请注意，发送方可能会将 AMSDU 帧的大小限制为小于接收站指定的最大值。 另请注意，设备不需要支持 7935 限制，规范只需要 3839，较大的值可能需要更多的内存来专用于支持很少使用的功能。

[`apbridge`](#apbridge)

当作为接入点运行时，直接在无线客户端之间传递数据包（默认）。 要让它们通过系统向上传递并使用其他机制转发，请使用 `-apbridge` 。 当要使用数据包过滤处理流量时，禁用内部桥接很有用。

[`authmode`](#authmode) mode

在基础架构模式下设置所需的身份验证模式。 并非所有适配器都支持所有模式。 有效模式集是 `none`, `open`, `shared` (共享密钥), `8021x` (IEEE 802.1x) 和 `wpa` (IEEE WPA/WPA2/802.11i)。 `8021x` 和 `wpa` 模式仅在使用身份验证服务（客户端操作的请求者或作为接入点操作时的身份验证器）时有用。 模式不区分大小写。

[`bgscan`](#bgscan)

作为工作站运行时启用后台扫描。 背景扫描是一种技术，与接入点相关联的站点将暂时离开信道以扫描相邻站点。 这允许站点维护附近接入点的缓存，以便可以在接入点之间漫游而无需冗长的扫描操作。 后台扫描仅在站点不忙且任何出站流量将取消扫描操作时进行。 后台扫描绝不会导致数据包丢失，尽管如果出站流量中断扫描操作可能会有一些小的延迟。 如果设备有能力，默认情况下会启用后台扫描。 要禁用后台扫描，请使用 `-bgscan` 。后台扫描由 `bgscanidle` 和 `bgscanintvl` 参数控制。 漫游必须启用后台扫描；这是当前实现的产物，将来可能不需要。

[`bgscanidle`](#bgscanidle) idletime

设置在启动后台扫描之前站点必须处于空闲状态（不发送或接收帧）的最短时间。 idletime 参数以毫秒为单位指定。 默认情况下，在启动后台扫描之前，站点必须至少空闲 250 毫秒。 空闲时间不能设置为小于 100 毫秒。

[`bgscanintvl`](#bgscanintvl) interval

设置尝试后台扫描的时间间隔。 interval 参数以秒为单位指定。 默认情况下，每 300 秒（5 分钟）考虑一次后台扫描。 interval 不能设置为小于 15 秒。

[`bintval`](#bintval) interval

设置在 ad-hoc 或 ap 模式下操作时发送信标帧的间隔。 interval 参数在 TU (1024 微秒) 中指定。 默认情况下，每 100 个 TU 发送一次信标帧。

[`bmissthreshold`](#bmissthreshold) count

设置站点尝试漫游（即搜索新接入点）的连续丢失信标的数量。 count 参数必须在 1 到 255 的范围内；尽管上限可能会根据设备能力而降低。 默认阈值为 7 个连续丢失的信标；但这可能会被设备驱动程序覆盖。 `bmissthreshold` 参数的另一个名称是 `bmiss` 。

[`bssid`](#bssid_2) address

指定作为 BSS 网络中的站运行时要使用的接入点的 MAC 地址。 这会覆盖系统所做的任何自动选择。 要禁用先前选择的接入点，请为地址提供 `any`, `none` 或 `-` 。 当多个接入点使用相同的 SSID 时，此选项很有用。 `bssid` 参数的另一个名称是 `ap` 。

[`burst`](#burst)

启用数据包突发。 分组突发是一种传输技术，其中一次获取无线介质以发送多个帧并减少帧间间隔。 这种技术可以通过减少传输开销来显着提高吞吐量。 802.11e QoS 规范支持数据包突发，并且某些不支持 QoS 的设备可能仍然可以使用。 默认情况下，如果设备能够做到这一点，则会启用数据包突发。 要禁用数据包突发，请使用 `-burst` 。

[`chanlist`](#chanlist) channels

设置在扫描接入点、IBSS 网络中的邻居或作为接入点运行时查找未占用信道时使用的所需信道。 通道集指定为逗号分隔的列表，列表中的每个元素表示单个通道号或 “`a-b`” 形式的范围。 通道编号必须在 1 到 255 范围内，并且根据设备的操作特性是允许的。

[`channel`](#channel) number

设置单个所需频道。 通道范围从 1 到 255，但可用的确切选择取决于您的适配器的制造地区。 将通道设置为 `any` 或 `-` 将清除任何所需的通道，如果设备已标记，则强制扫描通道以运行。 或者，可以指定以兆赫为单位的频率，而不是频道号。

当有多种方式使用频道时，频道编号/频率可能会附加属性以进行说明。 例如，如果一个设备能够使用 802.11n 和 802.11g 在通道 6 上运行，那么可以通过指定 \`\`6:g'' 来指定只使用 g 。 类似地，可以通过附加 “/” 来指定通道宽度；例如，“6/40” 指定一个 40MHz 宽的频道，这些属性可以组合为：“6:ht/40”。 在 a \`\`:'' 之后指定的完整标志集是： `a` (802.11a), `b` (802.11b), `d` (Atheros 静态 Turbo 模式), `g` (802.11g), `h` 或 `n` (802.11n aka HT), `s` (Atheros 静态 Turbo 模式), 和 `t` (Atheros 动态 Turbo 模式，或附加到 \`\`st'' 和 \`\`dt'')。 `5` (5MHz 又名 1/4 速率信道), `10` (10MHz 又名半速率信道), `20` (20MHz 主要用于指定 ht20) 和 `40` (40MHz 主要用于用于指定 ht40) 。此外，一个 40MHz HT 信道规范可以包括扩展信道的位置，分别在上面和下面附加 \`\`+'' 或 \`\`-'' ；例如，\`\`2437:ht/40+'' 指定 40MHz 宽的 HT 操作，中心通道在 2437 频率，扩展通道在上面。

[`country`](#country) name

设置国家代码以用于计算操作的监管限制。 特别是可用信道的集合、无线设备将如何在信道上运行以及可以在信道上使用的最大发射功率由该设置定义。 国家/地区代码指定为 ISO 3166 定义的 2 字符缩写或使用更长但可能不明确的拼写；例如， "ES" 和 "Spain" 。 国家代码集取自 /etc/regdomain.xml ，也可以通过 \`\`list countries'' 请求查看。 请注意，并非所有设备都支持从默认设置更改国家代码；通常存储在 EEPROM 中。 另请参阅 `regdomain`, `indoor`, `outdoor` 和 `anywhere` 。

[`dfs`](#dfs)

启用 802.11h 中指定的动态频率选择 (DFS)。 DFS 包含多种功能，包括检测重叠雷达信号、动态发射功率控制以及根据最不拥塞标准进行信道选择。 在某些区域（例如，ETSI）中，某些 5GHz 频率必须支持 DFS。 默认情况下，根据 /etc/regdomain.xml 中指定的监管定义以及当前的国家代码、regdomain 和通道启用 DFS。 请注意，底层设备（和驱动程序）必须支持雷达检测才能完全支持 DFS 工作。 为了完全符合要求 DFS 的当地监管机构频率，除非得到完全支持，否则不应使用。 使用 `-dfs` 禁用此功能以进行测试。

[`dotd`](#dotd)

启用对 802.11d 规范的支持（默认）。 当在站模式下启用此支持时，通告与当前配置的国家代码不同的国家代码的信标帧将导致将事件分派给用户应用程序。 电台可以使用该事件来采用该国家代码并根据相关的监管限制进行操作。 当作为启用了 802.11d 的接入点运行时，发送的信标和探测响应帧将通告当前的监管域设置。 要禁用 802.11d，请使用 `-dotd` 。

[`doth`](#doth)

启用 802.11h 支持，包括频谱管理。 当启用 802.11h 时，信标和探测响应帧将在功能字段中设置 SpectrumMgt 位，并且将出现国家和功率限制信息元素。 802.11h 支持还包括处理信道切换公告 (CSA)，这是一种通过接入点协调信道更改的机制。 默认情况下，如果设备支持，则启用 802.11h。 要禁用 802.11h，请使用 `-doth` 。

[`deftxkey`](#deftxkey) index

设置用于传输的默认密钥。 通常这仅在使用 WEP 加密时设置。 请注意，您必须为系统设置默认传输密钥，才能知道在加密出站流量时使用哪个密钥。 `weptxkey` 是这个请求的别名；提供它是为了向后兼容。

[`dtimperiod`](#dtimperiod) period

设置在 ap 模式下运行时传输缓冲组播数据帧的 DTIM 周期。 period 指定 DTIM 之间的信标间隔数，并且必须在 1 到 15 的范围内。 默认情况下 DTIM 为 1（即，DTIM 在每个信标处发生）。

[`quiet`](#quiet)

启用安静的 IE 使用。 当在 5GHz 频率上运行并启用 doth 支持时，Hostap 将使用它来使其他电台静音以减少对雷达检测的干扰。 使用 `-quiet` 禁用此功能。

[`quiet_period`](#quiet_period) period

将 QUIET period 设置为由 Quiet 元素定义的定期安排的静默间隔开始之间的信标间隔数。

[`quiet_count`](#quiet_count) count

将 QUIET count 设置为 TBTT 的数量，直到下一个静默间隔开始的信标间隔。 值 1 表示静默间隔将在从下一个 TBTT 开始的信标间隔期间开始。 保留值 0。

[`quiet_offset`](#quiet_offset) offset

将 QUIET offset 偏移量设置为从 Quiet 计数指定的 TBTT 开始的安静间隔的偏移量，以 TU 表示。 offset 应小于一个信标间隔。

[`quiet_duration`](#quiet_duration) dur

将 QUIET dur 设置为 Quiet 间隔的持续时间，以 TU 表示。 该值应小于信标间隔。

[`dturbo`](#dturbo)

在与另一个支持 Dynamic Turbo 的工作站通信时启用 Atheros Dynamic Turbo 模式。 动态 Turbo 模式是 Atheros 特有的机制，站通过该机制在正常 802.11 操作和使用 40MHz 宽信道进行通信的\`\`boosted'' 模式之间切换。 只有当频道没有非 dturbo 电台时，使用 Dynamic Turbo 模式的电台才会加速运行；当在频道上识别出非 dturbo 电台时，所有电台将自动恢复正常运行。 默认情况下，动态 Turbo 模式未启用，即使设备支持。 请注意，Turbo 模式（动态或静态）仅允许在某些频道上使用，具体取决于监管限制；使用 `list chan` 命令来识别可以使用 turbo 模式的通道。 要禁用动态 Turbo 模式，请使用 `-dturbo` 。

[`dwds`](#dwds)

启用动态 WDS (DWDS) 支持。 DWDS 是一种设施，通过它可以在基础设施模式下运行的站之间传输 4 地址流量。 站点首先与接入点相关联并使用正常程序（例如 WPA）进行身份验证。 然后传递 4 个地址帧，为在无线链路任一侧运行的站点传输流量。 DWDS 通过利用现有的安全协议和消除静态绑定扩展了正常的 WDS 机制。

当在接入点上启用 DWDS 时，从授权站接收的 4 地址帧将为用户应用程序生成 \`\`DWDS discovery'' 事件。 此事件应用于创建绑定到远程站（通常连接到网桥）的 WDS 接口。 一旦 WDS 接口启动并运行 4 地址流量，然后逻辑上流过该接口。

当一个站点启用 DWDS 时，目标地址与对等站点不同的流量被封装在一个 4 地址帧中并传输给对等站点。 所有 4 地址流量都使用站的安全信息（例如，加密密钥）。 使用 802.11n 设施关联的站可以使用这些相同的机制传输 4 地址流量；这取决于设备的可用资源和功能。 DWDS 实施可防止多播流量的第 2 层路由循环。

[`ff`](#ff)

在与另一个支持快速帧的工作站通信时启用 Atheros 快速帧。 快速帧是一种封装技术，通过它可以在单个 802.11 帧中传输两个 802.3 帧。 这可以显着提高吞吐量，但需要接收站了解如何解封装帧。 使用 Atheros 802.11 供应商特定的协议扩展来协商快速帧的使用，因此在与非 Atheros 设备通信时启用使用是安全的。 默认情况下，如果设备支持，则启用快速帧。 要显式禁用快速帧，请使用 `-ff` 。

[`fragthreshold`](#fragthreshold) length

设置将传输帧分成片段的阈值。 length 参数是以字节为单位的帧大小，必须在 256 到 2346 的范围内。 将 length-
设置为 `2346`, `any` 或 `-` 禁用传输分段。 并非所有适配器都遵守碎片阈值。

[`hidessid`](#hidessid)

当作为接入点运行时，不要在信标帧中广播 SSID 或响应探测请求帧，除非它们被定向到 ap（即，它们包括 ap 的 SSID）。 默认情况下，SSID 包含在信标帧中，并且会回答无向探测请求帧。 要重新启用 SSID 等的广播，请使用 `-hidessid` 。

[`ht`](#ht)

在使用 802.11n（默认）时启用高吞吐量 (HT)。 802.11n 规范包括在 20MHz 和 40MHz 宽信道上使用不同于 802.11b、802.11g 和 802.11a 中指定的信令机制的机制。 车站在联系时协商使用这些称为 HT20 和 HT40 的设施。 要禁用 802.11n 的所有使用，请使用 `-ht` 。 要禁用 HT20（例如，强制仅使用 HT40），请使用 `-ht20` 。 要禁用 HT40，请使用 `-ht40` 。

当有多个选项可用时，HT 配置用于 \`\`auto promote'' 操作。 例如，如果一个站点关联到一个支持 11n 的接入点，它将控制该站点是使用传统操作、HT20 还是 HT40。 当支持 11n 的设备设置为接入点并使用自动通道选择来定位要操作的通道时，HT 配置控制是否在所选通道上设置传统、HT20 或 HT40 操作。 如果为站点指定了固定信道，则可以将 HT 配置作为信道规范的一部分给出；例如，6:ht/20 设置通道 6 上的 HT20 操作。

[`htcompat`](#htcompat)

启用对 802.11n 之前的设备的兼容性支持（默认）。 802.11n 协议规范经历了几次不兼容的迭代。 一些供应商实现了对旧规范的 11n 支持，这些规范不会与纯粹的 11n 兼容站互操作。 特别是旧设备的管理帧中包含的信息元素是不同的。 当启用兼容性支持时，将提供标准和兼容数据。 使用兼容性机制关联的站在 \`\`list sta'' 中标记。 要禁用兼容性支持，请使用 `-htcompat` 。

[`htprotmode`](#htprotmode) technique

对于在 802.11n 中运行的接口，使用指定的 technique 来保护混合的 legacy/HT 网络中的 HT 帧。 有效技术集是 `off` 和 `rts` (RTS/CTS, 默认)。 技术名称不区分大小写。

[`inact`](#inact)

为与接入点关联的站启用不活动处理（默认）。 当作为接入点运行时，802.11 层监控每个相关站点的活动。 当一个站点 5 分钟不活动时，它将发送几个 \`\`probe frames'' 以查看该站点是否仍然存在。 如果没有收到响应，则取消对站的身份验证。 喜欢处理这项工作的应用程序可以使用 `-inact` 禁用此功能。

[`indoor`](#indoor)

设置用于计算监管约束的位置。 当使用 `dotd` 启用 802.11d 时，该位置也会在信标和探测响应帧中公布。 另请参阅 `outdoor`, `anywhere`, `country` 和 `regdomain` 。

[`list active`](#list_active)

显示可供使用的频道列表，考虑到使用 `chanlist` 指令设置的任何限制。 有关详细信息，请参阅 `list chan` 的描述。

[`list caps`](#list_caps)

显示适配器的功能，包括支持的操作模式。

[`list chan`](#list_chan)

显示可供使用的频道列表。 频道显示为其 IEEE 频道号、等效频率和使用模式。 标识为 ‘`11g`’ 的通道也可用于 ‘`11b`’ 模式。 标识为 ‘`11a Turbo`’ 的通道只能用于 Atheros 的静态 Turbo 模式（使用 `mediaopt turbo` 指定）。 标有 ‘`*`’ 的频道具有被动扫描的监管约束。 这意味着站点在识别出该信道正用于 802.11 通信之前，不允许在该信道上进行传输；通常通过收听来自在信道上运行的接入点的信标帧。 `list freq` 是请求此信息的另一种方式。 默认情况下会显示压缩的频道列表；如果指定了 `-v` 选项，则显示所有通道。

[`list countries`](#list_countries)

地区 显示可在法规配置中使用的国家代码和法规域集。

[`list mac`](#list_mac)

显示当前 MAC 访问控制列表状态。 每个地址都以一个字符为前缀，表示应用到它的当前策略： ‘`+`’ 表示允许访问该地址， ‘`-`’ 表示拒绝访问该地址， ‘`*`’ 表示该地址存在但当前策略打开（因此不参考 ACL）。

[`list mesh`](#list_mesh)

显示网状路由表，用于在网状网络上转发数据包。

[`list regdomain`](#list_regdomain)

显示当前监管设置，包括可用信道和传输功率上限。

[`list roam`](#list_roam)

显示控制漫游操作的参数。

[`list txparam`](#list_txparam)

显示控制传输操作的参数。

[`list txpower`](#list_txpower)

显示每个通道的发射功率上限。

[`list scan`](#list_scan)

显示位于附近的接入点和/或临时邻居。 适配器可以通过 `scan` 请求或通过后台扫描自动更新此信息。 根据站的能力，输出中可以包含以下标志：

[`A`](#A)

敏捷性。

[`B`](#B)

PBCC 调制。

[`C`](#C)

轮询请求能力。

[`D`](#D)

DSSS/OFDM 能力。

[`E`](#E)

扩展服务集 (ESS)。

[`I`](#I)

独立基本服务集 (IBSS)。

[`P`](#P)

隐私能力。该站需要身份验证。

[`R`](#R)

强大的安全网络 (RSN)。

[`S`](#S)

简短的序言。 指示该站正在执行短前导码以选择性地提高 802.11g 和 802.11b 的吞吐量性能。

[`c`](#c)

可轮询能力。

[`s`](#s)

短时隙能力。

默认情况下，从相邻站点捕获的有趣信息元素显示在每行的末尾。 可能的元素包括： `WME` (站台支持 WME), `WPA` (站台支持 WPA), `WPS` (站台支持 WPS), `RSN` (站台支持 802.11i/RSN), `HTCAP` (站台支持 802.11n/HT 通信), `ATH` (站台支持 Atheros 协议扩展), `VEN` (站台支持未知的供应商特定扩展）。如果使用 `-v` 标志，则将显示所有信息元素及其内容。 指定 `-v` 标志还可以显示长 SSID。 `list ap` 命令是请求此信息的另一种方式。

[`list sta`](#list_sta)

当作为接入点运行时，显示当前关联的电台。 在 ad-hoc 模式下运行时，显示站被识别为 IBSS 中的邻居。 当在网格模式下运行时，显示站被识别为 MBSS 中的邻居。 在站模式下操作时显示接入点。 站所通告的功能在 `scan` 请求下进行了描述。 输出中可以包含以下标志：

[`A`](#A_2)

授权。 表示允许站点发送/接收数据帧。

[`E`](#E_2)

扩展速率物理 (ERP)。 表示该站点正在使用扩展传输速率的 802.11g 网络中运行。

[`H`](#H)

高吞吐量 (HT)。 指示该站正在使用 HT 传输速率。 如果 ‘`+`’ 紧随其后，则仅当启用 `htcompat` 时才支持使用已弃用的机制关联的站。

[`P`](#P_2)

省电。 表示该站正在节电模式下运行。

[`Q`](#Q)

服务质量 (QoS)。 表示该站点正在对数据帧使用 QoS 封装。 仅当启用 WME 模式时才启用 QoS 封装。

[`S`](#S_2)

启用 HT 40MHz 模式下的短 GI。 如果紧随其后的是 ‘`+`’ ，那么在 HT 20MHz 模式下的短 GI 也会被启用。

[`T`](#T)

过渡安全网络 (TSN)。表示使用TSN关联的台站；另见下面的 `tsn` 。

[`W`](#W)

Wi-Fi 保护设置 (WPS)。 表示使用 WPS 关联的站。

[`s`](#s_2)

启用 HT 20MHz 模式下的短 GI。

默认情况下，从相关站点接收到的信息元素以简短形式显示； `-v` 标志使此信息以符号方式显示。

[`list wme`](#list_wme)

显示在 WME 模式下操作时要使用的当前通道参数。 如果指定了 `-v` 选项，则显示每个 AC 的通道和 BSS 参数（第一个通道，然后是 BSS）。 当适配器启用 WME 模式时，此信息将与常规状态一起显示；当 WME 模式被禁用时，此命令对于检查参数非常有用。 有关各种参数的信息，请参阅 `wme` 指令的描述。

[`maxretry`](#maxretry) count

设置用于发送单播帧的最大尝试次数。 默认设置为 6，但驱动程序可以用他们选择的值覆盖它。

[`mcastrate`](#mcastrate) rate

设置传输多播/广播帧的速率。 速率指定为十进制的兆位/秒；例如，5.5 表示 5.5 Mb/s。 该比率应适用于当前的运行条件；如果指定了无效费率，司机可以自由选择合适的费率。

[`mgtrate`](#mgtrate) rate

设置传输管理和/或控制帧的速率。 速率指定为十进制的兆位/秒；例如，5.5 表示 5.5 Mb/s。

[`outdoor`](#outdoor)

设置用于计算监管约束的位置。 当使用 `dotd` 启用 802.11d 时，该位置也会在信标和探测响应帧中公布。 另请参阅 `anywhere`, `country`, `indoor` 和 `regdomain` 。

[`powersave`](#powersave)

启用省电操作。 当作为客户端运行时，站点将通过定期关闭无线电并监听来自接入点的消息来告诉它有数据包等待来节省电力。 然后该站必须检索数据包。 并非所有设备都支持作为客户端的省电操作。 802.11 规范要求所有接入点都支持节能，但有些驱动程序不支持。 当作为客户端运行时，使用 `-powersave` 禁用省电操作。

[`powersavesleep`](#powersavesleep) sleep

以 TU（1024 微秒）为单位设置所需的最大节能睡眠时间。 默认情况下，最大省电睡眠时间为 100 TU。

[`protmode`](#protmode) technique

对于在 802.11g 中运行的接口，使用指定的 technique 来保护混合 11b/11g 网络中的 OFDM 帧。 有效技术的集合是 `off`, `cts` (CTS to self) 和 `rtscts` (RTS/CTS)。 技术名称不区分大小写。 并非所有设备都支持 `cts` 作为保护技术。

[`pureg`](#pureg)

在 802.11g 模式下作为接入点运行时，仅允许关联 11g 站点（不允许关联仅 11b 站点）。 要允许 11g 和 11b-only 站点关联，请使用 `-pureg` 。

[`puren`](#puren)

在 802.11n 模式下作为接入点运行时，仅允许关联具有 HT 能力的站点（不允许关联旧站点）。 要允许 HT 和旧站关联，请使用 `-puren` 。

[`regdomain`](#regdomain) sku

设置监管域以用于计算操作的监管约束。 特别是可用信道的集合、无线设备将如何在信道上运行以及可以在信道上使用的最大发射功率由该设置定义。 Regdomain 代码（SKU）取自 /etc/regdomain.xml ，也可以通过 \`\`list countries'' 请求查看。 请注意，并非所有设备都支持从默认设置更改 regdomain；通常存储在 EEPROM 中。 另请参阅 `country`, `indoor`, `outdoor` 和 `anywhere` 。

[`rifs`](#rifs)

在 HT 通道上的 802.11n 中运行时启用缩减帧间间隔 (RIFS)。 请注意，站点和接入点都必须支持 RIFS 才能使用它。 要禁用 RIFS，请使用 `-rifs` 。

[`roam:rate`](#roam:rate) rate

设置在 BSS 中操作时控制漫游的阈值。 rate 参数指定应考虑漫游的传输速率（以兆比特为单位）。 如果当前传输速率低于此设置并且启用了后台扫描，则系统将检查是否有更理想的接入点可用并切换到该接入点。 如果根据 `scanvalid` 参数认为它们是有效的，则使用当前的扫描缓存内容；否则在任何选择发生之前触发后台扫描操作。 每种通道类型都有单独的速率阈值；默认值为：12 Mb/s (11a)、2 Mb/s (11b)、2 Mb/s (11g)、MCS 1 (11na, 11ng)。

[`roam:rssi`](#roam:rssi) rssi

设置在 BSS 中操作时控制漫游的阈值。 rssi 参数以 dBm 为单位指定应考虑漫游的接收信号强度。 如果当前 rssi 低于此设置并且启用了后台扫描，则系统将检查是否有更理想的接入点可用并切换到该接入点。 如果根据 `scanvalid` 参数认为它们是有效的，则使用当前的扫描缓存内容；否则在任何选择发生之前触发后台扫描操作。 每种通道类型都有单独的 rssi 阈值；默认值都是 7 dBm。

[`roaming`](#roaming) mode

作为工作站运行时，控制系统在与当前接入点的通信中断时的行为方式。 mode 参数可以是 `device` （留给硬件设备来决定）、 `auto` （在设备或操作系统中处理—视情况而定）、 `manual` 手动（在明确指示之前什么都不做）之一。 默认情况下，如果有能力，设备将自行处理；否则，操作系统将自动尝试重新建立通信。 手动模式由想要控制接入点选择的应用程序使用，例如 wpa\_supplicant(8) 。

[`rtsthreshold`](#rtsthreshold) length

设置在传输帧之前传输 RTS 控制帧的阈值。 length 参数是以字节为单位的帧大小，必须在 1 到 2346 的范围内。 将 length 设置为 `2346`, `any` 或 `-` 会禁用 RTS 帧的传输。 并非所有适配器都支持设置 RTS 阈值。

[`scan`](#scan)

开始扫描相邻电台，等待扫描完成，然后显示所有找到的电台。 只有超级用户可以启动扫描。 有关显示屏的信息，请参阅 `list scan` 。 默认情况下会进行后台扫描；否则会进行前景扫描，并且站点可能会漫游到不同的接入点。 `list scan` 请求可用于显示最近的扫描结果，而无需启动新扫描。

[`scanvalid`](#scanvalid) threshold

设置扫描缓存内容被认为有效的最长时间；即，将在不首先触发扫描操作来刷新数据的情况下使用。 threshold 参数以秒为单位指定，默认为 60 秒。 threshold 的最小设置为 10 秒。 应该注意设置这个阈值；如果设置得太低，则尝试漫游到另一个接入点可能会触发不必要的后台扫描操作。

[`shortgi`](#shortgi)

在 HT 通道上以 802.11n 运行时启用短保护间隔。 注意：这目前在 HT40 和 HT20 通道上都启用了 Short GI。 要禁用 Short GI，请使用 `-shortgi` 。

[`smps`](#smps)

在 802.11n 中运行时启用静态空间多路复用节能 (SMPS)。 使用静态 SMPS 运行的站仅保持单个接收链处于活动状态（这可以显着降低功耗）。 要禁用 SMPS，请使用 `-smps` 。

[`smpsdyn`](#smpsdyn)

在 802.11n 中运行时启用动态空间多路复用节能 (SMPS)。 使用动态 SMPS 运行的站仅保持单个接收链处于活动状态，但在接收到 RTS 帧时切换到多个接收链（这可以显着降低功耗）。 请注意，电台无法区分旨在启用多个接收链的 RTS/CTS 和用于其他目的的 RTS/CTS。 要禁用 SMPS，请使用 `-smps` 。

[`ssid`](#ssid) ssid

设置所需的服务集标识符（又名网络名称）。 SSID 是一个长度最多为 32 个字符的字符串，可以指定为普通字符串，也可以指定为以 ‘`0x`’ 开头的十六进制。 此外，可以通过将 SSID 设置为 ‘`-`’ 来清除 SSID。

[`tdmaslot`](#tdmaslot) slot

使用 TDMA 操作时，请使用指定的 slot 配置。 slot 是一个介于 0 和 BSS 中的最大时隙数之间的数字。 请注意，配置为时隙 0 的站是主站，将广播信标帧来通告 BSS；配置为使用其他时隙的站将始终在传输之前扫描以定位主站。 默认情况下 `tdmaslot` 设置为 1。

[`tdmaslotcnt`](#tdmaslotcnt) cnt

使用 TDMA 操作时，设置带有 cnt 插槽的 BSS。 时隙数最多可以是 8 个。当前的实现只测试了两个站（即点对点应用程序）。 此设置仅在站点配置为插槽 0 时才有意义；其他站从它们加入的 BSS 中采用此设置。 默认情况下 `tdmaslotcnt` 设置为 2。

[`tdmaslotlen`](#tdmaslotlen) len

当使用 TDMA 操作时，设置一个 BSS 以便每个站都有一个时隙 len 微秒长。 时隙长度必须至少为 150 微秒 (1/8 TU) 且不超过 65 毫秒。 请注意，设置过小的时隙长度可能会由于定时器粒度和保护时间等因素导致信道带宽利用率不佳。 此设置仅在站点配置为插槽 0 时才有意义；其他站从它们加入的 BSS 中采用此设置。 默认情况下， `tdmaslotlen` 设置为 10 毫秒。

[`tdmabintval`](#tdmabintval) intval

使用 TDMA 操作时，设置 BSS 以便在每个 intval 超帧发送信标以同步 TDMA 时隙时序。 超帧定义为时隙数乘以时隙长度；例如，具有两个 10 毫秒时隙的 BSS 具有 20 毫秒的超帧。 信标间隔可能不为零。 较低的 `tdmabintval` 设置会导致计时器更频繁地重新同步；如果观察到明显的计时器漂移，这可能会有所帮助。 默认情况下， `tdmabintval` 设置为 5。

[`tsn`](#tsn)

当使用 WPA/802.11i 作为接入点运行时，允许旧站使用静态密钥 WEP 和开放式身份验证进行关联。 要禁止旧站使用 WEP，请使用 `-tsn` 。

[`txpower`](#txpower) power

设置用于传输帧的功率。 power 参数以 0.5 dBm 为单位指定。 超出范围的值将被截断。 通常只有几个谨慎的电源设置可用，驱动程序将使用最接近指定值的设置。 并非所有适配器都支持更改发射功率。

[`ucastrate`](#ucastrate) rate

设置传输单播帧的固定速率。 速率指定为十进制的兆位/秒；例如，5.5 表示 5.5 Mb/s。 该比率应适用于当前的运行条件；如果指定了无效费率，司机可以自由选择合适的费率。

[`wepmode`](#wepmode) mode

设置所需的 WEP 模式。 并非所有适配器都支持所有模式。 有效模式集是 `off`, `on` 和 `mixed` 。 `mixed` 模式明确告诉适配器允许与允许加密和未加密流量的接入点关联。 在这些适配器上， `on` 表示接入点必须只允许加密连接。 在其他适配器上， `on` 通常是 `mixed` 的另一个名称。 模式不区分大小写。

[`weptxkey`](#weptxkey) index

设置用于传输的 WEP 密钥。 这与使用 `deftxkey` 设置默认传输密钥相同。

[`wepkey`](#wepkey) key|index:key

设置选择的 WEP 密钥。 如果未给出 index ，则设置键 1。 WEP 密钥将是 5 或 13 个字符（40 或 104 位），具体取决于本地网络和适配器的功能。 它可以指定为纯字符串或以 ‘`0x`’ 开头的十六进制数字字符串。 为了获得最大的便携性，建议使用十六进制键；文本密钥到 WEP 加密的映射通常是特定于驱动程序的。 特别是，Windows 驱动程序执行此映射的方式与 FreeBSD 不同。 可以通过将键设置为 ‘`-`’ 来清除键。 如果支持 WEP，则至少有四个密钥。 一些适配器支持四个以上的键。 如果是这种情况，那么前四个密钥 (1-4) 将是标准临时密钥，任何其他密钥将是适配器特定密钥，例如存储在 NVRAM 中的永久密钥。

请注意，您必须使用 `deftxkey` 设置默认传输密钥，以便系统知道在加密出站流量时使用哪个密钥。

[`wme`](#wme)

为指定的接口启用无线多媒体扩展 (WME) 支持（如果可用）。 WME 是 IEEE 802.11e 标准的子集，用于支持实时和多媒体数据的高效通信。 要禁用 WME 支持，请使用 `-wme` 。 此参数的另一个名称是 `wmm` 。

以下参数仅在使用 WME 支持时才有意义。 参数是按 AC（访问类别）指定的，并分为站点作为接入点时使用的参数和 BSS 中客户端站点使用的参数。 后者是从接入点接收的，并且可能不会更改（在站）。 认可以下访问类别：

[`AC_BE`](#AC_BE)

(或 `BE`) 尽力交付，

[`AC_BK`](#AC_BK)

(或 `BK`) 后台流量、

[`AC_VI`](#AC_VI)

(或 `VI`) 视频流量、

[`AC_VO`](#AC_VO)

(或 `VO`) 语音流量。

AC 参数不区分大小写。 流量分类是在操作系统中使用与数据帧相关联的 vlan 优先级或 IP 封装帧中的 ToS（服务类型）指示来完成的。 如果两个信息都不存在，则将流量分配给尽力而为 (BE) 类别。

[`ack`](#ack) ac

设置本地站QoS传输的ACK策略；这控制了一个站发送的数据帧是否需要接收站的 ACK 响应。 要禁用等待 ACK，请使用 `-ack` 。 此参数仅适用于本地站。

[`acm`](#acm) ac

为本地站的传输启用强制准入控制 (ACM) 机制。 要禁用 ACM，请使用 `-acm` 。 在 BSS 中的站上，此参数是只读的，表示从接入点接收的设置。 注意：目前不支持 ACM。

[`aifs`](#aifs) ac count

设置仲裁帧间间隔 (AIFS) 通道访问参数以用于本地站的传输。 在 BSS 中的站上，此参数是只读的，表示从接入点接收的设置。

[`cwmin`](#cwmin) ac count

设置 CWmin 信道访问参数以用于本地站的传输。 在 BSS 中的站上，此参数是只读的，表示从接入点接收的设置。

[`cwmax`](#cwmax) ac count

设置 CWmax 信道访问参数以用于本地站的传输。在 BSS 中的站上，此参数是只读的，表示从接入点接收的设置。

[`txoplimit`](#txoplimit) ac limit

设置传输机会限制信道访问参数以用于本地站的传输。 该参数定义了 WME 站有权在无线介质上发起传输的时间间隔。 在 BSS 中的站上，此参数是只读的，表示从接入点接收的设置。

[`bss:aifs`](#bss:aifs) ac count

设置 AIFS 信道访问参数以发送到 BSS 中的站。 该参数仅在 ap 模式下运行时才有意义。

[`bss:cwmin`](#bss:cwmin) ac count

设置 CWmin 信道访问参数以发送到 BSS 中的站。 该参数仅在 ap 模式下运行时才有意义。

[`bss:cwmax`](#bss:cwmax) ac count

设置 CWmax 信道访问参数以发送到 BSS 中的站。 该参数仅在 ap 模式下运行时才有意义。

[`bss:txoplimit`](#bss:txoplimit) ac limit

设置 TxOpLimit 信道访问参数以发送到 BSS 中的站。 该参数仅在 ap 模式下运行时才有意义。

[`wps`](#wps)

启用无线隐私订阅者支持。 请注意，WPS 支持需要支持 WPS 的请求者。 要禁用此功能，请使用 `-wps` 。

以下参数支持在 ap 模式下运行时某些适配器可用的可选访问控制列表功能；参见 wlan\_acl(4) 。 该工具允许接入点根据站点的 MAC 地址接受/拒绝关联请求。 请注意，此功能不会显着增强安全性，因为 MAC 地址欺骗很容易做到。

[`mac:add`](#mac:add) address

将指定的 MAC 地址添加到数据库中。根据策略设置，来自指定站的关联请求将被允许或拒绝。

[`mac:allow`](#mac:allow)

将 ACL 策略设置为仅允许在数据库中注册的站点进行关联。

[`mac:del`](#mac:del) address

从数据库中删除指定的 MAC 地址。

[`mac:deny`](#mac:deny)

将 ACL 策略设置为仅拒绝与数据库中注册的站点关联。

[`mac:kick`](#mac:kick) address

强制取消对指定站的身份验证。 这通常是为了在更新地址数据库后封锁一个电台。

[`mac:open`](#mac:open)

设置 ACL 策略以允许所有站点关联。

[`mac:flush`](#mac:flush)

删除数据库中的所有条目。

[`mac:radius`](#mac:radius)

将 ACL 策略设置为仅允许由 RADIUS 服务器批准的站点关联。 请注意，此功能需要将 hostapd(8) 程序配置为在处理 RADIUS 处理（并将站点标记为已授权）时执行正确的操作。

以下参数与在 Mesh 模式下运行的无线接口相关：

[`meshid`](#meshid) meshid

设置所需的 Mesh 标识符。 Mesh ID 是一个最长 32 个字符的字符串。 网格接口必须具有指定的网格标识符才能达到操作状态。

[`meshttl`](#meshttl) ttl

为网状转发数据包设置所需的 \`\`time to live'' ；这是一个数据包在被丢弃之前可以转发的跳数。 `meshttl` 的默认设置是 31。

[`meshpeering`](#meshpeering)

启用或禁用与相邻网状站的对等。 在交换任何数据包之前，站点必须对等。 默认情况下， `meshpeering` 已启用。

[`meshforward`](#meshforward)

启用或禁用网状接口转发数据包。 默认情况下启用 `meshforward` 。

[`meshgate`](#meshgate)

该属性指定 mesh STA 是否激活mesh Gate 通告。 默认情况下， `meshgate` 是禁用的。

[`meshmetric`](#meshmetric) protocol

将指定的 protocol 设置为 mesh 网络中使用的链路度量协议。 默认协议称为 AIRTIME 。 更改此设置后，mesh 界面将重新启动。

[`meshpath`](#meshpath) protocol

将指定的 protocol 设置为 mesh 网络中使用的路径选择协议。 目前唯一可用的协议称为 HWMP （混合无线网状网协议）。 更改此设置后，mesh 界面将重新启动。

[`hwmprootmode`](#hwmprootmode) mode

网状网络上的站点可以作为 \`\`root nodes'' 运行。 根节点尝试找到通向所有网状节点的路径并定期通告自己。 当网络上有根网状节点时，其他网状节点可以更快地在它们之间建立路径，因为它们可以使用根节点找到目的地。 这条路径可能不是最好的，但按需路由最终会找到最好的路径。 可识别以下模式：

[`DISABLED`](#DISABLED)

禁用 root 模式。

[`NORMAL`](#NORMAL)

每两秒发送一次广播路径请求。 网格上没有通往该根网格站的路径的节点会尝试发现通往我们的路径。

[`PROACTIVE`](#PROACTIVE)

每两秒发送一次广播路径请求，每个节点都必须用路径回复进行回复，即使它已经有到该根网状站的路径。

[`RANN`](#RANN)

发送广播根通告 (RANN) 帧。 网格上没有通往该根网格站的路径的节点会尝试发现通往我们的路径。

默认情况下， `hwmprootmode` 设置为 DISABLED 。

[`hwmpmaxhops`](#hwmpmaxhops) cnt

将 HMWP 路径中允许的最大跳数设置为 cnt 。 `hwmpmaxhops` 的默认设置是 31。

以下参数是为了与其他系统兼容：

[`nwid`](#nwid) ssid

[`ssid`](#ssid_2) 参数的另一个名称。 包括 NetBSD 兼容性。

[`stationname`](#stationname) name

设置本站的名称。 站名不是 IEEE 802.11 协议的一部分，尽管某些接口支持它。 因此，它似乎只对相同或几乎相同的设备有意义。设置站名的语法与设置 SSID 相同。 也可以使用 `station` 来实现 BSD/OS 兼容性。

[`wep`](#wep)

[`wepmode on`](#wepmode_on) 的另一种说法。 包括用于 BSD/OS 兼容性。

[`-wep`](#wep_2)

[`wepmode off`](#wepmode_off) 的另一种说法。 包括用于 BSD/OS 兼容性。

[`nwkey key`](#nwkey_key)

另一种说法： “`wepmode on weptxkey 1 wepkey 1:key wepkey 2:- wepkey 3:- wepkey 4:-`” 。 包括 NetBSD 兼容性。

[`nwkey`](#nwkey) n:k1,k2,k3,k4

“`wepmode on weptxkey n wepkey 1:k1 wepkey 2:k2 wepkey 3:k3 wepkey 4:k4`” 的另一种说法。 包括 NetBSD 兼容性。

[`-nwkey`](#nwkey_2)

[`wepmode off`](#wepmode_off_2) 另一种说法。 包括 NetBSD 兼容性。

以下参数特定于网桥接口：

[`addm`](#addm) interface

将 interface 命名的接口添加为网桥的成员。 该接口被置于混杂模式，以便它可以接收网络上发送的每个数据包。

[`deletem`](#deletem) interface

从网桥中删除由 interface 命名的接口。 当从网桥中删除接口时，混杂模式在接口上被禁用。

[`maxaddr`](#maxaddr) size

将桥地址缓存的大小设置为 size 。 默认值为 2000 个条目。

[`timeout`](#timeout) seconds

将地址缓存条目的超时时间设置为 seconds 秒。 如果 seconds 为零，则地址缓存条目不会过期。 默认值为 1200 秒。

[`addr`](#addr)

显示网桥已获知的地址。

[`static`](#static) interface-name address

将静态条目添加到指向 interface-name 的地址缓存中。 即使在不同的接口上看到地址，静态条目也不会从缓存中老化或重新放置。

[`deladdr`](#deladdr) address

从地址缓存中删除 address 。

[`flush`](#flush)

从地址缓存中删除所有动态学习的地址。

[`flushall`](#flushall)

从地址缓存中删除所有地址，包括静态地址。

[`discover`](#discover) interface

标记为 “discovering” 接口。 当网桥没有针对数据包目的地址的地址缓存条目（动态或静态）时，网桥会将数据包转发到所有标记为 “discovering” 的成员接口。 这是添加到网桥的所有接口的默认设置。

[`-discover`](#-discover) interface

清除成员接口上的 “discovering” 属性。 对于没有 “discovering” 属性的数据包，在接口上转发的唯一数据包是广播或多播数据包以及已知目标地址位于接口网段上的数据包。

[`learn`](#learn) interface

标记为 “learning” 界面。 当数据包到达这样的接口时，数据包的源地址将作为接口段上的目标地址输入地址缓存。 这是添加到网桥的所有接口的默认设置。

[`-learn`](#-learn) interface

清除成员接口上的 “learning” 属性。

[`sticky`](#sticky) interface

标记为 “sticky” 界面。 动态学习的地址条目一旦进入高速缓存，就会被静态处理。 粘性条目永远不会从缓存中老化或被替换，即使在不同的接口上看到地址也是如此。

[`-sticky`](#-sticky) interface

清除成员接口的 “sticky” 属性。

[`private`](#private) interface

标记为 “private” 接口。 私有接口不会将任何流量转发到也是私有接口的任何其他端口。

[`-private`](#-private) interface

清除成员接口上的 “private” 属性。

[`span`](#span) interface

在网桥上添加 interface 命名的接口作为 span 端口。 Span 端口传输网桥接收到的每个帧的副本。 这对于在连接到桥接器的跨接端口之一的另一台主机上被动地窥探桥接网络最有用。

[`-span`](#-span) interface

从网桥的 span 端口列表中删除以 interface 命名的接口。

[`stp`](#stp) interface

在 interface 上启用生成树协议。 if\_bridge(4) 驱动程序支持 IEEE 802.1D 生成树协议 (STP)。 生成树用于检测和移除网络拓扑中的环路。

[`-stp`](#-stp) interface

在 interface 上禁用生成树协议。这是添加到网桥的所有接口的默认设置。

[`edge`](#edge) interface

将 interface 设置为边缘端口。 直接连接到终端站的边缘端口不能在网络中创建桥接环路，这允许它直接转换为转发。

[`-edge`](#-edge) interface

在 interface 上禁用边缘状态。

[`autoedge`](#autoedge) interface

允许 interface 自动检测边缘状态。 这是添加到网桥的所有接口的默认设置。

[`-autoedge`](#-autoedge) interface

禁用 interface 上的自动边缘状态。

[`ptp`](#ptp) interface

将 interface 设置为点对点链接。 这是直接转换到转发所必需的，并且应该在到另一个支持 RSTP 的交换机的直接链路上启用。

[`-ptp`](#-ptp) interface

禁用 interface 上的点对点链接状态。 对于半双工链路和连接到共享网段（如集线器或无线网络）的接口，应禁用此功能。

[`autoptp`](#autoptp) interface

通过检查全双工链路状态自动检测 interface 上的点对点状态。 这是添加到网桥的接口的默认设置。

[`-autoptp`](#-autoptp) interface

禁用 interface 上的自动点对点链接检测。

[`maxage`](#maxage) seconds

设置生成树协议配置有效的时间。 默认值为 20 秒。 最短为 6 秒，最长为 40 秒。

[`fwddelay`](#fwddelay) seconds

设置启用 Spanning Tree 时接口开始转发数据包之前必须经过的时间。 默认值为 15 秒。 最短为 4 秒，最长为 30 秒。

[`hellotime`](#hellotime) seconds

设置生成树协议配置消息广播之间的时间。 hello 时间只能在旧 stp 模式下操作时更改。 默认值为 2 秒。 最小值为 1 秒，最大值为 2 秒。

[`priority`](#priority) value

设置生成树的网桥优先级。 默认为 32768。 最小值为 0，最大值为 61440。

[`proto`](#proto) value

设置 Spanning Tree 协议。 默认值为 rstp。 可用的选项是 stp 和 rstp。

[`holdcnt`](#holdcnt) value

设置 Spanning Tree 的传输保持计数。这是在速率限制之前传输的数据包数量。 默认值为 6。 最小值为 1，最大值为 10。

[`ifpriority`](#ifpriority) interface value

将 interface 的生成树优先级设置为 value 。 默认值为 128。 最小值为 0，最大值为 240。

[`ifpathcost`](#ifpathcost) interface value

将 interface 的 Spanning Tree 路径成本设置为 value 。 默认值是根据链接速度计算的。 要将先前选择的路径成本更改回自动，请将成本设置为 0。 最小值为 1，最大值为 200000000。

[`ifmaxaddr`](#ifmaxaddr) interface size

设置接口允许的最大主机数，源地址未知的数据包将被丢弃，直到现有的主机缓存条目过期或被删除。 设置为 0 以禁用。

以下参数特定于滞后接口：

[`laggtype`](#laggtype) type

创建 lagg 接口时，可以将类型指定为 `ethernet` 或 `infiniband` 。 如果未指定以太网是默认滞后类型。

[`laggport`](#laggport) interface

将 interface 命名的接口添加为聚合接口的端口。

[`-laggport`](#-laggport) interface

从聚合 interface 中删除接口命名的接口。

[`laggproto`](#laggproto) proto

设置聚合协议。 默认为 `failover` 。 可用选项包括 `failover`, `lacp`, `loadbalance`, `roundrobin`, `broadcast` 和 `none` 。

[`lagghash`](#lagghash) option\[,option\]

将数据包层设置为散列以用于负载平衡的聚合协议。 默认值为 “l2,l3,l4” 。 可以使用逗号组合选项。

[`l2`](#l2)

src/dst mac 地址和可选的 vlan 号。

[`l3`](#l3)

IPv4 或 IPv6 的 src/dst 地址。

[`l4`](#l4)

src/dst 端口用于 TCP/UDP/SCTP。

[`-use_flowid`](#-use_flowid)

为接口上的 RSS 散列启用本地散列计算。 `loadbalance` 和 `lacp` 模式将使用来自网卡的 RSS 哈希（如果可用）以避免计算一个，如果哈希无效或使用较少的协议头信息，这可能会导致流量分布不佳。 `-use_flowid` 禁止使用来自网卡的 RSS 散列。 默认值可以通过 net.link.lagg.default\_use\_flowid sysctl(8) 变量设置。 `0` 表示 “disabled” ， `1` 表示 “enabled” 。

[`use_flowid`](#use_flowid)

如果可用，请使用网卡中的 RSS 哈希。

[`flowid_shift`](#flowid_shift) number

设置 RSS 本地哈希计算的 shift 参数。 哈希是通过使用数据包头 mbuf 中的 flowid 位来计算的，这些位移动了该参数的数量。

[`use_numa`](#use_numa)

根据正在传输的数据包的本机 NUMA(4) 域启用出口端口选择。 目前仅对 lacp 模式实施。 这仅适用于 NUMA(4) 硬件，运行使用 NUMA(4) 选项编译的内核，并且当来自多个 NUMA(4) 域的接口是聚合接口的端口时。

[`-use_numa`](#-use_numa)

禁止根据本机 NUMA(4) 域为正在传输的数据包选择出口端口。

[`lacp_fast_timeout`](#lacp_fast_timeout)

在接口上启用 lacp fast-timeout。

[`-lacp_fast_timeout`](#-lacp_fast_timeout)

在接口上禁用 lacp 快速超时。

[`lacp_strict`](#lacp_strict)

在接口上启用 lacp 严格合规性。 默认值可以通过 net.link.lagg.lacp.default\_strict\_mode sysctl(8) 变量设置。 `0` 表示 “disabled” ， `1` 表示 “enabled” 。

[`-lacp_strict`](#-lacp_strict)

在接口上禁用 lacp 严格合规性。

[`rr_limit`](#rr_limit) number

为轮询模式的接口配置步幅。 默认步幅为 1。

以下参数适用于 IP 隧道接口 gif(4):

[`tunnel`](#tunnel) src\_addr dest\_addr

配置 IP 隧道接口的物理源地址和目标地址。 参数 src\_addr 和 dest\_addr 被解释为封装 IPv4/IPv6 标头的外部源/目标。

[`-tunnel`](#tunnel_2)

取消配置以前使用 `tunnel` 配置的 IP 隧道接口的物理源和目标地址。

[`deletetunnel`](#deletetunnel)

[`-tunnel`](#tunnel_3) 参数的另一个名称。

[`accept_rev_ethip_ver`](#accept_rev_ethip_ver)

设置一个标志以接受正确的 EtherIP 数据包和具有反转版本字段的数据包。 默认启用。 这是为了向后兼容 FreeBSD 6.1, 6.2, 6.3, 7.0, 和 7.1 。

[`-accept_rev_ethip_ver`](#-accept_rev_ethip_ver)

清除标志 `accept_rev_ethip_ver` 。

[`ignore_source`](#ignore_source)

设置一个标志以独立于源地址接受发往该主机的封装数据包。 这对于从负载平衡器接收封装数据包的主机可能很有用。

[`-ignore_source`](#-ignore_source)

清除标志 `ignore_source` 。

[`send_rev_ethip_ver`](#send_rev_ethip_ver)

设置一个标志以故意发送带有反转版本字段的 EtherIP 数据包。 默认禁用。 这是为了向后兼容 FreeBSD 6.1, 6.2, 6.3, 7.0, 和 7.1 。

[`-send_rev_ethip_ver`](#-send_rev_ethip_ver)

清除标志 `send_rev_ethip_ver` 。

以下参数适用于 GRE 隧道接口 gre(4):

[`tunnel`](#tunnel_4) src\_addr dest\_addr

配置 GRE 隧道接口的物理源地址和目标地址。 参数 src\_addr 和 dest\_addr 被解释为封装 IPv4/IPv6 标头的外部源/目标。

[`-tunnel`](#tunnel_5)

取消之前配置了 `tunnel` 的 GRE 隧道接口的物理源地址和目标地址。

[`deletetunnel`](#deletetunnel_2)

[`-tunnel`](#tunnel_6) 参数的另一个名称。

[`grekey`](#grekey) key

配置用于传出数据包的 GRE 密钥。 请注意， gre(4) 将始终接受带有无效或缺少密钥的 GRE 数据包。 此命令将导致接口上的 4 字节 MTU 减少。

以下参数特定于 pfsync(4) 接口：

[`syncdev`](#syncdev) iface

使用指定的接口发送和接收 pfsync 状态同步消息。

[`-syncdev`](#syncdev_2)

停止通过网络发送 pfsync 状态同步消息。

[`syncpeer`](#syncpeer) peer\_address

使 pfsync 链接点对点，而不是使用多播来广播状态同步消息。 peer\_address 是参与 pfsync 集群的其他主机的 IP 地址。

[`-syncpeer`](#syncpeer_2)

使用多播广播数据包。

[`maxupd`](#maxupd) n

设置可以折叠为一个的单个状态的最大更新次数。 这是一个 8 位数字；默认值为 128。

[`defer`](#defer)

延迟状态中第一个数据包的传输，直到对等方确认已插入关联状态。

[`-defer`](#defer_2)

不要延迟状态中的第一个数据包。 这是默认设置。

以下参数特定于 vlan(4) 接口：

[`vlan`](#vlan) vlan\_tag

将 VLAN 标记值设置为 vlan\_tag 。 该值是一个 12 位 VLAN 标识符 (VID)，用于为从 vlan(4) 接口发送的数据包创建 802.1Q 或 802.1ad VLAN 标头。 注意 `vlan` 和 `vlandev` 必须同时设置。

[`vlanproto`](#vlanproto) vlan\_proto

将 VLAN 封装协议设置为 vlan\_proto 。 目前支持的封装协议有 “802.1Q” 和 “802.1ad” 。 默认封装协议为 “802.1Q” 。 “802.1ad” 协议也俗称 “QinQ” ；可以使用任何一个名称。

[`vlanpcp`](#vlanpcp) priority\_code\_point

级代码点 (`PCP`) 是一个 3 位字段，它涉及 IEEE 802.1p 服务类别并映射到帧优先级。

Values in order of priority are: `1` (`背景（最低）,`) `0` (`尽力而为（默认）`), `2` (`出色的工作`), `3` (`关键应用程序`), `4` (`视频，< 100ms 延迟`), `5` (`视频，< 10ms 延迟`), `6` (`网络控制`), `7` (`网络控制（最高）`) 。

[`vlandev`](#vlandev) iface

将物理接口 iface 与 vlan(4) 接口相关联。 通过 vlan(4) 接口传输的数据包将被转移到具有 802.1Q VLAN 封装的指定物理接口 iface 。 具有正确 VLAN 标识符的父接口接收到的带有 802.1Q 封装的数据包将被转移到关联的 vlan(4) 伪接口。 vlan(4) 接口被分配了父接口标志和父接口以太网地址的副本。 `vlandev` 和 `vlan` 必须同时设置。 如果 vlan(4) 接口已经有一个与之关联的物理接口，则此命令将失败。 要将关联更改为另一个物理接口，必须先清除现有关联。

注意：如果在父接口上设置了硬件标记能力， vlan(4) 伪接口的行为会发生变化： vlan(4) 接口识别出父接口支持自己插入和提取 VLAN 标签（通常在固件中）并且它应该将数据包原封不动地传入和传出父级。

[`-vlandev`](#vlandev_2) \[iface\]

如果驱动程序是 vlan(4) 伪设备，则取消父接口与其的关联。 这会中断 vlan(4) 接口与其父接口之间的链路，清除其 VLAN 标识符、标志及其链路地址并关闭接口。 iface 参数是无用的，因此不推荐使用。

以下参数用于配置 vxlan(4) 接口。

[`vxlanid`](#vxlanid) identifier

该值是一个 24 位 VXLAN 网络标识符 (VNI)，用于标识接口的虚拟网段成员资格。

[`vxlanlocal`](#vxlanlocal) address

封装 IPv4/IPv6 标头中使用的源地址。 该地址应该已经分配给现有接口。 当接口配置为单播模式时，监听套接字绑定到该地址。

[`vxlanremote`](#vxlanremote) address

该接口可以配置为单播或点对点模式，以在两台主机之间创建隧道。 这是隧道远端的 IP 地址。

[`vxlangroup`](#vxlangroup) address

该接口可以配置为多播模式以创建主机虚拟网络。 这是接口将加入的 IP 多播组地址。

[`vxlanlocalport`](#vxlanlocalport) port

接口将侦听的端口号。 默认端口号为 4789。

[`vxlanremoteport`](#vxlanremoteport) port

封装 IPv4/IPv6 标头中使用的目标端口号。 远程主机应该在这个端口上监听。 默认端口号为 4789。 请注意，其他一些实现，例如 Linux，不默认使用 IANA 分配的端口，而是侦听端口 8472。

[`vxlanportrange`](#vxlanportrange) low high

封装 IPv4/IPv6 标头中使用的源端口范围。 在该范围内选择的端口基于内部帧的哈希。 范围可用于在外部 IP 标头中提供熵，以实现更有效的负载平衡。 默认范围在 sysctl(8) 变量 net.inet.ip.portrange.first 和 net.inet.ip.portrange.last 之间。

[`vxlantimeout`](#vxlantimeout) timeout

转发表中的条目被修剪之前的最长时间（以秒为单位）。 默认值为 1200 秒（20 分钟）。

[`vxlanmaxaddr`](#vxlanmaxaddr) max

转发表中的最大条目数。 默认值为 2000。

[`vxlandev`](#vxlandev) dev

当接口配置为组播模式时， `dev` 接口用于传输 IP 组播数据包。

[`vxlanttl`](#vxlanttl) ttl

封装 IPv4/IPv6 标头中使用的 TTL。 默认值为 64。

[`vxlanlearn`](#vxlanlearn)

接收数据包的源 IP 地址和内部源以太网 MAC 地址用于动态填充转发表。 在多播模式下，转发表中的条目允许接口直接将帧发送到远程主机，而不是将帧广播到多播组。 这是默认设置。

[`-vxlanlearn`](#vxlanlearn_2)

转发表不会由接收到的数据包填充。

[`vxlanflush`](#vxlanflush)

从转发表中删除所有动态学习的地址。

[`vxlanflushall`](#vxlanflushall)

从转发表中删除所有地址，包括静态地址。

以下参数用于在接口上配置 carp(4) 协议：

[`vhid`](#vhid) n

设置虚拟主机 ID。 这是启动 carp(4) 所需的设置。 如果虚拟主机 ID 尚不存在，则创建并附加到接口，否则调整现有 vhid 的配置。 如果 `vhid` 关键字与 “inet6” 或 “inet” 地址一起提供，则此地址配置为在指定 vhid 的控制下运行。 每当从接口中删除引用特定 vhid 的最后一个地址时，vhid 就会自动从接口中删除并销毁。 carp(4) 协议的任何其他配置参数都应与 `vhid` 关键字一起提供。 vhid 的可接受值为 1 到 255。

[`advbase`](#advbase) seconds

以秒为单位指定广播间隔的基数。 可接受的值为 1 到 255。 默认值为 1。

[`advskew`](#advskew) interval

指定要添加到基本通告间隔的偏差，以使一个主机的通告速度比另一台主机慢。 它以 1/256 秒为单位指定。 可接受的值为 1 到 254。 默认值为 0。

[`pass`](#pass) phrase

将身份验证密钥设置为 phrase 。

[`state`](#state) MASTER|BACKUP

强制更改给定 vhid 的状态。

如果未提供可选参数， `ifconfig` 实用程序会显示网络接口的当前配置。 如果指定了协议族， `ifconfig` 将仅报告特定于该协议族的详细信息。

如果在接口名称之前传递 `-m` 标志， `ifconfig` 将显示指定接口的功能列表和所有支持的媒体。 如果提供 `-L` 标志，则显示 IPv6 地址的地址生存期，作为时间偏移字符串。

可选地，可以使用 `-a` 标志代替接口名称。 此标志指示 `ifconfig` 显示有关系统中所有接口的信息。 `-d` 标志将其限制为关闭的接口， `-u` 将其限制为启动的接口， `-g` 将其限制为指定接口组的成员， `-G` 从列表中排除指定组的成员。 可以同时指定 `-g` 和 `-G` 标志来应用这两个条件。 只有一个选项 `-g` 应指定为稍后覆盖以前的选项（与 `-G` 相同）。 **groupname** 可能包含 shell 模式，在这种情况下它应该被引用。 当没有给出参数时， `-a` 是隐含的。

`-l` 标志可用于列出系统上所有可用的接口，没有其他附加信息。 如果指定了 address\_family ，则只会列出该类型的接口。 `-l` “ether” 将仅列出以太网适配器，不包括环回接口。 此标志的使用与所有其他标志和命令互斥，但 `-d` （仅列出已关闭的接口）和 `-u` （仅列出已启动的接口）除外。

`-v` 标志可用于获取接口的更详细状态。

`-C` 标志可用于列出系统上所有可用的接口克隆器，无需额外信息。 此标志的使用与所有其他标志和命令互斥。

`-k` 标志会打印接口的密钥信息（如果可用）。 例如，如果当前用户可以访问，则将打印 802.11 WEP 密钥和 carp(4) 密码短语的值。 默认情况下不打印此信息，因为它可能被视为敏感信息。

如果内核中不存在网络接口驱动程序，则 `ifconfig` 将尝试加载它。 `-n` 标志禁用此行为。

只有超级用户可以修改网络接口的配置。

[实例](#__u5B9E___u4F8B_)
=======================

将 IPv4 地址 `192.0.2.10` 和网络掩码 `255.255.255.0` 分配给接口 `em0`:

`# ifconfig em0 inet 192.0.2.10 netmask 255.255.255.0`

将带有 CIDR 网络前缀 `/28` 的 IPv4 地址 `192.0.2.45` 添加到接口 `em0` ，使用 `add` 作为选项 `alias` 的规范形式的同义词：

`# ifconfig em0 inet 192.0.2.45/28 add`

从接口 `em0` 中删除 IPv4 地址 `192.0.2.45` :

`# ifconfig em0 inet 192.0.2.45 -alias`

启用接口的 IPv6 功能：

`# ifconfig em0 inet6 -ifdisabled`

将 IPv6 地址 `2001:DB8:DBDB::123/48` 添加到接口 `em0`:

`# ifconfig em0 inet6 2001:db8:bdbd::123 prefixlen 48 alias`

请注意，小写十六进制 IPv6 地址是可接受的。

删除上面示例中添加的 IPv6 地址，使用 `/` 字符作为网络前缀的简写，并使用 `delete` 作为选项 `-alias` 的规范形式的同义词：

`# ifconfig em0 inet6 2001:db8:bdbd::123/48 delete`

在 igb0 上配置一个 CARP 冗余地址，然后切换为 master：

`# ifconfig igb0 vhid 1 10.0.0.1/24 pass foobar up`

`# ifconfig igb0 vhid 1 state master`

配置接口 `xl0`, 使用 100baseTX，全双工以太网媒体选项：

`# ifconfig xl0 media 100baseTX mediaopt full-duplex`

将 em0 接口标记为上行链路：

`# ifconfig em0 description "Uplink to Gigabit Switch 2"`

创建软件网络接口 `gif1`:

`# ifconfig gif1 create`

破坏软件网络接口 `gif1`:

`# ifconfig gif1 destroy`

使用 `wlan0` 显示可用的无线网络：

`# ifconfig wlan0 list scan`

以 CIDR 表示法显示 inet 和 inet6 地址子网掩码

`# ifconfig -f inet:cidr,inet6:cidr`

显示除环回外的已启动接口

`# ifconfig -a -u -G lo`

[诊断](#__u8BCA___u65AD_)
=======================

指示指定接口不存在、请求的地址未知或用户没有特权并试图更改接口配置的消息。

[参见](#__u53C2___u89C1_)
=======================

netstat(1), carp(4), gif(4), netintro(4), pfsync(4), polling(4), vlan(4), vxlan(4), devd.conf(5), devd(8), jail(8), rc(8), routed(8), sysctl(8)

[历史](#__u5386___u53F2_)
=======================

`ifconfig` 实用程序出现在 4.2BSD 中。

[缺陷](#__u7F3A___u9677_)
=======================

基本 IPv6 节点操作需要为 IPv6 配置的每个接口上的链路本地地址。 通常，内核会在每个添加到系统或启用的接口上自动配置这样的地址；可以通过设置每个接口标志 `-auto_linklocal` 来禁用此行为。 此标志的默认值为 1，可以使用 sysctl MIB 变量 net.inet6.ip6.auto\_linklocal 禁用。

不要使用 `ifconfig` 配置没有链路本地地址的 IPv6 地址。 它可能导致内核的意外行为。

November 1, 2020

FreeBSD 13.1-RELEASE