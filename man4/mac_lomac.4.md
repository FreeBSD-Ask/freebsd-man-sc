# mac_lomac.4

`mac_lomac` — 低水位强制访问控制数据完整性策略

## 名称

`mac_lomac`

## 概要

要将 LOMAC 编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_LOMAC

或者，要在引导时加载 LOMAC 模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_lomac_load="YES"
```

## 描述

`mac_lomac` 策略模块实现 LOMAC 完整性模型，通过信息流策略结合浮动标签的主体降级来保护系统对象和主体的完整性。在 LOMAC 中，所有系统主体和对象都被分配完整性标签，根据其类型由一个或多个层次化等级组成。这些标签元素共同允许所有标签置于偏序关系中，信息流保护和降级决策基于描述该次序的支配运算符。层次化等级字段表示为 0 到 65535 之间的值，值越高反映的完整性越高。

存在三个特殊标签组件值：

| **标签** | **比较** |
| --- | --- |
| `low` | 被所有其他标签支配 |
| `equal` | 等于所有其他标签 |
| `high` | 支配所有其他标签 |

“`high`”标签分配给影响整个系统完整性的系统对象。“`equal`”标签可用于指示特定主体或对象豁免 LOMAC 保护。例如，标签“`lomac/equal(equal-equal)`”可能用于一个将被用于管理性地重新标记系统上任何内容的主体。

几乎所有系统对象都标记有单个活动标签元素，反映对象的完整性或对象所含数据的完整性。文件系统对象可能包含一个额外的辅助标签，用于确定在目录中创建的新文件所继承的完整性级别，或主体在执行可执行文件时采用的替代标签。通常，对象标签以如下形式表示：

> `lomac /` `grade` [`auxgrade`]

例如：

```sh
lomac/10[2]
lomac/low
```

主体标签由三个标签元素组成：一个单（活动）标签，以及一个可用标签范围。该范围使用两个有序的 LOMAC 标签元素表示，设置于进程上时，允许进程将活动标签更改为完整性大于或等于范围低端、小于或等于范围高端的任何标签。通常，主体标签以如下形式表示：

> `lomac /` `singlegrade ( lograde` - `higrade`)

对象的修改限制为通过以下比较访问：

> `subject`::`higrade` [>=] `target-object`::`grade`

主体的修改相同，因为目标主体的单等级是参与比较的唯一元素。

当以下比较为真时，主体发生降级：

> `subject`::`singlegrade` > `object`::`grade`

发生降级时，主体的 `singlegrade` 和 `higrade` 会降低到对象的等级，必要时 `lograde` 也会降低。发生降级时，除了主体的权限降低外，其在内存空间中打开的共享 mmap(2) 对象可能根据以下 sysctl(3) 变量被撤销：

- `security.mac.lomac.revocation_enabled`
- `security.mac.enforce_vm`
- `security.mac.mmap_revocation`
- `security.mac.mmap_revocation_via_cow`

执行文件时，如果可执行文件有辅助标签，且该标签在当前 `lograde`-`higrade` 范围内，主体将立即采用该标签。此后，与任何其他读取操作一样，以可执行文件为目标执行降级。通过使用辅助标签，程序可以最初以较低的有效完整性级别执行，同时保留再次提升的能力。

这些规则通过阻止信息流，从而阻止低完整性主体影响高完整性主体的行为，防止低完整性主体修改高完整性对象或作用于这些对象的高完整性主体。LOMAC 完整性策略在多种环境中可能适用，既可防止操作系统损坏，也可在用户数据标记为高于攻击者完整性时防止其损坏。

LOMAC 安全模型在许多方面与 [mac_biba(4)](mac_biba.4.md) 和 [mac_mls(4)](mac_mls.4.md) 非常相似。更多背景信息请参见各自的手册页。

## 参见

mmap(2), sysctl(3), [mac(4)](mac.4.md), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [mac(9)](../man9/mac.9.md)

## 历史

`mac_lomac` 策略模块首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分贡献给 FreeBSD 项目。
