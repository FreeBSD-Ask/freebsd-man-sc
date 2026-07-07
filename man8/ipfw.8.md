# ipfw(8)

`ipfw` — 防火墙、流量整形器、包调度器和内核内 NAT 的用户界面

## 名称

`ipfw`, `dnctl`

## 概要

### 防火墙配置（FIREWALL CONFIGURATION）

`ipfw [-cq] add rule`

`ipfw [-acdefnNStT] [set N] {list | show} [rule | first-last ...]`

`ipfw [-f | -q] [set N] flush`

`ipfw [-q] [set N] {delete | zero | resetlog} [number ...]`

`ipfw set [disable number ...] [enable number ...]`

`ipfw set move [rule] number to number`

`ipfw set swap number number`

`ipfw set show`

### SYSCTL 快捷方式

`ipfw enable {firewall | altq | one_pass | debug | verbose | dyn_keepalive | skipto_cache}`

`ipfw disable {firewall | altq | one_pass | debug | verbose | dyn_keepalive | skipto_cache}`

### 查找表（LOOKUP TABLES）

`ipfw [set N] table name create create-options`

`ipfw [set N] table {name | all} destroy`

`ipfw [set N] table name modify modify-options`

`ipfw [set N] table name swap name`

`ipfw [set N] table name add table-key [value]`

`ipfw [set N] table name add [table-key value ...]`

`ipfw [set N] table name atomic add [table-key value ...]`

`ipfw [set N] table name delete [table-key ...]`

`ipfw [set N] table name lookup addr`

`ipfw [set N] table name lock`

`ipfw [set N] table name unlock`

`ipfw [set N] table {name | all} list`

`ipfw [set N] table {name | all} info`

`ipfw [set N] table {name | all} detail`

`ipfw [set N] table {name | all} flush`

### DUMMYNET 配置（流量整形器和包调度器）

`dnctl {pipe | queue | sched} number config config-options`

`dnctl [-s [field]] {pipe | queue | sched} {delete | list | show} [number ...]`

### 内核内 NAT

`ipfw [-q] nat number config config-options`

`ipfw [-q] nat number delete`

`ipfw nat number show {config | log}`

### 有状态 IPv6/IPv4 网络地址和协议转换

`ipfw [set N] nat64lsn name create create-options`

`ipfw [set N] nat64lsn name config config-options`

`ipfw [set N] nat64lsn {name | all} {list | show} [states]`

`ipfw [set N] nat64lsn {name | all} destroy`

`ipfw [set N] nat64lsn name stats [reset]`

### 无状态 IPv6/IPv4 网络地址和协议转换

`ipfw [set N] nat64stl name create create-options`

`ipfw [set N] nat64stl name config config-options`

`ipfw [set N] nat64stl {name | all} {list | show}`

`ipfw [set N] nat64stl {name | all} destroy`

`ipfw [set N] nat64stl name stats [reset]`

### XLAT464 CLAT IPv6/IPv4 网络地址和协议转换

`ipfw [set N] nat64clat name create create-options`

`ipfw [set N] nat64clat name config config-options`

`ipfw [set N] nat64clat {name | all} {list | show}`

`ipfw [set N] nat64clat {name | all} destroy`

`ipfw [set N] nat64clat name stats [reset]`

### IPv6 到 IPv6 网络前缀转换

`ipfw [set N] nptv6 name create create-options`

`ipfw [set N] nptv6 {name | all} {list | show}`

`ipfw [set N] nptv6 {name | all} destroy`

`ipfw [set N] nptv6 name stats [reset]`

### 内部诊断

`ipfw internal iflist`

`ipfw internal monitor [filter-comment]`

`ipfw internal talist`

`ipfw internal vlist`

### 规则列表与预处理

`ipfw [-cfnNqS] [-p preproc [preproc-flags]] pathname`

## 描述

`ipfw` 工具是用于控制 ipfw(4) 防火墙、dummynet(4) 流量整形器/包调度器以及内核内 NAT 服务的用户界面。

防火墙配置（或称 *ruleset*，规则集）由从 1 到 65535 编号的 *规则* 列表组成。数据包从协议栈中多个不同的位置传递给防火墙（取决于数据包的源和目的，同一数据包可能会被多次传递给防火墙）。传递给防火墙的数据包会按规则编号顺序与 *规则集* 中的每条规则进行比较（允许存在多条具有相同编号的规则，此时它们按插入顺序处理）。当找到匹配项时，执行与匹配规则对应的动作。

根据动作和某些系统设置，数据包可以在匹配规则之后的某条规则处重新注入防火墙进行进一步处理。

规则集始终包含一条 *default*（默认）规则（编号 65535），该规则无法修改或删除，并匹配所有数据包。与 *default* 规则关联的动作可以是 `deny` 或 `allow`，具体取决于内核的配置方式。

如果规则集包含一条或多条带有 `keep-state`、`record-state`、`limit` 或 `set-limit` 选项的规则，防火墙将具有 *有状态*（stateful）行为，即在匹配时会创建 *动态规则*（dynamic rules），这些规则匹配与触发其创建的数据包具有相同 5 元组（协议、源和目的地址及端口）的数据包。动态规则具有有限的生存期，在第一次出现 `check-state`、`keep-state` 或 `limit` 规则时进行检查，通常用于按需为合法流量打开防火墙。请注意，`keep-state` 和 `limit` 对所有数据包（不仅是被该规则匹配的数据包）隐含 `check-state`，但 `record-state` 和 `set-limit` 没有隐含的 `check-state`。有关 `ipfw` 有状态行为的更多信息，请参见下面的"有状态防火墙"（STATEFUL FIREWALL）和"实例"（EXAMPLES）章节。

所有规则（包括动态规则）都有一些关联的计数器：数据包计数、字节计数、日志计数以及指示上次匹配时间的时间戳。计数器可以通过 `ipfw` 命令显示或重置。

每条规则属于 32 个不同 *集合*（sets）之一，并且有 `ipfw` 命令可以原子地操作集合，例如启用、禁用、交换集合、将一个集合中的所有规则移动到另一个集合、删除一个集合中的所有规则。这些功能可用于安装临时配置或进行测试。有关 *集合* 的更多信息，请参见"规则集合"（SETS OF RULES）章节。

可以使用 `add` 命令添加规则；使用 `delete` 命令单独或分组删除；使用 `flush` 命令全局删除（set 31 中的除外）；使用 `show` 和 `list` 命令显示（可选地包含计数器内容）。最后，可以使用 `zero` 和 `resetlog` 命令重置计数器。

### 命令选项

调用 `ipfw` 时可使用以下通用选项：

**`-a`** 列出规则时显示计数器值。`show` 命令隐含此选项。

**`-b`** 仅显示动作和注释，不显示规则体。隐含 `-c`。

**`-c`** 输入或显示规则时，以紧凑形式打印，即在不携带任何额外信息时省略 "ip from any to any" 字符串。

**`-d`** 列表时，除静态规则外还显示动态规则。

**`-D`** 列表时仅显示动态状态。删除时仅删除动态状态。

**`-f`** 对于误用可能导致问题的命令（如 `flush`），运行时不提示确认。如果进程没有关联的 tty，则隐含此选项。带有此标志的 `delete` 命令会忽略可能的错误（如不存在的规则编号）。对于批量命令执行，会继续执行下一条命令。

**`-i`** 列出查找表时（有关查找表的更多信息，请参见下面的"查找表"章节），将值格式化为 IP 地址。默认情况下，值以整数显示。

**`-n`** 仅检查命令字符串的语法，而不实际将其传递给内核。

**`-N`** 尝试在输出中解析地址和服务名称。

**`-q`** 在执行 `add`、`nat`、`zero`、`resetlog` 或 `flush` 命令时保持安静；（隐含 `-f`）。在通过脚本（例如 `sh /etc/rc.firewall`）执行多个 `ipfw` 命令来更新规则集，或通过远程登录会话处理包含许多 `ipfw` 规则的文件时非常有用。它还能防止表添加或删除在条目已存在或不存在时失败。此选项可能重要的原因是，对于其中某些操作，`ipfw` 可能会打印消息；如果该操作导致到远程客户端的流量被阻断，远程登录会话将被关闭，规则集的其余部分将不会被处理。此时需要控制台访问权限来恢复。

**`-S`** 列出规则时，显示每条规则所属的 *集合*。如果未指定此标志，已禁用的规则不会被列出。

**`-s`** [`field`] 列出 pipe 时，根据四个计数器之一（总数据包数或当前数据包数、字节数）排序。

**`-t`** 列表时，显示由 `ctime()` 转换的上次匹配时间戳。

**`-T`** 列表时，将上次匹配时间戳显示为自纪元以来的秒数。这种形式对于脚本后处理可能更方便。

### 规则列表与预处理

为简化配置，可以将规则放入文件中，使用 `ipfw` 按概要最后一行所示进行处理。必须使用绝对 `pathname`。文件将逐行读取并作为参数应用到 `ipfw` 工具。

可以选择使用 `-p` `preproc` 指定预处理器，`pathname` 将通过该预处理器进行管道处理。有用的预处理器包括 cpp(1) 和 m4(1)。如果 `preproc` 不以斜杠（`/`）作为第一个字符，则执行通常的 `PATH` 名称搜索。在并非所有文件系统都（尚未）挂载的环境中使用此功能时应谨慎（例如，当它们通过 NFS 挂载时）。一旦指定了 `-p`，任何附加参数都会传递给预处理器进行解释。这允许灵活的配置文件（如根据本地主机名进行条件化）以及使用宏来集中常用参数（如 IP 地址）。

### 流量整形器配置

`ipfw` 的 `pipe`、`queue` 和 `sched` 命令用于配置流量整形器和包调度器。有关详细信息，请参见下面的"流量整形器（DUMMYNET）配置"章节。

如果用户空间和内核不同步，`ipfw` 的 ABI 可能会中断，导致无法添加任何规则。这可能会对启动过程产生不利影响。可以使用 `ipfw` `disable` `firewall` 临时禁用防火墙以重新获得网络访问权限，从而修复问题。

## 数据包流（PACKET FLOW）

数据包在协议栈的多个位置根据活动规则集进行检查，这些位置受多个 sysctl 变量控制。这些位置和变量如下所示，了解这一点对于设计正确的规则集非常重要。

```sh
       ^    到上层    V
       |                       |
       +----------->-----------+
       ^                       V
 [ip(6)_input]           [ip(6)_output]     net.inet(6).ip(6).fw.enable=1
       |                       |
       ^                       V
 [ether_demux]        [ether_output_frame]  net.link.ether.ipfw=1
       |                       |
       +-->--[bdg_forward]-->--+            net.link.bridge.ipfw=1
       ^                       V
       |      到设备       |
```

同一数据包通过防火墙的次数在 0 到 4 之间变化，具体取决于数据包的源和目的以及系统配置。

请注意，随着数据包流经协议栈，头部可能会被剥离或添加，因此它们可能可用于检查，也可能不可用。例如，当从 `ether_demux()` 调用 `ipfw` 时，传入的数据包将包含 MAC 头部，但当从 `ip_input()` 或 `ip6_input()` 调用 `ipfw` 时，同一数据包的 MAC 头部将被剥离。

另请注意，每个数据包始终会根据完整的规则集进行检查，无论检查发生在何处或数据包的来源如何。如果规则包含对调用位置无效的某些匹配模式或动作（例如，尝试在 `ip_input` 或 `ip6_input` 中匹配 MAC 头部），则匹配模式将不匹配，但此类模式前面的 `not` 运算符 *将* 导致该模式在这些数据包上 *始终* 匹配。因此，如有必要，程序员有责任编写合适的规则集来区分可能的位置。`skipto` 规则在此处可能很有用，例如：

```sh
# 来自 ether_demux 或 bdg_forward 的数据包
ipfw add 10 skipto 1000 all from any to any layer2 in
# 来自 ip_input 的数据包
ipfw add 10 skipto 2000 all from any to any not layer2 in
# 来自 ip_output 的数据包
ipfw add 10 skipto 3000 all from any to any not layer2 out
# 来自 ether_output_frame 的数据包
ipfw add 10 skipto 4000 all from any to any layer2 out
```

（是的，目前没有办法区分 ether_demux 和 bdg_forward）。

另请注意，对于 `layer2` 帧，仅处理 `allow`、`deny`、`netgraph`、`ngtee` 以及与 `dummynet` 相关的动作，所有其他动作对于此类帧相当于 `allow`。仅对不带 `layer2` 头部的 IP 数据包支持完整的动作集。例如，`divert` 动作不会对 `layer2` 帧执行 divert。

## 语法

通常，每个关键字或参数必须作为单独的命令行参数提供，不带前导或尾随空格。关键字区分大小写，而参数是否区分大小写取决于其性质（例如 uid 区分大小写，主机名不区分）。

某些参数（如端口或地址列表）是逗号分隔的值列表。在这种情况下，逗号 ',' 后的空格是允许的，以使行更易读。你也可以将整个命令（包括标志）放入单个参数中。例如，以下形式是等效的：

```sh
ipfw -q add deny src-ip 10.0.0.0/24,127.0.0.1/8
ipfw -q add deny src-ip 10.0.0.0/24, 127.0.0.1/8
ipfw "-q add deny src-ip 10.0.0.0/24, 127.0.0.1/8"
```

## 规则格式（RULE FORMAT）

防火墙规则的格式如下：

```
[rule_number] [set set_number] [prob match_probability] action [log [log_opts]] [altq queue] {tag | untag} number body
```

其中规则体指定用于过滤数据包的信息，包括以下内容：

**Layer2** 头部字段（可用时）
**IPv4** 和 IPv6 协议（SCTP、TCP、UDP、ICMP 等）
**源**和目的地址及端口
**方向**（参见"数据包流"章节）
**发送**和接收接口（按名称或地址）
**杂项** IP 头部字段（版本、服务类型、数据报长度、标识、分片标志、生存时间）
**IP** 选项
**IPv6** 扩展头部（分片、逐跳选项、路由头部、源路由 rthdr0、移动 IPv6 rthdr2、IPSec 选项）
**IPv6** Flow-ID
**杂项** TCP 头部字段（TCP 标志如 SYN、FIN、ACK、RST 等，序列号、确认号、窗口）
**TCP** 选项
**ICMP** 类型（用于 ICMP 数据包）
**ICMP6** 类型（用于 ICMP6 数据包）
**用户/组** ID（当数据包可以关联到本地套接字时）
**Divert** 状态（数据包是否来自 divert 套接字，例如 natd(8)）
**Fib** 标注状态（数据包是否已被标记以在未来的转发决策中使用特定的 FIB（路由表））

请注意，上述某些信息（如源 MAC 或 IP 地址以及 TCP/UDP 端口）很容易被伪造，因此仅基于这些字段进行过滤可能无法保证所需的结果。

**`syslog`** 将数据包记录到 syslogd(8)，使用 `LOG_SECURITY` 设施。

**`bpf`** 将数据包记录到名为 `ipfwXXXXX` 的 bpf(4) tap，其中 XXXXX 是规则编号。

**`rtsock`** 将数据包记录到 route(4) 套接字。有关消息结构的更多信息，请参见 ipfw 源代码中 `ipfw_log_rtsock()` 的注释。

```
log logamount 100 logdst syslog,bpf ...
```

**`rule_number`** 每条规则关联一个 1..65535 范围内的 `rule_number`，后者保留给 *default* 规则。规则按规则编号顺序检查。多条规则可以具有相同的编号，此时它们按添加顺序检查（和列出）。如果在输入规则时未指定编号，内核将以使该规则成为 *default* 规则之前最后一条的方式分配编号。自动规则编号通过将最后一条非默认规则编号增加 sysctl 变量 `net.inet.ip.fw.autoinc_step`（默认为 100）的值来分配。如果这不可能（例如，因为我们会超过最大允许规则编号），则使用最后一条非默认值的编号。

**`set`** `set_number` 每条规则关联一个 0..31 范围内的 `set_number`。集合可以单独禁用和启用，因此此参数对于原子规则集操作至关重要。它也可用于简化成组规则的删除。如果在输入规则时未指定集合编号，将使用 set 0。Set 31 是特殊的，它不能被禁用，且 set 31 中的规则不会被 `ipfw` 命令删除（但你可以使用 `ipfw` 命令删除它们）。Set 31 也用于 *default* 规则。

**`prob`** `match_probability` 仅以指定概率（0 到 1 之间的浮点数）声明匹配。这对于许多应用很有用，例如随机丢包或（与 `dummynet` 结合使用）模拟导致乱序数据包传递的多路径效果。注意：此条件在任何其他条件之前检查，包括可能具有副作用的 `keep-state` 或 `check-state` 等条件。

**`log`** [`logamount` `number`] 匹配带有 `log` 关键字的规则的数据包将被提供用于记录。除非通过 `logdst` `logdst_spec` 选项指定了每规则日志目标（见下文），否则数据包以两种方式记录：如果 sysctl 变量 `net.inet.ip.fw.verbose` 设置为 0（默认），可以使用名为 `ipfwXXXXX` 的 bpf(4) tap，其中 XXXXX 是具有 `log` 关键字的规则编号。名为 `ipfw0` 的兼容 bpf(4) tap 仍然存在。如果每规则 tap 上没有 bpf(4) 监听器，它将捕获数据包。当没有 bpf(4) 监听器附加到 tap 时，开销为零。如果 `net.inet.ip.fw.verbose` 设置为 1，数据包将使用 `LOG_SECURITY` 设施记录到 syslogd(8)，最多 `logamount` 个数据包。如果未指定 `logamount`，则限制取自 sysctl 变量 `net.inet.ip.fw.verbose_limit`。在两种情况下，值为 0 表示无限记录。一旦达到限制，可以通过清除该条目的日志计数器或数据包计数器来重新启用记录，参见 `resetlog` 命令。注意：记录是在成功验证所有其他数据包匹配条件之后，在对数据包执行最终动作（接受、拒绝等）之前完成的。

