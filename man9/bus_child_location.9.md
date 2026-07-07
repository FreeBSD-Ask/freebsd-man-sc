# BUS_CHILD_LOCATION(9)

`BUS_CHILD_LOCATION` — 获取子设备在总线上的位置

## 名称

`BUS_CHILD_LOCATION`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <sys/sbuf.h>
```

```c
void
BUS_CHILD_LOCATION(device_t dev, device_t child, struct sbuf *sb)
```

## 描述

`BUS_CHILD_LOCATION` 方法返回 `child` 设备的位置。该位置是一系列 key=value 对。字符串必须格式化为以空格分隔的 key=value 对列表。名称只能包含字母数字字符、下划线（`_`）和连字符（`-`）。值可以包含任何非空白字符。包含空白的值可以用双引号（`"`）括起来。引号内的双引号和反斜杠可以用反斜杠（`\`）转义。

位置定义为 `child` 设备的一系列特征，可用于定位该设备而与所附加的驱动程序无关。通常这些是插槽号、总线地址或某种拓扑结构。在可能的情况下，鼓励总线提供从一次启动到另一次启动、以及在添加或删除其他设备时保持稳定的位置。位置不依赖于该位置上的设备类型。

## 参见

bus(9), [device(9)](device.9.md)
