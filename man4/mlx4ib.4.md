# mlx4ib.4

`mlx4ib` — Mellanox ConnectX-3 10GbE/40GbE 网络适配器驱动

## 名称

`mlx4ib`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> options COMPAT_LINUXKPI
> device mlx4
> device mlx4ib

`要在运行时以模块形式加载此驱动，请以 root 身份执行以下命令：`

```sh
kldload mlx4ib
```

`要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
mlx4ib_load="YES"
```

## 描述

带有 Virtual Protocol Interconnect（VPI）的 Mellanox ConnectX 适配卡为企业数据中心、高性能计算和嵌入式环境提供了性能最高且最灵活的互联解决方案。集群数据库、并行化应用、事务服务以及高性能嵌入式 I/O 应用将获得显著的性能提升，从而缩短完成时间并降低每次操作的成本。

## 硬件

`mlx4ib` 驱动支持以下网络适配器：

- Mellanox ConnectX-2（IB）
- Mellanox ConnectX-3（IB）

## 支持

有关一般信息和支持，请访问 Mellanox 支持网站：`http://www.mellanox.com/`。

如果在使用本驱动和受支持的网络适配器时发现问题，请将相关具体信息通过电子邮件发送至 <freebsd-drivers@mellanox.com>。

## 参见

[mlx4en(4)](mlx4en.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`mlx4ib` 设备驱动首次出现于 FreeBSD 9.0。

## 作者

`mlx4ib` 驱动由 Mellanox Technologies <freebsd-drivers@mellanox.com> 编写。
