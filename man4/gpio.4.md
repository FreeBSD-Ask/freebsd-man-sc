# gpio(4)

`gpiobus` — GPIO 总线系统

## 名称

`gpiobus`

## 概要

要将这些设备编译进内核并使用设备提示，请在内核配置文件中加入以下行：

> device gpio
> device gpioiic
> device gpioled

ARM 架构的额外设备条目包括：

> device a10_gpio
> device bcm_gpio
> device imx51_gpio
> device lpcgpio
> device mv_gpio
> device ti_gpio
> device gpio_avila
> device gpio_cambria
> device zy7_gpio
> device pxagpio

MIPS 架构的额外设备条目包括：

> device ar71xxx_gpio
> device octeon_gpio
> device rt305_gpio

POWERPC 架构的额外设备条目包括：

> device wiigpio
> device macgpio

RISC-V 架构的额外设备条目包括：

> device sifive_gpio

## 描述

`gpiobus` 系统提供了一个对 GPIO 引脚的简单接口，这些引脚通常在嵌入式架构上可用，并可为系统提供位操作（bit banging）风格的设备。

缩写 `GPIO` 表示“General-Purpose Input/Output”（通用输入/输出）。

总线在物理上由多个引脚组成，可配置为输入/输出、IRQ 传递、SDA/SCL *iicbus* 使用等。

在某些嵌入式架构（如 MIPS）上，总线的发现和引脚的配置通过平台 kernel config(5) 文件中的 [device.hints(5)](../man5/device.hints.5.md) 完成。

在其他架构（如 ARM）上，使用 FDT(4) 来描述设备树，总线发现通过传递给内核的 DTS 完成，DTS 可以静态编译进内核，也可通过多种方式由引导加载程序（或启用 Open Firmware 的系统）在引导时将 DTS blob 传递给内核。

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统上，这些提示可用于配置附加到 `gpiobus` 引脚的设备的驱动：

**`hint.driver.unit.at`** 设备附加到的 `gpiobus`。例如“gpiobus0”。`driver` 和 `unit` 是设备驱动的驱动名和单元号。

**`hint.driver.unit.pins`** 这是 `gpiobus` 上连接到设备的引脚的位掩码。这些引脚将分配给指定的驱动实例。使用此提示仅可指定编号为 0 到 31 的引脚。

**`hint.driver.unit.pin_list`** 这是 `gpiobus` 上连接到设备的引脚的引脚号列表。这些引脚将分配给指定的驱动实例。这是 `pins` 提示的一种更用户友好的替代方案。此外，此提示允许指定大于 31 的引脚号。数字可以是十进制或带 0x 前缀的十六进制。任何非数字字符都可作为分隔符。例如，可以是逗号、斜杠或空格。分隔符后可跟任意数量的空格字符。

以下 [device.hints(5)](../man5/device.hints.5.md) 仅由 `ar71xx_gpio` 驱动提供：

**`hint.gpio.%d.pinmask`** 这是 GPIO 板上希望暴露给主机操作系统使用的引脚位掩码。要暴露引脚 0、4 和 7，请使用 bitmask 10010001 转换为十六进制值 0x0091。

**`hint.gpio.%d.pinon`** 这是 GPIO 板上将在主机启动时设置为 ON 的引脚位掩码。要在引导时将引脚 2、5 和 13 设置为 ON，请使用 bitmask 10000000010010 转换为十六进制值 0x2012。

**`hint.gpio.function_set`**

**`hint.gpio.function_clear`** 这些是将在 Atheros 功能寄存器中重新映射引脚以处理特定功能（USB、UART TX/RX 等）的引脚位掩码。主要用于设置/清除我们在 uBoot 设置或未设置时所需的功能。

简而言之，GPIO 接口的每个引脚都连接到系统中某个设备的输入/输出。

## 参见

[gpioiic(4)](gpioiic.4.md), [gpioled(4)](gpioled.4.md), [iicbus(4)](iicbus.4.md), [device.hints(5)](../man5/device.hints.5.md), [gpioctl(8)](../man8/gpioctl.8.md)

## 历史

`gpiobus` 手册页首次出现于 FreeBSD 10.0。

## 作者

本手册页由 Sean Bruno <sbruno@FreeBSD.org> 编写。
