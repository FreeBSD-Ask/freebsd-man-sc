# pca954x(4)

`pca954x` — PCA9548A I2C 交换机驱动

## 名称

`pca954x`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device pca954x
> device iicmux
> device iicbus

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
pca954x_load="YES"
```

## 描述

`pca954x` 驱动支持 PCA9548A I2C 总线交换机及兼容芯片（如 TCA9548A）。当下游总线上的从设备发起 I/O 时，它会根据需要自动将上游 I2C 总线连接到若干下游总线之一。有关自动切换行为的更多信息，请参见 [iicmux(4)](iicmux.4.md)。

## FDT 配置

在基于 FDT(4) 的系统上，`pca954x` 设备节点定义为其上游 I2C 总线的子节点。`pca954x` 节点的子节点是额外的 I2C 总线，这些总线将在其子节点中描述各自的 I2C 从设备。

`pca954x` 驱动附加到 `compatible` 属性设置为以下值之一的节点：

- "nxp,pca9548"

除标准 I2C 多路复用器属性外，`pca954x` 驱动还支持以下可选属性：

**`i2c-mux-idle-disconnect`** 如果定义，则强制交换机在空闲状态断开所有子节点。

## HINTS 配置

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统上，可为 `pca954x` 配置以下值：

**`hint.pca954x.<unit>.at`** `pca954x` 实例附加到的上游 [iicbus(4)](iicbus.4.md)。

**`hint.pca954x.<unit>.chip_type`** 芯片类型。目前仅支持 "pca9548"。

通过 hints 配置时，驱动会为芯片支持的每个下游总线自动添加一个 [iicbus(4)](iicbus.4.md) 实例。目前无法指示已用与未用通道。

## 参见

[iicbus(4)](iicbus.4.md), [iicmux(4)](iicmux.4.md)

## 历史

`pca954x` 驱动及本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。