**`log`** [`logamount` `number`] `logdst` `logdst_spec` `logdst_spec` 是用于记录匹配规则的数据包的日志目标的逗号分隔列表。支持的目标有：注意：`logamount` 限制的是日志事件数量而不是被记录的数据包数量。即，匹配带有 `logamount` 50 的规则的数据包最多记录 50 个数据包。

**`tag`** `number` 当数据包匹配带有 `tag` 关键字的规则时，1..65534 范围内给定 `number` 的数字标签将附加到数据包。标签作为内部标记（不通过网络发送），可用于稍后识别这些数据包。例如，这可用于在接口之间建立信任并开始执行基于策略的过滤。一个数据包可以同时具有多个标签。标签是"粘性的"，意味着一旦标签由匹配规则应用到数据包，它就会一直存在直到显式删除。标签在内核中与数据包一起保留，但当数据包离开内核时会丢失，例如，将数据包发送到网络或将数据包发送到 divert(4) 套接字。要检查先前应用的标签，请使用 `tagged` 规则选项。要删除先前应用的标签，请使用 `untag` 关键字。注意：由于标签在内核空间中与数据包一起保留，因此可以在内核网络子系统的任何位置设置和取消设置它们（使用 mbuf_tags(9) 机制），而不仅仅是通过 ipfw(4) 的 `tag` 和 `untag` 关键字。例如，可以有专门的 netgraph(4) 节点进行流量分析并标记，以便稍后在防火墙中检查。

**`untag`** `number` 当数据包匹配带有 `untag` 关键字的规则时，会在附加到此数据包的标签中搜索编号为 `number` 的标签，如果找到，则从中删除。绑定到数据包的其他标签（如果存在）保持不变。

**`setmark`** `value | tablearg` 当数据包匹配带有 `setmark` 关键字的规则时，将为数据包分配一个 32 位数字标记。标记是标签的扩展。标记在单个 ipfw 规则集遍历中为数据包保留，并在数据包下次根据活动规则集检查时（参见"数据包流"章节）或离开 ipfw 上下文（例如被接受、divert、桥接或路由）时丢失。与标签不同，标记可以作为查找表键进行匹配，或与对另一个值应用按位掩码进行比较。每个数据包只能有一个标记，因此 `setmark` 总是覆盖之前的标记值。初始标记值为 0。要检查当前标记值，请使用 `mark` 规则选项。标记 `value` 可以以十进制或十六进制（如果以 0x 为前缀）输入，并且它们始终以十六进制打印。

**`altq`** `queue` 当数据包匹配带有 `altq` 关键字的规则时，将附加给定 `queue`（参见 altq(4)）的 ALTQ 标识符。请注意，此 ALTQ 标签仅对"离开"IPFW 的数据包有意义，而不是被拒绝或前往 divert 套接字的数据包。请注意，如果在处理数据包时内存不足，数据包将不会被标记，因此明智的做法是让你的 ALTQ "default" 队列策略考虑到这一点。如果多个 `altq` 规则匹配单个数据包，则只有第一个规则添加 ALTQ 分类标签。这样做可以通过在规则集早期使用 `count` `altq` `queue` 规则进行分类，然后稍后应用过滤决策来整形流量。例如，`check-state` 和 `keep-state` 规则可能在后面出现，除了回退 ALTQ 标签外，还提供实际的过滤决策。你必须运行 pfctl(8) 来设置队列，IPFW 才能按名称查找它们，如果 ALTQ 规则被重新排列，内核中包含队列标识符的规则可能已经过时并需要重新加载。过时的队列标识符可能导致错误分类。所有系统 ALTQ 处理可以通过 `ipfw` `enable` `altq` 和 `ipfw` `disable` `altq` 来开启或关闭。`net.inet.ip.fw.one_pass` 的使用与 ALTQ 流量整形无关，因为在添加 ALTQ 标签后始终会跟随实际规则动作。

### 规则动作（RULE ACTIONS）

规则可以关联以下动作之一，当数据包匹配规则体时将执行该动作。

```sh
# 添加一条没有实际体的规则
ipfw add 2999 return via any
# 列出不含 "from any to any" 部分的规则
ipfw -c list
```

```sh
# 重新组装传入的分片
ipfw add reass all from any to any in
```

**`allow | accept | pass | permit`** 允许匹配规则的数据包。搜索终止。

**`check-state`** [`:flowname |` `:any`] 根据动态规则集检查数据包。如果找到匹配项，执行生成此动态规则的规则关联的动作，否则移动到下一条规则。`check-state` 规则没有体。如果未找到 `check-state` 规则，则在第一条 `keep-state` 或 `limit` 规则处检查动态规则集。`:flowname` 是由 `keep-state` 操作码分配给动态规则的符号名称。特殊流名 `:any` 可用于在匹配时忽略状态流名。`:default` 关键字是用于与旧规则集兼容的特殊名称。

**`count`** 更新所有匹配规则的数据包的计数器。搜索继续到下一条规则。

**`deny | drop`** 丢弃匹配此规则的数据包。搜索终止。

**`divert`** `port` 将匹配此规则的数据包 divert 到绑定到端口 `port` 的 divert(4) 套接字。搜索终止。

**`fwd | forward`** `ipaddr | tablearg`[,`port`] 将匹配数据包的下一跳更改为 `ipaddr`，可以是 IP 地址或主机名。下一跳也可以通过使用 `tablearg` 关键字代替显式地址，由为该数据包查找的最后一个表提供。如果此规则匹配，搜索终止。如果 `ipaddr` 是本地地址，则匹配的数据包将被转发到本地机器上的 `port`（如果规则中未指定，则为数据包中的端口号）。如果 `ipaddr` 不是本地地址，则端口号（如果指定）被忽略，数据包将使用该 IP 的本地路由表中找到的路由转发到远程地址。`fwd` 规则不会匹配 layer2 数据包（在 ether_input、ether_output 或桥接上接收的数据包）。`fwd` 动作根本不会更改数据包的内容。特别是，目的地址保持不变，因此转发到另一个系统的数据包通常会被该系统拒绝，除非该系统上有匹配的规则来捕获它们。对于本地转发的数据包，套接字的本地地址将设置为数据包的原始目的地址。这使得 netstat(1) 条目看起来相当奇怪，但旨在用于透明代理服务器。

**`nat`** `nat_nr | global | tablearg` 将数据包传递给 nat 实例（用于网络地址转换、地址重定向等）：有关更多信息，请参见"网络地址转换（NAT）"章节。

**`nat64lsn`** `name` 将数据包传递给有状态 NAT64 实例（用于 IPv6/IPv4 网络地址和协议转换）：有关更多信息，请参见"IPv6/IPv4 网络地址和协议转换"章节。

**`nat64stl`** `name` 将数据包传递给无状态 NAT64 实例（用于 IPv6/IPv4 网络地址和协议转换）：有关更多信息，请参见"IPv6/IPv4 网络地址和协议转换"章节。

**`nat64clat`** `name` 将数据包传递给 CLAT NAT64 实例（用于客户端 IPv6/IPv4 网络地址和协议转换）：有关更多信息，请参见"IPv6/IPv4 网络地址和协议转换"章节。

**`nptv6`** `name` 将数据包传递给 NPTv6 实例（用于 IPv6 到 IPv6 网络前缀转换）：有关更多信息，请参见"IPv6 到 IPv6 网络前缀转换（NPTv6）"章节。

**`pipe`** `pipe_nr` 将数据包传递给 `dummynet` "pipe"（用于带宽限制、延迟等）。有关更多信息，请参见"流量整形器（DUMMYNET）配置"章节。搜索终止；但是，从 pipe 退出时，如果 sysctl(8) 变量 `net.inet.ip.fw.one_pass` 未设置，数据包将从下一条规则开始再次传递给防火墙代码。

**`queue`** `queue_nr` 将数据包传递给 `dummynet` "queue"（使用 WF2Q+ 进行带宽限制）。

**`reject`** （已弃用）。`unreach host` 的同义词。

**`reset`** 丢弃匹配此规则的数据包，如果数据包是 TCP 数据包，尝试发送 TCP 重置（RST）通知。搜索终止。

**`reset6`** 丢弃匹配此规则的数据包，如果数据包是 TCP 数据包，尝试发送 TCP 重置（RST）通知。搜索终止。

**`skipto`** `number | tablearg` 跳过所有编号小于 `number` 的后续规则。搜索从编号为 `number` 或更高的第一条规则继续。可以将 `tablearg` 关键字与 skipto 一起使用以实现 *计算* skipto。skipto 可以以 O(log(N)) 或 O(1) 的方式工作，具体取决于内存量和/或 sysctl 变量。有关更多详细信息，请参见"SYSCTL 变量"章节。

**`call`** `number | tablearg` 当前规则编号保存在内部栈中，规则集处理从编号为 `number` 或更高的第一条规则继续。如果后来遇到带有 `return` 动作的规则，处理将返回到编号为该 `call` 规则编号加一或更高的第一条规则（与数据包从 divert(4) 套接字在 `divert` 动作后返回的行为相同）。这可用于对具有不同接口的常见检查的规则进行类似汇编语言"子程序"调用。任何编号的规则都可以被调用，而不仅仅是像 `skipto` 那样的前向跳转。因此，为了防止在出错时出现无限循环，`call` 和 `return` 动作在无法分配内存或栈溢出/下溢时都不执行任何跳转，而只是转到下一条规则。规则编号的栈内部使用 mbuf_tags(9) 机制实现，目前大小为 16 个条目。由于数据包离开内核时 mbuf 标签会丢失，因此不应在子程序中使用 `divert`，以避免无限循环和其他不良影响。

**`return`** 取出由上次 `call` 动作保存到内部栈的规则编号，并将规则集处理返回到编号大于相应 `call` 规则编号的第一条规则。有关更多详细信息，请参见 `call` 动作的描述。请注意，`return` 规则通常结束一个"子程序"，因此是无条件的，但 `dummynet` 命令行工具目前要求除 `check-state` 之外的每个动作都有体。虽然有时只对某些数据包返回很有用，但通常为了可读性你只想打印 "return"。解决方法是使用新语法和 `-c` 开关：这种外观上的烦恼可能会在未来版本中修复。

**`tee`** `port` 将匹配此规则的数据包副本发送到绑定到端口 `port` 的 divert(4) 套接字。搜索继续到下一条规则。

**`unreach`** `code` [mtu] 丢弃匹配此规则的数据包，并尝试发送带有代码 `code` 的 ICMP 不可达通知，其中 `code` 是 0 到 255 的数字，或以下别名之一：`net`、`host`、`protocol`、`port`、`needfrag`、`srcfail`、`net-unknown`、`host-unknown`、`isolated`、`net-prohib`、`host-prohib`、`tosnet`、`toshost`、`filter-prohib`、`host-precedence` 或 `precedence-cutoff`。`needfrag` 代码可以有一个可选的 `mtu` 参数。如果指定，MTU 值将放入生成的 ICMP 数据包中。搜索终止。

**`unreach6`** `code` 丢弃匹配此规则的数据包，并尝试发送带有代码 `code` 的 ICMPv6 不可达通知，其中 `code` 是 0、1、3 或 4 的数字，或以下别名之一：`no-route`、`admin-prohib`、`address` 或 `port`。搜索终止。

**`netgraph`** `cookie` 将数据包 divert 到具有给定 `cookie` 的 netgraph 中。搜索终止。如果数据包后来从 netgraph 返回，它要么被接受，要么继续到下一条规则，具体取决于 `net.inet.ip.fw.one_pass` sysctl 变量。

**`ngtee`** `cookie` 数据包副本被 divert 到 netgraph，原始数据包继续到下一条规则。有关 `netgraph` 和 `ngtee` 动作的更多信息，请参见 ng_ipfw(4)。

**`setfib`** `fibnum | tablearg` 数据包被标记以在后续的任何转发决策中使用 FIB（路由表）`fibnum`。在当前实现中，这限于值 0 到 15，参见 setfib(2)。处理在下一条规则继续。可以将 `tablearg` 关键字与 setfib 一起使用。如果 tablearg 值不在编译的 fib 范围内，数据包的 fib 设置为 0。

**`setdscp`** `DSCP | number | tablearg` 为 IPv4/IPv6 数据包设置指定的 DiffServ 代码点。处理在下一条规则继续。支持的值有：`cs0`（`000000`）、`cs1`（`001000`）、`cs2`（`010000`）、`cs3`（`011000`）、`cs4`（`100000`）、`cs5`（`101000`）、`cs6`（`110000`）、`cs7`（`111000`）、`af11`（`001010`）、`af12`（`001100`）、`af13`（`001110`）、`af21`（`010010`）、`af22`（`010100`）、`af23`（`010110`）、`af31`（`011010`）、`af32`（`011100`）、`af33`（`011110`）、`af41`（`100010`）、`af42`（`100100`）、`af43`（`100110`）、`va`（`101100`）、`ef`（`101110`）、`be`（`000000`）。此外，DSCP 值可以按数字（0..63）指定。也可以将 `tablearg` 关键字与 setdscp 一起使用。如果 tablearg 值不在 0..63 范围内，则使用提供值的低 6 位。

**`tcp-setmss`** `mss` 将 TCP 段中的最大段大小（MSS）设置为值 `mss`。应加载内核模块 `ipfw_pmod` 或内核应具有 `options IPFIREWALL_PMOD` 才能使用此动作。如果原始 MSS 值低于指定值，此命令不会更改数据包。支持基于 IPv4 和 IPv6 的 TCP。无论是否被 `tcp-setmss` 规则匹配，搜索都会继续到下一条规则。

**`reass`** 排队并重新组装 IPv4 分片。如果数据包未分片，则更新计数器并继续到下一条规则处理。如果数据包是最后一个逻辑分片，则重新组装数据包，如果 `net.inet.ip.fw.one_pass` 设置为 0，处理继续到下一条规则。否则，允许数据包通过，搜索终止。如果数据包是逻辑分片组中间的分片，则被消耗，处理立即停止。分片处理可以通过 `net.inet.ip.maxfragpackets` 和 `net.inet.ip.maxfragsperpacket` 进行调整，它们分别限制可处理的最大分片数（默认：800）和每个数据包的最大分片数（默认：16）。注意：由于分片不包含端口号，因此应避免在 `reass` 规则中使用。或者，可以使用基于方向（如 `in`/`out`）和基于源（如 `via`）的匹配模式来选择分片。通常在规则集开头使用如下简单规则即可满足需求。

**`abort`** 丢弃匹配此规则的数据包，如果数据包是 SCTP 数据包，尝试发送包含 ABORT 块的 SCTP 数据包。搜索终止。

**`abort6`** 丢弃匹配此规则的数据包，如果数据包是 SCTP 数据包，尝试发送包含 ABORT 块的 SCTP 数据包。搜索终止。

### 规则体（RULE BODY）

规则体包含零个或多个模式（如特定的源和目的地址或端口、协议选项、传入或传出接口等），数据包必须匹配这些模式才能被识别。通常，这些模式通过（隐含的）`and` 运算符连接——即所有模式都必须匹配才能使规则匹配。单个模式可以加 `not` 运算符前缀以反转匹配结果，如

```sh
ipfw add 100 allow ip from not 1.2.3.4 to any
```

此外，可以通过将模式放在括号 () 或大括号 {} 之间的列表中，并使用 `or` 运算符来构造一组备选匹配模式（*or-blocks*），如下所示：

```sh
ipfw add 100 allow ip from { x or not y or z } to any
```

只允许一级括号。请注意，大多数 shell 对括号或大括号有特殊含义，因此建议在它们前面加反斜杠以防止这种解释。

规则体通常必须包含源和目的地址说明符。关键字 `any` 可在多处用于指定必填字段的内容无关紧要。

规则体具有以下格式：

```
[proto from src to dst] [options]
```

第一部分（proto from src to dst）是为了与早期版本的 FreeBSD 向后兼容。在现代 FreeBSD 中，任何匹配模式（包括 MAC 头部、IP 协议、地址和端口）都可以在 `options` 部分指定。

规则字段的含义如下：

**`ip4 | ipv4`** 匹配 IPv4 数据包。

**`ip6 | ipv6`** 匹配 IPv6 数据包。

**`ip | all`** 匹配任何数据包。

**`any`** 匹配任何 IP 地址。

**`me`** 匹配系统上接口上配置的任何 IP 地址。

**`me6`** 匹配系统上接口上配置的任何 IPv6 地址。地址列表在分析数据包时评估。

**table(`name`)** 匹配查找表 `number` 中存在条目的任何 IPv4 或 IPv6 地址。

**table(`name`,`value`)** 匹配查找表 `number` 中存在条目且指定的 32 位无符号 `value` 与条目值匹配的任何 IPv4 或 IPv6 地址。

**table(`name`,`value-type`=`value`)** 匹配查找表 `number` 中存在条目且指定的 32 位无符号 `value` 与找到记录的对应 `value-type` 字段匹配的任何 IPv4 或 IPv6 地址。

**`numeric-ip | hostname`** 匹配单个 IPv4 地址，指定为点分四元组或主机名。主机名在规则添加到防火墙列表时解析。

**`addr`**/`masklen` 匹配基址为 `addr`（指定为 IP 地址、网络号或主机名）且掩码宽度为 `masklen` 位的所有地址。例如，1.2.3.4/25 或 1.2.3.0/25 将匹配从 1.2.3.0 到 1.2.3.127 的所有 IP 号。

**`addr`**:`mask` 匹配基址为 `addr`（指定为 IP 地址、网络号或主机名）且掩码为 `mask`（指定为点分四元组）的所有地址。例如，1.2.3.4:255.0.255.0 或 1.0.3.0:255.0.255.0 将匹配 1.\*.3.\*。此形式仅建议用于非连续掩码。对于连续掩码，最好使用 `addr`/`masklen` 格式，它更紧凑且不易出错。

**`numeric-ip | hostname`** 匹配 inet_pton(3) 允许的单个 IPv6 地址或主机名。主机名在规则添加到防火墙列表时解析。

