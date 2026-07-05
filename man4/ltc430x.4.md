# ltc430x.4

`ltc430x` — LTC4305 和 LTC4306 I2C 复用芯片驱动

## 名称

`ltc430x`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device ltc430x

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
ltc430x_load="YES"
```

## 描述

`ltc430x` 驱动支持 LTC4305 和 LTC4306 I2C 总线复用器（mux）芯片。当下游总线上的从设备发起 I/O 时，它会根据需要自动将上游 I2C 总线连接到若干下游总线之一。有关自动切换行为的更多信息，请参见 [iicmux(4)](iicmux.4.md)。

## FDT 配置

在基于 [fdt(4)](fdt.4.md) 的系统上，`ltc430x` 设备节点定义为其上游 i2c 总线的子节点。`ltc430x` 节点的子节点是额外的 i2c 总线，这些总线将在其子节点中描述各自的 i2c 从设备。

`ltc430x` 驱动遵循标准的 `i2c/i2c-mux-ltc4306.txt` 绑定文档，但以下可选属性当前不受支持，如果存在将被忽略：

**** enable-gpios
**** gpio-controller
**** #gpio-cells
**** ltc,downstream-accelerators-enable
**** ltc,upstream-accelerators-enable

此外，还支持以下附加属性：

**`freebsd,ctlreg2`** 在初始化期间存入芯片控制寄存器 2 的值。各比特位的含义请查阅芯片数据手册。

## HINTS 配置

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统上，需要以下 hints：

**`hint.ltc430x.<unit>.at`** `ltc430x` 实例附加到的上游 [iicbus(4)](iicbus.4.md)。

**`hint.ltc430x.<unit>.addr`** `ltc430x` 实例在上游总线上的从地址。

**`hint.ltc430x.<unit>.chip_type`** 驱动控制的芯片类型。有效值为“ltc4305”和“ltc4306”。

以下 hints 可选：

**`hint.ltc430x.<unit>.ctlreg2`** 在初始化期间存入芯片控制寄存器 2 的值。各比特位的含义请查阅芯片数据手册。此 hint 可选；缺失时，驱动不更新控制寄存器 2。

**`hint.ltc430x.<unit>.idle_disconnect`** 空闲时是否将所有下游总线与上游总线断开。设为零时，最近使用的下游总线在 I/O 完成后保持与上游总线的连接。任何非零值都会导致空闲时所有下游总线断开。此 hint 可选；缺失时，驱动行为如同将其设为零。

通过 hints 配置时，驱动会为芯片支持的每个下游总线自动添加一个 iicbus 实例。目前无法指示已用与未用的下游通道。

## 参见

[iicbus(4)](iicbus.4.md), [iicmux(4)](iicmux.4.md)

## 历史

`ltc430x` 驱动首次出现于 FreeBSD 13.0。
