# owll.9

`owll` — Dallas Semiconductor 1-Wire 链路层接口

## 名称

`owll`, `OWLL_WRITE_ONE`, `OWLL_WRITE_ZERO`, `OWLL_READ_DATA`, `OWLL_REASET_AND_PRESENCE`

## 概要

```c
int
OWLL_WRITE_ONE(device_t lldev, struct ow_timing *timing)

int
OWLL_WRITE_ZERO(device_t lldev, struct ow_timing *timing)

int
OWLL_READ_DATA(device_t lldev, struct ow_timing *timing, int *bit)

int
OWLL_RESET_AND_PRESENCE(device_t lldev, struct ow_timing *timing,
    int *bit)
```

## 描述

`OWLL_REASET_AND_PRESENCE` 接口提供从协议的上层访问 Dallas Semiconductor 1-Wire 链路层的途径。

`OWLL_WRITE_ONE` 和 `OWLL_WRITE_ZERO` 分别在 1-Wire 总线上写入一个为 1 的位或一个为 0 的位。

`OWLL_READ_DATA` 从 1-Wire 总线读取一个位。这在 1-Wire 设备数据手册中通常被称为“Read Time Slot”。

`OWLL_RESET_AND_PRESENCE` 函数启动复位序列并检测总线上是否存在任何设备。这是所有 1-Wire 事务的开始。

## 注意事项

此接口旨在仅由 [ow(4)](../man4/ow.4.md) 设备用于与低层总线通信。按照约定，实现此接口的设备称为 [owc(4)](../man4/owc.4.md)。只有实现 [own(9)](own.9.md) 的设备才应调用这些接口。

## 参见

[ow(4)](../man4/ow.4.md), [owc(4)](../man4/owc.4.md), [own(9)](own.9.md)

## 法律条款

1-Wire 是 Maxim Integrated Products, Inc. 的注册商标。

## 历史

`OWLL_REASET_AND_PRESENCE` 驱动程序首次出现在 FreeBSD 11.0 中。

## 作者

`OWLL_REASET_AND_PRESENCE` 设备驱动程序和本手册页由 Warner Losh 编写。
