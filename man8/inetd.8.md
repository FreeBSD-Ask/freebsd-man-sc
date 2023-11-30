  INETD(8)  

INETD(8)

FreeBSD System Manager's Manual

INETD(8)

[名称](#__u540D___u79F0_)
=======================

`inetd` —

互联网 “超级服务器”

[概要](#__u6982___u8981_)
=======================

`inetd` \[`-d`\] \[`-l`\] \[`-w`\] \[`-W`\] \[`-c` maximum\] \[`-C` rate\] \[`-a` address | hostname\] \[`-p` filename\] \[`-R` rate\] \[`-s` maximum\] \[configuration file\]

[描述](#__u63CF___u8FF0_)
=======================

`inetd` 实用程序应在引导时由 /etc/rc 运行（请参阅 rc(8) ）。 然后它会侦听某些 Internet 套接字上的连接。 当在其中一个套接字上找到连接时，它会决定该套接字对应于什么服务，并调用一个程序来为请求提供服务。 使用服务套接字作为其标准输入、输出和错误描述符来调用服务器程序。 程序完成后， `inetd` 会继续监听套接字（某些情况下会在下面描述）。 从本质上讲， `inetd` 允许运行一个守护进程来调用其他几个守护进程，从而减少系统负载。

可以使用以下选项：

[`-d`](#d)

打开调试。

[`-l`](#l)

打开成功连接的日志记录。

[`-w`](#w)

为外部服务打开 TCP Wrapping。 有关 TCP Wrappers 支持的更多信息，请参阅 [实施说明](#__u5B9E___u65BD___u8BF4___u660E_) 部分。

[`-W`](#W)

为 `inetd` 内置的内部服务打开 TCP Wrapping。

[`-c`](#c) maximum

指定每个服务的默认最大同时调用次数；默认为无限制。 可以使用 "max-child" 参数在每个服务的基础上覆盖。

[`-C`](#C) rate

指定一分钟内单个IP地址可以调用服务的默认最大次数；默认为无限制。 可以使用 "max-connections-per-ip-per-minute" 参数在每个服务的基础上覆盖。

[`-R`](#R) rate

指定服务在一分钟内可以调用的最大次数；默认值为 256。 速率为 0 允许无限次数的调用。

[`-s`](#s) maximum

指定从单个 IP 地址同时调用每个服务的默认最大数量；默认为无限制。 可以使用 "max-child-per-ip" 参数在每个服务的基础上覆盖。

[`-a`](#a)

指定一个要绑定的特定 IP 地址。或者，可以指定主机名，在这种情况下，使用与该主机名对应的 IPv4 或 IPv6 地址。 通常，当 `inetd` 在 jail(8) 中运行时会指定主机名，在这种情况下，主机名对应于 jail(8) 环境的主机名。

当使用主机名规范并且需要 IPv4 和 IPv6 绑定时， /etc/inetd.conf 中的每个服务都需要一个具有每个绑定的适当 _protocol_ 类型的条目。 例如，基于 TCP 的服务需要两个条目，一个使用 “tcp4” 作为 _protocol_ ，另一个使用 “tcp6” 。 请参阅下面的 /etc/inetd.conf _protocol_ 字段的说明。

[`-p`](#p)

指定用于存储进程 ID 的备用文件。

在执行时， `inetd` 从配置文件中读取其配置信息，默认情况下，该配置文件是 /etc/inetd.conf 。 配置文件的每个字段都必须有一个条目，每个字段的条目由制表符或空格分隔。 注释在行首用 “#” 表示。 每个字段都必须有一个条目。 配置文件的字段如下：

service-name socket-type protocol {wait|nowait}\[/max-child\[/max-connections-per-ip-per-minute\[/max-child-per-ip\]\]\] user\[:group\]\[/login-class\] server-program server-program-arguments 

要指定基于 ONC RPC 的服务，该条目将包含以下字段：

service-name/version socket-type rpc/protocol {wait|nowait}\[/max-child\[/max-connections-per-ip-per-minute\[/max-child-per-ip\]\]\] user\[:group\]\[/login-class\] server-program server-program-arguments 

`inetd` 可以启动两种类型的服务：标准和 TCPMUX。 标准服务有一个众所周知的端口分配给它；它可能是实现官方 Internet 标准的服务，或者是特定于 BSD 的服务。 如 RFC 1078 所述，TCPMUX 服务是非标准服务，没有为其分配众所周知的端口。 当程序连接到 “tcpmux” 知名端口并指定服务名称时，会从 `inetd` 调用它们。 此功能对于添加本地开发的服务器很有用。 TCPMUX 请求仅在启用多路复用器服务本身时才被接受，超出特定的基于 TCPMUX 的服务器；请参阅下面对内部服务的讨论。

_service-name_ 条目是文件 /etc/services 中有效服务的名称，或者是 UNIX 域套接字的规范（见下文）。 对于 “internal” 服务（下面讨论），服务名称应该是服务的正式名称（即 /etc/services 中的第一个条目）。 当用于指定基于 ONC RPC 的服务时，该字段是文件 /etc/rpc 中列出的有效 RPC 服务名称。 “/” 右边的部分是RPC版本号。 这可以只是一个数字参数或一系列版本。 范围由低版本到高版本 - “rusers/1-3” 。 对于 TCPMUX 服务， _service-name_ 字段的值由字符串 “tcpmux” 后跟斜杠和本地选择的服务名称组成。 /etc/services 中列出的服务名称和名称 “help” 是保留的。 尝试为您的 TCPMUX 服务选择唯一的名称，方法是在它们前面加上您的组织名称，并在它们后面加上版本号。

The _socket-type_ 应该是 “stream”, “dgram”, “raw”, “rdm” 或 “seqpacket” 之一，具体取决于套接字是流、数据报、原始、可靠传递的消息还是序列数据包套接字. TCPMUX 服务必须使用 “stream” 。

_protocol_ 必须是有效的协议或 “unix” 。 例如 “tcp” 或 “udp” ，它们都暗示 IPv4 是为了向后兼容。 名称 “tcp4” 和 “udp4” 仅指定 IPv4。 名称 “tcp6” 和 “udp6” 仅指定 IPv6。 名称 “tcp46” 和 “udp46” 指定条目通过通配符 `AF_INET6`-
套接字接受 IPv4 和 IPv6 连接。 基于 Rpc 的服务使用 “rpc/tcp” 或 “rpc/udp” 服务类型指定。 可以使用 4、6 或 46 后缀指定 IPv4 和/或 IPv6，例如 “rpc/tcp6” 或 “rpc/udp46” 。 TCPMUX 服务必须使用 “tcp”, “tcp4”, “tcp6” 或 “tcp46” 。

_wait/nowait_ 条目指定 `inetd` 调用的服务器是否将接管与服务访问点关联的套接字，因此 `inetd` 是否应等待服务器退出后再侦听新的服务请求。 数据报服务器必须使用 “wait” ，因为它们总是使用绑定到指定服务地址的原始数据报套接字来调用。 这些服务器在退出之前必须从套接字读取至少一个数据报。 如果一个数据报服务器连接到它的对等点，释放套接字，以便 `inetd` 可以在套接字上接收更多消息，它被称为 “multi-threaded” 服务器；它应该从套接字读取一个数据报并创建一个连接到对等方的新套接字。 它应该分叉，然后父节点应该退出以允许 `inetd` 检查新服务请求以生成新服务器。 处理套接字上所有传入数据报并最终超时的数据报服务器被称为 “single-threaded” 。 comsat(8) 和 talkd(8) 实用程序是后一种数据报服务器的示例。 tftpd(8) 实用程序是多线程数据报服务器的一个示例。

使用流套接字的服务器通常是多线程的并使用 “nowait” 条目。 这些服务的连接请求被 `inetd` 接受，并且服务器只获得连接到服务客户端的新接受的套接字。 大多数基于流的服务都以这种方式运行。 使用 “wait” 的基于流的服务器以侦听服务套接字启动，并且在退出之前必须接受至少一个连接请求。 这样的服务器通常会接受并处理传入的连接请求，直到超时。 TCPMUX 服务必须使用 “nowait” 。

“nowait” 服务的未完成子进程（或 “threads”) 的最大数量可以通过在 “nowait” 关键字后面附加 “/” 后跟数字来明确指定。 通常（或者如果指定零值）没有最大值。 否则，一旦达到最大值，进一步的连接尝试将排队，直到现有的子进程退出。 这也适用于 “wait” 模式，尽管在某些情况下，非 1（默认值）的值可能没有意义。 您还可以指定给定 IP 地址每分钟的最大连接数，方法是在最大未完成子进程数后附加一个 “/” ，后跟数字。 一旦达到最大值，来自该 IP 地址的进一步连接将被丢弃，直到该分钟结束。 此外，您可以指定从单个 IP 地址同时调用每个服务的最大数量，方法是在未完成子进程的最大数量后面附加一个 “/” ，后跟数字。 一旦达到最大值，来自该 IP 地址的进一步连接将被丢弃。

_user_ 条目应包含运行服务器的用户的用户名。 这允许服务器获得比 root 更少的权限。 由 “:” 分隔的可选 _group_ 部分允许指定此用户的默认组以外的组名。 由 “/” 分隔的可选 _login-class_ 部分允许指定登录类，而不是默认的 “daemon” 登录类。

_server-program_ 条目应该包含程序的路径名，当在其套接字上找到请求时，将由 `inetd` 执行。 如果 `inetd` 在内部提供此服务，则此条目应为 “internal” 。

_server-program-arguments_ 条目列出了要传递给 _server-program_ 的参数，以 argv\[0\] 开头，通常是程序的名称。 如果服务是内部提供的，则服务的 _service-name_ （及其任何参数）或 “internal” 一词应代替此条目。

目前，唯一接受参数的内部服务是 “auth” 。 如果没有选项，服务将始终返回 “ERROR : HIDDEN-USER” 。 该服务改变其行为的可用参数是：

[`-d`](#d_2) fallback

提供 fallback 用户名。 如果启用了真正的 “auth” 服务（使用下面讨论的 `-r` 选项），则在查找套接字凭据或用户名失败时返回此用户名而不是错误。 如果真正的 “auth” 服务被禁用，则为每个请求返回此用户名。 这在 NAT 机器上运行此服务时主要有用。

[`-g`](#g)

不要将用户名返回给身份请求者，而是报告由随机字母数字字符组成的用户名，例如 “c0c993” 。 `-g` 标志不仅覆盖用户名，而且覆盖任何备用名称, .fakeid 或 .noident 文件。

[`-t`](#t) sec\[.usec\]

指定服务的超时时间。 默认超时为 10.0 秒。

[`-r`](#r)

根据 RFC 1413 提供真正的 “auth” 服务。 所有剩余的标志仅适用于这种情况。

[`-i`](#i)

返回数字用户 ID 而不是用户名。

[`-f`](#f)

如果文件 .fakeid-
存在于已识别用户的主目录中，则报告在该文件中找到的用户名而不是真实用户名。 如果在 .fakeid 中找到的用户名是现有用户的用户名，则报告真实用户名。 如果还给出了 `-i` 标志，则 .fakeid 中的用户名会根据现有用户 ID 检查。

[`-F`](#F)

与 `-f` 相同，但没有 .fakeid 中的用户名不能与现有用户匹配的限制。

[`-n`](#n)

如果文件 .noident 存在于已识别用户的主目录中，则返回 “ERROR : HIDDEN-USER” 。 这会覆盖任何可能存在的 fakeid 文件。

[`-o`](#o) osname

使用 osname 代替 uname(3) 报告的系统名称。

`inetd` 实用程序还通过使用自身内部的例程在内部提供了其他几个 “trivial” 的服务。 这些服务是 “echo”, “discard”, “chargen” (字符生成器), “daytime” (人类可读时间)和 “time” （机器可读时间），形式为自 1 月 1 日午夜以来的秒数, 1900)。 所有这些服务都在 TCP 和 UDP 版本中可用；如果请求指定了对应于任何内部服务的回复端口，则 UDP 版本将拒绝服务。 （这样做是为了防御循环攻击；记录远程 IP 地址。） 有关这些服务的详细信息，请参阅相应的 RFC 文档。

TCPMUX 解复用服务也作为内部服务实现。 要使任何基于 TCPMUX 的服务正常运行，必须在 inetd.conf 中包含以下行：

tcpmux stream tcp nowait root internal 

当给定 `-l` 选项时， `inetd` 将在每次接受连接时向 syslog 记录一个条目，记录选择的服务和远程请求者的 IP 号（如果可用）。 除非在配置文件中另有说明，并且在没有 `-W` 和 `-w` 选项的情况下， `inetd` 将登录到 “daemon” 设施。

当 `inetd` 实用程序接收到挂断信号 `SIGHUP` 时，它会重新读取其配置文件。 重新读取配置文件时，可能会添加、删除或修改服务。 除非在调试模式下启动，或使用 `-p` 选项进行其他配置，否则 `inetd` 会将其进程 ID 记录在文件 /var/run/inetd.pid 中以帮助重新配置。

[实施说明](#__u5B9E___u65BD___u8BF4___u660E_)
=========================================

[TCP Wrappers](#TCP_Wrappers)
-----------------------------

当给定 `-w` 选项时， `inetd` 将包装所有指定为 “stream nowait” 或 “dgram” 的服务， “internal” 服务除外。 如果给出了 `-W` 选项，则此类 “internal” 服务将被包装。 如果两个选项都给出，将启用内部和外部服务的包装。 任一包装选项都会导致失败的连接被记录到 “auth” 系统日志工具中。 将 `-l` 标志添加到包装选项将包括成功连接到 “auth” 设施的日志记录。

请注意， `inetd` 仅包装 “wait” 服务的请求，而没有服务器可用于服务请求。 一旦允许与此类服务的连接， `inetd` 就无法控制与该服务的后续连接，直到没有更多服务器监听连接请求。

启用包装时，不需要 tcpd 守护程序，因为该功能是内置的。 有关 TCP Wrappers 的更多信息，请参阅相关文档 (hosts\_access(5)) 。 阅读该文档时，请记住 “internal” 服务没有关联的守护进程名称。 因此， inetd.conf 中指定的服务名称应该用作 “internal” 服务的守护进程名称。

[TCPMUX](#TCPMUX)
-----------------

RFC 1078 描述了 TCPMUX 协议：“一个 TCP 客户端连接到 TCP 端口 1 上的外部主机。 它发送服务名称，后跟回车换行符<CRLF>。 服务名称从不区分大小写。 服务器用一个表示肯定 (+) 或否定 (-) 确认的字符进行回复，紧接着是可选的解释消息，以 <CRLF> 结束。 如果回复是肯定的，则选择的协议开始；否则连接关闭。

如果 TCPMUX 服务名称以 “+” 开头， `inetd` 会为程序返回肯定答复。 这允许您调用使用标准输入/标准输出的程序，而无需在其中放入任何特殊的服务器代码。

特殊的服务名称 “help” 使 `inetd` 列出在 inetd.conf 中启用的 TCPMUX 服务。

[IPsec](#IPsec)
---------------

该实现包括一个小技巧，以支持每个套接字的 IPsec 策略设置。 以 “`#@`” 开头的特殊形式的注释行被解释为策略说明符。 “`#@`” 之后的所有内容都将用作 IPsec 策略字符串，如 ipsec\_set\_policy(3)-
中所述。 每个策略说明符都应用于 inetd.conf 中的所有以下行，直到下一个策略说明符。 空策略说明符会重置 IPsec 策略。

如果 inetd.conf 中出现无效的 IPsec 策略说明符， `inetd` 将通过 syslog(3) 接口提供错误消息并中止执行。

UNIX 域套接字
---------

除了在 IP 套接字上运行服务之外， `inetd` 还可以管理 UNIX 域套接字。 为此，您指定 “unix” _protocol_ 并将 UNIX 域套接字指定为 _service-name_ 。 _service-type_ 可以是 “stream” 或 “dgram” 。 套接字的规范必须是绝对路径名，可选地以所有者和模式为前缀，格式为 _:user:group:mode:_ 。 规格：

`:news:daemon:220:/var/run/sock`

在组 “daemon” 中创建用户 “news” 拥有的套接字，其权限仅允许该用户和组连接。 默认所有者是运行 `inetd` 的用户。 默认模式只允许套接字的所有者进行连接。

**警告**: 在创建 UNIX 域套接字时， `inetd` 必须更改套接字的所有权和权限。 只有在创建套接字的目录只能由 root 写入时，才能安全地完成此操作。 _NOT_ 使用 `inetd` 在世界可写目录（例如 /tmp ）中创建套接字；请改用 /var/run 或类似的目录。

内部服务可以以通常的方式在 UNIX 域套接字上运行。 在这种情况下，内部服务的名称由套接字路径名的最后一个组成部分确定。 例如，指定一个名为 /var/run/chargen 的套接字将在该套接字上接收到连接时调用 “chargen” 服务。

[文件](#__u6587___u4EF6_)
=======================

/etc/inetd.conf

配置文件

/etc/netconfig

网络配置数据库

/etc/rpc

将服务名称翻译成 RPC 程序编号

/etc/services

将服务名称翻译成端口号

/var/run/inetd.pid

当前运行的 `inetd` 的 pid

[实例](#__u5B9E___u4F8B_)
=======================

以下是各种类型服务的几个示例服务条目：

\# 前四个在端口连接时启动相关守护进程 # 由 /etc/services 定义打开。 ftp stream tcp nowait root /usr/libexec/ftpd ftpd -l ntalk dgram udp wait root /usr/libexec/ntalkd ntalkd telnet stream tcp6 nowait root /usr/libexec/telnetd telnetd shell stream tcp46 nowait root /usr/libexec/rshd rshd # 让系统通过 tcpmux 响应日期请求 tcpmux/+date stream tcp nowait guest /bin/date date # 让人们通过 tcpmux 访问系统电话簿 tcpmux/phonebook stream tcp nowait guest /usr/local/bin/phonebook phonebook # 使内核统计信息可访问 rstatd/1-3 dgram rpc/udp wait root /usr/libexec/rpc.rstatd rpc.rstatd # 使用 netcat 作为 nc 的一次性 HTTP 代理（来自 freebsd-tips fortune） http stream tcp nowait nobody /usr/bin/nc nc -N dest-ip 80 # 在 /var/run/echo 设置一个 unix 套接字，它会回显写入的任何内容。 /var/run/echo stream unix nowait root internal # 为 IPsec 身份验证标头运行 chargen #@ ipsec ah/require chargen stream tcp nowait root internal #@ 

[错误信息](#__u9519___u8BEF___u4FE1___u606F_)
=========================================

`inetd` 服务器使用 syslog(3) 记录错误消息。 重要的错误消息及其解释是：

service/protocol server failing (looping), service terminated.

过去一分钟内对指定服务的请求数超过限制。 存在限制是为了防止损坏的程序或恶意用户淹没系统。 出现此消息的原因可能有多种：

1.  短时间内有很多主机请求服务。
2.  损坏的客户端程序过于频繁地请求服务。
3.  恶意用户正在运行程序以在拒绝服务攻击中调用服务。
4.  调用的服务程序有一个错误导致客户端快速重试。

如上所述，使用 `-R` rate 选项更改速率限制。 一旦达到限制，服务将在 10 分钟内自动重新启用。

service/protocol: No such user user, service ignored

service/protocol: getpwnam: user: No such user

passwd(5) 数据库中不存在 user 条目。 当 `inetd` （重新）读取配置文件时，会出现第一条消息。 第二条消息在调用服务时出现。

service: can't set uid uid

service: can't set gid gid

条目的 user 字段的用户或组 ID 无效。

setsockopt(SO\_PRIVSTATE): Operation not supported

`inetd` 实用程序试图放弃与套接字关联的特权状态，但无法放弃。

unknown rpc/udp 或 rpc/tcp

在 netconfig(5) 数据库中没有找到 udp 或 tcp 的条目。

unknown rpc/udp6 or rpc/tcp6

在 netconfig(5) 数据库中没有找到 udp6 或 tcp6 的条目。

[参见](#__u53C2___u89C1_)
=======================

nc(1), ipsec\_set\_policy(3), hosts\_access(5), hosts\_options(5), login.conf(5), netconfig(5), passwd(5), rpc(5), services(5), comsat(8), fingerd(8), ftpd(8), rlogind(8), rpcbind(8), rshd(8), talkd(8), telnetd(8), tftpd(8) Michael C. St. Johns, Identification Protocol, RFC1413.

[历史](#__u5386___u53F2_)
=======================

`inetd` 实用程序出现在 4.3BSD 中。 TCPMUX 基于 Mark Lottor 的代码和文档。 对基于 ONC RPC 的服务的支持模仿了 SunOS 提供的服务。 IPsec hack 由 KAME 项目于 1999 年贡献。 FreeBSD TCP Wrappers 支持首次出现在 FreeBSD 3.2 中。

May 14, 2020

FreeBSD 13.1-RELEASE