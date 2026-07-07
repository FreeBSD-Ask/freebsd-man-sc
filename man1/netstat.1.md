# netstat(1)

`netstat` — 显示网络状态和统计信息

## 名称

`netstat`

## 概要

`netstat [-j jail] [--libxo] [-46AaCLnPRSTWx] [-f protocol_family | -p protocol]`

`netstat -i | -I interface [-j jail] [--libxo] [-46abdhnW] [-f address_family] [-M core] [-N system]`

`netstat -w wait [-j jail] [--libxo] [-I interface] [-46d] [-M core] [-N system] [-q howmany]`

`netstat -s [-j jail] [--libxo] [-46sz] [-f protocol_family | -p protocol] [-M core] [-N system]`

`netstat -i | -I interface -s [-j jail] [--libxo] [-46s] [-f protocol_family | -p protocol] [-M core] [-N system]`

`netstat -m [-j jail] [--libxo] [-M core] [-N system]`

`netstat -B [-j jail] [--libxo] [-z] [-I interface]`

`netstat -r [-j jail] [--libxo] [-46nW] [-F fibnum] [-f address_family]`

`netstat -rs [-j jail] [--libxo] [-s] [-M core] [-N system]`

`netstat -g [-j jail] [--libxo] [-46W] [-F fibnum] [-f address_family]`

`netstat -gs [-j jail] [--libxo] [-46s] [-f address_family] [-M core] [-N system]`

`netstat -Q [-j jail]`

`netstat -o -4 | -6`

`netstat -O -4 | -6`

## 描述

`netstat` 命令显示各种网络相关数据结构的内容。传递的参数决定命令使用以下哪种输出格式。

`netstat` [`-46AaCLnRSTWx`] [`-f` `protocol_family` | `-p` `protocol`] [`-j` `jail`]

为每个网络协议显示活动套接字（协议控制块）列表。

活动套接字的默认显示包括本地和远程地址、发送和接收队列大小（字节）、协议以及协议的内部状态。如果套接字地址指定了网络但无特定主机地址，地址格式为 “host.port” 或 “network.port”。如果已知，主机和网络地址分别根据 [hosts(5)](../man5/hosts.5.md) 和 [networks(5)](../man5/networks.5.md) 数据库符号化显示。如果地址的符号名未知，或指定了 `-n` 选项，则根据地址族以数字形式打印地址。有关 Internet IPv4 “点分格式” 的更多信息，参见 [inet(3)](../man3/inet.3.md)。未指定的或 “通配” 地址和端口显示为 “`*`”。

- **`--libxo`** 通过 [libxo(3)](../man3/libxo.3.md) 以多种人类和机器可读格式生成输出。有关命令行参数的详细信息，参见 [xo_options(7)](../man7/xo_options.7.md)。
- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-A`** 显示与套接字关联的协议控制块（PCB）地址；用于调试。
- **`-a`** 显示所有套接字的状态；通常不显示服务器进程使用的套接字。
- **`-c`** 显示每个会话使用的 TCP 栈。
- **`-C`** 显示 TCP 套接字的拥塞控制算法和诊断信息。
- **`-L`** 显示各种监听队列的大小。第一个计数显示未接受连接数，第二个计数显示未接受的不完整连接数，第三个计数是排队的最大连接数。
- **`-n`** 不将数字地址和端口号解析为名称。参见通用选项。
- **`-P`** 显示每个套接字的日志 ID。
- **`-R`** 显示每个套接字的 flowid 和 flowtype。flowid 是每个流的 32 位硬件特定标识符。flowtype 定义哪些协议字段被哈希以生成 id。完整列表参见 **sys/mbuf.h** 中的 `M_HASHTYPE_*`。
- **`-S`** 将网络地址显示为数字（如同 `-n`）但以符号形式显示端口。
- **`-T`** 显示 TCP 控制块的诊断信息。字段包括需要重传的包数、乱序接收的包数以及通告零窗口的包数。
- **`-W`** 避免截断地址，即使这会导致某些字段溢出。
- **`-x`** 显示每个 Internet 套接字的套接字缓冲区和 TCP 定时器统计信息。

`-x` 标志使 `netstat` 输出有关套接字缓冲区中存储数据的所有记录信息。字段有：

| 字段 | 说明 |
| ---- | ---- |
| `R-HIWA` | 接收缓冲区高水位标记，字节。 |
| `S-HIWA` | 发送缓冲区高水位标记，字节。 |
| `R-LOWA` | 接收缓冲区低水位标记，字节。 |
| `S-LOWA` | 发送缓冲区低水位标记，字节。 |
| `R-BCNT` | 接收缓冲区字节计数。 |
| `S-BCNT` | 发送缓冲区字节计数。 |
| `R-BMAX` | 接收缓冲区可使用的最大字节数。 |
| `S-BMAX` | 发送缓冲区可使用的最大字节数。 |
| `rexmt` | 触发重传定时器的时间（秒），未启用则为 0。 |
| `persist` | 触发重传持久定时器的时间（秒），未启用则为 0。 |
| `keep` | 触发保活定时器的时间（秒），未启用则为 0。 |
| `2msl` | 触发 2*msl TIME_WAIT 定时器的时间（秒），未启用则为 0。 |
| `delack` | 触发延迟 ACK 定时器的时间（秒），未启用则为 0。 |
| `rcvtime` | 自上次接收数据包以来的时间（秒）。 |

- **`-f`** `protocol_family` 按 `protocol_family` 过滤。参见通用选项。
- **`-p`** `protocol` 按 `protocol` 过滤。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-i` | `-I` `interface` [`-46abdhnW`] [`-f` `address_family`] [`-M` `core`] [`-N` `system`] [`-j` `jail`]

