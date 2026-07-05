# fdt.4

`fdt` — Flattened Device Tree 支持

## 名称

`fdt`

## 概要

`options FDT`

`makeoptions FDT_DTS_FILE=<board name>.dts`

`options FDT_DTB_STATIC`

## 描述

*Flattened Device Tree* 是一种以统一且可移植的方式描述计算机硬件资源（无法探测或自枚举的资源）的机制。此技术的主要使用者是*嵌入式系统*，其中许多设计基于相似芯片，但引脚分配、内存布局、地址绑定、中断路由和其他资源各不相同。

无法在运行时自发现的配置数据必须从外部源提供。Flattened device tree 的概念是一种平台和架构无关的解决此类问题的方法。该想法继承自 Open Firmware IEEE 1275 device-tree 概念，并已被嵌入式行业成功采用。其工作方式如下：

- 硬件平台资源以人类可读的文本源格式*手动*描述，汇集所有非自枚举信息。
- 此源描述被转换（编译）为二进制对象，即 flattened device tree *blob*，在引导时传递给内核。
- 内核（驱动程序）从此[外部提供的] blob 中获取硬件资源详情和依赖关系，无需在内核中嵌入任何关于底层平台硬件资源的信息。
- Flattened device tree 机制原则上不依赖任何特定的第一阶段引导加载程序或固件功能。对环境的唯一总体要求是向内核提供完整的 device tree 描述。

`fdt` 层允许内核中的任何平台代码从统一来源获取硬件资源信息，这为嵌入式应用带来优势（消除硬编码配置方式，使代码数据驱动且可扩展），从而简化移植和维护。

## 定义

**Device tree source（DTS）** device tree 源是一个文本文件，以人类可读的形式描述计算机系统的硬件资源，具有一定的层次结构（树）。在 FreeBSD 源代码仓库中，DTS 文件的默认位置是 **sys/dts** 目录。

**Device tree blob（DTB）** 文本形式的 device tree 描述（DTS 文件）首先被转换（编译）为二进制对象（device tree blob），即 DTB，再交给最终使用者（通常为内核）解析和处理其内容。

**Device tree compiler（DTC）** 在主机上执行的实用程序，将 device tree 的文本描述（DTS）转换（编译）为二进制对象（DTB）。

**Device tree bindings** 虽然 device tree 文本描述和二进制对象是传达硬件配置信息的媒介，但内容的实际含义和解释由 device tree *bindings* 定义。它们是描述 device tree 中特定节点及其属性、允许值、范围等定义（编码）的某些约定。此类参考约定由旧版 Open Firmware bindings 提供，并由 ePAPR 规范进一步补充。

## 构建世界

为使系统支持 `fdt`，需要通过 [src.conf(5)](../man5/src.conf.5.md) 或命令行使用 -D 定义的 `WITH_FDT` 构建旋钮来构建 FreeBSD world。

这会创建用户空间 `dtc` 编译器，并在 [loader(8)](../man8/loader.8.md) 中启用 `fdt` 支持。

## 构建内核

在 FreeBSD 内核级别管理 `fdt` 支持有若干选项。

**`makeoptions DTS+=<board name>.dts`** 为给定内核指定 device tree 源（DTS）文件。指定的 DTS 文件将在构建内核本身时一并转换（编译）为二进制形式。任何未以绝对路径书写的 DTS 文件名必须相对于 DTS 源的默认位置（即 **sys/dts**）指定。

**`makeoptions DTSO+=<overlay name>.dtso`** 为给定内核指定 device tree 源覆盖（DTSO）文件。覆盖文件将如上文的 `DTS` makeoption 一样随内核构建。以相对路径指定的覆盖文件将相对于所构建平台的 DTS 覆盖默认位置（即 **sys/dts/arm/overlays**）。

**`options FDT`** 在内核中启用 `fdt` 支持的主要选项。它涵盖 `fdt` 内核支持的所有低级和基础设施部分，主要包括 [fdtbus(4)](fdtbus.4.md) 和 [simplebus(4)](simplebus.4.md) 驱动程序，以及辅助例程和库。

**`makeoptions FDT_DTS_FILE=<board name>.dts`** 为给定内核指定首选（默认）device tree 源（DTS）文件。它将如上文的 `DTS` makeoption 一样随内核构建。此 makeoption 不是必需的，除非同时定义了 FDT_DTB_STATIC（见下文）。

**`options FDT_DTB_STATIC`** 通常，device tree blob（DTB）是一个独立文件，与内核物理分离，但此选项允许将 DTB 文件静态嵌入内核映像。注意，指定此项时 FDT_DTS_FILE makeoption 变为必需（因为需要指定 DTS 文件才能将其嵌入内核映像）。

## 参见

[fdtbus(4)](fdtbus.4.md), [openfirm(4)](openfirm.4.md), [simplebus(4)](simplebus.4.md)

## 标准

IEEE Std 1275：IEEE Boot（初始化配置）固件标准：核心要求与实践（`Open Firmware`）。

Power.org 嵌入式 Power 架构平台要求标准（`ePAPR`）。

## 历史

`fdt` 支持首次出现于 FreeBSD 9.0。

## 作者

`fdt` 支持由 Semihalf 在 FreeBSD Foundation 赞助下开发。本手册页由 Rafal Jaworowski 编写。
