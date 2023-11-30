  BLACKLISTCTL(8)  

BLACKLISTCTL(8)

FreeBSD System Manager's Manual

BLACKLISTCTL(8)

[名称](#__u540D___u79F0_)
=======================

`blacklistctl` —

显示和更改 blacklistd 的状态

[概要](#__u6982___u8981_)
=======================

`blacklistctl` `dump` \[`-abdnrw`\]

[描述](#__u63CF___u8FF0_)
=======================

`blacklistctl` 是一个用于显示 blacklistd(8) 状态的程序

可以使用以下选项：

[`-a`](#a)

显示所有数据库条目，默认情况下它只显示胚胎条目。

[`-b`](#b)

仅显示被阻止的条目。

[`-d`](#d)

提高调试级别。

[`-n`](#n)

不显示标题。

[`-r`](#r)

显示剩余阻塞时间而不是上次活动时间。

[`-w`](#w)

通常地址的宽度对 IPv4 是有利的， `-w` 标志使显示的宽度足以显示 IPv6 地址。

[参见](#__u53C2___u89C1_)
=======================

blacklistd(8)

[笔记](#__u7B14___u8BB0_)
=======================

有时，报告的失败尝试次数可能超过 blacklistd(8) 配置为阻止的尝试次数。 这可能是因为手动删除了规则，或者在添加规则块时进行了更多尝试。 这种情况是正常的；在这种情况下， blacklistd(8) 将首先尝试删除现有规则，然后重新添加它以确保只有一个规则处于活动状态。

[历史](#__u5386___u53F2_)
=======================

`blacklistctl` 最早出现在 NetBSD 7 中。 FreeBSD 对 `blacklistctl` 的支持是在 FreeBSD 11 中实现的。

[作者](#__u4F5C___u8005_)
=======================

Christos Zoulas

June 7, 2016

FreeBSD 13.1-RELEASE