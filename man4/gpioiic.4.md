# gpioiic.4

`gpioiic` — GPIO I2C 位操作设备驱动

## 名称

`gpioiic`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device gpio
> device gpioiic
> device iicbb
> device iicbus

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
gpioiic_load="YES"
```

## 描述

`gpioiic` 驱动使用两个 GPIO 引脚作为总线上的 SCL 和 SDA 线，提供 IIC 位操作接口。

`gpioiic` 在管理总线上的引脚时，会模拟开漏（open collector）式的输出，即使在不直接支持以该模式配置 gpio 引脚的系统上也是如此。引脚永远不会被驱动到逻辑值“1”。它们被驱动到“0”或切换到输入模式（Hi-Z/三态），由外部上拉电阻将线路拉到 1 状态，除非总线上有其他设备将其驱动到 0。

## 提示配置

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统（如 MIPS）上，可为 `gpioiic` 配置以下值：

**`hint.gpioiic.%d.at`** 你要附加到的 `gpiobus`。在只有一组 gpio 引脚的系统上通常就是 gpiobus0。

**`hint.gpioiic.%d.pins`** 这是 `gpiobus` 上用于 GPIO IIC 位操作总线的 SCLOCK 和 SDATA 引脚的位掩码。要配置引脚 0 和 7，请使用 bitmask 0b10000001 并转换为十六进制值 0x0081。请注意，此掩码应只设置两个位（任何其他位——即引脚——将被忽略）。由于 `gpiobus` 必须是 gpiobus 的子设备，两个 gpio 引脚必须属于该总线。

**`hint.gpioiic.%d.scl`** 指示 `hint.gpioiic.%d.pins` 中的哪一位应用作 SCLOCK 源。可选，默认为 0。

**`hint.gpioiic.%d.sda`** 指示 `hint.gpioiic.%d.pins` 中的哪一位应用作 SDATA 源。可选，默认为 1。

## FDT 配置

在基于 FDT(4) 的系统（如 ARM）上，`gpioiic` 的 DTS 节点遵循标准绑定文档 i2c/i2c-gpio.yaml。设备节点通常出现在设备树的根节点处。以下是 `gpioiic` 节点带一个 IIC 总线从设备的示例：

```sh
/ {
	gpioiic0 {
		compatible = "i2c-gpio";
		pinctrl-names = "default";
		pinctrl-0 = <&pinctrl_gpioiic0>;
		scl-gpios = <&gpio1  5 GPIO_ACTIVE_HIGH>;
		sda-gpios = <&gpio7 11 GPIO_ACTIVE_HIGH>;
		status = "okay";
		/* i2c 总线上的一个从设备。 */
		rtc@51 {
			compatible="nxp,pcf2127";
			reg = <0x51>;
			status = "okay";
		};
	};
};
```

其中：

**`compatible`** 应设置为“i2c-gpio”。为向后兼容，也接受已弃用的字符串“gpioiic”。

**`scl-gpios`** `sda-gpios` 这些属性指示应将哪些 GPIO 引脚用于 GPIO IIC 位操作总线上的时钟和数据。两个引脚不必属于同一个 gpio 控制器。

**`pinctrl-names pinctrl-0`** 除非引脚在你的系统上默认就处于该状态，否则可能需要这些属性将所选引脚配置为 gpio 引脚。

## 参见

[fdt(4)](fdt.4.md), [gpio(4)](gpio.4.md), [iic(4)](iic.4.md), [iicbb(4)](iicbb.4.md), [iicbus(4)](iicbus.4.md)

## 历史

`gpioiic` 手册页首次出现于 FreeBSD 10.1。

## 作者

本手册页由 Luiz Otavio O Souza 编写。
