  ROUTE6D(8)  

ROUTE6D(8)

FreeBSD System Manager's Manual

ROUTE6D(8)

[名称](#__u540D___u79F0_)
=======================

`route6d` —

RIP6 路由守护进程

[概要](#__u6982___u8981_)
=======================

`route6d` \[`-adDhlnqsS`\] \[`-R` routelog\] \[`-A` prefix/preflen,if1\[,if2...\]\] \[`-L` prefix/preflen,if1\[,if2...\]\] \[`-N` if1\[,if2...\]\] \[`-O` prefix/preflen,if1\[,if2...\]\] \[`-P` number\] \[`-p` pidfile\] \[`-Q` number\] \[`-T` if1\[,if2...\]\] \[`-t` tag\]

[描述](#__u63CF___u8FF0_)
=======================

`route6d` 实用程序是一个支持 RIP over IPv6 的路由守护程序。

选项是：

[`-a`](#a)

启用静态定义路由的老化。 使用此选项，任何静态定义的路由都将被删除，除非相应的更新到达，就像在 `route6d` 启动时接收到的路由一样。

[`-R`](#R) routelog

此选项使 `route6d` 将路由更改（添加/删除）记录到文件 routelog 。

[`-A`](#A) prefix/preflen,if1\[,if2...\]

此选项用于聚合路由。 prefix/preflen 指定聚合路由的前缀和前缀长度。 发布路由时， `route6d` 过滤聚合覆盖的特定路由，并将聚合路由 prefix/preflen 发布到以逗号分隔的接口列表 if1\[,if2...\] 中指定的接口。 接口列表中的字符 “`*`”, “`?`” 和 “`[`” 将被解释为 shell 样式模式。 `route6d` 实用程序使用 `RTF_REJECT` 标志创建到内核路由表的 prefix/preflen 的静态路由。

[`-d`](#d)

启用调试消息的输出。 此选项还指示 `route6d` 在前台模式下运行（不会成为守护进程）。

[`-D`](#D)

启用调试消息的广泛输出。 此选项还指示 `route6d` 在前台模式下运行（不会成为守护进程）。

[`-h`](#h)

禁用水平分割处理。

[`-l`](#l)

默认情况下，出于安全原因， `route6d` 不会交换站点本地路由。 这是因为站点本地地址空间的语义比较模糊（规范仍在制定中），并且没有好的方法来定义站点本地边界。 使用 `-l` 选项, `route6d` 也将交换站点本地路由。 它不能用于站点边界路由器，因为 `-l` 选项假定所有接口都在同一个站点中。

[`-L`](#L) prefix/preflen,if1\[,if2...\]

过滤来自接口 if1,\[if2...\] 的传入路由。 `route6d` 实用程序将接受 prefix/preflen 中的传入路由。 如果指定了多个 `-L` 选项，则接受与其中一个选项匹配的任何路由。 `::/0` 被特别视为默认路由，而不是 “任何前缀长度大于或等于 0 的路由” 。 如果您想接受任何路由，请不指定 `-L` 选项。 例如，使用 “`-L` `2001:db8::/16,if1` `-L` `::/0,if1`” `route6d`-
将接受默认路由和 6bone 测试地址中的路由，但不接受其他路由。

[`-n`](#n)

不要更新内核路由表。

[`-N`](#N) if1\[,if2...\]

不要监听或通告从/到由 if1,\[if2...\] 指定的接口的路由。

[`-O`](#O) prefix/preflen,if1\[,if2...\]

限制向 if1,\[if2...\] 指定的接口发布路由。 使用此选项， `route6d` 将仅通告与 prefix/preflen 匹配的路由。

[`-P`](#P) number

指定在计算过期计时器时要忽略的路由。 number 必须是 `1`, `2` 或 `3` and it means route flags of `RTF_PROTO1`, `RTF_PROTO2`, or `RTF_PROTO3` 的路由标志。 当指定为 `1` 时，具有 `RTF_PROTO1` 的路由将永不过期。

[`-p`](#p) pidfile

指定用于存储进程 ID 的替代文件。 默认为 /var/run/route6d.pid 。

[`-Q`](#Q) number

指定将用于 RIP 协议添加的路由的标志。 默认值为 `2` (`RTF_PROTO2`) 。

[`-q`](#q)

使 `route6d` 处于只听模式。 不发送广告。

[`-s`](#s)

当 `route6d` 调用时，使 `route6d` 通告存在于内核路由表中的静态定义的路由。 公告遵循常规的水平分割规则。

[`-S`](#S)

此选项与 `-s` 选项相同，但不适用水平分割规则。

[`-T`](#T) if1\[,if2...\]

只通告默认路由，指向 if1,\[if2...\] 。

[`-t`](#t) tag

将路由标签 tag 附加到原始路由条目。 tag 可以是十进制、以 `0` 为前缀的八进制或以 `0x` 为前缀的十六进制。

收到信号 `SIGINT` 或 `SIGUSR1` 后， `route6d` 会将当前内部状态转储到 /var/run/route6d\_dump 。

[文件](#__u6587___u4EF6_)
=======================

/var/run/route6d\_dump

在 `SIGINT` 或 `SIGUSR1` 上转储内部状态

[参见](#__u53C2___u89C1_)
=======================

G. Malkin and R. Minnear, RIPng for IPv6, RFC2080, January 1997.

[笔记](#__u7B14___u8BB0_)
=======================

`route6d` 实用程序使用 RFC2292 中定义的 IPv6 高级 API，用于使用链路本地地址与对等方通信。

在内部， `route6d` 将接口标识符嵌入到链接本地地址 (`fe80::xx` 和 `ff02::xx`) 的第 32 位到第 63 位中，因此它们将在内部状态转储文件 (/var/run/route6d\_dump) 中可见。

路由表操作因 IPv6 实施而异。 目前 `route6d` 遵循 WIDE Hydrangea/KAME IPv6 内核，将无法在其他平台上运行。

当前 `route6d` 在连续更新到达时不会降低触发更新的速率。

November 18, 2012

FreeBSD 13.1-RELEASE