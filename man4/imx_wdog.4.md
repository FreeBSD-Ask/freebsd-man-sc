# imx\_wdog.4

`imx_wdog` — NXP i.MX5 和 i.MX6 看门狗定时器驱动

## 名称

`imx_wdog`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device imxwdt

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
imx_wdog_load="YES"
```

## 描述

`imx_wdog` 驱动为 NXP i.MX5 和 i.MX6 处理器上存在的看门狗定时器提供 [watchdog(4)](watchdog.4.md) 支持。i.MX 看门狗硬件支持从 0.5 秒到 128 秒的可编程超时，步长为半秒。一旦激活，看门狗硬件即无法停用，但超时时间可更改为任意有效的非零值。

上电时，硬件会自动启用特殊的 16 秒“掉电定时器”模式。它会断言外部的 WDOG_B 信号，该信号可连接到导致系统复位或断电的外部硬件。掉电定时器通常由引导加载器（通常是 U-Boot）复位。如果在普通看门狗首次启用时掉电定时器仍处于活动状态，`imx_wdog` 驱动会自动将其禁用。

当存在 FDT `fsl,external-reset` 属性时，`imx_wdog` 驱动通过启用 WDOG_B 外部超时信号的断言来支持该属性。在此种运行方式下，看门狗超时需复位系统这一需求通过将 WDOG_B 线拉低来发出信号；预期某个外部实体将断言芯片的 POR 引脚作为响应。`imx_wdog` 驱动通过调度同时发生的中断来尝试为此外部复位提供后备。中断处理程序会等待 1 秒以便外部复位发生，随后触发普通的软件复位。注意，WDOG_B 信号可配置为使用芯片上的多种引脚。要使 `fsl,external-reset` 属性生效，必须由系统的 FDT pinctrl 数据将该信号连接到合适的引脚。

`imx_wdog` 驱动通过在驱动附加后立即使用给定的超时值启用看门狗来支持 FDT `timeout-secs` 属性。这使看门狗保护扩展到系统启动过程的绝大部分，但仍要求配置 watchdogd(4) 来服务看门狗。

## 参见

[fdt(4)](fdt.4.md), [watchdog(4)](watchdog.4.md), [watchdog(8)](../man8/watchdog.8.md), [watchdogd(8)](../man8/watchdogd.8.md), [watchdog(9)](../man9/watchdog.9.md)

## 历史

`imx_wdog` 驱动首次出现于 FreeBSD 10.0。
