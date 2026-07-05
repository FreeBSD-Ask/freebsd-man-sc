# mac_biba.4

`mac_biba` — Biba 数据完整性策略

## 名称

`mac_biba`

## 概要

要将 Biba 编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_BIBA

或者，要在引导时加载 Biba 模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_biba_load="YES"
```

## 描述

`mac_biba` 策略模块实现 Biba 完整性模型，通过严格的信息流策略保护系统对象和主体的完整性。在 Biba 中，所有系统主体和对象都被分配完整性标签，由层次化等级和非层次化组件组成。这些标签元素共同允许所有标签置于偏序关系中，信息流保护基于描述该次序的支配运算符。层次化等级字段表示为 0 到 65535 之间的值，值越高反映的完整性越高。非层次化分隔字段表示为最多 256 个组件的集合，编号从 0 到 255。一个完整的标签由层次化和非层次化元素共同组成。

存在三个特殊标签值：

| **标签** | **比较** |
| -------- | -------- |
| `biba/low` | 低于所有其他标签 |
| `biba/equal` | 等于所有其他标签 |
| `biba/high` | 高于所有其他标签 |

“`biba/high`”标签分配给影响整个系统完整性的系统对象。“`biba/equal`”标签可用于指示特定主体或对象豁免 Biba 保护。这些特殊标签值不指定任何分隔，但在标签比较中，“`biba/high`”看起来包含所有分隔，“`biba/equal`”包含与其比较的另一个标签的相同分隔，“`biba/low`”不含任何分隔。

通常，Biba 访问控制采用以下模型：

- 与对象处于同一完整性级别的主体可对该对象进行读写，如同 Biba 保护未生效。
- 完整性级别高于对象的主体可写入该对象，但不能读取。
- 完整性级别低于对象的主体可读取该对象，但不能写入。
- 如果主体和对象标签无法在偏序中比较，则所有限制访问。

这些规则通过阻止信息流，从而阻止低完整性主体影响高完整性主体的行为，防止低完整性主体修改高完整性对象或作用于这些对象的高完整性主体。Biba 完整性策略在多种环境中可能适用，既可防止操作系统损坏，也可在用户数据标记为高于攻击者完整性时防止其损坏。在传统可信操作系统中，Biba 完整性模型用于保护可信代码库（TCB）。

Biba 完整性模型类似于 [mac_lomac(4)](mac_lomac.4.md)，不同之处在于 LOMAC 允许高完整性主体访问低完整性对象，但会降低主体的完整性级别以防止违反完整性规则。Biba 是固定标签策略，即所有主体和对象标签更改都是显式的，而 LOMAC 是浮动标签策略。

Biba 完整性模型也类似于 [mac_mls(4)](mac_mls.4.md)，不同之处在于支配运算符和访问规则相反，防止信息向下流动而非向上流动。多级安全（MLS）保护主体和对象的机密性而非完整性。

### 标签格式

几乎所有系统对象都标记有一个有效的活动标签元素，反映对象的完整性或对象所含数据的完整性。通常，对象标签以如下形式表示：

> `biba /` `grade : compartments`

例如：

```sh
biba/10:2+3+6
biba/low
```

主体标签由三个标签元素组成：一个有效（活动）标签，以及一个可用标签范围。该范围使用两个有序的 Biba 标签元素表示，设置于进程上时，允许进程将活动标签更改为完整性大于或等于范围低端、小于或等于范围高端的任何标签。通常，主体标签以如下形式表示：

> `biba /` `effectivegrade : effectivecompartments ( lograde : locompartments -`

> `higrade : hicompartments`)

例如：

```sh
biba/10:2+3+6(5:2+3-20:2+3+4+5+6)
biba/high(low-high)
```

有效的范围标签必须满足以下元素要求：

> `rangehigh` [>=] `effective` [>=] `rangelow`

当前存在一类带范围的对象，即网络接口。对于网络接口，有效标签元素引用通过该接口接收的数据包的默认标签，范围表示通过该接口传输的可接受数据包标签范围。

### 运行时配置

以下 [sysctl(8)](../man8/sysctl.8.md) MIB 可用于微调此 MAC 策略的执行。

**`security.mac.biba.enabled`** 启用 Biba 完整性策略的执行。（默认：1）。

**`security.mac.biba.ptys_equal`** 创建时将 [pty(4)](pty.4.md) 标记为“`biba/equal`”。（默认：0）。

**`security.mac.biba.revocation_enabled`** 如果标签更改为支配主体，则撤销对对象的访问。（默认：0）。

## 参见

[mac(4)](mac.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [maclabel(7)](../man7/maclabel.7.md), [mac(9)](../man9/mac.9.md)

## 历史

`mac_biba` 策略模块首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分贡献给 FreeBSD 项目。
