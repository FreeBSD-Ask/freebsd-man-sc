# ftwd(4)

`ftwd` — Fintek F81803 看门狗定时器

## 名称

`ftwd`

## 概要

`要将本驱动程序编译进内核，请在你的内核配置文件中加入以下行：`

> device superio
> device ftwd

`或者，要在引导时以模块方式加载该驱动程序，请在 loader.conf(5) 中加入以下行：`

```sh
ftwd_load="YES"
```

## 描述

`ftwd` 驱动程序为 Fintek F81803 芯片中的看门狗定时器提供 [watchdog(4)](watchdog.4.md) 支持。

## 参见

[superio(4)](superio.4.md), [watchdog(4)](watchdog.4.md), [device.hints(5)](../man5/device.hints.5.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 作者

本手册页由 Poul-Henning Kamp <phk@FreeBSD.org> 编写。
