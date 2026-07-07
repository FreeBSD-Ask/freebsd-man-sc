# watchdog(8)

`watchdog` — 看门狗控制程序

## 名称

`watchdog`

## 概要

`watchdog [-d] [-t timeout]`

## 描述

`watchdog` 工具可用于控制内核的看门狗功能。

`-d` 选项启用调试。

`-t` `timeout` 选项指定所需的超时时间（以秒为单位），值为零将禁用看门狗。默认超时为 128 秒。

## 参见

[watchdog(4)](../man4/watchdog.4.md), [watchdogd(8)](watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`watchdog` 工具出现于 FreeBSD 5.1。

## 作者

`watchdog` 工具和手册页由 Sean Kelly <smkelly@FreeBSD.org> 和 Poul-Henning Kamp <phk@FreeBSD.org> 编写。

Jeff Roberson <jeff@FreeBSD.org> 做出了一些贡献。
