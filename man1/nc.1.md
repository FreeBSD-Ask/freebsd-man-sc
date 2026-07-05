# nc.1

`nc` — 任意 TCP 和 UDP 连接与监听

## 名称

`nc`

## 概要

`nc [-46DdEFhklMNnrStUuvz] [-e IPsec_policy] [-I length] [-i interval] [--lb] [--no-tcpopt] [--sctp] [--crlf] [-O length] [-P proxy_username] [-p source_port] [-s source] [-T toskeyword] [--tun tundev] [-V rtable] [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]] [destination] [port]`

## 描述

`nc`（或 `netcat`）实用程序可用于涉及 TCP、UDP 或 UNIX 域套接字的几乎任何操作。它可以打开 TCP 连接、发送 UDP 数据包、监听任意 TCP 和 UDP 端口、进行端口扫描，并处理 IPv4 和 IPv6。与 [telnet(1)](telnet.1.md) 不同，`nc` 便于编写脚本，并将错误消息分离到标准错误而非像 [telnet(1)](telnet.1.md) 那样将部分错误发送到标准输出。

常见用途包括：

- 简单的 TCP 代理
- 基于 shell 脚本的 HTTP 客户端和服务器
- 网络守护进程测试
- [ssh(1)](ssh.1.md) 的 SOCKS 或 HTTP ProxyCommand
- 以及更多

选项如下：

**`-4`** 强制 `nc` 仅使用 IPv4 地址。

**`-6`** 强制 `nc` 仅使用 IPv6 地址。

**`--crlf`** 通过网络发送数据时将 LF 转换为 CRLF。

**`-D`** 在套接字上启用调试。

**`-d`** 不尝试从标准输入读取。

**`-E`** 等同于 “`-e 'in ipsec esp/transport//require'` `-e 'out ipsec esp/transport//require'`” 的快捷方式，在两个方向上启用 IPsec ESP 传输模式。

**`-e`** 如果支持 IPsec，则可使用 [ipsec_set_policy(3)](../man3/ipsec_set_policy.3.md) 中描述的语法指定要使用的 IPsec 策略。此标志最多可指定两次，因为通常每个方向需要一个策略。

**`-F`** 使用 [sendmsg(2)](../man2/sendmsg.2.md) 将第一个已连接的套接字传递到标准输出并退出。这与 `-X` 结合使用时很有用，可让 `nc` 通过代理执行连接建立，然后将连接的其余部分留给另一个程序（例如 [ssh(1)](ssh.1.md) 使用 [ssh_config(5)](../man5/ssh_config.5.md) 的 `ProxyUseFdpass` 选项）。

**`-h`** 打印 `nc` 帮助。

**`-I`** `length` 指定 TCP 接收缓冲区的大小。

**`-i`** `interval` 指定发送和接收文本行之间的延迟时间间隔。也导致到多个端口的连接之间的延迟。

**`-k`** 强制 `nc` 在当前连接完成后继续监听另一个连接。不使用 `-l` 选项时使用此选项是错误的。与 `-u` 选项一起使用时，服务器套接字未连接，可接收来自多个主机的 UDP 数据报。

**`-l`** 用于指定 `nc` 应监听传入连接而非启动到远程主机的连接。将此选项与 `-p`、`-s` 或 `-z` 选项一起使用是错误的。此外，使用 `-w` 选项指定的任何超时都被忽略。

**`--lb`** 使用 `-l` 时，将套接字置于负载均衡模式。在此模式下，多个套接字可绑定到相同的地址和端口，传入连接在它们之间分配。

**`-M`** 使用 [stats(3)](../man3/stats.3.md) 框架收集每连接 TCP 统计信息，并在连接关闭后以 JSON 格式打印到 [stderr(4)](../man4/stderr.4.md)。

**`-N`** 在输入上的 EOF 之后对网络套接字执行 [shutdown(2)](../man2/shutdown.2.md)。某些服务器需要此操作来完成其工作。

**`-n`** 不对任何指定的地址、主机名或端口进行 DNS 或服务查找。

**`--no-tcpopt`** 通过设置布尔值 TCP_NOOPT 套接字选项，禁用套接字上 TCP 选项的使用。

**`--sctp`** 使用 SCTP 而非默认的 TCP。

**`-O`** `length` 指定 TCP 发送缓冲区的大小。

