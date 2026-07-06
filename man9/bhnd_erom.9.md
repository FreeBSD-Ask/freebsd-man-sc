# bhnd\_erom.9

`bhnd_erom` — BHND 设备枚举表解析

## 名称

`bhnd_erom`, `bhnd_erom_alloc`, `bhnd_erom_dump`, `bhnd_erom_fini_static`, `bhnd_erom_free`, `bhnd_erom_free_core_table`, `bhnd_erom_get_core_table`, `bhnd_erom_init_static`, `bhnd_erom_io`, `bhnd_erom_io_fini`, `bhnd_erom_io_map`, `bhnd_erom_io_read`, `bhnd_erom_iobus_init`, `bhnd_erom_iores_new`, `bhnd_erom_lookup_core`, `bhnd_erom_lookup_core_addr`, `bhnd_erom_probe`, `bhnd_erom_probe_driver_classes`

## 概要

```c
#include <dev/bhnd/bhnd.h>
#include <dev/bhnd/bhnd_erom.h>

typedef struct bhnd_erom bhnd_erom_t;
typedef struct kobj_class bhnd_erom_class_t;
typedef struct bhnd_erom_static bhnd_erom_static_t;

int
bhnd_erom_probe(bhnd_erom_class_t *cls, struct bhnd_erom_io *eio,
    const struct bhnd_chipid *hint, struct bhnd_chipid *cid)

bhnd_erom_class_t *
bhnd_erom_probe_driver_classes(devclass_t bus_devclass,
    struct bhnd_erom_io *eio, const struct bhnd_chipid *hint,
    struct bhnd_chipid *cid)

bhnd_erom_t *
bhnd_erom_alloc(bhnd_erom_class_t *cls, const struct bhnd_chipid *cid,
    struct bhnd_erom_io *eio)

void
bhnd_erom_free(bhnd_erom_t *erom)

int
bhnd_erom_init_static(bhnd_erom_class_t *cls, bhnd_erom_t *erom,
    size_t esize, const struct bhnd_chipid *cid, struct bhnd_erom_io *eio)

void
bhnd_erom_fini_static(bhnd_erom_t *erom)

int
bhnd_erom_dump(bhnd_erom_t *erom)

int
bhnd_erom_get_core_table(bhnd_erom_t *erom, struct bhnd_core_info **cores,
    u_int *num_cores)

void
bhnd_erom_free_core_table(bhnd_erom_t *erom, struct bhnd_core_info *cores)

int
bhnd_erom_lookup_core(bhnd_erom_t *erom, const struct bhnd_core_match *desc,
    struct bhnd_core_info *core)

int
bhnd_erom_lookup_core_addr(bhnd_erom_t *erom,
    const struct bhnd_core_match *desc, bhnd_port_type type, u_int port,
    u_int region, struct bhnd_core_info *core, bhnd_addr_t *addr,
    bhnd_size_t *size)
```

### 总线空间 I/O

```c
struct bhnd_erom_io *
bhnd_erom_iores_new(device_t dev, int rid)

int
bhnd_erom_iobus_init(struct bhnd_erom_iobus *iobus, bhnd_addr_t addr,
    bhnd_size_t size, bus_space_tag_t bst, bus_space_handle_t bsh)

void
bhnd_erom_io_fini(struct bhnd_erom_io *eio)

int
bhnd_erom_io_map(struct bhnd_erom_io *eio, bhnd_addr_t addr,
    bhnd_size_t size)

uint32_t
bhnd_erom_io_read(struct bhnd_erom_io *eio, bhnd_size_t offset, u_int width)
```

```c
#include <dev/bhnd/bhnd_eromvar.h>
```

```c
struct bhnd_erom_io {
	bhnd_erom_io_map_t	*map;
	bhnd_erom_io_read_t	*read;
	bhnd_erom_io_fini_t	*fini;
};
```

## 描述

`bhnd_erom_probe_driver_classes` 框架为 [bhnd(4)](../man4/bhnd.4.md) 总线驱动程序支持的 BHND 设备枚举表格式提供了通用解析器接口。

`bhnd_erom_probe` 函数用于识别 [bhnd(4)](../man4/bhnd.4.md) 总线设备，并确定 erom 类 `cls` 是否能够解析其设备枚举表。如果成功，探测到的芯片标识将写入 `cid` 指向的位置。

必须使用 `eio` 参数提供映射第一个硬件核设备寄存器的总线 I/O 实例指针。可以使用 `bhnd_erom_io_map` 映射寄存器。

在不通过第一个硬件核提供标准 [bhnd_chipc(4)](../man4/bhnd_chipc.4.md) 芯片标识寄存器的设备上，必须使用 `hint` 参数指定设备的芯片信息指针。否则，`hint` 参数应为 `NULL`。

`bhnd_erom_probe_driver_classes` 函数是 `bhnd_erom_probe` 的便利包装器。此函数将迭代设备类 `bus_devclass` 中的所有驱动程序实例，使用 bhnd_driver_get_erom_class(9) 获取每个驱动程序的 erom 类并探测由 `eio` 映射的硬件核。成功时返回具有最高探测优先级的 erom 类指针。如果 erom 类没有成功的探测结果，返回 `NULL`。

`bhnd_erom_alloc` 函数为 `cid` 标识的芯片分配并返回设备枚举类 `cls` 的新解析器实例，使用总线 I/O 实例 `eio` 映射和读取设备表。成功时，返回的 `bhnd_erom_t` 承担 `eio` 的所有权。

