# geom_linux_lvm.4

`geom_linux_lvm` — 基于 GEOM 的 Linux LVM 逻辑卷映射

## 名称

`geom_linux_lvm`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> options GEOM_LINUX_LVM

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
geom_linux_lvm_load="YES"
```

## 描述

`geom_linux_lvm` 框架提供将 Linux LVM 卷映射到 GEOM 提供程序的支持。`geom_linux_lvm` 目前支持在一个或多个物理磁盘上具有段的线性条带。解析器能够读取 LVM2 文本格式元数据，逻辑卷将被组装并使其在 **/dev/linux_lvm/** 下可用。元数据是只读的，无法分配或调整逻辑卷的大小。

## 实例

查看哪些 `geom_linux_lvm` 设备可用：

```sh
# geom linux_lvm list
Geom name: vg1
Providers:
1. Name: linux_lvm/vg1-home
   Mediasize: 4294967296 (4.0G)
   Sectorsize: 512
   Mode: r0w0e0
2. Name: linux_lvm/vg1-logs
   Mediasize: 4294967296 (4.0G)
   Sectorsize: 512
   Mode: r0w0e0
Consumers:
1. Name: ada0s1
   Mediasize: 80023716864 (75G)
   Sectorsize: 512
   Mode: r0w0e0
```

## 参见

GEOM(4), geom(8)

## 作者

`geom_linux_lvm` 驱动程序由 Andrew Thompson <thompsa@FreeBSD.org> 编写。
