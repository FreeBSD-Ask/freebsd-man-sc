# tcpdump.1

`tcpdump` — 转储网络上的流量

## 名称

`tcpdump` — 转储网络上的流量

## 概要

`tcpdump [-AbdDefghHIJKlLnNOpqStuUvxX#] [-B buffer_size] [-c count] [--count] [-C file_size] [-E spi@ipaddr algo:secret,...] [-F file] [-G rotate_seconds] [-i interface] [--immediate-mode] [-j tstamp_type] [-m module] [-M secret] [--number] [--print] [-Q in|out|inout] [-r file] [-s snaplen] [-T type] [--version] [-V file] [-w file] [-W filecount] [-y datalinktype] [-z postrotate-command] [-Z user] [--time-stamp-precision=tstamp_precision] [--micro] [--nano] [expression]`

## 描述

`tcpdump` 会打印出网络接口上与布尔 `expression` 匹配的数据包内容的描述（表达式语法参见 **pcap-filter (@MAN_MISC_INFO@)**）；描述前会有时间戳，默认以自午夜起的小时、分钟、秒和秒的小数部分形式打印。它也可以使用 `-w` 标志运行，这会将数据包数据保存到文件以供日后分析；和/或使用 `-r` 标志运行，这会从已保存的数据包文件读取，而不是从网络接口读取数据包。它也可以使用 `-V` 标志运行，这会读取已保存数据包文件的列表。在所有情况下，只有与 `expression` 匹配的数据包才会被 `tcpdump` 处理。

如果不使用 `-c` 标志运行，`tcpdump` 会持续捕获数据包，直到被 SIGINT 信号（例如，通过键入你的中断字符，通常是 control-C）或 SIGTERM 信号（通常通过 kill(1) 命令生成）中断；如果使用 `-c` 标志运行，它会捕获数据包直到被 SIGINT 或 SIGTERM 信号中断，或已处理指定数量的数据包。

`tcpdump` 完成捕获数据包后，会报告以下计数：IP 数据包 “已捕获”（这是 `tcpdump` 已接收并处理的数据包数量）；IP 数据包 “由过滤器接收”（其含义取决于运行 `tcpdump` 的操作系统，可能还取决于操作系统的配置方式——如果在命令行上指定了过滤器，某些操作系统会统计所有数据包，无论是否与过滤器表达式匹配，即使匹配也无论 `tcpdump` 是否已读取和处理它们；其他操作系统仅统计与过滤器表达式匹配的数据包，无论 `tcpdump` 是否已读取和处理它们；还有其他操作系统仅统计与过滤器表达式匹配且已被 `tcpdump` 处理的数据包）；IP 数据包 “被内核丢弃”（这是由于缓冲区空间不足，运行 `tcpdump` 的操作系统中的数据包捕获机制丢弃的数据包数量，如果操作系统向应用程序报告此信息；如果不报告，则报告为 0）。

在支持 SIGINFO 信号的平台（如大多数 BSD（包括 macOS）和 Digital/Tru64 UNIX）上，当收到 SIGINFO 信号（例如，通过键入你的 “status” 字符，通常是 control-T，虽然在某些平台如 macOS 上默认未设置 “status” 字符，因此必须使用 stty(1) 设置才能使用）时会报告这些计数，并继续捕获数据包。在不支持 SIGINFO 信号的平台，可以使用 SIGUSR1 信号达到相同效果。

使用 SIGUSR2 信号配合 `-w` 标志会强制将数据包缓冲区刷新到输出文件。

从网络接口读取数据包可能需要特殊权限；详情参见 pcap(3PCAP) 手册页。读取已保存的数据包文件不需要特殊权限。

## 选项

**`-A`** 以 ASCII 打印每个数据包（不含链路层头）。便于捕获网页。使用 `-x[x]` 或 `-X[X]` 选项时无效。

**`-b`** 在 BGP 数据包中以 ASDOT 表示法而非 ASPLAIN 表示法打印 AS 号。

**`-B`** `buffer_size`、**`--buffer-size=`**`buffer_size` 将操作系统捕获缓冲区大小设置为 `buffer_size`，单位为 KiB（1024 字节）。

**`-c`** `count` 接收 `count` 个数据包后退出。

**`--count`** 读取捕获文件时，仅在 stdout 打印数据包计数，而不解析/打印数据包。如果在命令行上指定了过滤器，`tcpdump` 仅统计与过滤器表达式匹配的数据包。

**`-C`** `file_size` 在将原始数据包写入保存文件之前，检查文件当前是否大于 `file_size`，如果是，则关闭当前保存文件并打开新文件。第一个保存文件之后的保存文件将具有用 `-w` 标志指定的名称，后面带有一个数字，从 1 开始递增。`file_size` 的默认单位是百万字节（1,000,000 字节，而非 1,048,576 字节）。通过在值后添加 k/K、m/M 或 g/G 后缀，可分别将单位更改为 1,024（KiB）、1,048,576（MiB）或 1,073,741,824（GiB）。

**`-d`** 将编译后的数据包匹配代码以人类可读的形式转储到标准输出并停止。请注意，虽然代码编译始终是特定于 DLT 的，但通常无法（也不必）指定转储使用哪个 DLT，因为 `tcpdump` 使用由 `-r` 指定的输入 pcap 文件的 DLT，或由 `-i` 指定的网络接口的默认 DLT，或由 `-y` 和 `-i` 指定的网络接口的特定 DLT。在这些情况下，转储显示的是与不带 `-d` 时过滤输入文件或网络接口完全相同的代码。但是，当既未指定 `-r` 也未指定 `-i` 时，指定 `-d` 会阻止 `tcpdump` 猜测合适的网络接口（参见 `-i`）。在这种情况下，DLT 默认为 EN10MB，可使用 `-y` 手动设置为其他有效值。

**`-dd`** 将数据包匹配代码作为 `C` 程序片段转储。

**`-ddd`** 将数据包匹配代码作为十进制数转储（前面带有计数）。

**`-D`**、**`--list-interfaces`** 打印系统上 `tcpdump` 可以捕获数据包的可用网络接口列表。对于每个网络接口，会打印一个编号和接口名，可能后跟接口的文本描述。接口名或编号可提供给 `-i` 标志以指定捕获的接口。这在没有命令列出接口的系统（如 Windows 系统，或缺少 `ifconfig -a` 的 UNIX 系统）上很有用；编号在 Windows 2000 及更高版本系统上很有用，因为接口名是一个相当复杂的字符串。如果 `tcpdump` 是使用缺少 pcap_findalldevs(3PCAP) 函数的旧版 `libpcap` 构建的，则不支持 `-D` 标志。

**`-e`** 在每个转储行上打印链路层头。例如，可用于打印 Ethernet 和 IEEE 802.11 等协议的 MAC 层地址。

**`-E`** 使用 `spi@ipaddr algo:secret` 解密地址为 `addr` 且包含安全参数索引值 `spi` 的 IPsec ESP 数据包。此组合可用逗号或换行符分隔重复。注意，目前支持为 IPv4 ESP 数据包设置密钥。算法可以是 `des-cbc`、`3des-cbc`、`blowfish-cbc`、`rc3-cbc`、`cast128-cbc` 或 `none`。默认为 `des-cbc`。解密数据包的能力仅在 `tcpdump` 编译时启用加密时才存在。`secret` 是 ESP 密钥的 ASCII 文本。如果前缀为 0x，则读取十六进制值。此选项假定 RFC 2406 ESP，而非 RFC 1827 ESP。此选项仅供调试，不鼓励将真实 “secret” 密钥与此选项一起使用。通过将 IPsec 密钥放在命令行上，你会使其通过 ps(1) 等途径对他人可见。除上述语法外，可使用语法 `file name` 让 `tcpdump` 读入提供的文件。文件在收到第一个 ESP 数据包时打开，因此 `tcpdump` 可能已被授予的任何特殊权限此时应该已经放弃。

