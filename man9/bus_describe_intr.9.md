# BUS_DESCRIBE_INTR(9)

`BUS_DESCRIBE_INTR` — 为活动中断处理程序关联描述

## 名称

`BUS_DESCRIBE_INTR`, `bus_describe_intr`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
BUS_DESCRIBE_INTR(device_t dev, device_t child, struct resource *irq,
    void *cookie, const char *descr)

int
bus_describe_intr(device_t dev, struct resource *irq, void *cookie,
    const char *fmt, ...)
```

## 描述

`BUS_DESCRIBE_INTR` 方法为活动中断处理程序关联一段描述。`cookie` 参数必须是针对中断 `irq` 成功调用 [BUS_SETUP_INTR(9)](bus_setup_intr.9.md) 所返回的值。

`bus_describe_intr` 函数是 `BUS_DESCRIBE_INTR` 的简单封装。作为便利，`bus_describe_intr` 允许调用者使用 [printf(9)](printf.9.md) 风格的格式化，通过 `fmt` 构建描述字符串。

当通过 [BUS_SETUP_INTR(9)](bus_setup_intr.9.md) 建立中断处理程序时，该处理程序以建立处理程序所针对的设备命名。此名称随后用于多处，例如 [systat(1)](../man1/systat.1.md) 和 [vmstat(8)](../man8/vmstat.8.md) 显示的中断统计信息。对于使用单个中断的设备，设备名已足够唯一地标识中断处理程序。然而，对于使用多个中断的设备，区分各中断处理程序会很有用。为活动中断处理程序设置描述时，会在设备名后追加冒号和描述，构成中断处理程序名。

## 返回值

成功时返回零，否则返回一个适当的错误。

## 参见

[systat(1)](../man1/systat.1.md), [vmstat(8)](../man8/vmstat.8.md), [BUS_SETUP_INTR(9)](bus_setup_intr.9.md), [device(9)](device.9.md), [printf(9)](printf.9.md)

## 历史

`BUS_DESCRIBE_INTR` 方法和 `bus_describe_intr` 函数首次出现于 FreeBSD 8.1。

## 缺陷

目前无法从活动中断处理程序中移除描述。