`bhnd_erom_free` 函数释放使用 `bhnd_erom_alloc` 成功分配的 erom 解析器持有的所有资源。

客户端可以使用 `bhnd_erom_init_static` 自行管理内存分配。这在 [malloc(9)](malloc.9.md) 初始化之前执行设备枚举等情况下很有用。调用 `bhnd_erom_init_static` 时，`erom` 设置为指向实例内存的指针，`esize` 为可用总字节数。

`bhnd_erom_static` 结构足够大，可以静态分配任何支持的解析器类实例状态。指向 `bhnd_erom_static` 结构的指针可以转换为 `bhnd_erom_t`。

`bhnd_erom_fini_static` 函数释放使用 `bhnd_erom_init_static` 成功初始化的 erom 解析器持有的所有资源。

`bhnd_erom_dump` 函数枚举并打印 `erom` 中的所有设备表条目。

`bhnd_erom_get_core_table` 函数枚举 `erom` 中的所有设备表条目，在 `cores` 中返回核信息结构表，在 `num_cores` 中返回计数。为表分配的内存必须使用 `bhnd_erom_free_core_table` 释放。

`bhnd_erom_free_core_table` 函数释放先前调用 `bhnd_erom_get_core_table` 时分配的任何内存。

`bhnd_erom_lookup_core` 函数定位 `erom` 中第一个匹配核匹配描述符 `desc` 的设备表条目，将匹配条目的核信息写入 `core`。

`bhnd_erom_lookup_core_addr` 函数定位 `erom` 中第一个匹配核匹配描述符 `desc` 的设备表条目，获取映射到 `type` 类型 `port` 的内存区域 `region` 的基地址和大小。成功时，匹配条目的核信息写入 `core`，端口区域的基地址写入 `addr`，端口区域的总大小写入 `size`。如果不需要核信息，将 `core` 设置为 `NULL`。

### 总线空间 I/O

`bhnd_erom_io` 结构提供了一组 I/O 回调，由 `bhnd_erom_probe_driver_classes` 用于映射和读取设备枚举表。客户端可以使用现有的 `bhnd_erom_iores_new` 或 `bhnd_erom_iobus_init` 函数分配总线 I/O 实例，或直接实现 `bhnd_erom_io` 回调。

`bhnd_erom_io` 结构包含这些必填字段：

**`map`** 实现 `bhnd_erom_io_map` 的函数。

**`read`** 实现 `bhnd_erom_io_read` 的函数。

**`fini`** 实现 `bhnd_erom_io_fini` 的函数。

`bhnd_erom_iores_new` 函数分配并返回一个新的总线 I/O 实例，该实例将使用 bhnd_alloc_resource(9) 按需从设备 `dev` 分配 `SYS_RES_MEMORY` 总线资源（资源 ID 为 `rid`）来执行映射。

`bhnd_erom_iobus_init` 函数初始化调用者分配的总线 I/O 实例 `iobus`，该实例将使用总线空间标签 `bst` 和句柄 `bsh` 执行总线 I/O。`bsh` 映射的基地址和总大小应使用 `addr` 和 `size` 参数指定。

`bhnd_erom_io_fini` 函数释放总线 I/O 实例 `eio` 持有的所有资源。

`bhnd_erom_io_map` 函数用于请求总线 I/O 实例 `eio` 在总线地址 `addr` 处映射大小为 `size` 的 [bhnd(4)](../man4/bhnd.4.md) 总线空间。

`bhnd_erom_io_read` 函数用于从总线 I/O 实例 `eio` 的 `offset` 处读取 `width` 字节的数据项，相对于先前使用 `bhnd_erom_io_map` 映射的总线地址。

`width` 必须是 1、2 或 4 字节之一。

## 返回值

`bhnd_erom_probe` 函数返回标准的 [DEVICE_PROBE(9)](DEVICE_PROBE.9.md) 结果。

等于或小于零的返回值表示成功。大于零的值表示错误，并将是适当的错误代码。对于小于或等于零的值，应使用返回最高值的 erom 类来解析 erom 表。如果解析器不支持设备，返回 `ENXIO`。

`bhnd_erom_probe_driver_classes` 函数成功时返回指向探测到的 `bhnd_erom_class_t` 实例的指针，否则返回空指针。

`bhnd_erom_alloc` 函数成功时返回指向 `bhnd_erom_t` 的指针，如果分配或初始化 EROM 解析器时出错则返回 `NULL`。

`bhnd_erom_init_static` 函数成功时返回 0，如果分配大小小于 erom 类所需则返回 `ENOMEM`，如果初始化以其他方式失败则返回适当的错误代码。

`bhnd_erom_lookup_core` 函数成功时返回 0，如果未找到匹配的核则返回 `ENOENT`，如果解析设备表以其他方式失败则返回适当的错误代码。

`bhnd_erom_dump`、`bhnd_erom_get_core_table`、`bhnd_erom_iobus_init`、`bhnd_erom_io_map` 函数成功时返回 0，否则返回适当的错误代码。

## 参见

[bhnd(4)](../man4/bhnd.4.md), [bhnd(9)](bhnd.9.md), bhnd_alloc_resource(9), bhnd_driver_get_erom_class(9), [bus_space(9)](bus_space.9.md)

## 作者

`bhnd_erom_probe_driver_classes` 框架和本手册页由 Landon Fuller <landonf@FreeBSD.org> 编写。
