# owc(4)

`owc` — Dallas Semiconductor 1-Wire 控制器

## 名称

`owc`

## 概要

`device owc`

## 描述

`owc` 模块实现 Dallas Semiconductor 1-Wire 信令。它附加到 [ow(4)](ow.4.md) 驱动的 1-Wire 总线协议。`owc` 设备实现 1-Wire 总线协议栈的链路层。

通过对 gpiobus(4) 上的引脚进行位操作（bit banging）是唯一支持的控制器。标准传输时序和过驱动传输时序均已实现。支持寄生模式所需的强上拉功能未实现。

要为 FDT 系统启用 1-Wire，需要修改板卡的 DTS，添加类似以下内容：

```sh
/ {
	...
	onewire {
		compatible = "w1-gpio";
		gpios = <&gpio 4 1>;
	};
	...
};
```

gpios 属性描述了 1-Wire 总线所连接的 GPIO 引脚。有关 `gpios` 属性的更多细节，请参阅 **/usr/src/sys/dts/bindings-gpio.txt**。

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统上，`owc` 需要以下值：

**`hint.owc.%d.at`** 你要附加到的 `gpiobus`。

**`hint.owc.%d.pins`** 这是一个位掩码，用于定义 `gpiobus` 上要用于 1-Wire 总线的引脚。例如，要配置引脚 10，使用位掩码 0x400。请注意，此掩码应仅设置一个位（任何其他位——即引脚——将被忽略）。

## 参见

gpiobus(4), [ow(4)](ow.4.md), [ow_temp(4)](ow_temp.4.md), [owll(9)](../man9/owll.9.md), [own(9)](../man9/own.9.md)

## 法律条款

1-Wire 是 Maxim Integrated Products, Inc. 的注册商标。

## 历史

`gpiobus` 驱动最早出现于 FreeBSD 11.0。

## 作者

`gpiobus` 设备驱动及本手册页由 Warner Losh 编写。

## 注意事项

gpio 驱动通过忙等待实现时序，这在较慢的系统上可能导致高负载。

## 缺陷

过驱动模式实际上尚未经过测试。
