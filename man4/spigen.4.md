# spigen(4)

`spigen` — SPI 通用 I/O 设备驱动

## 名称

`spigen`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device spi
> device spibus
> device spigen

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
spigen_load="YES"
```

## 描述

`spigen` 驱动提供对 SPI 总线上从设备的直接访问。每个 `spigen` 设备实例与总线上的一条片选线相关联，通过该实例执行的所有 I/O 都在该片选线被断言时完成。

SPI 数据传输本质上是双向的；不存在独立的读和写操作。当向设备发送命令和数据时，数据也会从设备返回，尽管在某些情况下这些数据可能没有用处（甚至对于某些设备而言没有文档说明或不可预测）。同样，在读操作中，操作开始时缓冲区中的任何数据都会被发送到设备（通常被设备忽略），随后每个发出的字节都会被相应的输入字节替换到缓冲区中。因此，传递给传输函数的所有缓冲区既是输入缓冲区也是输出缓冲区。

`spigen` 驱动通过以下 ioctl(2) 调用提供对 SPI 从设备的访问，这些调用定义于

`#include <sys/spigenio.h>`

```sh
struct spigen_transfer {
	struct iovec st_command;
	struct iovec st_data;
};
```

```sh
struct spigen_transfer_mmapped {
	size_t stm_command_length;
	size_t stm_data_length;
};
```

**`SPIGENIOC_TRANSFER`** （`struct spigen_transfer`）使用 `spigen_transfer` 中的 st_command 和 st_data 字段所描述的缓冲区，向/从设备传输命令和可选的关联数据。如果命令没有关联数据，请将 `st_data.iov_len` 设为零。

**`SPIGENIOC_TRANSFER_MMAPPED`** （`spigen_transfer_mmapped`）向/从设备传输命令和可选的关联数据。传输缓冲区是先前 mmap 映射的区域。该区域内命令和数据的长度由 `spigen_transfer_mmapped` 的 `stm_command_length` 和 `stm_data_length` 字段描述。如果 `stm_data_length` 不为零，则数据出现在该内存区域中紧随命令之后的位置（即从映射区域起始处偏移 `stm_command_length` 的位置）。

**`SPIGENIOC_GET_CLOCK_SPEED`** （`uint32_t`）获取与此从设备通信时使用的最大时钟速度（以赫兹为单位的总线频率）。

**`SPIGENIOC_SET_CLOCK_SPEED`** （`uint32_t`）设置与此从设备通信时使用的最大时钟速度（以赫兹为单位的总线频率）。该设置在后续传输中持续有效；不必在每次传输前重置。由于 SPI 总线控制器设备的硬件限制，实际总线频率可能更低。

**`SPIGENIOC_GET_SPI_MODE`** （`uint32_t`）获取与此设备通信时使用的 SPI 模式（时钟极性和相位）。

**`SPIGENIOC_SET_SPI_MODE`** （`uint32_t`）设置与此设备通信时使用的 SPI 模式（时钟极性和相位）。该设置在后续传输中持续有效；不必在每次传输前重置。

## HINTS 配置

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统（例如 `MIPS`）上，可对 `spigen` 进行以下配置：

**`hint.spigen.%d.at`** `spigen` 实例所附加到的 spibus。

**`hint.spigen.%d.clock`** 与此设备通信时使用的最大总线频率。实际总线速度可能更低，取决于 SPI 总线控制器硬件的能力。

**`hint.spigen.%d.cs`** 为此设备执行 I/O 时断言的片选号。设置最高位（1 << 31）以反转片选线的逻辑电平。

**`hint.spigen.%d.mode`** 与此设备通信时使用的 SPI 模式（0-3）。

## FDT 配置

在基于 [fdt(4)](fdt.4.md) 的系统上，spigen 设备被定义为 SPI 总线控制器节点的从设备子节点。`spibus.txt` 绑定文档中记录的所有属性都可用于 `spigen` 设备。下面记录最常用的属性。

`spigen` 设备子节点中需要以下属性：

**`compatible`** 必须为字符串 "freebsd,spigen"。

**`reg`** 设备的片选地址。

**`spi-max-frequency`** 与此从设备通信时使用的最大总线频率。实际总线速度可能更低，取决于 SPI 总线控制器硬件的能力。

`spigen` 设备子节点的以下属性是可选的：

**`spi-cpha`** 空属性，指示从设备需要移位时钟相位（CPHA）模式。

**`spi-cpol`** 空属性，指示从设备需要反向时钟极性（CPOL）模式。

**`spi-cs-high`** 空属性，指示从设备需要片选为高电平有效。

## 文件

**`/dev/spigen*`**

## 参见

[fdt(4)](fdt.4.md), [device.hints(5)](../man5/device.hints.5.md), [spi(8)](../man8/spi.8.md)

## 历史

`spigen` 驱动出现于 FreeBSD 11.0。FDT 支持出现于 FreeBSD 11.2。
