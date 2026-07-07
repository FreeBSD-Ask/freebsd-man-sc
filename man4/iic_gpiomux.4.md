# iic_gpiomux(4)

`iic_gpiomux` — 通过 GPIO 控制的 I2C 多路复用器硬件驱动

## 名称

`iic_gpiomux`

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device iic_gpiomux

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
iic_gpiomux_load="YES"
```

## 描述

`iic_gpiomux` 驱动支持任何通过操纵一个或多个 GPIO 引脚状态来控制的 I2C 总线多路复用器（mux）硬件。当下游总线上的从设备发起 I/O 时，它会按需自动将上游 I2C 总线连接到某条下游总线。有关自动切换行为的更多信息，参见 [iicmux(4)](iicmux.4.md)。

## FDT 配置

在基于 [fdt(4)](fdt.4.md) 的系统上，`iic_gpiomux` 设备节点可以定义为 FDT 数据中任意总线下的子节点。`i2c-parent` 属性指示与上游 I2C 总线的连接。`iic_gpiomux` 节点的子节点是额外的 i2c 总线，这些总线将在其子节点中描述各自的 i2c 从设备。

`iic_gpiomux` 驱动遵循标准的 Bk -words `i2c/i2c-mux-gpio.txt` Ek 绑定文档。

## 参见

[iicbus(4)](iicbus.4.md), [iicmux(4)](iicmux.4.md)

## 历史

`iic_gpiomux` 驱动最早出现于 FreeBSD 13.0。
