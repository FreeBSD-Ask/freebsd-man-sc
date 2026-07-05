# htu21.4

`htu21` — HTU21D 及兼容温湿度传感器驱动

## 名称

`htu21`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device htu21
> device iicbus

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
htu21_load="YES"
```

## 描述

`htu21` 驱动通过 I2C 总线为以下支持的传感器提供温度和相对湿度读数：

- HTU21D
- SHT21
- Si7021

`htu21` 驱动通过 [sysctl(8)](../man8/sysctl.8.md) 条目报告数据，位于 [sysctl(8)](../man8/sysctl.8.md) 树中设备节点下：

**temperature** 温度，单位为百分之一开尔文。

**humidity** 相对湿度，单位为百分之一百分比。

**crc_errors** 从设备读取测量数据时的 CRC 错误次数。

**power** 电源状态良好指示。对于电池供电的传感器很有用。

**heater** 内置加热器控制。加热器可用于测试以及在高湿度后从饱和状态恢复。

**hold_bus** 传感器在执行测量时是否将 SCL 保持为低电平。通常，传感器会释放总线并在测量完成前对所有访问返回 NACK。保持模式在多主控环境中可能有用。

在基于 FDT(4) 的系统上，必须设置以下属性：

**`compatible`** 必须设置为 "meas,htu21"。

**`reg`** `htu21` 的 I2C 地址。不过，在所有支持的传感器上它都硬连接为 0x40（7 位）。

`htu21` 设备的 DTS 部分通常如下所示：

```sh
/ {
	...
	htu21d {
		compatible = "meas,htu21";
		reg = <0x40>;
	};
};
```

## 参见

[fdt(4)](fdt.4.md), [iicbus(4)](iicbus.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`htu21` 驱动和本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。

## 缺陷

无法控制测量分辨率。

某些传感器变体不提供序列号，或使用不兼容的格式。`htu21` 驱动不区分这些变体，可能会报告序列号校验和不正确。