**`-f`** 以数字形式而非符号形式打印 “外部” IPv4 地址（此选项旨在绕过 Sun NIS 服务器的严重缺陷——通常在转换非本地 internet 号时会永远挂起）。对 “外部” IPv4 地址的测试使用进行捕获的接口的 IPv4 地址和网络掩码。如果该地址或网络掩码不可用（因为进行捕获的接口没有地址或网络掩码，或因为它是 “any” 伪接口（参见下面的 `-i` 标志）），此选项将无法正常工作。

**`-F`** `file` 使用 `file` 作为过滤器表达式的输入。命令行上给出的附加表达式将被忽略。

**`-g`**、**`--ip-oneline`** 在详细模式下，不在 IP 头后插入换行符。

**`-G`** `rotate_seconds` 如果指定，则每 `rotate_seconds` 秒轮转由 `-w` 选项指定的转储文件。保存文件将具有由 `-w` 指定的名称，其中应包含由 strftime(3) 定义的时间格式。如果未指定时间格式，每个新文件将覆盖前一个。每当生成的文件名不唯一时，`tcpdump` 会覆盖现有数据；因此不建议提供比捕获周期更粗的时间规范。如果与 `-C` 选项一起使用，文件名形式为 “`file`<count>”。

**`-h`**、**`--help`** 打印 tcpdump 和 libpcap 版本字符串，打印用法消息并退出。

**`--version`** 打印 tcpdump 和 libpcap 版本字符串并退出。

**`-H`** 尝试检测 802.11s 草案 mesh 头。

**`-i`** `interface`、**`--interface=`**`interface` 在 `interface` 上监听、报告链路层类型列表、报告时间戳类型列表，或报告在 `interface` 上编译过滤器表达式的结果。如果未指定且未给出 `-d` 标志，`tcpdump` 会搜索系统接口列表中编号最低、已配置为 up 的接口（不包括环回），例如可能是 “eth0”。在所有受支持的 Linux 系统以及近期版本的 macOS 和 Solaris 上，`interface` 参数为 “any” 表示一个特殊的伪接口，它捕获操作系统所有常规网络接口的数据包。什么被视为常规网络接口是操作系统的实现细节（例如，在 Linux 上这包括 SocketCAN 设备），因此在 “any” 伪接口上捕获的数据包可能代表比预期更多不同的网络协议。此外，所有常规网络接口都是 `-D` 标志打印的所有可用捕获设备的子集。后者还可能包括 `libpcap` 通过操作系统网络栈以外的方式实现的捕获设备：Bluetooth、DAG、D-Bus、SNF 和 USB。注意，在 “any” 伪接口上的捕获不会以混杂模式进行。如果支持 `-D` 标志，则该标志打印的接口编号可用作 `interface` 参数，前提是系统上没有接口以该编号作为名称。

**`-I`**、**`--monitor-mode`** 将接口置于 “监控模式”；这仅在 IEEE 802.11 Wi-Fi 接口上受支持，且仅在部分操作系统上受支持。注意，在监控模式下，适配器可能会从其关联的网络断开，因此你将无法使用该适配器的任何无线网络。这可能会阻止访问网络服务器上的文件，或解析主机名或网络地址（如果你在监控模式下捕获且未通过另一个适配器连接到其他网络）。此标志会影响 `-L` 标志的输出。如果未指定 `-I`，仅显示非监控模式下可用的链路层类型；如果指定了 `-I`，仅显示监控模式下可用的链路层类型。

**`--immediate-mode`** 以 “立即模式” 捕获。在此模式下，数据包一到达就交付给 `tcpdump`，而不是为提高效率而缓冲。当打印数据包而非保存到 “保存文件” 时（如果数据包正在打印到终端而非文件或管道），这是默认行为。

**`-j`** `tstamp_type`、**`--time-stamp-type=`**`tstamp_type` 将捕获的时间戳类型设置为 `tstamp_type`。时间戳类型使用的名称在 pcap-tstamp(@MAN_MISC_INFO@) 中给出；那里列出的类型不一定对任何给定接口都有效。

**`-J`**、**`--list-time-stamp-types`** 列出接口支持的时间戳类型并退出。如果无法为接口设置时间戳类型，则不会列出任何时间戳类型。

**`--time-stamp-precision=`**`tstamp_precision` 捕获时，将捕获的时间戳精度设置为 `tstamp_precision`。注意，高精度时间戳（纳秒）的可用性及其实际精度取决于平台和硬件。还应注意，将以纳秒精度写入的捕获保存到文件时，时间戳以纳秒分辨率写入，文件使用不同的魔数写入，以指示时间戳为秒和纳秒；并非所有读取 pcap 保存文件的程序都能读取这些捕获。读取保存文件时，将时间戳转换为 `timestamp_precision` 指定的精度，并以该分辨率显示。如果指定的精度小于文件中时间戳的精度，转换会损失精度。`timestamp_precision` 支持的值为 `micro`（微秒分辨率）和 `nano`（纳秒分辨率）。默认为微秒分辨率。

**`--micro`**、**`--nano`** --time-stamp-precision=micro 或 --time-stamp-precision=nano 的简写，相应调整时间戳精度。从保存文件读取数据包时，如果保存文件以纳秒精度创建，使用 `--micro` 会截断时间戳。相反，以微秒精度创建的保存文件在使用 `--nano` 时会在时间戳上添加尾随零。

**`-K`**、**`--dont-verify-checksums`** 不尝试验证 IP、TCP 或 UDP 校验和。这对于在硬件中执行部分或全部校验和计算的接口很有用；否则，所有传出 TCP 校验和都会被标记为错误。

**`-l`** 使 stdout 行缓冲。如果想在捕获数据时同时查看数据，这很有用。例如：

```sh
tcpdump -l | tee dat
```

或

```sh
tcpdump -l > dat & tail -f dat
```

注意，在 Windows 上，“行缓冲” 意味着 “无缓冲”，因此如果指定了 `-l`，WinDump 会单独写入每个字符。`-U` 在行为上类似于 `-l`，但它会使输出 “按数据包缓冲”，因此输出在每个数据包结束时写入 stdout 而非每行结束时；这在所有平台（包括 Windows）上都是缓冲的。

**`-L`**、**`--list-data-link-types`** 列出接口在指定模式下已知的链路类型并退出。已知数据链路类型的列表可能取决于指定的模式；例如，在某些平台上，Wi-Fi 接口在非监控模式下可能支持一组数据链路类型（例如，可能仅支持伪 Ethernet 头，或支持 802.11 头但不支持带无线信息的 802.11 头），而在监控模式下支持另一组数据链路类型（例如，可能仅在监控模式下支持 802.11 头或带无线信息的 802.11 头）。

**`-m`** `module` 从文件 `module` 加载 SMI MIB 模块定义。此选项可多次使用以将多个 MIB 模块加载到 `tcpdump`。

