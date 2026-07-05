# gpioths.4

`gpioths` — DHTxx 和 AM320x 温湿度传感器驱动

## 名称

`gpioths`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device gpioths

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
gpioths_load="YES"
```

## 描述

`gpioths` 驱动支持 DHTxx 和 AM320x 系列温湿度传感器。该驱动每 5 秒自动从传感器读取一次数值，并通过 [sysctl(8)](../man8/sysctl.8.md) 变量提供结果。

## 硬件

`gpioths` 驱动支持以下设备：

| DHT11 | DHT12 |
| --- | --- |
| DHT21 | DHT22 |
| AM3201 | AM3202 |

所支持的设备彼此都相似，主要在精度和分辨率上有所不同。这些设备使用单根线进行数据通信，采用自定义协议，与 Maxim 的 1-wire(tm) 不兼容。AM320x 设备还支持连接到 i2c 总线，但本驱动仅支持单线连接方式。

## SYSCTL 变量

使用 sysctl 变量访问最新的温度和湿度测量值。

**`dev.gpioths.<unit>.temperature`** 当前温度，以整数 deciKelvins 为单位。注意，[sysctl(8)](../man8/sysctl.8.md) 会将这些单位转换为以摄氏度为单位的十进制显示。

**`dev.gpioths.<unit>.humidity`** 当前相对湿度，以整数百分比表示。

**`dev.gpioths.<unit>.fails`** 自上次成功访问以来与传感器通信失败的次数。每当成功检索到一组测量值时即清除。

## FDT 配置

在基于 [fdt(4)](fdt.4.md) 的系统上，`gpioths` 设备节点通常直接定义在根节点下，或定义在表示板上一组设备的 simplebus 节点下。

`gpioths` 设备子节点中需要以下属性：

**`compatible`** 必须为“dht11”。

**`gpios`** 对用于数据通信的 gpio 设备和引脚的引用。

### 通过 overlay 添加传感器的示例

```sh
/dts-v1/;
/plugin/;
#include <dt-bindings/gpio/gpio.h>
/ {
    compatible = "wand,imx6q-wandboard";
};
&{/} {
    dht0 {
        compatible = "dht11";
        gpios = <&gpio5 15 GPIO_ACTIVE_HIGH>;
    };
};
```

## 提示配置

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统（如 `MIPS`）上，可为 `gpioths` 配置以下值：

**`hint.gpioths.<unit>.at`** `gpioths` 实例附加到的 gpiobus(4) 实例。

**`hint.gpioths.pins`** 一个设置了单个位的位掩码，指示使用 gpiobus(4) 上的哪个 gpio 引脚进行数据通信。

## 参见

[fdt(4)](fdt.4.md), gpiobus(4), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`gpioths` 驱动首次出现于 FreeBSD 11.1。
