# ng_checksum(4)

`ng_checksum` — 重建 IP 校验和的节点类型

## 名称

`ng_checksum`

## 概要

`#include <netgraph/ng_checksum.h>`

## 描述

`checksum` 节点可以计算或为硬件计算准备 IPv4 头部、TCP 和 UDP 校验和。

## 钩子

此节点类型有两个钩子：

**`in`** 在此钩子上接收的数据包按配置中指定的设置处理，然后转发到 `out` 钩子（如果存在且已连接）。否则它们被反射回 `in` 钩子。

**`out`** 在此钩子上接收的数据包不做任何更改转发到 `in` 钩子。

## 控制消息

此节点类型支持通用控制消息，外加以下消息：

`#include <net/bpf.h>`

```sh
struct ng_checksum_config {
	uint64_t	csum_flags;
	uint64_t	csum_offload;
};
```

**`NGM_CHECKSUM_SETDLT`** (`setdlt`) 设置 `in` 钩子上的数据链路类型。目前支持的类型有 `DLT_RAW`（原始 IP 数据报）和 `DLT_EN10MB`（以太网）。DLT_ 定义可在头文件中找到。当前使用的值为 `DLT_EN10MB` = 1 和 `DLT_RAW` = 12。

**`NGM_CHECKSUM_GETDLT`** (`getdlt`) 此控制消息获取 `in` 钩子上的数据链路类型。

**`NGM_CHECKSUM_SETCONFIG`** (`setconfig`) 设置节点配置。必须提供以下 `struct ng_checksum_config` 作为参数：`csum_flags` 可设置为 CSUM_IP、CSUM_TCP、CSUM_UDP、CSUM_TCP_IPV6 和 CSUM_UDP_IPV6 的任意组合（其他值被忽略），用于指示节点计算相应的校验和。`csum_offload` 值可设置为 CSUM_IP、CSUM_TCP、CSUM_UDP、CSUM_TCP_IPV6 和 CSUM_UDP_IPV6 的任意组合（其他值被忽略），用于指示节点应请求硬件计算哪些校验和。节点还考虑 mbuf 上已标记的 CSUM_IP、CSUM_TCP、CSUM_UDP、CSUM_TCP_IPV6 和 CSUM_UDP_IPV6 的任意组合。

**`NGM_CHECKSUM_GETCONFIG`** (`getconfig`) 此控制消息获取作为 `struct ng_checksum_config` 返回的当前节点配置。

**`NGM_CHECKSUM_GET_STATS`** (`getstats`) 返回作为 `struct ng_checksum_stats` 的节点统计信息。

**`NGM_CHECKSUM_CLR_STATS`** (`clrstats`) 清除节点统计信息。

**`NGM_CHECKSUM_GETCLR_STATS`** (`getclrstats`) 此命令与 `NGM_CHECKSUM_GET_STATS` 相同，区别在于统计信息也会被原子性地清除。

## 关闭

此节点在收到 `NGM_SHUTDOWN` 控制消息时，或当所有钩子都已断开时关闭。

## 实例

ngctl(8) 脚本：

```sh
/usr/sbin/ngctl -f- <<-SEQ
	msg checksum-1: setdlt 1
	msg checksum-1: setconfig { csum_flags=0 csum_offload=6 }
SEQ
```

将数据链路类型设置为 `DLT_EN10MB`（以太网），不设置额外的校验和标志，并请求硬件计算 CSUM_IP_UDP|CSUM_IP_TCP。

## 参见

[netgraph(4)](netgraph.4.md), [ng_patch(4)](ng_patch.4.md), ngctl(8)

## 历史

`checksum` 节点类型实现于 FreeBSD 10.2，并首次提交于 FreeBSD 12.0。

## 作者

Dmitry Vagin <daemon.hammer@ya.ru>.
