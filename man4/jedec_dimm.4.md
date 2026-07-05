# jedec_dimm.4

`jedec_dimm` — 报告 JEDEC DDR3/DDR4 DIMM 的资产信息和温度

## 名称

`jedec_dimm`

## 概要

> device jedec_dimm
> device smbus

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
jedec_dimm_load="YES"
```

`必须在 /boot/device.hints 中手动指定寻址信息：`

```sh
hint.jedec_dimm.0.at="smbus0"
hint.jedec_dimm.0.addr="0xa0"
hint.jedec_dimm.0.slotid="Silkscreen"
```

## 描述

`jedec_dimm` 驱动报告 JEDEC DDR3 和 DDR4 DIMM 上“Serial Presence Detect”（SPD）数据中编码的资产信息（部件号、序列号）。它还计算并报告 DIMM 的内存容量（以兆字节为单位）。如果 DIMM 包含“Thermal Sensor On DIMM”（TSOD），还会报告温度。

`jedec_dimm` 驱动通过 smbus(4) 访问 SPD 和 TSOD。

数据通过 [sysctl(8)](../man8/sysctl.8.md) 接口报告；所有值均为只读：

**`dev.jedec_dimm.X.%desc`** DIMM 的字符串描述，如果存在则包括 TSOD 和 slotid 信息。

**`dev.jedec_dimm.X.capacity`** DIMM 的内存容量，以兆字节为单位。

**`dev.jedec_dimm.X.mfg_week`** DIMM 制造的当年的周次。

**`dev.jedec_dimm.X.mfg_year`** DIMM 制造的年份。

**`dev.jedec_dimm.X.part`** DIMM 的制造商部件号。

**`dev.jedec_dimm.X.serial`** DIMM 的制造商序列号。

**`dev.jedec_dimm.X.slotid`** 对应提示的副本（如果已设置）。

**`dev.jedec_dimm.X.temp`** 如果存在 TSOD，则为报告的温度。

**`dev.jedec_dimm.X.type`** DIMM 类型（DDR3 或 DDR4）。

这些值可通过 [device.hints(5)](../man5/device.hints.5.md) 为 `jedec_dimm` 进行配置：

**`hint.jedec_dimm.X.at`** DIMM 所连接的 smbus(4)。

**`hint.jedec_dimm.X.addr`** SPD 的 SMBus 地址。JEDEC 规定地址的最高四位是“Device Type Identifier”（DTI），且 SPD 的 DTI 为 0xa。由于 SMBus 地址的最低位是读/写位且始终写为 0，因此地址的最低四位必须为偶数。

**`hint.jedec_dimm.X.slotid`** 可选插槽标识符。如果填入主板上丝印的 DIMM 插槽名称，则提供 DIMM 插槽名称与 DIMM 序列号之间的映射。该映射对于详细的资产跟踪很有用，并使在更换时更容易在物理上定位特定 DIMM。在组装多个相同系统（如系统供应商可能做的那样）时非常有用。总线/地址与 DIMM 插槽之间的映射必须首先通过主板文档或试错法确定。

如果 DIMM 位于 [iicbus(4)](iicbus.4.md) 控制器后面的 I2C 总线上，则可使用 [iicsmb(4)](iicsmb.4.md) 桥接驱动来挂接 smbus(4)。

## 实例

考虑两个具有以下提示的 DDR4 DIMM：

```sh
hint.jedec_dimm.0.at="smbus0"
hint.jedec_dimm.0.addr="0xa0"
hint.jedec_dimm.0.slotid="A1"
hint.jedec_dimm.6.at="smbus1"
hint.jedec_dimm.6.addr="0xa8"
```

它们的 [sysctl(8)](../man8/sysctl.8.md) 输出（已排序）：

```sh
dev.jedec_dimm.0.%desc: DDR4 DIMM w/ Atmel TSOD (A1)
dev.jedec_dimm.0.%driver: jedec_dimm
dev.jedec_dimm.0.%location: addr=0xa0
dev.jedec_dimm.0.%parent: smbus0
dev.jedec_dimm.0.%pnpinfo:
dev.jedec_dimm.0.capacity: 16384
dev.jedec_dimm.0.mfg_week: 30
dev.jedec_dimm.0.mfg_year: 17
dev.jedec_dimm.0.part: 36ASF2G72PZ-2G1A2
dev.jedec_dimm.0.serial: 0ea815de
dev.jedec_dimm.0.slotid: A1
dev.jedec_dimm.0.temp: 32.7C
dev.jedec_dimm.0.type: DDR4
dev.jedec_dimm.6.%desc: DDR4 DIMM w/ TSE2004av compliant TSOD
dev.jedec_dimm.6.%driver: jedec_dimm
dev.jedec_dimm.6.%location: addr=0xa8
dev.jedec_dimm.6.%parent: smbus1
dev.jedec_dimm.6.%pnpinfo:
dev.jedec_dimm.6.capacity: 8192
dev.jedec_dimm.6.mfg_week: 13
dev.jedec_dimm.6.mfg_year: 19
dev.jedec_dimm.6.part: VRA9MR8B2H1603
dev.jedec_dimm.6.serial: 0c4c46ad
dev.jedec_dimm.6.temp: 43.1C
dev.jedec_dimm.6.type: DDR4
```

可以使用 smbmsg(8) 探测设备。

## 兼容性

`jedec_dimm` 实现了现已删除的 jedec_ts(4) 的功能超集。jedec_ts(4) 的提示可机械地转换为 `jedec_dimm` 使用。需要进行两处更改：

- 在所有 jedec_ts(4) 提示中，将“jedec_ts”替换为“jedec_dimm”。
- 在 jedec_ts(4) 的“addr”提示中，将 TSOD DTI“0x3”替换为 SPD DTI“0xa”。

以下 [sed(1)](../man1/sed.1.md) 脚本将执行必要的更改：

```sh
sed -i ".old" -e 's/jedec_ts/jedec_dimm/' \
    -e '/jedec_dimm/s/addr="0x3/addr="0xa/' /boot/device.hints
```

## 参见

[iicbus(4)](iicbus.4.md), [iicsmb(4)](iicsmb.4.md), smbus(4), [sysctl(8)](../man8/sysctl.8.md)

## 标准

（DDR3 SPD）

> JEDEC, "Standard 21-C, Annex K".

（DDR3 TSOD）

> JEDEC, "Standard 21-C, TSE2002av".

（DDR4 SPD）

> JEDEC, "Standard 21-C, Annex L".

（DDR4 TSOD）

> JEDEC, "Standard 21-C, TSE2004av".

## 历史

`jedec_dimm` 驱动最早出现于 FreeBSD 12.0。

## 作者

`jedec_dimm` 驱动和本手册页由 Ravi Pokala <rpokala@freebsd.org> 编写。两者都部分基于现已删除的 jedec_ts(4) 驱动和手册页，后者由 Andriy Gapon <avg@FreeBSD.org> 编写。
