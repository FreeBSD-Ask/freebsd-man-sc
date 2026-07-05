# ntb.4

`ntb` — 非透明桥接子系统

## 名称

`ntb`

## 概要

`要将其编译进内核，请在你的内核配置文件中加入以下行：`

> device ntb

`或者，要在引导时以模块方式加载，请在 loader.conf(5) 中加入以下行：`

```sh
ntb_load="YES"
```

`以下可调参数可在 loader(8) 中设置：`

`驱动调试级别。默认值为 0，数值越高输出越详细。`

`配置一组以逗号分隔的 NTB 功能及其资源分配。每个功能可配置为："[<name>][:<mw>[:<spad>[:<db>]]]"，其中：name 是要附接的驱动名称（空表示任意），mw 是要分配的内存窗口数量（空表示所有可用），spad 是要分配的 scratchpad 寄存器数量（空表示所有可用），db 是要分配的 doorbell 数量（空表示所有可用）。默认配置为空字符串，表示单一功能占用所有可用资源，允许任意驱动附接。`

**hw.ntb.debug_level**

**hint.ntb_hw.X.config**

## 描述

非透明桥接（Non-Transparent Bridge）通过 PCIe 链路连接两个计算机系统，为各自提供对另一方内存空间、scratchpad 寄存器和中断的有限访问。`ntb` 子系统使用硬件驱动以通用方式提供的这些资源，并根据指定配置在多个功能之间分配。

## 参见

[if_ntb(4)](if_ntb.4.md), [ntb_hw_amd(4)](ntb_hw_amd.4.md), [ntb_hw_intel(4)](ntb_hw_intel.4.md), [ntb_hw_plx(4)](ntb_hw_plx.4.md), [ntb_transport(4)](ntb_transport.4.md)

## 作者

`ntb` 子系统由 Intel 开发，最初由 Carl Delsey <carl@FreeBSD.org> 编写。后续改进由 Conrad E. Meyer <cem@FreeBSD.org> 和 Alexander Motin <mav@FreeBSD.org> 完成。
