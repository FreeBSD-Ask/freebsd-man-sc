# bus_generic_print_child(9)

`bus_generic_print_child` — [BUS_PRINT_CHILD(9)](bus_print_child.9.md) 的通用实现

## 名称

`bus_generic_print_child`, `bus_print_child_domain`, `bus_print_child_footer`, `bus_print_child_header`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>

int
bus_generic_print_child(device_t dev, device_t child)

int
bus_print_child_domain(device_t dev, device_t child)

int
bus_print_child_footer(device_t dev, device_t child)

int
bus_print_child_header(device_t dev, device_t child)
```

## 描述

`bus_generic_print_child` 打印默认的设备通告消息。假设总线 'bar0' 上的设备 'foo0'，foo0 的描述为 "FooCard 1234" 且关联 NUMA 域 1，将打印以下内容：

```c
foo0: <FooCard 1234> numa-domain 1 on bar0
```

`bus_generic_print_child` 调用三个辅助函数 `bus_print_child_header`、`bus_print_child_domain` 和 `bus_print_child_footer`。

`bus_print_child_header` 输出设备名和单元号，后跟尖括号中的设备描述（"foo0: <FooCard 1234>"）

`bus_print_child_domain` 如果 `bus_get_domain` 为设备返回有效域，则输出 "numa-domain" 后跟域号（"numa-domain 1"）。如果 `dev` 未关联有效域，则不输出任何内容。

`bus_print_child_footer` 输出字符串 "on" 后跟父设备的名称和单元号（"on bar0"）

如果 `bus_generic_print_child` 不足以满足需求，可以使用这些函数在总线驱动程序中实现 [BUS_PRINT_CHILD(9)](bus_print_child.9.md)。

## 返回值

输出的字符数。

## 参见

[BUS_PRINT_CHILD(9)](bus_print_child.9.md), [device(9)](device.9.md)

## 作者

本手册页由 Doug Rabson 编写。
