# mac_bsdextended.4

`mac_bsdextended` — 文件系统防火墙策略

## 名称

`mac_bsdextended`

## 概要

要将文件系统防火墙策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_BSDEXTENDED

或者，要在引导时加载文件系统防火墙策略模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_bsdextended_load="YES"
```

## 描述

`mac_bsdextended` 安全策略模块提供一个接口，让系统管理员就用户和某些系统对象施加强制性规则。规则上传到模块（通常使用 ugidfw(8) 或其他使用 libugidfw(3) 的工具），在内部存储并用于决定是否允许或拒绝特定访问（参见 ugidfw(8)）。

## 实现说明

虽然实现了传统的 [mac(9)](../man9/mac.9.md) 入口点，但不使用策略标签；访问控制决策通过遍历内部规则列表做出，直到找到拒绝特定访问的规则，或到达列表末尾。`mac_bsdextended` 策略的工作方式类似于 [ipfw(8)](../man8/ipfw.8.md)，使用*首次匹配语义*。这意味着并非所有规则都会应用，仅应用第一个匹配的规则；因此如果规则 A 允许访问而规则 B 阻止访问，规则 B 将永远不会被应用。

## SYSCTL 变量

以下 sysctl 可用于调整 `mac_bsdextended` 的行为：

**`security.mac.bsdextended.enabled`** 设为零或一以关闭或开启策略。

**`security.mac.bsdextended.rule_count`** 列出已定义的规则数，当前最大规则数为 256。

**`security.mac.bsdextended.rule_slots`** 列出当前正在使用的规则槽数。

**`security.mac.bsdextended.firstmatch_enabled`** 在旧的“所有规则匹配”功能和新的“首条规则匹配”功能之间切换。默认启用。

**`security.mac.bsdextended.logging`** 通过 `AUTHPRIV` syslog(3) 设施记录所有访问违规。

**`security.mac.bsdextended.rules`** 当前没有有用的功能。

## 参见

libugidfw(3), syslog(3), [mac(4)](mac.4.md), [mac_biba(4)](mac_biba.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [ipfw(8)](../man8/ipfw.8.md), ugidfw(8), [mac(9)](../man9/mac.9.md)

## 历史

`mac_bsdextended` 策略模块首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

“首次匹配”和日志功能后来由 Tom Rhodes <trhodes@FreeBSD.org> 添加。

## 作者

本软件由 NAI Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分贡献给 FreeBSD 项目。
