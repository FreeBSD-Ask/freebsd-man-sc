# amdtemp(4)

`amdtemp` — AMD 处理器片上数字温度传感器设备驱动

## 名称

`amdtemp` AMD 处理器片上数字温度传感器

## 概要

要将此驱动编译进内核，请将以下行放入你的内核配置文件中：

> device amdtemp

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
amdtemp_load="YES"
```

## 描述

`amdtemp` 驱动为 AMD Family 0Fh、10h、11h、12h、14h、15h、16h 和 17h 处理器中存在的片上数字温度传感器提供支持。

对于 Family 0Fh 处理器，`amdtemp` 驱动通过名为 `dev.amdtemp.%d.core{0,1}.sensor{0,1}` 的 sysctl 节点报告每个核心的温度。该驱动还会在相应 CPU 设备的 sysctl 树中创建 `dev.cpu.%d.temperature`，显示每个 CPU 核心中两个传感器的最高温度。

对于 Family 10h、11h、12h、14h、15h、16h 和 17h 处理器，该驱动通过名为 `dev.amdtemp.%d.core0.sensor0` 的 sysctl 节点报告每个封装的温度。该驱动还会在相应 CPU 设备的 sysctl 树中创建 `dev.cpu.%d.temperature`，显示每个 CPU 封装中共享传感器的温度。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数提供：

**`dev.amdtemp.%d.sensor_offset`**

将给定偏移量加到传感器温度上。默认为 0。

## 参见

[coretemp(4)](coretemp.4.md), [loader(8)](../man8/loader.8.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`amdtemp` 驱动首次出现于 FreeBSD 7.1。

## 作者

Rui Paulo <rpaulo@FreeBSD.org> Norikatsu Shigemura <nork@FreeBSD.org> Jung-uk Kim <jkim@FreeBSD.org>

## 注意事项

对于 Family 10h 及更高版本的处理器，根据

> "BIOS and Kernel Developer's Guide (BKDG) for AMD Processors"。

“（所报告的温度）是在任意刻度上测量的非物理温度，它并不代表实际的物理温度，如芯片温度或外壳温度。相反，它指定了相对于系统必须为处理器规定的最大外壳温度和最大散热功率提供最大散热的那个点的处理器温度”
