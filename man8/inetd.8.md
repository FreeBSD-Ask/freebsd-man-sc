# inetd(8)

`inetd` — 互联网“超级服务器”

## 名称

`inetd` “超级服务器”

## 概要

`inetd [-dlWw] [-a address] [-C rate] [-c maximum] [-p pidfile] [-R rate] [-s maximum] [configuration_file]`

## 描述

`inetd` 工具应在引导时由 **/etc/rc** 启动（参见 [rc(8)](rc.8.md)）。随后它监听某些互联网套接字上的连接。当在其某个套接字上发现连接时，它判断该套接字对应的服务，并调用一个程序来处理请求。服务器程序以服务套接字作为其标准输入、输出和错误描述符被调用。程序完成后，`inetd` 继续监听该套接字（下文将描述某些例外情况）。本质上，`inetd` 允许运行一个守护进程来调用其他多个守护进程，从而减轻系统负载。

可用选项如下：

**`-a`** `address` 指定要绑定的一个特定 IP 地址。也可以指定主机名，此时使用与该主机名对应的 IPv4 或 IPv6 地址。通常在 [jail(8)](jail.8.md) 中运行 `inetd` 时指定主机名，此时主机名对应于 [jail(8)](jail.8.md) 环境的主机名。使用主机名指定且同时需要 IPv4 和 IPv6 绑定时，**/etc/inetd.conf** 中每个服务需要为每种绑定提供一个具有相应 *protocol* 类型的条目。例如，基于 TCP 的服务需要两个条目，一个使用“tcp4”作为 *protocol*，另一个使用“tcp6”。参见下面对 **/etc/inetd.conf** *protocol* 字段的说明。

**`-C`** `rate` 指定每分钟从单个 IP 地址调用服务的默认最大次数；默认为无限。可通过每服务级别的“max-connections-per-ip-per-minute”参数覆盖。

**`-c`** `maximum` 指定每个服务的同时调用默认最大数量；默认为无限。可通过每服务级别的“max-child”参数覆盖。

**`-d`** 开启调试。

**`-l`** 开启成功连接的日志记录。

**`-p`** `pidfile` 指定一个备用文件来存储进程 ID。

**`-R`** `rate` 指定每分钟可调用服务的最大次数；默认为 256。比率为 0 表示允许无限次调用。

**`-s`** `maximum` 指定从单个 IP 地址同时调用每个服务的默认最大数量；默认为无限。可通过每服务级别的“max-child-per-ip”参数覆盖。

**`-W`** 为 `inetd` 内置的内部服务开启 TCP Wrappers。

**`-w`** 为外部服务开启 TCP Wrappers。有关 TCP Wrappers 支持的更多信息，请参见实现说明章节。

执行时，`inetd` 从配置文件中读取其配置信息，默认文件为 **/etc/inetd.conf** 。配置文件的每个字段都必须有条目，各字段条目之间以制表符或空格分隔。以“#”开头的行表示注释。每个字段都必须有条目。配置文件的字段如下：

```
service-name
socket-type
protocol
{wait|nowait}[/max-child[/max-connections-per-ip-per-minute[/max-child-per-ip]]]
user[:group][/login-class]
server-program
server-program-arguments
```

要指定基于 ONC RPC 的服务，条目包含以下字段：

```
service-name/version
socket-type
rpc/protocol
{wait|nowait}[/max-child[/max-connections-per-ip-per-minute[/max-child-per-ip]]]
user[:group][/login-class]
server-program
server-program-arguments
```

`inetd` 可启动两种类型的服务：标准和 TCPMUX。标准服务分配有公认的端口；它可以是实现官方互联网标准或 BSD 特定服务的服务。如 RFC 1078 所述，TCPMUX 服务是未分配公认端口的非标准服务。当程序连接到“tcpmux”公认端口并指定服务名时，`inetd` 会调用它们。此功能对于添加本地开发的服务器很有用。仅当多路复用器服务本身被启用时，TCPMUX 请求才会被接受（这独立于具体的基于 TCPMUX 的服务器之外）；参见下文对内部服务的讨论。

*service-name* 条目是 **/etc/services** 文件中有效服务的名称，或 UNIX 域套接字的规范（见下文）。对于“内部”服务（下文讨论），服务名应为该服务的官方名称（即 **/etc/services** 中的第一个条目）。用于指定基于 ONC RPC 的服务时，此字段是 **/etc/rpc** 文件中列出的有效 RPC 服务名。“/”右侧的部分是 RPC 版本号。可以只是单个数字参数或版本范围。范围由低版本到高版本界定——例如“rusers/1-3”。对于 TCPMUX 服务，*service-name* 字段的值由字符串“tcpmux”后跟斜杠和本地选择的服务名组成。**/etc/services** 中列出的服务名和名称“help”被保留。请尽量通过在 TCPMUX 服务名前加组织名称、后加版本号后缀来选择唯一的名称。

