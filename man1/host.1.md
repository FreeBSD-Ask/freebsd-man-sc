  HOST(1)  

HOST(1)

FreeBSD General Commands Manual

HOST(1)

[名称](#__u540D___u79F0_)
=======================

`host` —

DNS lookup utility

[概要](#__u6982___u8981_)
=======================

`host` \[`-aCdilrsTvw46`\] \[`-c` class\] \[`-N` ndots\] \[`-R` number\] \[`-t` type\] \[`-W` wait\] name \[server\]

[描述](#__u63CF___u8FF0_)
=======================

`host` 是一个用于执行 DNS 查找的简单实用程序。 它通常用于将名称转换为 IP 地址，反之亦然。

name 是要查找的域名。 它也可以是点分十进制 IPv4 地址或冒号分隔的 IPv6 地址，在这种情况下， `host` 默认会对该地址执行反向查找。

如果未提供 name , `host` 会打印其使用情况的简短摘要。

server 是一个可选参数，它是 `host` 应查询的名称服务器的域名或 IP 地址，而不是 /etc/resolv.conf 中列出的服务器或服务器。 当 server 为域名时，系统解析器用于获取其地址。

支持的选项：

[`-a`](#a)

进行 `ANY`-
类型的详细查询。 等效于 `-v` `-t` `ANY` 。

[`-C`](#C)

从所有权威 name 服务器查询区域名称的 `SOA` 记录。 名称服务器列表是通过 `NS` 查询 name 获得的。

[`-c`](#c) class

执行类 class 的 DNS 查询。 公认的类别是 `IN` (Internet), `CH` (Chaosnet), `HS` (Hesiod), `NONE`, `ANY` 和 `CLASS`N (其中 N 是从 1 到 255 的数字）。 默认为 `IN` 。

[`-d`](#d)

产生详细的输出。 这是 `-v` 的同义词，是为了向后兼容而提供的。

[`-i`](#i)

使用 IP6.INT 域进行 IPv6 地址的反向查找（如 RFC1886 中所定义；请注意，RFC4159 不推荐使用 IP6.INT）。 默认使用 IP6.ARPA。

[`-l`](#l)

通过执行区域传输 (`AXFR`) 列出区域 name 中的所有 `NS, PTR, A` 和 `AAAA` 记录。 您可以将此选项与 `-a` 组合以打印所有记录，或与 `-t` 组合以仅打印特定记录。

[`-N`](#N) ndots

将至少有这么多点的名称视为绝对名称。 也就是说，尝试在从 /etc/resolv.conf `domain` 或 `search` 选项之前直接解决它们。

[`-r`](#r)

通过清除查询的 (“recursion desired”) 位对名称服务器执行非递归查询。

[`-R`](#R) number

当查询未及时收到答案时，请重试多次。 默认值为 1 次重试。 如果 number 为负数或零，则使用 1 代替。

[`-s`](#s)

按原样报告 SERVFAIL 响应，不要忽略它们。

[`-T`](#T)

通过 TCP 查询名称服务器。 默认情况下使用 UDP，但需要 TCP 的 `AXFR` 和 `IXFR` 查询除外。 如果 UDP 响应被截断（即设置了 TC 位）， `host` 也会在 TCP 模式下重试 UDP 查询。

[`-t`](#t) type

执行类型 type 的 DNS 查询，可以是任何标准查询类型名称 (`A`, `CNAME`, `MX`, `TXT`, 等 、) 通配符查询 (`ANY`) 或 `TYPE`N, 其中 N 是从 1 到 65535 的数字。 对于 `IXFR` (incremental zone transfer) 查询，可以通过在数字后面附加等号来指定起始序列号 (例如 `-t` `IXFR`\=12345678) 。

默认是查询 `A`, `AAAA`, 和 `MX` 记录，除非给出 `-C` 或 `-l` 选项（在这种情况下进行 `SOA` 或 `AXFR` 查询）或 name 是有效的 IP 地址（在这种情况下使用 `PTR` 查询进行反向查找被执行）。

[`-v`](#v)

产生详细的输出。

[`-w`](#w)

永远（或很长时间）等待来自名称服务器的响应。

[`-W`](#W) wait

在超时之前等待这么多秒以等待来自名称服务器的回复。 如果 wait 为负数或零，则使用值 1。 默认情况下，TCP 连接等待 10 秒，UDP 连接等待 5 秒（两者都需要重试，请参阅选项 `-R` )。

[`-4`](#4)

仅使用 IPv4 传输。

[`-6`](#6)

仅使用 IPv6 传输。

[文件](#__u6587___u4EF6_)
=======================

/etc/resolv.conf

[参见](#__u53C2___u89C1_)
=======================

drill(1), resolv.conf(5)

[兼容性](#__u517C___u5BB9___u6027_)
================================

`host`-
旨在与 BIND9 发行版中的 ‘host’ 实用程序合理兼容，包括支持的选项和生成的输出。 以下是已知显着差异的列表：

*   不支持调试选项 (`-D` 和 `-m`) 。
*   不支持查询类 `CLASS0` 和类型 `TYPE0` 。
*   特别对待域名中的反斜杠。
*   最多支持 255 次重试（选项 `-R` )。
*   某些资源记录的格式不同。 例如， `RRSIG` 和 `DNSKEY` 记录显示时没有空格。 解析 /etc/resolv.conf 命令时，会忽略 `sortlist` 和 `options` 。 当存在多个 `search` 和/或 `domain` 命令时， `host` 首先使用最后一个 `domain` 命令，然后是所有 `search` 命令，而 BIND9 中的 ‘host’ 使用最后指定的任何命令。
*   详细数据包输出中缺少 ‘Pseudosection TSIG’ 。

[作者](#__u4F5C___u8005_)
=======================

Vitaly Magerya ⟨magv@tx97.net⟩

August 27, 2012

FreeBSD 13.1-RELEASE