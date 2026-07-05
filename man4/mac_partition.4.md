# mac_partition.4

`mac_partition` — 进程分区策略

## 名称

`mac_partition`

## 概要

要将进程分区策略编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_PARTITION

或者，要在引导时加载进程分区模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_partition_load="YES"
```

## 描述

`mac_partition` 策略模块实现了一种进程分区策略，允许管理员根据进程的数字进程分区（在进程的 MAC 标签中指定）将运行中的进程放入“分区”中。指定了分区的进程只能看到同一分区中的进程。如果未为进程指定分区，则它可以查看系统中的所有其他进程（受本手册页中未定义的其他 MAC 策略限制约束）。无法将进程放入多个分区。

### 标签格式

分区标签采用以下格式：

```sh
`partition /` `value`
```

其中 `value` 可以是任何整数值或“`none`”。例如：

```sh
partition/1
partition/20
partition/none
```

## 参见

[mac(4)](mac.4.md), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [maclabel(7)](../man7/maclabel.7.md), [mac(9)](../man9/mac.9.md)

## 历史

`mac_partition` 策略模块首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分，贡献给 FreeBSD 项目。

## 缺陷

虽然 MAC 框架的设计意图是支持对 root 用户的限制，但目前并非所有攻击通道都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防御恶意的特权用户。