**`addr`**/`masklen` 匹配基址为 `addr`（指定为 inet_pton(3) 允许的形式或主机名）且掩码宽度为 `masklen` 位的所有 IPv6 地址。

**`addr`**/`mask` 匹配基址为 `addr`（指定为 inet_pton(3) 允许的形式或主机名）且掩码为 `mask`（指定为 inet_pton(3) 允许的形式）的所有 IPv6 地址。例如，fe::640:0:0/ffff::ffff:ffff:0:0 将匹配 fe:\*:\*:\*:\*:0:640:\*:\*。此形式仅建议用于非连续掩码。对于连续掩码，最好使用 `addr`/`masklen` 格式，它更紧凑且不易出错。

```sh
ipfw add count tcp from any ftpee-data-ftp to any
```

**`proto : protocol |`** `{` `protocol` `or ... }`

**`protocol`** : [`not` ]`protocol-name | protocol-number`] 由数字或名称指定的 IP 协议（完整列表见 **/etc/protocols**），或以下关键字之一：`proto` 选项中的 `ipv6` 将被视为内部协议。并且 `ipv4` 在 `proto` 选项中不可用。`{` `protocol` `or ... }` 格式（*or-block*）仅为方便而提供，但其使用已弃用。

**`src`** 和 `dst`: {`addr |` `{` `addr` `or ... }` }[[`not` ]`ports`]]} 一个地址（或列表，见下文），可选后跟 `ports` 说明符。第二种格式（具有多个地址的 *or-block*）仅为方便而提供，不鼓励使用。

**`addr`** : [`not` ]{}] `any | me | me6 |` `table-ref` `| addr-list | addr-set` }

**`table-ref`** : 表查找可以通过以下方式之一指定：有关查找表的更多信息，请参见下面的"查找表"章节。

**`addr-list : ip-addr`** [,`addr-list`]

**`ip-addr`** : 以以下方式之一指定的主机或子网地址：

**`addr-set : addr`**[/`masklen` ]`{``list``}`]

**`list`** : {`num | num-num` }[,`list`]} 匹配基址为 `addr`（指定为 IP 地址、网络号或主机名）且最后一个字节在大括号 {} 之间列表中的所有地址。请注意，大括号和数字之间不得有空格（逗号后的空格是允许的）。列表元素可以指定为单个条目或范围。`masklen` 字段用于限制地址集的大小，可以具有 24 到 32 之间的任何值。如果未指定，则假定为 24。此格式对于在单个规则中处理稀疏地址集特别有用。因为匹配使用位掩码进行，所以它花费恒定时间并显著降低了规则集的复杂性。例如，指定为 1.2.3.4/24{128,35-55,89} 或 1.2.3.0/24{128,35-55,89} 的地址将匹配以下 IP 地址：1.2.3.128、1.2.3.35 到 1.2.3.55、1.2.3.89。

**`addr6-list : ip6-addr`** [,`addr6-list`]

**`ip6-addr`** : 以以下方式之一指定的主机或子网：不支持 IPv6 地址集，因为 IPv6 地址通常在初始前缀之后是随机的。

**`ports`** : {`port | port`-`port`}[,`ports`]} 对于支持端口号的协议（如 SCTP、TCP 和 UDP），可选的 `ports` 可以指定为一个或多个端口或端口范围，以逗号分隔但不带空格，以及可选的 `not` 运算符。`-` 表示法指定端口范围（包括边界）。服务名称（来自 **/etc/services**）可以代替数字端口值使用。端口列表长度限制为 30 个端口或范围，但可以通过在规则 `options` 部分使用 *or-block* 来指定更大的范围。反斜杠（`\`）可用于转义服务名称中的破折号（`-`）字符（从 shell 中，反斜杠必须键入两次以避免 shell 本身将其解释为转义字符）。具有非零偏移量的分片数据包（即不是第一个分片）永远不会匹配具有一个或多个端口规范的规则。有关匹配分片数据包的详细信息，请参见 `frag` 选项。

### 规则选项（匹配模式）

可以在规则内使用其他匹配模式。这些所谓的 *选项* 可以存在零个或多个，可选地以 `not` 操作数为前缀，并可能分组为 *or-blocks*。

可以使用以下匹配模式（按字母顺序列出）：

- 以点分四元组形式，例如 **127.88.34.0**。此形式可用于 IPv4 查找以及所有数字查找类型。
- 以 32 位数字形式，例如 0xf00baa1 或 255。此形式可用于 IPv4 查找以及所有数字查找类型。
- 当与 `dst-ip6` 或 `src-ip6` 字段一起指定时，作为 IPv6 地址。如果使用，规则将仅匹配 IPv6 数据包。示例：src-ip6:afff:ff00:ffff:ffff:0:0:0:0f0f。
- 当与 `dst-mac` 或 `src-mac` 字段一起指定时，作为以太网 MAC 地址。例如 00:11:22:33:44:55。

```sh
MAC 10:20:30:40:50:60/33 any
```

```sh
MAC 10:20:30:40:50:60&00:00:00:00:ff:ff any
```

- 斜杠（/）后跟有效位数。例如，具有 33 个有效位的地址可以指定为：
- &符号（&）后跟以六个用冒号分隔的十六进制数字组指定的位掩码。例如，最后 16 位有效的地址可以指定为：请注意，&符号在许多 shell 中具有特殊含义，通常应进行转义。

```sh
ipfw add deny ip from any to any out recv ed0 xmit ed1
```

```sh
ip verify unicast reverse-path
```

```sh
ip verify unicast source reachable-via any
```

**`// this is a comment`** 在规则中插入指定文本作为注释。// 之后的所有内容都被视为注释并存储在规则中。你可以有仅注释的规则，这些规则被列为具有 `count` 动作后跟注释。

**`bridged`** `layer2` 的别名。

**`defer-immediate-action | defer-action`** 带有此选项的规则在匹配时不会执行正常动作。此选项旨在与 `record-state` 或 `keep-state` 一起使用，因为创建但在匹配时被忽略的动态规则将按预期工作。同时具有 `record-state` 和 `defer-immediate-action` 的规则会创建动态规则并继续到下一条规则，而不实际执行此规则的动作部分。当规则稍后通过状态表激活时，动作照常执行。

**`diverted`** 仅匹配由 divert 套接字生成的数据包。

**`diverted-loopback`** 仅匹配来自 divert 套接字回到 IP 栈输入以进行传递的数据包。

**`diverted-output`** 仅匹配从 divert 套接字回到 IP 栈输出以进行传递的数据包。

**`dst-ip`** `ip-address` 匹配目的 IP 为指定参数中地址之一的 IPv4 数据包。

**{`dst-ip6** | dst-ipv6` }`ip6-address`} 匹配目的 IP 为指定参数中地址之一的 IPv6 数据包。

**`dst-port`** `ports` 匹配目的端口为指定参数中端口之一的 IP 数据包。

**`established`** 匹配设置了 RST 或 ACK 位的 TCP 数据包。

**`ext6hdr`** `header` 匹配包含由 `header` 给定的扩展头部的 IPv6 数据包。支持的头部有：Fragment（`frag`）、Hop-to-hop 选项（`hopopt`）、任何类型的路由头部（`route`）、源路由路由头部类型 0（`rthdr0`）、移动 IPv6 路由头部类型 2（`rthdr2`）、目的选项（`dstopt`）、IPSec 认证头部（`ah`）和 IPSec 封装安全负载头部（`esp`）。

**`fib`** `fibnum` 匹配已被标记为使用给定 FIB（路由表）编号的数据包。

**`flow`** `table-ref` 在由 `table-ref` 指定的查找表中搜索流条目。如果未找到，匹配失败。否则，匹配成功并且 `tablearg` 设置为从表中提取的值。此选项可用于根据某些数据包字段快速分发流量。有关查找表的更多信息，请参见下面的"查找表"章节。

**`flow-id`** `labels` 匹配包含 `labels` 中给定的任何流标签的 IPv6 数据包。`labels` 是逗号分隔的数字流标签列表。

**`dst-mac`** `table-ref` 在由 `table-ref` 指定的查找表中搜索目的 MAC 地址条目。如果未找到，匹配失败。否则，匹配成功并且 `tablearg` 设置为从表中提取的值。

**`src-mac`** `table-ref` 在由 `table-ref` 指定的查找表中搜索源 MAC 地址条目。如果未找到，匹配失败。否则，匹配成功并且 `tablearg` 设置为从表中提取的值。

**`frag`** `spec` 匹配 `ip_off` 字段包含 `spec` 中指定的逗号分隔 IPv4 分片选项列表的 IPv4 数据包。可识别的选项有：`df`（`don't fragment`，不分片）、`mf`（`more fragments`，更多分片）、`rf`（`reserved fragment bit`，保留分片位）`offset`（`non-zero fragment offset`，非零分片偏移）。特定选项的缺失可以用 `!` 表示。空选项列表默认匹配非零分片偏移。这样的规则将匹配所有非第一个分片数据报，包括 IPv4 和 IPv6。这是与旧规则集的向后兼容。

**`gid`** `group` 匹配由 `group` 发送或为 `group` 接收的所有 TCP 或 UDP 数据包。`group` 可以按名称或数字指定。

**`jail`** `jail` 匹配由 ID 或名称为 `jail` 的 jail 发送或为该 jail 接收的所有 TCP 或 UDP 数据包。

**`icmptypes`** `types` 匹配 ICMP 类型在列表 `types` 中的 ICMP 数据包。该列表可以指定为以逗号分隔的单个类型（数字）的任意组合。*不允许范围。* 支持的 ICMP 类型有：echo reply（`0`）、destination unreachable（`3`）、source quench（`4`）、redirect（`5`）、echo request（`8`）、router advertisement（`9`）、router solicitation（`10`）、time-to-live exceeded（`11`）、IP header bad（`12`）、timestamp request（`13`）、timestamp reply（`14`）、information request（`15`）、information reply（`16`）、address mask request（`17`）和 address mask reply（`18`）。

**`icmp6types`** `types` 匹配 ICMP6 类型在 `types` 列表中的 ICMP6 数据包。该列表可以指定为以逗号分隔的单个类型（数字）的任意组合。*不允许范围。*

**`in | out`** 分别匹配传入或传出数据包。`in` 和 `out` 是互斥的（实际上，`out` 实现为 `not in`）。

**`ipid`** `id-list` 匹配 `ip_id` 字段值包含在 `id-list` 中的 IPv4 数据包，`id-list` 是单个值或以与 `ports` 相同方式指定的值或范围列表。

**`iplen`** `len-list` 匹配总长度（包括头部和数据）在集合 `len-list` 中的 IP 数据包，`len-list` 是单个值或以与 `ports` 相同方式指定的值或范围列表。

**`ipoptions`** `spec` 匹配 IPv4 头部包含 `spec` 中指定的逗号分隔选项列表的数据包。支持的 IP 选项有：`ssrr`（严格源路由）、`lsrr`（松散源路由）、`rr`（记录数据包路由）和 `ts`（时间戳）。特定选项的缺失可以用 `!` 表示。

**`ipprecedence`** `precedence` 匹配 precedence 字段等于 `precedence` 的 IPv4 数据包。

**`ipsec`** 匹配具有关联 IPSEC 历史的数据包（即数据包以 IPSEC 封装传入，内核具有 IPSEC 支持，并且可以正确解封装它）。请注意，指定 `ipsec` 与指定 `proto` `ipsec` 不同，因为后者仅查看特定 IP 协议字段，而不考虑 IPSEC 内核支持和 IPSEC 数据的有效性。进一步请注意，在没有 IPSEC 支持的内核中，此标志会被静默忽略。它不会影响给定时的规则处理，规则处理就像没有 `ipsec` 标志一样。

**`iptos`** `spec` 匹配 `tos` 字段包含 `spec` 中指定的逗号分隔服务类型列表的 IPv4 数据包。支持的 IP 服务类型有：`lowdelay`（`IPTOS_LOWDELAY`）、`throughput`（`IPTOS_THROUGHPUT`）、`reliability`（`IPTOS_RELIABILITY`）、`mincost`（`IPTOS_MINCOST`）、`congestion`（`IPTOS_ECN_CE`）。特定类型的缺失可以用 `!` 表示。

**`dscp spec`** [,`spec`] 匹配 `DS` 字段值包含在 `spec` 掩码中的 IPv4/IPv6 数据包。可以通过逗号分隔列表指定多个值。值可以是 `setdscp` 动作中使用的关键字之一或精确数字。

**`ipttl`** `ttl-list` 匹配生存时间包含在 `ttl-list` 中的 IPv4 数据包，`ttl-list` 是单个值或以与 `ports` 相同方式指定的值或范围列表。

**`ipversion`** `ver` 匹配 IP 版本字段为 `ver` 的 IP 数据包。

**`keep-state`** [`:flowname`] 匹配时，防火墙将创建动态规则，其默认行为是使用相同协议匹配源和目的 IP/端口之间的双向流量。该规则具有有限的生存期（由一组 sysctl(8) 变量控制），并且每次找到匹配数据包时都会刷新生存期。`:flowname` 用于向动态规则添加额外的地址、端口和协议参数。它可用于通过 `check-state` 规则进行更精确的匹配。`:default` 关键字是用于与旧规则集兼容的特殊名称。

**`layer2`** 仅匹配 layer2 数据包，即从 `ether_demux()` 和 `ether_output_frame()` 传递到 `via` 的数据包。

**`limit`** {`src-addr | src-port | dst-addr | dst-port` }`N` [`:flowname`]} 防火墙将仅允许具有规则中指定相同参数集的 `N` 个连接。可以指定源和目的地址及端口中的一个或多个。

**`lookup`** {`dst-ip | dst-ip4 | dst-ip6 | dst-port | dst-mac | src-ip |`} `src-ip4 | src-ip6 | src-port | src-mac | uid | jail | dscp | mark |` `rulenum` }[:`bitmask` ]`name`] 在查找表 `name` 中搜索与指定为参数的字段匹配的条目。如果未找到，匹配失败。否则，匹配成功并且 `tablearg` 设置为从表中提取的值。如果指定了可选的 `bitmask`，则字段的值通过按位 AND 与 `bitmask` 进行修改，并搜索结果值而不是原始值。`bitmask` 接受以下格式：`bitmask` 不能为 `dst-ip` 或 `src-ip` 指定，因为这些字段说明符同时查找 IPv4 和 IPv6 地址。此选项可用于根据某些数据包字段快速分发流量。`bitmask` 允许通过向表中插入掩码前缀并在每次查找时应用 `bitmask` 来实现通配符查找。有关查找表的更多信息，请参见下面的"查找表"章节。

**`{ MAC | mac }`** `dst-mac src-mac` 匹配具有给定 `dst-mac` 和 `src-mac` 地址的数据包，指定为 `any` 关键字（匹配任何 MAC 地址）或六个用冒号分隔的十六进制数字组，可选后跟指示有效位的掩码。掩码可以使用以下任一方法指定：请注意 MAC 地址的顺序（先目的，后源）与网络上的顺序相同，但与 IP 地址使用的顺序相反。

**`mac-type`** `mac-type` 匹配以太网类型字段对应于指定为参数之一的那些数据包。`mac-type` 的指定方式与 `port numbers` 相同（即一个或多个逗号分隔的单个值或范围）。你可以对已知值使用符号名称，如 *vlan*、*ipv4*、*ipv6*。值可以以十进制或十六进制（如果以 0x 为前缀）输入，并且它们始终以十六进制打印（除非使用 `-N` 选项，在这种情况下将尝试符号解析）。

**`proto`** `protocol` 匹配具有相应 IP 协议的数据包。

**`record-state`** 匹配时，防火墙将创建动态规则，就像指定了 `keep-state` 一样。但是，与 `keep-state` 不同，此选项不隐含 `check-state`。

**`recv | xmit | via`** {`ifX |` `ifmask |` `table-ref |` `ipno |` `any`} 分别匹配在指定接口上接收、发送或通过的数据包，指定方式为按精确名称（`ifX`）、按设备掩码（`ifmask`）、按 IP 地址或通过某个接口。接口名称可以根据 shell 使用的规则与 `ifmask` 进行 fnmatch(3) 匹配（例如 tun*）。另请参见"实例"章节。可以使用由 `table-ref` 指定的查找表按内核 ifindex 匹配接口。有关查找表的更多信息，请参见下面的"查找表"章节。`via` 关键字使接口始终被检查。如果使用 `recv` 或 `xmit` 代替 `via`，则仅检查接收或发送接口（分别）。通过指定两者，可以根据接收和发送接口匹配数据包，例如：`recv` 接口可以在传入或传出数据包上测试，而 `xmit` 接口只能在传出数据包上测试。因此，每当使用 `xmit` 时，需要 `out`（而 `in` 是无效的）。数据包可能没有接收或发送接口：源自本地主机的数据包没有接收接口，而发往本地主机的数据包没有发送接口。

**`set-limit`** {`src-addr | src-port | dst-addr | dst-port` }`N`} 工作方式类似于 `limit`，但没有隐含的 `check-state`。

**`setup`** 匹配设置了 SYN 位但没有 ACK 位的 TCP 数据包。这是 "`tcpflags\ syn,!ack`" 的简写形式。

**`sockarg`** 匹配关联到本地套接字且 SO_USER_COOKIE 套接字选项已设置为非零值的数据包。作为副作用，该选项的值可作为 `tablearg` 值使用，进而可用作 `skipto` 或 `pipe` 编号。

**`src-ip`** `ip-address` 匹配源 IP 为指定参数中地址之一的 IPv4 数据包。

**`src-ip6`** `ip6-address` 匹配源 IP 为指定参数中地址之一的 IPv6 数据包。

**`src-port`** `ports` 匹配源端口为指定参数中端口之一的 IP 数据包。

**`tagged`** `tag-list` 匹配标签包含在 `tag-list` 中的数据包，`tag-list` 是单个值或以与 `ports` 相同方式指定的值或范围列表。标签可以通过 `tag` 规则动作参数应用到数据包（有关标签的详细信息，请参见其描述）。

