# mac_seeotheruids(4)

`mac_seeotheruids` — 控制用户是否能查看其他用户的简单策略

## 名称

`mac_seeotheruids`

## 概要

要将此策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_SEEOTHERUIDS

或者，要在引导时加载该模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_seeotheruids_load="YES"
```

## 描述

`mac_seeotheruids` 策略模块在启用时会禁止用户查看其他用户拥有的进程或套接字。

要启用 `mac_seeotheruids`，请将 sysctl OID `security.mac.seeotheruids.enabled` 设置为 1。要允许超级用户凭借特权感知其他凭据，请将 sysctl OID `security.mac.seeotheruids.suser_privileged` 设置为 1。

要允许用户查看同一主组拥有的进程和套接字，请将 sysctl OID `security.mac.seeotheruids.primarygroup_enabled` 设置为 1。

要允许具有特定组 ID 的进程免受该策略约束，请将 sysctl OID `security.mac.seeotheruids.specificgid_enabled` 设置为 1，并将 `security.mac.seeotheruids.specificgid` 设置为要豁免的组 ID 列表。

### 标签格式

`mac_seeotheruids` 未定义任何标签。

## 参见

[mac(4)](mac.4.md), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_test(4)](mac_test.4.md), [mac(9)](../man9/mac.9.md)

## 历史

`mac_seeotheruids` 策略模块首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分，贡献给 FreeBSD 项目。

## 缺陷

虽然 MAC 框架的设计意图是支持对 root 用户的限制，但目前并非所有攻击通道都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防御恶意的特权用户。
