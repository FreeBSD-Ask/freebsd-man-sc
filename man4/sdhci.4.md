# sdhci(4)

`sdhci` — PCI SD 主机控制器桥驱动

## 名称

`sdhci`

## 概要

`要将此驱动编译进内核，请将以下行添加到你的内核配置文件中：`

> device mmc
> device mmcsd
> device sdhci

`或者，要在引导时以模块形式加载此驱动，请将以下行添加到 loader.conf(5) 中：`

```sh
mmc_load="YES"
mmcsd_load="YES"
sdhci_load="YES"
```

## 描述

`sdhci` 驱动支持符合 SD 主机控制器规范、class 为 8 且 subclass 为 5 的 PCI 设备。该驱动每个控制器最多支持六个高速 4 位 MMC/SD 插槽。驱动在卡片插入时将 mmc 总线附加到相应插槽，并在卡片移除时分离。

## 硬件

`sdhci` 驱动支持 SD 主机控制器规范。通过 PCI 总线附加时，控制器会自动配置。许多 SoC 芯片提供直接映射到 I/O 内存的 SDHCI 控制器。对于此类芯片，可使用由你的主板厂商提供的 [fdt(4)](fdt.4.md) 或 [acpi(4)](acpi.4.md) 方法配置控制器。

与大多数支持通用标准的其他驱动不同，`sdhci` 需要大量 quirk 来应对硬件缺陷、专有寄存器以及定义不清的电源管理。虽然来自 Intel、Xilinx、Rockchip、Freescale、Ricoh 和 TI 的许多芯片组已有这些条目，但使用某些控制器时可能出现性能不佳。通过 [fdt(4)](fdt.4.md) 或 [acpi(4)](acpi.4.md) 配置设备时，通常最需要 quirk 和自定义配置。

## 参见

[mmc(4)](mmc.4.md), [mmcsd(4)](mmcsd.4.md)

> "SD Specifications, Part 2, SD Host Controller, Simplified Specification"。

## 作者

Alexander Motin <mav@FreeBSD.org>
