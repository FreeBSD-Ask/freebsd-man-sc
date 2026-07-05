# devinfo.8

`devinfo` — 打印系统设备配置信息

## 名称

`devinfo`

## 概要

`devinfo [-rv]`

`devinfo -p dev [-v]`

`devinfo -u [-v]`

## 描述

不带任何参数时，`devinfo` 工具会显示系统中可用设备的层次结构，从“nexus”设备开始。

接受以下选项：

**`-p`** `dev` 显示 `dev` 回溯到设备树根的路径。`dev` 可以是设备名称、ACPI 句柄的绝对路径（必须以 **\\** 开头）或 PCI 选择器（**pci**`domain`:`bus`:`slot`:`function` 或 **pci**`bus`:`slot`:`function`）。如果指定了 `-v`，每个设备单独占一行输出，包括设备名称和额外的详细信息；否则输出以空格分隔的设备名称列表。

**`-r`** 使硬件资源信息（如 IRQ、I/O 端口、I/O 内存地址）也列在已预留这些资源的每个设备下。

**`-u`** 显示与 `-r` 相同的信息，但按资源类型而非设备排序，便于按使用情况查看系统资源集合和可用资源。例如，它会将所有 IRQ 使用者列在一起。

**`-v`** 显示驱动程序树中的所有设备，而不仅仅是已附加或忙碌的设备。不带此标志时，只报告已附加的设备。此标志还显示每个设备的详细信息。

## 参见

[systat(1)](../man1/systat.1.md), devinfo(3), [devctl(8)](devctl.8.md), [iostat(8)](iostat.8.md), pciconf(8), [vmstat(8)](vmstat.8.md), [devclass(9)](../man9/devclass.9.md), [device(9)](../man9/device.9.md)

## 历史

`devinfo` 工具出现于 FreeBSD 5.0。

## 作者

Mike Smith <msmith@FreeBSD.org>