**`mark`** `value[:bitmask] | tablearg[:bitmask]` 匹配标记等于 `value`（可选应用 `bitmask`）的数据包。也可以使用 `tablearg` 代替显式 `value` 来匹配由上次表查找提供的值。`value` 和 `bitmask` 都可以以十进制或十六进制（如果以 0x 为前缀）输入，并且它们始终以十六进制打印。

**`tcpack`** `ack` 仅 TCP 数据包。匹配 TCP 头部确认号字段设置为 `ack` 的数据包。

**`tcpdatalen`** `tcpdatalen-list` 匹配 TCP 数据长度为 `tcpdatalen-list` 的 TCP 数据包，`tcpdatalen-list` 是单个值或以与 `ports` 相同方式指定的值或范围列表。

**`tcpflags`** `spec` 仅 TCP 数据包。匹配 TCP 头部包含 `spec` 中指定的逗号分隔标志列表的数据包。支持的 TCP 标志有：`fin`、`syn`、`rst`、`psh`、`ack` 和 `urg`。特定标志的缺失可以用 `!` 表示。包含 `tcpflags` 规范的规则永远不会匹配具有非零偏移量的分片数据包。有关匹配分片数据包的详细信息，请参见 `frag` 选项。

**`tcpmss`** `tcpmss-list` 匹配 MSS（最大段大小）值设置为 `tcpmss-list` 的 TCP 数据包，`tcpmss-list` 是单个值或以与 `ports` 相同方式指定的值或范围列表。

**`tcpseq`** `seq` 仅 TCP 数据包。匹配 TCP 头部序列号字段设置为 `seq` 的数据包。

**`tcpwin`** `tcpwin-list` 匹配头部窗口字段设置为 `tcpwin-list` 的 TCP 数据包，`tcpwin-list` 是单个值或以与 `ports` 相同方式指定的值或范围列表。

**`tcpoptions`** `spec` 仅 TCP 数据包。匹配 TCP 头部包含 `spec` 中指定的逗号分隔选项列表的数据包。支持的 TCP 选项有：`mss`（最大段大小）、`window`（tcp 窗口通告）、`sack`（选择性确认）、`ts`（rfc1323 时间戳）和 `cc`（rfc1644 t/tcp 连接计数）。特定选项的缺失可以用 `!` 表示。

**`uid`** `user` 匹配由 `user` 发送或为 `user` 接收的所有 TCP 或 UDP 数据包。`user` 可以按名称或标识号匹配。

**`verrevpath`** 对于传入数据包，根据数据包的源地址进行路由表查找。如果数据包进入系统的接口与路由的输出接口匹配，则数据包匹配。如果接口不匹配，则数据包不匹配。所有传出数据包或没有传入接口的数据包都匹配。该选项的名称和功能有意类似于 Cisco IOS 命令：此选项可用于制作反欺骗规则，以拒绝所有源地址不来自此接口的数据包。另请参见 `antispoof` 选项。

**`versrcreach`** 对于传入数据包，根据数据包的源地址进行路由表查找。如果存在到源地址的路由，但不是默认路由或黑洞/拒绝路由，则数据包匹配。否则，数据包不匹配。所有传出数据包都匹配。该选项的名称和功能有意类似于 Cisco IOS 命令：此选项可用于制作反欺骗规则，以拒绝所有源地址不可达的数据包。

**`antispoof`** 对于传入数据包，检查数据包的源地址是否属于直接连接的网络。如果网络是直接连接的，则将数据包进入的接口与网络连接的接口进行比较。当传入接口和直接连接的接口不同时，数据包不匹配。否则，数据包匹配。所有传出数据包都匹配。此选项可用于制作反欺骗规则，以拒绝所有伪装来自直接连接网络但实际上并非通过该接口进入的数据包。此选项类似于但比 `verrevpath` 更受限制，因为它仅对具有直接连接网络源地址（而不是所有源地址）的数据包生效。

## 查找表（LOOKUP TABLES）

查找表对于处理大型稀疏地址集或其他搜索键（如端口、jail ID、接口名称）非常有用。在本节的其余部分，我们将使用术语 "键"。表名需要匹配以下规范：`table-name`。可以在不同 `集合` 中创建同名表。但是，规则默认链接到 `set 0` 中的表。此行为可以通过 `net.inet.ip.fw.tables_sets` 变量控制。有关更多信息，请参见"规则集合"章节。最多可以有 65535 个不同的查找表。

支持以下表类型：

**`table-type`** : `addr | iface | number | flow | mac`

**`table-key`** : `addr`[/`masklen` ]]

**`flow-spec`** : `flow-field`[,`flow-spec`]

**`flow-field : src-ip | proto | src-port | dst-ip | dst-port`**

**`addr`** 匹配 IPv4 或 IPv6 地址。每个条目由 `addr`[/`masklen`] 表示，并将匹配基址为 `addr`（指定为 IPv4/IPv6 地址或主机名）且掩码宽度为 `masklen` 位的所有地址。如果未指定 `masklen`，IPv4 默认为 32，IPv6 默认为 128。在表中查找 IP 地址时，最具体的条目将匹配。

**`iface`** 匹配接口名称。每个条目由被视为接口名称的字符串表示。不支持通配符。

**`number`** 匹配协议端口、uid/gid 或 jail ID。每个条目由 32 位无符号整数表示。不支持范围。

**`flow`** 匹配由 `flow` 类型子选项指定的数据包字段与表条目。

**`mac`** 匹配 MAC 地址。每个条目由 `addr`[/`masklen`] 表示，并将匹配基址为 `addr` 且掩码宽度为 `masklen` 位的所有地址。如果未指定 `masklen`，则默认为 48。在表中查找 MAC 地址时，最具体的条目将匹配。

表在使用前需要通过 `create` 显式创建。

支持以下创建选项：

**`create-options`** : `create-option | create-options`

**`create-option`** : `type` `table-type |` `valtype` `value-mask |` `algo` `algo-desc |` `limit` `number |` `locked |` `missing |` `or-flush`

**`type`** 表键类型。

**`valtype`** 表值掩码。

**`algo`** 要使用的表算法（见下文）。

**`limit`** 可以插入表中的最大条目数。

**`locked`** 限制任何表修改。

**`missing`** 如果表已存在且具有与新表完全相同的选项，则不会失败。

**`or-flush`** 刷新具有相同名称的现有表而不是返回错误。隐含 `missing`，因此现有表必须与新表兼容。

某些选项可以在稍后通过 `modify` 关键字修改。以下选项可以更改：

**`modify-options`** : `modify-option | modify-options`

**`modify-option`** : `limit` `number`

**`limit`** 更改可以插入表中的最大条目数。

此外，可以使用 `lock` 或 `unlock` 命令锁定或解锁表。

相同 `type` 的表可以使用 `swap` `name` 命令相互交换。如果设置了表限制且数据交换会导致达到限制，则交换可能失败。操作以原子方式执行。

可以使用 `add` 命令一次向表中添加一个或多个条目。所有条目的添加以原子方式执行。默认情况下，一个条目添加中的错误不会影响其他条目的添加。但是，在这种情况下会返回非零错误代码。可以在 `add` 之前指定特殊的 `atomic` 关键字以指示全有或全无的添加请求。

可以使用 `delete` 命令一次从表中删除一个或多个条目。默认情况下，一个条目删除中的错误不会影响其他条目的删除。但是，在这种情况下会返回非零错误代码。

可以使用 `lookup` `table-key` 命令检查在特定 `table-key` 上将找到什么条目。此功能是可选的，在某些算法中可能不受支持。

以下操作可以在 `一个` 或 `所有` 表上执行：

**`list`** 列出所有条目。

**`flush`** 删除所有条目。

**`info`** 显示通用表信息。

**`detail`** 显示通用表信息和算法特定数据。

支持以下查找算法：

**`algo-desc : algo-name | algo-name algo-data`**

**`algo-name`** : `addr: radix | addr: hash | iface: array | number: array | flow: hash | mac: radix`

**`addr: radix`** IPv4 和 IPv6 的独立 Radix 树，与路由表相同（参见 route(4)）。`addr` 类型的默认选择。

**`addr:hash`** IPv4 和 IPv6 的独立自动增长哈希。接受通过 `addr:hash masks=/v4,/v6` 算法创建选项初始指定的相同掩码长度的条目。默认假定 /32 和 /128 掩码。搜索从提供的地址中移除主机位（根据掩码）并检查适当哈希中的结果键。主要针对 /64 和字节范围的 IPv6 掩码进行优化。

**`iface:array`** 存储系统中存在的条目的排序索引的数组。针对非常快速的查找进行了优化。

**`number:array`** 存储排序的 u32 数字的数组。

**`flow:hash`** 存储流条目的自动增长哈希。搜索计算所需数据包字段上的哈希并在所选桶中搜索匹配条目。

**`mac: radix`** MAC 地址的 Radix 树。

`tablearg` 功能提供了使用在表中查找的值作为规则动作、动作参数或规则选项的参数的能力。这可以在某些配置中显著减少规则数量。如果在规则中使用两个表，则使用第二个（目的）表的结果。

每条记录可以根据 `value-mask` 保存一个或多个值。此掩码在创建表时通过 `valtype` 选项设置。支持以下值类型：

**`value-mask`** : `value-type`[,`value-mask`]

**`value-type`** : `skipto | pipe | fib | nat | dscp | tag | divert |` `netgraph | limit | ipv4 | ipv6 | mark`

**`skipto`** 要跳转到的规则编号。

**`pipe`** 要使用的 pipe 编号。

**`fib`** 要匹配/设置的 fib 编号。

**`nat`** 要跳转到的 nat 编号。

**`dscp`** 要匹配/设置的 dscp 值。

**`tag`** 要匹配/设置的标签编号。

**`divert`** 要将流量 divert 到的端口号。

**`netgraph`** 要将数据包移动到的 hook 编号。

**`limit`** 最大连接数。

**`ipv4`** 用于 fwd 数据包的 IPv4 下一跳。

**`ipv6`** 用于 fwd 数据包的 IPv6 下一跳。

**`mark`** 要匹配/设置的标记值。

`tablearg` 参数可用于以下动作：`nat`、`pipe`、`queue`、`divert`、`tee`、`netgraph`、`ngtee`、`fwd`、`skipto`、`setfib`、`setmark`，动作参数：`tag`、`untag`，规则选项：`limit`、`tagged`、`mark`。

与 `skipto` 动作一起使用时，用户应注意代码将遍历规则集直到等于或超过给定编号的规则。

有关表和 tablearg 关键字的示例用法，请参见"实例"章节。

## 规则集合（SETS OF RULES）

每条规则或表属于 32 个不同 *集合* 之一，编号 0 到 31。Set 31 保留给默认规则。

默认情况下，规则或表放入 set 0，除非在添加新规则或表时使用 `set N` 属性。集合可以单独且原子地启用或禁用，因此此机制允许存储防火墙的多个配置并快速（且原子地）在它们之间切换的简便方法。

默认情况下，添加带有表操作码的规则时引用 set 0 中的表，而不考虑规则集。可以通过将 `net.inet.ip.fw.tables_sets` 变量设置为 1 来更改此行为。然后将使用规则的集合进行表引用。

启用/禁用集合的命令是

```
ipfw set [disable number ...] [enable number ...]
```

其中可以指定多个 `enable` 或 `disable` 部分。命令执行在命令中指定的所有集合上都是原子的。默认情况下，所有集合都已启用。

当你禁用一个集合时，其规则的行为就像它们不存在于防火墙配置中一样，只有一个例外：

> 在规则被禁用之前从其创建的动态规则仍将保持活动状态，直到它们过期。
> 要删除动态规则，你必须显式删除生成它们的父规则。

可以使用以下命令更改规则的集合编号

```
ipfw set move {rule rule-number | old-set} to new-set
```

此外，你可以使用以下命令原子地交换两个规则集

```
ipfw set swap first-set second-set
```

有关规则集合的一些可能用法，请参见"实例"章节。

## 有状态防火墙（STATEFUL FIREWALL）

有状态操作是防火墙在检测到匹配给定模式的数据包时为特定流动态创建规则的一种方式。有状态操作的支持通过规则的 `check-state`、`keep-state`、`record-state`、`limit` 和 `set-limit` 选项实现。

当数据包匹配 `keep-state`、`record-state`、`limit` 或 `set-limit` 规则时，会创建动态规则，该规则将匹配给定 *协议* 在一对 *src-ip/src-port dst-ip/dst-port* 地址之间的所有且仅那些数据包（这里使用 *src* 和 *dst* 仅表示初始匹配地址，但之后它们完全等效）。由 `keep-state` 选项创建的规则还具有从其获取的 `:flowname`。此名称与地址、端口和协议一起用于匹配。动态规则将在第一次 `check-state`、`keep-state` 或 `limit` 出现时检查，匹配时执行的动作将与父规则中的相同。

请注意，动态规则上不检查协议和 IP 地址及端口及 :flowname 之外的任何其他属性。

动态规则的典型用途是保持防火墙配置关闭，但让来自内部网络的第一个 TCP SYN 数据包为该流安装动态规则，以便属于该会话的数据包将被允许通过防火墙：

```sh
ipfw add check-state :OUTBOUND
```

```sh
ipfw add allow tcp from my-subnet to any setup keep-state :OUTBOUND
```

```sh
ipfw add deny tcp from any to any
```

类似的方法可用于 UDP，其中来自内部的 UDP 数据包将安装动态规则以让响应通过防火墙：

```sh
ipfw add check-state :OUTBOUND
```

```sh
ipfw add allow udp from my-subnet to any keep-state :OUTBOUND
```

```sh
ipfw add deny udp from any to any
```

动态规则在一段时间后过期，这取决于流的状态和某些 `sysctl` 变量的设置。有关更多详细信息，请参见"SYSCTL 变量"章节。对于 TCP 会话，可以指示动态规则定期发送 keepalive 数据包以在规则即将过期时刷新其状态。

有关如何使用动态规则的更多示例，请参见"实例"章节。

## 流量整形器（DUMMYNET）配置

`ipfw` 也是 `dummynet` 流量整形器、包调度器和网络模拟器的用户界面，这是一个可以人为排队、延迟或丢弃数据包以模拟某些网络链路或排队系统行为的子系统。

`dummynet` 首先使用防火墙使用任何可在 `dummynet` 规则中使用的匹配模式来选择数据包。匹配的数据包然后被传递到两个不同的对象之一，这些对象实现流量调节：

***pipe*** *pipe* 模拟具有给定带宽和传播延迟的 *链路*，由 FIFO 调度器和具有可编程队列大小和数据包丢失率的单个队列驱动。数据包从 `ipfw` 出来时被附加到队列，然后以所需速率按 FIFO 顺序传输到链路。

***queue*** *queue* 是用于使用多种包调度算法之一实现包调度的抽象。发送到 *queue* 的数据包首先根据 5 元组上的掩码分组为流。然后将流传递到与 *queue* 关联的调度器，每个流使用 *queue* 本身中配置的调度参数（权重等）。调度器反过来连接到模拟链路，并根据权重和所使用调度算法的特性在积压流之间仲裁链路的带宽。

实际上，*pipes* 可用于设置流可以使用的带宽的硬限制，而 *queues* 可用于确定不同流如何共享可用带宽。

队列、流、调度器和链路绑定的图形表示如下。

```sh
                 (flow_mask|sched_mask)  sched_mask
         +---------+   weight Wx  +-------------+
         |         |->-[flow]-->--|             |-+
    -->--| QUEUE x |   ...        |             | |
         |         |->-[flow]-->--| SCHEDuler N | |
         +---------+              |             | |
             ...                  |             +--[LINK N]-->--
         +---------+   weight Wy  |             | +--[LINK N]-->--
         |         |->-[flow]-->--|             | |
    -->--| QUEUE y |   ...        |             | |
         |         |->-[flow]-->--|             | |
         +---------+              +-------------+ |
                                    +-------------+
```

理解通过以下命令配置的 SCHED_MASK 和 FLOW_MASK 的作用非常重要

```sh
ipfw sched N config mask SCHED_MASK ...
```

和

```sh
ipfw queue X config mask FLOW_MASK ... .
```

SCHED_MASK 用于将流分配给一个或多个调度器实例，每个实例对应应用 SCHED_MASK 后数据包 5 元组的一个值。例如，使用 "src-ip 0xffffff00" 为每个 /24 目的子网创建一个实例。

FLOW_MASK 与 SCHED_MASK 一起用于将数据包拆分为流。例如，将 "src-ip 0x000000ff" 与前面的 SCHED_MASK 一起使用会为每个单独的源地址创建一个流。反过来，每个 /24 子网的流将被发送到同一个调度器实例。

上图即使对于 *pipe* 情况也成立，唯一的限制是 *pipe* 仅支持 SCHED_MASK，并强制使用 FIFO 调度器（这些是出于向后兼容性原因；实际上，在内部，`dummynet` 的 pipe 完全按上述方式实现）。

`dummynet` 操作有两种模式："normal" 和 "fast"。"normal" 模式尝试模拟真实链路：`dummynet` 调度器确保数据包不会比在具有给定带宽的真实链路上更快地离开 pipe。"fast" 模式允许某些数据包绕过 `dummynet` 调度器（如果数据包流不超过 pipe 的带宽）。这就是 "fast" 模式每数据包需要更少 CPU 周期（平均）的原因，并且与具有相同带宽的真实链路相比，数据包延迟可以显著降低。默认模式是 "normal"。可以通过将 `net.inet.ip.dummynet.io_fast` sysctl(8) 变量设置为非零值来启用 "fast" 模式。

### PIPE、QUEUE 和调度器配置

*pipe*、*queue* 和 *scheduler* 配置命令如下：

```
pipe number config pipe-configuration
queue number config queue-configuration
sched number config sched-configuration
```

可以为 pipe 配置以下参数：

