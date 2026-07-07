# aibs(4)

`aibs` — ASUSTeK AI Booster ACPI ATK0110 电压、温度和风扇传感器

## 名称

`aibs`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device aibs

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
aibs_load="YES"
```

## 描述

`aibs` 驱动为通过 ASUSTeK 主板上的 ATK0110 ASOC ACPI 设备可用的电压、温度和风扇传感器提供支持。每种类型传感器的数量以及每个传感器的描述因主板而异。

该驱动支持任意传感器集合，提供每个传感器用途的描述，并报告当前值以及主板制造商通过 ACPI 定义的每个传感器输入的假定范围规范。

范围规范如下：

- 电压传感器具有下限和上限范围规范。
- 温度传感器具有两个上限规范。
- 风扇传感器可能仅有下限规范，或者根据 DSDT，有一个下限和一个上限规范。

传感器读数和范围规范通过 sysctl(3) 接口提供，可使用 [sysctl(8)](../man8/sysctl.8.md) 进行监视。例如，在 ASUS V3-P5G965 准系统上：

```sh
> sysctl dev.aibs.0.{volt,temp,fan}
dev.aibs.0.volt.0: 1192 850 1600
dev.aibs.0.volt.1: 3312 2970 3630
dev.aibs.0.volt.2: 5017 4500 5500
dev.aibs.0.volt.3: 12302 10200 13800
dev.aibs.0.temp.0: 28.0C 80.0C 95.0C
dev.aibs.0.temp.1: 55.0C 60.0C 95.0C
dev.aibs.0.fan.0: 878 600 7200
dev.aibs.0.fan.1: 0 700 7200
> sysctl -d dev.aibs.0.{volt,temp,fan}
dev.aibs.0.volt:
dev.aibs.0.volt.0: Vcore Voltage
dev.aibs.0.volt.1:  +3.3 Voltage
dev.aibs.0.volt.2:  +5 Voltage
dev.aibs.0.volt.3:  +12 Voltage
dev.aibs.0.temp:
dev.aibs.0.temp.0: CPU Temperature
dev.aibs.0.temp.1: MB Temperature
dev.aibs.0.fan:
dev.aibs.0.fan.0: CPU FAN Speed
dev.aibs.0.fan.1: CHASSIS FAN Speed
```

通常，`aibs` 驱动提供的传感器也可能由直接访问 ISA/LPC 或 I2C/SMBus 设备的某些其他驱动或实用程序支持。`aibs` 传感器的精确集合由主板设计中专门使用的传感器组成，这些传感器可能通过一个或多个物理硬件监视芯片的组合来支持。

但与本地硬件监视驱动或其他实用程序相比，`aibs` 驱动具有以下优势：

- `aibs` 的传感器值预期更可靠。例如，许多硬件监视芯片中的电压传感器只能感测 0 至 2 或 4 伏的电压，多余的电压由电阻器去除，这可能因主板和所感测的电压而异。在 `aibs` 中，所需的电阻因子由主板制造商通过 ACPI 提供；而在本地驱动中，电阻因子根据芯片制造商的建议编码到驱动中。本质上，`aibs` 的传感器值很可能与 BIOS 中硬件监视屏幕的读数一致。
- `aibs` 的传感器描述更可能匹配主板上的标记。
- `aibs` 支持传感器范围规范。根据主板制造商的建议为每个传感器报告范围规范。例如，CPU 温度传感器的阈值可能显著高于机箱温度传感器的阈值。
- `aibs` 支持更新的芯片。较新的芯片可能缺少本地驱动，但应能通过 `aibs` 获得支持。

## 参见

sysctl(3), [acpi(4)](acpi.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`aibs` 驱动最早出现在 OpenBSD 4.7、Dx 2.5、NetBSD 6.0 和 FreeBSD 9.0 中。

该驱动的早期版本 `acpi_aiboost` 最早出现在 FreeBSD 7.0 和 NetBSD 5.0 中。

## 作者

`acpi_aiboost` 驱动由 Constantine A. Murenin <cnst@FreeBSD.org>、Raouf Boutaba Research Group、David R. Cheriton School of Computer Science、University of Waterloo 为 OpenBSD、Dx、NetBSD 和 FreeBSD 编写。

该驱动的早期版本名为 `acpi_aiboost`，由 Takanori Watanabe 为 FreeBSD 编写。