**`-P`** `proxy_username` 指定要向需要身份验证的代理服务器提供的用户名。如果未指定用户名，则不尝试身份验证。目前仅 HTTP CONNECT 代理支持代理身份验证。

**`-p`** `source_port` 指定 `nc` 应使用的源端口，受权限限制和可用性约束。将此选项与 `-l` 选项一起使用是错误的。

**`-r`** 指定源和/或目标端口应随机选择，而非在范围内按顺序或系统分配的顺序选择。

**`-S`** 启用 RFC 2385 TCP MD5 签名选项。

**`-s`** `source` 指定用于发送数据包的接口 IP。对于 UNIX 域数据报套接字，指定要创建和使用的本地临时套接字文件，以便接收数据报。将此选项与 `-l` 选项一起使用是错误的。

**`-T`** `toskeyword` 更改 IPv4 TOS 值。`toskeyword` 可以是 `critical`、`inetcontrol`、`lowdelay`、`netcontrol`、`throughput`、`reliability` 之一，或 DiffServ 代码点之一：`ef`、`af11 ... af43`、`cs0 ... cs7`；或以十六进制或十进制表示的数字。

**`-t`** 使 `nc` 对 RFC 854 DO 和 WILL 请求发送 RFC 854 DON'T 和 WON'T 响应。这使得使用 `nc` 编写 telnet 会话脚本成为可能。

**`--tun`** `tundev` 使 `nc` 使用提供的 [tun(4)](../man4/tun.4.md) 进行输入和输出，而非默认的标准输入和标准输出。

**`-U`** 指定使用 UNIX 域套接字。

**`-u`** 使用 UDP 而非默认的 TCP。对于 UNIX 域套接字，使用数据报套接字而非流套接字。如果使用 UNIX 域套接字，将在 **/tmp** 中创建临时接收套接字，除非给出了 `-s` 标志。

**`-V`** `rtable` 设置要使用的路由表（“FIB”）。

**`-v`** 使 `nc` 提供更详细的输出。

**`-w`** `timeout` 无法建立或空闲的连接在 `timeout` 秒后超时。`-w` 标志对 `-l` 选项无效，即无论是否有 `-w` 标志，`nc` 都将永远监听连接。默认为无超时。

**`-X`** `proxy_protocol` 请求 `nc` 在与代理服务器通信时使用指定的协议。支持的协议有 “4”（SOCKS v.4）、“5”（SOCKS v.5）和 “connect”（HTTPS 代理）。如果未指定协议，则使用 SOCKS 版本 5。

**`-x`** `proxy_address`[:`port`] 请求 `nc` 使用位于 `proxy_address` 和 `port` 的代理连接到 `destination`。如果未指定 `port`，则使用代理协议的知名端口（SOCKS 为 1080，HTTPS 为 3128）。

**`-z`** 指定 `nc` 应仅扫描监听守护进程，不向它们发送任何数据。将此选项与 `-l` 选项一起使用是错误的。

`destination` 可以是数字 IP 地址或符号主机名（除非给出了 `-n` 选项）。通常必须指定目标，除非给出了 `-l` 选项（此种情况下使用本地主机）。对于 UNIX 域套接字，必须指定目标，它是要连接到的套接字路径（如果给出了 `-l` 选项，则是要监听的套接字路径）。

`port` 可以指定为数字端口号或服务名。端口可以以 nn-mm 形式的范围指定。通常必须指定目标端口，除非给出了 `-U` 选项。

## 客户端/服务器模型

使用 `nc` 构建非常基本的客户端/服务器模型非常简单。在一个控制台上，启动 `nc` 在特定端口上监听连接。例如：

```sh
$ nc -l 1234
```

`nc` 现在正在端口 1234 上监听连接。在第二个控制台（或第二台机器）上，连接到正在监听的机器和端口：

```sh
$ nc 127.0.0.1 1234
```

现在两个端口之间应该有连接。在第二个控制台上输入的任何内容都将连接到第一个，反之亦然。连接建立后，`nc` 并不真正关心哪一侧用作 “服务器”，哪一侧用作 “客户端”。可使用 `EOF`（‘`^D`’）终止连接。

## 数据传输

上一节的示例可以扩展为构建基本的数据传输模型。输入连接一端的任何信息都将输出到另一端，输入和输出可以轻松捕获以模拟文件传输。

首先使用 `nc` 在特定端口上监听，将输出捕获到文件：

```sh
$ nc -l 1234 > filename.out
```

