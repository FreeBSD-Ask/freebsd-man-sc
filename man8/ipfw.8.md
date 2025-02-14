  IPFW(8)  

IPFW(8)

FreeBSD System Manager's Manual

IPFW(8)

[名称](#__u540D___u79F0_)
=======================

`ipfw` —

防火墙、流量整形器、数据包调度器、内核内 NAT 的用户界面。

[概要](#__u6982___u8981_)
=======================

[防火墙配置](#__u9632___u706B___u5899___u914D___u7F6E_)
--------------------------------------------------

`ipfw` \[`-cq`\] `add` rule `ipfw` \[`-acdefnNStT`\] \[`set` N\] {`list` | `show`} \[rule | first-last ...\] `ipfw` \[`-f` | `-q`\] \[`set` N\] `flush` `ipfw` \[`-q`\] \[`set` N\] {`delete` | `zero` | `resetlog`} \[number ...\]

`ipfw` `set` \[`disable` number ...\] \[`enable` number ...\] `ipfw` `set move` \[`rule`\] number `to` number `ipfw` `set swap` number number `ipfw` `set show`

[SYSCTL 快捷键](#SYSCTL___u5FEB___u6377___u952E_)
----------------------------------------------

`ipfw` `enable` {`firewall` | `altq` | `one_pass` | `debug` | `verbose` | `dyn_keepalive`} `ipfw` `disable` {`firewall` | `altq` | `one_pass` | `debug` | `verbose` | `dyn_keepalive`}

[查找表](#__u67E5___u627E___u8868_)
--------------------------------

`ipfw` \[`set` N\] `table` name `create` create-options `ipfw` \[`set` N\] `table` {name | all} `destroy` `ipfw` \[`set` N\] `table` name `modify` modify-options `ipfw` \[`set` N\] `table` name `swap` name `ipfw` \[`set` N\] `table` name `add` table-key \[value\] `ipfw` \[`set` N\] `table` name `add` \[table-key value ...\] `ipfw` \[`set` N\] `table` name `atomic add` \[table-key value ...\] `ipfw` \[`set` N\] `table` name `delete` \[table-key ...\] `ipfw` \[`set` N\] `table` name `lookup` addr `ipfw` \[`set` N\] `table` name `lock` `ipfw` \[`set` N\] `table` name `unlock` `ipfw` \[`set` N\] `table` {name | all} `list` `ipfw` \[`set` N\] `table` {name | all} `info` `ipfw` \[`set` N\] `table` {name | all} `detail` `ipfw` \[`set` N\] `table` {name | all} `flush`

[DUMMYNET 配置（流量整形器和数据包调度器）](#DUMMYNET___u914D___u7F6E___uFF08___u6D41___u91CF___u6574___u5F62___u5668___u548C___u6570___u636E___u5305___u8C03___u5EA6___u5668___uFF09_)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

`ipfw` {`pipe` | `queue` | `sched`} number `config` config-options `ipfw` \[`-s` \[field\]\] {`pipe` | `queue` | `sched`} {`delete` | `list` | `show`} \[number ...\]

[IN-KERNEL NAT](#IN_KERNEL_NAT)
-------------------------------

`ipfw` \[`-q`\] `nat` number `config` config-options

[有状态的 IPv6/IPv4 网络地址和协议转换](#__u6709___u72B6___u6001___u7684__IPv6/IPv4___u7F51___u7EDC___u5730___u5740___u548C___u534F___u8BAE___u8F6C___u6362_)
------------------------------------------------------------------------------------------------------------------------------------------------

`ipfw` \[`set` N\] `nat64lsn` name `create` create-options `ipfw` \[`set` N\] `nat64lsn` name `config` config-options `ipfw` \[`set` N\] `nat64lsn` {name | all} {`list` | `show`} \[`states`\] `ipfw` \[`set` N\] `nat64lsn` {name | all} `destroy` `ipfw` \[`set` N\] `nat64lsn` name `stats` \[`reset`\]

[无状态 IPv6/IPv4 网络地址和协议转换](#__u65E0___u72B6___u6001__IPv6/IPv4___u7F51___u7EDC___u5730___u5740___u548C___u534F___u8BAE___u8F6C___u6362_)
---------------------------------------------------------------------------------------------------------------------------------------

`ipfw` \[`set` N\] `nat64stl` name `create` create-options `ipfw` \[`set` N\] `nat64stl` name `config` config-options `ipfw` \[`set` N\] `nat64stl` {name | all} {`list` | `show`} `ipfw` \[`set` N\] `nat64stl` {name | all} `destroy` `ipfw` \[`set` N\] `nat64stl` name `stats` \[`reset`\]

[XLAT464 CLAT IPv6/IPv4 网络地址和协议翻译](#XLAT464_CLAT_IPv6/IPv4___u7F51___u7EDC___u5730___u5740___u548C___u534F___u8BAE___u7FFB___u8BD1_)
------------------------------------------------------------------------------------------------------------------------------------

`ipfw` \[`set` N\] `nat64clat` name `create` create-options `ipfw` \[`set` N\] `nat64clat` name `config` config-options `ipfw` \[`set` N\] `nat64clat` {name | all} {`list` | `show`} `ipfw` \[`set` N\] `nat64clat` {name | all} `destroy` `ipfw` \[`set` N\] `nat64clat` name `stats` \[`reset`\]

[IPv6 到 IPv6 网络前缀转换](#IPv6___u5230__IPv6___u7F51___u7EDC___u524D___u7F00___u8F6C___u6362_)
------------------------------------------------------------------------------------------

`ipfw` \[`set` N\] `nptv6` name `create` create-options `ipfw` \[`set` N\] `nptv6` {name | all} {`list` | `show`} `ipfw` \[`set` N\] `nptv6` {name | all} `destroy` `ipfw` \[`set` N\] `nptv6` name `stats` \[`reset`\]

[内部诊断](#__u5185___u90E8___u8BCA___u65AD_)
-----------------------------------------

`ipfw` `internal iflist` `ipfw` `internal talist` `ipfw` `internal vlist`

[规则清单和预处理](#__u89C4___u5219___u6E05___u5355___u548C___u9884___u5904___u7406_)
-----------------------------------------------------------------------------

`ipfw` \[`-cfnNqS`\] \[`-p` preproc \[preproc-flags\]\] pathname

[描述](#__u63CF___u8FF0_)
=======================

`ipfw` 实用程序是用于控制 ipfw(4) 防火墙、 dummynet(4) 流量整形器/数据包调度器和内核内 NAT 服务的用户界面。

防火墙配置或 _ruleset_ 由编号从 1 到 65535 的 _rules_ 列表组成。 数据包从协议栈中的多个不同位置传递到防火墙（取决于数据包的源和目的地，防火墙可能会在同一个数据包上被多次调用）。 将传递到防火墙的数据包与 _ruleset_ 中的每个规则进行比较，按照规则编号顺序（允许多个具有相同编号的规则，在这种情况下，它们按插入顺序进行处理）。 当找到匹配时，执行匹配规则对应的动作。

根据操作和某些系统设置，数据包可以在匹配后以某种规则重新注入防火墙以进行进一步处理。

一个规则集总是包含一个不能修改或删除的 _default_ 规则（编号为 65535），它匹配所有的数据包。 与 _default_ 规则关联的操作可以是 `deny` 或 `allow` ，具体取决于内核的配置方式。

如果规则集包含一个或多个带有 `keep-state`, `record-state`, `limit` 或 `set-limit` 选项的规则，防火墙将具有 _stateful_ 行为，即在匹配时它将创建 _dynamic rules_ 即匹配数据包的规则与导致它们创建的数据包具有相同的 5 元组（协议、源和目标地址和端口）。 具有有限生命周期的动态规则在第一次出现 `check-state`, `keep-state` 或 `limit` 规则时进行检查，通常仅用于按需打开防火墙以访问合法流量。 请注意， `keep-state` 和 `limit` 意味着所有数据包的隐式 `check-state` （不仅是与规则匹配的数据包），但 `record-state` 和 `set-limit` 没有隐式 `check-state` 。 有关 `ipfw` 的状态行为的更多信息，请参阅下面的 [状态防火墙](#__u72B6___u6001___u9632___u706B___u5899_) 和 [实例](#__u5B9E___u4F8B_) 部分。

所有规则（包括动态规则）都有一些相关的计数器：数据包计数、字节计数、日志计数和指示上次匹配时间的时间戳。 可以使用 `ipfw` 命令显示或重置计数器。

每个规则都属于 32 个不同的 _sets_ 之一，并且有 `ipfw` 命令可以原子地操作集合，例如启用、禁用、交换集合、将集合中的所有规则移动到另一个集合中、删除集合中的所有规则。 这些对于安装临时配置或测试它们很有用。 有关 _sets_ 的更多信息，请参阅 [规则集](#__u89C4___u5219___u96C6_) 部分。

可以使用 `add` 命令添加规则；使用 `delete` 命令单独或成组删除，使用 `flush` 命令全局删除（第 31 组除外）；使用 `show` 和 `list` 命令显示，可选地与计数器的内容一起显示。 最后，可以使用 `zero` 和 `resetlog` 命令重置计数器。

[命令选项](#__u547D___u4EE4___u9009___u9879_)
-----------------------------------------

调用 `ipfw` 时可以使用以下常规选项：

[`-a`](#a)

列出规则时显示计数器值。 `show` 命令暗示了这个选项。

[`-b`](#b)

只显示动作和评论，而不是规则的主体。 暗示 `-c` 。

[`-c`](#c)

输入或显示规则时，以紧凑的形式打印它们，即，当 "ip from any to any" 字符串不携带任何附加信息时，省略。

[`-d`](#d)

列出时，除静态规则外，还显示动态规则。

[`-D`](#D)

列出时，仅显示动态状态。 删除时，只删除动态状态。

[`-f`](#f)

运行时不提示确认误用可能导致问题的命令，即 `flush` 。 如果没有与进程关联的 tty，则这是隐含的。 带有此标志的 `delete` 命令忽略可能的错误，即不存在的规则编号。 对于批处理命令，下一个命令继续执行。

[`-i`](#i)

列出表时（有关 [查找表的](#__u67E5___u627E___u8868___u7684_) 的更多信息，请参阅下面的查找表部分），将值格式化为 IP 地址。 默认情况下，值显示为整数。

[`-n`](#n)

仅检查命令字符串的语法，而不将它们实际传递给内核。

[`-N`](#N)

尝试解析输出中的地址和服务名称。

[`-q`](#q)

执行 `add`, `nat`, `zero`, `resetlog` 或 `flush` 命令时保持安静；（暗示 `-f` ）。 这在通过在脚本中执行多个 `ipfw` 命令（例如， ‘`sh /etc/rc.firewall`’ ）或通过在远程登录会话中处理具有许多 `ipfw` 规则的文件来更新规则集时很有用。 如果条目已经存在或不存在，它还会阻止表添加或删除失败。

这个选项可能很重要的原因是，对于其中一些操作， `ipfw` 可能会打印一条消息；如果该操作导致阻止到远程客户端的流量，则远程登录会话将被关闭并且规则集的其余部分将不会被处理。 然后需要访问控制台才能恢复。

[`-S`](#S)

列出规则时，显示每个规则所属的 _set_ 。 如果未指定此标志，则不会列出禁用的规则。

[`-s`](#s) \[field\]

列出管道时，根据四个计数器之一（总或当前数据包或字节）进行排序。

[`-t`](#t)

列出时，显示使用 `ctime`() 转换的最后匹配时间戳。

[`-T`](#T)

列出时，将上次匹配时间戳显示为从纪元开始的秒数。 这种形式可以更方便地通过脚本进行后期处理。

[规则清单和预处理](#__u89C4___u5219___u6E05___u5355___u548C___u9884___u5904___u7406__2)
-------------------------------------------------------------------------------

为了简化配置，可以将规则放入使用 `ipfw` 处理的文件中，如最后概要行所示。 必须使用绝对 pathname 。 该文件将被逐行读取并作为参数应用到 `ipfw` 实用程序。

可选地，可以使用 `-p` preproc 指定预处理器，其中要通过管道传输 pathname 。 有用的预处理器包括 cpp(1) 和 m4(1) 。 如果 preproc 不以斜杠 (‘`/`’) 作为其第一个字符开始，则执行通常的 `PATH` 名称搜索。 在运行 `ipfw` 时（例如，当它们通过 NFS 安装时）尚未安装所有文件系统的环境中，应注意这一点。 一旦指定了 `-p` ，任何额外的参数都会传递给预处理器进行解释。 这允许灵活的配置文件（例如根据本地主机名对它们进行条件化）并使用宏来集中经常需要的参数，例如 IP 地址。

[流量整形配置](#__u6D41___u91CF___u6574___u5F62___u914D___u7F6E_)
-----------------------------------------------------------

`ipfw` `pipe`, `queue` 和 `sched` 命令用于配置流量整形器和数据包调度器。 有关详细信息，请参阅下面的 [TRAFFIC SHAPER (DUMMYNET) CONFIGURATION](#TRAFFIC_SHAPER_(DUMMYNET)_CONFIGURATION) 配置部分。

如果世界和内核不同步， `ipfw` ABI 可能会中断，从而阻止您添加任何规则。 这会对引导过程产生不利影响。 您可以使用 `ipfw` `disable` `firewall` 临时禁用防火墙以重新访问网络，从而解决问题。

[包流](#__u5305___u6D41_)
=======================

在多个 sysctl 变量的控制下，在协议栈的多个位置根据活动规则集检查数据包。 这些地方和变量如下所示，重要的是要记住这张图片，以便设计正确的规则集。

 ^ to upper layers V | | +----------->-----------+ ^ V \[ip(6)\_input\] \[ip(6)\_output\] net.inet(6).ip(6).fw.enable=1 | | ^ V \[ether\_demux\] \[ether\_output\_frame\] net.link.ether.ipfw=1 | | +-->--\[bdg\_forward\]-->--+ net.link.bridge.ipfw=1 ^ V | to devices | 

同一数据包通过防火墙的次数可以在 0 到 4 之间变化，具体取决于数据包源和目标以及系统配置。

请注意，当数据包流经堆栈时，标头可以被剥离或添加到其中，因此它们可能会或可能不会被检查。 例如，当从 `ether_demux()` 调用 `ipfw` 时，传入的数据包将包含 MAC 标头，但是当从 `ip_input()` 或 `ip6_input()` 调用 `ipfw` 时，相同的数据包将剥离 MAC 标头。

另请注意，始终根据完整的规则集检查每个数据包，而与检查发生的位置或数据包的来源无关。 如果规则包含一些对调用位置无效的匹配模式或操作（例如，尝试匹配 `ip_input` 或 `ip6_input` 中的 MAC 标头），则匹配模式将不匹配，但此类模式前面的 `not` 运算符 _will_ 导致在这些数据包上 _always_ 匹配的模式。 因此，如有必要，程序员有责任编写合适的规则集来区分可能的位置。 `skipto` 规则在这里很有用，例如：

\# packets from ether\_demux or bdg\_forward ipfw add 10 skipto 1000 all from any to any layer2 in # packets from ip\_input ipfw add 10 skipto 2000 all from any to any not layer2 in # packets from ip\_output ipfw add 10 skipto 3000 all from any to any not layer2 out # packets from ether\_output\_frame ipfw add 10 skipto 4000 all from any to any layer2 out 

（是的，目前无法区分 ether\_demux 和 bdg\_forward）。

另请注意，只有动作 `allow`, `deny`, `netgraph`, `ngtee` 以及与 `dummynet` 相关的动作才会针对 `layer2` 帧进行处理，而所有其他动作都如同 `allow` 此类帧一样。 仅对没有 `layer2` 标头的 IP 数据包支持全套操作。 例如， `divert` 动作不会转移 `layer2` 帧。

[语法](#__u8BED___u6CD5_)
=======================

通常，每个关键字或参数必须作为单独的命令行参数提供，没有前导或尾随空格。 关键字区分大小写，而参数可能区分大小写，也可能不区分大小写，具体取决于它们的性质（例如，uid 是，主机名不是）。

一些参数（例如，端口或地址列表）是逗号分隔的值列表。在这种情况下，允许逗号“，”后的空格使该行更具可读性。 您还可以将整个命令（包括标志）放入单个参数中。例如，以下形式是等价的：

ipfw -q add deny src-ip 10.0.0.0/24,127.0.0.1/8 ipfw -q add deny src-ip 10.0.0.0/24, 127.0.0.1/8 ipfw "-q add deny src-ip 10.0.0.0/24, 127.0.0.1/8" 

[规则格式](#__u89C4___u5219___u683C___u5F0F_)
=========================================

防火墙规则的格式如下：

\[rule\_number\] \[`set` set\_number\] \[`prob` match\_probability\] action \[`log` \[`logamount` number\]\] \[`altq` queue\] \[{`tag` | `untag`} number\] body

其中规则的主体指定了哪些信息用于过滤数据包，其中包括：

Layer-2 header fields

当可用的

IPv4 and IPv6 Protocol

SCTP, TCP, UDP, ICMP, etc.

Source and dest. addresses and ports

Direction

参见 [数据包流](#__u6570___u636E___u5305___u6D41_) 部分

Transmit and receive interface

按姓名或地址

Misc. IP header fields

版本、服务类型、数据报长度、标识、碎片标志、生存时间

IP options

IPv6 Extension headers

分段、逐跳选项、路由标头、源路由 rthdr0、移动 IPv6 rthdr2、IPSec 选项。

IPv6 Flow-ID

Misc. TCP header fields

TCP 标志（SYN、FIN、ACK、RST 等）、序列号、确认号、窗口

TCP options

ICMP types

对于 ICMP 数据包

ICMP6 types

对于 ICMP6 数据包

User/group ID

当数据包可以与本地套接字关联时。

Divert status

数据包是否来自转移套接字（例如， natd(8) ）。

Fib annotation state

数据包是否已标记为在未来的转发决策中使用特定的 FIB（路由表）。

请注意，上述某些信息（例如源 MAC 或 IP 地址和 TCP/UDP 端口）很容易被欺骗，因此仅对这些字段进行过滤可能无法保证获得所需的结果。

rule\_number

每个规则都与 1..65535 范围内的 rule\_number 相关联，后者为 _default_ 规则保留。 规则按规则编号顺序检查。多个规则可以有相同的编号，在这种情况下，它们会根据添加的顺序进行检查（并列出）。 如果在没有指定数字的情况下输入规则，内核将分配一个，使得该规则成为 _default_ 规则之前的最后一个。 自动规则编号是通过将最后一个非默认规则编号增加 sysctl 变量 net.inet.ip.fw.autoinc\_step 的值来分配的，该变量默认为 100。 如果这是不可能的（例如，因为我们会超出允许的最大规则编号），则使用最后一个非默认值的编号。

[`set`](#set) set\_number

每个规则都与 0..31 范围内的 set\_number 相关联。 集合可以单独禁用和启用，因此此参数对于原子规则集操作至关重要。 它还可用于简化规则组的删除。 如果输入规则时未指定集合编号，则将使用集合 0。-
Set 31 的特殊之处在于它不能被禁用，并且 set 31 中的规则不会被 `ipfw flush` 命令删除（但您可以使用 `ipfw delete set 31` 命令删除它们）。 Set 31 也用于 _default_ 规则。

[`prob`](#prob) match\_probability

仅以指定的概率（0 到 1 之间的浮点数）声明匹配。 这对于许多应用程序很有用，例如随机数据包丢弃或（与 `dummynet`) 一起）模拟导致无序数据包传递的多条路径的影响。

注意：在任何其他条件之前检查此条件，包括可能有副作用的 `keep-state` 或 `check-state` 。

[`log`](#log) \[`logamount` number\]

使用 `log` 关键字匹配规则的数据包将以两种方式用于记录：如果 sysctl 变量 net.inet.ip.fw.verbose 设置为 0（默认），则可以使用附加到 `ipfw0` 的 bpf(4) 伪接口。 可以在系统启动后使用以下命令手动创建此伪接口：

\# ifconfig ipfw0 create 

或者，在引导时通过将以下行添加到 rc.conf(5) 文件中自动：

firewall\_logif="YES" 

当没有 bpf(4) 附加到伪接口时，开销为零。

如果 net.inet.ip.fw.verbose 置为 1，则数据包将使用 `LOG_SECURITY` 工具记录到 syslogd(8) ，最多为 `logamount` 数据包。 如果未指定 `logamount` ，则从 sysctl 变量 net.inet.ip.fw.verbose\_limit 获取限制。 在这两种情况下，值 0 表示无限日志记录。

达到限制后，可以通过清除该条目的日志记录计数器或数据包计数器来重新启用日志记录，请参阅 `resetlog` 命令。

注意：在成功验证所有其他数据包匹配条件之后，并且在对数据包执行最终操作（接受、拒绝等）之前进行记录。

[`tag`](#tag) number

当一个数据包匹配带有 `tag` 关键字的规则时，1..65534 范围内给定 number 的数字标签将附加到数据包上。 标签充当内部标记（它不会通过线路发送），可用于稍后识别这些数据包。 例如，这可用于提供接口之间的信任并开始进行基于策略的过滤。 一个数据包可以同时有多个标签。 标签是 "sticky" ，这意味着一旦通过匹配规则将标签应用于数据包，它就会一直存在，直到明确删除。 标签在内核中随数据包随处保存，但在数据包离开内核时丢失，例如，在将数据包传输到网络或将数据包发送到 divert(4) 套接字时。

要检查以前应用的标记，请使用 `tagged` 规则选项。 要删除以前应用的标签，请使用 `untag` 关键字。

注意：由于标签在内核空间的任何地方都与数据包一起保存，它们可以在内核网络子系统的任何地方设置和取消设置（使用 mbuf\_tags(9) 工具），而不仅仅是通过 ipfw(4) `tag` 和 `untag` 关键字。 例如，可以有一个专门的 netgraph(4) 节点进行流量分析和标记，以便以后在防火墙中进行检查。

[`untag`](#untag) number

当一个数据包匹配带有 `untag` 关键字的规则时，将在附加到该数据包的标签中搜索带有编号 number 的标签，如果找到，则从中删除。 绑定到数据包的其他标签（如果存在）保持不变。

[`altq`](#altq) queue

当数据包与 `altq` 关键字匹配规则时，将附加给定 queue 的 ALTQ 标识符（请参阅 altq(4) ）。 请注意，此 ALTQ 标记仅对 "out" IPFW 的数据包有意义，不会被拒绝或转移套接字。 请注意，如果在处理数据包时内存不足，则不会对其进行标记，因此明智的做法是将您的 ALTQ 设置为 "default" 队列策略帐户。 如果多个 `altq` 规则匹配单个数据包，则只有第一个添加 ALTQ 分类标记。 这样做时，可以通过在规则集中早期使用 `count` `altq` queue 规则进行分类，然后应用过滤决策来塑造流量。 例如， `check-state` 和 `keep-state` 规则可能会在稍后出现，并提供实际过滤决策以及备用 ALTQ 标记。

您必须运行 pfctl(8) 来设置队列，然后 IPFW 才能按名称查找它们，如果重新排列 ALTQ 规则，内核中包含队列标识符的规则可能已经过时，需要被重新加载。 陈旧的队列标识符可能会导致错误分类。

所有系统 ALTQ 处理都可以通过 `ipfw` `enable` altq 和 `ipfw` `disable` altq 打开或关闭。 net.inet.ip.fw.one\_pass 的使用与 ALTQ 流量整形无关，因为在添加 ALTQ 标记后始终遵循实际的规则操作。

[规则行动](#__u89C4___u5219___u884C___u52A8_)
-----------------------------------------

规则可以与以下操作之一相关联，这些操作将在数据包与规则正文匹配时执行。

[`allow`](#allow) | [`accept`](#accept) | [`pass`](#pass) | [`permit`](#permit)

允许匹配规则的数据包。 搜索终止。

[`check-state`](#check-state) \[:flowname | `:any`\]

根据动态规则集检查数据包。 如果找到匹配项，则执行与生成此动态规则的规则相关联的操作，否则转到下一个规则。-
`Check-state` 规则没有正文。 如果没有找到 `check-state` 规则，则在第一个 `keep-state` 或 `limit` 规则处检查动态规则集。 :flowname 是由 `keep-state` 操作码分配给动态规则的符号名称。 特殊的 flowname `:any` 可用于在匹配时忽略状态 flowname。 `:default` 关键字是用于与旧规则集兼容的特殊名称。

[`count`](#count)

更新所有匹配规则的数据包的计数器。 搜索继续下一条规则。

[`deny`](#deny) | [`drop`](#drop)

丢弃符合此规则的数据包。搜索终止。

[`divert`](#divert) port

将匹配此规则的数据包转移到绑定到 port 的 divert(4) 套接字。 搜索终止。

[`fwd`](#fwd) | [`forward`](#forward) ipaddr | tablearg\[,port\]

将匹配数据包的下一跳更改为 ipaddr 它可以是 IP 地址或主机名。 下一跳也可以通过使用 `tablearg` 关键字而不是显式地址来查找数据包的最后一个表提供。 如果此规则匹配，则搜索终止。

如果 ipaddr 是本地地址，那么匹配的数据包将被转发到本地机器上的 port （或数据包中的端口号，如果规则中未指定端口号）。-
如果 ipaddr 不是本地地址，则忽略端口号（如果指定），并且数据包将使用在该 IP 的本地路由表中找到的路由转发到远程地址。-
fwd 规则将不匹配第 2 层数据包（在 ether\_input、ether\_output 或桥接上接收的数据包）。-
`fwd` 操作根本不会更改数据包的内容。 特别是，目标地址保持不变，因此转发到另一个系统的数据包通常会被该系统拒绝，除非该系统上有匹配的规则来捕获它们。 对于本地转发的数据包，套接字的本地地址将设置为数据包的原始目标地址。 这使得 netstat(1) 条目看起来很奇怪，但它是用于透明代理服务器的。

[`nat`](#nat) nat\_nr | tablearg

将数据包传递给 nat 实例（用于网络地址转换、地址重定向等）：有关详细信息，请参阅 [网络地址转换 (NAT)](#__u7F51___u7EDC___u5730___u5740___u8F6C___u6362__(NAT)) 部分。

[`nat64lsn`](#nat64lsn) name

将数据包传递给有状态的 NAT64 实例（用于 IPv6/IPv4 网络地址和协议转换）：有关详细信息，请参阅 [IPv6/IPv4 网络地址和协议转换](#IPv6/IPv4___u7F51___u7EDC___u5730___u5740___u548C___u534F___u8BAE___u8F6C___u6362_) 部分。

[`nat64stl`](#nat64stl) name

将数据包传递给无状态的 NAT64 实例（用于 IPv6/IPv4 网络地址和协议转换）：有关详细信息，请参阅 [IPv6/IPv4 网络地址和协议转换](#IPv6/IPv4___u7F51___u7EDC___u5730___u5740___u548C___u534F___u8BAE___u8F6C___u6362_) 部分。

[`nat64clat`](#nat64clat) name

将数据包传递给 CLAT NAT64 实例（用于客户端 IPv6/IPv4 网络地址和协议转换）：有关详细信息，请参阅 [IPv6/IPv4 网络地址和协议转换](#IPv6/IPv4___u7F51___u7EDC___u5730___u5740___u548C___u534F___u8BAE___u8F6C___u6362_) 部分。

[`nptv6`](#nptv6) name

将数据包传递到 NPTv6 实例（用于 IPv6 到 IPv6 网络前缀转换）：有关详细信息，请参阅 [IPv6-to-IPv6 NETWORK PREFIX TRANSLATION (NPTv6)](#IPv6-to_IPv6_NETWORK_PREFIX_TRANSLATION_(NPTv6)) 部分。

[`pipe`](#pipe) pipe\_nr

将数据包传递到 `dummynet` “pipe” （用于带宽限制、延迟等）。 有关详细信息，请参阅 [TRAFFIC SHAPER (DUMMYNET) 配置](#TRAFFIC_SHAPER_(DUMMYNET)___u914D___u7F6E_) 部分。 搜索终止；但是，从管道退出时，如果未设置 sysctl(8) 变量 net.inet.ip.fw.one\_pass ，则从下一条规则开始，数据包将再次传递给防火墙代码。

[`queue`](#queue) queue\_nr

将数据包传递到 `dummynet` “queue” （使用 WF2Q+ 进行带宽限制）。

[`reject`](#reject)

（已弃用）。 `unreach host` 的同义词。

[`reset`](#reset)

丢弃符合此规则的数据包，如果数据包是 TCP 数据包，则尝试发送 TCP 重置 (RST) 通知。 搜索终止。

[`reset6`](#reset6)

丢弃符合此规则的数据包，如果数据包是 TCP 数据包，则尝试发送 TCP 重置 (RST) 通知。 搜索终止。

[`skipto`](#skipto) number | tablearg

跳过编号小于 number 的所有后续规则。 搜索以第一个编号 number 或更高编号的规则继续。 可以将 `tablearg` 关键字与 skipto 一起用于 _computed_ 的 skipto。 Skipto 可以在 O(log(N)) 或 O(1) 中工作，具体取决于内存量和/或 sysctl 变量。 有关详细信息，请参阅 [SYSCTL 变量](#SYSCTL___u53D8___u91CF_) 部分。

[`call`](#call) number | tablearg

当前规则编号保存在内部堆栈中，并且规则集处理继续使用第一个编号 number 或更高编号的规则。 如果稍后遇到具有 `return` 操作的规则，则处理返回到此 `call` 规则的编号加一或更高的第一个规则（与在 `divert` 操作后从 divert(4) 套接字返回的数据包相同的行为）。 这可以用于对规则进行类似于汇编语言的 “subroutine” 调用，并对不同的接口等进行通用检查。

可以调用任何数字的规则，而不仅仅是像 `skipto` 那样的向前跳转。 因此，为了防止出现错误时出现无限循环， `call` 和 `return` 操作都不会进行任何跳转，如果无法分配内存或堆栈溢出/下溢，则只需转到下一条规则。

规则编号的内部堆栈是使用 mbuf\_tags(9) 工具实现的，当前大小为 16 个条目。 由于 mbuf 标记在数据包离开内核时丢失，因此不应在子程序中使用 `divert` 以避免无限循环和其他不良影响。

[`return`](#return)

将最后一次 `call` 操作保存到内部堆栈的规则编号取回，并将规则集处理返回给编号大于相应 `call` 规则编号的第一个规则。 有关更多详细信息，请参阅 `call` 操作的描述。

请注意， `return` 规则通常结束一个 “subroutine” ，因此是无条件的，但 `ipfw` 命令行实用程序当前要求除 `check-state` 之外的每个操作都具有正文。 虽然有时只返回某些数据包很有用，但通常您只想打印 “return” 以提高可读性。 解决方法是使用新语法和 `-c` 开关：

\# Add a rule without actual body ipfw add 2999 return via any # List rules without "from any to any" part ipfw -c list 

这种外观上的烦恼可能会在未来的版本中得到修复。

[`tee`](#tee) port

将匹配此规则的数据包副本发送到绑定到端口 port 的 divert(4) 套接字。 搜索继续下一条规则。

[`unreach`](#unreach) code

丢弃符合此规则的数据包，并尝试发送带有代码 code 的 ICMP 不可达通知，其中 code 是从 0 到 255 的数字，或以下别名之一： `net`, `host`, `protocol`, `port`, `needfrag`, `srcfail`, `net-unknown`, `host-unknown`, `isolated`, `net-prohib`, `host-prohib`, `tosnet`, `toshost`, `filter-prohib`, `host-precedence` 或 `precedence-cutoff` 。 搜索终止。

[`unreach6`](#unreach6) code

丢弃符合此规则的数据包，并尝试发送带有代码 code 的 ICMPv6 不可达通知，其中 code 是 0、1、3 或 4 中的数字，或以下别名之一： `no-route, admin-prohib, address` 或 `port` 。搜索终止。

[`netgraph`](#netgraph) cookie

使用给定的 cookie. 将数据包转移到网络图。 搜索终止。 如果稍后从 netgraph 返回数据包，则它要么被接受，要么继续下一条规则，具体取决于 net.inet.ip.fw.one\_pass 变量。

[`ngtee`](#ngtee) cookie

数据包的副本被转移到网络图，原始数据包继续下一条规则。 有关 `netgraph` 和 `ngtee` 操作的更多信息，请参阅 ng\_ipfw(4) 。

[`setfib`](#setfib) fibnum | tablearg

数据包被标记以便在任何后续转发决策中使用 FIB（路由表） fibnum 。 在当前实现中，这仅限于值 0 到 15，请参见 setfib(2) 。 处理在下一条规则处继续。 可以将 `tablearg` 关键字与 setfib 一起使用。 如果 tablearg 值不在 fibs 的编译范围内，则数据包的 fib 设置为 0。

[`setdscp`](#setdscp) DSCP | number | tablearg

为 IPv4/IPv6 数据包设置指定的 DiffServ 代码点。 处理在下一条规则处继续。支持的值是：

`cs0` (`000000`), `cs1` (`001000`), `cs2` (`010000`), `cs3` (`011000`), `cs4` (`100000`), `cs5` (`101000`), `cs6` (`110000`), `cs7` (`111000`), `af11` (`001010`), `af12` (`001100`), `af13` (`001110`), `af21` (`010010`), `af22` (`010100`), `af23` (`010110`), `af31` (`011010`), `af32` (`011100`), `af33` (`011110`), `af41` (`100010`), `af42` (`100100`), `af43` (`100110`), `ef` (`101110`), `be` (`000000`). 此外，DSCP 值可以通过数字 (0..63) 指定。 也可以将 `tablearg` 关键字与 setdscp 一起使用。 如果 tablearg 值不在 0..63 范围内，则使用所提供值的低 6 位。

[`tcp-setmss`](#tcp-setmss) mss

将 TCP 段中的最大段大小 (MSS) 设置为值 mss 。 内核模块 `ipfw_pmod` 应该被加载或者内核应该有 `options IPFIREWALL_PMOD` 才能使用这个动作。 如果原始 MSS 值低于指定值，此命令不会更改数据包。 支持 IPv4 上的 TCP 和 IPv6 上的 TCP。 无论 `tcp-setmss` 规则是否匹配数据包，搜索都会继续下一条规则。

[`reass`](#reass)

排队并重新组装 IPv4 片段。 如果数据包没有分段，则更新计数器并继续处理下一个规则。 如果数据包是最后一个逻辑片段，则重新组装数据包，如果 net.inet.ip.fw.one\_pass 设置为 0，则继续处理下一个规则。 否则，允许数据包通过并且搜索终止。 如果数据包是一组逻辑片段中间的一个片段，它会被消耗并立即停止处理。

可以通过 net.inet.ip.maxfragpackets 和 net.inet.ip.maxfragsperpacket 调整片段处理，它们分别限制可处理片段的最大数量（默认值：800）和每个数据包的最大片段数（默认值：16）。

NOTA BENE: 由于片段不包含端口号，因此应使用 `reass` 规则避免它们。 或者，可以使用基于方向（如 `in` / `out` ) 和基于源（如 `via` ) 的匹配模式来选择片段。

通常是一个简单的规则，例如：

\# reassemble incoming fragments ipfw add reass all from any to any in 

是您在规则集开始时所需要的。

[`abort`](#abort)

丢弃符合此规则的数据包，如果数据包是 SCTP 数据包，则尝试发送包含 ABORT 块的 SCTP 数据包。 搜索终止。

[`abort6`](#abort6)

丢弃符合此规则的数据包，如果数据包是 SCTP 数据包，则尝试发送包含 ABORT 块的 SCTP 数据包。 搜索终止。

[规则体](#__u89C4___u5219___u4F53_)
--------------------------------

规则的主体包含零个或多个模式（例如特定的源和目标地址或端口、协议选项、传入或传出接口等） 数据包必须匹配才能被识别。 通常，模式由（隐式） `and` 运算符连接 -- 即，所有模式都必须匹配才能使规则匹配。单个模式可以用 `not` 运算符作为前缀来反转匹配的结果，如

`ipfw add 100 allow ip from not 1.2.3.4 to any`

此外，可以通过将模式放在括号 ( ) 或大括号 { } 之间的列表中并使用 `or` 运算符来构造一组替代匹配模式 (_or-blocks_) ，如下所示：

`ipfw add 100 allow ip from { x or not y or z } to any`

只允许使用一级括号。 请注意，大多数 shell 对圆括号或大括号都有特殊含义，因此建议在它们前面放置一个反斜杠 \\ 以防止这种解释。

规则的主体通常必须包括源地址和目标地址说明符。 关键字 any 可以在不同的地方使用，以指定必填字段的内容是不相关的。

规则正文具有以下格式：

\[proto `from` src `to` dst\] \[options\]

第一部分（从 src 到 dst 的 proto）是为了向后兼容早期版本的 FreeBSD 。 在现代 FreeBSD 中，任何匹配模式（包括 MAC 头、IP 协议、地址和端口）都可以在 options 部分中指定。

规则字段具有以下含义：

proto: protocol | [`{`](#_) protocol `or ... }`

protocol: \[`not`\] protocol-name | protocol-number

由编号或名称指定的 IP 协议（完整列表参见 /etc/protocols), 或以下关键字之一：

[`ip4`](#ip4) | [`ipv4`](#ipv4)

匹配 IPv4 数据包。

[`ip6`](#ip6) | [`ipv6`](#ipv6)

匹配 IPv6 数据包。

[`ip`](#ip) | [`all`](#all)

匹配任何数据包。

`proto` 选项中的 `ipv6` 将被视为内部协议。 而且， `ipv4` 在 `proto` 选项中不可用。

`{` protocol `or ... }` 格式（ _or-block_) 仅为了方便而提供，但它的使用已被弃用。

src and dst: {`addr` | `{` addr `or ... }`} \[\[`not`\] ports\]

地址（或列表，见下文）可选地后跟 ports 说明符。

第二种格式（具有多个地址的 _or-block_ ）仅为了方便而提供，不鼓励使用。

addr: \[`not`\] {`any` | `me` | `me6` | `table`(name\[,value\]) | addr-list | addr-set}

[`any`](#any)

匹配任何 IP 地址。

[`me`](#me)

匹配系统中接口上配置的任何 IP 地址。

[`me6`](#me6)

匹配系统中接口上配置的任何 IPv6 地址。在分析数据包时评估地址列表。

[`table`](#table)(name\[,value\])

匹配查找表 number 中存在条目的任何 IPv4 或 IPv6 地址。 如果还指定了可选的 32 位无符号 value ，则只有具有该值的条目才会匹配。 有关 [LOOKUP TABLES](#LOOKUP_TABLES) 的更多信息，请参阅下面的查找表部分。

addr-list: ip-addr\[,addr-list\]

ip-addr:

以下列方式之一指定的主机或子网地址：

numeric-ip | hostname

匹配单个 IPv4 地址，指定为 dotted-quad 或主机名。 在将规则添加到防火墙列表时解析主机名。

addr/masklen

将所有地址与基本 addr （指定为 IP 地址、网络号或主机名）和 `masklen` 位的掩码宽度匹配。 例如， 1.2.3.4/25 或 1.2.3.0/25 将匹配从 1.2.3.0 到 1.2.3.127 的所有 IP 号码。

addr:mask

匹配所有带有基 addr （指定为 IP 地址、网络号或主机名）和 mask 的掩码（指定为点分四边形）的地址。 例如，1.2.3.4:255.0.255.0 或 1.0.3.0:255.0.255.0 将匹配 1.\*.3.\*。 此表格仅适用于非连续口罩。 对于连续掩码，最好使用 addr/masklen 格式，这样更紧凑，更不容易出错。

addr-set: addr\[/masklen\]`{`list`}`

list: {num | num-num}\[,list\]

匹配所有带有基地址 addr 的地址（指定为 IP 地址、网络号或主机名）并且其最后一个字节在大括号 { } 之间的列表中。 请注意，大括号和数字之间不能有空格（允许逗号后有空格）。 列表的元素可以指定为单个条目或范围。 masklen 字段用于限制地址集的大小，可以是 24 到 32 之间的任何值。 如果未指定，则假定为 24。-
这种格式对于处理单个规则中的稀疏地址集特别有用。 因为匹配是使用位掩码进行的，所以它需要恒定的时间并大大降低了规则集的复杂性。-
例如，指定为 1.2.3.4/24{128,35-55,89} 或 1.2.3.0/24{128,35-55,89} 的地址将匹配以下 IP 地址：-
1.2.3.128, 1.2.3.35 到 1.2.3.55, 1.2.3.89 。

addr6-list: ip6-addr\[,addr6-list\]

ip6-addr:

主机或子网指定以下方式之一：

numeric-ip | hostname

匹配 inet\_pton(3) 允许的单个 IPv6 地址或主机名。 在将规则添加到防火墙列表时解析主机名。

addr/masklen

将所有 IPv6 地址与基本 addr （由 inet\_pton(3) 或主机名指定）和 `masklen` 位的掩码宽度匹配。

addr/mask

将所有 IPv6 地址与基本 addr （由 inet\_pton(3) 或主机名指定）和 mask 掩码（由 inet\_pton(3). 指定）匹配。 例如，fe::640:0:0/ffff::ffff:ffff:0:0 将匹配 fe:\*:\*:\*:0:640:\*:\*。 此表格仅适用于非连续口罩。 对于连续掩码，最好使用 addr/masklen 格式，这样更紧凑，更不容易出错。

不提供对 IPv6 地址集的支持，因为 IPv6 地址通常在初始前缀之后是随机的。

ports: {port | port\-port}\[,ports\]

对于支持端口号的协议（如 SCTP、TCP 和 UDP），可选 `ports` 可以指定为一个或多个端口或端口范围，用逗号分隔但不能有空格，可选的 `not` 运算符。 ‘`-`’ 符号指定了一个端口范围（包括边界）。

可以使用服务名称（来自 /etc/services) 代替数字端口值。 端口列表的长度限制为 30 个端口或范围，但可以通过在规则的 `options` 部分中使用 _or-block_ 来指定更大的范围。

反斜杠 (‘`\`’) 可用于转义服务名称中的破折号 (‘`-`’) 字符（在 shell 中，必须键入两次反斜杠以避免 shell 本身将其解释为转义字符）。

`ipfw add count tcp from any ftp\\-data-ftp to any`

具有非零偏移（即，不是第一个片段）的分段数据包永远不会匹配具有一个或多个端口规范的规则。 有关匹配分段数据包的详细信息，请参阅 `frag` 选项。

[规则选项（匹配模式）](#__u89C4___u5219___u9009___u9879___uFF08___u5339___u914D___u6A21___u5F0F___uFF09_)
-----------------------------------------------------------------------------------------------

这些所谓的 _options_ 中的零个或多个可以出现在规则中，可选地以 `not` 操作数作为前缀，并且可能分组到 _or-blocks_ 中。

可以使用以下匹配模式（按字母顺序列出）：

[`// this is a comment`](#//_this_is_a_comment).

在规则中插入指定文本作为注释。 // 后面的所有内容都被视为注释并存储在规则中。 您可以拥有仅评论规则，这些规则被列为具有评论后跟 `count` 操作的规则。

[`bridged`](#bridged)

[`layer2`](#layer2) 的别名。

[`defer-immediate-action`](#defer-immediate-action) | [`defer-action`](#defer-action)

带有此选项的规则不会在匹配时执行正常操作。 此选项旨在与 `record-state` 或 `keep-state` 一起使用，因为在匹配时创建但被忽略的动态规则将按预期工作。 具有 `record-state` 和 `defer-immediate-action` 的规则创建一个动态规则并继续下一个规则，而不实际执行该规则的操作部分。 当稍后通过状态表激活该规则时，将照常执行该操作。

[`diverted`](#diverted)

仅匹配由转移套接字生成的数据包。

[`diverted-loopback`](#diverted-loopback)

仅将来自转移套接字的数据包匹配回 IP 堆栈输入以进行传递。

[`diverted-output`](#diverted-output)

仅匹配从转移套接字返回到 IP 堆栈输出以进行传递的数据包。

[`dst-ip`](#dst-ip) ip-address

匹配目标 IP 是作为参数指定的地址之一的 IPv4 数据包。

{`dst-ip6` | `dst-ipv6`} ip6-address

匹配目标 IP 是作为参数指定的地址之一的 IPv6 数据包。

[`dst-port`](#dst-port) ports

匹配目标端口是作为参数指定的端口之一的 IP 数据包。

[`established`](#established)

匹配设置了 RST 或 ACK 位的 TCP 数据包。

[`ext6hdr`](#ext6hdr) header

匹配包含 header 给出的扩展头的 IPv6 数据包。 支持的标头是：

分段, (`frag`), Hop-to-hop 选项 (`hopopt`), 任何类型的路由标头 (`route`), 源路由路由标头类型 0 (`rthdr0`), 移动 IPv6 路由标头类型 2 (`rthdr2`), 目的地选项 (`dstopt`), IPSec 身份验证标头 (`ah`), IPsec 封装的安全负载标头 (`esp`) 。

[`fib`](#fib) fibnum

匹配已标记为使用给定 FIB（路由表）编号的数据包。

[`flow`](#flow) table(name\[,value\])

在查找表 name 中搜索流条目。 如果未找到，则匹配失败。 否则，匹配成功并且 `tablearg` 设置为从表中提取的值。

此选项可用于根据某些数据包字段快速调度流量。 有关查找表的更多信息，请参阅下面的 [查找表](#__u67E5___u627E___u8868_) 部分。

[`flow-id`](#flow-id) labels

匹配包含 labels 中给出的任何流标签的 IPv6 数据包。 labels 是数字流标签的逗号分隔列表。

[`frag`](#frag) spec

匹配 `ip_off` 字段包含在 spec 中指定的 IPv4 分片选项的逗号分隔列表的 IPv4 数据包。 公认的选项是： `df` (`不分片`), `mf` (`更多分片`), `rf` (`保留分片位`) `偏移量` (`非零分片偏移量`) 。 缺少特定选项可以用 ‘`!`’ 表示。

空选项列表默认匹配非零片段偏移。 这样的规则将匹配不是所有的第一个分片数据报，包括 IPv4 和 IPv6。 这是与旧规则集的向后兼容性。

[`gid`](#gid) group

匹配 group 发送或接收的所有 TCP 或 UDP 数据包。 可以按名称或编号指定 group 。

[`jail`](#jail) jail

匹配 ID 或名称为 jail 的 jail 发送或接收的所有 TCP 或 UDP 数据包。

[`icmptypes`](#icmptypes) types

匹配 ICMP 类型在列表 types 中的 ICMP 数据包。 该列表可以指定为以逗号分隔的各个类型（数字）的任意组合。 _范围是不允许的。_ 支持的 ICMP 类型有：

echo 回复 (`0`), 目标不可达 (`3`), 源淬火 (`4`), 重定向 (`5`), echo request (`8`), 路由器通告 (`9`), 路由器请求 (`10`), 超过生存时间 (`11`), IP头坏 (`12`), 时间戳请求 (`13`), 时间戳回复 (`14`), 信息请求 (`15`), 信息回复 (`16`), 地址掩码请求 (`17`) 和地址掩码回复 (`18`) 。

[`icmp6types`](#icmp6types) types

匹配 ICMP6 类型在 types 列表中的 ICMP6 数据包。 该列表可以指定为以逗号分隔的各个类型（数字）的任意组合。 _范围是不允许的。_

[`in`](#in) | [`out`](#out)

分别匹配传入或传出的数据包。 `in` 和 `out` 是互斥的（实际上 `out` 是作为 `not in`实现的）。

[`ipid`](#ipid) id-list

匹配 `ip_id` 字段的值包含在 id-list 中的 IPv4 数据包，id-list 可以是单个值，也可以是与 ports 相同的值或范围指定的列表。

[`iplen`](#iplen) len-list

匹配总长度（包括标头和数据）在 set len-list 中的 IP 数据包，该列表可以是单个值，也可以是与 ports 相同的值或范围的列表。

[`ipoptions`](#ipoptions) spec

匹配 IPv4 标头包含 spec 中指定的逗号分隔选项列表的数据包。 支持的 IP 选项有：

`ssrr` (严格源路由), `lsrr` (松散源路由), `rr` (记录包路由) 和 `ts` (时间戳)。 缺少特定选项可以用 ‘`!`’ 表示。

[`ipprecedence`](#ipprecedence) precedence

匹配优先级字段等于 precedence 的 IPv4 数据包。

[`ipsec`](#ipsec)

匹配具有与其关联的 IPSEC 历史记录的数据包（即，数据包封装在 IPSEC 中，内核支持 IPSEC，并且可以正确解封装）

请注意，指定 `ipsec` 与指定 `proto` ipsec 不同，因为后者只会查看特定的 IP 协议字段，而与 IPSEC 内核支持和 IPSEC 数据的有效性无关。

进一步注意，在没有 IPSEC 支持的内核中，该标志会被静默忽略。 给定时它不会影响规则处理，并且规则的处理就像没有 `ipsec` 标志一样。

[`iptos`](#iptos) spec

匹配其 `tos` 字段包含在 spec 中指定的逗号分隔的服务类型列表的 IPv4 数据包。 支持的 IP 服务类型有：

`低延迟` (`IPTOS_LOWDELAY`), `吞吐量` (`IPTOS_THROUGHPUT`), `可靠性` (`IPTOS_RELIABILITY`), `最小成本` (`IPTOS_MINCOST`), `拥塞` (`IPTOS_ECN_CE`) 。 缺少特定类型可以用 ‘`!`’ 表示。

[`dscp spec`](#dscp_spec)\[,spec\]

匹配其 `DS` 字段值包含在 spec 掩码中的 IPv4/IPv6 数据包。 可以通过逗号分隔的列表指定多个值。 值可以是 `setdscp` 操作中使用的关键字之一，也可以是精确数字。

[`ipttl`](#ipttl) ttl-list

匹配生存时间包含在 ttl-list 中的 IPv4 数据包，该列表可以是单个值，也可以是值或范围的列表，其指定方式与 ports 相同。

[`ipversion`](#ipversion) ver

匹配 IP 版本字段为 ver 的 IP 数据包。

[`keep-state`](#keep-state) \[:flowname\]

匹配后，防火墙将创建一个动态规则，其默认行为是使用相同的协议匹配源和目标 IP/端口之间的双向流量。 该规则有一个有限的生命周期（由一组 sysctl(8) 变量控制），并且每次找到匹配的数据包时都会刷新生命周期。 :flowname 用于为动态规则分配额外的地址、端口和协议参数。 它可以通过 `check-state` 规则用于更准确的匹配。 `:default` 关键字是用于与旧规则集兼容的特殊名称。

[`layer2`](#layer2_2)

仅匹配第 2 层数据包，即从 `ether_demux`() 和 `ether_output_frame`() 传递到 `ipfw` 的数据包。

[`limit`](#limit) {`src-addr` | `src-port` | `dst-addr` | `dst-port`} N \[:flowname\]

防火墙将只允许 N 个与规则中指定的参数集相同的连接。 可以指定一个或多个源和目标地址和端口。

[`lookup`](#lookup) {`dst-ip` | `dst-port` | `src-ip` | `src-port` | `uid` | `jail`} name

在查找表 name 中搜索与指定为参数的字段匹配的条目。 如果未找到，则匹配失败。 否则，匹配成功并且 `tablearg` 设置为从表中提取的值。

此选项可用于根据某些数据包字段快速调度流量。 有关查找表的更多信息，请参阅下面的 [查找表](#__u67E5___u627E___u8868_) 部分。

[`{ MAC`](#__MAC) | [`mac }`](#mac__) dst-mac src-mac

匹配具有给定 dst-mac 和 src-mac 地址的数据包，指定为 `any` 关键字（匹配任何 MAC 地址），或由冒号分隔的六组十六进制数字，并且可选地后跟指示有效位的掩码。 可以使用以下任一方法指定掩码：

1.  斜杠 (/) 后跟有效位数。 例如，具有 33 个有效位的地址可以指定为：
    
    `MAC 10:20:30:40:50:60/33 any`
    
2.  与号 (&) 后跟一个位掩码，指定为六组由冒号分隔的十六进制数字。 例如，最后 16 位有效的地址可以指定为：
    
    `MAC 10:20:30:40:50:60&00:00:00:00:ff:ff any`
    
    请注意，& 字符在许多 shell 中具有特殊含义，通常应该被转义。
    

请注意，MAC 地址的顺序（目标第一，源第二）与网络上的顺序相同，但与用于 IP 地址的顺序相反。

[`mac-type`](#mac-type) mac-type

匹配以太网类型字段对应于作为参数指定的那些之一的数据包。 mac-type 的指定方式与 `port numbers` 相同（即，一个或多个逗号分隔的单个值或范围）。 您可以为已知值使用符号名称，例如 _vlan_, _ipv4, ipv6_ 。 值可以输入为十进制或十六进制（如果以 0x 为前缀），并且它们始终以十六进制打印（除非使用 `-N` 选项，在这种情况下将尝试符号解析）。

[`proto`](#proto) protocol

将数据包与相应的 IP 协议匹配。

[`record-state`](#record-state)

匹配后，防火墙将创建一个动态规则，就像指定了 `keep-state` 一样。 但是，与 `keep-state` 相比，此选项并不意味着隐式 `check-state` 。

[`recv`](#recv) | [`xmit`](#xmit) | [`via`](#via) {ifX | if`*` | table(name\[,value\]) | ipno | any}

分别匹配由确切名称 (ifX) 、设备名称 (if\*) 、IP 地址或通过某个接口指定的接口接收、传输或通过的数据包。 表 name 可以通过其内核 ifindex 来匹配接口。 有关查找表的更多信息，请参阅下面的 [查找表](#__u67E5___u627E___u8868_) 部分。

`via` 关键字使接口始终被检查。 如果使用 `recv` 或 `xmit` 而不是 `via` ，则仅检查接收或发送接口（分别）。 通过指定两者，可以根据接收和发送接口匹配数据包，例如：

`ipfw add deny ip from any to any out recv ed0 xmit ed1`

`recv` 接口可以在传入或传出数据包上测试，而 `xmit` 接口只能在传出数据包上测试。 因此，无论何时使用 `xmit` ，都需要 `out` （并且 `in` 无效）。

数据包可能没有接收或传输接口：来自本地主机的数据包没有接收接口，而发往本地主机的数据包没有传输接口。

[`set-limit`](#set-limit) {`src-addr` | `src-port` | `dst-addr` | `dst-port`} N

像 `limit` 一样工作，但没有附加隐式 `check-state` 。

[`setup`](#setup)

匹配设置了 SYN 位但没有 ACK 位的 TCP 数据包。 这是 “`tcpflags syn,!ack`” 的缩写形式。

[`sockarg`](#sockarg)

匹配与本地套接字关联并且 SO\_USER\_COOKIE 套接字选项已设置为非零值的数据包。 作为副作用，该选项的值可用作 `tablearg` 值，而该值又可用作 `skipto` 或 `pipe` 编号。

[`src-ip`](#src-ip) ip-address

匹配源 IP 是作为参数指定的地址之一的 IPv4 数据包。

[`src-ip6`](#src-ip6) ip6-address

匹配源 IP 是作为参数指定的地址之一的 IPv6 数据包。

[`src-port`](#src-port) ports

匹配源端口是作为参数指定的端口之一的 IP 数据包。

[`tagged`](#tagged) tag-list

匹配其标签包含在 tag-list 中的数据包，标签列表可以是单个值，也可以是值或范围的列表，指定方式与 ports 相同。 可以使用 `tag` 规则操作参数将标记应用于数据包（有关标记的详细信息，请参见它的描述）。

[`tcpack`](#tcpack) ack

仅限 TCP 数据包。 如果 TCP 头确认号字段设置为 ack ，则匹配。

[`tcpdatalen`](#tcpdatalen) tcpdatalen-list

匹配 TCP 数据长度为 tcpdatalen-list 的 TCP 数据包，该数据包可以是单个值，也可以是值或范围的列表，指定方式与 ports 相同。

[`tcpflags`](#tcpflags) spec

仅限 TCP 数据包。 如果 TCP 标头包含 spec 中指定的逗号分隔的标志列表，则匹配。 支持的 TCP 标志是：

`fin`, `syn`, `rst`, `psh`, `ack` 和 `urg` 。缺少特定标志可以用 ‘`!`’ 表示。 包含 `tcpflags` 规范的规则永远不会匹配具有非零偏移量的分段数据包。 有关匹配分段数据包的详细信息，请参阅 `frag` 选项。

[`tcpmss`](#tcpmss) tcpmss-list

匹配 MSS（最大段大小）值设置为 tcpmss-list 的 TCP 数据包，该列表可以是单个值，也可以是值或范围的列表，其指定方式与 ports 相同。

[`tcpseq`](#tcpseq) seq

仅限 TCP 数据包。 如果 TCP 标头序列号字段设置为 seq ，则匹配。

[`tcpwin`](#tcpwin) tcpwin-list

匹配标头窗口字段设置为 tcpwin-list 的 TCP 数据包，该列表可以是单个值，也可以是值或范围的列表，其指定方式与 ports 相同。

[`tcpoptions`](#tcpoptions) spec

仅限 TCP 数据包。 如果 TCP 标头包含 spec 中指定的逗号分隔的选项列表，则匹配。 支持的 TCP 选项有：

`mss` (大段大小), `window` (tcp 窗口通告), `sack` (选择性 ack), `ts` (rfc1323 时间戳) 和 `cc` (rfc1644 t/tcp 连接数)。 缺少特定选项可以用 ‘`!`’ 表示。

[`uid`](#uid) user

匹配 user 户发送或接收的所有 TCP 或 UDP 数据包。 user 可以通过姓名或标识号进行匹配。

[`verrevpath`](#verrevpath)

对于传入的数据包，会在数据包的源地址上进行路由表查找。 如果数据包进入系统的接口与路由的出接口匹配，则数据包匹配。 如果接口不匹配，则数据包不匹配。 所有传出数据包或没有传入接口的数据包都匹配。

该选项的名称和功能有意类似于 Cisco IOS 命令：

`ip verify unicast reverse-path`

此选项可用于制定反欺骗规则以拒绝源地址不是来自该接口的所有数据包。 另请参阅选项 `antispoof` 。

[`versrcreach`](#versrcreach)

对于传入的数据包，会在数据包的源地址上进行路由表查找。 如果存在到源地址的路由，但不存在默认路由或黑洞/拒绝路由，则数据包匹配。 否则，数据包不匹配。 所有传出数据包匹配。

该选项的名称和功能有意类似于 Cisco IOS 命令：

`ip verify unicast source reachable-via any`

此选项可用于制定反欺骗规则以拒绝所有源地址不可达的数据包。

[`antispoof`](#antispoof)

对于传入的数据包，检查数据包的源地址是否属于直接连接的网络。 如果网络是直接连接的，则将数据包进入的接口与网络连接的接口进行比较。 当入接口和直连接口不相同时，报文不匹配。 否则，数据包匹配。 所有传出数据包匹配。

此选项可用于制定反欺骗规则，以拒绝所有假装来自直接连接的网络但不通过该接口进入的数据包。 此选项与 `verrevpath` 相似但比 verrevpath 更受限制，因为它仅处理具有直接连接网络的源地址的数据包，而不是所有源地址。

[查找表](#__u67E5___u627E___u8868__2)
==================================

查找表对于处理大型稀疏地址集或其他搜索键（例如，端口、 jail  ID、接口名称）很有用。 在本节的其余部分，我们将使用术语 \`\`key''。 表名需要符合以下规范： table-name 。 可以在不同的 sets 中创建具有相同名称的表。 但是，默认情况下，规则链接到 set 0 中的表。 此行为可以由 net.inet.ip.fw.tables\_sets 变量控制。 有关详细信息，请参阅 [规则集](#__u89C4___u5219___u96C6_) 部分。 最多可能有 65535 个不同的查找表。

支持以下表格类型：

table-type: addr | iface | number | flow

table-key: addr\[/masklen\] | iface-name | number | flow-spec

flow-spec: flow-field\[,flow-spec\]

flow-field: src-ip | proto | src-port | dst-ip | dst-port

[`addr`](#addr)

匹配 IPv4 或 IPv6 地址。 每个条目由一个 addr\[/masklen\] 表示，并将匹配所有带有基本 addr （指定为 IPv4/IPv6 地址或主机名）和 masklen 位的掩码宽度的地址。 如果未指定 masklen ，则默认为 IPv4 的 32 和 IPv6 的 128。 在表中查找 IP 地址时，将匹配最具体的条目。

[`iface`](#iface)

匹配接口名称。 每个条目都由被视为接口名称的字符串表示。 不支持通配符。

[`number`](#number)

匹配协议端口、uids/gids 或 jail ID。 每个条目由 32 位无符号整数表示。不支持范围。

[`flow`](#flow_2)

将 flow 类型子选项指定的数据包字段与表项匹配。

表需要在使用前通过 `create` 显式创建。

支持以下创建选项：

create-options: create-option | create-options

create-option: `type` table-type | [`valtype`](#valtype) value-mask | [`algo`](#algo) algo-desc |

[`limit`](#limit_2) number | [`locked`](#locked) | [`missing`](#missing) | [`or-flush`](#or-flush)

[`type`](#type)

表键类型。

[`valtype`](#valtype_2)

表值掩码。

[`algo`](#algo_2)

要使用的表算法（见下文）。

[`limit`](#limit_3)

可以插入到表中的最大项目数。

[`locked`](#locked_2)

限制任何表修改。

[`missing`](#missing_2)

如果表已经存在并且具有与新表完全相同的选项，则不要失败。

[`or-flush`](#or-flush_2)

刷新具有相同名称的现有表，而不是返回错误。 意味着 `missing` ，因此现有表必须与新表兼容。

其中一些选项可以稍后通过 `modify` 关键字进行修改。可以更改以下选项：

modify-options: modify-option | modify-options

modify-option: `limit` number

[`limit`](#limit_4)

更改可以插入表中的最大项目数。

此外，可以使用 `lock` 或 `unlock` 命令锁定或解锁表。

相同 type 的表可以使用 `swap` name 命令相互交换。 如果设置了表限制并且数据交换会导致限制命中，则交换可能会失败。 操作以原子方式执行。

可以使用 `add` 命令一次将一个或多个条目添加到表中。 所有项目的添加都是原子执行的。 默认情况下，添加一个条目的错误不会影响其他条目的添加。 但是，在这种情况下会返回非零错误代码。 可以在 `add` 之前指定特殊的 `atomic` 关键字以指示全或无添加请求。

可以使用 `delete` 命令一次从表中删除一个或多个条目。 默认情况下，删除一个条目的错误不会影响其他条目的删除。 但是，在这种情况下会返回非零错误代码。

可以使用 `lookup` table-key 命令检查在特定 table-key 上可以找到哪些条目。 此功能是可选的，在某些算法中可能不受支持。

可以对 one 或 `all` 表执行以下操作：

[`list`](#list)

列出所有条目。

[`flush`](#flush)

删除所有条目。

[`info`](#info)

显示通用表信息

[`detail`](#detail)

显示通用表格信息和特定于算法的数据。

支持以下查找算法：

algo-desc: algo-name | algo-name algo-data

algo-name: addr: radix | addr: hash | iface: array | number: array | flow: hash

[`addr: radix`](#addr:_radix)

IPv4 和 IPv6 的单独基数树，与路由表相同（参见 route(4) ）。 addr 类型的默认选择。

[`addr:hash`](#addr:hash)

分离 IPv4 和 IPv6 的自动增长哈希。接受最初通过 `addr:hash masks=/v4,/v6` 算法创建选项指定的具有相同掩码长度的条目。 默认情况下假设 /32 和 /128 掩码。 搜索从提供的地址中删除主机位（根据掩码），并检查生成的密钥是否具有适当的哈希值。 主要针对 /64 和字节范围的 IPv6 掩码进行了优化。

[`iface:array`](#iface:array)

存储系统中出现的条目的排序索引的数组。 针对非常快速的查找进行了优化。

[`number:array`](#number:array)

存储排序的 u32 数字的数组。

[`flow:hash`](#flow:hash)

自动增长的哈希存储流条目。 搜索计算所需数据包字段的哈希值，并在所选存储桶中搜索匹配条目。

`tablearg` 特性提供了使用在表中查找的值作为规则操作、操作参数或规则选项的参数的能力。 这可以显着减少某些配置中的规则数量。 如果在一个规则中使用了两个表，则使用第二个（目标）的结果。

每个记录可以根据 value-mask 保存一个或多个值。 此掩码是通过 `valtype` 选项在创建表时设置的。 支持以下值类型：

value-mask: value-type\[,value-mask\]

value-type: skipto | pipe | fib | nat | dscp | tag | divert |

netgraph | limit | ipv4

[`skipto`](#skipto_2)

要跳转到的规则编号。

[`pipe`](#pipe_2)

要使用的管道编号。

[`fib`](#fib_2)

要匹配/设置的 fib 号码。

[`nat`](#nat_2)

要跳转到的 nat 编号。

[`dscp`](#dscp)

要匹配/设置的 dscp 值。

[`tag`](#tag_2)

要匹配/设置的标签号。

[`divert`](#divert_2)

将流量转移到的端口号。

[`netgraph`](#netgraph_2)

要将数据包移动到的挂钩编号。

[`limit`](#limit_5)

最大连接数。

[`ipv4`](#ipv4_2)

IPv4 nexthop 将数据包转发到。

[`ipv6`](#ipv6_2)

IPv6 nexthop 将数据包转发到。

`tablearg` 参数可用于以下操作： `nat, pipe, queue, divert, tee, netgraph, ngtee, fwd, skipto, setfib`, 操作参数： `tag, untag`, 规则选项： `limit, tagged` 。

当与 `skipto` 操作一起使用时，用户应该知道代码会将规则集遍历到等于或超过给定数字的规则。

有关表和 tablearg 关键字的示例用法，请参见 [实例](#__u5B9E___u4F8B_) 部分。

[规则集](#__u89C4___u5219___u96C6_)
================================

每个规则或表都属于 32 个不同的 _sets_ 之一，编号为 0 到 31。 Set 31 为默认规则保留。

默认情况下，规则或表放在 set 0 中，除非您在添加新规则或表时使用 `set N` 属性。 集合可以单独和原子地启用或禁用，因此这种机制允许一种简单的方法来存储防火墙的多个配置并在它们之间快速（和原子地）切换。

默认情况下，在添加带有表操作码的规则时，会引用集合 0 中的表，而不管规则集如何。 可以通过将 net.inet.ip.fw.tables\_sets 变量设置为 1 来更改此行为。 然后，规则集将用于表引用。

启用/禁用集合的命令是

`ipfw` `set` \[`disable` number ...\] \[`enable` number ...\]

其中可以指定多个 `enable` 或 `disable` 部分。 命令执行在命令中指定的所有集合上是原子的。 默认情况下，启用所有集。

当您禁用一组时，其规则的行为就好像它们不存在于防火墙配置中一样，只有一个例外：

从被禁用之前的规则创建的动态规则在到期之前仍将处于活动状态。 为了删除动态规则，您必须明确删除生成它们的父规则。

可以使用命令更改设置的规则数量

`ipfw` `set move` {`rule` rule-number | old-set} `to` new-set

此外，您可以使用命令自动交换两个规则集

`ipfw` `set swap` first-set second-set

有关规则集的一些可能用途，请参见 [实例](#__u5B9E___u4F8B_) 部分。

[状态防火墙](#__u72B6___u6001___u9632___u706B___u5899_)
==================================================

状态操作是防火墙在检测到与给定模式匹配的数据包时为特定流动态创建规则的一种方式。 对有状态操作的支持来自 `rules` 的 `check-state`, `keep-state`, `record-state`, `limit` 和 `set-limit` 选项。

动态规则时创建一个包匹配一个 `keep-state`, `record-state`, `limit` 或 `set-limit` 规定,导致建立一个 _dynamic_ 规则相匹配的所有,只有与给定 _protocol_ 数据包之间的 _src-ip/src-port dst-ip/dst-port_ 一双地址(这里使用 (_src_ 和 _dst_ 只表示初始匹配地址,但它们之后是完全相同的)。 由 `keep-state` 选项创建的规则也有一个 :flowname 取自它。 此名称与地址、端口和协议一起用于匹配。 动态规则将在第一次出现 `check-state, keep-state` 或 `limit` 时被检查，并且在匹配时执行的操作将与父规则中的相同。

请注意，除了协议和 IP 地址和端口以及 :flowname 之外，不会在动态规则上检查其他属性。

动态规则的典型用途是保持封闭的防火墙配置，但让来自内部网络的第一个 TCP SYN 数据包为流安装动态规则，以便允许属于该会话的数据包通过防火墙：

`ipfw add check-state :OUTBOUND`

`ipfw add allow tcp from my-subnet to any setup keep-state :OUTBOUND`

`ipfw add deny tcp from any to any`

类似的方法可用于 UDP，其中来自内部的 UDP 数据包将安装动态规则以让响应通过防火墙：

`ipfw add check-state :OUTBOUND`

`ipfw add allow udp from my-subnet to any keep-state :OUTBOUND`

`ipfw add deny udp from any to any`

动态规则会在一段时间后过期，这取决于流的状态和一些 `sysctl` 变量的设置。 有关详细信息，请参阅 [SYSCTL 变量](#SYSCTL___u53D8___u91CF_) 部分。 对于 TCP 会话，可以指示动态规则在规则即将到期时定期发送 keepalive 数据包以刷新规则状态。

有关如何使用动态规则的更多示例，请参见 [示例](#__u793A___u4F8B_) 部分。

[流量整形（DUMMYNET）配置](#__u6D41___u91CF___u6574___u5F62___uFF08_DUMMYNET__uFF09___u914D___u7F6E_)
=============================================================================================

`ipfw` 也是 `dummynet` 量整形器、数据包调度器和网络仿真器的用户界面，该子系统可以人为地排队、延迟或丢弃数据包，以模拟某些网络链接或排队系统的行为。

`dummynet` 通过首先使用防火墙来使用任何可以在 `ipfw` 规则中使用的匹配模式来选择数据包。 匹配的数据包然后被传递到两个不同的对象中的任何一个，这两个对象实现了流量调节：

_pipe_

_pipe_ 模拟具有给定带宽和传播延迟的 _link_ ，由 FIFO 调度器和具有可编程队列大小和丢包率的单个队列驱动。 数据包从 `ipfw` 出来时会附加到队列中，然后以 FIFO 顺序以所需速率传输到链路。

_queue_

_queue_ 是一种抽象，用于使用几种数据包调度算法之一来实现数据包调度。 发送到 _queue_ 的数据包首先根据 5 元组上的掩码分组为流。 然后将流传递给与 _queue_ 关联的调度程序，每个流使用 _queue_ 本身中配置的调度参数（权重和其他）。 调度器依次连接到模拟链路，并根据权重和使用的调度算法的特征在积压流之间仲裁链路的带宽。

在实践中， _pipes_ 可用于对流可以使用的带宽设置硬限制，而 _queues_ 可用于确定不同流如何共享可用带宽。

下面是队列、流、调度程序和链接绑定的图形表示。

 (flow\_mask|sched\_mask) sched\_mask +---------+ weight Wx +-------------+ | |->-\[flow\]-->--| |-+ -->--| QUEUE x | ... | | | | |->-\[flow\]-->--| SCHEDuler N | | +---------+ | | | ... | +--\[LINK N\]-->-- +---------+ weight Wy | | +--\[LINK N\]-->-- | |->-\[flow\]-->--| | | -->--| QUEUE y | ... | | | | |->-\[flow\]-->--| | | +---------+ +-------------+ | +-------------+ 

了解 SCHED\_MASK 和 FLOW\_MASK 的作用很重要，它们是通过命令配置的

`ipfw sched N config mask SCHED_MASK ...`

和

`ipfw queue X config mask FLOW_MASK ....`

SCHED\_MASK 用于将流分配给一个或多个调度程序实例，在应用 SCHED\_MASK 后，为数据包的 5 元组的每个值分配一个。 例如，使用 \`\`src-ip 0xffffff00'' 为每个 /24 目标子网创建一个实例。

FLOW\_MASK 与 SCHED\_MASK 一起用于将数据包拆分为流。 例如，使用 \`\`src-ip 0x000000ff'' 和前面的 SCHED\_MASK 为每个单独的源地址创建一个流。 反过来，每个 /24 子网的流将被发送到同一个调度程序实例。

上图甚至适用于 _pipe_ 情况，唯一的限制是 _pipe_ 仅支持 SCHED\_MASK，并强制使用 FIFO 调度程序（这些是出于向后兼容性的原因；实际上，在内部， `dummynet` 的管道完全按照多于）。 `dummynet` 操作有两种模式： “normal” 和 “fast” 。 “normal” 模式试图模拟一个真实的链接： `dummynet` 调度程序确保数据包不会比它在给定带宽的真实链接上更快地离开管道。 “fast” 模式允许某些数据包绕过 `dummynet` 调度程序（如果数据包流不超过管道的带宽）。 这就是为什么 “fast” 模式需要更少的 CPU 周期（平均），并且与具有相同带宽的真实链路相比，数据包延迟可以显着降低。 默认模式为 “normal” 。 可以通过将 net.inet.ip.dummynet.io\_fast sysctl(8) 变量设置为非零值来启用 “fast” 模式。

[管道、队列和调度器配置](#__u7BA1___u9053___u3001___u961F___u5217___u548C___u8C03___u5EA6___u5668___u914D___u7F6E_)
--------------------------------------------------------------------------------------------------------

The _pipe_, _queue_ 和 _scheduler_ 程序配置命令如下：

`pipe` number `config` pipe-configuration

`queue` number `config` queue-configuration

`sched` number `config` sched-configuration

可以为管道配置以下参数：

[`bw`](#bw) bandwidth | device

带宽，单位为 \[`K` | `M`|`G`\]{`bit/s`|`Byte/s`}。

值 0（默认值）表示无限带宽。单位必须紧跟在数字后面，如

`ipfw pipe 1 config bw 300Kbit/s`

如果指定设备名称而不是数值，如

`ipfw pipe 1 config bw tun0`

然后发送时钟由指定的设备提供。 目前只有 tun(4) 设备支持此功能，与 ppp(8) 一起使用。

[`delay`](#delay) ms-delay

传播延迟，以毫秒为单位。 该值四舍五入到时钟滴答的下一个倍数（通常为 10 毫秒，但最好使用 “options HZ=1000” 运行内核以将粒度降低到 1 毫秒或更小）。 默认值为 0，表示无延迟。

[`burst`](#burst) size

如果要发送的数据超过了管道的带宽限制（并且管道之前是空闲的），则最多允许 size 个字节的数据绕过 `dummynet` 调度程序，并且将在物理链路允许的情况下以最快的速度发送。 任何附加数据都将以管道带宽指定的速率传输。 突发大小取决于 `pipe` 空闲的时间；有效突发大小计算如下： MAX( size , `bw` \* pipe\_idle\_time)。

[`profile`](#profile) filename

指定在链路上传输数据包时产生的额外开销的文件。

某些链路类型在数据包的传输中引入了额外的延迟，例如，由于 MAC 级别的成帧、信道使用的争用、MAC 级别的重传等。 从我们的角度来看，在这段额外的时间内，通道实际上是不可用的，这取决于链路类型是恒定的还是可变的。 此外，在此时间之后，可能会丢弃数据包（例如，在太多重传后的无线链路上）。 我们可以用代表其分布的经验曲线对额外延迟进行建模。

 累积概率 1.0 ^ | L +-- 损失级别 x | \*\*\*\*\*\* | \* | \*\*\*\*\* | \* | \*\* | \* +-------\*-------------------> 延迟 

经验曲线可以同时具有垂直线和水平线。 垂直线代表一系列概率的恒定延迟。 水平线对应于延迟分布的不连续性：管道将使用给定概率的最大延迟。

文件格式如下，空格作为分隔符， '#' 表示注释的开头：

[`name`](#name) identifier

可选名称（由 "ipfw pipe show" 列出）标识延迟分布；

[`bw`](#bw_2) value

用于管道的带宽。 如果此处未指定，则它必须作为管道的配置参数显式存在；

[`loss-level`](#loss-level) L

数据包丢失的概率。 （0.0 <= L <= 1.0，默认1.0，即无损失）；

[`samples`](#samples) N

曲线内部表示中使用的样本数（2..1024；默认为 100）；

[`delay prob`](#delay_prob) | [`prob delay`](#prob_delay)

这两行之一是强制性的，并使用数据点定义以下行的格式。

XXX YYY

根据选择的格式，2 条或更多条线代表曲线中的点，优先考虑延迟或概率。 延迟的单位是毫秒。 数据点不需要排序。 此外，实际线的数量可能与 "samples" 参数的值不同： `ipfw` 实用程序将根据需要对曲线进行排序和插值。

配置文件示例：

name bla\_bla\_bla samples 100 loss-level 0.86 prob delay 0 200 # minimum overhead is 200ms 0.5 200 0.5 300 0.8 1000 0.9 1300 1 1300 #configuration file end 

可以为队列配置以下参数：

[`pipe`](#pipe_3) pipe\_nr

将队列连接到指定管道。 多个队列（具有相同或不同的权重）可以连接到同一管道，该管道指定队列集的聚合速率。

[`weight`](#weight) weight

指定要用于匹配此队列的流的权重。 权重必须在 1..100 范围内，默认为 1。

可以为调度程序配置以下不区分大小写的参数：

[`type`](#type_2) {fifo | wf2q+ | rr | qfq | fq\_codel | fq\_pie}

指定要使用的调度算法。

[`fifo`](#fifo)

只是一个 FIFO 调度程序（这意味着所有数据包在到达调度程序时都存储在同一个队列中）。 FIFO 的每个数据包时间复杂度为 O(1)，常数非常低（在 2GHz 台式机上估计为 60-80ns），但不提供服务保证。

[`wf2q+`](#wf2q+)

实现 WF2Q+ 算法，这是一种加权公平排队算法，允许流根据其权重共享带宽。 请注意，权重不是优先级；即使是重量很小的流量也永远不会饿死。 WF2Q+ 的每个数据包处理成本为 O(log N)，其中 N 是流的数量，并且是以前版本 dummynet 的队列使用的默认算法。

[`rr`](#rr)

实现了 Deficit Round Robin 算法，该算法具有 O(1) 处理成本（大约每个数据包 100-150ns）并允许根据权重分配带宽，但服务保证很差。

[`qfq`](#qfq)

实现了 QFQ 算法，它是 WF2Q+ 的一个非常快速的变体，具有类似的服务保证和 O(1) 处理成本（大约每个数据包 200-250ns）。

[`fq_codel`](#fq_codel)

实现了 FQ-CoDel (FlowQueue-CoDel) 调度器/AQM 算法，该算法使用改进的 Deficit Round Robin 调度器来管理两个子队列列表（旧子队列和新子队列），为轻量级提供短暂的优先级或短脉冲流。 默认情况下，子队列总数为 1024。 FQ-CoDel 的内部动态创建的子队列由 CoDel AQM 的单独实例控制。

[`fq_pie`](#fq_pie)

实现了 FQ-PIE (FlowQueue-PIE) 调度器/AQM 算法，该算法类似于 `fq_codel` 但使用每个子队列 PIE AQM 实例来控制队列延迟。

`fq_codel` 从 `codel` 继承 AQM 参数和选项（见下文）， `fq_pie` 从 `pie` 继承 AQM 参数和选项（见下文）。 此外， `fq_codel` 和 `fq_pie` 都具有共享的调度程序参数，它们是：

[`quantum`](#quantum)

m 指定调度程序的量程（信用）。 m 是队列在移动到旧队列列表尾部之前可以服务的字节数。 默认值为 1514 字节，最大可接受值为 9000 字节。

[`limit`](#limit_6)

m 指定由调度程序实例管理的所有队列的硬大小限制（以数据包为单位）。 m 的默认值为 10240 个数据包，最大可接受值为 20480 个数据包。

[`flows`](#flows)

m 指定 fq\_\* 创建和管理的流队列（子队列）的总数。 默认情况下，创建 fq\_{codel/pie} 调度程序实例时会创建 1024 个子队列。 可接受的最大值为 65536。

请注意， `fq_codel` 或 `fq_pie` 之后的任何标记都被视为 fq\_{codel/pie} 的参数。 因此，确保所有与 fq\_{codel/pie} 无关的调度程序配置选项都写在 `fq_codel/fq_pie` 令牌之前。

除了类型之外，还可以为调度程序指定管道允许的所有参数。

最后，可以为管道和队列配置以下参数：

[`buckets`](#buckets) hash-table-size

桶哈希表大小 指定用于存储各种队列的散列表的大小。 默认值为 64，由 sysctl(8) 变量 net.inet.ip.dummynet.hash\_size, 控制，允许范围为 16 到 65536。

[`mask`](#mask) mask-specifier

通过 `ipfw` 规则发送到给定管道或队列的数据包可以进一步分类为多个流，然后将每个流发送到不同的 _dynamic_ 管道或队列。 流标识符是通过对管道或队列配置中的 `mask` 选项指定的 IP 地址、端口和协议类型进行掩码来构造的。 对于每个不同的流标识符，都会使用与原始对象相同的参数创建一个新的管道或队列，并将匹配的数据包发送给它。

因此，当使用 _dynamic pipes_ 管道时，每个流将获得与管道定义的相同带宽，而当使用 _dynamic queues_ 时，每个流将与同一队列生成的其他流平均共享父级的管道带宽（注意其他队列不同重量的可能连接到同一管道）。-
可用的掩码说明符是以下一项或多项的组合：

`dst-ip` mask, `dst-ip6` mask, `src-ip` mask, `src-ip6` mask, `dst-port` mask, `src-port` mask, `flow-id` mask, `proto` mask 或 `all`,

其中后者意味着所有字段中的所有位都是有效的。

[`noerror`](#noerror)

当一个数据包被一个 `dummynet` 队列或管道丢弃时，错误通常会报告给内核中的调用程序，就像设备队列填满时一样。 设置此选项会报告数据包已成功传递，这对于您想要模拟远程路由器的丢失或拥塞的一些实验设置可能需要。

[`plr`](#plr) packet-loss-rate

丢包率。 参数 packet-loss-rate 是一个介于 0 和 1 之间的浮点数，其中 0 表示不丢失，1 表示 100% 丢失。 丢失率在内部以 31 位表示。

[`queue`](#queue_2) {slots | size`Kbytes`}

队列大小，以 slots 或 `KBytes` 为单位。 默认值为 50 个插槽，这是以太网设备的典型队列大小。 请注意，对于慢速链接，您应该保持队列大小较短，否则您的流量可能会受到严重排队延迟的影响。 例如，50 个最大大小的以太网数据包（1500 字节）意味着 600Kbit 或 30Kbit/s 管道上的 20s 队列。 如果您从具有更大 MTU 的接口获取数据包，例如具有 16KB 数据包的环回接口，则可能会导致更糟糕的效果。 sysctl(8) 变量 _net.inet.ip.dummynet.pipe\_byte\_limit_ 和 _net.inet.ip.dummynet.pipe\_slot\_limit_ 控制可以指定的最大长度。

[`red`](#red) | [`gred`](#gred) w\_q/min\_th/max\_th/max\_p

\[ecn\] 利用 RED（随机早期检测）队列管理算法。 w\_q 和 max\_p 是介于 0 和 1（含）之间的浮点数，而 min\_th 和 max\_th 是指定队列管理阈值的整数（如果队列以字节为单位，则阈值以字节为单位，否则以槽为单位）。 如果需要，这两个参数也可以具有相同的值。 `dummynet` 还支持温和的 RED 变体 (gred) 和 ECN (Explicit Congestion Notification) 作为可选的。 三个 sysctl(8) 变量可用于控制 RED 行为：

net.inet.ip.dummynet.red\_lookup\_depth

指定链路空闲时计算平均队列的精度（默认为 256，必须大于零）

net.inet.ip.dummynet.red\_avg\_pkt\_size

指定预期的平均数据包大小（默认为 512，必须大于零）

net.inet.ip.dummynet.red\_max\_pkt\_size

指定预期的最大数据包大小，仅在队列阈值以字节为单位时使用（默认为 1500，必须大于零）。

[`codel`](#codel) \[`target` time\] \[`interval` time\] \[`ecn` | `noecn`\]

利用 CoDel（受控延迟）队列管理算法。 默认情况下， time 被解释为毫秒，但可以指定秒 (s)、毫秒 (ms) 或微秒 (us)。 CoDel 根据队列中的数据包停留时间丢弃或标记 (ECN) 数据包。 `target` time （默认为 5 毫秒）是 CoDel 允许的最小可接受的持久队列延迟。 CoDel 不会在数据包停留时间高于 `target` time 后直接丢弃数据包，而是在丢弃之前等待 `interval` time （默认为 100 毫秒）。 `interval` time 应设置为所有预期连接的最大 RTT。 当队列延迟变高时， `ecn` 为启用 ECN 的 TCP 流启用（默认禁用）数据包标记（而不是丢弃）。

请注意， `codel` 之后的任何标记都被视为 CoDel 的参数。 因此，请确保所有管道/队列配置选项都写在 `codel` 令牌之前。

sysctl(8) 变量 net.inet.ip.dummynet.codel.target 和 net.inet.ip.dummynet.codel.interval 可用于设置 CoDel 默认参数。

[`pie`](#pie) \[`target` time\] \[`tupdate` time\] \[`alpha` n\] \[`beta` n\] \[`max_burst` time\] \[`max_ecnth` n\] \[`ecn` | `noecn`\] \[`capdrop` | `nocapdrop`\] \[`drand` | `nodrand`\] \[`onoff`\] \[`dre` | `ts`\]

利用 PIE（增强型比例积分控制器）队列管理算法。 PIE 在入队过程中根据计算的丢弃概率丢弃或标记数据包，目的是在保持低队列延迟的同时实现高吞吐量。 在 `tupdate` time 时间（默认为 15ms）的固定时间间隔内，后台进程（重新）根据与 `target` time （默认为 15ms）的队列延迟偏差和队列延迟趋势计算概率。 PIE 通过使用出发率估计方法或（可选地）使用类似于 CoDel 的数据包时间戳方法来近似当前队列延迟。 默认情况下， time 被解释为毫秒，但可以指定秒 (s)、毫秒 (ms) 或微秒 (us)。 其他 PIE 参数和选项如下：

[`alpha`](#alpha) n

n 是一个介于 0 和 7 之间的浮点数，它指定了在丢弃概率计算中使用的队列延迟偏差的权重。 0.125 是默认值。

[`beta`](#beta) n

n 是一个介于 0 和 7 之间的浮点数，它指定了在丢弃概率计算中使用的队列延迟趋势的权重。 1.25 是默认值。

[`max_burst`](#max_burst) time

PIE 不丢弃/标记数据包的最长时间。150ms 是默认值，10s 是最大值。

[`max_ecnth`](#max_ecnth) n

即使启用了 ECN，当丢弃概率高于 ECN 概率阈值 `max_ecnth` n 时，PIE 也会丢弃数据包而不是标记它们，默认值为 0.1（即 10%），最大值为 1。

[`ecn`](#ecn) | [`noecn`](#noecn)

为启用 ECN 的 TCP 流启用或禁用 ECN 标记。默认禁用。

[`capdrop`](#capdrop) | [`nocapdrop`](#nocapdrop)

启用或禁用上限下降调整。 默认情况下启用上限调整。

[`drand`](#drand) | [`nodrand`](#nodrand)

启用或禁用丢弃概率去随机化。 去随机化消除了丢包太近或太远的问题。 默认情况下启用去随机化。

[`onoff`](#onoff)

启用根据队列负载打开和关闭 PIE。 如果启用此选项，PIE 会在超过 1/3 的队列已满时打开。 默认情况下禁用此选项。

[`dre`](#dre) | [`ts`](#ts)

使用出发率估计 `dre` 或时间戳 `ts` 计算队列延迟。 默认使用 `dre` 。

请注意， `pie` 之后的任何标记都被视为 PIE 的参数。 因此，请确保所有管道/队列的配置选项都写在 `pie` token 之前。 sysctl(8) 变量可用于控制 `pie` 的默认参数。 有关详细信息，请参阅 [SYSCTL 变量](#SYSCTL___u53D8___u91CF_) 部分。

当与 IPv6 数据一起使用时， `dummynet` 目前有几个限制。 `dummynet` 处理后，将链路本地数据包路由到接口所需的信息不可用，因此这些数据包在输出路径中被丢弃。 应注意确保链路本地数据包不会传递到 `dummynet` 。

[清单](#__u6E05___u5355_)
=======================

以下是设计规则时需要考虑的一些要点：

*   请记住，您过滤 `in` 和 `out` 的数据包。 大多数连接都需要双向数据包。
*   记住要非常仔细地测试。 执行此操作时最好靠近控制台。 如果您不能靠近控制台，请使用自动恢复脚本，例如 /usr/share/examples/ipfw/change\_rules.sh 中的脚本。
*   不要忘记环回接口。

[要点](#__u8981___u70B9_)
=======================

*   在某些情况下，碎片数据报会被无条件丢弃。 如果 TCP 数据包不包含至少 20 字节的 TCP 标头，则丢弃 TCP 数据包，如果它们不包含完整的 8 字节 UDP 标头，则丢弃 UDP 数据包，如果它们不包含 4 字节的 ICMP 标头，则丢弃 ICMP 数据包，足够了指定 ICMP 类型、代码和校验和。 这些数据包被简单地记录为 “pullup failed” ，因为数据包中可能没有足够的好数据来产生有意义的日志条目。
*   另一种类型的数据包被无条件丢弃，即片段偏移量为 1 的 TCP 数据包。 这是一个有效的数据包，但它只有一个用途，可以绕过防火墙。 启用日志记录后，这些数据包被报告为被规则 -1 丢弃。
*   如果您通过网络登录，加载 kld(4) 版本的 `ipfw` 可能并不像您想象的那么简单。 建议使用以下命令行：
    
    kldload ipfw && \\ ipfw add 32000 allow ip from any to any 
    
    同样，做一个
    
    ipfw flush 
    
    在类似的环境中也是一个坏主意。
    
*   如果系统安全级别设置为 3 或更高，则不能修改 `ipfw` 过滤器列表（有关系统安全级别的信息，请参见 init(8) ）。

[数据包转移](#__u6570___u636E___u5305___u8F6C___u79FB_)
==================================================

绑定到指定端口的 divert(4) 套接字将接收转移到该端口的所有数据包。 如果没有套接字绑定到目标端口，或者没有加载转移模块，或者如果内核没有使用转移套接字支持编译，则丢弃数据包。

[网络地址转换 (NAT)](#__u7F51___u7EDC___u5730___u5740___u8F6C___u6362__(NAT))
=======================================================================

`ipfw` 支持使用内核版本的 libalias(3) 进行内核内 NAT。 内核模块 `ipfw_nat` 应该被加载或者内核应该有 `options IPFIREWALL_NAT` 才能使用 NAT。

nat配置命令如下：

`nat` nat\_number `config` nat-configuration

可以配置以下参数：

[`ip`](#ip_2) ip\_address

定义用于别名的 IP 地址。

[`if`](#if) nic

使用网卡的ip地址进行别名，如果网卡的ip地址发生变化，动态改变它。

[`log`](#log_2)

在此 nat 实例上启用日志记录。

[`deny_in`](#deny_in)

拒绝来自外界的任何传入连接。

[`same_ports`](#same_ports)

尝试使别名端口号与实际本地端口号保持不变。

[`unreg_only`](#unreg_only)

本地网络上不是源自 RFC 1918 未注册地址空间的流量将被忽略。

[`unreg_cgn`](#unreg_cgn)

与 unreg\_only 类似，但包括 RFC 6598（运营商级 NAT）地址范围。

[`reset`](#reset_2)

在地址更改时重置数据包别名引擎的表。

[`reverse`](#reverse)

颠倒 libalias 处理别名的方式。

[`proxy_only`](#proxy_only)

仅遵守透明代理规则，不执行数据包别名。

[`skip_global`](#skip_global)

在全局状态查找的情况下跳过实例（见下文）。

可以提供一些特殊值而不是 nat\_number:

[`global`](#global)

在所有配置的 nat 实例中查找翻译状态。 如果找到条目，则根据该条目对数据包进行别名。 如果在任何实例中都没有找到条目，则数据包原封不动地传递，并且不会创建新条目。 有关详细信息，请参阅 natd(8) 中的 [多个实例](#__u591A___u4E2A___u5B9E___u4F8B_) 部分。

[`tablearg`](#tablearg)

使用查找表中提供的参数。有关查找表的更多信息，请参阅下面的 [查找表](#__u67E5___u627E___u8868_) 部分。

要让数据包在（去）别名后继续，请将 sysctl 变量 net.inet.ip.fw.one\_pass 设置为 0。 有关别名模式的更多信息，请参阅 libalias(3) 。 有关 nat 用法的一些示例，请参见 [实例](#__u5B9E___u4F8B_) 部分。

[IPFW 中的重定向和 LSNAT 支持](#IPFW___u4E2D___u7684___u91CD___u5B9A___u5411___u548C__LSNAT___u652F___u6301_)
-----------------------------------------------------------------------------------------------------

重定向和 LSNAT 支持紧密遵循 natd(8) 中使用的语法。 有关如何进行重定向和 lsnat 的一些示例，请参见 [实例](#__u5B9E___u4F8B_) 部分。

[SCTP NAT 支持](#SCTP_NAT___u652F___u6301_)
-----------------------------------------

SCTP nat 可以通过 `ipfw` 命令行工具以与 TCP 类似的方式配置。 主要区别在于 `sctp nat` 不做端口转换。 由于本地和全局侧端口相同，因此无需同时指定。 端口重定向如下：

`nat` nat\_number `config if` nic `redirect_port sctp` ip\_address \[,addr\_list\] {\[port | port-port\] \[,ports\]}

大多数 `sctp nat` 配置可以通过 sysctl(8) 接口实时完成。 一切都可以动态改变，尽管 hash\_table 的大小只会针对新的 `nat` 实例而改变。 有关详细信息，请参阅 [SYSCTL 变量](#SYSCTL___u53D8___u91CF_) 。

[IPv6/IPv4 网络地址和协议转换](#IPv6/IPv4___u7F51___u7EDC___u5730___u5740___u548C___u534F___u8BAE___u8F6C___u6362_)
==========================================================================================================

[有状态的翻译](#__u6709___u72B6___u6001___u7684___u7FFB___u8BD1_)
-----------------------------------------------------------

`ipfw` 支持内核内 IPv6/IPv4 网络地址和协议转换。 有状态的 NAT64 转换允许纯 IPv6 客户端使用单播 TCP、UDP 或 ICMP 协议联系 IPv4 服务器。 分配给有状态 NAT64 转换器的一个或多个 IPv4 地址在多个仅 IPv6 客户端之间共享。 当有状态 NAT64 与 DNS64 结合使用时，通常不需要在 IPv6 客户端或 IPv4 服务器中进行任何更改。 内核模块 `ipfw_nat64` 应该被加载或者内核应该有 `options IPFIREWALL_NAT64` 能够使用有状态的 NAT64 转换器。

有状态的 NAT64 为几种类型的对象使用一堆内存。 当 IPv6 客户端发起连接时，NAT64 转换器在状态表中创建一个主机条目。 每个主机条目都使用预先分配的 IPv4 别名条目。 每个别名条目都有一些按需分配的端口组条目。 端口组条目包含连接状态条目。 有几个选项可以控制这些对象的限制和生命周期。

NAT64 转换器在进行 ICMPv6/ICMP 转换时遵循 RFC7915，不支持的消息类型将被静默丢弃。 IPv6 需要明确允许正确操作的几种 ICMPv6 消息类型。 确保转换规则不会处理 ND6 邻居请求（ICMPv6 类型 135）和邻居通告（ICMPv6 类型 136）消息。

翻译后 NAT64 翻译器默认通过相应的 netisr 队列发送数据包。 因此转换器主机应配置为 IPv4 和 IPv6 路由器。 这也意味着，一个数据包由防火墙处理两次。 翻译器第一次处理和消费原始数据包，然后将其作为翻译数据包再次处理。 此行为可以通过 sysctl 变量 net.inet.ip.fw.nat64\_direct\_output 进行更改。 翻译后的数据包也可以使用 `tag` 规则动作进行标记，然后通过 `tagged` 的操作码进行匹配，以避免循环和额外开销。

有状态的 NAT64 配置命令如下：

`nat64lsn` name `create` create-options

可以配置以下参数：

[`prefix4`](#prefix4) ipv4\_prefix/plen

带掩码的 IPv4 前缀定义了转换后用作源地址的 IPv4 地址池。 有状态的 NAT64 模块将客户端的 IPv6 源地址转换为该池中的一个 IPv4 地址。 请注意，在状态表中没有相应状态条目的传入 IPv4 数据包将被转换器丢弃。 确保转换规则处理数据包，目的地为配置的前缀。

[`prefix6`](#prefix6) ipv6\_prefix/length

IPv6 前缀定义了转换器用来表示 IPv4 地址的嵌入 IPv4 的 IPv6 地址。 此 IPv6 前缀应在 DNS64 中配置。 转换器实现遵循 RFC6052，它将前缀的长度限制为以下之一：32、40、48、56、64 或 96。 众所周知的 IPv6 前缀 64:ff9b:: 必须是 96 位长。 特殊的 ::/length 前缀可用于处理具有一个 NAT64 实例的多个 IPv6 前缀。 NAT64 实例将根据前缀 length 确定目标 IPv4 地址。

[`states_chunks`](#states_chunks) number

单个端口组中的状态块数。 默认情况下，每个端口组可以在单个块中保留 64 个状态条目。 上述值会影响可与单个 IPv4 别名地址和端口关联的最大状态数。 该值必须是 2 的幂，最大为 128。

[`host_del_age`](#host_del_age) seconds

IPv6 客户端的主机条目将被删除并由于不活动而释放其所有资源之前的秒数。 默认值为 3600 。

[`pg_del_age`](#pg_del_age) seconds

释放未使用状态条目的端口组之前的秒数。 默认值为 900 。

[`tcp_syn_age`](#tcp_syn_age) seconds

将保留仅发送 SYN 的 TCP 连接状态条目的秒数。 如果 TCP 连接建立没有完成，状态条目将被删除。 默认值为 10 。

[`tcp_est_age`](#tcp_est_age) seconds

将保留已建立 TCP 连接的状态条目的秒数。 默认值为 7200 。

[`tcp_close_age`](#tcp_close_age) seconds

关闭 TCP 连接的状态条目将被保留的秒数。 需要为关闭的连接保留状态条目，因为 IPv4 服务器通常将关闭的连接保持在 TIME\_WAIT 状态几分钟。 由于转换器的 IPv4 地址在所有 IPv6 客户端之间共享，因此来自相同地址和端口的新连接可能会被服务器拒绝，因为这些连接仍处于 TIME\_WAIT 状态。 将它们保存在翻译器的状态表中可以防止此类拒绝。 默认值为 180 。

[`udp_age`](#udp_age) seconds

翻译器在等待对已发送 UDP 数据报的回复时保持状态条目的秒数。 默认值为 120 。

[`icmp_age`](#icmp_age) seconds

翻译器保持状态条目等待对已发送 ICMP 消息的回复的秒数。 默认值为 60 。

[`log`](#log_3)

通过 ipfwlog0 接口通过 BPF 打开所有已处理数据包的日志记录。 ipfwlog0 是一个伪接口，可以在启动后使用 `ifconfig` 命令手动创建。 请注意，它的用途与 ipfw0 接口不同。 翻译器随每个数据包向 BPF 发送附加信息。 使用 `tcpdump` ，您可以在翻译前后查看每个处理过的数据包。

[`-log`](#-log)

关闭所有通过 BPF 处理的数据包的日志记录。

[`allow_private`](#allow_private)

打开处理私有 IPv4 地址。 默认情况下，不处理目标映射到 RFC1918 定义的私有地址范围的 IPv6 数据包。

[`-allow_private`](#-allow_private)

关闭 `nat64` 实例中的私有地址处理。

要检查有状态 NAT64 的状态表，可以使用以下命令：

`nat64lsn` name `show` `states`

无状态 NAT64 转换器不使用状态表进行转换，而是仅根据从配置的查找表中获取的映射将 IPv4 地址转换为 IPv6，反之亦然。 由于无状态转换器不使用状态表，因此可以将其配置为将 IPv4 客户端传递给仅 IPv6 的服务器。

无状态 NAT64 配置命令如下：

`nat64stl` name `create` create-options

可以配置以下参数：

[`prefix6`](#prefix6_2) ipv6\_prefix/length

IPv6 前缀定义了转换器用来表示 IPv4 地址的嵌入 IPv4 的 IPv6 地址。 此 IPv6 前缀应在 DNS64 中配置。

[`table4`](#table4) table46

查找表 table46 包含应如何将 IPv4 地址转换为 IPv6 地址的映射。

[`table6`](#table6) table64

查找表 table64 包含应如何将 IPv6 地址转换为 IPv4 地址的映射。

[`log`](#log_4)

通过 ipfwlog0 接口通过 BPF 打开所有已处理数据包的日志记录。

[`-log`](#-log_2)

关闭所有通过 BPF 处理的数据包的日志记录。

[`allow_private`](#allow_private_2)

打开处理私有 IPv4 地址。 默认情况下，不处理目标映射到 RFC1918 定义的私有地址范围的 IPv6 数据包。

[`-allow_private`](#-allow_private_2)

关闭 `nat64` 实例中的私有地址处理。

请注意，无状态翻译器对不匹配数据包的行为与有状态翻译器不同。 如果在查找表中没有找到相应的地址，则不会丢弃数据包并继续搜索。

[XLAT464 CLAT 翻译](#XLAT464_CLAT___u7FFB___u8BD1_)
-------------------------------------------------

XLAT464 CLAT NAT64 转换器实现了 RFC6877 中定义的客户端无状态转换，与上面解释的无状态 NAT64 转换器非常相似。 它不是使用查找表，而是使用配置的前缀在 IPv4 和 IPv6 地址之间进行一对一映射。 对于不使用 DNS64 服务的应用程序（例如 VoIP），这种模式可以替代 DNS64 服务，允许它们在远程 NAT64 转换器的帮助下通过纯 IPv6 网络访问纯 IPv4 互联网。

CLAT NAT64 配置命令如下：

`nat64clat` name `create` create-options

可以配置以下参数：

[`clat_prefix`](#clat_prefix) ipv6\_prefix/length

IPv6 前缀定义了转换器使用的嵌入 IPv4 的 IPv6 地址来表示源 IPv4 地址。

[`plat_prefix`](#plat_prefix) ipv6\_prefix/length

IPv6 前缀定义了转换器使用的嵌入 IPv4 的 IPv6 地址来表示目标 IPv4 地址。 此 IPv6 前缀应在远程 NAT64 转换器上配置。

[`log`](#log_5)

通过 ipfwlog0 接口通过 BPF 打开所有已处理数据包的日志记录。

[`-log`](#-log_3)

关闭所有通过 BPF 处理的数据包的日志记录。

[`allow_private`](#allow_private_3)

打开处理私有 IPv4 地址。 默认情况下， `nat64clat` 实例不会处理具有 RFC1918 中定义的私有范围的目标地址的 IPv4 数据包。

[`-allow_private`](#-allow_private_3)

关闭 `nat64clat` 实例中的私有地址处理。

请注意，CLAT 翻译器对不匹配数据包的行为与有状态翻译器不同。 如果相应的地址与配置的前缀不匹配，则不会丢弃数据包并继续搜索。

[IPv6 到 IPv6 网络前缀转换 (NPTv6)](#IPv6___u5230__IPv6___u7F51___u7EDC___u524D___u7F00___u8F6C___u6362__(NPTv6))
==========================================================================================================

`ipfw` 支持内核内 IPv6 到 IPv6 网络前缀转换，如 RFC6296 中所述。 内核模块 `ipfw_nptv6` 应该被加载或者内核应该有 `options IPFIREWALL_NPTV6` 能够使用 NPTv6 翻译器。

NPTv6 配置命令如下：

`nptv6` name `create` create-options

可以配置以下参数：

[`int_prefix`](#int_prefix) ipv6\_prefix

内部网络中使用的 IPv6 前缀。 NPTv6 模块在匹配此前缀时转换源地址。

[`ext_prefix`](#ext_prefix) ipv6\_prefix

外部网络中使用的 IPv6 前缀。 NPTv6 模块在匹配此前缀时转换目标地址。

[`ext_if`](#ext_if) nic

NPTv6 模块将使用来自接口 nic 的第一个全局 IPv6 地址作为外部前缀。 在动态获取外部网络的 IPv6 前缀时很有用。 `ext_prefix` 和 `ext_if` 选项是互斥的。

[`prefixlen`](#prefixlen) length

指定 IPv6 前缀的长度。 它必须在 8 到 64 的范围内。

请注意，当 IPv6 数据包转发被禁用时，前缀转换规则会被忽略。 要启用数据包转发，请将 sysctl 变量 net.inet6.ip6.forwarding 设置为 1。

要让数据包在翻译后继续，请将 sysctl 变量 net.inet.ip.fw.one\_pass 设置为 0。

[加载程序可调参数](#__u52A0___u8F7D___u7A0B___u5E8F___u53EF___u8C03___u53C2___u6570_)
=============================================================================

在加载 ipfw 模块之前，可以在 loader(8) 提示、 loader.conf(5) 或 kenv(1) 中设置可调参数。

net.inet.ip.fw.default\_to\_accept: 0

定义 ipfw last 规则行为。 此值覆盖内核配置文件中的 `options IPFW_DEFAULT_TO_(ACCEPT|DENY)` 。

net.inet.ip.fw.tables\_max: 128

定义 ipfw 中可用的表数。 数量不能超过 65534。

[SYSCTL 变量](#SYSCTL___u53D8___u91CF_)
=====================================

一组 sysctl(8) 变量控制防火墙和相关模块（ (`dummynet`, `bridge`, `sctp nat`) ）的行为。 下面显示了它们及其默认值（但始终使用 sysctl(8) 命令检查实际使用的值）和含义：

net.inet.ip.alias.sctp.accept\_global\_ootb\_addip: 0

定义 `nat` 如何响应接收到全局 OOTB ASCONF-AddIP：

[`0`](#0)

无响应（除非存在部分匹配的关联 - 端口和 vtag 匹配但全局地址不匹配）

[`1`](#1)

`nat` 将接受并处理所有 OOTB 全局 AddIP 消息。

永远不应选择选项 1，因为这会构成安全风险。 攻击者可以通过发送 AddIP 消息建立多个虚假关联。

net.inet.ip.alias.sctp.chunk\_proc\_limit: 5

定义 SCTP 数据包中的最大块数，该数据包将被解析为与现有关联匹配的数据包。 此值强制大于或等于 `net.inet.ip.alias.sctp.initialising_chunk_proc_limit` 。 高值是 DoS 风险，但设置过低的值可能会导致无法定位和解析数据包中的重要控制块。

net.inet.ip.alias.sctp.error\_on\_ootb: 1

定义 `nat` 何时响应任何带有 ErrorM 数据包的 Out-of-the-Blue (OOTB) 数据包。 OOTB 数据包是到达时没有在 `nat` 中注册的现有关联的数据包，并且不是 INIT 或 ASCONF-AddIP 数据包：

[`0`](#0_2)

永远不会发送 ErrorM 以响应 OOTB 数据包。

[`1`](#1_2)

ErrorM 仅发送到本地接收到的 OOTB 数据包。

[`2`](#2)

仅当存在部分匹配（端口和 vtag 匹配但源全局 IP 不匹配）时，才会将 ErrorM 发送到本地端和全局端。 此值仅在 `nat` 跟踪全局 IP 地址时有用。

[`3`](#3)

发送 ErrorM 以响应本地和全局端的所有 OOTB 数据包（DoS 风险）。

目前默认值为 0，因为大多数 SCTP 堆栈尚不支持 ErrorM 数据包。 如果支持，并且如果不跟踪全局地址，我们建议将此值设置为 1 以允许多宿主本地主机与 `nat` 一起工作。 要跟踪全局地址，我们建议将此值设置为 2，以允许在需要（重新）发送 ASCONF-AddIP 时通知全局主机。 永远不应选择值 3（调试除外），因为 `nat` 将响应所有 OOTB 全局数据包（DoS 风险）。

net.inet.ip.alias.sctp.hashtable\_size: 2003

用于 `nat` 查找的哈希表大小 (100 < prime\_number > 1000001)。 此值设置任何未来创建的 `nat` 实例的 `hash table` 大小，因此必须在创建 `nat` 实例之前设置。 桌子的大小可以根据特定需要进行更改。 如果并发关联很少，并且内存稀缺，则可以将它们变小。 如果会有数千（或数百万）个并发关联，则应该使它们更大。 素数最适合表格大小。 sysctl 更新功能会将您的输入值调整为下一个最高质数。

net.inet.ip.alias.sctp.holddown\_time: 0

在收到 SHUTDOWN-COMPLETE 后，在表中保持关联这么多秒。 这允许端点在shutdown\_complete丢失并且需要重新传输时优雅地纠正关闭。

net.inet.ip.alias.sctp.init\_timer: 15

等待 (INIT-ACK|AddIP-ACK) 时的超时值。 此值不能为 0。

net.inet.ip.alias.sctp.initialising\_chunk\_proc\_limit: 2

定义当不存在与该数据包匹配的现有关联时将解析的 SCTP 数据包中的最大块数。 理想情况下，此数据包将只是一个 INIT 或 ASCONF-AddIP 数据包。 较高的值可能会成为 DoS 风险，因为格式错误的数据包会消耗处理资源。

net.inet.ip.alias.sctp.param\_proc\_limit: 25

定义将在数据包中解析的块内的最大参数数。 至于其他类似的 sysctl 变量，较大的值会带来 DoS 风险。

net.inet.ip.alias.sctp.log\_level: 0

系统日志消息中的详细级别（0 - 最小, 1 - 事件, 2 - 信息, 3 - 详细信息, 4 - 调试, 5 - 最大调试）。 May be a good 在高损耗环境中可能是一个不错的选择。

net.inet.ip.alias.sctp.shutdown\_time: 15

等待 SHUTDOWN-COMPLETE 时的超时值。此值不能为 0。

net.inet.ip.alias.sctp.track\_global\_addresses: 0

在 `nat` 中启用/禁用全局 IP 地址跟踪，并对每个关联跟踪的地址数量设置上限：

[`0`](#0_3)

全局跟踪已禁用

[`>1`](#_1)

启用跟踪，每个关联跟踪的最大地址数限制为该值

该变量是完全动态的，所有新到达的关联都将采用新值，现有关联将按以前的方式处理。 全局跟踪将减少 `nat` 内的冲突数量，但会增加处理负载、内存使用、复杂性以及在具有多个 `nat` 的复杂网络中可能出现的 `nats` 状态问题。 我们建议不要跟踪全球 IP 地址，这仍然会导致功能齐全的 `nat` 。

net.inet.ip.alias.sctp.up\_timer: 300

在没有流量的情况下保持关联的超时值。 此值不能为 0。

net.inet.ip.dummynet.codel.interval: 100000

默认 `codel` AQM 间隔（以微秒为单位）。 该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.codel.target: 5000

默认 `codel` AQM 目标延迟时间（以微秒为单位）（可接受的最小持久队列延迟）。 该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.expire: 1

一旦没有待处理的流量，就懒惰地删除动态管道/队列。 您可以通过将变量设置为 0 来禁用此功能，在这种情况下，只有在达到阈值时才会删除管道/队列。

net.inet.ip.dummynet.fqcodel.flows: 1024

定义 `fq_codel` 创建和管理的流队列（子队列）的默认总数。 该值必须在 1..65536 范围内。

net.inet.ip.dummynet.fqcodel.interval: 100000

默认 `fq_codel` 调度程序/AQM 间隔（以微秒为单位）。 该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.fqcodel.limit: 10240

由 `fq_codel` 调度程序实例管理的所有队列的默认硬大小限制（以数据包为单位）。 该值必须在 1..20480 范围内。

net.inet.ip.dummynet.fqcodel.quantum: 1514

[`fq_codel`](#fq_codel_2) 的默认量程（信用），以字节为单位。 该值必须在 1..9000 范围内。

net.inet.ip.dummynet.fqcodel.target: 5000

默认 `fq_codel` 调度程序/AQM 目标延迟时间，以微秒为单位（可接受的最小持久队列延迟）。 该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.fqpie.alpha: 125

[`fq_pie`](#fq_pie_2) 调度程序/AQM 的默认 alpha 参数（按 1000 缩放）。 该值必须在 1..7000 范围内。

net.inet.ip.dummynet.fqpie.beta: 1250

[`fq_pie`](#fq_pie_3) 调度程序/AQM 的默认 beta 参数（按 1000 缩放）。 该值必须在 1..7000 范围内。

net.inet.ip.dummynet.fqpie.flows: 1024

定义 `fq_pie` 创建和管理的流队列（子队列）的默认总数。 该值必须在 1..65536 范围内。

net.inet.ip.dummynet.fqpie.limit: 10240

由 `fq_pie` 调度程序实例管理的所有队列的默认硬大小限制（以数据包为单位）。 该值必须在 1..20480 范围内。

net.inet.ip.dummynet.fqpie.max\_burst: 150000

[`fq_pie`](#fq_pie_4) 调度程序/AQM 不丢弃/标记数据包的默认最大微秒周期。 该值必须在 1..10000000 范围内。

net.inet.ip.dummynet.fqpie.max\_ecnth: 99

[`fq_pie`](#fq_pie_5) 调度程序/AQM 的默认最大 ECN 概率阈值（按 1000 缩放）。 该值必须在 1..7000 范围内。

net.inet.ip.dummynet.fqpie.quantum: 1514

[`fq_pie`](#fq_pie_6) 的默认量程（信用），以字节为单位。 该值必须在 1..9000 范围内。

net.inet.ip.dummynet.fqpie.target: 15000

[`fq_pie`](#fq_pie_7) 的默认 `target` 延迟，以微秒为单位。 该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.fqpie.tupdate: 15000

[`fq_pie`](#fq_pie_8) 的默认 `tupdate` 以微秒为单位。 该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.hash\_size: 64

用于动态管道/队列的哈希表的默认大小。 在配置管道/队列时未指定 `buckets` 选项时使用此值。

net.inet.ip.dummynet.io\_fast: 0

如果设置为非零值，则启用 `dummynet` 操作的 “fast” 模式（见上文）。

net.inet.ip.dummynet.io\_pkt

传递到 `dummynet` 传递到

net.inet.ip.dummynet.io\_pkt\_drop

`dummynet` 丢弃的数据包数。

net.inet.ip.dummynet.io\_pkt\_fast

`dummynet` 调度程序绕过的数据包数。

net.inet.ip.dummynet.max\_chain\_len: 16

哈希桶中最大管道/队列数的目标值。 乘积 `max_chain_len*hash_size` 用于确定空管道/队列过期的阈值，即使 `net.inet.ip.dummynet.expire=0` 。

net.inet.ip.dummynet.red\_lookup\_depth: 256

net.inet.ip.dummynet.red\_avg\_pkt\_size: 512

net.inet.ip.dummynet.red\_max\_pkt\_size: 1500

用于计算 RED 算法的丢弃概率的参数。

net.inet.ip.dummynet.pie.alpha: 125

[`pie`](#pie_2) AQM 的默认 alpha 参数（按 1000 缩放）。该值必须在 1..7000 范围内。

net.inet.ip.dummynet.pie.beta: 1250

[`pie`](#pie_3) AQM 的默认 beta 参数（按 1000 缩放）。该值必须在 1..7000 范围内。

net.inet.ip.dummynet.pie.max\_burst: 150000

[`pie`](#pie_4) AQM 不丢弃/标记数据包的默认最大微秒周期。该值必须在 1..10000000 范围内。

net.inet.ip.dummynet.pie.max\_ecnth: 99

[`pie`](#pie_5) AQM 的默认最大 ECN 概率阈值（按 1000 缩放）。 该值必须在 1..7000 范围内。

net.inet.ip.dummynet.pie.target: 15000

[`pie`](#pie_6) AQM 的默认 `target` 延迟，以微秒为单位。该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.pie.tupdate: 15000

[`pie`](#pie_7) AQM 的默认 `tupdate` ，以微秒为单位。 该值必须在 1..5000000 范围内。

net.inet.ip.dummynet.pipe\_byte\_limit: 1048576

net.inet.ip.dummynet.pipe\_slot\_limit: 100

可以以字节或数据包为单位指定的最大队列大小。 这些限制可防止意外耗尽资源，例如 mbuf。 如果您提高这些限制，您应该确保系统配置为有足够的资源可用。

net.inet.ip.fw.autoinc\_step: 100

自动生成规则编号时的增量。 该值必须在 1..1000 范围内。

net.inet.ip.fw.curr\_dyn\_buckets: net.inet.ip.fw.dyn\_buckets

动态规则的哈希表中的当前桶数（只读）。

net.inet.ip.fw.debug: 1

控制 `ipfw` 产生的调试消息。

net.inet.ip.fw.default\_rule: 65535

默认规则编号（只读）。 根据 `ipfw` 的设计，默认规则是最后一条，所以它的编号也可以作为一个规则允许的最大编号。

net.inet.ip.fw.dyn\_buckets: 256

动态规则的哈希表中的桶数。必须是 2 的幂，最大为 65536。 它仅在所有动态规则都过期后才生效，因此建议您使用 `flush` 命令确保哈希表已调整大小。

net.inet.ip.fw.dyn\_count: 3

当前动态规则数（只读）。

net.inet.ip.fw.dyn\_keepalive: 1

启用为 TCP 会话上的 `keep-state` 规则生成保活数据包。 在规则生命周期的最后 20 秒内，每 5 秒向连接的两端生成一个 keepalive。

net.inet.ip.fw.dyn\_max: 8192

最大动态规则数。 当您达到此限制时，在旧规则过期之前无法安装更多动态规则。

net.inet.ip.fw.dyn\_ack\_lifetime: 300

net.inet.ip.fw.dyn\_syn\_lifetime: 20

net.inet.ip.fw.dyn\_fin\_lifetime: 1

net.inet.ip.fw.dyn\_rst\_lifetime: 1

net.inet.ip.fw.dyn\_udp\_lifetime: 5

net.inet.ip.fw.dyn\_short\_lifetime: 30

这些变量控制动态规则的生命周期（以秒为单位）。在初始 SYN 交换时，生命周期保持较短，然后在看到两个 SYN 后增加，然后在最终 FIN 交换期间或收到 RST 时再次减少。 _dyn\_fin\_lifetime_ 和 _dyn\_rst\_lifetime_ 都必须严格低于 5 秒，即 keepalive 的重复周期。 防火墙强制执行此操作。

net.inet.ip.fw.dyn\_keep\_states: 0

保持规则/集删除的动态状态。 状态重新链接到默认规则 (65535)。 这可以方便地重新加载规则集。

net.inet.ip.fw.enable: 1

启用防火墙。将此变量设置为 0 可以让您在没有防火墙的情况下运行您的机器，即使已编译进去。

net.inet6.ip6.fw.enable: 1

为 IPv6 案例提供与上述相同的功能。

net.inet.ip.fw.one\_pass: 1

设置后，从 `dummynet` 管道或 ng\_ipfw(4) 节点退出的数据包不会再次通过防火墙。 否则，在某个操作之后，数据包会在下一条规则处重新注入防火墙。

net.inet.ip.fw.tables\_max: 128

最大表数。

net.inet.ip.fw.verbose: 1

启用详细消息。

net.inet.ip.fw.verbose\_limit: 0

限制详细防火墙生成的消息数量。

net.inet6.ip6.fw.deny\_unknown\_exthdrs: 1

如果启用了带有未知 IPv6 扩展标头的数据包，将被拒绝。

net.link.ether.ipfw: 0

控制是否将第 2 层数据包传递给 `ipfw` 。默认为否。

net.link.bridge.ipfw: 0

控制是否将桥接数据包传递给 `ipfw` 。默认为否。

net.inet.ip.fw.nat64\_debug: 0

控制 `ipfw_nat64` 模块产生的调试消息。

net.inet.ip.fw.nat64\_direct\_output: 0

控制 `ipfw_nat64` 模块使用的输出方法：

[`0`](#0_4)

一个数据包由 `ipfw` 处理两次。 第一次原始数据包由 `ipfw` 处理并由 `ipfw_nat64` 转换器使用。 然后翻译后的数据包通过 netisr 排队再次输入处理。

[`1`](#1_3)

一个数据包只被 `ipfw` 处理一次，翻译后直接推送到出接口。

[内部诊断](#__u5185___u90E8___u8BCA___u65AD__2)
===========================================

有一些命令可能有助于了解内核模块中某些子系统的当前状态。 这些命令提供调试输出，可能会更改，恕不另行通知。

目前，以下命令可用作 `internal` 子选项：

[`iflist`](#iflist)

列出当前由 `ipfw` 跟踪的所有接口及其内核状态。

[`talist`](#talist)

列出当前可用的所有查表算法。

[实例](#__u5B9E___u4F8B_)
=======================

`ipfw` 有太多可能的用途，因此本节将仅提供一小部分示例。

[基本包过滤](#__u57FA___u672C___u5305___u8FC7___u6EE4_)
--------------------------------------------------

此命令添加一个条目，该条目拒绝从 _cracker.evil.org_ 到 _wolf.tambov.su_ 的 telnet 端口的所有 tcp 数据包被主机转发：

`ipfw add deny tcp from cracker.evil.org to wolf.tambov.su telnet`

这个不允许从整个破解者的网络到我的主机的任何连接：

`ipfw add deny ip from 123.45.67.0/24 to my.host.org`

限制访问（不使用动态规则）的第一种有效方法是使用以下规则：

`ipfw add allow tcp from any to any established`

`ipfw add allow tcp from net1 portlist1 to net2 portlist2 setup`

`ipfw add allow tcp from net3 portlist3 to net3 portlist3 setup`

`...`

`ipfw add deny tcp from any to any`

第一条规则将是普通 TCP 数据包的快速匹配，但它不会匹配初始 SYN 数据包， `setup` 规则将仅匹配选定的源/目标对。 所有其他 SYN 数据包将被最终 `deny` 规则拒绝。

如果您管理一个或多个子网，您可以利用地址集和或块并编写极其紧凑的规则集，这些规则集可以选择性地为客户端块启用服务，如下所示：

`goodguys="{ 10.1.2.0/24{20,35,66,18} or 10.2.3.0/28{6,3,11} }"`

`badguys="10.1.2.0/24{8,38,60}"`

`ipfw add allow ip from ${goodguys} to any`

`ipfw add deny ip from ${badguys} to any`

`... normal policies ...`

通过将以下内容添加到规则集的顶部， `verrevpath` 选项可用于执行自动反欺骗：

`ipfw add deny ip from any to any not verrevpath in`

此规则会丢弃所有似乎在错误接口上进入系统的传入数据包。 例如，如果数据包试图从外部接口进入系统，其源地址属于受保护的内部网络上的主机，则会被丢弃。

通过将以下内容添加到规则集的顶部，可以使用 `antispoof` 选项来执行类似但更受限制的反欺骗：

`ipfw add deny ip from any to any not antispoof in`

此规则丢弃所有看似来自另一个直接连接的系统但在错误接口上的传入数据包。 例如，源地址为 `192.168.0.0/24` 、在 `fxp0` 上配置但在 `fxp1` 上进入的数据包将被丢弃。

`setdscp` 选项可用于（重新）标记用户流量，方法是将以下内容添加到规则集中的适当位置：

`ipfw add setdscp be ip from any to any dscp af11,af21`

[选择性镜像](#__u9009___u62E9___u6027___u955C___u50CF_)
--------------------------------------------------

如果您的网络有网络流量分析器通过专用接口直接连接到您的主机或通过 RSPAN vlan 远程连接，您可以选择性地将一些以太网 layer2 帧镜像到分析器。

首先，确保您的防火墙已经配置并运行。 然后，如果尚未启用，则启用 layer2 处理：

`sysctl net.link.ether.ipfw=1`

接下来，加载所需的额外内核模块：

`kldload ng_ether ng_ipfw`

或者，使系统在启动时自动加载这些模块：

`sysrc kld_list+="ng_ether ng_ipfw"`

接下来，配置 ng\_ipfw(4) 内核模块以通过 vlan900 接口将 layer2 帧的镜像副本传输出去：

`ngctl connect ipfw: vlan900: 1 lower`

将此处的 "1" 视为 "mirroring instance index" ，vlan900 是其目的地。 您可以拥有任意数量的实例。 有关详细信息，请参阅 ng\_ipfw(4) 。

最后，使用 "instance 1" 实际开始对选定帧进行镜像。对于从 em0 接口传入的帧：

`ipfw add ngtee 1 ip from any to 192.168.0.1 layer2 in recv em0`

对于传出到 em0 接口的帧：

`ipfw add ngtee 1 ip from any to 192.168.0.1 layer2 out xmit em0`

对于流经 em0 的传入和传出帧：

`ipfw add ngtee 1 ip from any to 192.168.0.1 layer2 via em0`

确保您不对已经复制的帧执行镜像，否则内核可能会因为没有安全网而挂起。

[动态规则](#__u52A8___u6001___u89C4___u5219_)
-----------------------------------------

为了保护站点免受涉及虚假 TCP 数据包的洪水攻击，使用动态规则更安全：

`ipfw add check-state`

`ipfw add deny tcp from any to any established`

`ipfw add allow tcp from my-net to any setup keep-state`

这将让防火墙只为那些以来自我们网络内部的常规 SYN 数据包开始的连接安装动态规则。 当遇到第一次出现的 `check-state`, `keep-state` 或 `limit` 规则时，会检查动态规则。 `check-state` 规则通常应该放在规则集的开头附近，以尽量减少扫描规则集的工作量。 你的旅费可能会改变。

对于具有动态规则的更复杂的场景， `record-state` 和 `defer-action` 可用于精确控制动态规则的创建和检查。 [NETWORK ADDRESS TRANSLATION (NAT)](#NETWORK_ADDRESS_TRANSLATION_(NAT)) 部分提供了这些选项的使用示例。

要限制用户可以打开的连接数，您可以使用以下类型的规则：

`ipfw add allow tcp from my-net/24 to any setup limit src-addr 10`

`ipfw add allow tcp from any to me setup limit src-addr 4`

前者（假设它在网关上运行）将允许 /24 网络上的每个主机最多打开 10 个 TCP 连接。 后者可以放置在服务器上，以确保单个客户端不使用超过 4 个同时连接。

_BEWARE_: 有状态规则可能会受到 SYN 洪水的拒绝服务攻击，这会打开大量动态规则。 通过作用于一组控制防火墙操作的 sysctl(8) 变量，可以部分限制此类攻击的影响。

下面是一个很好的使用 `list` 命令查看记帐记录和时间戳信息的方法：

`ipfw -at list`

或没有时间戳的简短形式：

`ipfw -a list`

这相当于：

`ipfw show`

下一条规则将所有来自 192.168.2.0/24 的传入数据包转移到转移端口 5000：

`ipfw divert 5000 ip from 192.168.2.0/24 to any in`

[流量塑造](#__u6D41___u91CF___u5851___u9020_)
-----------------------------------------

以下规则展示了 `ipfw` 和 `dummynet` 用于模拟等的一些应用。

此规则以 5% 的概率丢弃随机传入的数据包：

`ipfw add prob 0.05 deny ip from any to any in`

使用 `dummynet` 管道可以实现类似的效果：

`ipfw add pipe 10 ip from any to any`

`ipfw pipe 10 config plr 0.05`

我们可以使用管道人为地限制带宽，例如在充当路由器的机器上，如果我们想限制来自 192.168.2.0/24 上本地客户端的流量，我们可以这样做：

`ipfw add pipe 1 ip from 192.168.2.0/24 to any out`

`ipfw pipe 1 config bw 300Kbit/s queue 50KBytes`

请注意，我们使用了 `out` 修饰符，因此该规则不会被使用两次。 事实上，请记住， `ipfw` 规则会在传入和传出数据包上进行检查。

如果我们想模拟一个有带宽限制的双向链路，正确的方法如下：

`ipfw add pipe 1 ip from any to any out`

`ipfw add pipe 2 ip from any to any in`

`ipfw pipe 1 config bw 64Kbit/s queue 10Kbytes`

`ipfw pipe 2 config bw 64Kbit/s queue 10Kbytes`

以上可能非常有用，例如，如果您想查看您的精美网页将如何查找仅通过慢速链接连接的住宅用户。 除非您想模拟半双工介质（例如 AppleTalk、以太网、IRDA），否则不应在两个方向上只使用一个管道。 两个管道不必具有相同的配置，因此我们也可以模拟非对称链接。

我们是否要使用 RED 队列管理算法来验证网络性能：

`ipfw add pipe 1 ip from any to any`

`ipfw pipe 1 config bw 500Kbit/s queue 100 red 0.002/30/80/0.1`

流量整形器的另一个典型应用是在通信中引入一些延迟。 这会显着影响执行大量远程过程调用的应用程序，并且连接的往返时间通常成为比带宽更重要的限制因素：

`ipfw add pipe 1 ip from any to any out`

`ipfw add pipe 2 ip from any to any in`

`ipfw pipe 1 config delay 250ms bw 1Mbit/s`

`ipfw pipe 2 config delay 250ms bw 1Mbit/s`

按流排队可用于多种目的。 一个非常简单的方法是计算流量：

`ipfw add pipe 1 tcp from any to any`

`ipfw add pipe 1 udp from any to any`

`ipfw add pipe 1 ip from any to any`

`ipfw pipe 1 config mask all`

上述规则集将为所有流量创建队列（并收集统计信息）。 因为管道没有限制，唯一的作用就是收集统计数据。 请注意，我们需要 3 条规则，而不仅仅是最后一条，因为当 `ipfw` 尝试匹配 IP 数据包时，它不会考虑端口，因此我们不会将不同端口上的连接视为不同的连接。

一个更复杂的示例是使用每个主机限制而不是每个网络限制来限制网络上的出站流量：

`ipfw add pipe 1 ip from 192.168.2.0/24 to any out`

`ipfw add pipe 2 ip from any to 192.168.2.0/24 in`

`ipfw pipe 1 config mask src-ip 0x000000ff bw 200Kbit/s queue 20Kbytes`

`ipfw pipe 2 config mask dst-ip 0x000000ff bw 200Kbit/s queue 20Kbytes`

[查找表](#__u67E5___u627E___u8868__3)
----------------------------------

在下面的示例中，我们需要创建多个流量带宽类，并且我们需要不同的主机/网络属于不同的类。 我们为每个类创建一个管道并相应地配置它们。 然后我们创建一个表并用 IP 子网和地址填充它。 对于每个子网/主机，我们将参数设置为它应该使用的管道数。 然后我们使用单个规则对流量进行分类：

`ipfw pipe 1 config bw 1000Kbyte/s`

`ipfw pipe 4 config bw 4000Kbyte/s`

`...`

`ipfw table T1 create type addr`

`ipfw table T1 add 192.168.2.0/24 1`

`ipfw table T1 add 192.168.0.0/27 4`

`ipfw table T1 add 192.168.0.2 1`

`...`

`ipfw add pipe tablearg ip from 'table(T1)' to any`

使用 `fwd` 操作，表条目可能包括主机名和 IP 地址。

`ipfw table T2 create type addr ftype ip`

`ipfw table T2 add 192.168.2.0/24 10.23.2.1`

`ipfw table T21 add 192.168.0.0/27 router1.dmz`

`...`

`ipfw add 100 fwd tablearg ip from any to table(1)`

在以下示例中，创建了每个接口的防火墙：

`ipfw table IN create type iface valtype skipto,fib`

`ipfw table IN add vlan20 12000,12`

`ipfw table IN add vlan30 13000,13`

`ipfw table OUT create type iface valtype skipto`

`ipfw table OUT add vlan20 22000`

`ipfw table OUT add vlan30 23000`

`..`

`ipfw add 100 setfib tablearg ip from any to any recv 'table(IN)' in`

`ipfw add 200 skipto tablearg ip from any to any recv 'table(IN)' in`

`ipfw add 300 skipto tablearg ip from any to any xmit 'table(OUT)' out`

以下示例说明了流表的用法：

`ipfw table fl create type flow:src-ip,proto,dst-ip,dst-port`

`ipfw table fl add 2a02:6b8:77::88,tcp,2a02:6b8:77::99,80 11`

`ipfw table fl add 10.0.0.1,udp,10.0.0.2,53 12`

`..`

`ipfw add 100 allow ip from any to any flow 'table(fl,11)' recv ix0`

[规则集](#__u89C4___u5219___u96C6__2)
----------------------------------

以原子方式添加一组规则，例如设置 18：

`ipfw set disable 18`

`ipfw add NN set 18 ... # repeat as needed`

`ipfw set enable 18`

要以原子方式删除一组规则，命令很简单：

`ipfw delete set 18`

测试规则集并禁用它并在出现问题时重新获得控制：

`ipfw set disable 18`

`ipfw add NN set 18 ... # repeat as needed`

`ipfw set enable 18; echo done; sleep 30 && ipfw set disable 18`

在这里，如果一切顺利，您在 "sleep" 终止之前按 control-C，您的规则集将保持活动状态。 否则，例如，如果您无法访问您的盒子，则在睡眠终止后规则集将被禁用，从而恢复以前的情况。

显示特定集合的规则：

`ipfw set 18 show`

要显示禁用集的规则：

`ipfw -S set 18 show`

清除特定集合的特定规则计数器：

`ipfw set 18 zero NN`

要删除特定集的特定规则：

`ipfw set 18 delete NN`

[NAT、重定向和 LSNAT](#NAT__u3001___u91CD___u5B9A___u5411___u548C__LSNAT)
--------------------------------------------------------------------

首先将所有流量重定向到 nat 实例 123：

`ipfw add nat 123 all from any to any`

然后将 nat 实例 123 配置为使用 ip 192.168.0.123 对所有传出流量进行别名，阻止所有传入连接，尝试在两侧保持相同的端口，清除地址更改的别名表并记录流量/链接统计信息：

`ipfw nat 123 config ip 192.168.0.123 log deny_in reset same_ports`

或者要更改实例 123 的地址，别名表将被清除（参见重置选项）：

`ipfw nat 123 config ip 10.0.0.1`

查看 nat 实例 123 的配置：

`ipfw nat 123 show config`

要显示 111-999 范围内所有实例的日志：

`ipfw nat 111-999 show`

查看所有实例的配置：

`ipfw nat show config`

或者具有混合模式的重定向规则可能如下所示：

ipfw nat 123 config redirect\_addr 10.0.0.1 10.0.0.66 redirect\_port tcp 192.168.0.1:80 500 redirect\_proto udp 192.168.1.43 192.168.1.1 redirect\_addr 192.168.0.10,192.168.0.11 10.0.0.100 # LSNAT redirect\_port tcp 192.168.0.1:80,192.168.0.10:22 500 # LSNAT 

或者它可以分为：

ipfw nat 1 config redirect\_addr 10.0.0.1 10.0.0.66 ipfw nat 2 config redirect\_port tcp 192.168.0.1:80 500 ipfw nat 3 config redirect\_proto udp 192.168.1.43 192.168.1.1 ipfw nat 4 config redirect\_addr 192.168.0.10,192.168.0.11,192.168.0.12 10.0.0.100 ipfw nat 5 config redirect\_port tcp 192.168.0.1:80,192.168.0.10:22,192.168.0.20:25 500 

有时您可能希望混合使用 NAT 和动态规则。它可以通过 `record-state` 和 `defer-action` 选项来实现。 问题是，您需要在 NAT 之前创建动态规则，并在 NAT 操作之后检查它（反之亦然），以获得一致的地址和端口。 带有 `keep-state` 选项的规则将触发现有动态状态的激活，并且一旦规则匹配，就会执行该规则的动作。 如果是 NAT 并且 `allow` 规则数据包需要传递给 NAT，可以尽快不允许。

有一组规则可以实现这一点。 请记住，这只是示例，它本身并不是很有用。

在出路时，所有检查都放置以下规则：

`ipfw add allow record-state skip-action`

`ipfw add nat 1`

在进去的路上应该有这样的东西：

`ipfw add nat 1`

`ipfw add check-state`

请注意，退出的第一条规则不允许数据包并且不执行现有的动态规则。 它所做的一切，如果尚未创建，则使用 `allow` 操作创建新的动态规则。 后来，这个动态规则被 `check-state` 规则使用。

[配置 CODEL、PIE、FQ-CODEL 和 FQ-PIE AQM](#__u914D___u7F6E__CODEL__u3001_PIE__u3001_FQ_CODEL___u548C__FQ_PIE_AQM)
------------------------------------------------------------------------------------------------------------

`codel` 和 `pie` AQM 可以配置为 `dummynet` `pipe` 或 `queue` 。

要使用来自 192.168.0.0/24 的流量和 1Mbits/s 速率限制的默认配置来配置具有 `codel` AQM 的 `pipe` ，我们执行以下操作：

`ipfw pipe 1 config bw 1mbits/s codel`

`ipfw add 100 pipe 1 ip from 192.168.0.0/24 to any`

要使用来自 192.168.0.0/24 的流量和 1Mbits/s 速率限制的不同配置参数来配置带有 `codel` AQM 的 `queue` ，我们这样做：

`ipfw pipe 1 config bw 1mbits/s`

`ipfw queue 1 config pipe 1 codel target 8ms interval 160ms ecn`

`ipfw add 100 queue 1 ip from 192.168.0.0/24 to any`

要使用来自 192.168.0.0/24 的流量和 1Mbits/s 速率限制的默认配置来配置具有 `pie` AQM 的 `pipe` ，我们执行以下操作：

`ipfw pipe 1 config bw 1mbits/s pie`

`ipfw add 100 pipe 1 ip from 192.168.0.0/24 to any`

要使用 192.168.0.0/24 的流量和 1Mbits/s 速率限制的不同配置参数来配置带有 `pie`-
AQM 的 `queue` ，我们这样做：

`ipfw pipe 1 config bw 1mbits/s`

`ipfw queue 1 config pipe 1 pie target 20ms tupdate 30ms ecn`

`ipfw add 100 queue 1 ip from 192.168.0.0/24 to any`

可以为 `dummynet` 调度程序配置 `fq_codel` 和 `fq_pie` 。

要使用来自 192.168.0.0/24 的流量和 1Mbits/s 速率限制的不同配置参数来配置 `fq_codel` 调度程序，我们这样做：

`ipfw pipe 1 config bw 1mbits/s`

`ipfw sched 1 config pipe 1 type fq_codel`

`ipfw queue 1 config sched 1`

`ipfw add 100 queue 1 ip from 192.168.0.0/24 to any`

要更改 `sched` 的 `fq_codel` 默认配置，例如禁用 ECN 并将 target 更改为 10ms，我们执行以下操作：

`ipfw sched 1 config pipe 1 type fq_codel target 10ms noecn`

与 `fq_codel`-
类似，要使用来自 192.168.0.0/24 的流量和 1Mbits/s 速率限制的不同配置参数来配置 `fq_pie` 调度程序，我们这样做：

`ipfw pipe 1 config bw 1mbits/s`

`ipfw sched 1 config pipe 1 type fq_pie`

`ipfw queue 1 config sched 1`

`ipfw add 100 queue 1 ip from 192.168.0.0/24 to any`

`fq_pie` `sched` 的配置可以通过与 `fq_codel` 类似的方式进行更改

[参见](#__u53C2___u89C1_)
=======================

cpp(1), m4(1), altq(4), divert(4), dummynet(4), if\_bridge(4), ip(4), ipfirewall(4), ng\_ether(4), ng\_ipfw(4), protocols(5), services(5), init(8), kldload(8), reboot(8), sysctl(8), syslogd(8), sysrc(8)

[历史](#__u5386___u53F2_)
=======================

`ipfw` 实用程序首先出现在 FreeBSD 2.0 中。 `dummynet` 是在 FreeBSD 2.2.8 中引入的。 在 FreeBSD 4.0 中引入了有状态的扩展。 `ipfw2` 于 2002 年夏季推出。

[作者](#__u4F5C___u8005_)
=======================

Ugen J. S. Antsilevich, Poul-Henning Kamp, Alex Nash, Archie Cobbs, Luigi Rizzo, Rasool Al-Saadi.

API 基于 Daniel Boulet 为 BSDI 编写的代码。

Dummynet 由 Luigi Rizzo 在 1997-1998 年推出。

Akamba 公司支持的 `dummynet` 流量整形器的一些早期工作（1999-2000 年）。

Luigi Rizzo 在 2002 年夏天对 ipfw 核心 (ipfw2) 进行了完全重新设计和重新实现。 多年来，各种开发人员添加了进一步的操作和选项。

Paolo Pisati <[piso@FreeBSD.org](mailto:piso@FreeBSD.org)\> 作为 Summer of Code 2005 项目的一部分编写的内核内 NAT 支持。

SCTP `nat` 支持由 The Centre for Advanced Internet Architectures (CAIA) ⟨http://www.caia.swin.edu.au⟩ 开发。 主要的开发人员和维护人员是 David Hayes 和 Jason But。 欲了解更多信息，请访问： ⟨http://www.caia.swin.edu.au/urp/SONATA⟩

Alessandro Cerri 和 Luigi Rizzo 在欧盟委员会 Onelab 和 Onelab2 项目的支持下开发了延迟配置文件。

CoDel、PIE、FQ-CoDel 和 FQ-PIE AQM for Dummynet 已于 2016 年由 The Centre for Advanced Internet Architectures (CAIA) 在康卡斯特创新基金的支持下实施。 主要开发商是 Rasool Al-Saadi。

[缺陷](#__u7F3A___u9677_)
=======================

语法多年来一直在增长，有时可能会令人困惑。 不幸的是，向后兼容性阻止了清理语法定义中的错误。

_!!! WARNING !!!_

错误配置防火墙会使您的计算机处于无法使用的状态，可能会关闭网络服务并需要控制台访问才能重新控制它。

被 `divert` 转移的传入数据包片段在传递到套接字之前被重新组装。 对这些数据包使用的操作是与数据包的第一个片段匹配的规则中的操作。

被转移到用户态，然后由用户态进程重新插入的数据包可能会丢失各种数据包属性。 如果包源接口名称短于 8 个字节，并且用户态进程保存并重用 sockaddr\_in（与 natd(8) 一样），则将保留数据包源接口名称；否则，它可能会丢失。 如果以这种方式重新插入数据包，则可能会错误地应用后面的规则，从而使规则序列中的 `divert` 规则的顺序非常重要。

Dummynet 丢弃所有具有 IPv6 链路本地地址的数据包。

使用 `uid` 或 `gid` 的规则可能无法按预期运行。 特别是，传入的 SYN 数据包可能没有与之关联的 uid 或 gid，因为它们尚不属于 TCP 连接，如果相关进程调用 setuid(2) 或类似的系统调用。

规则语法受命令行环境的影响，某些模式可能需要使用反斜杠字符进行转义或适当地引用。

由于 libalias(3) 的架构，ipfw nat 与 TCP 分段卸载 (TSO) 不兼容。 因此，为了可靠地 nat 您的网络流量，请使用 ifconfig(8) 在您的 NIC 上禁用 TSO。

ICMP 错误消息不会被相应对话的动态规则隐式匹配。 为了避免网络错误检测和路径MTU 发现失败，可能需要通过静态规则明确允许 ICMP 错误消息。

如果规则集有错误和/或使用与其他子系统（网络图、虚拟网络等）的交互，则使用 `call` 和 `return` 操作的规则可能会导致令人困惑的行为。 一种可能的情况是数据包在输入过程中将 `ipfw` 留在子程序中，而稍后在输出中首先遇到不成对的 `return` 。 由于调用堆栈在输入传递后保持不变，数据包将突然返回输入传递使用的规则编号，而不是输出一。 应仔细检查处理顺序以避免此类错误。

August 21, 2020

FreeBSD 13.1-RELEASE