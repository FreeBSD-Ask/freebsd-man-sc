# mlx5en(4)

`mlx5en` — 基于 NVIDIA Mellanox ConnectX-4/5/6 [Dx/Ex/Lx] 的 200Gb、100Gb、50Gb、40Gb、25Gb 和 10Gb 以太网适配器驱动

## 名称

`mlx5en`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> options COMPAT_LINUXKPI
> options RATELIMIT
> options KERN_TLS
> device xz
> device mlxfw
> device firmware
> device mlx5
> device mlx5en

`要在运行时以模块形式加载此驱动，请以 root 身份执行以下命令：`

```sh
kldload mlx5en
```

`要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
mlx5en_load="YES"
```

## 描述

`mlx5en` 驱动为基于 ConnectX-4/5/6（Dx、Ex 和 Lx 变体）的 PCI Express 以太网适配器提供支持。该驱动支持 Jumbo Frames、发送和接收校验和卸载、TCP 分段卸载（TSO）、大接收卸载（LRO）、硬件大接收卸载（HW LRO）、VLAN 标签插入和提取、VLAN 校验和卸载、VLAN TSO、硬件速率限制（TXRTLMT）、用于接收和发送的无状态 VxLAN 硬件卸载、用于发送的硬件 TLS 卸载、接收端引导（RSS）以及 [numa(4)](numa.4.md) 感知。

网络接口名为 `mce<N>`，对应于一个 PCI 功能 `mlx_core<N>`，其中 `<N>` 是从零开始的数字。每个 PCI 功能最多对应一个网络接口。

有关硬件需求的进一步信息和问题，参见 `https://www.mellanox.com`。

## 硬件

`mlx5en` 驱动支持 200Gb、100Gb、50Gb、40Gb、25Gb 和 10Gb 以太网适配器。

- ConnectX-6 支持 10/20/25/40/50/56/100Gb/s 和 200Gb/s 速率。
- ConnectX-5 支持 10/20/25/40/50/56/100Gb/s 速率。
- ConnectX-4 支持 10/20/25/40/50/56/100Gb/s 速率。
- ConnectX-4 LX 支持 10/25/40/50Gb/s 速率，且功耗更低。

## 配置

`mlx5en` 网络接口使用 [ifconfig(8)](../man8/ifconfig.8.md) 以及位于 `dev.mce.<N>` 的 [sysctl(8)](../man8/sysctl.8.md) 树进行配置。所有可配置条目同时也是可调参数，可直接放入 loader.conf(5) 以实现持久化配置。

## 支持

有关一般信息和支持，请访问 NVIDIA Mellanox 网络支持网站：`https://www.mellanox.com`。

如果在使用本驱动和受支持的适配器时发现问题，请将与问题相关的所有具体信息通过电子邮件发送至 <nbu-freebsd-drivers@nvidia.com>。

## 参见

[ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`mlx5en` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`mlx5en` 驱动由 NVIDIA Mellanox networking <nbu-freebsd-drivers@nvidia.com> 编写。
