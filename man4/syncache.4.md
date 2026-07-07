# syncache(4)

`syncache` —

## 名称

`syncache` 用于控制 TCP SYN 缓存的 [sysctl(8)](../man8/sysctl.8.md) MIB

## 概要

`sysctl net.inet.tcp.syncookies`

`sysctl net.inet.tcp.syncookies_only`

-
-

`sysctl net.inet.tcp.syncache.hashsize`

`sysctl net.inet.tcp.syncache.bucketlimit`

`sysctl net.inet.tcp.syncache.cachelimit`

`sysctl net.inet.tcp.syncache.rexmtlimit`

`sysctl net.inet.tcp.syncache.count`

`sysctl net.inet.tcp.syncache.see_other`

`sysctl net.inet.tcp.syncache.rst_on_sock_fail`

-
-
-
-
-
-
-

## 描述

`sysctl` [sysctl(8)](../man8/sysctl.8.md) MIB 用于控制系统中的 TCP SYN 缓存，旨在处理 SYN flood 拒绝服务攻击。

当 TCP SYN 段到达与监听套接字对应的端口时，会在 `sysctl` 中创建条目，并向对端返回 SYN,ACK 段。`sysctl` 条目持有初始 SYN 的 TCP 选项、足够执行 SYN,ACK 重传的状态，且占用空间比 TCP 控制块端点更少。包含对 SYN,ACK 的 ACK 且与某个 `sysctl` 条目匹配的入站段将使系统创建一个 TCP 控制块，使用 `sysctl` 条目中存储的选项，随后该 `sysctl` 条目被释放。

`sysctl` 通过最小化服务器上保持的状态以及限制 `sysctl` 的总体大小来保护系统免受 SYN flood DoS 攻击。

`Syncookies` 通过将初始 SYN 的状态保留在网络中来提供一种虚拟扩展 `Syncookies` 大小的方法。启用 `syncookies` 会在 SYN,ACK 回复中向客户端机器发送一个加密值，该值随后在客户端的 ACK 中返回。如果在 `syncookies` 中找不到对应条目，但该值通过特定安全检查，则连接将被接受。仅当 `syncookies` 无法处理入站连接量且先前条目已从缓存中驱逐时才使用此机制。

`Syncookies` 有一些缺点，谨慎的管理员可能希望注意。由于初始 SYN 的 TCP 选项未被保存，因此不会应用于连接，从而无法使用窗口缩放、时间戳或精确 MSS 调整等功能。由于返回的 ACK 建立连接，攻击者可能通过 ACK flood 一台机器以尝试建立连接。虽然已采取措施缓解此风险，但这可能提供一种绕过对设置 SYN 位的入站段进行过滤的防火墙的方法。

要禁用 `syncache` 并仅使用 `syncookies` 运行，将 `net.inet.tcp.syncookies_only` 设为 1。要使用 `syncookies` 处理 `syncache` 中的桶溢出，将 `net.inet.tcp.syncookies` 设为 1。`net.inet.tcp.syncookies_only` 的默认值为 0，`net.inet.tcp.syncookies` 的默认值为 1。

`syncache` 在 sysctl(3) MIB 的 `net.inet.tcp.syncache` 分支中实现了若干变量。其中几个可通过在 [loader(8)](../man8/loader.8.md) 中设置相应变量来调整。

**`hashsize`** `syncache` 哈希表的大小，必须是 2 的幂。只读，可通过 [loader(8)](../man8/loader.8.md) 调整。

**`bucketlimit`** 哈希表每个桶中允许的条目数限制。应保持低值以最小化搜索时间。只读，可通过 [loader(8)](../man8/loader.8.md) 调整。

**`cachelimit`** `syncache` 中条目总数的限制。默认为 `( hashsize` × `bucketlimit )`，可设为更低以最小化内存消耗。只读，可通过 [loader(8)](../man8/loader.8.md) 调整。

**`rexmtlimit`** SYN,ACK 在被丢弃前重传的最大次数。默认 3 次重传对应 45 秒超时，可根据到客户端机器的 RTT 增加此值。可通过 sysctl(3) 调整。

**`count`** `syncache` 中存在的条目数（只读）。

**`see_other`** 如果设为真值，则所有 `syncache` 条目都将通过 `net.inet.tcp.pcblist` sysctl 或 [netstat(1)](../man1/netstat.1.md) 可见，忽略所有 [security(7)](../man7/security.7.md) UID/GID、jail(2) 和 [mac(4)](mac.4.md) 检查。如果关闭，则强制执行可见性检查。然而，每处理一个入站 SYN 数据包都需要额外的 [ucred(9)](../man9/ucred.9.md) 引用。默认为关闭。

**`rst_on_sock_fail`** 如果套接字分配失败，则发送 TCP RST 段。默认为开启。

可通过 [netstat(1)](../man1/netstat.1.md) 获取 `syncache` 性能的统计信息，提供以下计数：

**`syncache entries added`** 成功插入 `syncache` 的条目。

**`retransmitted`** 因超时到期而重传的 SYN,ACK。

**`dupsyn`** 匹配现有条目的入站 SYN 段。

**`dropped`** 因无法发送 SYN,ACK 而丢弃的 SYN。

**`completed`** 成功完成的连接。

**`bucket overflow`** 因超出每桶大小而丢弃的条目。

**`cache overflow`** 因超出总体缓存大小而丢弃的条目。

**`reset`** 收到 RST 段。

**`stale`** 因达到最大重传次数或监听套接字消失而丢弃的条目。

**`aborted`** 新套接字分配失败。

**`badack`** 因错误 ACK 回复而丢弃的条目。

**`unreach`** 因 ICMP 不可达消息而丢弃的条目。

**`zone failures`** 分配新 `syncache` 条目失败。

**`cookies sent`** 在 SYN ACK 段中发送的 SYN cookies。

**`cookies received`** 带有有效 syncookies 且导致 TCP 连接建立的 ACK 段。

**`spurious cookies rejected`** syncache 查找失败且最近未发送 syncookie 的接收 ACK。

**`failed cookies rejected`** syncookie 验证失败的接收 ACK。

## 参见

[netstat(1)](../man1/netstat.1.md), jail(2), [mac(4)](mac.4.md), [tcp(4)](tcp.4.md), [security(7)](../man7/security.7.md), [loader(8)](../man8/loader.8.md), [sysctl(8)](../man8/sysctl.8.md), [ucred(9)](../man9/ucred.9.md)

## 历史

现有的 `syncache` 实现首次出现于 FreeBSD 4.5。`syncache` 的原始概念最初出现于 BSD/OS，后来被 NetBSD 修改，并在此进一步扩展。

## 作者

`syncache` 代码和手册页由 Jonathan Lemon <jlemon@FreeBSD.org> 编写。
