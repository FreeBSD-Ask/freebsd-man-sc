# altq.4

`ALTQ` — 网络数据包的交替排队

## 名称

`ALTQ`

## 概要

`options ALTQ`

`options ALTQ_CBQ options ALTQ_CODEL options ALTQ_RED options ALTQ_RIO options ALTQ_HFSC options ALTQ_CDNR options ALTQ_PRIQ options ALTQ_FAIRQ`

## 描述

`ALTQ` 系统是一个框架，提供多种排队规则用于对发出的网络数据包进行排队。这是通过对接口数据包队列的修改来实现的。详见 [altq(9)](../man9/altq.9.md)。

`ALTQ` 的用户界面由 pfctl(8) 工具实现，因此关于 `ALTQ` 能力的完整描述及使用方法，请参阅 pfctl(8) 和 [pf.conf(5)](../man5/pf.conf.5.md) 手册页。

### 内核选项

内核配置文件中与 `ALTQ` 操作相关的选项如下：

**`ALTQ`** 启用 `ALTQ`。
**`ALTQ_CBQ`** 构建“基于类的排队”（Class Based Queuing）规则。
**`ALTQ_CODEL`** 构建“受控延迟”（Controlled Delay）规则。
**`ALTQ_RED`** 构建“随机早期检测”（Random Early Detection）扩展。
**`ALTQ_RIO`** 为输入和输出构建“随机早期丢弃”（Random Early Drop）。
**`ALTQ_HFSC`** 构建“分层包调度器”（Hierarchical Packet Scheduler）规则。
**`ALTQ_CDNR`** 构建流量调节器。此选项目前无意义，因为该调节器未被任何可用的规则或使用者使用。
**`ALTQ_PRIQ`** 构建“优先级排队”（Priority Queuing）规则。
**`ALTQ_FAIRQ`** 构建“公平排队”（Fair Queuing）规则。
**`ALTQ_NOPCC`** 当 TSC 不可用时必需。
**`ALTQ_DEBUG`** 启用额外的调试功能。

注意，`ALTQ` 规则不能作为内核模块加载。要使用某种规则，必须将其构建进自定义内核。`ALTQ` 配置过程所必需的 [pf(4)](pf.4.md) 接口可以作为模块加载。

## 支持的设备

要将某块网卡与 `ALTQ` 配合使用，需要 [altq(9)](../man9/altq.9.md) 中描述的驱动修改。这些修改已应用于以下硬件驱动：[ae(4)](ae.4.md), [age(4)](age.4.md), [alc(4)](alc.4.md), [ale(4)](ale.4.md), [aue(4)](aue.4.md), [axe(4)](axe.4.md), [bce(4)](bce.4.md), [bfe(4)](bfe.4.md), [bge(4)](bge.4.md), [bxe(4)](bxe.4.md), [cas(4)](cas.4.md), [dc(4)](dc.4.md), [em(4)](em.4.md), [epair(4)](epair.4.md), [et(4)](et.4.md), [fxp(4)](fxp.4.md), [gem(4)](gem.4.md), igb(4), [ix(4)](ix.4.md), [jme(4)](jme.4.md), le(4), [liquidio(4)](liquidio.4.md), [msk(4)](msk.4.md), [mxge(4)](mxge.4.md), [my(4)](my.4.md), [nfe(4)](nfe.4.md), [nge(4)](nge.4.md), [qlxgb(4)](qlxgb.4.md), [re(4)](re.4.md), [rl(4)](rl.4.md), [sge(4)](sge.4.md), [sis(4)](sis.4.md), [sk(4)](sk.4.md), [ste(4)](ste.4.md), [stge(4)](stge.4.md), [ti(4)](ti.4.md), [udav(4)](udav.4.md), [vge(4)](vge.4.md), [vr(4)](vr.4.md), [vte(4)](vte.4.md), 和 [xl(4)](xl.4.md)。

[tun(4)](tun.4.md), if_bridge(4), if_vlan(4), 和 [ng_iface(4)](ng_iface.4.md) 伪驱动也支持 `ALTQ`。

示例：

```sh
altq on igb0 cbq queue { def aq }
queue def bandwidth 90% cbq (default borrow)
queue aq bandwidth 10Mb cbq
pass in on igb0.10 proto udp all queue aq keep state
```

## 参见

[pf(4)](pf.4.md), [pf.conf(5)](../man5/pf.conf.5.md), [ipfw(8)](../man8/ipfw.8.md), pfctl(8), [altq(9)](../man9/altq.9.md)

## 历史

`ALTQ` 系统首次出现于 1997 年 3 月，并成为 KAME 项目（https://www.kame.net）的一部分。它在 FreeBSD 5.3 中被引入。