**`-M`** `secret` 使用 `secret` 作为共享密钥，用于验证 TCP 段中带有 TCP-MD5 选项（RFC 2385）的摘要（如果存在）。

**`-n`** 不将地址（即主机地址、端口号等）转换为名称。

**`-N`** 不打印主机名的域名限定。例如，如果给出此标志，则 `tcpdump` 会打印 “nic” 而非 “nic.ddn.mil”。

**`-#`**、**`--number`** 在行首打印数据包编号。

**`-O`**、**`--no-optimize`** 不运行数据包匹配代码优化器。仅当你怀疑优化器有 bug 时才有用。

**`-p`**、**`--no-promiscuous-mode`** 不将接口置为混杂模式。注意，接口可能因其他原因处于混杂模式；因此，`-p` 不能用作 “`ether host {local-hw-addr} or ether broadcast`” 的缩写。

**`--print`** 即使原始数据包正在用 `-w` 标志保存到文件，也打印解析后的数据包输出。

**`-Q`** `direction`、**`--direction=`**`direction` 选择应捕获数据包的发送/接收方向 `direction`。可能值为 `in`、`out` 和 `inout`。并非所有平台都可用。

**`-q`** 快速（安静？）输出。打印更少的协议信息，使输出行更短。

**`-r`** `file` 从 `file` 读取数据包（由 `-w` 选项创建或由其他写入 pcap 或 pcapng 文件的工具创建）。如果 `file` 是 “-”，则使用标准输入。

**`-S`**、**`--absolute-tcp-sequence-numbers`** 打印绝对而非相对 TCP 序列号。

**`-s`** `snaplen`、**`--snapshot-length=`**`snaplen` 从每个数据包中抓取 `snaplen` 字节的数据，而非默认的 262144 字节。由于快照有限而被截断的数据包在输出中以 “[|proto]” 标示，其中 `proto` 是发生截断的协议层名称。注意，采用较大的快照既会增加处理数据包所需的时间，又实际上会减少数据包缓冲量。这可能导致数据包丢失。还应注意，采用较小的快照会丢弃传输层以上协议的数据，这会丢失可能重要的信息。例如，NFS 和 AFS 请求与响应非常大，如果选择过短的快照长度，许多细节将不可用。如果需要将快照大小减小到默认值以下，应将 `snaplen` 限制为能捕获你感兴趣的协议信息的最小数字。将 `snaplen` 设为 0 会将其设为默认值 262144，以与近期旧版本的 `tcpdump` 向后兼容。

**`-T`** `type` 强制将 “expression” 选中的数据包解释为指定类型。当前已知的类型有：aodv（Ad-hoc On-demand Distance Vector protocol）、carp（Common Address Redundancy Protocol）、cnfp（Cisco NetFlow protocol）、domain（Domain Name System）、lmp（Link Management Protocol）、pgm（Pragmatic General Multicast）、pgm_zmtp1（ZMTP/1.0 inside PGM/EPGM）、ptp（Precision Time Protocol）、radius（RADIUS）、resp（REdis Serialization Protocol）、rpc（Remote Procedure Call）、rtcp（Real-Time Applications control protocol）、rtp（Real-Time Applications protocol）、snmp（Simple Network Management Protocol）、someip（SOME/IP）、tftp（Trivial File Transfer Protocol）、vat（Visual Audio Tool）、vxlan（Virtual eXtensible Local Area Network）、wb（distributed White Board）和 zmtp1（ZeroMQ Message Transport Protocol 1.0）。注意，上面的 pgm 类型仅影响 UDP 解释，原生 PGM 始终被识别为 IP 协议 113。UDP 封装的 PGM 通常称为 “EPGM” 或 “PGM/UDP”。注意，上面的 pgm_zmtp1 类型同时影响原生 PGM 和 UDP 的解释。在原生 PGM 解码期间，ODATA/RDATA 数据包的应用数据会被解码为带 ZMTP/1.0 帧的 ZeroMQ 数据报。在 UDP 解码期间，除此之外，任何 UDP 数据包都会被视为封装的 PGM 数据包。

**`-t`** 不在每个转储行上打印时间戳。

**`-tt`** 在每个转储行上打印时间戳，为自 1970 年 1 月 1 日 00:00:00 UTC 以来的秒数和自该时间以来的秒的小数部分。

**`-ttt`** 在每个转储行上打印当前行与前一行之间的差值（根据 `--time-stamp-precision` 选项为微秒或纳秒分辨率）。默认为微秒分辨率。

**`-tttt`** 在每个转储行上打印时间戳，为自午夜起的小时、分钟、秒和秒的小数部分，前面带有日期。

**`-ttttt`** 在每个转储行上打印当前行与第一行之间的差值（根据 `--time-stamp-precision` 选项为微秒或纳秒分辨率）。默认为微秒分辨率。

**`-u`** 打印未解码的 NFS 句柄。

**`-U`**、**`--packet-buffered`** 如果未指定 `-w` 选项，或指定了但同时也指定了 `--print` 标志，则使打印的数据包输出 “按数据包缓冲”；即，随着每个数据包内容的描述被打印，它会写入标准输出，而非在不写入终端时仅在输出缓冲区填满时写入。如果指定了 `-w` 选项，则使保存的原始数据包输出 “按数据包缓冲”；即，随着每个数据包被保存，它会写入输出文件，而非仅在输出缓冲区填满时写入。如果 `tcpdump` 是使用缺少 pcap_dump_flush(3PCAP) 函数的旧版 `libpcap` 构建的，则不支持 `-U` 标志。

**`-v`** 解析和打印时，生成（稍微更多）详细输出。例如，会打印 IP 数据包中的生存时间、标识、总长度和选项。还会启用额外的数据包完整性检查，如验证 IP 和 ICMP 头校验和。使用 `-w` 选项写入文件且同时不使用 `-r` 选项从文件读取时，每秒向 stderr 报告一次捕获的数据包数量。在 Solaris、FreeBSD 和可能的其他操作系统上，此定期更新当前可能导致数据包在从内核到 `tcpdump` 的途中丢失。

**`-vv`** 更加详细的输出。例如，会从 NFS 回复数据包中打印额外字段，并完全解码 SMB 数据包。

**`-vvv`** 更加详细的输出。例如，telnet SB ... SE 选项会完整打印。使用 `-X` 时，Telnet 选项还会以十六进制打印。

**`-V`** `file` 从 `file` 读取文件名列表。如果 `file` 是 “-”，则使用标准输入。

**`-w`** `file` 将原始数据包写入 `file` 而非解析和打印它们。它们之后可以用 `-r` 选项打印。如果 `file` 是 “-”，则使用标准输出。如果写入文件或管道，此输出会被缓冲，因此从文件或管道读取的程序可能在数据包收到后任意时间内都看不到数据包。使用 `-U` 标志可使数据包一收到就写入。MIME 类型 application/vnd.tcpdump.pcap 已在 IANA 注册用于 pcap 文件。文件扩展名 .pcap 似乎是最常用的，还有 .cap 和 .dmp。`tcpdump` 本身在读取捕获文件时不检查扩展名，在写入时也不添加扩展名（它使用文件头中的魔数）。但是，许多操作系统和应用程序在扩展名存在时会使用它，建议添加一个（如 .pcap）。文件格式描述参见 pcap-savefile(@MAN_FILE_FORMATS@)。

