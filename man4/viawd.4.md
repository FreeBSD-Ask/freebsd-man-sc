# viawd(4)

`viawd` — VIA 南桥看门狗定时器设备驱动

## 名称

`viawd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device viawd

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
viawd_load="YES"
```

## 描述

`viawd` 驱动为 VIA 南桥芯片组（VT8251、CX700、VX800、VX855、VX900）上存在的看门狗中断定时器提供 [watchdog(4)](watchdog.4.md) 支持。

VIA 南桥内置看门狗定时器，可由用户程序启用和禁用，并可在 1 到 1023 秒之间设置。

`viawd` 驱动在卸载时若看门狗仍在运行，会将看门狗重新调度至 5 分钟。

## 参见

[watchdog(4)](watchdog.4.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`viawd` 驱动最早出现于 FreeBSD 10.0。

## 作者

`viawd` 驱动及本手册页由 Fabien Thomas <fabient@FreeBSD.org> 编写。
