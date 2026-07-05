# isci.4

`isci` — Intel C600 Serial Attached SCSI 驱动

## 名称

`isci`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device scbus
> device isci

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
isci_load="YES"
```

## 硬件

`isci` 驱动为 Intel C600 SAS 控制器提供支持。

## 配置

要强制所有 `isci` 驱动实例使用传统中断，在 loader.conf(5) 中设置以下可调参数：

```sh
hw.isci.force_legacy_interrupts=1
```

## 调试

要启用 `isci` 驱动的调试输出，在 loader.conf(5) 中将

```sh
hw.isci.debug_level
```

变量设置为 1 至 4 之间的值。

`isci` 驱动中的硬件层具有丰富的日志功能，由于性能原因默认禁用。可以在内核配置文件中加入

```sh
options ISCI_LOGGING
```

来启用。

## 参见

[cd(4)](cd.4.md), [ch(4)](ch.4.md), [da(4)](da.4.md), [pci(4)](pci.4.md), [sa(4)](sa.4.md), [scsi(4)](scsi.4.md)

## 历史

`isci` 驱动最早出现于 FreeBSD 8.3 和 9.1。

## 作者

`isci` 驱动由 Intel 开发，最初由 Jim Harris <jimharris@FreeBSD.org> 编写，Sohaib Ahsan 贡献，Scott Long <scottl@FreeBSD.org> 提供意见。

本手册页由 Jim Harris <jimharris@FreeBSD.org> 编写。
