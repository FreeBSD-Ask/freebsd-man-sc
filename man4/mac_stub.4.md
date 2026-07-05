# mac_stub.4

`mac_stub` — MAC 策略桩模块

## 名称

`mac_stub`

## 概要

要将桩策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_STUB

或者，要在引导时加载 stub 模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_stub_load="YES"
```

## 描述

`mac_stub` 策略模块实现了一个桩 MAC 策略，对系统中的访问控制没有任何影响。与 [mac_none(4)](mac_none.4.md) 不同，每个 MAC 入口点都被定义为“no-op”，因此该策略模块会在每个事件中被调用，但不会对系统行为产生任何改变。

### 标签格式

`mac_stub` 未定义任何标签。

## 参见

[mac(4)](mac.4.md), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [mac(9)](../man9/mac.9.md)

## 历史

`mac_stub` 策略模块首次出现于 FreeBSD 5.1，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分，贡献给 FreeBSD 项目。

## 缺陷

虽然 MAC 框架的设计意图是支持对 root 用户的限制，但目前并非所有攻击通道都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防御恶意的特权用户。
