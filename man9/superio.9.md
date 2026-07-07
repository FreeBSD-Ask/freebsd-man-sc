# superio(9)

`superio` — Super I/O 总线接口

## 名称

`superio`, `superio_devid`, `superio_dev_disable`, `superio_dev_enable`, `superio_dev_enabled`, `superio_find_dev`, `superio_get_dma`, `superio_get_iobase`, `superio_get_irq`, `superio_get_ldn`, `superio_get_type`, `superio_read`, `superio_revid`, `superio_vendor`, `superio_write`

## 概要

```c
#include <sys/bus.h>
#include <dev/superio/superio.h>

uint16_t
superio_devid(device_t dev)

void
superio_dev_disable(device_t dev, uint8_t mask)

void
superio_dev_enable(device_t dev, uint8_t mask)

bool
superio_dev_enabled(device_t dev, uint8_t mask)

device_t
superio_find_dev(device_t dev, superio_dev_type_t type, int ldn)

uint8_t
superio_get_dma(device_t dev)

uint16_t
superio_get_iobase(device_t dev)

uint8_t
superio_get_irq(device_t dev)

uint8_t
superio_get_ldn(device_t dev)

superio_dev_type_t
superio_get_type(device_t dev)

uint8_t
superio_read(device_t dev, uint8_t reg)

uint8_t
superio_revid(device_t dev)

superio_vendor_t
superio_vendor(device_t dev)

void
superio_write(device_t dev, uint8_t reg, uint8_t val)
```

## 描述

`superio_write` 系列函数用于管理 Super I/O 设备。这些函数支持原始配置访问、定位设备、设备信息和设备配置。

### 控制器接口

`superio_vendor` 函数用于获取 Super I/O 控制器 `dev` 的供应商。可能的返回值是 `SUPERIO_VENDOR_ITE` 和 `SUPERIO_VENDOR_NUVOTON`。

`superio_devid` 函数用于获取 Super I/O 控制器 `dev` 的设备 ID。

`superio_revid` 函数用于获取 Super I/O 控制器 `dev` 的修订 ID。

`superio_find_dev` 函数用于在 [superio(4)](../man4/superio.4.md) 总线上查找由 `dev` 指定的、具有请求类型和逻辑设备号的设备。这两者中任一（但不是两者）可以是通配符。支持的类型有 `SUPERIO_DEV_GPIO`、`SUPERIO_DEV_HWM` 和 `SUPERIO_DEV_WDT`。`type` 的通配符值是 `SUPERIO_DEV_NONE`。`ldn` 的通配符值是 -1。

### 设备接口

`superio_read` 函数用于从设备 `dev` 的 Super I/O 配置寄存器读取数据。

`superio_write` 函数用于向设备 `dev` 的 Super I/O 配置寄存器写入数据。

`superio_dev_enable`、`superio_dev_disable` 和 `superio_dev_enabled` 函数用于启用、禁用或检查设备 `dev` 的状态。`mask` 参数选择支持子功能的设备的子功能。对于没有子功能的设备，`mask` 应设置为 1。

### 访问器接口

`superio_get_dma` 用于获取为设备 `dev` 配置的 DMA 通道号。

`superio_get_iobase` 用于获取为设备 `dev` 配置的基 I/O 端口。设备可能通过 I/O 端口公开额外或替代的配置访问。

`superio_get_irq` 用于获取为设备 `dev` 配置的中断号。

`superio_get_ldn` 用于获取设备 `dev` 的逻辑设备号。

`superio_get_type` 用于获取设备 `dev` 的类型。

## 参见

[superio(4)](../man4/superio.4.md), [device(9)](device.9.md), [driver(9)](driver.9.md)

## 作者

本手册页由 Andriy Gapon <avg@FreeBSD.org> 编写。
