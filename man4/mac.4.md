# mac.4

`mac` — 强制访问控制

## 名称

`mac`

## 概要

`options MAC`

## 描述

### 简介

强制访问控制（Mandatory Access Control，MAC）框架通过提供可加载的安全策略架构，使管理员能够精细地控制系统安全。重要的是，由于其性质，MAC 安全策略只能相对于彼此和基本系统策略限制访问；它们无法覆盖传统的 UNIX 安全规定，如文件权限和超级用户检查。

目前，FreeBSD 附带以下 MAC 策略模块：

| **名称** | **描述** | **标签化** | **加载时机** |
| -------- | -------- | ---------- | ------------ |
| [mac_biba(4)](mac_biba.4.md) | Biba 完整性策略 | 是 | 仅引导时 |
| [mac_bsdextended(4)](mac_bsdextended.4.md) | 文件系统防火墙 | 否 | 任意时刻 |
| [mac_ddb(4)](mac_ddb.4.md) | ddb(4) 接口限制 | 否 | 任意时刻 |
| [mac_do(4)](mac_do.4.md) | 更改命令的 uid/gid | 否 | 任意时刻 |
| [mac_ifoff(4)](mac_ifoff.4.md) | 接口静默 | 否 | 任意时刻 |
| [mac_ipacl(4)](mac_ipacl.4.md) | IP 地址访问控制 | 否 | 任意时刻 |
| [mac_lomac(4)](mac_lomac.4.md) | 低水位 MAC 策略 | 是 | 仅引导时 |
| [mac_mls(4)](mac_mls.4.md) | 机密性策略 | 是 | 仅引导时 |
| [mac_ntpd(4)](mac_ntpd.4.md) | 非 root NTP 守护进程策略 | 否 | 任意时刻 |
| [mac_partition(4)](mac_partition.4.md) | 进程分区策略 | 是 | 任意时刻 |
| [mac_portacl(4)](mac_portacl.4.md) | 端口 bind(2) 访问控制 | 否 | 任意时刻 |
| [mac_priority(4)](mac_priority.4.md) | 调度优先级策略 | 否 | 任意时刻 |
| [mac_seeotheruids(4)](mac_seeotheruids.4.md) | 查看其他 UID 策略 | 否 | 任意时刻 |
| [mac_test(4)](mac_test.4.md) | MAC 测试策略 | 否 | 任意时刻 |

### MAC 标签

每个系统主体（进程、套接字等）和每个系统对象（文件系统对象、jail、套接字等）都可以携带一个 MAC 标签。MAC 标签包含任意格式的数据，在进行给定操作的访问控制决策时会考虑这些数据。系统主体和对象上的大多数 MAC 标签可由系统管理员直接或间接修改。给定策略标签的格式可能因被标记的对象或主体类型而异。有关 MAC 标签格式的更多信息，请参见 [maclabel(7)](../man7/maclabel.7.md) 手册页。

### UFS2 文件系统的 MAC 支持

默认情况下，文件系统对带标签 MAC 策略的执行依赖于单个文件系统标签（参见 Sx MAC 标签），以便为特定文件系统中的所有文件做出访问控制决策。对于某些策略，此配置可能无法让管理员充分利用各项功能。要为特定文件系统启用按文件单独标记的支持，必须在文件系统上启用“multilabel”标志。要设置“multilabel”标志，请切换到单用户模式并卸载文件系统，然后执行以下命令：

```sh
tunefs -l enable `filesystem`
```

其中 `filesystem` 可以是挂载点（在 [fstab(5)](../man5/fstab.5.md) 中），也可以是对应于要启用 multilabel 支持的文件系统的特殊文件（在 `/dev` 中）。

### 策略执行

策略执行分为系统的以下几个方面：

****文件系统** 文件系统挂载、修改目录、修改文件等。

****Jail**** 创建、修改、删除和附加到 jail

****KLD**** 加载、卸载和检索已加载内核模块的统计信息

****网络**** 网络接口、[bpf(4)](bpf.4.md)、数据包交付和传输、接口配置（ioctl、[ifconfig(8)](../man8/ifconfig.8.md)）

****管道**** pipe(2) 对象的创建和操作

****进程**** 调试（如 ktrace(2)、进程可见性（[ps(1)](../man1/ps.1.md)）、进程执行（execve(2)）、信号（kill(2)））

****套接字**** socket(2) 对象的创建和操作

****系统**** 内核环境（[kenv(1)](../man1/kenv.1.md)）、系统记账（acct(2)）、reboot(2)、settimeofday(2)、swapon(2)、sysctl(3)、nfsd(8) 相关操作

****VM**** mmap(2) 映射的文件

### 设置 MAC 标签

从命令行来看，每种类型的系统对象都有其自己的设置和修改 MAC 策略标签的方式。

| **主体/对象** | **工具** |
| ------------- | -------- |
| 文件系统对象 | setfmac(8)、setfsmac(8) |
| Jail | [jail(8)](../man8/jail.8.md) |
| 网络接口 | [ifconfig(8)](../man8/ifconfig.8.md) |
| TTY（按登录类） | login.conf(5) |
| 用户（按登录类） | login.conf(5) |

此外，[su(1)](../man1/su.1.md) 和 setpmac(8) 工具可用于以与 shell 当前标签不同的进程标签运行命令。

### MAC 编程

MAC 安全执行本身对应用程序是透明的，但某些程序可能需要注意各种系统调用返回的额外 errno(2)。

检索、处理和设置策略标签的接口记录在 mac(3) 手册页中。

## 参见

mac(3), [mac_biba(4)](mac_biba.4.md), [mac_bsdextended(4)](mac_bsdextended.4.md), [mac_ddb(4)](mac_ddb.4.md), [mac_do(4)](mac_do.4.md), [mac_ifoff(4)](mac_ifoff.4.md), [mac_ipacl(4)](mac_ipacl.4.md), [mac_lomac(4)](mac_lomac.4.md), [mac_mls(4)](mac_mls.4.md), [mac_none(4)](mac_none.4.md), [mac_ntpd(4)](mac_ntpd.4.md), [mac_partition(4)](mac_partition.4.md), [mac_portacl(4)](mac_portacl.4.md), [mac_priority(4)](mac_priority.4.md), [mac_seeotheruids(4)](mac_seeotheruids.4.md), [mac_stub(4)](mac_stub.4.md), [mac_test(4)](mac_test.4.md), login.conf(5), [maclabel(7)](../man7/maclabel.7.md), [jail(8)](../man8/jail.8.md), getfmac(8), getpmac(8), setfmac(8), setpmac(8), [mac(9)](../man9/mac.9.md)

> “强制访问控制”，*The FreeBSD Handbook*。

## 历史

`mac` 实现首次出现于 FreeBSD 5.0，由 TrustedBSD 项目开发。

## 作者

本软件由 Network Associates Labs（Network Associates Inc. 的安全研究部门）在 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）下，作为 DARPA CHATS 研究计划的一部分贡献给 FreeBSD 项目。

## 缺陷

虽然 MAC 框架设计旨在支持对 root 用户的限制，但并非所有攻击渠道目前都受到入口点检查的保护。因此，不应单独依赖 MAC 框架策略来防范恶意的特权用户。