```sh
dnctl pipe 1 config bw 300Kbit/s
```

```sh
dnctl pipe 1 config bw tun0
```

```sh
      cumulative probability
      1.0 ^
          |
      L   +-- loss-level          x
          |                 ******
          |                *
          |           *****
          |          *
          |        **
          |       *
          +-------*------------------->
                      delay
```

**`name`** `identifier` 可选名称（由 "dnctl pipe show" 列出）用于标识延迟分布；

**`bw`** `value` 用于 pipe 的带宽。如果未在此处指定，则必须作为 pipe 的配置参数显式存在；

**`loss-level`** `L` 数据包丢失的概率上限。（0.0 <= L <= 1.0，默认 1.0 即无丢失）；

**`samples`** `N` 用于曲线内部表示的样本数（2..1024；默认 100）；

**`delay prob | prob delay`** 这两行之一是必需的，并定义了以下数据点行的格式。

**`XXX`** `YYY` 2 行或更多行表示曲线中的点，根据所选格式，先延迟或先概率。延迟的单位是毫秒。数据点不需要排序。此外，实际行数可以与 "samples" 参数的值不同：`bw` 工具将根据需要对曲线进行排序和插值。

```sh
name    bla_bla_bla
samples 100
loss-level    0.86
prob    delay
0       200	# 最小开销为 200ms
0.5     200
0.5     300
0.8     1000
0.9     1300
1       1300
#配置文件结束
```

**`bw`** `bandwidth | device` 带宽，以 [`K | M | G`] {`bit/s | Byte/s`} 为单位测量。值为 0（默认）表示无限带宽。单位必须紧跟在数字后面，如如果指定设备名称而不是数字值，如则发送时钟由指定设备提供。目前仅 tun(4) 设备支持此功能，用于与 ppp(8) 一起使用。
**`delay`** `ms-delay` 传播延迟，以毫秒为单位测量。该值四舍五入到时钟滴答的下一个倍数（通常为 10ms，但运行带有 "options HZ=1000" 的内核以将粒度减少到 1ms 或更低是良好的做法）。默认值为 0，表示无延迟。
**`burst`** `size` 如果要发送的数据超过 pipe 的带宽限制（且 pipe 之前是空闲的），则最多允许 `size` 字节的数据绕过 `dummynet` 调度器，并将以物理链路允许的最快速度发送。任何额外数据将以 `pipe` 带宽指定的速率传输。突发大小取决于 pipe 空闲的时间长度；有效突发大小计算如下：MAX(`size`, `bw` * pipe_idle_time)。
**`profile`** `filename` 指定在链路上传输数据包时产生的额外开销的文件。某些链路类型在传输数据包时会引入额外延迟，例如，由于 MAC 级别成帧、争用通道使用权、MAC 级别重传等。从我们的角度来看，通道在这段额外时间内实际上是不可用的，这取决于链路类型是恒定的还是可变的。此外，数据包可能在此时间后被丢弃（例如，在无线链路上重传次数过多后）。我们可以用代表其分布的经验曲线来建模额外延迟。经验曲线可以具有垂直线和水平线。垂直线表示一系列概率的恒定延迟。水平线对应于延迟分布中的不连续性：pipe 将使用给定概率的最大延迟。文件格式如下，其中空格作为分隔符，'#' 表示注释的开始：配置文件示例：

可以为 queue 配置以下参数：

**`pipe`** `pipe_nr` 将队列连接到指定的 pipe。多个队列（具有相同或不同权重）可以连接到同一个 pipe，该 pipe 指定队列集合的聚合速率。
**`weight`** `weight` 指定用于匹配此队列的流的权重。权重必须在 1..100 范围内，默认为 1。

可以为调度器配置以下不区分大小写的参数：

**`fifo`** 只是 FIFO 调度器（意味着所有数据包按到达调度器的顺序存储在同一队列中）。FIFO 具有 O(1) 的每数据包时间复杂度，常数非常低（在 2GHz 桌面机器上估计 60-80ns），但不提供服务保证。
**`wf2q+`** 实现 WF2Q+ 算法，这是一种加权公平排队算法，允许流根据其权重共享带宽。请注意，权重不是优先级；即使是具有微小权重的流也永远不会饿死。WF2Q+ 具有 O(log N) 的每数据包处理成本，其中 N 是流数，是以前版本 dummynet 队列使用的默认算法。
**`rr`** 实现 Deficit Round Robin 算法，具有 O(1) 处理成本（大约每数据包 100-150ns）并允许根据权重分配带宽，但服务保证较差。
**`qfq`** 实现 QFQ 算法，这是 WF2Q+ 的非常快速变体，具有类似的服务保证和 O(1) 处理成本（大约每数据包 200-250ns）。
**`fq_codel`** 实现 FQ-CoDel（FlowQueue-CoDel）调度器/AQM 算法，使用修改的 Deficit Round Robin 调度器管理两个子队列列表（旧子队列和新子队列），为轻量级或短突发流提供短暂的优先级。默认情况下，子队列总数为 1024。FQ-CoDel 的内部动态创建子队列由 CoDel AQM 的单独实例控制。
**`fq_pie`** 实现 FQ-PIE（FlowQueue-PIE）调度器/AQM 算法，类似于 `fq_codel`，但使用每个子队列 PIE AQM 实例来控制队列延迟。

**`quantum`** `m` 指定调度器的量子（信用）。`m` 是队列在被移动到旧队列列表尾部之前可以服务的字节数。默认为 1514 字节，最大可接受值为 9000 字节。

**`limit`** `m` 指定调度器实例管理的所有队列的硬大小限制（以数据包为单位）。`m` 的默认值为 10240 个数据包，最大可接受值为 20480 个数据包。

**`flows`** `m` 指定 fq_* 创建和管理的流队列（子队列）总数。默认情况下，创建 fq_{codel/pie} 调度器实例时创建 1024 个子队列。最大可接受值为 65536。

**`type`** `{fifo | wf2q+ | rr | qfq | fq_codel | fq_pie}` 指定要使用的调度算法。`fq_codel` 从 `codel` 继承 AQM 参数和选项（见下文），`fq_pie` 从 `pie` 继承 AQM 参数和选项（见下文）。此外，`fq_codel` 和 `fq_pie` 都具有共享调度器参数，这些参数是：请注意，`fq_codel` 或 `fq_pie` 之后的任何标记都被视为 fq_{codel/pie} 的参数。因此，确保所有与 fq_{codel/pie} 无关的调度器配置选项都写在 `fq_codel/fq_pie` 标记之前。

除了类型之外，pipe 允许的所有参数也可以为调度器指定。

最后，可以为 pipe 和 queue 配置以下参数：

```sh
                        r
               .----------------.
               v                |
         .------------.   .------------.
         |     G      |   |     B      |
         |  drop (K)  |   |  drop (H)  |
         '------------'   '------------'
               |                ^
               '----------------'
                        p
```

**`net.inet.ip.dummynet.red_lookup_depth`** 指定链路空闲时计算平均队列的精度（默认为 256，必须大于零）

**`net.inet.ip.dummynet.red_avg_pkt_size`** 指定预期的平均数据包大小（默认为 512，必须大于零）

**`net.inet.ip.dummynet.red_max_pkt_size`** 指定预期的最大数据包大小，仅在队列阈值以字节为单位时使用（默认为 1500，必须大于零）。

**`alpha`** `n` `n` 是 0 到 7 之间的浮点数，指定用于丢包概率计算的队列延迟偏差的权重。默认值为 0.125。

**`beta`** `n` `n` 是 0 到 7 之间的浮点数，指定用于丢包概率计算的队列延迟趋势的权重。默认值为 1.25。

**`max_burst`** `time` PIE 不丢弃/标记数据包的最长时间段。默认值为 150ms，最大值为 10s。

**`max_ecnth`** `n` 即使启用了 ECN，当丢包概率变得高于 ECN 概率阈值 `max_ecnth` `n` 时，PIE 会丢弃数据包而不是标记它们，默认值为 0.1（即 10%），最大值为 1。

**`ecn | noecn`** 为启用 ECN 的 TCP 流启用或禁用 ECN 标记。默认禁用。

**`capdrop | nocapdrop`** 启用或禁用 cap drop 调整。默认启用 cap drop 调整。

**`drand | nodrand`** 启用或禁用丢包概率去随机化。去随机化消除了过于接近或过远丢弃数据包的问题。默认启用去随机化。

**`onoff`** 启用根据队列负载开启和关闭 PIE。如果启用此选项，当队列充满超过 1/3 时 PIE 开启。此选项默认禁用。

**`dre | ts`** 使用离开速率估计 `dre` 或时间戳 `ts` 计算队列延迟。默认使用 `dre`。

**`buckets`** `hash-table-size` 指定用于存储各种队列的哈希表的大小。默认值为 64，由 sysctl(8) 变量 `net.inet.ip.dummynet.hash_size` 控制，允许范围为 16 到 65536。
**`mask`** `mask-specifier` 由 `ipfw` 规则发送到给定 pipe 或 queue 的数据包可以进一步分类为多个流，每个流然后被发送到不同的 *动态* pipe 或 queue。流标识符是通过根据 pipe 或 queue 配置中的 `mask` 选项指定的方式掩码 IP 地址、端口和协议类型构造的。对于每个不同的流标识符，创建一个具有与原始对象相同参数的新 pipe 或 queue，匹配的数据包被发送到该 pipe 或 queue。因此，当使用 *动态 pipes* 时，每个流将获得与 pipe 定义的相同带宽，而当使用 *动态 queues* 时，每个流将与同一队列生成的其他流均匀共享父 pipe 的带宽（请注意，具有不同权重的其他队列可能连接到同一个 pipe）。可用的掩码说明符是以下一个或多个的组合：`dst-ip` `mask`、`dst-ip6` `mask`、`src-ip` `mask`、`src-ip6` `mask`、`dst-port` `mask`、`src-port` `mask`、`flow-id` `mask`、`proto` `mask` 或 `all`，其中后者意味着所有字段中的所有位都是有效的。
**`noerror`** 当数据包被 `dummynet` 队列或 pipe 丢弃时，错误通常会报告给内核中的调用例程，就像设备队列填满时一样。设置此选项会将数据包报告为成功交付，这对于某些实验设置可能是必需的，你想在这些设置中模拟远程路由器的丢失或拥塞。
**`plr`** `packet-loss-rate`
**`plr`** `K,p,H,r` 数据包丢失率。参数 `packet-loss-rate` 是 0 到 1 之间的浮点数，0 表示无丢失，1 表示 100% 丢失。当使用四个参数调用时，使用具有两个状态（Good 和 Bad）的简单 Gilbert-Elliott 通道模型。这具有相关的概率（`K` 和 `H`）用于丢失概率。这与文献不同，文献中该模型用成功传输的概率 k 和 h 描述。但是，从文献转换很容易：K = 1 - k; H = 1 - h 这是为了在接口内保持一致性，并允许在仅给出单个参数时快速重用丢失概率。此外，还给出了状态更改概率（`p` 和 `r`）。上述所有概率都在内部以 31 位表示。
**`queue`** {`slots | size``Kbytes`} 队列大小，以 `slots` 或 `KBytes` 为单位。默认值为 50 slots，这是以太网设备的典型队列大小。请注意，对于低速链路，你应该保持队列大小较短，否则你的流量可能会受到显著排队延迟的影响。例如，50 个最大大小的以太网数据包（1500 字节）意味着 600Kbit 或 30Kbit/s pipe 上 20s 的队列。如果从具有更大 MTU 的接口获取数据包，则会导致更糟糕的影响，例如，具有 16KB 数据包的环回接口。sysctl(8) 变量 *net.inet.ip.dummynet.pipe_byte_limit* 和 *net.inet.ip.dummynet.pipe_slot_limit* 控制可以指定的最大长度。
**`red | gred`** `w_q`/`min_th`/`max_th`/`max_p` [ecn] 使用 RED（随机早期检测）队列管理算法。`w_q` 和 `max_p` 是 0 到 1（含）之间的浮点数，而 `min_th` 和 `max_th` 是指定队列管理阈值的整数（如果队列以字节定义，则阈值以字节计算，否则以 slots 计算）。如果需要，这两个参数也可以具有相同的值。`dummynet` 还支持 gentle RED 变体（gred）和 ECN（显式拥塞通知）作为可选。三个 sysctl(8) 变量可用于控制 RED 行为：
**`codel`** [`target` `time` ][`interval` `time` ][`ecn |`]]] `noecn` ] 使用 CoDel（受控延迟）队列管理算法。`time` 默认解释为毫秒，但可以指定秒（s）、毫秒或微秒（us）。CoDel 根据数据包在队列中的逗留时间丢弃或标记（ECN）数据包。`target` `time`（默认 5ms）是 CoDel 允许的最低可接受持续队列延迟。CoDel 不会在数据包逗留时间高于 `target` `time` 后直接丢弃数据包，而是等待 `interval` `time`（默认 100ms）后再丢弃。`interval` `time` 应设置为所有预期连接的最大 RTT。`ecn` 为启用 ECN 的 TCP 流在队列延迟变高时启用（默认禁用）数据包标记（而不是丢弃）。请注意，`codel` 之后的任何标记都被视为 CoDel 的参数。因此，确保所有 pipe/queue 配置选项都写在 `codel` 标记之前。sysctl(8) 变量 `net.inet.ip.dummynet.codel.target` 和 `net.inet.ip.dummynet.codel.interval` 可用于设置 CoDel 默认参数。
**`pie`** [`target` `time` ][`tupdate` `time` ][]]] `alpha` `n` ][`beta` `n` ][`max_burst` `time` ][]]] `max_ecnth` `n` ][`ecn |` `noecn` ][`capdrop |`]] `nocapdrop` ][`drand |` `nodrand` ][`onoff`]] ][`dre |` `ts` ]] 使用 PIE（比例积分控制器增强）队列管理算法。PIE 根据入队过程中计算的丢包概率丢弃或标记数据包，旨在实现高吞吐量同时保持低队列延迟。在 `tupdate` `time`（默认 15ms）的规律时间间隔，后台进程根据 `target` `time`（默认 15ms）的队列延迟偏差和队列延迟趋势（重新）计算概率。PIE 使用离开速率估计方法近似当前队列延迟，或（可选）使用类似于 CoDel 的数据包时间戳方法。`time` 默认解释为毫秒，但可以指定秒（s）、毫秒或微秒（us）。其他 PIE 参数和选项如下：请注意，`pie` 之后的任何标记都被视为 PIE 的参数。因此确保所有 pipe/queue 配置选项都写在 `pie` 标记之前。sysctl(8) 变量可用于控制 `pie` 默认参数。有关更多详细信息，请参见"SYSCTL 变量"章节。

当与 IPv6 数据一起使用时，`dummynet` 目前有一些限制。链路本地数据包路由到接口所需的信息在 `dummynet` 处理后不可用，因此这些数据包在输出路径上被丢弃。应注意确保链路本地数据包不会传递到 `dummynet`。

## 检查清单（CHECKLIST）

以下是设计规则时需要考虑的一些重要点：

- 请记住，你需要过滤 `in` 和 `out` 两个方向的数据包。大多数连接需要双向数据包。
- 请记住要非常仔细地测试。这样做时最好靠近控制台。如果你不能靠近控制台，请使用自动恢复脚本，如 **/usr/share/examples/ipfw/change_rules.sh** 中的脚本。
- 不要忘记环回接口。

## 注意事项（FINE POINTS）

```sh
kldload ipfw && ipfw add 32000 allow ip from any to any
```

```sh
ipfw flush
```

- 在某些情况下，分片数据报会被无条件丢弃。如果 TCP 数据包不包含至少 20 字节的 TCP 头部，则会被丢弃；如果 UDP 数据包不包含完整的 8 字节 UDP 头部，则会被丢弃；如果 ICMP 数据包不包含 4 字节的 ICMP 头部（足以指定 ICMP 类型、代码和校验和），则会被丢弃。这些数据包仅被记录为 "pullup failed"，因为数据包中可能没有足够的好数据来产生有意义的日志条目。
- 另一种类型的数据包会被无条件丢弃，即分片偏移量为 1 的 TCP 数据包。这是有效的数据包，但它只有一个用途，即试图绕过防火墙。启用日志记录时，这些数据包被报告为由规则 -1 丢弃。
- 如果你通过网络登录，加载 dummynet 的 kld(4) 版本可能不像你想象的那么简单。建议使用以下命令行：在类似环境中执行 `ipfw flush` 也是个坏主意。
- 如果系统安全级别设置为 3 或更高，则无法修改 `dummynet` 过滤列表（有关系统安全级别的信息，请参见 init(8)）。

## 数据包分流（PACKET DIVERSION）

绑定到指定端口的 divert(4) 套接字将接收所有 divert 到该端口的数据包。如果没有套接字绑定到目标端口，或者如果 divert 模块未加载，或者如果内核未编译 divert 套接字支持，则数据包将被丢弃。

## 网络地址转换（NAT）

`ipfw` 使用 libalias(3) 的内核版本支持内核内 NAT。应加载内核模块 `ipfw_nat` 或内核应具有 `options IPFIREWALL_NAT` 才能使用 NAT。

nat 配置命令如下：

```
nat nat_number config nat-configuration
```

可以配置以下参数：

**`ip`** `ip_address` 定义用于别名化的 IP 地址。

**`if`** `nic` 使用 NIC 的 IP 地址进行别名化，如果 NIC 的 IP 地址更改则动态更改。

**`log`** 在此 nat 实例上启用日志记录。

**`deny_in`** 拒绝来自外部的任何传入连接。

**`same_ports`** 尝试使别名端口号与实际本地端口号保持不变。

**`unreg_only`** 来自非 RFC 1918 未注册地址空间的本地网络流量将被忽略。

**`unreg_cgn`** 类似于 unreg_only，但包括 RFC 6598（运营商级 NAT）地址范围。

**`reset`** 在地址更改时重置数据包别名引擎的表。