显示所有网络接口或单个 `interface` 的状态，这些接口已自动配置（静态配置到系统中但引导时未定位的接口不显示）。接口名后的星号（“`*`”）表示该接口处于 “down” 状态。

当 `netstat` 以 `-i`（所有接口）或 `-I` `interface` 调用时，它提供有关传输的数据包、错误和冲突的累积统计信息表。还显示接口的网络地址和最大传输单元（“mtu”）。如果同时指定了 `-i` 和 `-I`，`-I` 覆盖任何 `-i` 实例。

- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-a`** 为每个以太网接口和每个 IP 接口地址显示当前正在使用的多播地址。多播地址显示在与它们关联的接口地址之后的单独行上。
- **`-b`** 显示进出字节数。
- **`-d`** 显示丢弃的输出数据包数。
- **`-h`** 以人类可读形式打印所有计数器。
- **`-n`** 不将数字地址和端口号解析为名称。参见通用选项。
- **`-W`** 避免截断地址，即使这会导致某些字段溢出。参见通用选项。但是，在大多数情况下字段宽度由 `-i` 选项自动确定，此选项效果甚微。
- **`-f`** `protocol_family` 按 `protocol_family` 过滤。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-w` `wait` [`-I` `interface`] [`-46d`] [`-M` `core`] [`-N` `system`] [`-q` `howmany`] [`-j` `jail`]

以 `wait` 秒为间隔，显示所有已配置网络接口或指定 `-I` 时的单个 `interface` 上有关数据包流量的信息。

此选项的一个过时版本使用不带选项的数字参数，目前为向后兼容而支持。

- **`-I`** `interface` 仅显示有关 `interface` 的信息。
- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-d`** 显示丢弃的输出数据包数。
- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-q`** 在 `howmany` 次输出后退出。值为零表示无限制，是默认值。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-o` `-4` | `-6`

打印与路由条目关联的下一跳（nhops）信息。与 `-4` 或 `-6` 一起使用时，分别将输出限制为 IPv4 或 IPv6 路由。此选项提供有关路由决策中使用的各个下一跳地址的详细信息。

`netstat` `-O` `-4` | `-6`

打印与路由条目关联的下一跳组（nhgrp）信息。与 `-4` 或 `-6` 一起使用时，分别将输出限制为 IPv4 或 IPv6 下一跳组。此选项显示用于多路径或负载均衡路由设置的分组下一跳条目。

`netstat` `-s` [`-46sz`] [`-f` `protocol_family` | `-p` `protocol`] [`-M` `core`] [`-N` `system`] [`-j` `jail`]

为每个网络协议显示系统范围的统计信息。

- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-s`** 如果重复 `-s`，则抑制值为零的计数器。
- **`-z`** 显示后重置统计计数器。
- **`-f`** `protocol_family` 按 `protocol_family` 过滤。参见通用选项。
- **`-p`** `protocol` 按 `protocol` 过滤。参见通用选项。
- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-i` | `-I` `interface` `-s` [`-46s`] [`-f` `protocol_family` | `-p` `protocol`] [`-M` `core`] [`-N` `system`] [`-j` `jail`]

为每个网络协议显示每个接口的统计信息。如果同时指定了 `-i` 和 `-I`，`-I` 覆盖任何 `-i` 实例。

- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-s`** 如果重复 `-s`，则抑制值为零的计数器。
- **`-f`** `protocol_family` 按 `protocol_family` 过滤。参见通用选项。
- **`-p`** `protocol` 按 `protocol` 过滤。参见通用选项。
- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-m` [`-M` `core`] [`-N` `system`] [`-j` `jail`]

显示内存管理例程（[mbuf(9)](../man9/mbuf.9.md)）记录的统计信息。网络管理一个私有内存缓冲池。

- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-B` [`-z`] [`-I` `interface`] [`-j` `jail`]

