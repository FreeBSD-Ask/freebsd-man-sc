  SOCKSTAT(1)  

SOCKSTAT(1)

FreeBSD General Commands Manual

SOCKSTAT(1)

[名称](#__u540D___u79F0_)
=======================

`sockstat` —

列出打开的套接字

[概要](#__u6982___u8981_)
=======================

`sockstat` \[`-46CcLlnSsUuvw`\] \[`-j` jid\] \[`-p` ports\] \[`-P` protocols\]

[描述](#__u63CF___u8FF0_)
=======================

`sockstat` 命令列出打开的 Internet 或 UNIX 套接字。

可以使用以下选项：

[`-4`](#4)

显示 `AF_INET` (IPv4) 套接字。

[`-6`](#6)

显示 `AF_INET6` (IPv6) 套接字。

[`-C`](#C)

显示拥塞控制模块（如果适用）。 这目前仅针对 TCP 实现。

[`-c`](#c)

显示连接的套接字。

[`-j`](#j) jail

仅显示属于指定监狱 ID 或名称的套接字。

[`-L`](#L)

仅当本地和外部地址不在环回网络前缀 `127.0.0.0/8` 中或不包含 IPv6 环回地址 `::1` 时才显示 Internet 套接字。

[`-l`](#l)

显示监听套接字。

[`-n`](#n)

不要将数字 UID 解析为用户名。

[`-p`](#p) ports

仅当本地或外部端口号在指定列表中时才显示 Internet 套接字。 ports 参数是以逗号分隔的端口号和范围列表，指定为第一个和最后一个端口，用破折号分隔。

[`-P`](#P) protocols

仅显示指定 protocols 的套接字。 protocols 参数是一个逗号分隔的协议名称列表，它们在 protocols(5) 中定义。

[`-q`](#q)

安静模式，不打印标题行。

[`-S`](#S)

显示协议栈（如果适用）。 这目前仅针对 TCP 实现。

[`-s`](#s)

显示协议状态（如果适用）。 这目前仅针对 SCTP 和 TCP 实现。

[`-U`](#U)

显示远程 UDP 封装端口号（如果适用）。 这目前仅适用于 SCTP。

[`-u`](#u)

显示 `AF_LOCAL` (UNIX) 套接字。

[`-v`](#v)

详细模式。

[`-w`](#w)

使用更宽的字段大小来显示地址。

如果未指定 `-4`, `-6` 或 `-u` , `sockstat` 将列出所有三个域中的套接字。

如果 `-c` 或 `-l` 都没有指定， `sockstat` 将列出监听和连接的套接字。

为每个套接字列出的信息是：

[`USER`](#USER)

拥有套接字的用户。

[`COMMAND`](#COMMAND)

持有套接字的命令。

[`PID`](#PID)

持有套接字的命令的进程 ID。

[`FD`](#FD)

套接字的文件描述符编号。

[`PROTO`](#PROTO)

与 Internet 套接字的套接字关联的传输协议，或 UNIX 套接字的套接字类型 (stream, datagram, or seqpacket) 。

[`LOCAL ADDRESS`](#LOCAL_ADDRESS)

对于 Internet 套接字，这是套接字本地端绑定到的地址（请参阅 getsockname(2) ）。 对于绑定的 UNIX 套接字，它是套接字的文件名。 对于其他 UNIX 套接字，它是一个右箭头，后跟端点的文件名，或 “`??`” 如果无法确定终点。

[`FOREIGN ADDRESS`](#FOREIGN_ADDRESS)

（仅限 Internet 套接字）套接字的外部端绑定到的地址（请参阅 getpeername(2) )。

[`ENCAPS`](#ENCAPS)

如果指定了 `-U` ，则为远程 UDP 封装端口号（仅适用于 SCTP）。

[`PATH STATE`](#PATH_STATE)

指定了 `-s` 时的路径状态（仅适用于 SCTP）。

[`CONN STATE`](#CONN_STATE)

如果指定了 `-s` ，则连接状态（仅适用于 SCTP 或 TCP）。

[`STACK`](#STACK)

如果指定了 `-S` ，则为协议栈（仅适用于 TCP）。

[`CC`](#CC)

如果指定了 `-C` ，则拥塞控制（仅适用于 TCP）。

如果一个套接字与多个文件描述符相关联，则会多次显示。 如果套接字不与任何文件描述符相关联，则前四列没有意义。

[实例](#__u5B9E___u4F8B_)
=======================

显示使用 TCP 协议在端口 22 上侦听的 IPv4 套接字的信息：

$ sockstat -4 -l -P tcp -p 22 

显示使用 TCP 或 UDP 的套接字的信息，如果本地地址和外部地址都不在环回网络中：

$ sockstat -L -P tcp,udp 

显示正在侦听和连接的 TCP IPv6 套接字（默认）：

$ sockstat -6 -P tcp 

[参见](#__u53C2___u89C1_)
=======================

fstat(1), netstat(1), procstat(1), inet(4), inet6(4), protocols(5)

[历史](#__u5386___u53F2_)
=======================

`sockstat` 命令出现在 FreeBSD 3.1 中。

[作者](#__u4F5C___u8005_)
=======================

`sockstat` 命令和本手册页由 Dag-Erling Smørgrav <[des@FreeBSD.org](mailto:des@FreeBSD.org)\> 编写。

December 30, 2020

FreeBSD 13.1-RELEASE