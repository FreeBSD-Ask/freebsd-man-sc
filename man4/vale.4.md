# vale.4

`vale` — 使用 netmap API 的极快虚拟局域以太网

## 名称

`vale`

## 概要

`device netmap`

## 描述

`vale` 是 [netmap(4)](netmap.4.md) 模块的一项功能，实现了多个虚拟交换机，可用于互连 netmap 客户端，包括流量源和接收器、数据包转发器、用户空间防火墙等。

`vale` 完全以软件实现，速度极快。在现代机器上，使用小帧时每个核心每秒可移动近 2000 万个数据包（Mpps），使用 1500 字节帧时约为 70 Gbit/s。

## 操作

`vale` 在客户端使用 [netmap(4)](netmap.4.md) API 连接到它时动态创建交换机和端口。

`vale` 端口命名为 `valeSSS:PPP`，其中 `vale` 是前缀，表示这是一个 VALE 交换机而非标准接口，`SSS` 表示特定交换机（冒号是分隔符），`PPP` 表示交换机内的端口。SSS 和 PPP 的形式均为 [0-9a-zA-Z_]+ ，字符串不能超过 IFNAMSIZ 个字符，且 PPP 不能是任何现有操作系统网络接口的名称。

关于 API 的详细信息，请参见 [netmap(4)](netmap.4.md)。

### 限制

`vale` 目前每个交换机最多支持 254 个端口。交换机的最大数量由 max_bridges sysctl 变量提供。

## SYSCTL 变量

影响 `vale` 网桥的 sysctl 变量列表，请参见 [netmap(4)](netmap.4.md)。

## 实例

创建一个交换机，一个端口连接流量发生器，另一个端口连接启用 netmap 的 tcpdump 实例：

```sh
tcpdump -ni valea:1 &
pkt-gen  -i valea:0 -f tx &
```

创建两个交换机，每个交换机在不同端口上连接两台 qemu 机器。

```sh
qemu -net nic -net netmap,ifname=vale1:a ... &
qemu -net nic -net netmap,ifname=vale1:b ... &
qemu -net nic -net netmap,ifname=vale2:c ... &
qemu -net nic -net netmap,ifname=vale2:d ... &
```

## 参见

[netmap(4)](netmap.4.md), valectl(8)

Luigi Rizzo, Giuseppe Lettieri: VALE, a switched ethernet for virtual machines, June 2012, http://info.iet.unipi.it/~luigi/vale/

## 作者

`vale` 交换机由 Luigi Rizzo 和 Giuseppe Lettieri 于 2012 年在 Universita` di Pisa 设计和实现。

`vale` 由欧洲委员会在 FP7 项目 CHANGE（257422）和 OPENLAB（287581）中资助。
