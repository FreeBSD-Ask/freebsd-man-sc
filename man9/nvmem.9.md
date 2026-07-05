# nvmem.9.md

`nvmem` — 非易失性内存单元访问

## 名称

`nvmem`, `nvmem_get_cell_len`, `nvmem_read_cell_by_name`, `nvmem_read_cell_by_idx`, `nvmem_write_cell_by_name`, `nvmem_write_cell_by_idx`

## 概要

```c
options FDT
device nvmem
```

```c
#include <sys/extres/nvmem/nvmem.h>
```

```c
int
nvmem_get_cell_len(phandle_t node, const char *name)

int
nvmem_read_cell_by_name(phandle_t node, const char *name, void *cell, size_t buflen)

int
nvmem_read_cell_by_idx(phandle_t node, int idx, void *cell, size_t buflen)

int
nvmem_write_cell_by_name(phandle_t node, const char *name, void *cell, size_t buflen)

int
nvmem_write_cell_by_idx(phandle_t node, int idx, void *cell, size_t buflen)
```

## 描述

在某些嵌入式主板上，制造商将一些数据存储在 NVMEM（非易失性内存）上，这些数据通常存储在某些 eeprom 或熔丝中。

`nvmem_write_cell_by_idx` API 由供消费者使用的辅助函数和供提供者使用的设备方法组成。

## 函数

**`nvmem_get_cell_len`** `phandle_t node, const char *name` 根据节点上的 reg 属性获取单元的大小。返回大小，如果未找到单元名称则返回 ENOENT。

**`nvmem_read_cell_by_name`** `phandle_t node, const char *name, void *cell, size_t buflen` 根据名称获取单元内容。成功返回 0，如果单元不存在返回 ENOENT，如果未找到提供者设备返回 ENXIO，如果大小不正确返回 EINVAL。

**`nvmem_read_cell_by_idx`** `phandle_t node, int idx, void *cell, size_t buflen` 根据索引获取单元内容。成功返回 0，如果单元不存在返回 ENOENT，如果未找到提供者设备返回 ENXIO，如果大小不正确返回 EINVAL。

**`nvmem_write_cell_by_name`** `phandle_t node, const char *name, void *cell, size_t buflen` 根据名称写入单元内容。成功返回 0，如果单元不存在返回 ENOENT，如果未找到提供者设备返回 ENXIO，如果大小不正确返回 EINVAL。

**`nvmem_write_cell_by_idx`** `phandle_t node, int idx, void *cell, size_t buflen` 根据索引写入单元内容。成功返回 0，如果单元不存在返回 ENOENT，如果未找到提供者设备返回 ENXIO，如果大小不正确返回 EINVAL。

## 设备方法

**`nvmem_read`** `device_t dev, uint32_t offset, uint32_t size, uint8_t *buffer` 提供者设备方法，用于读取单元内容。

**`nvmem_write`** `device_t dev, uint32_t offset, uint32_t size, uint8_t *buffer` 提供者设备方法，用于写入单元内容。

## 实例

考虑以下 DTS

```dts
/* 提供者 */
eeprom: eeprom@20000 {
	board_id: id@0 {
		reg = <0x0 0x4>;
	};
};
/* 消费者 */
device@30000 {
	...
	nvmem-cells = <&board_id>
	nvmem-cell-names = "boardid";
};
```

eeprom@20000 的设备驱动程序需要将自身暴露为提供者

```c
#include "nvmem_if.h"
int
foo_nvmem_read(device_t dev, uint32_t offset, uint32_t size, uint8_t *buffer)
{
	/* 读取数据 */
}
int
foo_attach(device_t dev)
{
	phandle_t node;
	node = ofw_bus_get_node(dev);
	...
	/* 注册设备以便消费者能够找到我们 */
	OF_device_register_xref(OF_xref_from_node(node), dev);
	...
}
static device_method_t foo_methods[] = {
	...
	/* nvmem 接口 */
	DEVMETHOD(nvmem_read, foo_nvmem_read),
	/* 终止方法列表 */
	DEVMETHOD_END
};
```

device@30000 的消费者设备驱动程序现在可以读取 nvmem 数据

```c
int
bar_attach(device_t dev)
{
	phandle_t node;
	uint32_t boardid;
	...
	node = ofw_bus_get_node(dev);
	nvmem_read_cell_by_name(node, "boardid", (void *)&boardid, sizeof(boardid));
	...
}
```

## 历史

nvmem 相关函数首次出现于 FreeBSD 12.0。nvmem 接口和手册页由 Emmanuel Vadot <manu@FreeBSD.org> 编写。
