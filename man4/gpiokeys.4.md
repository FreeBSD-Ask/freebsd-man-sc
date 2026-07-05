# gpiokeys.4

`gpiokeys` — GPIO 按键设备驱动

## 名称

`gpiokeys`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> options FDT
> device gpio
> device gpiokeys

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
gpiokeys_load="YES"
```

## 描述

`gpiokeys` 驱动提供了一种将一组通用输入表示为 [keyboard(4)](keyboard.4.md) 设备的方法。目前该驱动仅支持基于 FDT(4) 的系统。DTS 决定哪些引脚映射到按钮，以及每个虚拟按钮生成什么键码。可从用户态使用 [keyboard(4)](keyboard.4.md) 设备监视输入变化。

在基于 FDT(4) 的系统上，`gpiokeys` 设备的 DTS 部分通常如下所示：

```sh
/ {
	...
	gpio_keys {
		compatible = "gpio-keys";
		btn1 {
			label = "button1";
			linux,code = <KEY_1>;
			gpios = <&gpio 0 3 GPIO_ACTIVE_LOW>
		};
		btn2 {
			label = "button2";
			linux,code = <KEY_2>;
			gpios = <&gpio 0 4 GPIO_ACTIVE_LOW>
		};
	};
};
```

关于 `gpios` 属性的更多细节，请参阅 **`/usr/src/sys/dts/bindings-gpio.txt`**。

`gpiokeys` 驱动支持两个属性来指定键码。

属性 `freebsd,code` 指定与 kbdmap(5) 键盘映射兼容的 FreeBSD 原生扫描码。

属性 `linux,code` 指定 evdev 扫描码。该扫描码会在内部转换为原生扫描码。注意，并非所有 evdev 扫描码都有对应的原生扫描码。如果扫描码无法转换，将打印诊断消息并忽略该输入。

属性 `label` 是按钮的描述性名称。仅用于诊断消息。此属性可选。如未设置，则使用节点名代替。

属性 `autorepeat` 决定按钮是否启用自动重复。

属性 `debounce-interval` 定义去抖动间隔时间（以毫秒为单位）。如未指定，间隔默认为 5。

## 参见

[fdt(4)](fdt.4.md), [gpio(4)](gpio.4.md), [keyboard(4)](keyboard.4.md), kbdmap(5)

## 历史

`gpiokeys` 手册页首次出现于 FreeBSD 12.2。

## 作者

`gpiokeys` 驱动由 Oleksandr Tymoshenko <gonzo@FreeBSD.org> 编写。本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。