显示有关 [bpf(4)](../man4/bpf.4.md) 对等端的统计信息。包括有多少数据包被匹配、丢弃和被 bpf 设备接收等信息，以及当前缓冲区大小和设备状态信息。

`netstat` 以 `-B` 选项调用时显示的 [bpf(4)](../man4/bpf.4.md) 标志表示 bpf 对等端的基础参数。每个标志由单个小写字母表示。字母与标志之间的映射按出现顺序为：

| 字母 | 说明 |
| ---- | ---- |
| `p` | 以混杂模式监听时设置 |
| `i` | 设备上已设置 `BIOCIMMEDIATE` |
| `f` | `BIOCGHDRCMPLT` 状态：源链路地址正被自动填充 |
| `s` | `BIOCGSEESENT` 状态：查看接口上本地和远程发起的数据包 |
| `a` | 数据包接收会生成信号 |
| `l` | `BIOCLOCK` 状态：描述符已被锁定 |

有关这些标志的更多信息，请参见 [bpf(4)](../man4/bpf.4.md)。

- **`-z`** 显示后重置统计计数器。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-r` [`-46AnW`] [`-F` `fibnum`] [`-f` `address_family`] [`-M` `core`] [`-N` `system`] [`-j` `jail`]

显示路由表的内容。

当 `netstat` 以路由表选项 `-r` 调用时，它列出可用路由及其状态。每个路由由目标主机或网络和用于转发数据包的网关组成。flags 字段显示以二进制选择形式存储的有关路由的信息集合。各个标志在 [route(8)](../man8/route.8.md) 和 [route(4)](../man4/route.4.md) 手册页中更详细地讨论。字母与标志的映射为：

| 字母 | 标志 | 说明 |
| ---- | ---- | ---- |
| `1` | `RTF_PROTO1` | 协议特定路由标志 #1 |
| `2` | `RTF_PROTO2` | 协议特定路由标志 #2 |
| `3` | `RTF_PROTO3` | 协议特定路由标志 #3 |
| `B` | `RTF_BLACKHOLE` | 直接丢弃数据包（更新期间） |
| `b` | `RTF_BROADCAST` | 该路由表示广播地址 |
| `D` | `RTF_DYNAMIC` | 动态创建（由重定向） |
| `G` | `RTF_GATEWAY` | 目标需要中间者转发 |
| `H` | `RTF_HOST` | 主机条目（否则为网络） |
| `L` | `RTF_LLINFO` | 有效的协议到链路地址转换 |
| `M` | `RTF_MODIFIED` | 动态修改（由重定向） |
| `R` | `RTF_REJECT` | 主机或网络不可达 |
| `S` | `RTF_STATIC` | 手动添加 |
| `U` | `RTF_UP` | 路由可用 |
| `X` | `RTF_XRESOLVE` | 外部守护进程将协议转换为链路地址 |

为连接到本地主机的每个接口创建直接路由；此类条目的网关字段显示传出接口的地址。refcnt 字段给出路由的当前活动使用数。面向连接的协议通常在连接期间持有单个路由，而无连接协议在发送到同一目标时获取路由。use 字段提供使用该路由发送的数据包数计数。interface 条目指示用于该路由的网络接口。

- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-n`** 不将数字地址和端口号解析为名称。参见通用选项。
- **`-W`** 显示每个路由的度量和路径 MTU，并以更宽的字段大小打印接口名。
- **`-F`** 显示编号为 `fibnum` 的路由表。如果指定的 `fibnum` 为 -1 或未指定 `-F`，则显示默认路由表。
- **`-f`** 显示特定 `address_family` 的路由表。
- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-rs` [`-s`] [`-M` `core`] [`-N` `system`] [`-j` `jail`]

显示路由统计信息。

- **`-s`** 如果重复 `-s`，则抑制值为零的计数器。
- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-g` [`-46W`] [`-F` `fibnum`] [`-f` `address_family`] [`-M` `core`] [`-N` `system`] [`-j` `jail`]

显示多播虚拟接口表和多播转发缓存的内容。仅当内核主动转发多播会话时，这些表中的条目才会出现。此选项仅适用于 `inet` 和 `inet6` 地址族。

- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-W`** 避免截断地址，即使这会导致某些字段溢出。
- **`-F`** 显示编号为 `fibnum` 的路由表。如果指定的 `fibnum` 为 -1 或未指定 `-F`，则显示默认路由表。
- **`-f`** `protocol_family` 按 `protocol_family` 过滤。参见通用选项。
- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-gs` [`-46s`] [`-f` `address_family`] [`-M` `core`] [`-N` `system`] [`-j` `jail`]

