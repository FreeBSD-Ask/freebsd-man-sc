  NETSTAT(1)  

NETSTAT(1)

FreeBSD General Commands Manual

NETSTAT(1)

[名称](#__u540D___u79F0_)
=======================

`netstat` —

显示网络状态和统计信息

[概要](#__u6982___u8981_)
=======================

`netstat`

\[`--libxo`\] \[`-46AaCLnPRSTWx`\] \[`-f` protocol\_family | `-p` protocol\] \[`-M` core\] \[`-N` system\]

`netstat` `-i` | [`-I`](#I) interface

\[`--libxo`\] \[`-46abdhnW`\] \[`-f` address\_family\] \[`-M` core\] \[`-N` system\]

`netstat` `-w` wait

\[`--libxo`\] \[`-I` interface\] \[`-46d`\] \[`-M` core\] \[`-N` system\] \[`-q` howmany\]

`netstat` `-s`

\[`--libxo`\] \[`-46sz`\] \[`-f` protocol\_family | `-p` protocol\] \[`-M` core\] \[`-N` system\]

`netstat` `-i` | [`-I`](#I_2) interface `-s`

\[`--libxo`\] \[`-46s`\] \[`-f` protocol\_family | `-p` protocol\] \[`-M` core\] \[`-N` system\]

`netstat` `-m`

\[`--libxo`\] \[`-M` core\] \[`-N` system\]

`netstat` `-B`

\[`--libxo`\] \[`-z`\] \[`-I` interface\]

`netstat` `-r`

\[`--libxo`\] \[`-46nW`\] \[`-F` fibnum\] \[`-f` address\_family\]

`netstat` `-rs`

\[`--libxo`\] \[`-s`\] \[`-M` core\] \[`-N` system\]

`netstat` `-g`

\[`--libxo`\] \[`-46W`\] \[`-f` address\_family\]

`netstat` `-gs`

\[`--libxo`\] \[`-46s`\] \[`-f` address\_family\] \[`-M` core\] \[`-N` system\]

`netstat` `-Q`

\[`--libxo`\]

[描述](#__u63CF___u8FF0_)
=======================

`netstat` 命令象征性地显示各种网络相关数据结构的内容。 有多种输出格式，具体取决于所提供信息的选项。

`netstat` \[`-46AaCLnRSTWx`\] \[`-f` protocol\_family | `-p` protocol\] \[`-M` core\] \[`-N` system\]

显示每个网络协议的活动套接字（协议控制块）列表。

活动套接字的默认显示显示本地和远程地址、发送和接收队列大小（以字节为单位）、协议和协议的内部状态。 如果套接字的地址指定了网络但没有特定的主机地址，则地址格式为 “host.port” 或 “network.port” 形式。 当已知时，主机和网络地址分别根据数据 hosts(5) 和 networks(5) 象征性地显示。 如果地址的符号名称未知，或者指定了 `-n` 选项，则根据地址族以数字形式打印地址。 有关 Internet IPv4 “dot format” 的更多信息，请参阅 inet(3) 。 未指定或 “wildcard” 的地址和端口显示为 “`*`” 。

[`--libxo`](#-libxo)

通过 libxo(3) 以不同的人类和机器可读格式生成输出。 有关命令行参数的详细信息，请参阅 xo\_parse\_args(3) 。

[`-4`](#4)

仅显示 IPv4。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6)

仅显示 IPv6。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-A`](#A)

显示与套接字关联的协议控制块 (PCB) 的地址；用于调试。

[`-a`](#a)

显示所有套接字的状态；通常不显示服务器进程使用的套接字。

[`-c`](#c)

显示每个会话使用的 TCP 堆栈。

[`-C`](#C)

显示 TCP 套接字的拥塞控制算法和诊断信息。

[`-L`](#L)

显示各种监听队列的大小。 第一个计数显示未接受的连接数，第二个计数显示未接受的不完整连接数，第三个计数是排队连接的最大数量。

[`-n`](#n)

不要将数字地址和端口号解析为名称。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-P`](#P)

显示每个套接字的日志 ID。

[`-R`](#R)

显示每个套接字的 flowid 和 flowtype。 flowid 是每个流的 32 位硬件特定标识符。 flowtype 定义了对哪些协议字段进行哈希处理以生成 id。 完整列表可在 sys/mbuf.h 中的 `M_HASHTYPE_*` 下找到。

[`-S`](#S)

将网络地址显示为数字（与 `-n` 一样），但以符号方式显示端口。

[`-T`](#T)

显示来自 TCP 控制块的诊断信息。 字段包括需要重传的数据包数量、无序接收的数据包数量以及宣传零大小窗口的数据包数量。

[`-W`](#W)

避免截断地址，即使这会导致某些字段溢出。

[`-x`](#x)

显示每个 Internet 套接字的套接字缓冲区和 TCP 计时器统计信息。

`-x` 标志使 `netstat` 输出有关存储在套接字缓冲区中的数据的所有记录信息。 这些字段是：

[`R-MBUF`](#R-MBUF)

接收队列中的 mbuf 数量。

[`S-MBUF`](#S-MBUF)

发送队列中的 mbuf 数量。

[`R-CLUS`](#R-CLUS)

接收队列中任何类型的簇数。

[`S-CLUS`](#S-CLUS)

发送队列中任何类型的集群数。

[`R-HIWA`](#R-HIWA)

接收缓冲区高水位标记，以字节为单位。

[`S-HIWA`](#S-HIWA)

发送缓冲区高水位标记，以字节为单位。

[`R-LOWA`](#R-LOWA)

接收缓冲区低水位标记，以字节为单位。

[`S-LOWA`](#S-LOWA)

发送缓冲区低水位标记，以字节为单位。

[`R-BCNT`](#R-BCNT)

接收缓冲区字节计数。

[`S-BCNT`](#S-BCNT)

发送缓冲区字节数。

[`R-BMAX`](#R-BMAX)

可以在接收缓冲区中使用的最大字节数。

[`S-BMAX`](#S-BMAX)

可以在发送缓冲区中使用的最大字节数。

[`rexmt`](#rexmt)

触发重传定时器的时间（以秒为单位），如果未设防，则为 0。

[`persist`](#persist)

触发 Retransmit Persistence 的时间（以秒为单位），如果未设防，则为 0。

[`keep`](#keep)

发射 Keep Alive 的时间（以秒为单位），如果未设防，则为 0。

[`2msl`](#2msl)

触发 2\*msl TIME\_WAIT 定时器的时间，以秒为单位，如果未设防，则为 0。

[`delack`](#delack)

触发延迟 ACK 定时器的时间，以秒为单位，如果未设防，则为 0。

[`rcvtime`](#rcvtime)

自收到最后一个数据包以来的时间，以秒为单位。

[`-f`](#f) protocol\_family

按 protocol\_family 过滤。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-p`](#p) protocol

按 protocol 过滤。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-M`](#M)

使用替代核心。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N)

使用替代内核映像。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-i` | `-I` interface \[`-46abdhnW`\] \[`-f` address\_family\] \[`-M` core\] \[`-N` system\]

显示已自动配置的所有网络接口或单个 interface 的状态（未显示静态配置到系统中但未在引导时定位的接口）。 接口名称后的星号 (“`*`”) 表示接口 “down” 。

当使用 `-i` (all interfaces) 或 `-I` interface 调用 `netstat` 时，它会提供有关传输的数据包、错误和冲突的累积统计信息表。 还会显示接口的网络地址和最大传输单元 (“mtu”) 。

[`-4`](#4_2)

仅显示 IPv4。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6_2)

仅显示 IPv6。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-a`](#a_2)

为每个以太网接口和每个 IP 接口地址显示当前使用的多播地址。 多播地址显示在与其关联的接口地址之后的单独行上。

[`-b`](#b)

显示输入和输出的字节数。

[`-d`](#d)

显示丢弃的数据包数。

[`-h`](#h)

以人类可读的形式打印所有计数器。

[`-n`](#n_2)

不要将数字地址和端口号解析为名称。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-W`](#W_2)

避免截断接口名称，即使这会导致某些字段溢出。 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-f`](#f_2) protocol\_family

按 protocol\_family 过滤。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-w` wait \[`-I` interface\] \[`-46d`\] \[`-M` core\] \[`-N` system\] \[`-q` howmany\]

每隔 wait 秒，在所有配置的网络接口或单个 interface 上显示有关数据包流量的信息。

当使用 `-w` 选项和 wait 间隔参数调用 `netstat` 时，它会显示与网络接口相关的统计信息的运行计数。 此选项的过时版本使用没有选项的数字参数，当前支持向后兼容。 默认情况下，此显示汇总所有接口的信息。 可以使用 `-I` interface 选项显示特定接口的信息。

[`-I`](#I_3) interface

仅显示有关 interface 的信息

[`-4`](#4_3)

仅显示 IPv4。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6_3)

仅显示 IPv6。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-d`](#d_2)

显示丢弃的数据包数。

[`-M`](#M_2)

使用替代核心。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_2)

使用替代内核映像。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-q`](#q)

输出 howmany 后退出。

`netstat` `-s` \[`-46sz`\] \[`-f` protocol\_family | `-p` protocol\] \[`-M` core\] \[`-N` system\]

显示每个网络协议的系统范围的统计信息。

[`-4`](#4_4)

仅显示 IPv4。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6_4)

仅显示 IPv6。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-s`](#s)

如果重复 `-s` ，则值为零的计数器将被抑制。

[`-z`](#z)

显示后重置统计计数器。

[`-f`](#f_3) protocol\_family

按 protocol\_family 过滤。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-p`](#p_2) protocol

按 protocol 过滤。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-M`](#M_3)

使用替代核心。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_3)

使用替代内核映像 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-i` | `-I` interface `-s` \[`-46s`\] \[`-f` protocol\_family | `-p` protocol\] \[`-M` core\] \[`-N` system\]

显示每个网络协议的每个接口统计信息。

[`-4`](#4_5)

仅显示 IPv4 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6_5)

仅显示 IPv6 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-s`](#s_2)

如果重复 `-s` ，则值为零的计数器将被抑制。

[`-f`](#f_4) protocol\_family

按 protocol\_family 过滤。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-p`](#p_3) protocol

按 protocol 过滤。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-M`](#M_4)

使用替代核心 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_4)

使用替代内核映像 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-m` \[`-M` core\] \[`-N` system\]

显示由内存管理例程 (mbuf(9)) 记录的统计信息。 网络管理一个私有的内存缓冲区池。

[`-M`](#M_5)

使用替代核心 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_5)

使用替代内核映像 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-B` \[`-z`\] \[`-I` interface\]

显示有关 bpf(4) 对等点的统计信息。 这包括 bpf 设备匹配、丢弃和接收的数据包数量等信息，以及有关当前缓冲区大小和设备状态的信息。

使用 `-B` 选项调用 `netstat` 时显示的 bpf(4) 标志表示 bpf 对等体的基础参数。 每个标志都表示为一个小写字母。 字母和标志之间按出现顺序的映射为：

[`p`](#p_4)

设置是否混杂收听

[`i`](#i)

[`BIOCIMMEDIATE`](#BIOCIMMEDIATE) 已在设备上设置

[`f`](#f_5)

[`BIOCGHDRCMPLT`](#BIOCGHDRCMPLT) 状态：正在自动填充源链接地址

[`s`](#s_3)

[`BIOCGSEESENT`](#BIOCGSEESENT) 状态：查看在接口上本地和远程发起的数据包。

[`a`](#a_3)

数据包接收产生一个信号

[`l`](#l)

[`BIOCLOCK`](#BIOCLOCK) 状态：描述符已被锁定

有关这些标志的更多信息，请参阅 bpf(4) 。

[`-z`](#z_2)

显示后重置统计计数器。

`netstat` `-r` \[`-46AnW`\] \[`-F` fibnum\] \[`-f` address\_family\] \[`-M` core\] \[`-N` system\]

显示路由表的内容。

当使用路由表选项 `-r` 调用 `netstat` 时，它会列出可用路由及其状态。 每条路由都包含一个目标主机或网络，以及一个用于转发数据包的网关。 flags 字段显示有关存储为二进制选择的路线的信息集合。 在 route(8) 和 route(4) 手册页中更详细地讨论了各个标志。 字母和标志之间的映射为：

[`1`](#1)

[`RTF_PROTO1`](#RTF_PROTO1)

协议特定路由标志#1

[`2`](#2)

[`RTF_PROTO2`](#RTF_PROTO2)

协议特定路由标志#2

[`3`](#3)

[`RTF_PROTO3`](#RTF_PROTO3)

协议特定路由标志#3

[`B`](#B)

[`RTF_BLACKHOLE`](#RTF_BLACKHOLE)

只丢弃 pkts（更新期间）

[`b`](#b_2)

[`RTF_BROADCAST`](#RTF_BROADCAST)

路由代表一个广播地址

[`D`](#D)

[`RTF_DYNAMIC`](#RTF_DYNAMIC)

动态创建（通过重定向）

[`G`](#G)

[`RTF_GATEWAY`](#RTF_GATEWAY)

目的地需要中介转发

[`H`](#H)

[`RTF_HOST`](#RTF_HOST)

主机条目（否则为净）

[`L`](#L_2)

[`RTF_LLINFO`](#RTF_LLINFO)

链接地址转换的有效协议

[`M`](#M_6)

[`RTF_MODIFIED`](#RTF_MODIFIED)

动态修改（通过重定向）

[`R`](#R_2)

[`RTF_REJECT`](#RTF_REJECT)

主机或网络不可达

[`S`](#S_2)

[`RTF_STATIC`](#RTF_STATIC)

手动添加

[`U`](#U)

[`RTF_UP`](#RTF_UP)

路由可用

[`X`](#X)

[`RTF_XRESOLVE`](#RTF_XRESOLVE)

外部守护进程将 proto 转换为链接地址

为连接到本地主机的每个接口创建直接路由；此类条目的网关字段显示传出接口的地址。 refcnt 字段给出了路由的当前活跃使用次数。 面向连接的协议通常在连接期间保持单个路由，而无连接协议在发送到同一目的地时获取路由。 使用字段提供使用该路由发送的数据包数量的计数。 接口条目指示用于路由的网络接口。

[`-4`](#4_6)

仅显示 IPv4。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6_6)

仅显示 IPv6。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-n`](#n_3)

不要将数字地址和端口号解析为名称。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-W`](#W_3)

显示每个路由的路径 MTU，并以更宽的字段大小打印接口名称。

[`-F`](#F)

显示编号为 fibnum 的路由表。 如果指定的 fibnum 为 -1 或未指定 `-F` ，则显示默认路由表。

[`-f`](#f_6)

显示特定 address\_family 的路由表。

[`-M`](#M_7)

使用替代核心，请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_6)

使用替代内核映像 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-rs` \[`-s`\] \[`-M` core\] \[`-N` system\]

显示路由统计信息。

[`-s`](#s_4)

如果重复 `-s` ，则值为零的计数器将被抑制。

[`-M`](#M_8)

使用替代核心 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_7)

使用替代内核映像，请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-g` \[`-46W`\] \[`-f` address\_family\] \[`-M` core\] \[`-N` system\]

显示组播虚拟接口表和组播转发缓存的内容。 这些表中的条目仅在内核主动转发多播会话时才会出现。 此选项仅适用于 `inet` 和 `inet6` 地址系列。

[`-4`](#4_7)

仅显示 IPv4 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6_7)

仅显示 IPv6 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-W`](#W_4)

避免截断地址，即使这会导致某些字段溢出。

[`-f`](#f_7) protocol\_family

按 protocol\_family 过滤。 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-M`](#M_9)

使用替代核心，请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_8)

使用替代内核映像，请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-gs` \[`-46s`\] \[`-f` address\_family\] \[`-M` core\] \[`-N` system\]

显示多播路由统计信息。

[`-4`](#4_8)

仅显示 IPv4 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-6`](#6_8)

仅显示 IPv6 请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-s`](#s_5)

如果重复 `-s` ，则值为零的计数器将被抑制。

[`-f`](#f_8) protocol\_family

按 protocol\_family 过滤。请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-M`](#M_10)

使用替代核心，请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

[`-N`](#N_9)

使用替代内核映像，请参阅 [一般选项](#__u4E00___u822C___u9009___u9879_) 。

`netstat` `-Q`

显示 netisr(9) 统计信息。 flags 字段显示可用的 ISR 处理程序：

[`C`](#C_2)

[`NETISR_SNP_FLAGS_M2CPUID`](#NETISR_SNP_FLAGS_M2CPUID)

能够将 mbuf 映射到 cpu id

[`D`](#D_2)

[`NETISR_SNP_FLAGS_DRAINEDCPU`](#NETISR_SNP_FLAGS_DRAINEDCPU)

有队列排空处理程序

[`F`](#F_2)

[`NETISR_SNP_FLAGS_M2FLOW`](#NETISR_SNP_FLAGS_M2FLOW)

能够将 mbuf 映射到流 id

[一般选项](#__u4E00___u822C___u9009___u9879_)
-----------------------------------------

一些选项具有一般含义：

[`-4`](#4_9)

是 `-f` inet 的简写 (仅显示 IPv4)

[`-6`](#6_9)

是 `-f` inet6 的简写 (仅显示 IPv6)

[`-f`](#f_9) address\_family, `-p` protocol

将显示限制为指定 address\_family 或单个 protocol 的那些记录。 识别以下地址系列和协议：

_Family_

_Protocols_

[`inet`](#inet) (`AF_INET`)

[`divert`](#divert), `icmp`, `igmp`, `ip`, `ipsec`, `pim, sctp`, `tcp`, `udp`

[`inet6`](#inet6) (`AF_INET6`)

[`icmp6`](#icmp6), `ip6`, `ipsec6`, `rip6`, `sctp`, `tcp`, `udp`

[`pfkey`](#pfkey) (`PF_KEY`)

[`pfkey`](#pfkey_2)

[`netgraph`](#netgraph), `ng` (`AF_NETGRAPH`)

[`ctrl`](#ctrl), `data`

[`unix`](#unix) (`AF_UNIX`)

[`link`](#link) (`AF_LINK`)

如果 protocol 未知或没有统计例程，程序将抱怨。

[`-M`](#M_11)

从指定的核心而不是默认的 /dev/kmem 中提取与名称列表关联的值。

[`-N`](#N_10)

从指定系统中提取名称列表，而不是从默认系统中引导的内核映像。

[`-n`](#n_4)

将网络地址和端口显示为数字。 通常 `netstat` 会尝试解析地址和端口，并象征性地显示它们。

[实例](#__u5B9E___u4F8B_)
=======================

显示接口 re0 的数据包流量信息（数据包、字节、错误、数据包丢失等），每 2 秒更新一次，并在 5 个输出后退出：

$ netstat -w 2 -q 5 -I re0 

在任何接口上显示 ICMP 的统计信息：

$ netstat -s -p icmp 

显示路由表：

$ netstat -r 

与上面相同，但不将数字地址和端口号解析为名称：

$ netstat -rn 

[参见](#__u53C2___u89C1_)
=======================

fstat(1), nfsstat(1), procstat(1), ps(1), sockstat(1), libxo(3), xo\_parse\_args(3), bpf(4), inet(4), route(4), unix(4), hosts(5), networks(5), protocols(5), services(5), iostat(8), route(8), trpt(8), vmstat(8), mbuf(9)

[历史](#__u5386___u53F2_)
=======================

`netstat` 命令出现在 4.2BSD 中。

WIDE/KAME 项目添加了 IPv6 支持。

[缺陷](#__u7F3A___u9677_)
=======================

错误的概念是不明确的。

September 25, 2020

FreeBSD 13.1-RELEASE