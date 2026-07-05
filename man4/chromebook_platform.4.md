# chromebook_platform.4

`chromebook_platform` — 各种 Chromebook 型号硬件的支持驱动

## 名称

`chromebook_platform`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device chromebook_platform

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
chromebook_platform_load="YES"
```

## 描述

`chromebook_platform` 驱动为无法枚举或无法安全探测的设备提供自动配置。特别是，I2C 外设因型号而异。`chromebook_platform` 具有关于 I2C 外设、其驱动程序、其总线附加和从地址的型号特定信息。

注意，`chromebook_platform` 不会为外设加载驱动模块。这些必须编译进内核或单独加载。

## 参见

[cyapa(4)](cyapa.4.md), [iicbus(4)](iicbus.4.md), [isl(4)](isl.4.md)

## 作者

`chromebook_platform` 驱动和本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。