**`-W`** `filecount` 与 `-C` 选项一起使用时，这会将创建的文件数限制为指定数量，并从开头开始覆盖文件，从而创建 “循环” 缓冲区。此外，它会以足够多的前导 0 命名文件以支持最大文件数，使它们能正确排序。与 `-G` 选项一起使用时，这会限制创建的轮转转储文件数，达到限制时以状态 0 退出。如果与 `-C` 和 `-G` 同时使用，`-W` 选项当前会被忽略，仅影响文件名。

**`-x`** 解析和打印时，除了打印每个数据包的头外，以十六进制打印每个数据包的数据（不含链路层头）。会打印整个数据包或 `snaplen` 字节中较小者。注意，这是整个链路层数据包，因此对于会填充的链路层（如 Ethernet），当较高层数据包短于所需填充时，填充字节也会被打印。在当前实现中，如果数据包被截断，此标志可能与 `-xx` 效果相同。使用 `-X[X]` 选项时无效。

**`-xx`** 解析和打印时，除了打印每个数据包的头外，以十六进制打印每个数据包的数据，*包括* 链路层头。使用 `-X[X]` 选项时无效。

**`-X`** 解析和打印时，除了打印每个数据包的头外，以十六进制和 ASCII 打印每个数据包的数据（不含链路层头）。这对于分析新协议非常方便。在当前实现中，如果数据包被截断，此标志可能与 `-XX` 效果相同。

**`-XX`** 解析和打印时，除了打印每个数据包的头外，以十六进制和 ASCII 打印每个数据包的数据，*包括* 链路层头。

**`-y`** `datalinktype`、**`--linktype=`**`datalinktype` 将捕获数据包时使用的数据链路类型（参见 `-L`）或仅编译和转储数据包匹配代码时使用的数据链路类型（参见 `-d`）设置为 `datalinktype`。

**`-z`** `postrotate-command` 与 `-C` 或 `-G` 选项一起使用时，这会使 `tcpdump` 运行 “`postrotate-command file`”，其中 `file` 是每次轮转后正在关闭的保存文件。例如，指定 `-z gzip` 或 `-z bzip2` 会使用 gzip 或 bzip2 压缩每个保存文件。此选项仅在实现了 fork 子进程时可用（如非 Windows 系统）。注意，`tcpdump` 会以最低优先级并行运行该命令，以免干扰捕获过程。如果你想使用本身带标志或不同参数的命令，你始终可以编写一个 shell 脚本，将保存文件名作为唯一参数，安排标志和参数并执行你想要的命令。

**`-Z`** `user`、**`--relinquish-privileges=`**`user` 如果 `tcpdump` 以 root 身份运行，在打开捕获设备或输入保存文件后，但在打开任何输出保存文件之前，将用户 ID 更改为 `user`，将组 ID 更改为 `user` 的主组。此行为也可以在编译时默认启用。

`expression` 选择将转储哪些数据包。如果未给出表达式，将转储网络上的所有数据包。否则，仅转储 `expression` 为 “真” 的数据包。

表达式语法参见 pcap-filter(@MAN_MISC_INFO@)。

`expression` 参数可以作为单个 Shell 参数或多个 Shell 参数传递给 `tcpdump`，以更方便者为准。通常，如果表达式包含 Shell 元字符（如用于转义协议名的反斜杠），将其作为单个带引号的参数传递比转义 Shell 元字符更容易。多个参数在解析前以空格连接。

## 实例

打印所有到达或离开 sundown 的数据包：

```sh
tcpdump host sundown
```

打印 helios 与 hot 或 ace 之间的流量：

```sh
tcpdump host helios and \( hot or ace \)
```

打印 ace 与除 helios 外任何主机之间的所有 IP 数据包：

```sh
tcpdump ip host ace and not helios
```

打印本地主机与 Berkeley 主机之间的所有流量：

```sh
tcpdump net ucb-ether
```

打印通过 Internet 网关 snup 的所有 ftp 流量（注意，表达式加引号以防止 shell（错误）解释括号）：

```sh
tcpdump 'gateway snup and (port ftp or ftp-data)'
```

打印既非来自也非发往本地主机的流量（如果你通过一个其他网络网关，这些内容不应出现在本地网络上）：

```sh
tcpdump ip and not net localnet
```

打印涉及非本地主机的每个 TCP 会话的开始和结束数据包（SYN 和 FIN 数据包）：

```sh
tcpdump 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0 and not src and dst net localnet'
```

打印同时设置 RST 和 ACK 标志的 TCP 数据包（即，在 flags 字段中仅选择 RST 和 ACK 标志，如果结果为 “RST 和 ACK 同时设置”，则匹配）：

```sh
tcpdump 'tcp[tcpflags] & (tcp-rst|tcp-ack) == (tcp-rst|tcp-ack)'
```

打印与端口 80 之间的所有 IPv4 HTTP 数据包，即仅打印包含数据的数据包，而非例如 SYN 和 FIN 数据包以及仅 ACK 数据包（IPv6 留给读者练习）：

```sh
tcpdump 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
```

打印通过网关 snup 发送的大于 576 字节的 IP 数据包：

```sh
tcpdump 'gateway snup and ip[2:2] > 576'
```

打印 *未* 通过 Ethernet 广播或多播发送的 IP 广播或多播数据包：

```sh
tcpdump 'ether[0] & 1 = 0 and ip[16] >= 224'
```

打印所有非回显请求/回复（即非 ping 数据包）的 ICMP 数据包：

```sh
tcpdump 'icmp[icmptype] != icmp-echo and icmp[icmptype] != icmp-echoreply'
```

## 输出格式

`tcpdump` 的输出取决于协议。以下给出大多数格式的简要描述和示例。

### 时间戳

默认情况下，所有输出行前都有时间戳。时间戳是当前时钟时间，形式为 `hh:mm:ss.frac`，精度与内核时钟一致。时间戳反映内核对数据包应用时间戳的时间。不会尝试考虑网络接口从网络接收完数据包到内核对数据包应用时间戳之间的时间差；该时间差可能包括网络接口从网络接收完数据包到向内核传递中断以让其读取数据包之间的延迟，以及内核服务 “新数据包” 中断到对数据包应用时间戳之间的延迟。

### 接口

当在捕获时选择 any 接口或读取链路类型为 LINUX_SLL2 的捕获文件时，接口名打印在时间戳之后。后面是数据包类型，In 和 Out 分别表示发往本主机或来自本主机的数据包。其他可能值为 B（广播数据包）、M（多播数据包）和 P（发往其他主机的数据包）。

### 链路层头

如果给出 `-e` 选项，会打印链路层头。在 Ethernet 上，会打印源地址和目标地址、协议以及数据包长度。

在 FDDI 网络上，`-e` 选项使 `tcpdump` 打印 “frame control” 字段、源地址和目标地址以及数据包长度。（“frame control” 字段控制数据包其余部分的解释。正常数据包（如包含 IP 数据报的）是 “async” 数据包，优先级值在 0 到 7 之间；例如 “async4”。假定此类数据包包含 802.2 Logical Link Control（LLC）数据包；如果不是 ISO 数据报或所谓的 SNAP 数据包，则打印 LLC 头。

在 Token Ring 网络上，`-e` 选项使 `tcpdump` 打印 “access control” 和 “frame control” 字段、源地址和目标地址以及数据包长度。与 FDDI 网络一样，假定数据包包含 LLC 数据包。无论是否指定 `-e` 选项，对于源路由数据包都会打印源路由信息。

