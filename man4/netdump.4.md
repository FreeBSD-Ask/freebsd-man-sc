# netdump(4)

`netdump` — 将内核转储传输到远程服务器的协议

## 名称

`netdump`

## 概要

要将 netdump 客户端支持编译进内核，请在内核配置文件中加入以下行：

> options INET
> options DEBUGNET
> options NETDUMP

## 描述

netdump 是一种基于 UDP 的协议，用于将内核转储传输到远程主机。netdump 客户端是发生 panic 的内核，netdump 服务器是运行 `netdump` 守护进程的主机，该守护进程作为 `ports/ftp/netdumpd` 在 ports 中提供。`netdump` 客户端使用 dumpon(8) 实用程序或 [ddb(4)](ddb.4.md) 中的 `netdump` 命令进行配置。

`netdump` 客户端消息由固定大小的头部和可变大小的有效负载组成。头部包含消息类型、序列号、有效负载数据在内核转储中的偏移量以及有效负载数据的长度（不包括头部）。消息类型为 `HERALD , FINISHED , KDH , VMCORE` 和 `EKCD_KEY`。`netdump` 服务器消息具有固定大小，仅包含客户端消息的序列号。这些消息指示服务器已成功处理了具有相应序列号的客户端消息。所有客户端消息都以此方式确认。服务器消息始终发送到客户端的 20024 端口。

要启动 `netdump`，客户端向服务器的 20023 端口发送 `HERALD` 消息。客户端可以在其有效负载中包含相对路径，在这种情况下，`netdump` 服务器应尝试将转储保存到相对于其配置的转储目录的该路径。服务器将使用随机源端口确认 `HERALD`，客户端必须将所有后续消息发送到该端口。

`KDH , VMCORE` 和 `EKCD_KEY` 消息有效负载分别包含内核转储头、转储内容和转储加密密钥。消息头中的偏移量应视为相应文件中的查找偏移量。这些消息没有顺序要求。

通过向服务器发送 `FINISHED` 消息来完成 `netdump`。

以下网络驱动程序支持 netdump：[alc(4)](alc.4.md), [bge(4)](bge.4.md), [bnxt(4)](bnxt.4.md), [bxe(4)](bxe.4.md), [cxgb(4)](cxgb.4.md), [em(4)](em.4.md), igb(4), [ix(4)](ix.4.md), [ixl(4)](ixl.4.md), [mlx4en(4)](mlx4en.4.md), [mlx5en(4)](mlx5en.4.md), [re(4)](re.4.md), [vtnet(4)](vtnet.4.md)。

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 变量使用：

**`net.netdump.debug`** 控制调试消息的详细程度。调试消息默认禁用，但在故障排除或开发驱动程序支持时很有用。

**`net.netdump.path`** 指定相对于服务器转储目录的路径，用于存储转储。例如，如果 `netdump` 服务器配置为将转储存储在 **`/var/crash`** 中，路径“foo”将导致服务器尝试将来自客户端的转储存储在 **`/var/crash/foo`** 中。服务器不会自动创建相对目录。

**`net.netdump.polls`** 客户端在等待确认时会轮询已配置的网络接口。此参数控制放弃前的最大轮询尝试次数，通常会导致重传。每次轮询尝试耗时 0.5ms。

**`net.netdump.retries`** 客户端因缺乏确认而中止转储之前重传数据包的次数。在丢包较多的环境中，默认值可能太小。

**`net.netdump.arp_retries`** 客户端在放弃并中止转储之前尝试学习已配置网关或服务器 MAC 地址的次数。

## 参见

decryptcore(8), dumpon(8), savecore(8)

## 历史

`netdump` 客户端支持首次出现于 FreeBSD 12.0。

## 缺陷

仅支持 IPv4。

`netdump` 只能在内核发生 panic 后使用。