显示多播路由统计信息。

- **`-4`** 仅显示 IPv4。参见通用选项。
- **`-6`** 仅显示 IPv6。参见通用选项。
- **`-s`** 如果重复 `-s`，则抑制值为零的计数器。
- **`-f`** `protocol_family` 按 `protocol_family` 过滤。参见通用选项。
- **`-M`** 使用替代核心转储。参见通用选项。
- **`-N`** 使用替代内核映像。参见通用选项。
- **`-j`** `jail` 在 jail 中运行。参见通用选项。

`netstat` `-Q` [`-j` `jail`]

显示 [netisr(9)](../man9/netisr.9.md) 统计信息。flags 字段显示可用的 ISR 处理程序：

| 字母 | 标志 | 说明 |
| ---- | ---- | ---- |
| `C` | `NETISR_SNP_FLAGS_M2CPUID` | 能将 mbuf 映射到 cpu id |
| `D` | `NETISR_SNP_FLAGS_DRAINEDCPU` | 有队列排空处理程序 |
| `F` | `NETISR_SNP_FLAGS_M2FLOW` | 能将 mbuf 映射到流 id |

- **`-j`** `jail` 在 jail 中运行。参见通用选项。

### 通用选项

某些选项具有通用含义：

**`-4`** 是 `-f` `inet` 的简写（仅显示 IPv4）。

**`-6`** 是 `-f` `inet6` 的简写（仅显示 IPv6）。

**`-f`** `address_family`, **`-p`** `protocol` 将显示限制为指定 `address_family` 或单个 `protocol` 的记录。识别以下地址族和协议：

| 族 | 协议 |
| -- | ---- |
| `inet` (`AF_INET`) | `divert`, `icmp`, `igmp`, `ip`, `ipsec`, `pim`, `sctp`, `tcp`, `udp` |
| `inet6` (`AF_INET6`) | `icmp6`, `ip6`, `ipsec6`, `rip6`, `sctp`, `tcp`, `udp` |
| `pfkey` (`PF_KEY`) | `pfkey` |
| `netgraph`, `ng` (`AF_NETGRAPH`) | `ctrl`, `data` |
| `unix` (`AF_UNIX`) | |
| `link` (`AF_LINK`) | |

如果 `protocol` 未知或没有针对它的统计例程，程序将报错。

**`-M`** 从指定的核心转储而非默认的 **/dev/kmem** 中提取与名称列表关联的值。

**`-N`** 从指定的系统而非默认的（系统引导时使用的内核映像）提取名称列表。

**`-n`** 将网络地址和端口显示为数字。通常 `netstat` 尝试解析地址和端口，并以符号形式显示它们。指定两次 `-n` 还将在显示路由表内容时禁止为默认 IPv4 和 IPv6 路由打印关键字 “`default`”。

**`-W`** 更宽的输出；扩展地址字段等以避免截断。非数字值（如域名）仍可能被截断；如有必要使用 `-n` 选项以避免歧义。

**`-j`** `jail` 在 `jail` 内执行操作。即使 `netstat` 二进制文件在 `jail` 中不可用，这允许访问网络状态。

## 实例

显示接口 re0 的数据包流量信息（数据包、字节、错误、数据包丢弃等），每 2 秒更新一次，5 次输出后退出：

```sh
netstat -w 2 -q 5 -I re0
```

显示任意接口上的 ICMP 统计信息：

```sh
netstat -s -p icmp
```

显示路由表：

```sh
netstat -r
```

同上，但不将数字地址和端口号解析为名称：

```sh
netstat -rn
```

显示 IPv4 监听套接字：

```sh
netstat -4l
```

## 参见

[fstat(1)](fstat.1.md), [nfsstat(1)](nfsstat.1.md), [procstat(1)](procstat.1.md), [ps(1)](ps.1.md), [sockstat(1)](sockstat.1.md), [libxo(3)](../man3/libxo.3.md), [xo_options(7)](../man7/xo_options.7.md), [bpf(4)](../man4/bpf.4.md), [inet(4)](../man4/inet.4.md), [route(4)](../man4/route.4.md), [unix(4)](../man4/unix.4.md), [hosts(5)](../man5/hosts.5.md), [networks(5)](../man5/networks.5.md), [protocols(5)](../man5/protocols.5.md), [services(5)](../man5/services.5.md), [iostat(8)](../man8/iostat.8.md), [route(8)](../man8/route.8.md), [vmstat(8)](../man8/vmstat.8.md), [mbuf(9)](../man9/mbuf.9.md)

## 历史

`netstat` 命令首次出现于 4.2BSD。

IPv6 支持由 WIDE/KAME 项目添加。

## 缺陷

错误的概念定义不明确。
