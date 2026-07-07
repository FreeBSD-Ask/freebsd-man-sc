# BUS_BIND_INTR(9)

`BUS_BIND_INTR` — 将中断资源绑定到特定 CPU

## 名称

`BUS_BIND_INTR`, `bus_bind_intr`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
```

```c
int
BUS_BIND_INTR(device_t dev, device_t child, struct resource *irq,
    int cpu)

int
bus_bind_intr(device_t dev, struct resource *irq, int cpu)
```

## 描述

`BUS_BIND_INTR` 方法允许将中断资源固定到特定 CPU。该中断资源必须已通过 [BUS_SETUP_INTR(9)](bus_setup_intr.9.md) 附加了中断处理程序。`cpu` 参数对应于系统中某个有效 CPU 的 ID。绑定中断会将任何关联中断线程的 cpuset(2) 限制为仅包含指定的 CPU。它也可能将中断的低级中断处理定向到指定的 CPU，但此行为与平台相关。如果 `cpu` 使用 `NOCPU` 值，则该中断将被"解除绑定"，从而将任何关联的中断线程恢复为默认 cpuset。

在调用这些函数期间不应持有不可睡眠的锁，例如互斥锁。

`bus_bind_intr` 函数是 `BUS_BIND_INTR` 的简单封装。

注意，目前不会对来自同一设备或多个设备的同一中断的多个绑定请求进行仲裁。用户态通过 cpuset(2) 提交的中断绑定请求与 `BUS_BIND_INTR` 之间也没有仲裁。最近的绑定请求将生效。

## 返回值

成功时返回零，否则返回一个适当的错误。

## 参见

cpuset(2), [BUS_SETUP_INTR(9)](bus_setup_intr.9.md), [device(9)](device.9.md)

## 历史

`BUS_BIND_INTR` 方法和 `bus_bind_intr` 函数首次出现于 FreeBSD 7.2。