使用第二台机器，连接到正在监听的 `nc` 进程，向其提供要传输的文件：

```sh
$ nc -N host.example.com 1234 < filename.in
```

文件传输完成后，连接将自动关闭。

## 与服务器通信

有时 “手动” 与服务器通信而非通过用户界面很有用。它可以帮助故障排除，当可能需要验证服务器在响应客户端发出的命令时发送了什么数据时。例如，要检索网站的主页：

```sh
$ printf "GET / HTTP/1.0\r\n\r\n" | nc host.example.com 80
```

注意，这也会显示 Web 服务器发送的标头。如有必要，可使用 [sed(1)](sed.1.md) 等工具过滤它们。

当用户知道服务器所需的请求格式时，可以构建更复杂的示例。作为另一个示例，可使用以下方式向 SMTP 服务器提交电子邮件：

```sh
$ nc localhost 25 << EOF
HELO host.example.com
MAIL FROM:<user@host.example.com>
RCPT TO:<user2@host.example.com>
DATA
Body of email.
.
QUIT
EOF
```

## 端口扫描

了解目标机器上哪些端口开放并运行服务可能很有用。`-z` 标志可用于告诉 `nc` 报告开放端口，而非启动连接。例如：

```sh
$ nc -z host.example.com 20-30
Connection to host.example.com 22 port [tcp/ssh] succeeded!
Connection to host.example.com 25 port [tcp/smtp] succeeded!
```

端口范围指定为将搜索限制在端口 20-30。

或者，了解正在运行哪些服务器软件及哪些版本可能很有用。此信息通常包含在问候横幅中。要检索这些信息，需要先建立连接，然后在检索到横幅后断开连接。这可以通过使用 `-w` 标志指定较小的超时来完成，或者可能通过向服务器发出 `QUIT` 命令：

```sh
$ echo "QUIT" | nc host.example.com 20-30
SSH-1.99-OpenSSH_3.6.1p2
Protocol mismatch.
220 host.example.com IMS SMTP Receiver Version 0.84 Ready
```

## 实例

使用端口 31337 作为源端口，打开到 host.example.com 端口 42 的 TCP 连接，超时为 5 秒：

```sh
$ nc -p 31337 -w 5 host.example.com 42
```

打开到 host.example.com 端口 53 的 UDP 连接：

```sh
$ nc -u host.example.com 53
```

使用 10.1.2.3 作为连接本地端的 IP，打开到 host.example.com 端口 42 的 TCP 连接：

```sh
$ nc -s 10.1.2.3 host.example.com 42
```

对传入和传出流量使用 IPsec ESP，打开到 host.example.com 端口 42 的 TCP 连接：

```sh
$ nc -E host.example.com 42
```

仅对传出流量使用 IPsec ESP，打开到 host.example.com 端口 42 的 TCP 连接：

```sh
$ nc -e 'out ipsec esp/transport//require' host.example.com 42
```

创建并监听 UNIX 域流套接字：

```sh
$ nc -lU /var/tmp/dsocket
```

通过位于 10.2.3.4 端口 8080 的 HTTP 代理连接到 host.example.com 的端口 42。此示例也可由 [ssh(1)](ssh.1.md) 使用；更多信息参见 [ssh_config(5)](../man5/ssh_config.5.md) 中的 `ProxyCommand` 指令。

```sh
$ nc -x10.2.3.4:8080 -Xconnect host.example.com 42
```

同样的示例，这次如果代理需要，使用用户名 “ruser” 启用代理身份验证：

```sh
$ nc -x10.2.3.4:8080 -Xconnect -Pruser host.example.com 42
```

## 退出状态

`nc` 实用程序成功时退出值为 0，发生错误时大于 0。

## 参见

[cat(1)](cat.1.md), [setfib(1)](setfib.1.md), [ssh(1)](ssh.1.md), [tcp(4)](../man4/tcp.4.md)

## 作者

原始实现由 *Hobbit* <hobbit@avian.org> 完成。

由 Eric Jackson <ericj@monkey.org> 重写并添加 IPv6 支持。

## 注意事项

使用 `-uz` 标志组合的 UDP 端口扫描将始终报告成功，无论目标机器的状态如何。但是，结合目标机器或中间设备上的流量嗅探器，`-uz` 组合可用于通信诊断。注意，生成的 UDP 流量可能因硬件资源和/或配置设置而受限。