*socket-type* 应为“stream”、“dgram”、“raw”、“rdm”或“seqpacket”之一，分别对应流、数据报、原始、可靠传递消息或有序分组套接字。TCPMUX 服务必须使用“stream”。

*protocol* 必须是有效的协议或“unix”。例如“tcp”或“udp”，为向后兼容两者均隐含 IPv4。“tcp4”和“udp4”指定仅 IPv4。“tcp6”和“udp6”指定仅 IPv6。“tcp46”和“udp46”指定条目通过通配 `AF_INET6` 套接字同时接受 IPv4 和 IPv6 连接。基于 RPC 的服务使用“rpc/tcp”或“rpc/udp”服务类型指定。可以使用 4、6 或 46 后缀指定 IPv4 和/或 IPv6，例如“rpc/tcp6”或“rpc/udp46”。TCPMUX 服务必须使用“tcp”、“tcp4”、“tcp6”或“tcp46”。

*wait/nowait* 条目指定由 `inetd` 调用的服务器是否将接管与服务访问点关联的套接字，从而决定 `inetd` 是否应等待服务器退出后再监听新的服务请求。数据报服务器必须使用“wait”，因为它们总是以绑定到指定服务地址的原始数据报套接字被调用。这些服务器在退出前必须至少从套接字读取一个数据报。如果数据报服务器连接到其对端，释放套接字使 `inetd` 能在该套接字上接收更多消息，则称为“多线程”服务器；它应从套接字读取一个数据报并创建一个连接到对端的新套接字。它应 fork，然后父进程退出以允许 `inetd` 检查新的服务请求以生成新的服务器。在套接字上处理所有传入数据报并最终超时的数据报服务器称为“单线程”。comsat(8) 和 talkd(8) 工具是后一类数据报服务器的示例。[tftpd(8)](tftpd.8.md) 工具是多线程数据报服务器的示例。

使用流套接字的服务器通常是多线程的，使用“nowait”条目。这些服务的连接请求由 `inetd` 接受，服务器仅获得连接到服务客户端的新接受套接字。大多数基于流的服务以此方式运行。使用“wait”的基于流的服务器以监听服务套接字启动，在退出前必须至少接受一个连接请求。此类服务器通常会接受并处理传入连接请求直到超时。TCPMUX 服务必须使用“nowait”。

“nowait”服务的未完成子进程（或“线程”）最大数量可通过在“nowait”关键字后附加“/”和数字来显式指定。通常（或指定值为零时）没有最大值限制。否则，一旦达到最大值，进一步的连接尝试将排队等待，直到现有子进程退出。这在“wait”模式下也适用，尽管非一（默认）的值在某些情况下可能没有意义。你还可以通过在最大未完成子进程数后附加“/”和数字来指定给定 IP 地址每分钟的最大连接数。一旦达到最大值，该 IP 地址的进一步连接将被丢弃，直到该分钟结束。此外，你还可以通过在最大未完成子进程数后附加“/”和数字来指定从单个 IP 地址同时调用每个服务的最大数量。一旦达到最大值，该 IP 地址的进一步连接将被丢弃。

*user* 条目应包含服务器运行时所使用的用户名。这允许服务器获得比 root 更少的权限。以“:”分隔的可选 *group* 部分允许指定非该用户默认组的组名。以“/”分隔的可选 *login-class* 部分允许指定非默认“daemon”登录类的登录类。

*server-program* 条目应包含当 `inetd` 在其套接字上发现请求时要执行的程序路径名。如果 `inetd` 内部提供此服务，此条目应为“internal”。

*server-program-arguments* 条目列出要传递给 *server-program* 的参数，以 argv[0] 开头（通常是程序名）。如果服务是内部提供的，该服务的 *service-name*（及其任何参数）或单词“internal”应取代此条目。

目前，唯一接受参数的内部服务是“auth”。不带选项时，该服务始终返回“ERROR : HIDDEN-USER”。改变此服务行为的可用参数如下：

**`-d`** `fallback` 提供一个 `fallback` 用户名。如果真正的“auth”服务已启用（使用下文讨论的 `-r` 选项），当套接字凭据或用户名查找失败时，返回此用户名而非错误。如果真正的“auth”服务已禁用，则对每个请求都返回此用户名。这主要在 NAT 机器上运行此服务时有用。

**`-F`** 与 `-f` 相同，但不限制 **.fakeid** 中的用户名不能与现有用户匹配。

**`-f`** 如果在被识别用户的主目录中存在 **.fakeid** 文件，则报告该文件中的用户名而非真实用户名。如果 **.fakeid** 中的用户名是现有用户，则报告真实用户名。如果同时给出 `-i` 标志，则 **.fakeid** 中的用户名将改为与现有用户 ID 进行核对。

