# ses(4)

`ses` — SCSI 环境服务驱动

## 名称

`ses`

## 概要

`device ses`

## 描述

`ses` 驱动为通过受支持的 SCSI 主机适配器连接到系统的所有 SCSI 环境服务类设备提供支持，同时提供对 SAF-TE（SCSI Accessible Fault Tolerant Enclosures）的模拟支持。环境服务类通常是指提供环境信息（如电源数量及状态、温度、设备插槽等）的机箱设备。

在配置 SCSI 环境服务设备之前，还必须单独将 SCSI 主机适配器配置到系统中。

## 内核配置

只需显式配置一个 `ses` 设备；数据结构会在 SCSI 总线上发现设备时动态分配。

可指定一个单独的选项 `SES_ENABLE_PASSTHROUGH`，允许 `ses` 驱动对声称也支持 `ses` 功能的其他类设备执行操作。

## IOCTLS

以下 ioctl(2) 调用适用于 `ses` 设备。它们定义于头文件

`#include <cam/scsi/scsi_enc.h>`

（参见下文）。

**`ENCIOC_GETNELM`** 用于查明此特定设备实例驱动了多少个 `ses` 元素。

**`ENCIOC_GETELMMAP`** 从内核读取一个 SES 元素数组，其中包含元素标识符、所属子机箱以及该元素的 `ses` 类型。

**`ENCIOC_GETENCSTAT`** 获取机箱整体状态。

**`ENCIOC_SETENCSTAT`** 设置机箱整体状态。

**`ENCIOC_GETELMSTAT`** 获取特定元素的状态。

**`ENCIOC_SETELMSTAT`** 设置特定元素的状态。

**`ENCIOC_GETTEXT`** 获取元素的相关帮助文本（尚未实现）。`ses` 设备通常具有描述性文本，可告知你位置等信息（例如"left power supply"）。

**`ENCIOC_INIT`** 初始化机箱。

**`ENCIOC_GETELMDESC`** 获取元素的描述字符串。

**`ENCIOC_GETELMDEVNAMES`** 获取与此元素关联的设备名称（如有）。

**`ENCIOC_GETSTRING`** 用于读取 SES String In Diagnostic Page。此页面的内容因设备而异。

**`ENCIOC_SETSTRING`** 用于设置 SES String Out Diagnostic Page。此页面的内容因设备而异。

**`ENCIOC_GETENCNAME`** 用于获取机箱名称。

**`ENCIOC_GETENCID`** 用于获取机箱逻辑标识符。

## 用法示例

以下文件中包含的内容

`#include </usr/share/examples/ses>`

展示了使用这些接口的简单机制，以及一个非常简单的监控守护进程。

## 文件

**`/dev/ses`** `N` 第 *N* 个 `SES` 设备。

## 诊断

当内核配置启用了 DEBUG 时，首次打开 SES 设备会将机箱整体参数输出到控制台。

## 参见

sesutil(8)

## 历史

`SES` 驱动最初由 Matthew Jacob 为 CAM SCSI 子系统编写，首次发布于 FreeBSD 4.3。它在功能上等效于 Solaris Release 7 中的类似驱动。后在 FreeBSD 9.2 中由 Alexander Motin、Justin Gibbs 和 Will Andrews 进行了大范围重写。
