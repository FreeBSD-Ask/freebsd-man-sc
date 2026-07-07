# pflow(4)

`pflow` — 用于 pflow 数据导出的内核接口

## 名称

`pflow`

## 概要

`pseudo-device pflow`

## 描述

`pflow` 子系统使用 [udp(4)](udp.4.md) 包从内核导出 `pflow` 计费数据。`pflow` 兼容 netflow 版本 5 和 IPFIX (10)。数据从 [pf(4)](pf.4.md) 状态表中提取。

可在运行时使用 `pflowctl``N` `-c` 命令创建多个 `pflow` 接口。每个接口必须配置流接收者 IP 地址和流接收者端口号。

只有由标记为 `pflow` 关键字的规则创建的状态才会被 `pflow` 导出。

`pflow` 会尝试在一个 UDP 包中导出多个 `pflow` 记录，但不会将记录保留超过 30 秒。

在此接口上看到的每个包都有一个头和可变数量的流。头指示协议的版本、包中的流数、唯一的序列号、系统时间以及引擎 ID 和类型。头和流结构定义于

`#include <net/pflow.h>`

`pflow` 的源地址和目的地址由 pflowctl(8) 控制。`src` 是 UDP 包的发送者 IP 地址，可用于在 `pflow` 收集器上标识数据源。`dst` 定义收集器 IP 地址和端口。必须定义 `dst` IP 地址和端口才能启用流导出。

例如，以下命令将 10.0.0.1 设为源，10.0.0.2:1234 设为目的：

```sh
# pflowctl -s pflow0 src 10.0.0.1 dst 10.0.0.2:1234
```

通过以下命令将协议设为 IPFIX：

```sh
# pflowctl -s pflow0 proto 10
```

## 参见

[netintro(4)](netintro.4.md), [pf(4)](pf.4.md), [udp(4)](udp.4.md), [pf.conf(5)](../man5/pf.conf.5.md), pflowctl(8), tcpdump(8)

## 标准

> B. Claise, "Specification of the IP Flow Information Export (IPFIX) Protocol for the Exchange of IP Traffic Flow Information", January 2008.

## 历史

`pflow` 设备首次出现于 OpenBSD 4.5，并导入到 FreeBSD 15.0。

## 缺陷

由 [pfsync(4)](pfsync.4.md) 创建的状态可能具有早于机器启动时间的创建或过期时间。在这种情况下，`pflow` 会假定这些流是在机器启动时创建或过期的。

IPFIX 实现不完整：不支持所需的传输协议 SCTP。也不支持通过 TCP 和受 DTLS 保护的流导出传输。
