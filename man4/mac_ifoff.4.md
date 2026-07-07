# mac_ifoff(4)

`mac_ifoff` — 接口静默策略

## 名称

`mac_ifoff`

## 概要

要将接口静默策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_IFOFF

或者，要在引导时加载接口静默策略模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_ifoff_load="YES"
```

## 描述

`mac_ifoff` 接口静默模块允许管理员通过 [sysctl(8)](../man8/sysctl.8.md) 接口启用和禁用系统网络接口上的传入和传出数据流。

要禁用环回（[lo(4)](lo.4.md)）接口上的网络流量，将 [sysctl(8)](../man8/sysctl.8.md) OID `security.mac.ifoff.lo_enabled` 设为 0（默认 1）。

要启用其他接口上的网络流量，将 [sysctl(8)](../man8/sysctl.8.md) OID `security.mac.ifoff.other_enabled` 设为 1（默认 0）。

要允许接收 BPF 流量（即使其他流量被禁用），将 [sysctl(8)](../man8/sysctl.8.md) OID `security.mac.ifoff.bpfrecv_enabled` 设为 1（默认 0）。

### 标签格式

未定义任何标签。

## 参见

[mac(4)](mac.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [mac(9)](../man9/mac.9.md)

## 历史

`mac_ifoff` 策略模块首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分贡献给 FreeBSD 项目。

## 缺陷

虽然 MAC 框架设计旨在支持对 root 用户的限制，但并非所有攻击渠道目前都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防范恶意的特权用户。
