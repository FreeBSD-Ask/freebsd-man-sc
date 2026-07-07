# maclabel(7)

`maclabel` — 强制访问控制（MAC）标签格式

## 名称

`maclabel`

## 描述

如果在内核中启用了强制访问控制（MAC），那么除了传统的凭据外，每个主体（通常是用户或套接字）和对象（文件系统对象、套接字等）都会被赋予一个 *MAC 标签*。MAC 标签指定了 MAC 安全策略对主体/对象实施访问控制所需的特定于主体或特定于对象的信息。

MAC 标签的格式定义如下：

> `policy1` / `qualifier1 , policy2` / `qualifier2`, ...

MAC 标签由一个策略名称、一个正斜杠和该主体或对象的限定符组成，可选地后跟一个逗号和一个或多个额外的策略标签。例如：

```sh
biba/low(low-low)
biba/high(low-high),mls/equal(equal-equal),partition/0
```

## 参见

mac(3), posix1e(3), [mac_biba(4)](../man4/mac_biba.4.md), [mac_bsdextended(4)](../man4/mac_bsdextended.4.md), [mac_ifoff(4)](../man4/mac_ifoff.4.md), [mac_mls(4)](../man4/mac_mls.4.md), [mac_none(4)](../man4/mac_none.4.md), [mac_partition(4)](../man4/mac_partition.4.md), [mac_seeotheruids(4)](../man4/mac_seeotheruids.4.md), [mac_test(4)](../man4/mac_test.4.md), login.conf(5), getfmac(8), getpmac(8), [ifconfig(8)](../man8/ifconfig.8.md), setfmac(8), setpmac(8), [mac(9)](../man9/mac.9.md)

## 历史

MAC 首次出现于 FreeBSD 5.0。

## 作者

该软件由 NAI Labs（Network Associates Inc. 的安全研究部门）根据 DARPA/SPAWAR 合同 N66001-01-C-8035（“CBOSS”）作为 DARPA CHATS 研究计划的一部分贡献给 FreeBSD 项目。