**`-g`** 不向 ident 请求者返回用户名，而是报告一个由随机字母数字字符组成的用户名，例如“c0c993”。`-g` 标志不仅覆盖用户名，还覆盖任何 fallback 名称、**.fakeid** 或 **.noident** 文件。

**`-i`** 返回数字用户 ID 而非用户名。

**`-n`** 如果在被识别用户的主目录中存在 **.noident** 文件，则返回“ERROR : HIDDEN-USER”。这会覆盖可能存在的任何 `fakeid` 文件。

**`-o`** `osname` 使用 `osname` 代替 uname(3) 报告的系统名称。

**`-r`** 提供符合 RFC 1413 的真正“auth”服务。所有其余标志仅在此情况下适用。

**`-t`** `sec`[`.usec`] 指定该服务的超时时间。默认超时为 10.0 秒。

`inetd` 工具还通过自身内部的例程提供了其他几个“简单”服务。这些服务是“echo”、“discard”、“chargen”（字符生成器）、“daytime”（人类可读时间）和“time”（机器可读时间，自 1900 年 1 月 1 日午夜以来的秒数）。所有这些服务都有 TCP 和 UDP 两个版本；如果请求指定的回复端口对应任何内部服务，UDP 版本将拒绝服务。（这是为了防御循环攻击；远程 IP 地址会被记录。）有关这些服务的详情，请参阅相应的 RFC 文档。

TCPMUX 多路分解服务也作为内部服务实现。要使任何基于 TCPMUX 的服务正常工作，必须在 inetd.conf 中包含以下行：

```sh
tcpmux	stream	tcp	nowait	root	internal
```

指定 `-l` 选项时，`inetd` 每次接受连接都会向 syslog 记录一条日志，注明所选服务和远程请求者的 IP 号（如果可用）。除非配置文件中另有指定，且未指定 `-W` 和 `-w` 选项，`inetd` 将记录到“daemon”设施。

`inetd` 收到挂起信号 `SIGHUP` 时会重新读取配置文件。重新读取配置文件时可添加、删除或修改服务。除非以调试模式启动，或使用 `-p` 选项另行配置，`inetd` 会将其进程 ID 记录在 **/var/run/inetd.pid** 文件中，以协助重新配置。

## 实现说明

### TCP Wrappers

指定 `-w` 选项时，`inetd` 会包装所有指定为“stream nowait”或“dgram”的服务，但“internal”服务除外。如果指定 `-W` 选项，此类“internal”服务也将被包装。如果同时指定两个选项，内部和外部服务的包装都将启用。任一包装选项都会导致失败的连接被记录到“auth”syslog 设施。在包装选项中加入 `-l` 标志会将成功的连接也包含在“auth”设施的日志中。

注意，`inetd` 仅在没有可用服务器处理请求时才包装“wait”服务的请求。一旦允许了到此类服务的连接，`inetd` 对后续到该服务的连接没有控制权，直到没有更多服务器在监听连接请求。

启用包装时，不需要 `tcpd` 守护进程，因为该功能是内置的。有关 TCP Wrappers 的更多信息，请参阅相关文档（hosts_access(5)）。阅读该文档时，请注意“internal”服务没有关联的守护进程名。因此，inetd.conf 中指定的服务名应用作“internal”服务的守护进程名。

### TCPMUX

RFC 1078 描述了 TCPMUX 协议：“TCP 客户端连接到远程主机的 TCP 端口 1。它发送服务名，后跟回车换行 <CRLF>。服务名不区分大小写。服务器以单个字符回复，指示肯定 (+) 或否定 (-) 确认，紧接着是可选的说明消息，以 <CRLF> 结束。如果回复为肯定，则所选协议开始；否则连接关闭。”程序通过文件描述符 0 和 1 获得 TCP 连接。

如果 TCPMUX 服务名以“+”开头，`inetd` 会为程序返回肯定回复。这允许你调用使用 stdin/stdout 的程序，而无需在其中放入特殊的服务器代码。

特殊服务名“help”会使 `inetd` 列出 inetd.conf 中已启用的 TCPMUX 服务。

### IPsec

实现中包含一个小技巧，以支持每个套接字的 IPsec 策略设置。一种特殊形式的注释行，以“#@”开头，被解释为策略说明符。“#@”之后的所有内容将用作 IPsec 策略字符串，如 ipsec_set_policy(3) 所述。每个策略说明符应用于 inetd.conf 中其后的所有行，直到下一个策略说明符。空的策略说明符重置 IPsec 策略。

如果 inetd.conf 中出现无效的 IPsec 策略说明符，`inetd` 将通过 syslog(3) 接口提供错误消息并中止执行。

### UNIX 域套接字

