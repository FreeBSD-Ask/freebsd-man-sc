# amdsbwd.4

`amdsbwd` — AMD 南桥看门狗定时器设备驱动

## 名称

`amdsbwd`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device amdsbwd

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
amdsbwd_load="YES"
```

## 描述

`amdsbwd` 驱动为所支持芯片组中存在的看门狗定时器提供 [watchdog(4)](watchdog.4.md) 支持。

## 硬件

`amdsbwd` 驱动支持以下芯片组：

- AMD SB600/7x0/8x0/9x0 南桥
- AMD Axx/Hudson/Bolton FCH
- 集成于 Family 15h Models 60h-6Fh、70h-7Fh 处理器中的 AMD FCH
- 集成于 Family 16h Models 00h-0Fh、30h-3Fh 处理器中的 AMD FCH

## 参见

[watchdog(4)](watchdog.4.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`amdsbwd` 驱动首次出现于 FreeBSD 7.3 和 FreeBSD 8.1。

## 作者

`amdsbwd` 驱动由 Andriy Gapon <avg@FreeBSD.org> 编写。本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。
