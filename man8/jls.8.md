  JLS(8)  

JLS(8)

FreeBSD System Manager's Manual

JLS(8)

[名称](#__u540D___u79F0_)
=======================

`jls` —

列出 jails

[概要](#__u6982___u8981_)
=======================

`jls` \[`--libxo`\] \[`-dhNnqsv`\] \[`-j` jail\] \[parameter ...\]

[描述](#__u63CF___u8FF0_)
=======================

`jls` 实用程序列出所有活动的 jail ，或指定的 jail 。 每个 jail 由一行表示，其中包含列出 parameters 的空格分隔值，包括伪参数 all ，它将显示所有可用的 jail 参数。 可以通过 “`sysctl` `-d` security.jail.param” 检索可用参数列表。 有关一些核心参数的描述，请参见 jail(8) 。

If no parameters 如果没有给定参数或任何选项 `-hns` ，将打印以下四列： jail 标识符 (jid)、IP 地址 (ip4.addr)、主机名 (host.hostname) 和路径 (path)。

可以使用以下选项：

[`--libxo`](#-libxo)

通过 libxo(3) 以不同的人类和机器可读格式生成输出。 有关命令行参数的详细信息，请参阅 xo\_parse\_args(3) 。

[`-d`](#d)

列出 dying 的 jail 和活跃的 jail 。.

[`-h`](#h)

打印包含所列参数的标题行。 如果命令行上没有给出参数，则假定 all 参数。

[`-N`](#N)

在标准显示模式下，打印每个 jail 的名称而不是其数字 ID。 如果 jail 没有名称，则打印数字 ID。

[`-n`](#n)

以 “name=value” 格式打印参数，其中每个参数前面都有其名称。 如果命令行上没有给出参数，则假定 all 参数。

[`-q`](#q)

如果参数包含空格或引号，或者是空字符串，请在参数周围加上引号。

[`-s`](#s)

打印适合传递给 jail(8) 的参数，跳过只读和未使用的参数。 暗示 `-nq` 。

[`-v`](#v)

使用每个 jail 的多行摘要扩展标准显示，包含以下参数： jail 标识符 (jid)、主机名 (host.hostname)、路径 (path)、 jail 名称 (name)、 jail 状态 (dying)、cpuset ID (cpuset)、IP 地址（ip4.addr 和 ip6.addr）。

[`-j`](#j) jail

要列出的 jail 的 jail 或名称。 如果没有此选项，将列出所有活动的 jail 。

[参见](#__u53C2___u89C1_)
=======================

jail\_get(2), libxo(3), xo\_parse\_args(3), jail(8), jexec(8)

[历史](#__u5386___u53F2_)
=======================

`jls` 实用程序是在 FreeBSD 5.1 中添加的。 FreeBSD 8.0 中引入了可扩展的 jail 参数。在 FreeBSD 11.0 中添加了 libxo 支持。

July 20, 2012

FreeBSD 13.1-RELEASE