在 802.11 网络上，`-e` 选项使 `tcpdump` 打印 “frame control” 字段、802.11 头中的所有地址以及数据包长度。与 FDDI 网络一样，假定数据包包含 LLC 数据包。

（注意：以下描述假定熟悉 RFC 1144 中描述的 SLIP 压缩算法。）

在 SLIP 链路上，会打印方向指示符（“I” 表示入站，“O” 表示出站）、数据包类型和压缩信息。首先打印数据包类型。三种类型为 ip、utcp 和 ctcp。对于 ip 数据包，不打印进一步的链路信息。对于 TCP 数据包，类型后跟连接标识符。如果数据包被压缩，则打印其编码的头。特殊情况打印为 `*S+n` 和 `*SA+n`，其中 `n` 是序列号（或序列号和 ack）的变化量。如果不是特殊情况，则打印零个或多个变化。变化由 U（紧急指针）、W（窗口）、A（ack）、S（序列号）和 I（数据包 ID）指示，后跟一个增量（+n 或 -n）或新值（=n）。最后，打印数据包中的数据量和压缩头长度。

例如，以下行显示一个出站压缩 TCP 数据包，带有隐式连接标识符；ack 变化了 6，序列号变化了 49，数据包 ID 变化了 6；有 3 字节数据和 6 字节压缩头：

```
O ctcp * A+6 S+49 I+6 3 (6)
```

### ARP/RARP 数据包

ARP/RARP 输出显示请求类型及其参数。该格式旨在自解释。以下是从主机 rtsg 到主机 csam 的 `rlogin` 开始时取的简短示例：

```
arp who-has csam tell rtsg
arp reply csam is-at CSAM
```

第一行表示 rtsg 发送了一个 ARP 数据包，询问 internet 主机 csam 的 Ethernet 地址。Csam 用其 Ethernet 地址回复（在此示例中，Ethernet 地址为大写，internet 地址为小写）。

如果我们执行 `tcpdump -n`，看起来会更少冗余：

```
arp who-has 128.3.254.6 tell 128.3.254.68
arp reply 128.3.254.6 is-at 02:07:01:00:01:c4
```

如果我们执行 `tcpdump -e`，第一个数据包是广播而第二个是点对点这一事实将可见：

```
RTSG Broadcast 0806 64: arp who-has csam tell rtsg
CSAM RTSG 0806 64: arp reply csam is-at CSAM
```

对于第一个数据包，这表示 Ethernet 源地址是 RTSG，目标是 Ethernet 广播地址，类型字段包含十六进制 0806（类型 ETHER_ARP），总长度为 64 字节。

### IPv4 数据包

如果未打印链路层头，对于 IPv4 数据包，IP 打印在时间戳之后。

如果指定 `-v` 标志，IPv4 头中的信息显示在 IP 或链路层头之后的括号中。此信息的一般格式为：

```
tos tos, ttl ttl, id id, offset offset, flags [flags], proto proto, length length, options (options)
```

`tos` 是服务类型字段；如果 ECN 位非零，则报告为 ECT(1)、ECT(0) 或 CE。`ttl` 是生存时间；如果为零则不报告。`id` 是 IP 标识字段。`offset` 是分片偏移字段；无论是否为分片数据报的一部分都会打印。`flags` 是 MF 和 DF 标志；如果设置了 MF 则报告 `+`，如果设置了 DF 则报告 `DF`。如果都未设置，则报告 `.`。`proto` 是协议 ID 字段。`length` 是总长度字段；如果数据包假定为 TSO（TCP Segmentation Offload）发送，则报告 `[was 0, presumed TSO]`。`options` 是 IP 选项（如果有）。

接下来，对于 TCP 和 UDP 数据包，会打印源和目标 IP 地址以及 TCP 或 UDP 端口，每个 IP 地址与其对应端口之间用点分隔，源和目标之间用 `>` 分隔。对于其他协议，会打印地址，源和目标之间用 `>` 分隔。之后会打印更高层协议信息（如果有）。

对于分片 IP 数据报，第一个分片包含更高层协议头；第一个分片之后的分片不包含更高层协议头。仅在 `-v` 标志下，在 IP 头信息中打印分片信息，如上所述。

### TCP 数据包

（注意：以下描述假定熟悉 RFC 793 中描述的 TCP 协议。如果你不熟悉该协议，此描述对你用处不大。）

TCP 协议行的一般格式为：

```
src > dst: Flags [tcpflags], seq data-seqno, ack ackno, win window, urg urgent, options [opts], length len
```

`Src` 和 `dst` 是源和目标 IP 地址和端口。`Tcpflags` 是 S（SYN）、F（FIN）、P（PSH）、R（RST）、U（URG）、W（CWR）、E（ECE）或 `.`（ACK）的某种组合，如果未设置任何标志则为 `none`。`Data-seqno` 描述此数据包中数据覆盖的序列空间部分（参见下面的示例）。`Ackno` 是另一方向上此连接预期的下一个数据的序列号。`Window` 是另一方向上此连接可用的接收缓冲区空间字节数。`Urg` 表示数据包中有 “紧急” 数据。`Opts` 是 TCP 选项（如 mss 1024）。`Len` 是有效载荷数据长度。

`Iptype`、`Src`、`dst` 和 `flags` 始终存在。其他字段取决于数据包 TCP 协议头的内容，仅在适当时输出。

以下是从主机 rtsg 到主机 csam 的 rlogin 的开头部分：

```
IP rtsg.1023 > csam.login: Flags [S], seq 768512:768512, win 4096, opts [mss 1024]
IP csam.login > rtsg.1023: Flags [S.], seq, 947648:947648, ack 768513, win 4096, opts [mss 1024]
IP rtsg.1023 > csam.login: Flags [.], ack 1, win 4096
IP rtsg.1023 > csam.login: Flags [P.], seq 1:2, ack 1, win 4096, length 1
IP csam.login > rtsg.1023: Flags [.], ack 2, win 4096
IP rtsg.1023 > csam.login: Flags [P.], seq 2:21, ack 1, win 4096, length 19
IP csam.login > rtsg.1023: Flags [P.], seq 1:2, ack 21, win 4077, length 1
IP csam.login > rtsg.1023: Flags [P.], seq 2:3, ack 21, win 4077, urg 1, length 1
IP csam.login > rtsg.1023: Flags [P.], seq 3:4, ack 21, win 4077, urg 1, length 1
```

第一行表示 rtsg 上的 TCP 端口 1023 向 csam 上的端口 login 发送了一个数据包。`S` 表示设置了 SYN 标志。数据包序列号为 768512，不包含数据。（表示法为 “first:last”，意为 “序列号从 first 到但不包括 last”。）没有附带 ACK，可用接收窗口为 4096 字节，有一个请求 1024 字节 MSS 的 max-segment-size 选项。

Csam 用类似数据包回复，但它包含对 rtsg 的 SYN 的附带 ACK。然后 Rtsg ACK csam 的 SYN。`.` 表示设置了 ACK 标志。数据包不包含数据，因此没有数据序列号或长度。注意，ACK 序列号是一个小整数（1）。`tcpdump` 首次看到 TCP “会话” 时，会打印数据包中的序列号。在会话的后续数据包中，会打印当前数据包序列号与此初始序列号之间的差值。这意味着第一个之后的序列号可解释为会话数据流中的相对字节位置（每个方向的第一个数据字节为 “1”）。`-S` 会覆盖此功能，使原始序列号输出。

