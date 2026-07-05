# intpm.4

`intpm` — Intel PIIX4 电源管理控制器驱动

## 名称

`intpm`

## 概要

`device pci device smbus device smb device intpm`

## 描述

`intpm` 驱动提供对 Intel PIIX4 兼容电源管理控制器的访问。目前仅实现了 [smbus(4)](smbus.4.md) 控制器功能。

## 硬件

`intpm` 驱动支持以下芯片组：

- Intel 82371AB/82443MX
- ATI IXP400
- AMD SB600/7x0/8x0/9x0 南桥
- AMD Axx/Hudson/Bolton FCH
- 集成于 Family 15h Models 60h-6Fh、70h-7Fh 处理器中的 AMD FCH
- 集成于 Family 16h Models 00h-0Fh、30h-3Fh 处理器中的 AMD FCH

## 参见

[amdpm(4)](amdpm.4.md), [amdsmb(4)](amdsmb.4.md), [ichsmb(4)](ichsmb.4.md), [smb(4)](smb.4.md), [smbus(4)](smbus.4.md)

## 历史

`intpm` 驱动首次出现于 FreeBSD 3.4。

## 作者

本手册页由 Takanori Watanabe <takawata@shidahara1.planet.sci.kobe-u.ac.jp> 编写。

## 缺陷

此设备独占使用 IRQ 9。要使用此设备，应在 BIOS 配置中启用 ACPI 功能，否则 PnP 机制可能为 PnP ISA 卡分配冲突的 IRQ。此外，不要将 IRQ 9 用于非 PnP ISA 卡。
