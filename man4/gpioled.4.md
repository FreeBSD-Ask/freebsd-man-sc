# gpioled.4

`gpioled` — GPIO LED 通用设备驱动

## 名称

`gpioled`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device gpio
> device gpioled

## 描述

`gpioled` 驱动提供粘合层，将 [led(4)](led.4.md) 兼容设备附加到 GPIO 引脚。系统中每个 LED 都有一个 `name`，用于将设备导出为 **`/dev/led/<name>`**。然后可以按 [led(4)](led.4.md) 中所述通过写入此设备来控制 GPIO 引脚。

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统（如 `MIPS`）上，可为 `gpioled` 配置以下值：

**`auto`** 如可用则使用硬件引脚反相，否则回退到软件引脚反相。这是默认值。

**`hw`** 使用硬件引脚反相。

**`sw`** 使用软件引脚反相。

**`hint.gpioled.%d.at`** 你要附加到的 gpiobus。通常分配给 gpiobus0。

**`hint.gpioled.%d.name`** 在 **`/dev/led/`** 中为 [led(4)](led.4.md) 创建的设备的任意名称。

**`hint.gpioled.%d.pins`** GPIO 接口上映射到此实例的引脚。请注意，此掩码应只设置一个位（任何其他位——即引脚——将被忽略）。

**`hint.gpioled.%d.invert`** 使用引脚反相。如设置为 1，引脚将被设置为 0 以点亮 LED，设置为 1 以熄灭它。

**`hint.gpioled.%d.invmode`** 请求引脚反相时是否使用硬件支持。必须为以下之一：

**`hint.gpioled.%d.state`** 驱动接管 LED 时的初始状态。如设置为 1 或 0，LED 将相应地亮起或熄灭。如设置为 -1，LED 将保持其原始状态。

在基于 FDT(4) 的系统（如 `ARM`）上，`gpioled` 设备的 DTS 部分通常如下所示：

```sh
gpio: gpio {
	gpio-controller;
	...
	led0 {
		compatible = "gpioled";
		gpios = <&gpio 16 2 0>;		/* GPIO 引脚 16。 */
		name = "ok";
	};
	led1 {
		compatible = "gpioled";
		gpios = <&gpio 17 2 0>;		/* GPIO 引脚 17。 */
		name = "user-led1";
	};
};
```

或者，你可以选择将所有 LED 组合在单个“gpio-leds”compatible 节点下：

```sh
simplebus0 {
	...
	leds {
		compatible = "gpio-leds";
		led0 {
			gpios = <&gpio 16 2 0>;
			name = "ok"
		};
		led1 {
			gpios = <&gpio 17 2 0>;
			name = "user-led1"
		};
	};
};
```

两种方法都同样受支持，可以任意混合使用这两种方法来定义 LED。唯一的限制是一个 GPIO 引脚不能被两个不同的 (gpio)led 映射。

关于 `gpios` 属性的更多细节，请参阅 **`/usr/src/sys/dts/bindings-gpio.txt`**。

属性 `name` 是在 **`/dev/led/`** 中为 [led(4)](led.4.md) 创建的设备的任意名称。

## 参见

[fdt(4)](fdt.4.md), [gpio(4)](gpio.4.md), [gpioiic(4)](gpioiic.4.md), [led(4)](led.4.md)

## 历史

`gpioled` 手册页首次出现于 FreeBSD 10.1。

## 作者

本手册页由 Luiz Otavio O Souza 编写。