第 6 行，rtsg 向 csam 发送 19 字节数据（rtsg → csam 方会话中的第 2 到 20 字节）。数据包中设置了 PSH 标志。第 7 行，csam 表示它已收到 rtsg 发送的数据，直到但不包括第 21 字节。由于 csam 的接收窗口缩小了 19 字节，这些数据大部分显然在套接字缓冲区中。Csam 还在此数据包中向 rtsg 发送一个字节数据。第 8 和 9 行，csam 向 rtsg 发送两字节紧急、推送数据。

如果快照足够小，`tcpdump` 未能捕获完整的 TCP 头，它会尽可能多地解释头，然后报告 “[|tcp]” 表示无法解释其余部分。如果头包含错误选项（长度太小或超出头尾），`tcpdump` 会将其报告为 “[bad opt]”，并不再解释任何进一步选项（因为无法判断它们的起始位置）。如果头长度指示存在选项但 IP 数据报长度不足以实际容纳选项，`tcpdump` 会将其报告为 “[bad hdr length]”。

### 特定 TCP 标志组合（SYN-ACK、URG-ACK 等）

TCP 头的控制位部分有 8 位：

- `CWR | ECE | URG | ACK | PSH | RST | SYN | FIN`

假设我们要观察用于建立 TCP 连接的数据包。回想 TCP 在初始化新连接时使用 3 次握手协议；就 TCP 控制位而言，连接序列为：

1. 调用方发送 SYN
2. 接收方以 SYN、ACK 响应
3. 调用方发送 ACK

现在我们有兴趣捕获仅设置 SYN 位的数据包（步骤 1）。注意，我们不想要步骤 2（SYN-ACK）的数据包，仅是普通的初始 SYN。我们需要的是 `tcpdump` 的正确过滤器表达式。

回想不带选项的 TCP 头结构：

```
0                   15                  31
-----------------------------------------------------------------
|          source port          |       destination port        |
-----------------------------------------------------------------
|                        sequence number                        |
-----------------------------------------------------------------
|                    acknowledgment number                      |
-----------------------------------------------------------------
|  HL   | rsvd |C|E|U|A|P|R|S|F|        window size            |
-----------------------------------------------------------------
|         TCP checksum          |       urgent pointer          |
-----------------------------------------------------------------
```

TCP 头通常容纳 20 字节数据，除非存在选项。图的第一行包含字节 0-3，第二行显示字节 4-7，依此类推。

从 0 开始计数，相关的 TCP 控制位位于字节 13：

```
0               7|             15|             23|             31
----------------|---------------|---------------|----------------
|  HL   | rsvd  |C|E|U|A|P|R|S|F|        window size            |
----------------|---------------|---------------|----------------
                                 |  13th octet   |
                                 |               |
```

仔细看第 13 个字节：

```
                               | |
                               |---------------|
                               |C|E|U|A|P|R|S|F|
                               |---------------|
                               |7   5   3   0  |
```

这些是我们感兴趣的 TCP 控制位。我们从此字节的位从 0 到 7 编号，从右到左，因此 PSH 位是第 3 位，URG 位是第 5 位。

回想我们要捕获仅设置 SYN 的数据包。看看当 TCP 数据报头中设置 SYN 位时，字节 13 会发生什么：

```
                               |C|E|U|A|P|R|S|F|
                               |---------------|
                               |0 0 0 0 0 0 1 0|
                               |---------------|
                               |7 6 5 4 3 2 1 0|
```

查看控制位部分，我们看到仅第 1 位（SYN）被设置。

假设字节 13 是网络字节序的 8 位无符号整数，此字节的二进制值为：

```
00000010
```

其十进制表示为：

```
7 6 5 4 3 2 1 0
0*2 + 0*2 + 0*2 + 0*2 + 0*2 + 0*2 + 1*2 + 0*2 = 2
```

我们几乎完成了，因为现在我们知道如果仅设置 SYN，TCP 头中第 13 个字节的值（当解释为网络字节序的 8 位无符号整数时）必须正好是 2。

此关系可表示为：

```
tcp[13] == 2
```

我们可以将此表达式用作 `tcpdump` 的过滤器，以观察仅设置 SYN 的数据包：

```sh
tcpdump -i xl0 'tcp[13] == 2'
```

该表达式表示 “让 TCP 数据报的第 13 个字节具有十进制值 2”，这正是我们想要的。

现在，假设我们需要捕获 SYN 数据包，但不关心 ACK 或任何其他 TCP 控制位是否同时设置。看看当设置 SYN-ACK 的 TCP 数据报到达时，字节 13 会发生什么：

```
                               |C|E|U|A|P|R|S|F|
                               |---------------|
                               |0 0 0 1 0 0 1 0|
                               |---------------|
                               |7 6 5 4 3 2 1 0|
```

现在第 13 个字节中设置了第 1 和第 4 位。字节 13 的二进制值为：

```
00010010
```

转换为十进制：

```
7 6 5 4 3 2 1 0
0*2 + 0*2 + 0*2 + 1*2 + 0*2 + 0*2 + 1*2 + 0*2 = 18
```

现在我们不能仅在 `tcpdump` 过滤器表达式中使用 “tcp[13] == 18”，因为那只会选择设置 SYN-ACK 的数据包，而不会选择仅设置 SYN 的数据包。记住，只要设置了 SYN，我们不关心 ACK 或任何其他控制位是否设置。

为达到目标，我们需要将字节 13 的二进制值与某个其他值进行逻辑与以保留 SYN 位。我们知道我们希望 SYN 在任何情况下都设置，因此我们将第 13 个字节的值与 SYN 的二进制值进行逻辑与：

```
00010010  SYN-ACK              00000010  SYN
AND 00000010  (we want SYN)    AND 00000010  (we want SYN)
--------                       --------
=   00000010                   =   00000010
```

我们看到此 AND 操作无论 ACK 或其他 TCP 控制位是否设置都交付相同结果。AND 值的十进制表示以及此操作的结果都是 2（二进制 00000010），因此我们知道对于设置了 SYN 的数据包，以下关系必须成立：

```
( ( value of octet 13 ) AND ( 2 ) ) == ( 2 )
```

这指向 `tcpdump` 过滤器表达式：

```sh
tcpdump -i xl0 'tcp[13] & 2 == 2'
```

某些偏移和字段值可以用名称而非数字表示。例如，`tcp[13]` 可替换为 `tcp[tcpflags]`。以下 TCP 标志字段值也可用：`tcp-fin`、`tcp-syn`、`tcp-rst`、`tcp-push`、`tcp-ack`、`tcp-urg`、`tcp-ece` 和 `tcp-cwr`。

这可以演示为：

```sh
tcpdump -i xl0 'tcp[tcpflags] & tcp-push != 0'
```

注意，你应在表达式中使用单引号或反斜杠以隐藏 AND（“&”）特殊字符不传递给 shell。

### UDP 数据包

UDP 格式由这个 rwho 数据包说明：

```
actinide.who > broadcast.who: udp 84
```

这表示主机 actinide 上的端口 who 向主机 broadcast（Internet 广播地址）上的端口 who 发送了一个 UDP 数据报。该数据包包含 84 字节用户数据。

