# mlx5ib.4

`mlx5ib` — 基于 Mellanox ConnectX-4 和 ConnectX-4 LX 的 100Gb、50Gb、40Gb、25Gb 和 10Gb 网络适配器驱动

## 名称

`mlx5ib`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> options COMPAT_LINUXKPI
> device mlx5
> device mlx5ib

`要在运行时以模块形式加载此驱动，请以 root 身份执行以下命令：`

```sh
kldload mlx5ib
```

`要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
mlx5ib_load="YES"
```

## 描述

`mlx5ib` 驱动为基于 ConnectX-4 和 ConnectX-4 LX 的 PCI Express 网络适配器提供对 InfiniBand 以及聚合以太网上的远程 DMA（RoCE）的支持。有关硬件需求的进一步信息和问题，参见 `http://www.mellanox.com/`。

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`mlx5ib` 驱动支持 100Gb、50Gb、40Gb、25Gb 和 10Gb 网络适配器。ConnectX-4 支持：10/20/25/40/50/56/100Gb/s 速率。ConnectX-4 LX 支持：10/25/40/50Gb/s 速率（且功耗更低）：

- Mellanox MCX455A-ECAT
- Mellanox MCX456A-ECAT
- Mellanox MCX415A-CCAT
- Mellanox MCX416A-CCAT
- Mellanox MCX455A-FCAT
- Mellanox MCX456A-FCAT
- Mellanox MCX415A-BCAT
- Mellanox MCX416A-BCAT
- Mellanox MCX4131A-GCAT
- Mellanox MCX4131A-BCAT
- Mellanox MCX4121A-ACAT
- Mellanox MCX4111A-ACAT
- Mellanox MCX4121A-XCAT
- Mellanox MCX4111A-XCAT

## 支持

有关一般信息和支持，请访问 Mellanox 支持网站：`http://www.mellanox.com/`。

如果在使用本驱动和受支持的适配器时发现问题，请将与问题相关的所有具体信息通过电子邮件发送至 <freebsd-drivers@mellanox.com>。

## 参见

[mlx5en(4)](mlx5en.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`mlx5ib` 设备驱动首次出现于 FreeBSD 12.0。

## 作者

`mlx5ib` 驱动由 Mellanox Technologies <freebsd-drivers@mellanox.com> 编写。
