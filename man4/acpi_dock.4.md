# acpi_dock.4

`acpi_dock` — 笔记本扩展坞设备驱动

## 名称

`acpi_dock`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device acpi_dock

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
acpi_dock_load="YES"
```

## 描述

`acpi_dock` 驱动提供对笔记本扩展坞的支持。

## 参见

[acpi(4)](acpi.4.md)

## 历史

`acpi_dock` 设备驱动首次出现于 FreeBSD 7.0。

## 作者

`acpi_dock` 设备驱动由 Mitsuru IWASAKI <iwasaki@FreeBSD.org> 编写。
