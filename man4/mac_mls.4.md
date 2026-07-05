# mac_mls.4

`mac_mls` — 多级安全机密性策略

## 名称

`mac_mls`

## 概要

要将 MLS 编译进内核，请在内核配置文件中加入以下行：

> options MAC
> options MAC_MLS

或者，要在引导时加载 MLS 模块，请在内核配置文件中加入以下行：

> options MAC

并在 loader.conf(5) 中加入：

```sh
mac_mls_load="YES"
```

## 描述

`mac_mls` 策略模块实现多级安全（Multi-Level Security，MLS）模型，通过严格的信息流策略基于主体和对象的机密性控制它们之间的访问。系统中每个主体和对象都有一个与之关联的 MLS 标签；每个主体的 MLS 标签包含其许可级别信息，每个对象的 MLS 标签包含其分类信息。

在 MLS 中，所有系统主体和对象都被分配机密性标签，由一个敏感级别和零个或多个分隔组成。这些标签元素共同允许所有标签置于偏序关系中，机密性保护基于描述该次序的支配运算符。敏感级别表示为 0 到 65535 之间的值，值越高反映的敏感级别越高。分隔字段表示为最多 256 个组件的集合，编号从 1 到 256。一个完整的标签由敏感级别和分隔元素共同组成。

对于普通标签，支配定义为：一个标签具有大于或等于的活动敏感级别，并且至少具有与其比较标签相同的所有分隔。在标签比较方面，“`lower`”定义为被比较标签所支配，“`higher`”定义为支配比较标签，“`equal`”定义为两个标签都能满足对彼此的支配要求。

存在三个特殊标签值：

| **标签** | **比较** |
| -------- | -------- |
| `mls/low` | 被所有其他标签支配 |
| `mls/equal` | 等于所有其他标签 |
| `mls/high` | 支配所有其他标签 |

“`mls/equal`”标签可应用于不希望强制执行 MLS 安全策略的主体和对象。

MLS 模型强制执行以下基本限制：

- 如果主体的许可级别低于其试图观察的对象的许可级别，主体不得观察另一主体的进程。
- 主体不得在没有适当许可的情况下读取、写入或以其他方式观察对象（例如，主体不得观察分类标签支配其自身许可标签的对象）。
- 主体不得写入分类级别低于其自身许可级别的对象。
- 如果主体的许可级别等于对象的分类级别，主体可对对象进行读写，如同 MLS 保护未生效。

这些规则防止低许可主体获取超出其许可级别的分类信息以保护分类信息的机密性，防止高许可主体写入低分类对象以防止信息意外或恶意泄露，并防止低许可主体完全观察高许可主体。在传统可信操作系统中，MLS 机密性模型与 Biba 完整性模型（mac_biba）协同使用，以保护可信代码库（TCB）。

### 标签格式

几乎所有系统对象都标记有一个有效的活动标签元素，反映对象的分类或对象所含数据的分类。通常，对象标签以如下形式表示：

> `mls /` `grade : compartments`

例如：

```sh
mls/10:2+3+6
mls/low
```

主体标签由三个标签元素组成：一个有效（活动）标签，以及一个可用标签范围。该范围使用两个有序的 MLS 标签元素表示，设置于进程上时，允许进程将活动标签更改为完整性大于或等于范围低端、小于或等于范围高端的任何标签。通常，主体标签以如下形式表示：

> `mls /` `effectivegrade : effectivecompartments ( lograde : locompartments` -

> `higrade : hicompartments`)

例如：

```sh
mls/10:2+3+6(5:2+3-20:2+3+4+5+6)
mls/high(low-high)
```

有效的范围标签必须满足以下元素要求：

> `rangehigh` [>=] `effective` [>=] `rangelow`

当前存在一类带范围的对象，即网络接口。对于网络接口，有效标签元素引用通过该接口接收的数据包的默认标签，范围表示通过该接口传输的可接受数据包标签范围。

### 运行时配置

以下 [sysctl(8)](../man8/sysctl.8.md) MIB 可用于微调此 MAC 策略的执行。

**`security.mac.mls.enabled`** 启用 MLS 机密性策略的执行。（默认：1）。

**`security.mac.mls.ptys_equal`** 创建时将 [pty(4)](pty.4.md) 标记为“`mls/equal`”。（默认：0）。

**`security.mac.mls.revocation_enabled`** 如果标签更改为比主体更敏感的级别，则撤销对对象的访问。（默认：0）。

## 实现说明

目前，`mac_mls` 策略依赖超级用户状态（suser(9)）来更改网络接口 MLS 标签。这最终会消失，但目前是一个隐患，可能允许超级用户绕过 MLS 保护。

## 参见

[mac(4)](mac.4.md), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_none(4)](mac_none.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_test(4)](mac_test.4.md), [maclabel(7)](../man7/maclabel.7.md), [mac(9)](../man9/mac.9.md)

## 历史

`mac_mls` 策略模块首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Laboratories（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分贡献给 FreeBSD 项目。

## 缺陷

虽然 MAC 框架设计旨在支持对 root 用户的限制，但并非所有攻击渠道目前都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防范恶意的特权用户。
