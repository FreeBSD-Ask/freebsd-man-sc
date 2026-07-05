# iicbus.4

`iicbus` — I2C 总线系统

## 名称

`iicbus`

## 概要

`device iicbus device iicbb`

`device iic device ic device iicsmb`

## 描述

*iicbus* 系统为控制各种 I2C 设备和利用不同 I2C 控制器的驱动实现提供了一个统一、模块化且与体系结构无关的系统。

## I2C

I2C 是 Inter Integrated Circuit bus（内部集成电路总线）的缩写。I2C 总线由 Philips 半导体公司于 20 世纪 80 年代初开发。其目的是提供一种简便的方式将 CPU 与电视机中的外设芯片连接起来。

总线在物理上由 2 根有效线和 1 根地线连接组成。有效线 SDA 和 SCL 均为双向。其中 SDA 是串行数据线（Serial DAta），SCL 是串行时钟线（Serial CLock）。

挂在总线上的每个组件，无论是 CPU、LCD 驱动器、内存还是复杂功能芯片，都有自己唯一的地址。这些芯片中的每一个都可以根据其功能充当接收器和/或发送器。显然，LCD 驱动器仅是接收器，而内存或 I/O 芯片则既可以是发送器也可以是接收器。此外，总线上可能存在一个或多个总线主控（BUS MASTER）。

总线主控是在总线上发出命令的芯片。在 I2C 协议规范中指出，在总线上发起数据传输的 IC 被视为总线主控。此时其他所有设备被视为总线从设备（BUS SLAVE）。如前所述，IC 总线是一种多主控总线（Multi-MASTER BUS）。这意味着可以连接多个能够发起数据传输的 IC。

## 设备

提供以下 I2C 设备驱动：

| *Devices* | *Description* |
| --------- | ------------- |
| **iic** | 通用 I/O 操作 |
| **ic** | 网络 IP 接口 |
| **iicsmb** | I2C 到 SMB 软件桥 |

## 接口

I2C 协议可由硬件或软件实现。软件接口依赖于非常简单的硬件，通常是由 2 个寄存器操纵的两根线。硬件接口则更智能，接收 8 位字符并根据 I2C 协议将其写入总线。

得益于 I2C 协议的多主控能力，I2C 接口可作为从设备在总线上运作，允许自发的双向通信。

提供以下 I2C 接口：

| *Interface* | *Description* |
| ----------- | ------------- |
| **pcf** | Philips PCF8584 主/从接口 |
| **iicbb** | 通用位敲击仅主控驱动 |
| **lpbb** | 并口专用位敲击接口 |

## 总线频率配置

I2C 总线的工作频率可以是固定的，也可以是可配置的。总线可能作为某个更大标准接口的一部分使用，而该接口规范可能要求固定频率。该硬件的驱动将不接受尝试配置不同速度。通用 I2C 总线（如许多嵌入式系统中的那些）通常支持多种总线频率。

当系统支持多个 I2C 总线时，可通过编号为每条总线配置不同的频率，编号对应下面变量名中的 `%d`。可使用设备提示、扁平设备树（FDT）数据、通过 [loader(8)](../man8/loader.8.md) 设置的可调参数，或在运行时使用 [sysctl(8)](../man8/sysctl.8.md) 的任意组合来配置总线。当使用多种方法提供配置时，FDT 和提示数据将被可调参数覆盖，而可调参数又可被 [sysctl(8)](../man8/sysctl.8.md) 覆盖。

### 设备提示

在使用设备提示配置 I2C 设备的系统上，将 `hint.iicbus.%d.frequency` 设置为以 Hz 为单位的频率。如果未使用 FDT 配置频率，使用 FDT 数据的系统也会遵循此提示。

### 扁平设备树数据

使用描述 I2C 控制器硬件节点的 FDT 标准 `clock-frequency` 属性配置 I2C 总线速度。

### Sysctl 和可调参数

在 loader.conf(5) 中设置 `dev.iicbus.%d.frequency`。同一变量可随时使用 [sysctl(8)](../man8/sysctl.8.md) 更改。使用 [i2c(8)](../man8/i2c.8.md) 或 [iic(4)](iic.4.md) 的 `I2CRSTCARD` ioctl 复位总线以使更改生效。

## 参见

[fdt(4)](fdt.4.md), [iic(4)](iic.4.md), [iicbb(4)](iicbb.4.md), [lpbb(4)](lpbb.4.md), [pcf(4)](pcf.4.md), [i2c(8)](../man8/i2c.8.md)

## 历史

`iicbus` 手册页最早出现于 FreeBSD 3.0。

## 作者

本手册页由 Nicolas Souchu 编写。
