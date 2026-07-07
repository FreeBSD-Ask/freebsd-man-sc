# BUS_CHILD_PNPINFO(9)

`BUS_CHILD_PNPINFO` — 从设备获取即插即用信息

## 名称

`BUS_CHILD_PNPINFO`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <sys/sbuf.h>
```

```c
void
BUS_CHILD_PNPINFO(device_t dev, device_t child, struct sbuf *sb)
```

## 描述

`BUS_CHILD_PNPINFO` 方法返回关于 `child` 设备的标识信息。某些总线将此信息称为即插即用（pnp）详细信息。此信息是一系列 key=value 对。字符串必须格式化为以空格分隔的 key=value 对列表。名称只能包含字母数字字符、下划线（`_`）和连字符（`-`）。值可以包含任何非空白字符。包含空白的值可以用双引号（`"`）括起来。引号内的双引号和反斜杠可以用反斜杠（`\`）转义。

pnpinfo 定义为 `child` 设备的一系列特征，这些特征与所附加的驱动程序无关，但用于允许驱动程序认领设备。通常，即插即用信息编码了设备的制造商、型号以及一些关于设备的通用详细信息。按照惯例，仅报告该总线上的驱动程序用来决定是否接受该设备的通用信息。不报告设备运行所需但不能将其与其他设备广泛区分开来的其他配置信息（如缓存突发大小）。

## 参见

bus(9), [device(9)](device.9.md)