某些 UDP 服务会被识别（从源或目标端口号），并打印更高层协议信息。特别是，域名服务请求（RFC 1034/1035）和 Sun RPC 调用（RFC 1050）到 NFS。

### TCP 或 UDP 名称服务器请求

（注意：以下描述假定熟悉 RFC 1035 中描述的域名服务协议。如果你不熟悉该协议，以下描述将看起来像希腊语。）

名称服务器请求格式为：

```
src > dst: id op? flags qtype qclass name (len)
h2opolo.1538 > helios.domain: 3+ A? ucbvax.berkeley.edu. (37)
```

主机 h2opolo 向 helios 上的域名服务器请求与名称 ucbvax.berkeley.edu 关联的地址记录（qtype=A）。查询 ID 为 “3”。“+” 表示设置了递归期望标志。查询长度为 37 字节，不包括 TCP 或 UDP 和 IP 协议头。查询操作是正常的 Query，因此省略了 op 字段。如果 op 是其他任何值，它将打印在 “3” 和 “+” 之间。类似地，qclass 是正常的 C_IN，被省略。任何其他 qclass 将紧跟 “A” 打印。

检查少数异常并可能导致方括号中的额外字段：如果查询包含回答、授权记录或附加记录部分，`ancount`、`nscount` 或 `arcount` 会打印为 “[na]”、”[nn]” 或 “[nau]”，其中 n 是相应的计数。如果设置了任何响应位（AA、RA 或 rcode）或第二和第三字节中的任何 “必须为零” 位被设置，则打印 “[b2&3=x]”，其中 x 是头字节二和三的十六进制值。

### TCP 或 UDP 名称服务器响应

名称服务器响应格式为：

```
src > dst: id op rcode flags a/n/au type class data (len)
helios.domain > h2opolo.1538: 3 3/3/7 A 128.32.137.3 (273)
helios.domain > h2opolo.1537: 2 NXDomain* 0/1/0 (97)
```

第一个示例中，helios 用 3 个回答记录、3 个名称服务器记录和 7 个附加记录响应 h2opolo 的查询 ID 3。第一个回答记录类型为 A（地址），其数据为 internet 地址 128.32.137.3。响应总大小为 273 字节，不包括 TCP 或 UDP 和 IP 头。op（Query）和响应代码（NoError）被省略，A 记录的类（C_IN）也被省略。

第二个示例中，helios 用不存在域（NXDomain）的响应代码、无回答、一个名称服务器和无授权记录响应查询 2。“*” 表示设置了权威回答位。由于没有回答，未打印类型、类或数据。

其他可能出现的标志字符有 “-”（递归可用，RA，未设置）和 “|”（截断消息，TC，设置）。如果 “question” 部分不包含正好一个条目，则打印 “[nq]”。

### SMB/CIFS 解码

`tcpdump` 现在包含对 UDP/137、UDP/138 和 TCP/139 上数据的相当广泛的 SMB/CIFS/NBT 解码。还对 IPX 和 NetBEUI SMB 数据进行了一些原始解码。

默认情况下进行相当少的解码，如果使用 `-v` 则进行更详细的解码。请注意，使用 `-v` 时，单个 SMB 数据包可能占用一页或更多，因此仅在确实想要所有血腥细节时才使用 `-v`。

有关 SMB 数据包格式和所有字段含义的信息，参见 https://download.samba.org/pub/samba/specs/ 和其他在线资源。SMB 补丁由 Andrew Tridgell（tridge@samba.org）编写。

### NFS 请求和回复

Sun NFS（Network File System）请求和回复打印为：

```
src.sport > dst.nfs: NFS request xid xid len op args
src.nfs > dst.dport: NFS reply xid xid reply stat len op results
sushi.1023 > wrl.nfs: NFS request xid 26377
	112 readlink fh 21,24/10.73165
wrl.nfs > sushi.1023: NFS reply xid 26377
	reply ok 40 readlink "../var"
sushi.1022 > wrl.nfs: NFS request xid 8219
	144 lookup fh 9,74/4096.6878 "xcolors"
wrl.nfs > sushi.1022: NFS reply xid 8219
	reply ok 128 lookup fh 9,74/4134.3150
```

第一行，主机 sushi 向 wrl 发送一个 ID 为 26377 的事务。请求为 112 字节，不包括 UDP 和 IP 头。操作是对文件句柄（fh）21,24/10.731657119 的 readlink（读取符号链接）。（如果幸运的话，如本例所示，文件句柄可以解释为 major、minor 设备号对，后跟 inode 号和生成号。）第二行，wrl 用相同事务 ID 和链接内容回复 “ok”。

第三行，sushi（使用新事务 ID）请求 wrl 在目录文件 9,74/4096.6878 中查找名称 “xcolors”。第四行，wrl 用相应事务 ID 发送回复。

注意，打印的数据取决于操作类型。该格式旨在与 NFS 协议规范一起阅读时自解释。还注意，旧版本的 `tcpdump` 以略有不同的格式打印 NFS 数据包：会打印事务 ID（xid）而非数据包的非 NFS 端口号。

如果给出 `-v`（详细）标志，会打印附加信息。例如：

```
sushi.1023 > wrl.nfs: NFS request xid 79658
	148 read fh 21,11/12.195 8192 bytes @ 24576
wrl.nfs > sushi.1023: NFS reply xid 79658
	reply ok 1472 read REG 100664 ids 417/0 sz 29388
```

（`-v` 还打印 IP 头 TTL、ID、长度和分片字段，本例中已省略。）第一行，sushi 请求 wrl 从文件 21,11/12.195 的字节偏移 24576 处读取 8192 字节。Wrl 回复 “ok”；第二行显示的数据包是回复的第一个分片，因此仅 1472 字节长（其他字节将在后续分片中跟随，但这些分片没有 NFS 甚至 UDP 头，因此可能不会打印，取决于使用的过滤器表达式）。由于给出了 `-v` 标志，会打印一些文件属性（与文件数据一起返回）：文件类型（“REG”，常规文件）、文件模式（八进制）、UID 和 GID 以及文件大小。

如果多次给出 `-v` 标志，会打印更多细节。

NFS 回复数据包不显式标识 RPC 操作。相反，`tcpdump` 跟踪 “最近” 的请求，并使用事务 ID 将它们与回复匹配。如果回复未紧跟相应请求，可能无法解析。

### AFS 请求和回复

Transarc AFS（Andrew File System）请求和回复打印为：

```
src.sport > dst.dport: rx packet-type
src.sport > dst.dport: rx packet-type service call call-name args
src.sport > dst.dport: rx packet-type service reply call-name args
elvis.7001 > pike.afsfs:
	rx data fs call rename old fid 536876964/1/1 ".newsrc.new"
	new fid 536876964/1/1 ".newsrc"
pike.afsfs > elvis.7001: rx data fs reply rename
```

第一行，主机 elvis 向 pike 发送一个 RX 数据包。这是到 fs（fileserver）服务的 RX 数据数据包，是 RPC 调用的开始。RPC 调用是 rename，旧目录文件 ID 为 536876964/1/1，旧文件名为 “.newsrc.new”，新目录文件 ID 为 536876964/1/1，新文件名为 “.newsrc”。主机 pike 用对 rename 调用的 RPC 回复响应（成功，因为它是数据数据包而非中止数据包）。

