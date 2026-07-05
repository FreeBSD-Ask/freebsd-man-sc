# cc_dctcp.4

`cc_dctcp` — DCTCP 拥塞控制算法

## 名称

`cc_dctcp`

## 描述

DCTCP（数据中心 TCP）拥塞控制算法旨在利用从支持该功能的硬件所收到的显式拥塞通知（ECN）标记比例作为拥塞信号，从而在数据中心网络中最大化吞吐量并最小化延迟。

DCTCP 使用 ECN 标记数据包的比例来更新拥塞窗口。窗口缩减比例始终 <= 1/2。只有当所有数据包都被标记时，拥塞窗口才会减半。

为保持 ECN 标记比例的准确性，DCTCP 接收方通过设置（或清除）ECE 标记来镜像回传传入（或缺失）的 CE 标记。当接收方使用延迟 ACK 时，也会采用此反馈机制。

FreeBSD 的 DCTCP 实现包含两项面向单侧部署的 minor 修改。考虑到 DCTCP 用作发送方而传统 ECN 用作接收方的情况，DCTCP 会设置 CWR 标志作为对 ECE 标志的响应。此外，当传统 ECN 用作发送方而 DCTCP 用作接收方时，DCTCP 仅在传入数据包中设置了 CWR 标志时才避免镜像回传 ACK。

其他规范基于下文参见章节中引用的论文和 RFC。

## MIB 变量

该算法在 sysctl(3) MIB 的 `net.inet.tcp.cc.dctcp` 分支下暴露以下可调变量：

**`alpha`** 估算链路拥塞程度的初始值。有效范围为 0 到 1024，其中 1024 表示如果在第一个窗口中观察到 CE 且 `alpha` 尚未能调整到该路径的拥塞水平，则将拥塞窗口减半。默认值为 1024。

**`shift_g`** `alpha` 计算中的估算增益。它影响 alpha 调整到最近观察窗口时的响应速度。有效范围为 0 到 10，默认值为 4，对应有效增益为 1 / ( 2 ^ `shift_g` )，即 1/16。

**`slowstart`** 标志，指示慢启动后是否应将拥塞窗口减半。有效设置为 0 和 1，默认值为 0。

**`ect1`** 控制 DCTCP 会话在发送段时应使用 IP ECT(0) 标记（默认）还是使用 ECT(1) 标记以利用 L4S 基础设施。对此设置的更改仅影响新会话，现有会话将保留其先前的标记值。

## 参见

[cc_cdg(4)](cc_cdg.4.md), [cc_chd(4)](cc_chd.4.md), [cc_cubic(4)](cc_cubic.4.md), [cc_hd(4)](cc_hd.4.md), [cc_htcp(4)](cc_htcp.4.md), [cc_newreno(4)](cc_newreno.4.md), [cc_vegas(4)](cc_vegas.4.md), [mod_cc(4)](mod_cc.4.md), [tcp(4)](tcp.4.md), [mod_cc(9)](../man9/mod_cc.9.md)

> Mohammad Alizadeh, Albert Greenberg, David A. Maltz, Jitendra Padhye, Parveen Patel, Balaji Prabhakar, Sudipta Sengupta, Murari Sridharan, "Data Center TCP (DCTCP)", *ACM SIGCOMM 2010*, pp. 63-74, July 2010.

> Stephen Bensley, Dave Thaler, Praveen Balasubramanian, Lars Eggert, Glenn Judd, "Data Center TCP (DCTCP): TCP Congestion Control for Data Centers".

## 历史

`cc_dctcp` 拥塞控制模块首次出现于 FreeBSD 11.0。

该模块于 2014 年由在日本庆应义塾大学学习的 Midori Kato 首次发布。

## 作者

`cc_dctcp` 拥塞控制模块及本手册页由 Midori Kato <katoon@sfc.wide.ad.jp> 和 Lars Eggert <lars@netapp.com> 编写，并得到了 Hiren Panchasara <hiren@FreeBSD.org> 的帮助和修改。
