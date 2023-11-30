  NC(1)  

NC(1)

FreeBSD General Commands Manual

NC(1)

[名称](#__u540D___u79F0_)
=======================

`nc` —

任意 TCP 和 UDP 连接和监听

[概要](#__u6982___u8981_)
=======================

`nc` \[`-46DdEFhklMNnrStUuvz`\] \[`-e` IPsec\_policy\] \[`-I` length\] \[`-i` interval\] \[`--no-tcpopt`\] \[`--sctp`\] \[`-O` length\] \[`-P` proxy\_username\] \[`-p` source\_port\] \[`-s` source\] \[`-T` toskeyword\] \[`-V` rtable\] \[`-w` timeout\] \[`-X` proxy\_protocol\] \[`-x` proxy\_address\[:port\]\] \[destination\] \[port\]

[描述](#__u63CF___u8FF0_)
=======================

`nc` (或 `netcat`) 实用程序几乎用于任何涉及 TCP、UDP 或 UNIX\-domain 套接字的事情。 它可以打开 TCP 连接、发送 UDP 数据包、侦听任意 TCP 和 UDP 端口、进行端口扫描以及处理 IPv4 和 IPv6。 与 telnet(1) 不同 `nc` 可以很好地编写脚本，并将错误消息分离到标准错误中，而不是像 telnet(1) 那样将它们发送到标准输出。

常见用途包括：

*   简单的 TCP 代理
*   基于 shell 脚本的 HTTP 客户端和服务器
*   网络守护进程测试
*   用于 ssh(1) 的 SOCKS 或 HTTP ProxyCommand
*   还有很多很多

选项如下：

[`-4`](#4)

强制 `nc` 仅使用 IPv4 地址。

[`-6`](#6)

强制 `nc` 仅使用 IPv6 地址。

[`-D`](#D)

在套接字上启用调试。

[`-d`](#d)

不要尝试从标准输入读取。

[`-E`](#E)

“`-e 'in ipsec esp/transport//require'` `-e 'out ipsec esp/transport//require'`” 的快捷方式，可在两个方向启用 IPsec ESP 传输模式。

[`-e`](#e)

如果 IPsec 支持可用，则可以使用 ipsec\_set\_policy(3) 中描述的语法指定要使用的 IPsec 策略。 该标志最多可以指定两次，因为通常每个方向都需要一个策略。

[`-F`](#F)

使用 sendmsg(2) 将第一个连接的套接字传递到标准输出并退出。 这与 `-X` 一起使用非常有用，可以让 `nc` 使用代理执行连接设置，然后将其余连接留给另一个程序（例如，使用 ssh\_config(5) `ProxyUseFdpass` 选项的 ssh(1) )。

[`-h`](#h)

打印出 `nc` 帮助。

[`-I`](#I) length

指定 TCP 接收缓冲区的大小。

[`-i`](#i) interval

指定发送和接收的文本行之间的延迟时间间隔。 还会导致连接到多个端口之间的延迟时间。

[`-k`](#k)

强制 `nc` 在其当前连接完成后继续侦听另一个连接。 在没有 `-l` 选项的情况下使用此选项是错误的。 与 `-u` 选项一起使用时，服务器套接字不连接，它可以接收来自多个主机的 UDP 数据报。

[`-l`](#l)

用于指定 `nc` 应侦听传入连接而不是启动与远程主机的连接。 将此选项与 `-p`, `-s` 或 `-z` 选项结合使用是错误的。 此外，使用 `-w` 选项指定的任何超时都将被忽略。

[`-M`](#M)

使用 stats(3) 框架收集每个连接的 TCP 统计信息，并在连接关闭后以 JSON 格式将它们打印到 stderr(4) 。

[`-N`](#N)

shutdown(2) 输入 EOF 后的网络套接字。 一些服务器需要这个来完成他们的工作。

[`-n`](#n)

不要对任何指定的地址、主机名或端口进行任何 DNS 或服务查找。

[`--no-tcpopt`](#-no-tcpopt)

通过设置布尔 TCP\_NOOPT 套接字选项来禁用套接字上的 TCP 选项。

[`--sctp`](#-sctp)

使用 SCTP 代替 TCP 的默认选项。

[`-O`](#O) length

指定 TCP 发送缓冲区的大小。

[`-P`](#P) proxy\_username

指定要呈现给需要身份验证的代理服务器的用户名。 如果未指定用户名，则不会尝试身份验证。 目前仅 HTTP CONNECT 代理支持代理身份验证。

[`-p`](#p) source\_port

指定 `nc` 应使用的源端口，受权限限制和可用性限制。 将此选项与 `-l` 选项结合使用是错误的。

[`-r`](#r)

指定应随机选择源和/或目标端口，而不是在一个范围内或按系统分配它们的顺序顺序选择。

[`-S`](#S)

启用 RFC 2385 TCP MD5 签名选项。

[`-s`](#s) source

指定用于发送数据包的接口的 IP。 对于 UNIX\-domain 域数据报套接字，指定要创建和使用的本地临时套接字文件，以便可以接收数据报。 将此选项与 `-l` 选项结合使用是错误的。

[`-T`](#T) toskeyword

更改 IPv4 TOS 值。 toskeyword 可以是 critical, inetcontrol, lowdelay, netcontrol, throughput, reliability, 或 DiffServ 代码点之一: ef, af11 ... af43, cs0 ... cs7; 或十六进制或十进制的数字。

[`-t`](#t)

导致 `nc` 向 RFC 854 DO 和 WILL 请求发送 RFC 854 DON'T 和 WON'T 响应。 这使得使用 `nc` 编写 telnet 会话脚本成为可能。

[`-U`](#U)

指定使用 UNIX\-domain 套接字。

[`-u`](#u)

使用 UDP 而不是 TCP 的默认选项。 对于 UNIX\-domain 套接字，使用数据报套接字而不是流套接字。 如果使用 UNIX\-domain 套接字，则在 /tmp 中创建一个临时接收套接字，除非给出 `-s` 标志。

[`-V`](#V) rtable

设置要使用的路由表 (“FIB”) 。

[`-v`](#v)

让 `nc` 给出更详细的输出。

[`-w`](#w) timeout

timeout 秒后无法建立或空闲超时的连接。 `-w` 标志对 `-l` 选项没有影响，即 `nc` 将永远监听连接，无论有无 `-w` 标志。默认为无超时。

[`-X`](#X) proxy\_protocol

请求 `nc` 在与代理服务器通信时应使用指定的协议。 支持的协议是 “4” (SOCKS v.4), “5” (SOCKS v.5) 和 “connect” (HTTPS 代理)。 如果未指定协议，则使用 SOCKS 版本 5。

[`-x`](#x) proxy\_address\[:port\]

请求 `nc` 应使用 proxy\_address 和 port 处的代理连接到 destination 。 如果未指定 port ，则使用代理协议的知名端口（SOCKS 为 1080，HTTPS 为 3128）。

[`-z`](#z)

指定 `nc` 应该只扫描监听守护进程，而不向它们发送任何数据。 将此选项与 `-l` 选项结合使用是错误的。

destination 可以是数字 IP 地址或符号主机名（除非给出 `-n` 选项）。 通常，必须指定目的地，除非给出 `-l` 选项（在这种情况下使用本地主机）。 对于 UNIX\-domain 套接字，目标是必需的，并且是要连接到的套接字路径（或者如果给出 `-l` 选项则侦听）。

port 可以是单个整数或端口范围。范围的格式为 nn-mm。 通常，必须指定目标端口，除非给出 `-U` 选项。

[客户端/服务器模型](#__u5BA2___u6237___u7AEF_/__u670D___u52A1___u5668___u6A21___u578B_)
===============================================================================

使用 `nc` 构建一个非常基本的客户端/服务器模型非常简单。 在一个控制台上，启动 `nc` 在特定端口上侦听连接。 例如：

`$ nc -l 1234`

`nc` 现在正在端口 1234 上侦听连接。 在第二个控制台 (或第二台机器) 上，连接到正在监听的机器和端口：

`$ nc 127.0.0.1 1234`

现在应该在端口之间建立连接。 在第二个控制台输入的任何内容都将连接到第一个控制台，反之亦然。 建立连接后， `nc` 并不真正关心哪一侧被用作 ‘server’ 以及哪一侧被用作 ‘client’ 。 可以使用 `EOF` (‘^D’) 终止连接。

[数据传输](#__u6570___u636E___u4F20___u8F93_)
=========================================

可以扩展上一节中的示例以构建基本的数据传输模型。 输入到连接一端的任何信息都将输出到另一端，并且可以轻松捕获输入和输出以模拟文件传输。

首先使用 `nc` 侦听特定端口，并将输出捕获到文件中：

`$ nc -l 1234 > filename.out`

使用第二台机器，连接到正在监听的 `nc` 进程，将要传输的文件提供给它：

`$ nc -N host.example.com 1234 < filename.in`

传输文件后，连接将自动关闭。

[与服务器交谈](#__u4E0E___u670D___u52A1___u5668___u4EA4___u8C08_)
===========================================================

有时 “by hand” 而不是通过用户界面与服务器交谈是有用的。 当可能需要验证服务器响应客户端发出的命令而发送的数据时，它可以帮助进行故障排除。 例如，要检索网站的主页：

$ printf "GET / HTTP/1.0\\r\\n\\r\\n" | nc host.example.com 80 

请注意，这还会显示 Web 服务器发送的标头。 如有必要，可以使用 sed(1) 等工具过滤它们。

当用户知道服务器所需的请求格式时，可以构建更复杂的示例。 作为另一个示例，可以使用以下方式将电子邮件提交到 SMTP 服务器：

$ nc localhost 25 << EOF HELO host.example.com MAIL FROM:<user@host.example.com> RCPT TO:<user2@host.example.com> DATA Body of email. . QUIT EOF 

[端口扫描](#__u7AEF___u53E3___u626B___u63CF_)
=========================================

了解目标机器上哪些端口已打开并正在运行服务可能很有用。 `-z` 标志可用于告诉 `nc` 报告打开的端口，而不是启动连接。 例如：

$ nc -z host.example.com 20-30 Connection to host.example.com 22 port \[tcp/ssh\] succeeded! Connection to host.example.com 25 port \[tcp/smtp\] succeeded! 

指定端口范围以将搜索限制为端口 20 - 30。

或者，了解哪些服务器软件正在运行以及哪些版本可能会很有用。 此信息通常包含在问候横幅中。 为了检索这些，必须首先建立连接，然后在检索到横幅后断开连接。 这可以通过使用 `-w` 标志指定一个小的超时来完成，或者通过向服务器发出 “`QUIT`” 命令来完成：

$ echo "QUIT" | nc host.example.com 20-30 SSH-1.99-OpenSSH\_3.6.1p2 Protocol mismatch. 220 host.example.com IMS SMTP Receiver Version 0.84 Ready 

[实例](#__u5B9E___u4F8B_)
=======================

打开到 host.example.com 的 42 端口的 TCP 连接，使用端口 31337 作为源端口，超时 5 秒：

`$ nc -p 31337 -w 5 host.example.com 42`

打开与 host.example.com 的 53 端口的 UDP 连接：

`$ nc -u host.example.com 53`

使用 10.1.2.3 作为连接本地端的 IP，打开与 host.example.com 的端口 42 的 TCP 连接：

`$ nc -s 10.1.2.3 host.example.com 42`

使用 IPsec ESP 打开与 host.example.com 的端口 42 的 TCP 连接，用于传入和传出流量。

`$ nc -E host.example.com 42`

使用 IPsec ESP 打开与 host.example.com 端口 42 的 TCP 连接，仅用于传出流量。

`$ nc -e 'out ipsec esp/transport//require' host.example.com 42`

创建并侦听 UNIX\-domain 流套接字：

`$ nc -lU /var/tmp/dsocket`

通过位于 10.2.3.4 的 HTTP 代理，端口 8080 连接到 host.example.com 的端口 42。 这个例子也可以被 ssh(1) 使用；有关更多信息，请参阅 ssh\_config(5) 中的 `ProxyCommand` 指令。

`$ nc -x10.2.3.4:8080 -Xconnect host.example.com 42`

再次使用相同的示例，如果代理需要，这次使用用户名 “ruser” 启用代理身份验证：

`$ nc -x10.2.3.4:8080 -Xconnect -Pruser host.example.com 42`

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `nc` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

cat(1), setfib(1), ssh(1), tcp(4)

[作者](#__u4F5C___u8005_)
=======================

原始实现由 \*Hobbit\* <[hobbit@avian.org](mailto:hobbit@avian.org)\> 。-
由 Eric Jackson <[ericj@monkey.org](mailto:ericj@monkey.org)\> 重写，支持 IPv6。

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

无论目标机器的状态如何，使用 `-uz` 标志组合的 UDP 端口扫描将始终报告成功。 但是，结合目标机器或中间设备上的流量嗅探器， `-uz` 组合可能对通信诊断有用。 请注意，生成的 UDP 流量可能会受到硬件资源和/或配置设置的限制。

July 10, 2020

FreeBSD 13.1-RELEASE