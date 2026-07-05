# itwd.4

`itwd` — ITE Super I/O 芯片看门狗定时器驱动

## 名称

`itwd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device superio
> device itwd

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
itwd_load="YES"
```

## 描述

`itwd` 驱动为至少以下 Super I/O 芯片上存在的看门狗定时器提供 [watchdog(4)](watchdog.4.md) 支持：

- IT8721F
- IT8728F
- IT8771F

## 参见

[superio(4)](superio.4.md), [watchdog(4)](watchdog.4.md), [device.hints(5)](../man5/device.hints.5.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 作者

本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。