除了在 IP 套接字上运行服务外，`inetd` 还可以管理 UNIX 域套接字。为此，你需指定 *protocol* 为“unix”，并将 UNIX 域套接字指定为 *service-name*。*service-type* 可以为“stream”或“dgram”。套接字的规范必须是绝对路径名，可选地以 *:user:group:mode:* 形式的所有者和模式为前缀。以下规范：

```sh
:news:daemon:220:/var/run/sock
```

创建一个由用户“news”、组“daemon”拥有的套接字，权限仅允许该用户和组连接。默认所有者是运行 `inetd` 的用户。默认模式仅允许套接字的所有者连接。

**警告：** 创建 UNIX 域套接字时，`inetd` 必须更改套接字的所有权和权限。只有当创建套接字的目录仅可由 root 写入时，才能安全地执行此操作。*不要*使用 `inetd` 在 **/tmp** 等全局可写目录中创建套接字；请改用 **/var/run** 或类似目录。

内部服务可以按通常方式在 UNIX 域套接字上运行。在这种情况下，内部服务的名称使用套接字路径名的最后一个组件确定。例如，指定名为 **/var/run/chargen** 的套接字会在该套接字上收到连接时调用“chargen”服务。

## 文件

**`/etc/inetd.conf`** 配置文件
**`/etc/netconfig`** 网络配置数据库
**`/etc/rpc`** 服务名到 RPC 程序号的转换
**`/etc/services`** 服务名到端口号的转换
**`/var/run/inetd.pid`** 当前运行的 `inetd` 的 pid

## 实例

**/etc/inetd.conf** 中提供了多种服务的示例。

## 错误消息

`inetd` 服务器使用 syslog(3) 记录错误消息。重要的错误消息及其说明如下：

**`service`/`protocol` server failing (looping), service terminated.** 过去一分钟内对指定服务的请求数超过了限制。该限制用于防止有缺陷的程序或恶意用户淹没系统。出现此消息可能有以下原因：

- 短时间内有许多主机请求该服务。
- 有缺陷的客户端程序过于频繁地请求该服务。
- 恶意用户运行程序在拒绝服务攻击中调用该服务。
- 被调用的服务程序有错误，导致客户端快速重试。

使用 `-R` `rate` 选项（如上所述）更改速率限制。一旦达到限制，服务将在 10 分钟后自动重新启用。

**`service`/`protocol`: No such user `user`, service ignored**
**`service`/`protocol`: getpwnam: `user`: No such user** [passwd(5)](../man5/passwd.5.md) 数据库中不存在 `user` 的条目。第一条消息在 `inetd`（重新）读取配置文件时出现。第二条消息在调用服务时出现。

**`service`: can't set uid `uid`**
**`service`: can't set gid `gid`** 条目的 `user` 字段中的用户或组 ID 无效。

**setsockopt(SO_PRIVSTATE):** Operation not supported `inetd` 工具尝试放弃与套接字关联的特权状态，但未能成功。

**unknown `rpc/udp` or `rpc/tcp`** netconfig(5) 数据库中未找到 `udp` 或 `tcp` 的条目。

**unknown `rpc/udp6` or `rpc/tcp6`** netconfig(5) 数据库中未找到 `udp6` 或 `tcp6` 的条目。

## 参见

cvs(1) (`ports/devel/opencvs`), [date(1)](../man1/date.1.md), [nc(1)](../man1/nc.1.md), ipsec_set_policy(3), [ipsec(4)](../man4/ipsec.4.md), hosts_access(5), hosts_options(5), login.conf(5), netconfig(5), [passwd(5)](../man5/passwd.5.md), rpc(5), [services(5)](../man5/services.5.md), bootpd(8), comsat(8), fingerd(8), [ftpd(8)](ftpd.8.md) (`ports/ftp/freebsd-ftpd`), imapd(8) (`ports/mail/courier-imap`), nmbd(8) (`ports/net/samba412`), rlogind(8), rpc.rquotad(8), [rpc.rusersd(8)](rpc.rusersd.8.md), rpc.rwalld(8), rpc.statd(8), rshd(8), prometheus_sysctl_exporter(8), smbd(8) (`ports/net/samba412`), talkd(8), telnetd(8) (`ports/net/freebsd-telnetd`), [tftpd(8)](tftpd.8.md), uucpd(8) (`ports/net/freebsd-uucp`)

> Michael C. St. Johns, "Identification Protocol", RFC1413.

## 历史

`inetd` 工具出现于 4.3BSD。TCPMUX 基于 Mark Lottor 的代码和文档。对基于 ONC RPC 的服务的支持是模仿 SunOS 4.1 提供的功能。IPsec 技巧由 KAME 项目于 1999 年贡献。FreeBSD TCP Wrappers 支持首次出现于 FreeBSD 3.2。
