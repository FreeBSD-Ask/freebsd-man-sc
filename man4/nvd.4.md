# nvd(4)

`nvd` — NVM Express 磁盘驱动

## 名称

`nvd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device nvme
> device nvd

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
nvme_load="YES"
nvd_load="YES"
```

## 描述

`nvd` 驱动将 NVM Express（NVMe）命名空间作为磁盘暴露给内核磁盘存储 API。它依赖 [nvme(4)](nvme.4.md) 驱动获取现有 NVMe 命名空间通知和提交 NVM I/O 命令。

`nvd` 驱动的设备节点格式为 /dev/nvdX，是可由 geom(8) 分区的 GEOM(4) 磁盘。注意，[nvme(4)](nvme.4.md) 驱动的设备节点不是 GEOM(4) 磁盘，无法分区。

## 硬件

`nvd` 驱动支持使用 NVMe 命名空间的 NVMe 存储设备。

## 配置

`nvd` 驱动为 NVMe 设备定义系统范围的最大删除大小。默认为 1GB。要选择不同的值，请在 loader.conf(5) 中设置以下可调参数：

```sh
hw.nvd.delete_max=<delete size in bytes>
```

## 参见

GEOM(4), [nda(4)](nda.4.md), [nvme(4)](nvme.4.md), geom(8), nvmecontrol(8), [disk(9)](../man9/disk.9.md)

## 历史

`nvd` 驱动首次出现于 FreeBSD 9.2。

## 作者

`nvd` 驱动由 Intel 开发，最初由 Jim Harris <jimharris@FreeBSD.org> 编写，并得到 EMC 的 Joe Golio 的贡献。

本手册页由 Jim Harris <jimharris@FreeBSD.org> 编写。
