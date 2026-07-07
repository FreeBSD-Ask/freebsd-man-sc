# acpi_ged(4)

`acpi_ged` — ACPI 通用事件设备

## 名称

`acpi_ged`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device acpi_ged

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
acpi_ged_load="YES"
```

## 描述

`acpi_ged` 驱动为通用事件接口提供支持。它处理中断并求值特定的 ACPI 方法。这可以选择性地为另一个设备生成 ACPI 通知。

## 参见

[acpi(4)](acpi.4.md)

## 历史

`acpi_ged` 设备驱动最早出现在 FreeBSD 13.3 中。

## 作者

`acpi_ged` 驱动由 Takanori Watanabe <takawata@FreeBSD.org> 编写。
