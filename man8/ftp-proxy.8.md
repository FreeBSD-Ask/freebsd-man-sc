  FTP-PROXY(8)  

FTP-PROXY(8)

FreeBSD System Manager's Manual

FTP-PROXY(8)

[名称](#__u540D___u79F0_)
=======================

`ftp-proxy` —

Internet 文件传输协议代理守护进程

[概要](#__u6982___u8981_)
=======================

`ftp-proxy` \[`-6Adrv`\] \[`-a` address\] \[`-b` address\] \[`-D` level\] \[`-m` maxsessions\] \[`-P` port\] \[`-p` port\] \[`-q` queue\] \[`-R` address\] \[`-T` tag\] \[`-t` timeout\]

[描述](#__u63CF___u8FF0_)
=======================

`ftp-proxy` 是 Internet 文件传输协议的代理。 应该使用 pf(4) rdr 命令将 FTP 控制连接重定向到代理，之后代理会代表客户端连接到服务器。

代理允许数据连接通过、重写和重定向它们，以便使用正确的地址。 从客户端到服务器的所有连接都重写了它们的源地址，因此它们似乎来自代理。 因此，从服务器到代理的所有连接都重写了它们的目标地址，因此它们被重定向到客户端。 代理为此使 pf(4) anchor 功能。

假设FTP控制连接是从$client 到 $server，proxy 使用$proxy 源地址连接到server，$port 是协商好的，那么 `ftp-proxy` 在各个anchor上添加如下规则。 （这些示例规则使用 inet，但代理也支持 inet6。）

在活动模式（PORT 或 EPRT）的情况下：

rdr from $server to $proxy port $port -> $client pass quick inet proto tcp \\ from $server to $client port $port 

在被动模式（PASV 或 EPSV）的情况下：

nat from $client to $server port $port -> $proxy pass in quick inet proto tcp \\ from $client to $server port $port pass out quick inet proto tcp \\ from $proxy to $server port $port 

选项如下：

[`-6`](#6)

IPv6 模式。 代理将期望并使用 IPv6 地址进行所有通信。 IPv6 仅允许扩展 FTP 模式 EPSV 和 EPRT。 默认情况下，代理处于 IPv4 模式。

[`-A`](#A)

只允许匿名 FTP 连接。 允许用户 "ftp" 或用户 "anonymous" 。

[`-a`](#a) address

代理将使用它作为与服务器的控制连接的源地址。

[`-b`](#b) address

代理将侦听重定向控制连接的地址。 默认值为 127.0.0.1，或在 IPv6 模式下为 ::1。

[`-D`](#D) level

调试级别，范围从 0 到 7。 越高越详细。 默认值为 5。 （这些级别对应于 syslog(3) 级别。）

[`-d`](#d)

不要守护进程。 该进程将停留在前台，记录到标准错误。

[`-m`](#m) maxsessions

最大并发 FTP 会话数。 当代理达到此限制时，将拒绝新连接。 默认值为 100 个会话。 限制可以降低到最小值 1，或提高到最大值 500。

[`-P`](#P) port

固定服务器端口。 仅与 `-R` 结合使用。默认为端口 21。

[`-p`](#p) port

代理将侦听重定向连接的端口。 默认为端口 8021。

[`-q`](#q) queue

创建附加队列 queue 的规则，以便可以对数据连接进行排队。

[`-R`](#R) address

固定服务器地址，也称为反向模式。 代理将始终连接到同一个服务器，无论客户端想要连接到哪里（在它被重定向之前）。 使用此选项代理 NAT 后面的服务器，或将所有连接转发到另一个代理。

[`-r`](#r)

在主动模式下将 sourceport 重写为 20，以适应坚持此 RFC 属性的古老客户端。

[`-T`](#T) tag

过滤规则会将标签 tag 添加到数据连接中，并且不会快速匹配。 这样，使用 tagged 关键字的替代规则可以在 `ftp-proxy` 锚点之后实施。 这些规则可以使用特殊的 pf(4) 功能，如路由、回复、标签、rtable、重载等。 那个 `ftp-proxy` 并没有自己实现。

[`-t`](#t) timeout

在代理断开之前控制连接可以空闲的秒数。 最大值为 86400 秒，这也是默认值。 不要将此设置得太低，因为当发生大量数据传输时，控制连接通常是空闲的。

[`-v`](#v)

在 `ftp-proxy` 提交的 pf 规则上设置“日志”标志。 使用两次来设置“log-all”标志。 默认情况下，pf 规则不记录。

[配置](#__u914D___u7F6E_)
=======================

要使用代理， pf.conf(5) 需要以下规则。 所有锚都是强制性的。 根据需要调整规则。

在 NAT 部分：

nat-anchor "ftp-proxy/\*" rdr-anchor "ftp-proxy/\*" rdr pass on $int\_if proto tcp from $lan to any port 21 -> \\ 127.0.0.1 port 8021 

在规则部分：

anchor "ftp-proxy/\*" pass out proto tcp from $proxy to any port 21 

[参见](#__u53C2___u89C1_)
=======================

ftp(1), pf(4), pf.conf(5)

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

如果系统以高于 1 的 securelevel(7) 运行，则 pf(4) 不允许修改规则集。 在该级别， `ftp-proxy` 无法向锚点添加规则，并且 FTP 数据连接可能会被阻止。

不允许使用低于 1024 的协商数据连接端口。

出于安全原因，主动模式的协商 IP 地址将被忽略。 这使得第三方文件传输变得不可能。

`ftp-proxy` chroots 到 "/var/empty" 并更改为用户 "proxy" 以放弃特权。

February 26, 2008

FreeBSD 13.1-RELEASE