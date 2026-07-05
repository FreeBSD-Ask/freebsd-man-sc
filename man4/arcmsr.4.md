# arcmsr.4

`arcmsr` — Areca RAID 控制器驱动

## 名称

`arcmsr`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device pci
> device scbus
> device da
> device arcmsr

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
arcmsr_load="YES"
```

## 描述

`arcmsr` 驱动为 Areca ARC-11xx、ARC-12xx、ARC-13xx、ARC-16xx 和 ARC-18xx 系列 SAS 及 SATA RAID 控制器提供支持。这些控制器具有 RAID-0、1、3、5、6 和 10 以及 JBOD 加速功能，最多支持 16 个 SATA 驱动器。还支持 RAID 级别和条带级别迁移、在线容量扩展、热插拔、自动故障转移和重建以及 SMART。通过 SCSI CAM `/dev/da?` 设备节点访问阵列。还通过 `/dev/arcmsr?` 设备节点提供管理接口。Areca 提供 i386 和 amd64 的管理工具。

## 硬件

`arcmsr` 驱动支持以下 Areca PCI-X/PCIe SATA/SAS/NVMe RAID 主机适配器：

- ARC-1110
- ARC-1120
- ARC-1130
- ARC-1160
- ARC-1170
- ARC-1110ML
- ARC-1120ML
- ARC-1130ML
- ARC-1160ML
- ARC-1200
- ARC-1201
- ARC-1203
- ARC-1210
- ARC-1212
- ARC-1213
- ARC-1214
- ARC-1216
- ARC-1220
- ARC-1222
- ARC-1223
- ARC-1224
- ARC-1226
- ARC-1230
- ARC-1231
- ARC-1260
- ARC-1261
- ARC-1270
- ARC-1280
- ARC-1210ML
- ARC-1220ML
- ARC-1231ML
- ARC-1261ML
- ARC-1280ML
- ARC-1380
- ARC-1381
- ARC-1680
- ARC-1681
- ARC-1880
- ARC-1882
- ARC-1883
- ARC-1884
- ARC-1886

## 文件

**`/dev/da?`** 阵列块设备

**`/dev/arcmsr?`** 管理接口

## 参见

[da(4)](da.4.md), scbus(4)

## 历史

`arcmsr` 驱动首次出现于 FreeBSD 5.4。

## 作者

该驱动由 Erich Chen <erich@areca.com.tw> 编写。

## 缺陷

该驱动已在 i386 和 amd64 上测试。它可能需要额外的工作才能在大端架构上运行。
