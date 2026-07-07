# i2ctinyusb(4)

`i2ctinyusb` — USB/I2C 桥接设备驱动

## 名称

`i2ctinyusb`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device i2ctinyusb
> device usb
> device iicbus

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
i2ctinyusb_load="YES"
```

## 描述

`i2ctinyusb` 驱动为 Till Harbaum 设计的 i2c-tiny-usb 设备提供支持。这最初是一个使用 Atmel AVR ATtiny45 构建的非常简单的电路，但也存在 Raspberry Pi Pico (RP2040) 实现。

`i2ctinyusb` 驱动创建 [iicbus(4)](iicbus.4.md) 子总线以暴露 iic 功能，使 I2C 传感器、转换器和显示器能够连接到任何带有 USB 端口的计算机。

有关此设备的更多信息可在以下地址找到：

```sh
https://github.com/harbaum/I2C-Tiny-USB
```

以及（Raspberry Pi Pico 版本）：

```sh
https://github.com/Nicolai-Electronics/rp2040-i2c-interface
```

I2C 控制器支持最多 1024 字节数据的读写事务，以及写操作后跟重复起始后跟读操作的事务，最多 1024 字节。不支持零长度传输。

## 参见

[iicbus(4)](iicbus.4.md), [usb(4)](usb.4.md)

## 历史

`i2ctinyusb` 驱动和本手册页由 Denis Bodor <dbodor@rollmops.ninja> 编写。