通常，所有 AFS RPC 至少按 RPC 调用名解码。大多数 AFS RPC 至少解码部分参数（通常仅 “有趣” 参数，对于有趣的某些定义）。

该格式旨在自描述，但对不熟悉 AFS 和 RX 工作的人可能没用。

如果给出 `-v`（详细）标志两次，会打印确认数据包和附加头信息，如 RX 调用 ID、调用号、序列号、序列号和 RX 数据包标志。

如果给出 `-v` 标志两次，会打印附加信息，如 RX 调用 ID、序列号和 RX 数据包标志。还会从 RX ack 数据包打印 MTU 协商信息。

如果给出 `-v` 标志三次，会打印安全索引和服务 ID。

会为中止数据包打印错误代码，但 Ubik beacon 数据包除外（因为中止数据包用于表示对 Ubik 协议的赞成票）。

AFS 回复数据包不显式标识 RPC 操作。相反，`tcpdump` 跟踪 “最近” 的请求，并使用调用号和服务 ID 将它们与回复匹配。如果回复未紧跟相应请求，可能无法解析。

### KIP AppleTalk（DDP in UDP）

封装在 UDP 数据报中的 AppleTalk DDP 数据包会被解封装并作为 DDP 数据包转储（即丢弃所有 UDP 头信息）。文件 **/etc/atalk.names** 用于将 AppleTalk 网络和节点号转换为名称。此文件中的行形式为：

```
number	name
1.254		ether
16.1		icsd-net
1.254.110	ace
```

前两行给出 AppleTalk 网络的名称。第三行给出特定主机的名称（主机通过编号中的第 3 个字节与网络区分——网络号必须有两个字节，主机号必须有三个字节）。编号和名称应以空白（空格或制表符）分隔。**/etc/atalk.names** 文件可包含空行或注释行（以 “#” 开头的行）。

AppleTalk 地址以以下形式打印：

```
net.host.port
144.1.209.2 > icsd-net.112.220
office.2 > icsd-net.112.220
jssmag.149.235 > icsd-net.2
```

（如果 **/etc/atalk.names** 不存在或不包含某个 AppleTalk 主机/网络号的条目，地址以数字形式打印。）第一个示例中，网络 144.1 节点 209 上的 NBP（DDP 端口 2）正在发送到网络 icsd 节点 112 上端口 220 的任何监听者。第二行相同，只是源节点的全名已知（“office”）。第三行是从网络 jssmag 节点 149 上端口 235 到 icsd-net NBP 端口上的广播的发送（注意，广播地址（255）由没有主机号的网络名指示——因此最好在 /etc/atalk.names 中保持节点名和网络名不同）。

NBP（名称绑定协议）和 ATP（AppleTalk 事务协议）数据包会解释其内容。其他协议仅转储协议名（如果没有为协议注册名称，则为编号）和数据包大小。

### NBP 数据包

NBP 数据包格式类似于以下示例：

```
icsd-net.112.220 > jssmag.2: nbp-lkup 190: "=:LaserWriter@*"
jssmag.209.2 > icsd-net.112.220: nbp-reply 190: "RM1140:LaserWriter@*" 250
techpit.2 > icsd-net.112.220: nbp-reply 190: "techpit:LaserWriter@*" 186
```

第一行是网络 icsd 主机 112 发送的 laserwriter 名称查找请求，广播到网络 jssmag。查找的 nbp ID 为 190。第二行显示此请求的回复（注意它具有相同 ID），来自主机 jssmag.209，表示它在端口 250 上注册了名为 “RM1140” 的 laserwriter 资源。第三行是对同一请求的另一回复，表示主机 techpit 在端口 186 上注册了 laserwriter “techpit”。

### ATP 数据包

ATP 数据包格式由以下示例演示：

```
jssmag.209.165 > helios.132: atp-req 12266<0-7> 0xae030001
helios.132 > jssmag.209.165: atp-resp 12266:0 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp 12266:1 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp 12266:2 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp 12266:3 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp 12266:4 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp 12266:5 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp 12266:6 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp*12266:7 (512) 0xae040000
jssmag.209.165 > helios.132: atp-req 12266<3,5> 0xae030001
helios.132 > jssmag.209.165: atp-resp 12266:3 (512) 0xae040000
helios.132 > jssmag.209.165: atp-resp 12266:5 (512) 0xae040000
jssmag.209.165 > helios.132: atp-rel 12266<0-7> 0xae030001
jssmag.209.133 > helios.132: atp-req* 12267<0-7> 0xae030002
```

Jssmag.209 通过请求最多 8 个数据包（“<0-7>”）与主机 helios 启动事务 ID 12266。行尾的十六进制数是请求中 “userdata” 字段的值。

Helios 用 8 个 512 字节的数据包响应。事务 ID 后的 “:digit” 给出事务中的数据包序列号，括号中的数字是数据包中的数据量，不包括 ATP 头。数据包 7 上的 “*” 表示设置了 EOM 位。

Jssmag.209 然后请求重传数据包 3 和 5。Helios 重发它们，然后 jssmag.209 释放事务。最后，jssmag.209 启动下一个请求。请求上的 “*” 表示未设置 XO（“exactly once”）。

## 向后兼容性

TCP 标志名 `tcp-ece` 和 `tcp-cwr` 在与 libpcap 1.9.0 或更高版本链接时可用。

## 参见

stty(1), pcap(3PCAP), bpf(4), nit(4P), pcap-savefile(@MAN_FILE_FORMATS@), pcap-filter(@MAN_MISC_INFO@), pcap-tstamp(@MAN_MISC_INFO@)

<https://www.iana.org/assignments/media-types/application/vnd.tcpdump.pcap>

## 作者

原作者为：

Van Jacobson、Craig Leres 和 Steven McCanne，均来自 Lawrence Berkeley National Laboratory, University of California, Berkeley, CA。

目前由 The Tcpdump Group 维护。

当前版本可通过 HTTPS 获取：

<https://www.tcpdump.org/>

原始发行版可通过匿名 ftp 获取：

<ftp://ftp.ee.lbl.gov/old/tcpdump.tar.Z>

IPv6/IPsec 支持由 WIDE/KAME 项目添加。本程序在特定配置下使用 OpenSSL/LibreSSL。

## 缺陷

报告安全问题请发送电子邮件至 security@tcpdump.org。

报告 bug 和其他问题、贡献补丁、请求功能、提供通用反馈等，请参见 `tcpdump` 源码树根目录中的 `CONTRIBUTING.md` 文件。

NIT 不允许你观察自己的出站流量，BPF 会。我们建议你使用后者。

应尝试重新组装 IP 分片，或至少为更高层协议计算正确长度。

名称服务器反向查询未被正确转储：打印的是（空的）问题部分而非回答部分中的真实查询。有些人认为反向查询本身就是一个 bug，宁愿修复生成它们的程序而非 `tcpdump`。

跨越夏令时更改的数据包跟踪会给出歪斜的时间戳（时间更改被忽略）。

Token Ring 头中字段以外的字段上的过滤器表达式不会正确处理源路由 Token Ring 数据包。

802.11 头中字段以外的字段上的过滤器表达式不会正确处理同时设置 To DS 和 From DS 的 802.11 数据数据包。

`ip6 proto` 应追踪头链，但目前不会。`ip6 protochain` 用于此行为。

针对传输层头的算术表达式（如 `tcp[0]`）对 IPv6 数据包不起作用。它仅查看 IPv4 数据包。