**`reverse`** 反转 libalias 处理别名化的方式。

**`proxy_only`** 仅遵守透明代理规则，不执行数据包别名化。

**`skip_global`** 在全局状态查找时跳过实例（见下文）。

**`port_range`** `lower-upper` 设置给定范围内的别名化端口。端口必须在 1024-65535 范围内。上端口必须大于下端口。

**`udp_eim`** 启用时，UDP 数据包使用 RFC 4787 的端点无关映射（EIM）（RFC 3489 的 "full cone" NAT）。来自同一内部地址:端口的所有数据包都映射到相同的 NAT 地址:端口，而不考虑其目标地址:端口。如果过滤规则允许，且未设置 *deny_in*，任何其他外部地址:端口也可以通过其映射的 NAT 地址:端口发送到内部地址:端口。这与应用程序更兼容，可以减少端口转发的需求，但可扩展性较差，因为每个 NAT 地址:端口最多只能由一个内部地址:端口同时使用。禁用时，UDP 数据包使用端点相关映射（EDM）（"对称" NAT）。从特定内部地址:端口到不同外部地址:端口的每个连接都映射到随机且不可预测的 NAT 地址:端口。EDM NAT 后面的两个应用程序只能通过 NAT 上的端口转发或通过中间服务器进行隧道连接来相互连接。

可以在 nat 规则动作中使用一些特殊值代替 `nat_number`：

**`global`** 在所有配置的 nat 实例中查找转换状态。如果找到条目，数据包将根据该条目进行别名化。如果在任何实例中均未找到条目，数据包将 unchanged 通过，且不会创建新条目。有关更多信息，请参见 natd(8) 中的"多个实例"章节。

**`tablearg`** 使用查找表中提供的参数。有关查找表的更多信息，请参见下面的"查找表"章节。

要让数据包在被（去）别名化后继续，将 sysctl 变量 `net.inet.ip.fw.one_pass` 设置为 0。有关别名化模式的更多信息，请参见 libalias(3)。有关 nat 用法的一些示例，请参见"实例"章节。

要删除特定的 nat 配置实例，请使用以下命令：

```
nat nat_number delete
```

### IPFW 中的重定向和 LSNAT 支持

重定向和 LSNAT 支持密切遵循 natd(8) 中使用的语法。有关如何进行重定向和 lsnat 的一些示例，请参见"实例"章节。

### SCTP NAT 支持

SCTP nat 可以通过 `ipfw` 命令行工具以类似于 TCP 的方式进行配置。主要区别在于 `sctp` 不进行端口转换。由于本地和全局端口的端口相同，因此无需指定两者。端口按如下方式重定向：

```
nat nat_number config if nic redirect_port sctp ip_address [,addr_list] {[port | port-port] [,ports]}
```

大多数 `sctp` 配置可以通过 sysctl(8) 接口实时完成。所有配置都可以动态更改，尽管 hash_table 大小仅对新 `nat` 实例更改。有关更多信息，请参见"SYSCTL 变量"章节。

## IPv6/IPv4 网络地址和协议转换

### 有状态转换

`ipfw` 支持内核内 IPv6/IPv4 网络地址和协议转换。有状态 NAT64 转换允许仅 IPv6 客户端使用单播 TCP、UDP 或 ICMP 协议联系 IPv4 服务器。分配给有状态 NAT64 转换器的一个或多个 IPv4 地址在多个仅 IPv6 客户端之间共享。当有状态 NAT64 与 DNS64 一起使用时，通常不需要更改 IPv6 客户端或 IPv4 服务器。应加载内核模块 `ipfw_nat64` 或内核应具有 `options IPFIREWALL_NAT64` 才能使用有状态 NAT64 转换器。

有状态 NAT64 为几种类型的对象使用大量内存。当 IPv6 客户端发起连接时，NAT64 转换器在状态表中创建主机条目。每个主机条目使用预分配的 IPv4 别名条目。每个别名条目具有按需分配的多个端口组条目。端口组条目包含连接状态条目。有多个选项可以控制这些对象的限制和生存期。

NAT64 转换器在执行 ICMPv6/ICMP 转换时遵循 RFC7915，不支持的消息类型将被静默丢弃。IPv6 需要显式允许几种 ICMPv6 消息类型才能正确操作。确保 ND6 邻居请求（ICMPv6 类型 135）和邻居通告（ICMPv6 类型 136）消息不会被转换规则处理。

转换后，NAT64 转换器默认通过相应的 netisr 队列发送数据包。因此，转换器主机应配置为 IPv4 和 IPv6 路由器。这也意味着数据包由防火墙处理两次。第一次处理并消耗原始数据包，然后作为转换后的数据包再次处理。此行为可以通过 sysctl 变量 `net.inet.ip.fw.nat64_direct_output` 更改。转换后的数据包也可以使用 `tag` 规则动作进行标记，然后由 `tagged` 操作码匹配以避免循环和额外开销。

有状态 NAT64 配置命令如下：

```
nat64lsn name create create-options
```

可以配置以下参数：

**`prefix4`** `ipv4_prefix/plen` 带掩码的 IPv4 前缀定义了转换后用作源地址的 IPv4 地址池。有状态 NAT64 模块将客户端的 IPv6 源地址转换为此池中的一个 IPv4 地址。请注意，状态表中没有相应状态条目的传入 IPv4 数据包将被转换器丢弃。确保转换规则处理发往配置前缀的数据包。

**`prefix6`** `ipv6_prefix/length` IPv6 前缀定义了转换器用于表示 IPv4 地址的 IPv4 嵌入式 IPv6 地址。此 IPv6 前缀应在 DNS64 中配置。转换器实现遵循 RFC6052，将前缀长度限制为以下之一：32、40、48、56、64 或 96。Well-Known IPv6 前缀 64:ff9b:: 必须为 96 位长。特殊 `::/length` 前缀可用于使用一个 NAT64 实例处理多个 IPv6 前缀。NAT64 实例将从前缀 `length` 确定目标 IPv4 地址。

**`states_chunks`** `number` 单个端口组中的状态块数。默认情况下，每个端口组可以在单个块中保留 64 个状态条目。上述值影响可与单个 IPv4 别名地址和端口关联的最大状态数。该值必须是 2 的幂，最多为 128。

**`host_del_age`** `seconds` 由于不活动，IPv6 客户端的主机条目将被删除且其所有资源将被释放之前的秒数。默认值为 `3600`。

**`pg_del_age`** `seconds` 具有未使用状态条目的端口组将被释放之前的秒数。默认值为 `900`。

**`tcp_syn_age`** `seconds` 仅发送 SYN 的 TCP 连接的状态条目将保持的秒数。如果 TCP 连接建立未完成，状态条目将被删除。默认值为 `10`。

**`tcp_est_age`** `seconds` 已建立的 TCP 连接的状态条目将保持的秒数。默认值为 `7200`。

**`tcp_close_age`** `seconds` 已关闭 TCP 连接的状态条目将保持的秒数。保留已关闭连接的状态条目是必需的，因为 IPv4 服务器通常在 TIME_WAIT 状态下保持已关闭连接几分钟。由于转换器的 IPv4 地址在所有 IPv6 客户端之间共享，来自相同地址和端口的新连接可能会被服务器拒绝，因为这些连接仍处于 TIME_WAIT 状态。在转换器的状态表中保留它们可以防止此类拒绝。默认值为 `180`。

**`udp_age`** `seconds` 转换器在等待对发送 UDP 数据报的回复时保持状态条目的秒数。默认值为 `120`。

**`icmp_age`** `seconds` 转换器在等待对发送 ICMP 消息的回复时保持状态条目的秒数。默认值为 `60`。

**`log`** 通过名为 `ipfwlog0` 的 BPF tap 开启所有处理数据包的日志记录。请注意，它的目的与每规则 bpf(4) tap 不同。转换器随每个数据包向 BPF 发送附加信息。使用 `tcpdump` 你能够看到每个处理的数据包在转换前后的情况。

**`-log`** 关闭通过 BPF 的所有处理数据包的日志记录。

**`allow_private`** 开启私有 IPv4 地址处理。默认情况下，目的地映射到 RFC1918 定义的私有地址范围的 IPv6 数据包不会被处理。

**`-allow_private`** 关闭 `nat64` 实例中的私有地址处理。

可以使用以下命令检查有状态 NAT64 的状态表：

```
nat64lsn name show states
```

无状态 NAT64 转换器不使用状态表进行转换，仅根据从配置的查找表中获取的映射将 IPv4 地址转换为 IPv6，反之亦然。由于无状态转换器不使用状态表，因此可以将其配置为将 IPv4 客户端传递到仅 IPv6 服务器。

无状态 NAT64 配置命令如下：

```
nat64stl name create create-options
```

可以配置以下参数：

**`prefix6`** `ipv6_prefix/length` IPv6 前缀定义了转换器用于表示 IPv4 地址的 IPv4 嵌入式 IPv6 地址。此 IPv6 前缀应在 DNS64 中配置。

**`table4`** `table46` 查找表 `table46` 包含 IPv4 地址应如何转换为 IPv6 地址的映射。

**`table6`** `table64` 查找表 `table64` 包含 IPv6 地址应如何转换为 IPv4 地址的映射。

**`log`** 通过 `ipfwlog0` tap 开启通过 BPF 的所有处理数据包的日志记录。

**`-log`** 关闭通过 BPF 的所有处理数据包的日志记录。

**`allow_private`** 开启私有 IPv4 地址处理。默认情况下，目的地映射到 RFC1918 定义的私有地址范围的 IPv6 数据包不会被处理。

**`-allow_private`** 关闭 `nat64` 实例中的私有地址处理。

请注意，无状态转换器对于不匹配数据包的行为与有状态转换器不同。如果在查找表中未找到相应地址，数据包将不会被丢弃，搜索将继续。

### XLAT464 CLAT 转换

XLAT464 CLAT NAT64 转换器实现了 RFC6877 中定义的客户端无状态转换，与上面解释的无状态 NAT64 转换器非常相似。它不使用查找表，而是使用配置的前缀在 IPv4 和 IPv6 地址之间进行一对一映射。此模式可用作不使用它的应用程序（例如 VoIP）的 DNS64 服务的替代方案，允许它们在远程 NAT64 转换器的帮助下通过仅 IPv6 网络访问仅 IPv4 互联网。

CLAT NAT64 配置命令如下：

```
nat64clat name create create-options
```

可以配置以下参数：

**`clat_prefix`** `ipv6_prefix/length` IPv6 前缀定义了转换器用于表示源 IPv4 地址的 IPv4 嵌入式 IPv6 地址。

**`plat_prefix`** `ipv6_prefix/length` IPv6 前缀定义了转换器用于表示目标 IPv4 地址的 IPv4 嵌入式 IPv6 地址。此 IPv6 前缀应在远程 NAT64 转换器上配置。

**`log`** 通过 `ipfwlog0` tap 开启通过 BPF 的所有处理数据包的日志记录。

**`-log`** 关闭通过 BPF 的所有处理数据包的日志记录。

**`allow_private`** 开启私有 IPv4 地址处理。默认情况下，`nat64clat` 实例不会处理目标地址来自 RFC1918 定义的私有范围的数据包。

**`-allow_private`** 关闭 `nat64clat` 实例中的私有地址处理。

请注意，CLAT 转换器对于不匹配数据包的行为与有状态转换器不同。如果相应地址与配置的前缀不匹配，数据包将不会被丢弃，搜索将继续。

## IPv6 到 IPv6 网络前缀转换（NPTv6）

`ipfw` 支持 RFC6296 中所述的内核内 IPv6 到 IPv6 网络前缀转换。应加载内核模块 `ipfw_nptv6` 或内核应具有 `options IPFIREWALL_NPTV6` 才能使用 NPTv6 转换器。

NPTv6 配置命令如下：

```
nptv6 name create create-options
```

可以配置以下参数：

**`int_prefix`** `ipv6_prefix` 内部网络中使用的 IPv6 前缀。当源地址匹配此前缀时，NPTv6 模块转换源地址。

**`ext_prefix`** `ipv6_prefix` 外部网络中使用的 IPv6 前缀。当目标地址匹配此前缀时，NPTv6 模块转换目标地址。

**`ext_if`** `nic` NPTv6 模块将使用接口 `nic` 的第一个全局 IPv6 地址作为外部前缀。当外部网络的 IPv6 前缀是动态获取时，这很有用。`ext_prefix` 和 `ext_if` 选项是互斥的。

**`prefixlen`** `length` 指定的 IPv6 前缀的长度。它必须在 8 到 64 的范围内。

请注意，当禁用 IPv6 数据包转发时，前缀转换规则会被静默忽略。要启用数据包转发，将 sysctl 变量 `net.inet6.ip6.forwarding` 设置为 1。

要让数据包在转换后继续，将 sysctl 变量 `net.inet.ip.fw.one_pass` 设置为 0。

## 加载器可调参数（LOADER TUNABLES）

可调参数可以在 loader(8) 提示符、loader.conf(5) 或 kenv(1) 中在 ipfw 模块加载前设置。

**`net.inet.ip.fw.enable`** : 1 启用防火墙。将此变量设置为 0 让你在即使编译进内核的情况下也可以在没有防火墙的情况下运行机器。

**`net.inet6.ip6.fw.enable`** : 1 为 IPv6 情况提供与上述相同的功能。

**`net.link.ether.ipfw`** : 0 控制 layer2 数据包是否传递给 `ipfw`。默认为否。

**`net.inet.ip.fw.default_to_accept`** : 0 定义 ipfw 最后一条规则的行为。此值覆盖内核配置文件中的 `options IPFW_DEFAULT_TO_(ACCEPT|DENY)`。

**`net.inet.ip.fw.tables_max`** : 128 定义 ipfw 中可用的表数量。数字不能超过 65534。

## SYSCTL 变量

一组 sysctl(8) 变量控制防火墙和关联模块（`dummynet`）的行为。这些变量如下所示，连同其默认值（但始终使用 sysctl(8) 命令检查实际使用的值）和含义：

**`0`** 无响应（除非存在部分匹配的关联——端口和 vtag 匹配但全局地址不匹配）

**`1`** `nat` 将接受并处理所有 OOTB 全局 AddIP 消息。

**`0`** 永远不会响应 OOTB 数据包发送 ErrorM。

**`1`** ErrorM 仅发送到在本地侧接收的 OOTB 数据包。

**`2`** ErrorM 发送到本地侧和全局侧，但仅当存在部分匹配时（端口和 vtag 匹配但源全局 IP 不匹配）。此值仅在 `nat` 跟踪全局 IP 地址时有用。

**`3`** ErrorM 响应本地和全局侧的所有 OOTB 数据包发送（DoS 风险）。

**`0`** 全局跟踪已禁用

**`>1`** 启用跟踪，每个关联跟踪的最大地址数限制为此值

**`0`** 数据包由 `ipfw` 处理两次。第一次由 `ipfw` 处理原始数据包并被 `ipfw_nat64` 转换器消耗。然后转换后的数据包通过 netisr 排队到输入处理再次。

**`1`** 数据包仅由 `ipfw` 处理一次，转换后它将被直接推送到输出接口。

**`net.inet.ip.alias.sctp.accept_global_ootb_addip`** : 0 定义 `nat` 如何响应接收全局 OOTB ASCONF-AddIP：选项 1 永远不应选择，因为这会形成安全风险。攻击者可以通过发送 AddIP 消息来建立多个虚假关联。

**`net.inet.ip.alias.sctp.chunk_proc_limit`** : 5 定义匹配现有关联的数据包中将解析的 SCTP 数据包中块的最大数量。此值被强制为大于或等于 `net.inet.ip.alias.sctp.initialising_chunk_proc_limit`。高值是 DoS 风险，但设置过低的值可能导致数据包中的重要控制块未被定位和解析。

**`net.inet.ip.alias.sctp.error_on_ootb`** : 1 定义 `nat` 何时响应任何 Out-of-the-Blue（OOTB）数据包发送 ErrorM 数据包。OOTB 数据包是在 `nat` 中没有注册现有关联且不是 INIT 或 ASCONF-AddIP 数据包的数据包：目前默认值为 0，因为 ErrorM 数据包尚未被大多数 SCTP 栈支持。当它被支持时，如果不跟踪全局地址，我们建议将此值设置为 1 以允许多宿主本地主机与 `nat` 一起工作。要跟踪全局地址，我们建议将此值设置为 2 以允许在需要（重新）发送 ASCONF-AddIP 时通知全局主机。值 3 永远不应选择（调试除外），因为 `nat` 将响应所有 OOTB 全局数据包（DoS 风险）。

**`net.inet.ip.alias.sctp.hashtable_size`** : 2003 用于 `nat` 查找的哈希表大小（100 < prime_number > 1000001）。此值为任何未来创建的 `nat` 实例设置 `hash` 大小，因此必须在创建 `nat` 实例之前设置。表大小可以根据特定需求更改。如果并发关联很少，且内存稀缺，可以使这些更小。如果有数千（或数百万）并发关联，应使这些更大。质数最适合表大小。sysctl 更新函数会将你的输入值调整为下一个最高质数。

**`net.inet.ip.alias.sctp.holddown_time`** : 0 在接收 SHUTDOWN-COMPLETE 后在表中保持关联这么多的秒数。这允许端点在 shutdown_complete 丢失且需要重传时正确地优雅关闭。

**`net.inet.ip.alias.sctp.init_timer`** : 15 等待（INIT-ACK|AddIP-ACK）时的超时值。此值不能为 0。

**`net.inet.ip.alias.sctp.initialising_chunk_proc_limit`** : 2 定义当不存在匹配该数据包的现有关联时，SCTP 数据包中将解析的块的最大数量。理想情况下，此数据包将仅为 INIT 或 ASCONF-AddIP 数据包。较高的值可能成为 DoS 风险，因为格式不正确的数据包会消耗处理资源。

**`net.inet.ip.alias.sctp.param_proc_limit`** : 25 定义数据包中块内将解析的参数的最大数量。与其他类似 sysctl 变量一样，较大的值会带来 DoS 风险。

