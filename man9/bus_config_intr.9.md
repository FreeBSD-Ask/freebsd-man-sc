# BUS_CONFIG_INTR(9)

`BUS_CONFIG_INTR` — 配置中断极性与触发模式

## 名称

`BUS_CONFIG_INTR`, `bus_config_intr`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
BUS_CONFIG_INTR(device_t bus, device_t dev, int irq,
    enum intr_trigger trig, enum intr_polarity pol)

int
bus_config_intr(device_t dev, int irq, enum intr_trigger trig,
    enum intr_polarity pol)
```

## 描述

`BUS_CONFIG_INTR` 方法允许总线或设备驱动程序向父总线提供中断极性和触发模式。这通常会一路向上传递到根总线（例如 nexus），由其执行实际编程硬件所需的操作。由于 `BUS_CONFIG_INTR` 方法接受中断号作为参数，因此假定（但并非必须）它在 [BUS_SETUP_INTR(9)](bus_setup_intr.9.md) 之前调用。

`bus_config_intr` 函数是 `BUS_CONFIG_INTR` 的简单封装。

`trig` 参数可以是以下之一：

**`INTR_TRIGGER_CONFORM`** 中断触发模式为设备所附加总线的标准模式。

**`INTR_TRIGGER_EDGE`** 中断为边沿触发。这意味着中断由中断线上信号的上升沿引发。信号通常会恢复到原始状态，从而形成一个尖峰。

**`INTR_TRIGGER_LEVEL`** 中断为电平触发。这意味着中断在中断线上的信号发生跳变时引发，并在中断被服务之前保持不变，服务完成后信号跳变回去。

`pol` 参数可以是以下之一：

**`INTR_POLARITY_CONFORM`** 中断极性为设备所附加总线的标准极性。

**`INTR_POLARITY_HIGH`** 中断由中断线上的高电平激活。

**`INTR_POLARITY_LOW`** 中断由中断线上的低电平激活。

## 返回值

成功时返回零，否则返回一个适当的错误。

## 参见

[BUS_SETUP_INTR(9)](bus_setup_intr.9.md), BUS_TEARDOWN_INTR(9), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 历史

`BUS_CONFIG_INTR` 方法首次出现于 FreeBSD 5.2。

## 作者

本手册页由 Marcel Moolenaar <marcel@xcllnt.net> 编写。
