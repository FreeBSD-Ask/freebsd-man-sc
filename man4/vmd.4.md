# vmd.4

`vmd` — Intel 卷管理设备驱动

## 名称

`vmd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device vmd

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
vmd_load="YES"
```

## 描述

此驱动附加到 Intel VMD 设备，将其表示为 PCI 到 PCI 桥，并通过新的 PCI 域提供对子 PCI 设备的访问。Intel VMD 由 Intel 的 VROC（Virtual RAID on chip）用于管理 NVMe 驱动器。

## 加载器可调参数

以下可调参数可通过 [loader(8)](../man8/loader.8.md) 或 [sysctl(8)](../man8/sysctl.8.md) 设置：

**`hw.vmd.bypass_msi`** 默认情况下，所有 VMD 设备会将子设备的 MSI/MSI-X 中断重新映射到自身。这创造了额外的隔离，但也由于共享等原因使事情复杂化。幸运的是，某些 VMD 设备可以绕过重新映射。默认值为 1。

**`hw.vmd.max_msi`** 限制每个子设备允许的消息信号中断（MSI）向量数。VMD 无法区分同一设备的 MSI 向量，因此多于一个并无益处，除非特定设备驱动有此要求。默认值为 1。

**`hw.vmd.max_msix`** 限制每个子设备允许的扩展消息信号中断（MSI-X）向量数。VMD 用于映射子设备中断的中断向量数量有限，因此为避免/减少共享，需对子设备/驱动进行限制。默认值为 3。

## 参见

graid(8)

## 历史

`vmd` 驱动最早出现于 FreeBSD 13.0。
