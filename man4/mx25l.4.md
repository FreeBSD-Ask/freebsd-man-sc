# mx25l.4

`mx25l` — SpiFlash 兼容非易失性存储设备驱动

## 名称

`mx25l`

## 概要

`device mx25l`

`在 loader.conf(5) 中：mx25l_load="YES"`

## 描述

`mx25l` 驱动提供对统称为 SpiFlash(tm) 的非易失性存储设备系列的支持。SpiFlash 芯片的部件号通常以 EN25、IS25、MX25、S25、SST25 或 W25 开头。

`mx25l` 驱动使用操作码 0x9f 读取制造商和设备 ID 数据，以确定设备是否受支持。设备 ID 通过驱动程序内的数据表查找，该表描述了每个受支持设备的属性，如块大小、扇区大小和设备容量。找到受支持的设备时，`mx25l` 驱动会创建一个磁盘设备，并可通过 **`/dev/flash/spi?`** 访问。然后，新的磁盘设备会像任何磁盘设备一样被可用的 [geom(4)](geom.4.md) 模块品尝。

## 硬件

`mx25l` 驱动支持以下 spi 闪存设备：

- AT25DF641
- EN25F32
- EN25P32
- EN25P64
- EN25Q32
- EN25Q64
- GD25Q64
- M25P32
- M25P64
- MX25L1606E
- MX25LL128
- MX25LL256
- MX25LL32
- MX25LL64
- N25Q64
- S25FL032
- S25FL064
- S25FL128
- S25FL256S
- SST25VF010A
- SST25VF032B
- W25Q128
- W25Q256
- W25Q32
- W25Q64
- W25Q64BV
- W25X32
- W25X64

## FDT 配置

在基于 [fdt(4)](fdt.4.md) 的系统上，`mx25l` 设备被定义为 SPI 总线控制器节点的从设备子节点。`spibus.txt` 绑定文档中记录的所有属性都可用于 `mx25l` 设备。最常用的属性记录如下。

`mx25l` 设备子节点中需要以下属性：

**`compatible`** 必须为字符串 "jedec,spi-nor"。

**`reg`** 设备的片选地址。

**`spi-max-frequency`** 与此从设备通信时使用的最大总线频率。实际总线速度可能较低，取决于 SPI 总线控制器硬件的能力。

`mx25l` 设备子节点的以下属性是可选的：

**`spi-cpha`** 空属性，指示从设备需要移位时钟相位（CPHA）模式。

**`spi-cpol`** 空属性，指示从设备需要反相时钟极性（CPOL）模式。

**`spi-cs-high`** 空属性，指示从设备需要片选高电平有效。

## 提示配置

在基于 [device.hints(5)](../man5/device.hints.5.md) 的系统上（例如 `MIPS`），这些值可用于配置 `mx25l`：

**`hint.mx25l.%d.at`** `mx25l` 实例所连接的 spibus。

**`hint.mx25l.%d.clock`** 与此设备通信时使用的最大总线频率。实际总线速度可能较低，取决于 SPI 总线控制器硬件的能力。

**`hint.mx25l.%d.cs`** 为此设备执行 I/O 时要置位的片选号。设置最高位（1 << 31）以反转片选线的逻辑电平。

**`hint.mx25l.%d.mode`** 与此设备通信时使用的 SPI 模式（0-3）。

## 文件

**`/dev/flash/spi?`** 提供对存储设备的读/写访问。

## 参见

[fdt(4)](fdt.4.md), [geom(4)](geom.4.md)

## 历史

`mx25l` 驱动首次出现于 FreeBSD 8.0。
