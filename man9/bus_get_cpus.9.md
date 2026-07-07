# BUS_GET_CPUS(9)

`BUS_GET_CPUS` — 请求一组设备特定的 CPU

## 名称

`BUS_GET_CPUS`, `bus_get_cpus`

## 概要

```c
#include <sys/param.h>
#include <sys/bus.h>
#include <sys/cpuset.h>
```

```c
int
BUS_GET_CPUS(device_t dev, device_t child, enum cpu_sets op,
    size_t setsize, cpuset_t *cpuset)

int
bus_get_cpus(device_t dev, enum cpu_sets op, size_t setsize,
    cpuset_t *cpuset)
```

## 描述

`BUS_GET_CPUS` 方法向父总线设备查询一组设备特定的 CPU。`op` 参数指定要获取的 CPU 集合类型。如果成功，请求的 CPU 集合将通过 `cpuset` 返回。`setsize` 参数指定传入 `cpuset` 的集合大小（以字节为单位）。

`BUS_GET_CPUS` 通过 `op` 参数支持查询不同类型的 CPU 集合。并非所有设备都支持所有集合类型。如果某个集合类型不受支持，`BUS_GET_CPUS` 将以 `EINVAL` 失败。支持的集合类型如下：

**`LOCAL_CPUS`** 设备本地的 CPU 集合。如果设备在非一致性内存架构（NUMA）系统中更靠近某个特定内存域，则返回该内存域中的 CPU 集合。

**`INTR_CPUS`** 该设备用于设备中断的首选 CPU 集合。所有总线驱动程序都必须支持此集合类型。

`bus_get_cpus` 函数是 `BUS_GET_CPUS` 的简单封装。

## 返回值

成功时返回零，否则返回一个适当的错误。

## 参见

cpuset(2), [BUS_BIND_INTR(9)](bus_bind_intr.9.md), [device(9)](device.9.md)

## 历史

`BUS_GET_CPUS` 方法和 `bus_get_cpus` 函数首次出现于 FreeBSD 11.0。