**`net.inet.ip.alias.sctp.log_level`** : 0 系统日志消息中的详细级别（0 - 最少，1 - 事件，2 - 信息，3 - 详细，4 - 调试，5 - 最大调试）。在高丢包环境中可能是一个好选项。

**`net.inet.ip.alias.sctp.shutdown_time`** : 15 等待 SHUTDOWN-COMPLETE 时的超时值。此值不能为 0。

**`net.inet.ip.alias.sctp.track_global_addresses`** : 0 在 `nat` 中启用/禁用全局 IP 地址跟踪，并设置每个关联跟踪地址数的上限：此变量是完全动态的，新值将被所有新到达的关联采用，现有关联按之前方式处理。全局跟踪将以增加的处理负载、内存使用、复杂性以及可能的 `nat` 状态问题为代价减少 `nat` 内的冲突，在具有多个 `nat` 的复杂网络中。我们建议不跟踪全局 IP 地址，这仍将产生完全功能的 `nat`。

**`net.inet.ip.alias.sctp.up_timer`** : 300 在没有流量时保持关联的超时值。此值不能为 0。

**`net.inet.ip.dummynet.codel.interval`** : 100000 默认 `codel` AQM 间隔，以微秒为单位。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.codel.target`** : 5000 默认 `codel` AQM 目标延迟时间，以微秒为单位（最低可接受持续队列延迟）。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.expire`** : 1 在动态 pipe/queue 没有待处理流量时延迟删除它们。你可以通过将变量设置为 0 来禁用此功能，在这种情况下，pipe/queue 将仅在达到阈值时删除。

**`net.inet.ip.dummynet.fqcodel.flows`** : 1024 定义 `fq_codel` 创建和管理的默认流队列（子队列）总数。该值必须在 1..65536 范围内。

**`net.inet.ip.dummynet.fqcodel.interval`** : 100000 默认 `fq_codel` 调度器/AQM 间隔，以微秒为单位。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.fqcodel.limit`** : 10240 `fq_codel` 调度器实例管理的所有队列的默认硬大小限制（以数据包为单位）。该值必须在 1..20480 范围内。

**`net.inet.ip.dummynet.fqcodel.quantum`** : 1514 `fq_codel` 的默认量子（信用），以字节为单位。该值必须在 1..9000 范围内。

**`net.inet.ip.dummynet.fqcodel.target`** : 5000 默认 `fq_codel` 调度器/AQM 目标延迟时间，以微秒为单位（最低可接受持续队列延迟）。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.fqpie.alpha`** : 125 `fq_pie` 调度器/AQM 的默认 `alpha` 参数（乘以 1000）。该值必须在 1..7000 范围内。

**`net.inet.ip.dummynet.fqpie.beta`** : 1250 `fq_pie` 调度器/AQM 的默认 `beta` 参数（乘以 1000）。该值必须在 1..7000 范围内。

**`net.inet.ip.dummynet.fqpie.flows`** : 1024 定义 `fq_pie` 创建和管理的默认流队列（子队列）总数。该值必须在 1..65536 范围内。

**`net.inet.ip.dummynet.fqpie.limit`** : 10240 `fq_pie` 调度器实例管理的所有队列的默认硬大小限制（以数据包为单位）。该值必须在 1..20480 范围内。

**`net.inet.ip.dummynet.fqpie.max_burst`** : 150000 `fq_pie` 调度器/AQM 不丢弃/标记数据包的默认最长时间段，以微秒为单位。该值必须在 1..10000000 范围内。

**`net.inet.ip.dummynet.fqpie.max_ecnth`** : 99 `fq_pie` 调度器/AQM 的默认最大 ECN 概率阈值（乘以 1000）。该值必须在 1..7000 范围内。

**`net.inet.ip.dummynet.fqpie.quantum`** : 1514 `fq_pie` 的默认量子（信用），以字节为单位。该值必须在 1..9000 范围内。

**`net.inet.ip.dummynet.fqpie.target`** : 15000 `fq_pie` 的默认 `target` 延迟，以微秒为单位。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.fqpie.tupdate`** : 15000 `fq_pie` 的默认 `tupdate`，以微秒为单位。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.hash_size`** : 64 用于动态 pipe/queue 的哈希表的默认大小。当配置 pipe/queue 时未指定 `buckets` 选项时使用此值。

**`net.inet.ip.dummynet.io_fast`** : 0 如果设置为非零值，则启用 `dummynet` 操作的 "fast" 模式（见上文）。

**`net.inet.ip.dummynet.io_pkt`** 传递给 `dummynet` 的数据包数。

**`net.inet.ip.dummynet.io_pkt_drop`** 被 `dummynet` 丢弃的数据包数。

**`net.inet.ip.dummynet.io_pkt_fast`** 被 `dummynet` 调度器绕过的数据包数。

**`net.inet.ip.dummynet.max_chain_len`** : 16 哈希桶中 pipe/queue 的最大数量的目标值。乘积 `max_chain_len*hash_size` 用于确定即使 `net.inet.ip.dummynet.expire=0` 时也会过期空 pipe/queue 的阈值。

**`net.inet.ip.dummynet.red_lookup_depth`** : 256

**`net.inet.ip.dummynet.red_avg_pkt_size`** : 512

**`net.inet.ip.dummynet.red_max_pkt_size`** : 1500 用于 RED 算法的丢包概率计算中的参数。

**`net.inet.ip.dummynet.pie.alpha`** : 125 `pie` AQM 的默认 `alpha` 参数（乘以 1000）。该值必须在 1..7000 范围内。

**`net.inet.ip.dummynet.pie.beta`** : 1250 `pie` AQM 的默认 `beta` 参数（乘以 1000）。该值必须在 1..7000 范围内。

**`net.inet.ip.dummynet.pie.max_burst`** : 150000 `pie` AQM 不丢弃/标记数据包的默认最长时间段，以微秒为单位。该值必须在 1..10000000 范围内。

**`net.inet.ip.dummynet.pie.max_ecnth`** : 99 `pie` AQM 的默认最大 ECN 概率阈值（乘以 1000）。该值必须在 1..7000 范围内。

**`net.inet.ip.dummynet.pie.target`** : 15000 `pie` AQM 的默认 `target` 延迟，以微秒为单位。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.pie.tupdate`** : 15000 `pie` AQM 的默认 `tupdate`，以微秒为单位。该值必须在 1..5000000 范围内。

**`net.inet.ip.dummynet.pipe_byte_limit`** : 1048576

**`net.inet.ip.dummynet.pipe_slot_limit`** : 100 可以以字节或数据包指定的最大队列大小。这些限制可防止意外耗尽 mbuf 等资源。如果提高这些限制，应确保系统配置为有足够的资源可用。

**`net.inet.ip.fw.autoinc_step`** : 100 自动生成规则编号时规则编号之间的增量。该值必须在 1..1000 范围内。

**`net.inet.ip.fw.curr_dyn_buckets`** : `net.inet.ip.fw.dyn_buckets` 动态规则哈希表中当前的桶数（只读）。

**`net.inet.ip.fw.debug`** : 1 控制 `ipfw` 产生的调试消息。

**`net.inet.ip.fw.default_rule`** : 65535 默认规则编号（只读）。按设计，它也可以作为规则允许的最高编号。

**`net.inet.ip.fw.dyn_buckets`** : 256 动态规则哈希表中的桶数。必须是 2 的幂，最多 65536。它仅在所有动态规则过期后才生效，因此建议使用 `flush` 命令以确保调整哈希表大小。

**`net.inet.ip.fw.dyn_count`** : 3 当前动态规则数（只读）。

**`net.inet.ip.fw.dyn_keepalive`** : 1 为 `keep-state` 规则在 TCP 会话上启用 keepalive 数据包生成。在规则生存期的最后 20 秒内，每 5 秒向连接的双方生成一次 keepalive。

**`net.inet.ip.fw.dyn_max`** : 8192 最大动态规则数。当达到此限制时，在旧规则过期之前无法安装更多动态规则。

**`net.inet.ip.fw.dyn_ack_lifetime`** : 300

**`net.inet.ip.fw.dyn_syn_lifetime`** : 20

**`net.inet.ip.fw.dyn_fin_lifetime`** : 1

**`net.inet.ip.fw.dyn_rst_lifetime`** : 1

**`net.inet.ip.fw.dyn_udp_lifetime`** : 5

**`net.inet.ip.fw.dyn_short_lifetime`** : 30 这些变量控制动态规则的生存期（以秒为单位）。在初始 SYN 交换期间，生存期保持较短，然后在看到两个 SYN 后增加，最后在最终 FIN 交换期间或收到 RST 时再次减少。*dyn_fin_lifetime* 和 *dyn_rst_lifetime* 都必须严格低于 5 秒，即 keepalive 的重复周期。防火墙强制执行此要求。

**`net.inet.ip.fw.dyn_keep_states`** : 0 在规则/集合删除时保留动态状态。状态重新链接到默认规则（65535）。这对于规则集重新加载可能很方便。默认关闭。

**`net.inet.ip.fw.one_pass`** : 1 设置时，从 `dummynet` pipe 或从 ng_ipfw(4) 节点退出的数据包不会再次通过防火墙。否则，在动作之后，数据包在下一条规则处重新注入防火墙。

**`net.inet.ip.fw.tables_max`** : 128 最大表数。

**`net.inet.ip.fw.verbose`** : 1 启用详细消息。

**`net.inet.ip.fw.verbose_limit`** : 0 限制详细防火墙产生的消息数。

**`net.inet6.ip6.fw.deny_unknown_exthdrs`** : 1 如果启用，具有未知 IPv6 扩展头部的数据包将被拒绝。

**`net.link.bridge.ipfw`** : 0 控制桥接数据包是否传递给 `ipfw`。默认为否。

**`net.inet.ip.fw.nat64_debug`** : 0 控制 `ipfw_nat64` 模块产生的调试消息。

**`net.inet.ip.fw.nat64_direct_output`** : 0 控制 `ipfw_nat64` 模块使用的输出方法：

## 内部诊断

内核模块内部有一些命令可用于了解某些子系统的当前状态。这些命令提供的调试输出可能会在不通知的情况下更改。

目前以下命令作为 `internal` 子选项可用：

**`iflist`** 列出当前由 `ipfw` 跟踪的所有接口及其内核内状态。

**`monitor`** [`filter-comment`] 捕获来自 [route(4)](../man4/route.4.md) 套接字的消息，这些消息是使用带有 `log` `logdst` `rtsock` 操作码的规则记录的。可以指定可选的 `filter-comment`，仅显示由具有特定规则注释的规则记录的消息。

**`talist`** 列出当前可用的所有表查找算法。

## 实例

`ipfw` 的可能用途太多，因此本节只给出少量示例。

### 基本包过滤

以下命令添加一条规则，拒绝从 *cracker.evil.org* 到 *wolf.tambov.su* 的 telnet 端口的所有 tcp 数据包被主机转发：

```sh
ipfw add deny tcp from cracker.evil.org to wolf.tambov.su telnet
```

以下命令禁止从整个 cracker 的网络到我的主机的任何连接：

```sh
ipfw add deny ip from 123.45.67.0/24 to my.host.org
```

限制访问（不使用动态规则）的第一个有效方法是使用以下规则：

```sh
ipfw add allow tcp from any to any established
```

```sh
ipfw add allow tcp from net1 portlist1 to net2 portlist2 setup
```

```sh
ipfw add allow tcp from net3 portlist3 to net3 portlist3 setup
```

```sh
...
```

```sh
ipfw add deny tcp from any to any
```

第一条规则将快速匹配普通 TCP 数据包，但不会匹配初始 SYN 数据包，初始 SYN 数据包只会被仅针对选定源/目的对的 `setup` 规则匹配。所有其他 SYN 数据包将被最后的 `deny` 规则拒绝。

如果你管理一个或多个子网，可以利用地址集和 or 块的优势，编写极其紧凑的规则集，有选择地为客户端块启用服务，如下所示：

```sh
goodguys={ 10.1.2.0/24{20,35,66,18} or 10.2.3.0/28{6,3,11} }
```

```sh
badguys=10.1.2.0/24{8,38,60}
```

```sh

