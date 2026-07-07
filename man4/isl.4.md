# isl(4)

`isl` — Intersil(TM) I2C ISL29018 传感器驱动

## 名称

`isl`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device isl
> device ig4
> device iicbus

`或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
isl_load="YES"
ig4_load="YES"
```

`在许多 Chromebook 型号上，此驱动可在 chromebook_platform(4) 驱动的帮助下自动配置。或者，可以在 /boot/device.hints 中手动配置 isl 驱动：hint.isl.0.at="iicbus0" hint.isl.0.addr="0x88" hint.isl.1.at="iicbus1" hint.isl.1.addr="0x88"`

## 描述

`isl` 驱动为 Intersil(TM) I2C ISL29018 数字环境光传感器和带中断功能的接近传感器提供的传感器数据提供访问。功能为基础功能，通过 [sysctl(8)](../man8/sysctl.8.md) 接口提供。

在使用 [device.hints(5)](../man5/device.hints.5.md) 的系统上，`isl` 可配置以下值：

**`hint.isl.%d.at`** 目标 [iicbus(4)](iicbus.4.md)。

**`hint.isl.%d.addr`** `isl` 在 [iicbus(4)](iicbus.4.md) 上的 i2c 地址。

## SYSCTL 变量

以下 [sysctl(8)](../man8/sysctl.8.md) 变量可用：

**`dev.isl.X.als`** 当前 ALS（环境光传感器）读数。

**`dev.isl.X.ir`** 当前 IR（红外）传感器读数。

**`dev.isl.X.prox`** 当前接近传感器读数。

**`dev.isl.X.resolution`** 当前传感器分辨率。

**`dev.isl.X.range`** 当前传感器量程。

## 实例

### 读取环境光传感器

```sh
$ sysctl dev.isl.0.als
dev.isl.0.als: 64
```

### 自动调节亮度

这需要 `graphics/intel-backlight` port，仅适用于使用受支持 Intel(R) GPU 的笔记本电脑。

```sh
$ pkg install intel-backlight
$ sh /usr/local/share/examples/intel-backlight/isl_backlight.sh
```

## 参见

[chromebook_platform(4)](chromebook_platform.4.md), [ig4(4)](ig4.4.md), [iicbus(4)](iicbus.4.md)

## 作者

`isl` 驱动由 Michael Gmelin <freebsd@grem.de> 编写。

本手册页由 Michael Gmelin <freebsd@grem.de> 编写。

## 缺陷

`isl` 驱动基于 I2C 地址检测设备。如果将初始化序列发送到该地址上的未知设备，可能会产生不可预见的后果。