```

```sh
ipfw add allow ip from ${goodguys} to any
```

```sh
ipfw add deny ip from ${badguys} to any
```

```sh
... normal policies ...
```

允许来自单个 vlan 10 并发往 vlans 100-1000 的所有传输数据包：

```sh
ipfw add 10 allow out recv vlan10 e
```

```sh
{ xmit vlan1000 or xmit lan[1-9]?? }
```

可以通过在规则集顶部添加以下规则来使用 `verrevpath` 选项执行自动反欺骗：

```sh
ipfw add deny ip from any to any not verrevpath in
```

此规则丢弃所有看似从错误接口进入系统的传入数据包。例如，如果源地址属于受保护内部网络上主机的数据包试图从外部接口进入系统，则会被丢弃。

可以通过在规则集顶部添加以下规则来使用 `antispoof` 选项执行类似但更受限的反欺骗：

```sh
ipfw add deny ip from any to any not antispoof in
```

此规则丢弃所有看似来自另一个直接连接的系统但从错误接口进入的传入数据包。例如，配置在 `fxp0` 上的源地址为 **192.168.0.0/24** 但从 `fxp1` 进入的数据包将被丢弃。

可以通过在规则集中的适当位置添加以下规则来使用 `setdscp` 选项（重新）标记用户流量：

```sh
ipfw add setdscp be ip from any to any dscp af11,af21
```

### 选择性镜像

如果你的网络具有通过专用接口直接连接到主机或通过 RSPAN vlan 远程连接的网络流量分析器，则可以选择性地将某些以太网 layer2 帧镜像到分析器。

首先，确保防火墙已配置并运行。然后，如果尚未启用 layer2 处理，则启用它：

```sh
sysctl net.link.ether.ipfw=1
```

接下来，加载所需的额外内核模块：

```sh
kldload ng_ether ng_ipfw
```

可选地，使系统在启动时自动加载这些模块：

```sh
sysrc kld_list+="ng_ether ng_ipfw"
```

接下来，配置 [ng_ipfw(4)](../man4/ng_ipfw.4.md) 内核模块以通过 vlan900 接口向外传输 layer2 帧的镜像副本：

```sh
ngctl connect ipfw: vlan900: 1 lower
```

将此处的 "1" 视为"镜像实例索引"，vlan900 是其目标。你可以有任意数量的实例。有关详细信息，请参阅 [ng_ipfw(4)](../man4/ng_ipfw.4.md)。

最后，使用"实例 1"实际开始镜像所选帧。对于来自 em0 接口的传入帧：

```sh
ipfw add ngtee 1 ip from any to 192.168.0.1 layer2 in recv em0
```

对于发往 em0 接口的传出帧：

```sh
ipfw add ngtee 1 ip from any to 192.168.0.1 layer2 out xmit em0
```

对于流经 em0 时的传入和传出帧：

```sh
ipfw add ngtee 1 ip from any to 192.168.0.1 layer2 via em0
```

确保不对已复制的帧执行镜像，否则内核可能会挂起，因为没有安全网。

### 动态规则

为了保护站点免受涉及伪造 TCP 数据包的洪水攻击，使用动态规则更安全：

```sh
ipfw add check-state
```

```sh
ipfw add deny tcp from any to any established
```

```sh
ipfw add allow tcp from my-net to any setup keep-state
```

这将使防火墙仅对那些从我们网络内部以常规 SYN 数据包开始的连接安装动态规则。在遇到 `check-state`、`keep-state` 或 `limit` 规则的第一次出现时检查动态规则。`check-state` 规则通常应放置在规则集的开头附近，以最小化扫描规则集的工作量。实际效果可能因情况而异。

对于具有动态规则的更复杂场景，可以使用 `record-state` 和 `defer-action` 精确控制动态规则的创建和检查。这些选项的使用示例在 Sx 网络地址转换 (NAT) 部分中提供。

要限制用户可以打开的连接数，可以使用以下类型的规则：

```sh
ipfw add allow tcp from my-net/24 to any setup limit src-addr 10
```

```sh
ipfw add allow tcp from any to me setup limit src-addr 4
```

前者（假设它在网关上运行）将允许 /24 网络上的每台主机最多打开 10 个 TCP 连接。后者可以放置在服务器上，以确保单个客户端不会使用超过 4 个同时连接。

*注意：*有状态规则可能会受到 SYN 洪水拒绝服务攻击，这种攻击会打开大量动态规则。这种攻击的影响可以通过操作一组控制防火墙操作的 [sysctl(8)](sysctl.8.md) 变量来部分限制。

以下是 `list` 命令查看记帐记录和时间戳信息的好用法：

```sh
ipfw -at list
```

或简短形式（不带时间戳）：

```sh
ipfw -a list
```

等效于：

```sh
ipfw show
```

下一条规则将来自 **192.168.2.0/24** 的所有传入数据包转发到 divert 端口 5000：

```sh
ipfw divert 5000 ip from 192.168.2.0/24 to any in
```

### 流量整形

以下规则显示 `ipfw` 和 `dummynet` 在模拟等方面的某些应用。

此规则以 5% 的概率丢弃随机传入数据包：

```sh
ipfw add prob 0.05 deny ip from any to any in
```

可以利用 `dummynet` 管道实现类似效果：

```sh
dnctl add pipe 10 ip from any to any
```

```sh
dnctl pipe 10 config plr 0.05
```

我们可以使用管道人为限制带宽，例如，在作为路由器的机器上，如果我们想限制来自 **192.168.2.0/24** 上本地客户端的流量，我们这样做：

```sh
ipfw add pipe 1 ip from 192.168.2.0/24 to any out
```

```sh
dnctl pipe 1 config bw 300Kbit/s queue 50KBytes
```

请注意，我们使用 `out` 修饰符，以便规则不会被使用两次。事实上，请记住 `dummynet` 规则在传入和传出数据包上都会被检查。

如果我们想模拟具有带宽限制的双向链路，正确的方法如下：

```sh
ipfw add pipe 1 ip from any to any out
```

```sh
ipfw add pipe 2 ip from any to any in
```

```sh
dnctl pipe 1 config bw 64Kbit/s queue 10Kbytes
```

```sh
dnctl pipe 2 config bw 64Kbit/s queue 10Kbytes
```

上述方法可能非常有用，例如，如果你想查看你的精美网页对于仅通过慢速链路连接的住宅用户的外观。你不应该为两个方向只使用一个管道，除非你想模拟半双工介质（例如 AppleTalk、Ethernet、IRDA）。两个管道不必具有相同的配置，因此我们也可以模拟非对称链路。

如果我们想使用 RED 队列管理算法验证网络性能：

```sh
ipfw add pipe 1 ip from any to any
```

```sh
dnctl pipe 1 config bw 500Kbit/s queue 100 red 0.002/30/80/0.1
```

流量整形的另一个典型应用是在通信中引入一些延迟。这可能会显著影响执行大量远程过程调用的应用程序，其中连接的往返时间通常成为比带宽更具限制性的因素：

```sh
ipfw add pipe 1 ip from any to any out
```

```sh
ipfw add pipe 2 ip from any to any in
```

```sh
dnctl pipe 1 config delay 250ms bw 1Mbit/s
```

```sh
dnctl pipe 2 config delay 250ms bw 1Mbit/s
```

每流排队可用于各种目的。一个非常简单的目的是计算流量：

```sh
ipfw add pipe 1 tcp from any to any
```

```sh
ipfw add pipe 1 udp from any to any
```

```sh
ipfw add pipe 1 ip from any to any
```

```sh
dnctl pipe 1 config mask all
```

上述规则集将为所有流量创建队列（并收集统计信息）。由于管道没有限制，唯一的效果是收集统计信息。请注意，我们需要 3 条规则，而不仅仅是最后一条，因为当 `dummynet` 尝试匹配 IP 数据包时，它不会考虑端口，因此我们不会将不同端口上的连接视为不同的连接。

更复杂的示例是使用每主机限制而不是每网络限制来限制网络上的传出流量：

```sh
ipfw add pipe 1 ip from 192.168.2.0/24 to any out
```

```sh
ipfw add pipe 2 ip from any to 192.168.2.0/24 in
```

```sh
dnctl pipe 1 config mask src-ip 0x000000ff bw 200Kbit/s queue 20Kbytes
```

```sh
dnctl pipe 2 config mask dst-ip 0x000000ff bw 200Kbit/s queue 20Kbytes
```

### 查找表

在以下示例中，我们需要创建多个流量带宽类，并且需要不同的主机/网络落入不同的类。我们为每个类创建一个管道并相应地配置它们。然后我们创建一个表并用 IP 子网和地址填充它。对于每个子网/主机，我们将参数设置为它应使用的管道编号。然后我们使用单条规则对流量进行分类：

```sh
dnctl pipe 1 config bw 1000Kbyte/s
```

```sh
dnctl pipe 4 config bw 4000Kbyte/s
```

```sh
...
```

```sh
ipfw table T1 create type addr
```

```sh
ipfw table T1 add 192.168.2.0/24 1
```

```sh
ipfw table T1 add 192.168.0.0/27 4
```

```sh
ipfw table T1 add 192.168.0.2 1
```

```sh
...
```

```sh
ipfw add pipe tablearg ip from 'table(T1)' to any
```

使用 `fwd` 动作，表条目可以包含主机名和 IP 地址。

```sh
ipfw table T2 create type addr valtype ipv4
```

```sh
ipfw table T2 add 192.168.2.0/24 10.23.2.1
```

```sh
ipfw table T2 add 192.168.0.0/27 router1.dmz
```

```sh
...
```

```sh
ipfw add 100 fwd tablearg ip from any to 'table(T2)'
```

在以下示例中，创建了每接口防火墙：

```sh
ipfw table IN create type iface valtype skipto,fib
```

```sh
ipfw table IN add vlan20 12000,12
```

```sh
ipfw table IN add vlan30 13000,13
```

```sh
ipfw table OUT create type iface valtype skipto
```

```sh
ipfw table OUT add vlan20 22000
```

```sh
ipfw table OUT add vlan30 23000
```

```sh
..
```

```sh
ipfw add 100 setfib tablearg ip from any to any recv 'table(IN)' in
```

```sh
ipfw add 200 skipto tablearg ip from any to any recv 'table(IN)' in
```

```sh
ipfw add 300 skipto tablearg ip from any to any xmit 'table(OUT)' out
```

以下示例说明流表的使用：

```sh
ipfw table fl create type flow:src-ip,proto,dst-ip,dst-port
```

```sh
ipfw table fl add 2001:db8:77::88,tcp,2001:db8:77::99,80 11
```

```sh
ipfw table fl add 10.0.0.1,udp,10.0.0.2,53 12
```

```sh
..
```

```sh
ipfw add 100 allow ip from any to any flow 'table(fl,11)' recv ix0
```

以下示例说明掩码表查找，以帮助在多个 NAT 实例之间均匀分布客户端：

```sh
# 配置 NAT 实例
ipfw nat 10 config ip 192.0.2.0
ipfw nat 11 config ip 192.0.2.1
ipfw nat 12 config ip 192.0.2.2
ipfw nat 13 config ip 192.0.2.3
ipfw table mynats create type addr valtype nat
# 将外部 NAT 地址映射到 NAT 实例
ipfw table mynats add 192.0.2.0 10
ipfw table mynats add 192.0.2.1 11
ipfw table mynats add 192.0.2.2 12
ipfw table mynats add 192.0.2.3 13
# 将客户端 IP 地址的最后 2 位映射到 NAT 实例
ipfw table mynats add 0.0.0.0 10
ipfw table mynats add 0.0.0.1 11
ipfw table mynats add 0.0.0.2 12
ipfw table mynats add 0.0.0.3 13
# 入站 -> 出站 NAT，将客户端 IP 中的所有位清零，
# 仅保留最低的 2 位后再进行表查找
ipfw add nat tablearg ip from 10.0.0.0/24 to any
			lookup src-ip4:0.0.0.3 mynats
# 出站 -> 入站 NAT
ipfw add nat tablearg ip from any to 192.0.2.0/30
			lookup dst-ip mynats
```

### 规则集

要以原子方式添加一组规则（例如集合 18）：

```sh
ipfw set disable 18
```

```sh
ipfw add NN set 18 ... # 按需重复
```

```sh
ipfw set enable 18
```

要以原子方式删除一组规则，命令很简单：

```sh
ipfw delete set 18
```

要测试规则集并在出现问题时禁用它并重新获得控制权：

```sh
ipfw set disable 18
```

```sh
ipfw add NN set 18 ... # 按需重复
```

```sh
ipfw set enable 18; echo done; sleep 30 && ipfw set disable 18
```

在这里，如果一切顺利，你将在 sleep 终止之前按 control-C，你的规则集将保持活动状态。否则，例如如果你无法访问你的机器，规则集将在 sleep 终止后被禁用，从而恢复之前的情况。

要显示特定集合的规则：

```sh
ipfw set 18 show
```

要显示已禁用集合的规则：

```sh
ipfw -S set 18 show
```

要清除特定集合的特定规则计数器：

```sh
ipfw set 18 zero NN
```

要删除特定集合的特定规则：

```sh
ipfw set 18 delete NN
```

### NAT、重定向和 LSNAT

首先将所有流量重定向到 nat 实例 123：

```sh
ipfw add nat 123 all from any to any
```

然后配置 nat 实例 123，将所有传出流量别名为 ip **192.168.0.123**，阻止所有传入连接，尝试在两侧保持相同端口，在地址更改时清除别名表，并保留流量/链接统计信息的日志：

```sh
ipfw nat 123 config ip 192.168.0.123 log deny_in reset same_ports
```

或者要更改实例 123 的地址，别名表将被清除（参见 reset 选项）：

```sh
ipfw nat 123 config ip 10.0.0.1
```

要查看 nat 实例 123 的配置：

```sh
ipfw nat 123 show config
```

要显示所有实例的日志：

```sh
ipfw nat show log
```

要查看所有实例的配置：

```sh
ipfw nat show config
```

或者具有混合模式的重定向规则可能如下所示：

```sh
ipfw nat 123 config redirect_addr 10.0.0.1 10.0.0.66
			 redirect_port tcp 192.168.0.1:80 500
			 redirect_proto udp 192.168.1.43 192.168.1.1
			 redirect_addr 192.168.0.10,192.168.0.11
			 	    10.0.0.100	# LSNAT
			 redirect_port tcp 192.168.0.1:80,192.168.0.10:22
			 	    500		# LSNAT
```

或者它可以拆分为：

```sh
ipfw nat 1 config redirect_addr 10.0.0.1 10.0.0.66
ipfw nat 2 config redirect_port tcp 192.168.0.1:80 500
ipfw nat 3 config redirect_proto udp 192.168.1.43 192.168.1.1
ipfw nat 4 config redirect_addr 192.168.0.10,192.168.0.11,192.168.0.12
				         10.0.0.100
ipfw nat 5 config redirect_port tcp
			192.168.0.1:80,192.168.0.10:22,192.168.0.20:25 500
```

有时你可能想要混合使用 NAT 和动态规则。这可以通过 `record-state` 和 `defer-action` 选项实现。问题是，你需要在 NAT 之前创建动态规则并在 NAT 操作之后检查它（或反之），以获得一致的地址和端口。带有 `keep-state` 选项的规则将触发现有动态状态的激活，并且此类规则的动作将在规则匹配时立即执行。在 NAT 和 `allow` 规则的情况下，数据包需要传递给 NAT，而不是尽快允许。

有一组规则可以实现此目的的示例。请记住，这仅是示例，本身并不是很有用。

在出站时，所有检查之后放置这些规则：

```sh
ipfw add allow record-state defer-action
```

```sh
ipfw add nat 1
```

在入站时应该有类似这样的内容：

```sh
ipfw add nat 1
```

```sh
ipfw add check-state
```

请注意，出站时的第一条规则不允许数据包，也不执行现有动态规则。它所做的一切就是创建具有 `allow` 动作的新动态规则（如果尚未创建）。稍后，此动态规则在入站时由 `check-state` 规则使用。

### 配置 CODEL、PIE、FQ-CODEL 和 FQ-PIE AQM

`codel` 和 `pie` AQM 可以为 `dummynet` `pipe` 或 `queue` 配置。

要为来自 **192.168.0.0/24** 的流量使用默认配置的 `codel` AQM 配置 `pipe`，速率限制为 1Mbits/s，我们这样做：

```sh
dnctl pipe 1 config bw 1mbits/s codel
```

```sh
ipfw add 100 pipe 1 ip from 192.168.0.0/24 to any
```

要为来自 **192.168.0.0/24** 的流量使用不同配置参数的 `codel` AQM 配置 `queue`，速率限制为 1Mbits/s，我们这样做：

```sh
dnctl pipe 1 config bw 1mbits/s
```

```sh
dnctl queue 1 config pipe 1 codel target 8ms interval 160ms ecn
```

```sh
ipfw add 100 queue 1 ip from 192.168.0.0/24 to any
```

要为来自 **192.168.0.0/24** 的流量使用默认配置的 `pie` AQM 配置 `pipe`，速率限制为 1Mbits/s，我们这样做：

```sh
dnctl pipe 1 config bw 1mbits/s pie
```

```sh
ipfw add 100 pipe 1 ip from 192.168.0.0/24 to any
```

要为来自 **192.168.0.0/24** 的流量使用不同配置参数的 `pie` AQM 配置 `queue`，速率限制为 1Mbits/s，我们这样做：

```sh
dnctl pipe 1 config bw 1mbits/s
```

```sh
dnctl queue 1 config pipe 1 pie target 20ms tupdate 30ms ecn
```

```sh
ipfw add 100 queue 1 ip from 192.168.0.0/24 to any
```

`fq_codel` 和 `fq_pie` AQM 可以为 `dummynet` 调度器配置。

要为来自 **192.168.0.0/24** 的流量使用不同配置参数的 `fq_codel` 调度器，速率限制为 1Mbits/s，我们这样做：

```sh
dnctl pipe 1 config bw 1mbits/s
```

```sh
dnctl sched 1 config pipe 1 type fq_codel
```

```sh
dnctl queue 1 config sched 1
```

```sh
ipfw add 100 queue 1 ip from 192.168.0.0/24 to any
```

要更改 `sched` 的 `fq_codel` 默认配置（例如禁用 ECN 并将 `target` 更改为 10ms），我们这样做：

```sh
dnctl sched 1 config pipe 1 type fq_codel target 10ms noecn
```

类似于 `fq_codel`，要为来自 **192.168.0.0/24** 的流量使用不同配置参数的 `fq_pie` 调度器，速率限制为 1Mbits/s，我们这样做：

```sh
dnctl pipe 1 config bw 1mbits/s
```

```sh
dnctl sched 1 config pipe 1 type fq_pie
```

```sh
dnctl queue 1 config sched 1
```

```sh
ipfw add 100 queue 1 ip from 192.168.0.0/24 to any
```

`fq_pie` `sched` 的配置可以以与 `fq_codel` 类似的方式更改

## 参见

[cpp(1)](../man1/cpp.1.md), m4(1), fnmatch(3), [altq(4)](../man4/altq.4.md), [divert(4)](../man4/divert.4.md), [dummynet(4)](../man4/dummynet.4.md), if_bridge(4), [ip(4)](../man4/ip.4.md), [ipfirewall(4)](../man4/ipfirewall.4.md), [ng_ether(4)](../man4/ng_ether.4.md), [ng_ipfw(4)](../man4/ng_ipfw.4.md), [protocols(5)](../man5/protocols.5.md), [services(5)](../man5/services.5.md), [init(8)](init.8.md), [kldload(8)](kldload.8.md), [reboot(8)](reboot.8.md), [sysctl(8)](sysctl.8.md), syslogd(8), [sysrc(8)](sysrc.8.md)

## 历史

`dummynet` 工具首次出现在 FreeBSD 2.0 中。`dummynet` 在 FreeBSD 2.2.8 中引入。有状态扩展在 FreeBSD 4.0 中引入。`ipfw2` 在 2002 年夏天引入。

## 作者

Ugen J. S. Antsilevich, Poul-Henning Kamp, Alex Nash, Archie Cobbs, Luigi Rizzo, Rasool Al-Saadi。

API 基于 Daniel Boulet 为 BSDI 编写的代码。

Dummynet 由 Luigi Rizzo 在 1997-1998 年引入。

`dummynet` 流量整形器的一些早期工作（1999-2000）由 Akamba Corp. 支持。

ipfw 核心 (ipfw2) 由 Luigi Rizzo 在 2002 年夏天完全重新设计和重新实现。多年来，各种开发者添加了进一步的动作和选项。

内核内 NAT 支持由 Paolo Pisati <piso@FreeBSD.org> 作为 2005 年 Summer of Code 项目的一部分编写。

SCTP `nat` 支持由先进互联网架构中心 (CAIA) <http://www.caia.swin.edu.au> 开发。主要开发者和维护者是 David Hayes 和 Jason But。有关更多信息，请访问：<http://www.caia.swin.edu.au/urp/SONATA>

延迟配置文件由 Alessandro Cerri 和 Luigi Rizzo 开发，由欧洲委员会在 Onelab 和 Onelab2 项目中支持。

CoDel、PIE、FQ-CoDel 和 FQ-PIE AQM for Dummynet 由先进互联网架构中心 (CAIA) 在 2016 年实现，由 Comcast 创新基金支持。主要开发者是 Rasool Al-Saadi。

## 缺陷

语法多年来一直在增长，有时可能令人困惑。不幸的是，向后兼容性阻止了清理语法定义中犯的错误。

*！！！警告！！！*

错误配置防火墙可能使你的计算机处于不可用状态，可能关闭网络服务并需要控制台访问才能重新获得控制权。

由 `divert` 转发的传入数据包片段在传递到套接字之前会被重新组装。用于这些数据包的动作来自匹配数据包第一个片段的规则。

转移到用户空间，然后由用户空间进程重新插入的数据包可能会丢失各种数据包属性。如果数据包源接口名称短于 8 字节并且用户空间进程保存并重用 sockaddr_in（如 [natd(8)](natd.8.md) 所做的那样），则它将被保留；否则，它可能会丢失。如果以这种方式重新插入数据包，则后续规则可能被错误应用，使得 `divert` 规则在规则序列中的顺序非常重要。

Dummynet 丢弃所有具有 IPv6 链路本地地址的数据包。

使用 `uid` 或 `gid` 的规则可能不会按预期工作。特别是，传入 SYN 数据包可能没有与之关联的 uid 或 gid，因为它们尚不属于 TCP 连接，并且如果关联进程调用 setuid(2) 或类似系统调用，则与数据包关联的 uid/gid 可能与预期不同。

规则语法受命令行环境影响，某些模式可能需要用反斜杠字符转义或适当引用。

由于 libalias(3) 的架构，ipfw nat 与 TCP 分段卸载 (TSO) 不兼容。因此，要可靠地对网络流量进行 nat，请使用 [ifconfig(8)](ifconfig.8.md) 在你的网卡上禁用 TSO。

ICMP 错误消息不会由相应会话的动态规则隐式匹配。为了避免网络错误检测和路径 MTU 发现失败，可能需要通过静态规则显式允许 ICMP 错误消息。

使用 `call` 和 `return` 动作的规则如果规则集有错误和/或与其他子系统（netgraph、dummynet 等）交互使用，可能会导致令人困惑的行为。一种可能的情况是数据包在输入传递时在子例程中离开 `nat`，而稍后在输出时首先遇到未配对的 `return`。由于调用堆栈在输入传递后保持完整，数据包将突然返回到输入传递时使用的规则号，而不是输出传递时使用的规则号。应仔细检查处理顺序以避免此类错误。
