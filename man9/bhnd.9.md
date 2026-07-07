# bhnd(9)

`bhnd` — BHND 驱动程序编程接口

## 名称

`bhnd`

## 概要

```c
#include <dev/bhnd/bhnd.h>
```

### 总线资源函数

```c
int
bhnd_activate_resource(device_t dev, int type, int rid,
    struct bhnd_resource *r)

struct bhnd_resource *
bhnd_alloc_resource(device_t dev, int type, int *rid, rman_res_t start,
    rman_res_t end, rman_res_t count, u_int flags)

struct bhnd_resource *
bhnd_alloc_resource_any(device_t dev, int type, int *rid, u_int flags)

int
bhnd_alloc_resources(device_t dev, struct resource_spec *rs,
    struct bhnd_resource **res)

int
bhnd_deactivate_resource(device_t dev, int type, int rid,
    struct bhnd_resource *r)

int
bhnd_release_resource(device_t dev, int type, int rid,
    struct bhnd_resource *r)

void
bhnd_release_resources(device_t dev, const struct resource_spec *rs,
    struct bhnd_resource **res)
```

### 总线空间函数

```c
void
bhnd_bus_barrier(struct bhnd_resource *r, bus_size_t offset,
    bus_size_t length, int flags)

uint8_t
bhnd_bus_read_1(struct bhnd_resource *r, bus_size_t offset)

uint16_t
bhnd_bus_read_2(struct bhnd_resource *r, bus_size_t offset)

uint32_t
bhnd_bus_read_4(struct bhnd_resource *r, bus_size_t offset)

void
bhnd_bus_write_1(struct bhnd_resource *r, uint8_t value)

void
bhnd_bus_write_2(struct bhnd_resource *r, uint16_t value)

void
bhnd_bus_write_4(struct bhnd_resource *r, uint32_t value)
```

以及对应的 `read_multi`、`write_multi`、`read_multi_stream`、`write_multi_stream`、`read_region`、`write_region`、`read_region_stream`、`write_region_stream`、`read_stream`、`write_stream`、`set_multi`、`set_region` 系列函数（1/2/4 字节宽度变体）。

### 设备配置函数

```c
int
bhnd_read_ioctl(device_t dev, uint16_t *ioctl)

int
bhnd_write_ioctl(device_t dev, uint16_t value, uint16_t mask)

int
bhnd_read_iost(device_t dev, uint16_t *iost)

uint32_t
bhnd_read_config(device_t dev, bus_size_t offset, void *value, u_int width)

int
bhnd_write_config(device_t dev, bus_size_t offset, const void *value,
    u_int width)

int
bhnd_reset_hw(device_t dev, uint16_t ioctl, uint16_t reset_ioctl)

int
bhnd_suspend_hw(device_t dev, uint16_t ioctl)

bool
bhnd_is_hw_suspended(device_t dev)
```

### 设备信息函数

```c
bhnd_attach_type
bhnd_get_attach_type(device_t dev)

const struct bhnd_chipid *
bhnd_get_chipid(device_t dev)

bhnd_devclass_t
bhnd_get_class(device_t dev)

u_int
bhnd_get_core_index(device_t dev)

struct bhnd_core_info
bhnd_get_core_info(device_t dev)

int
bhnd_get_core_unit(device_t dev)

uint16_t
bhnd_get_device(device_t dev)

const char *
bhnd_get_device_name(device_t dev)

uint8_t
bhnd_get_hwrev(device_t dev)

uint16_t
bhnd_get_vendor(device_t dev)

const char *
bhnd_get_vendor_name(device_t dev)

int
bhnd_read_board_info(device_t dev, struct bhnd_board_info *info)
```

### 设备匹配函数

```c
bool
bhnd_board_matches(const struct bhnd_board_info *board,
    const struct bhnd_board_match *desc)

device_t
bhnd_bus_match_child(device_t bus, const struct bhnd_core_match *desc)

bool
bhnd_chip_matches(const struct bhnd_chipid *chip,
    const struct bhnd_chip_match *desc)

struct bhnd_core_match
bhnd_core_get_match_desc(const struct bhnd_core_info *core)

bool
bhnd_core_matches(const struct bhnd_core_info *core,
    const struct bhnd_core_match *desc)

bool
bhnd_cores_equal(const struct bhnd_core_info *lhs,
    const struct bhnd_core_info *rhs)

bool
bhnd_hwrev_matches(uint16_t hwrev, const struct bhnd_hwrev_match *desc)

const struct bhnd_core_info *
bhnd_match_core(const struct bhnd_core_info *cores, u_int num_cores,
    const struct bhnd_core_match *desc)
```

### 设备表函数

```c
const struct bhnd_device *
bhnd_device_lookup(device_t dev, const struct bhnd_device *table,
    size_t entry_size)

bool
bhnd_device_matches(device_t dev, const struct bhnd_device_match *desc)

uint32_t
bhnd_device_quirks(device_t dev, const struct bhnd_device *table,
    size_t entry_size)
```

```c
struct bhnd_device_quirk {
	struct bhnd_device_match	desc;
	uint32_t			quirks;
};
```

```c
struct bhnd_device {
    const struct bhnd_device_match	 core;
    const char			*desc;
    const struct bhnd_device_quirk	*quirks_table;
    uint32_t			 device_flags;
};
```

```c
enum {
	BHND_DF_ANY	= 0,
	BHND_DF_HOSTB	= (1 << 0),
	BHND_DF_SOC	= (1 << 1),
	BHND_DF_ADAPTER	= (1 << 2)
};
```

```c
#define BHND_DEVICE_END { { BHND_MATCH_ANY }, NULL, NULL, 0 }
```

```c
#define BHND_DEVICE_QUIRK_END { { BHND_MATCH_ANY }, 0 }
```

### DMA 地址转换函数

```c
int
bhnd_get_dma_translation(device_t dev, u_int width, uint32_t flags,
    bus_dma_tag_t *dmat, struct bhnd_dma_translation *translation)
```

```c
struct bhnd_dma_translation {
	bhnd_addr_t	base_addr;
	bhnd_addr_t	addr_mask;
	bhnd_addr_t	addrext_mask;
	uint32_t	flags;
};
```

```c
typedef enum {
	BHND_DMA_ADDR_30BIT	= 30,
	BHND_DMA_ADDR_32BIT	= 32,
	BHND_DMA_ADDR_64BIT	= 64
} bhnd_dma_addrwidth;
```

```c
enum bhnd_dma_translation_flags {
	BHND_DMA_TRANSLATION_PHYSMAP		= (1<<0),
	BHND_DMA_TRANSLATION_BYTESWAPPED	= (1<<1)
};
```

### 中断函数

```c
u_int
bhnd_get_intr_count(device_t dev)

int
bhnd_get_intr_ivec(device_t dev, u_int intr, u_int *ivec)

int
bhnd_map_intr(device_t dev, u_int intr, rman_res_t *irq)

void
bhnd_unmap_intr(device_t dev, rman_res_t irq)
```

### NVRAM 函数

```c
int
bhnd_nvram_getvar(device_t dev, const char *name, void *buf, size_t *len,
    bhnd_nvram_type type)

int
bhnd_nvram_getvar_array(device_t dev, const char *name, void *buf,
    size_t size, bhnd_nvram_type type)

int
bhnd_nvram_getvar_int(device_t dev, const char *name, void *value, int width)

int
bhnd_nvram_getvar_int8(device_t dev, const char *name, int8_t *value)

int
bhnd_nvram_getvar_int16(device_t dev, const char *name, int16_t *value)

int
bhnd_nvram_getvar_int32(device_t dev, const char *name, int32_t *value)

int
bhnd_nvram_getvar_uint(device_t dev, const char *name, void *value, int width)

int
bhnd_nvram_getvar_uint8(device_t dev, const char *name, uint8_t *value)

int
bhnd_nvram_getvar_uint16(device_t dev, const char *name, uint16_t *value)

int
bhnd_nvram_getvar_uint32(device_t dev, const char *name, uint32_t *value)

int
bhnd_nvram_getvar_str(device_t dev, const char *name, char *buf, size_t len,
    size_t *rlen)

const char *
bhnd_nvram_string_array_next(const char *inp, size_t ilen, const char *prev,
    size_t *olen)
```

```c
typedef enum {
	BHND_NVRAM_TYPE_UINT8		= 0,
	BHND_NVRAM_TYPE_UINT16		= 1,
	BHND_NVRAM_TYPE_UINT32		= 2,
	BHND_NVRAM_TYPE_UINT64		= 3,
	BHND_NVRAM_TYPE_INT8		= 4,
	BHND_NVRAM_TYPE_INT16		= 5,
	BHND_NVRAM_TYPE_INT32		= 6,
	BHND_NVRAM_TYPE_INT64		= 7,
	BHND_NVRAM_TYPE_CHAR		= 8,
	BHND_NVRAM_TYPE_STRING		= 9,
	BHND_NVRAM_TYPE_BOOL		= 10,
	BHND_NVRAM_TYPE_NULL		= 11,
	BHND_NVRAM_TYPE_DATA		= 12
	BHND_NVRAM_TYPE_UINT8_ARRAY	= 16,
	BHND_NVRAM_TYPE_UINT16_ARRAY	= 17,
	BHND_NVRAM_TYPE_UINT32_ARRAY	= 18,
	BHND_NVRAM_TYPE_UINT64_ARRAY	= 19,
	BHND_NVRAM_TYPE_INT8_ARRAY	= 20,
	BHND_NVRAM_TYPE_INT16_ARRAY	= 21,
	BHND_NVRAM_TYPE_INT32_ARRAY	= 22,
	BHND_NVRAM_TYPE_INT64_ARRAY	= 23,
	BHND_NVRAM_TYPE_CHAR_ARRAY	= 24,
	BHND_NVRAM_TYPE_STRING_ARRAY	= 25,
	BHND_NVRAM_TYPE_BOOL_ARRAY	= 26
} bhnd_nvram_type;
```

### 端口/区域函数

```c
int
bhnd_decode_port_rid(device_t dev, int type, int rid,
    bhnd_port_type *port_type, u_int *port, u_int *region)

u_int
bhnd_get_port_count(device_t dev, bhnd_port_type type)

int
bhnd_get_port_rid(device_t dev, bhnd_port_type type, u_int port,
    u_int region)

int
bhnd_get_region_addr(device_t dev, bhnd_port_type port_type, u_int port,
    u_int region, bhnd_addr_t *region_addr, bhnd_size_t *region_size)

u_int
bhnd_get_region_count(device_t dev, bhnd_port_type type, u_int port)

bool
bhnd_is_region_valid(device_t dev, bhnd_port_type type, u_int port,
    u_int region)
```

```c
typedef enum {
	BHND_PORT_DEVICE	= 0,
	BHND_PORT_BRIDGE	= 1,
	BHND_PORT_AGENT		= 2
} bhnd_port_type;
```

### 电源管理函数

```c
int
bhnd_alloc_pmu(device_t dev)

int
bhnd_release_pmu(device_t dev)

int
bhnd_enable_clocks(device_t dev, uint32_t clocks)

int
bhnd_request_clock(device_t dev, bhnd_clock clock)

int
bhnd_get_clock_freq(device_t dev, bhnd_clock clock, u_int *freq)

int
bhnd_get_clock_latency(device_t dev, bhnd_clock clock, u_int *latency)

int
bhnd_request_ext_rsrc(device_t dev, u_int rsrc)

int
bhnd_release_ext_rsrc(device_t dev, u_int rsrc)
```

```c
typedef enum {
	BHND_CLOCK_DYN	= (1 << 0),
	BHND_CLOCK_ILP	= (1 << 1),
	BHND_CLOCK_ALP	= (1 << 2),
	BHND_CLOCK_HT	= (1 << 3)
} bhnd_clock;
```

### 服务提供者函数

```c
int
bhnd_register_provider(device_t dev, bhnd_service_t service)

int
bhnd_deregister_provider(device_t dev, bhnd_service_t service)

device_t
bhnd_retain_provider(device_t dev, bhnd_service_t service)

void
bhnd_release_provider(device_t dev, device_t provider, bhnd_service_t service)
```

```c
typedef enum {
	BHND_SERVICE_CHIPC,
	BHND_SERVICE_PWRCTL,
	BHND_SERVICE_PMU,
	BHND_SERVICE_NVRAM,
	BHND_SERVICE_GPIO,
	BHND_SERVICE_ANY	= 1000
} bhnd_service_t;
```

### 工具函数

```c
bhnd_erom_class_t *
bhnd_driver_get_erom_class(driver_t *driver)

bhnd_devclass_t
bhnd_find_core_class(uint16_t vendor, uint16_t device)

const char *
bhnd_find_core_name(uint16_t vendor, uint16_t device)

bhnd_devclass_t
bhnd_core_class(const struct bhnd_core_info *ci)

const char *
bhnd_core_name(const struct bhnd_core_info *ci)

int
bhnd_format_chip_id(char *buffer, size_t size, uint16_t chip_id)

void
bhnd_set_custom_core_desc(device_t dev, const char *dev_name)

void
bhnd_set_default_core_desc(device_t dev)

const char *
bhnd_vendor_name(uint16_t vendor)
```

```c
#define	BHND_CHIPID_MAX_NAMELEN	32
```

## 描述

`bhnd` 为 Broadcom 家庭网络部门（BHND）设备中的片上互连和 IP 核提供了统一的总线和驱动程序编程接口。

BHND 设备系列由 MIPS/ARM SoC（片上系统）和基于通用 Broadcom IP 核库的主机连接芯片组组成，通过两种片上底板（硬件总线）架构之一连接。

2009 年之前设计的硬件使用 Broadcom 的 "SSB" 底板架构，基于 Sonics Silicon 的互连 IP。Sonics 底板上的每个核都提供一个 4 KiB 的寄存器块，包含设备特定的 CSR 和 SSB 特定的每核设备管理（启用/重置等）寄存器。

后续硬件基于 Broadcom 的 "BCMA" 底板，基于 ARM 的 AMBA IP。早期基于 SSB 的设备中使用的 IP 核经过适配以与新底板兼容，额外的"包装器"核提供每核设备管理功能，替代 SSB 的每核管理寄存器。

当 BHND 硬件用作主机连接外设（例如 PCI Wi-Fi 卡）时，片上外设控制器核配置为端点设备运行，桥接对 SoC 硬件的访问：

- 通过一组寄存器窗口（例如，通过 PCI BAR 映射到 SoC 地址空间的一组可配置窗口）提供主机对 SoC 地址空间的访问
- DMA 由桥接核将主机地址空间稀疏映射到底板地址空间来支持。这些地址区域可用作片上 DMA 引擎的目标。
- 路由到桥接核的任何底板中断向量都可由桥接映射到主机中断（例如 PCI INTx/MSI/MSI-X）。

`bhnd` 驱动程序编程接口和 [bhndb(4)](../man4/bhndb.4.md) 主机桥接驱动程序支持为 Broadcom IP 核实现通用驱动程序，无论它们是通过 BHND 主机桥接还是通过原生 SoC 底板连接。

### 总线资源函数

bhnd_resource 函数是标准 `struct resource` 总线 API 的包装器，为 `SYS_RES_MEMORY` 资源提供支持，这些资源在 [bhndb(4)](../man4/bhndb.4.md) 桥接芯片组上可能需要在访问总线内存之前按需重新映射地址窗口。

这些函数主要用于 BHND 平台设备驱动程序的实现，这些驱动程序在主机连接外设上必须在初始设置和拆卸期间共享少量寄存器窗口。

BHND 外设设计为在正常操作期间不需要寄存器窗口重新映射，大多数驱动程序可以直接安全地使用标准 `struct resource` API。

`bhnd_activate_resource` 函数激活先前分配的资源。

参数如下：

**`dev`** 持有已分配资源所有权的设备。

**`type`** 资源类型。

**`rid`** 标识要激活的资源的总线特定句柄。

**`r`** 指向 `bhnd_alloc_resource` 返回的资源的指针。

`bhnd_alloc_resource` 函数从设备的父 [bhnd(4)](../man4/bhnd.4.md) 总线分配资源。

参数如下：

**`dev`** 请求资源所有权的设备。

**`type`** 要分配的资源类型。可以是标准 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 函数支持的任何类型。

**`rid`** 标识要分配的资源的总线特定句柄。

**`start`** 资源的起始地址。

**`end`** 资源的结束地址。

**`count`** 资源的大小。

**`flags`** 要分配的资源的标志。可以是标准 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 函数支持的任何值。

要请求总线提供资源的默认 `start`、`end` 和 `count` 值，分别传递 0ul 和 ~0ul 作为 `start` 和 `end` 值，`count` 为 1。

`bhnd_alloc_resource_any` 函数是 `bhnd_alloc_resource` 的便利包装器，使用资源的默认 `start`、`end` 和 `count` 值。

`bhnd_alloc_resources` 函数从设备的父 [bhnd(4)](../man4/bhnd.4.md) 总线分配资源规范中定义的资源。

`bhnd_deactivate_resource` 函数停用先前由 `bhnd_activate_resource` 激活的资源。

`bhnd_release_resource` 函数释放先前由 `bhnd_alloc_resource` 返回的资源。

`bhnd_release_resources` 函数释放先前由 `bhnd_alloc_resources` 返回的资源。

`bhnd_resource` 结构包含以下字段：

**`res`** 指向总线 `struct resource` 的指针。

**`direct`** 如果为 true，资源在 MMIO 可访问之前需要总线窗口重新映射。

### 总线空间函数

bhnd_bus_space 函数包装其等效的 [bus_space(9)](bus_space.9.md) 对应函数，并提供通过 `struct bhnd_resource` 访问总线内存的支持。

`bhnd_bus_barrier`
`bhnd_bus_[read|write]_[1|2|4]`
`bhnd_bus_[read_multi|write_multi]_[1|2|4]`
`bhnd_bus_[read_multi_stream|write_multi_stream]_[1|2|4]`
`bhnd_bus_[read_region|write_region]_[1|2|4]`
`bhnd_bus_[read_region_stream|write_region_stream]_[1|2|4]`
`bhnd_bus_[read_stream|write_stream]_[1|2|4]`
`bhnd_bus_[set_multi|set_stream]_[1|2|4]`

不依赖 `struct bhnd_resource` 的驱动程序应直接使用标准 `struct resource` 和 [bus_space(9)](bus_space.9.md) API。

### 设备配置函数

`bhnd_read_ioctl` 函数用于读取设备 `dev` 的 I/O 控制寄存器值，在 `ioctl` 中返回当前值。

`bhnd_write_ioctl` 函数用于修改 `dev` 的 I/O 控制寄存器。寄存器的新值通过将 `mask` 中设置的任何位更新为 `value` 来计算。支持以下 I/O 控制标志：

**`BHND_IOCTL_BIST`** 启动内置自检（BIST）。必须在使用 IOST（I/O 状态）寄存器读取 BIST 结果后清除。

**`BHND_IOCTL_PME`** 启用核发布电源管理事件。

**`BHND_IOCTL_CLK_FORCE`** 强制禁用时钟门控，使所有时钟在核内分布。在断言/取消断言重置时应设置，以确保重置信号完全传播到整个核。

**`BHND_IOCTL_CLK_EN`** 如果清除，核时钟将被禁用。应在正常操作期间设置，在核保持重置状态时清除。

**`BHND_IOCTL_CFLAGS`** 为附加的核特定 I/O 控制标志保留的 IOCTL 位掩码。

`bhnd_read_iost` 函数用于读取设备 `dev` 的 I/O 状态寄存器，在 `iost` 中返回当前值。支持以下 I/O 状态标志：

**`BHND_IOST_BIST_DONE`** 在 BIST 完成时设置。使用 `bhnd_write_ioctl` 清除 I/O 控制寄存器的 `BHND_IOCTL_BIST` 标志时将清除此标志。

**`BHND_IOST_BIST_FAIL`** 在检测到 BIST 错误时设置；如果 BIST 尚未完成且 `BHND_IOST_BIST_DONE` 未设置，则值未指定。

**`BHND_IOST_CLK`** 如果核要求取消门控时钟则设置，否则清除。如果核不支持时钟门控，则值未定义。

**`BHND_IOST_DMA64`** 如果此核支持 64 位 DMA 则设置。

**`BHND_IOST_CFLAGS`** 为附加的核特定 I/O 状态标志保留的 IOST 位掩码。

`bhnd_read_config` 函数用于从设备 `dev` 的底板特定代理/配置空间的 `offset` 处读取 `width` 字节的数据项。

`bhnd_write_config` 函数用于向设备 `dev` 的底板特定代理/配置空间的 `offset` 处写入 `width` 字节的 `value` 数据项。请求的 `width` 必须是 1、2 或 4 字节之一。

通过 `bhnd_read_config` 和 `bhnd_write_config` 访问的代理/配置空间是底板特定的，这些函数应仅用于其他 `bhnd` 函数不可用的功能。

`bhnd_suspend_hw` 函数将设备 `dev` 转换到低功率 "RESET" 状态，将 `ioctl` 写入 `dev` 的 I/O 控制标志。可以使用 `bhnd_reset_hw` 将硬件从此状态恢复。

`bhnd_reset_hw` 函数首先将设备 `dev` 转换到低功率 RESET 状态，将 `ioctl_reset` 写入 `dev` 的 I/O 控制标志，然后将设备从 RESET 中恢复，将 `ioctl` 写入设备的 I/O 控制标志。

`bhnd_is_hw_suspended` 函数在设备 `dev` 当前保持在 RESET 状态或未时钟时返回 `true`。否则返回 `false`。

使用 `bhnd_enable_clocks`、`bhnd_request_clock` 或 `bhnd_request_ext_rsrc` 发出的任何未完成的每设备 PMU 请求将在设备进入 RESET 状态时自动释放。

### 设备信息函数

`bhnd_get_attach_type` 函数返回设备 `dev` 的父 [bhnd(4)](../man4/bhnd.4.md) 总线的附件类型。

支持以下附件类型：

**`BHND_ATTACH_ADAPTER`** 总线位于桥接适配器上，如 PCI Wi-Fi 设备。

**`BHND_ATTACH_NATIVE`** 总线位于原生主机上，如嵌入式 SoC 的主总线或辅助总线。

`bhnd_get_chipid` 函数从设备 `dev` 的父 [bhnd(4)](../man4/bhnd.4.md) 总线返回芯片信息。返回的 `bhnd_chipid` 结构包含以下字段：

**`chip_id`** 芯片标识符。

**`chip_rev`** 芯片的硬件修订版。

**`chip_pkg`** 芯片的半导体封装标识符。给定芯片可能存在多种不同的物理半导体封装变体，每种都可能需要驱动程序对硬件勘误、未填充组件等进行变通处理。

**`chip_type`** 此芯片使用的互连架构。

**`chip_caps`** 此芯片支持的 `bhnd` 能力标志。

**`enum_addr`** 底板枚举地址。在 SSB 设备上，这是第一个 SSB 核的基地址。在 BCMA 设备上，这是枚举 ROM（EROM）核的地址。

**`ncores`** 芯片底板上的核数，如果未知则为 0。

为已知 `chip_type` 值定义了以下常量：

**`BHND_CHIPTYPE_SIBA`** SSB 互连。

**`BHND_CHIPTYPE_BCMA`** BCMA 互连。

**`BHND_CHIPTYPE_BCMA_ALT`** 在 Broadcom Northstar ARM SoC 中发现的 BCMA 兼容变体。

**`BHND_CHIPTYPE_UBUS`** UBUS 互连。这种 BCMA 派生的互连见于 Broadcom BCM33xx DOCSIS SoC 和 BCM63xx xDSL SoC。 [bhnd(4)](../man4/bhnd.4.md) 目前不支持 UBUS。

支持以下 `chip_caps` 标志：

**`BHND_CAP_BP64`** 底板支持 64 位寻址。

**`BHND_CAP_PMU`** 存在 PMU。

为已知的 `chip_id`、`chip_pkg` 和 `chip_type` 值定义的附加符号常量见：

```c
#include <dev/bhnd/bhnd_ids.h>
```

`bhnd_get_class` 函数返回设备 `dev` 的 BHND 类（如果设备的*vendor* 和 *device* 标识符已知）。否则返回 `BHND_DEVCLASS_OTHER`。

将返回以下设备类之一：

**`BHND_DEVCLASS_CC`** ChipCommon I/O 控制器

**`BHND_DEVCLASS_CC_B`** ChipCommon 辅助控制器

**`BHND_DEVCLASS_PMU`** PMU 控制器

**`BHND_DEVCLASS_PCI`** PCI 主机/设备桥接

**`BHND_DEVCLASS_PCIE`** PCIe 主机/设备桥接

**`BHND_DEVCLASS_PCCARD`** PCMCIA 主机/设备桥接

**`BHND_DEVCLASS_RAM`** 内部 RAM/SRAM

**`BHND_DEVCLASS_MEMC`** 内存控制器

**`BHND_DEVCLASS_ENET`** IEEE 802.3 MAC/PHY

**`BHND_DEVCLASS_ENET_MAC`** IEEE 802.3 MAC

**`BHND_DEVCLASS_ENET_PHY`** IEEE 802.3 PHY

**`BHND_DEVCLASS_WLAN`** IEEE 802.11 MAC/PHY/Radio

**`BHND_DEVCLASS_WLAN_MAC`** IEEE 802.11 MAC

**`BHND_DEVCLASS_WLAN_PHY`** IEEE 802.11 PHY

**`BHND_DEVCLASS_CPU`** CPU 核

**`BHND_DEVCLASS_SOC_ROUTER`** 互连路由器

**`BHND_DEVCLASS_SOC_BRIDGE`** 互连主机桥接

**`BHND_DEVCLASS_EROM`** 设备枚举 ROM

**`BHND_DEVCLASS_NVRAM`** NVRAM/Flash 控制器

**`BHND_DEVCLASS_SOFTMODEM`** 模拟/PSTN 软调制解调器编解码器

**`BHND_DEVCLASS_USB_HOST`** USB 主机控制器

**`BHND_DEVCLASS_USB_DEV`** USB 设备控制器

**`BHND_DEVCLASS_USB_DUAL`** USB 主机/设备控制器

**`BHND_DEVCLASS_OTHER`** 其他/未知

**`BHND_DEVCLASS_INVALID`** 无效类

`bhnd_get_core_info` 函数返回设备 `dev` 的核信息。返回的 `bhnd_core_info` 结构包含以下字段：

**`vendor`** 供应商标识符（JEP-106，ARM 4 位续位编码）

**`device`** 设备标识符

**`hwrev`** 硬件修订版

**`core_idx`** 核索引

**`unit`** 核单元

`bhnd_get_core_index`、`bhnd_get_core_unit`、`bhnd_get_device`、`bhnd_get_hwrev` 和 `bhnd_get_vendor` 函数是 `bhnd_get_core_info` 的便利包装器，分别返回 `bhnd_core_info` 结构中的 `core_idx`、`core_unit`、`device`、`hwrev` 或 `vendor` 字段。

`bhnd_get_device_name` 函数返回设备 `dev` 的人类可读名称。

`bhnd_get_vendor_name` 函数返回设备 `dev` 供应商的人类可读名称。

`bhnd_read_board_info` 函数尝试读取设备 `dev` 的板信息。成功时，板信息将返回到 `info` 指向的位置。

`bhnd_board_info` 结构包含以下字段：

**`board_vendor`** 板制造商的供应商 ID（PCI-SIG 分配）。

**`board_type`** 板 ID。

**`board_devid`** 设备 ID。

**`board_rev`** 板修订版。

**`board_srom_rev`** 板 SROM 格式修订版。

**`board_flags`** 板标志（1）

**`board_flags2`** 板标志（2）

**`board_flags3`** 板标志（3）

`board_devid` 字段是最接近 BHND 设备能力（如果有）的 Broadcom PCI 设备 ID。

在 PCI 设备上，`board_vendor`、`board_type` 和 `board_devid` 字段默认为 PCI 子系统供应商 ID、PCI 子系统 ID 和 PCI 设备 ID，除非在设备 NVRAM 中覆盖。

在其他设备（包括 SoC）上，`board_vendor`、`board_type` 和 `board_devid` 字段将从设备 NVRAM 填充。

为常见板标志定义的符号常量见：

```c
#include <dev/bhnd/bhnd_ids.h>
```

### 设备匹配函数

bhnd 设备匹配函数用于匹配核、芯片和板级设备属性。匹配要求使用 `struct bhnd_board_match`、`struct bhnd_chip_match`、`struct bhnd_core_match`、`struct bhnd_device_match` 和 `struct bhnd_hwrev_match` 匹配描述符结构指定。

`bhnd_board_matches` 函数在 `board` 匹配板匹配描述符 `desc` 时返回 `true`。否则返回 `false`。

`bhnd_chip_matches` 函数在 `chip` 匹配芯片匹配描述符 `desc` 时返回 `true`。否则返回 `false`。

`bhnd_core_matches` 函数在 `core` 匹配核匹配描述符 `desc` 时返回 `true`。否则返回 `false`。

`bhnd_device_matches` 函数在设备 `dev` 匹配设备匹配描述符 `desc` 时返回 `true`。否则返回 `false`。

`bhnd_hwrev_matches` 函数在 `hwrev` 匹配硬件修订版匹配描述符 `desc` 时返回 `true`。否则返回 `false`。

`bhnd_bus_match_child` 函数返回 `bus` 的第一个匹配设备匹配描述符 `desc` 的子设备。如果未找到匹配的子设备，返回 `NULL`。

`bhnd_core_get_match_desc` 函数返回 `core` 中核信息的相等匹配描述符。返回的描述符仅匹配与 `core` 定义的核属性相同的核属性。

`bhnd_cores_equal` 函数是 `bhnd_core_matches` 和 `bhnd_core_get_match_desc` 的便利包装器。此函数在 `bhnd_core_info` 结构 `lhs` 和 `rhs` 相等时返回 `true`。否则返回 `false`。

`bhnd_match_core` 函数返回长度为 `num_cores` 的数组 `cores` 中第一个匹配 `desc` 的条目指针。如果未找到匹配的核，返回 `NULL`。

`bhnd_board_match` 匹配描述符可使用以下一个或多个宏初始化：

`BHND_MATCH_BOARD_VENDOR`(vendor) 匹配供应商等于 `vendor` 的板。

`BHND_MATCH_BOARD_TYPE`(type) 匹配类型等于 `BHND_BOARD_ ##` `type` 的板。

`BHND_MATCH_SROMREV`(sromrev) 匹配 sromrev 匹配 `BHND_HWREV_ ##` `sromrev` 的板。

`BHND_MATCH_BOARD_REV`(hwrev) 匹配硬件修订版匹配 `BHND_ ##` `hwrev` 的板。

`BHND_MATCH_BOARD`(vendor, type) `BHND_MATCH_BOARD_VENDOR` 和 `BHND_MATCH_BOARD_TYPE` 的便利包装器。

例如：

```c
struct bhnd_board_match board_desc = {
	BHND_MATCH_BOARD_VENDOR(BHND_MFGID_BROADCOM),
	BHND_MATCH_BOARD_TYPE(BCM94360X52C),
	BHND_MATCH_BOARD_REV(HWREV_ANY),
	BHND_MATCH_SROMREV(RANGE(0, 10))
};
```

`bhnd_chip_match` 匹配描述符可使用以下一个或多个宏初始化：

`BHND_MATCH_CHIP_ID`(id) 匹配 ID 等于 `BHND_CHIPID_ ##` `id` 的芯片。

`BHND_MATCH_CHIP_REV`(hwrev) 匹配硬件修订版匹配 `BHND_ ##` `hwrev` 的芯片。

`BHND_MATCH_CHIP_PKG`(pkg) 匹配封装 ID 等于 `BHND_PKGID_ ##` `pkg` 的芯片。

`BHND_MATCH_CHIP_TYPE`(type) 匹配芯片类型等于 `BHND_CHIPTYPE_ ##` `type` 的芯片。

`BHND_MATCH_CHIP_IP`(id, pkg) `BHND_MATCH_CHIP_ID` 和 `BHND_MATCH_CHIP_PKG` 的便利包装器。

`BHND_MATCH_CHIP_IPR`(id, pkg, hwrev) `BHND_MATCH_CHIP_ID`、`BHND_MATCH_CHIP_PKG` 和 `BHND_MATCH_CHIP_REV` 的便利包装器。

`BHND_MATCH_CHIP_IR`(id, hwrev) `BHND_MATCH_CHIP_ID` 和 `BHND_MATCH_CHIP_REV` 的便利包装器。

例如：

```c
struct bhnd_chip_match chip_desc = {
	BHND_MATCH_CHIP_IP(BCM4329, BCM4329_289PIN),
	BHND_MATCH_CHIP_TYPE(SIBA)
};
```

`bhnd_core_match` 匹配描述符可使用以下一个或多个宏初始化：

`BHND_MATCH_CORE_VENDOR`(vendor) 匹配供应商 ID 等于 `vendor` 的核。

`BHND_MATCH_CORE_ID`(id) 匹配设备 ID 等于 `id` 的核。

`BHND_MATCH_CORE_REV`(hwrev) 匹配硬件修订版匹配 `BHND_ ##` `hwrev` 的核。

`BHND_MATCH_CORE_CLASS`(class) 匹配核设备类等于 `class` 的核。

`BHND_MATCH_CORE_IDX`(idx) 匹配核索引等于 `idx` 的核。

`BHND_MATCH_CORE_UNIT`(unit) 匹配核单元等于 `unit` 的核。

`BHND_MATCH_CORE`(vendor, id) `BHND_MATCH_CORE_VENDOR` 和 `BHND_MATCH_CORE_ID` 的便利包装器。

例如：

```c
struct bhnd_core_match core_desc = {
	BHND_MATCH_CORE(BHND_MFGID_BROADCOM, BHND_COREID_CC),
	BHND_MATCH_CORE_REV(HWREV_RANGE(0, 10))
};
```

`bhnd_device_match` 匹配描述符支持匹配所有板、芯片和核属性，可使用任何 `bhnd_board_match`、`bhnd_chip_match` 或 `bhnd_core_match` 宏初始化。

例如：

```c
struct bhnd_device_match device_desc = {
	BHND_MATCH_CHIP_IP(BCM4329, BCM4329_289PIN),
	BHND_MATCH_BOARD_VENDOR(BHND_MFGID_BROADCOM),
	BHND_MATCH_BOARD_TYPE(BCM94329AGB),
	BHND_MATCH_CORE(BHND_MFGID_BROADCOM, BHND_COREID_CC),
};
```

`bhnd_hwrev_match` 匹配描述符可使用以下宏之一初始化：

**`BHND_HWREV_ANY`** 匹配任何硬件修订版。

`BHND_HWREV_EQ`(hwrev) 匹配任何等于 `hwrev` 的硬件修订版。

`BHND_HWREV_GTE`(hwrev) 匹配任何大于或等于 `hwrev` 的硬件修订版。

`BHND_HWREV_LTE`(hwrev) 匹配任何小于或等于 `hwrev` 的硬件修订版。

`BHND_HWREV_RANGE`(start, end) 匹配包含范围内的任何硬件修订版。如果指定 `BHND_HWREV_INVALID` 作为 `end` 值，将匹配任何等于或大于 `start` 的修订版。

### 设备表函数

bhnd 设备表函数用于查询设备和 quirks 表。

`bhnd_device_lookup` 函数返回设备表 `table` 中第一个匹配设备 `dev` 的条目指针。表条目大小由 `entry_size` 指定。

`bhnd_device_quirks` 函数扫描设备表 `table` 中所有匹配设备 `dev` 的 quirk 条目，返回所有匹配 quirk 标志的按位 OR。表条目大小由 `entry_size` 指定。

`bhnd_device` 结构包含以下字段：

**`core`** 一个 `bhnd_device_match` 描述符。

**`desc`** 适合与 [device_set_desc(9)](device_set_desc.9.md) 一起使用的详细设备描述，或 `NULL`。

**`quirks_table`** 此设备的 quirks 表，或 `NULL`。

**`device_flags`** 匹配此条目时所需的设备标志。

支持以下设备标志：

**`BHND_DF_ANY`** 匹配任何设备。

**`BHND_DF_HOSTB`** 仅当设备是 [bhndb(4)](../man4/bhndb.4.md) 主机桥接时匹配。隐含 `BHND_DF_ADAPTER`。

**`BHND_DF_SOC`** 仅当设备连接到原生 SoC 底板时匹配。

**`BHND_DF_ADAPTER`** 仅当设备连接到 [bhndb(4)](../man4/bhndb.4.md) 桥接底板时匹配。

`bhnd_device` 表条目可使用以下宏之一初始化：

`BHND_DEVICE`(vendor, device, desc, quirks, flags) 匹配供应商 ID 等于 `BHND_MFGID_ ##` `vendor` 且核设备 ID 等于 `BHND_COREID_ ##` `device` 的设备。设备的详细描述由 `desc` 参数指定，指向设备特定 quirks 表的指针由 `quirks` 参数指定，任何所需的设备标志可在 `flags` 中提供。可选的 `flags` 参数在省略时默认为 `BHND_DF_ANY`。

**`BHND_DEVICE_END`** 终止 `bhnd_device` 表。

例如：

```c
struct bhnd_device bhnd_usb11_devices[] = {
	BHND_DEVICE(BCM, USB, "Broadcom USB1.1 Controller",
	    bhnd_usb11_quirks),
	BHND_DEVICE_END
};
```

`bhnd_device_quirk` 结构包含以下字段：

**`desc`** 一个 `bhnd_device_match` 描述符。

**`quirks`** 适用的 quirk 标志。

bhnd_device_quirk 表条目可使用以下便利宏之一初始化：

`BHND_BOARD_QUIRK`(board, flags) 在板类型等于 `BHND_BOARD_ ##` `board` 的设备上设置 quirk 标志 `flags`。

`BHND_CHIP_QUIRK`(chip, hwrev, flags) 在芯片 ID 等于 `BHND_CHIPID_BCM ##` `chip` 且芯片硬件修订版匹配 `BHND_ ##` `hwrev` 的设备上设置 quirk 标志 `flags`。

`BHND_PKG_QUIRK`(chip, pkg, flags) 在芯片 ID 等于 `BHND_CHIPID_BCM ##` `chip` 且芯片封装等于 `BHND_ ## chip ##` `pkg` 的设备上设置 quirk 标志 `flags`。

`BHND_CORE_QUIRK`(hwrev, flags) 在核硬件修订版匹配 `BHND_ ##` `hwrev` 的设备上设置 quirk 标志 `flags`。

### DMA 地址转换函数

`bhnd_get_dma_translation` 函数用于请求适合最大 DMA 地址宽度 `width` 使用的 DMA 地址转换描述符，并支持请求的转换 `flags`。

如果找到合适的 DMA 地址转换描述符，它将存储在 `translation` 中，指定 DMA 转换地址限制的总线 DMA 标签将存储在 `dmat` 中。如果不需要转换描述符或 DMA 标签，`translation` 和 `dmat` 参数可为 `NULL`。

支持以下 DMA 转换标志：

**`BHND_DMA_TRANSLATION_PHYSMAP`** 转换重新映射设备的物理地址空间。这与 `BHND_DMA_TRANSLATION_BYTESWAPPED` 一起使用，定义在大端 MIPS SoC 上提供对物理内存的字节交换访问的 DMA 转换。

**`BHND_DMA_TRANSLATION_BYTESWAPPED`** 转换提供字节交换映射；写入请求在写入内存之前进行字节交换，读取请求在返回之前进行字节交换。这主要用于在大端模式执行的嵌入式 MIPS SoC 上执行 DMA 数据的高效字节交换。

为常见 DMA 地址宽度定义了以下符号常量：

**`BHND_DMA_ADDR_30BIT`** 30 位 DMA

**`BHND_DMA_ADDR_32BIT`** 32 位 DMA

**`BHND_DMA_ADDR_64BIT`** 64 位 DMA

`bhnd_dma_translation` 结构包含以下字段：

**`base_addr`** 主机到设备的物理地址转换。这可以加到主机物理地址上以产生设备 DMA 地址。

**`addr_mask`** 设备可寻址的地址掩码。这定义了设备 DMA 地址范围，不包括为在 `base_addr` 的转换窗口内映射地址而保留的任何位。

**`addrext_mask`** 设备可寻址的扩展地址掩码。如果每核 BHND DMA 引擎支持 'addrext' 控制字段，它可用于提供 `addr_mask` 排除的地址位。对 DMA 扩展地址更改的支持（包括与提供设备到主机 DMA 地址转换的核协调）由 DMA 引擎透明处理。例如，在 PCI Wi-Fi 设备上，Wi-Fi 核的 DMA 引擎将（实际上）更新 PCI 主机桥接核的 DMA `sbtopcitranslation` 基地址，以在执行 DMA 事务之前映射目标地址。

**`flags`** 转换标志。

### 中断函数

`bhnd_get_intr_count` 函数用于确定分配给设备 `dev` 的底板中断线数量。中断线标识符以单调递增顺序分配，从 0 开始。

`bhnd_get_intr_ivec` 函数用于确定分配给设备 `dev` 上中断线 `intr` 的底板中断向量，将结果写入 `ivec`。中断向量分配是底板特定的：在 BCMA 设备上，此函数返回分配给中断的 OOB 总线线。在 SIBA 设备上，它返回分配给中断的目标 OCP 从属标志号。

`bhnd_map_intr` 函数用于将分配给设备 `dev` 的中断线 `intr` 映射到 IRQ 号，将结果写入 `irq`。在取消映射之前，此 IRQ 可用于分配 SYS_RES_IRQ 类型的资源。

中断映射的所有权由调用者承担，必须使用 `bhnd_unmap_intr` 显式释放。

`bhnd_unmap_intr` 函数用于取消映射设备 `dev` 先前使用 `bhnd_map_intr` 映射的总线 IRQ `irq`。

### NVRAM 函数

`bhnd_nvram_getvar` 函数用于从设备 `dev` 的父 [bhnd(4)](../man4/bhnd.4.md) 总线注册的 NVRAM 提供者读取 NVRAM 变量 `name` 的值，强制转换为所需的数据表示 `type`，写入 `buf` 指定的缓冲区。

调用之前，`buf` 的最大容量由 `len` 指定。成功调用之后——或返回 `ENOMEM` 时——可用数据的大小将写入 `len`。所需数据表示的大小可以通过为 `buf` 传递 `NULL` 参数调用 `bhnd_nvram_getvar` 来确定。

支持以下 NVRAM 数据类型：

**`BHND_NVRAM_TYPE_UINT8`** 无符号 8 位整数

**`BHND_NVRAM_TYPE_UINT16`** 无符号 16 位整数

**`BHND_NVRAM_TYPE_UINT32`** 无符号 32 位整数

**`BHND_NVRAM_TYPE_UINT64`** 有符号 64 位整数

**`BHND_NVRAM_TYPE_INT8`** 有符号 8 位整数

**`BHND_NVRAM_TYPE_INT16`** 有符号 16 位整数

**`BHND_NVRAM_TYPE_INT32`** 有符号 32 位整数

**`BHND_NVRAM_TYPE_INT64`** 有符号 64 位整数

**`BHND_NVRAM_TYPE_CHAR`** UTF-8 字符

**`BHND_NVRAM_TYPE_STRING`** UTF-8 NUL 终止字符串

**`BHND_NVRAM_TYPE_BOOL`** uint8 布尔值

**`BHND_NVRAM_TYPE_NULL`** NULL（空）值

**`BHND_NVRAM_TYPE_DATA`** 不透明字节字符串

以及对应的数组类型（`_ARRAY` 后缀）。

`bhnd_nvram_getvar_array`、`bhnd_nvram_getvar_int`、`bhnd_nvram_getvar_int8`、`bhnd_nvram_getvar_int16`、`bhnd_nvram_getvar_int32`、`bhnd_nvram_getvar_uint`、`bhnd_nvram_getvar_uint8`、`bhnd_nvram_getvar_uint16`、`bhnd_nvram_getvar_uint32` 和 `bhnd_nvram_getvar_str` 函数是 `bhnd_nvram_getvar` 的便利包装器。

`bhnd_nvram_getvar_array` 函数在 `buf` 中返回恰好 `size` 的值，或如果数据表示长度不恰好为 `size` 则返回 `ENXIO` 错误代码。

`bhnd_nvram_getvar_int` 和 `bhnd_nvram_getvar_uint` 函数返回 NVRAM 变量 `name` 的值，强制转换为 `width`（1、2 或 4 字节）的有符号或无符号整数类型。

`bhnd_nvram_getvar_int8`、`bhnd_nvram_getvar_int16`、`bhnd_nvram_getvar_int32`、`bhnd_nvram_getvar_uint`、`bhnd_nvram_getvar_uint8`、`bhnd_nvram_getvar_uint16` 和 `bhnd_nvram_getvar_uint32` 函数返回 NVRAM 变量 `name` 的值，强制转换为有符号或无符号 8、16 或 32 位整数类型。

`bhnd_nvram_getvar_str` 函数返回 NVRAM 变量 `name` 的值，强制转换为 NUL 终止字符串。

`bhnd_nvram_string_array_next` 函数迭代 `inp` `BHND_NVRAM_TYPE_STRING_ARRAY` 值中的所有字符串。`inp` 的大小（包括任何终止 NUL 字符）使用 `ilen` 参数指定。`prev` 参数应是先前由 `bhnd_nvram_string_array_next` 返回的字符串指针，或 `NULL` 以开始迭代。如果 `prev` 不为 `NULL`，`olen` 参数必须是指向 `bhnd_nvram_string_array_next` 先前返回的长度的指针。成功时，下一个字符串元素的长度将写入此指针。

### 端口/区域函数

每设备互连内存映射由*端口类型*、*端口号*和*区域号*的组合标识。端口和内存区域标识符按每种*端口类型*以单调递增顺序分配，从 0 开始。

支持以下端口类型：

**`BHND_PORT_DEVICE`** 设备内存。设备的控制/状态寄存器始终由第一个设备端口和区域映射，并将分配 `SYS_RES_MEMORY` 资源 ID 0。

**`BHND_PORT_BRIDGE`** 桥接内存。

**`BHND_PORT_AGENT`** 互连代理/包装器。

`bhnd_decode_port_rid` 函数用于解码分配给设备 `dev` 的资源 ID `rid`（资源类型为 `type`），将端口类型写入 `port_type`，端口号写入 `port`，区域号写入 `region`。

`bhnd_get_port_count` 函数返回分配给设备 `dev` 的类型为 `type` 的端口数。

`bhnd_get_port_rid` 函数返回映射设备 `dev` 上 `type` 类型 `port` 的 `region` 的 `SYS_RES_MEMORY` 资源的资源 ID，如果端口或区域无效或没有分配的资源 ID 则返回 -1。

`bhnd_get_region_addr` 函数用于确定分配给 `dev` 的 `type` 类型 `port` 上内存 `region` 的基地址和大小。区域的基地址将写入 `region_addr`，区域大小写入 `region_size`。

`bhnd_get_region_count` 函数返回设备 `dev` 上映射到 `type` 类型 `port` 的内存区域数。

`bhnd_is_region_valid` 函数在 `region` 是设备 `dev` 上 `type` 类型 `port` 映射的有效区域时返回 `true`。

### 电源管理函数

驱动程序必须在调用任何其他 bhnd PMU 函数之前，使用 `bhnd_alloc_pmu` 请求父 [bhnd(4)](../man4/bhnd.4.md) 总线分配设备 PMU 状态。

`bhnd_alloc_pmu` 函数用于分配每设备 PMU 状态并为设备 `dev` 启用 PMU 请求处理。包含设备 PMU 寄存器块的内存区域必须在调用 `bhnd_alloc_pmu` 之前使用 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 或 `bhnd_alloc_resource` 分配，并且在调用 `bhnd_release_pmu` 之前不得释放。

在所有支持的 BHND 硬件上，PMU 寄存器块由设备第一个设备端口和区域中的设备控制/状态寄存器映射。

`bhnd_release_pmu` 函数释放先前使用 `bhnd_alloc_pmu` 为设备 `dev` 分配的每设备 PMU 状态。释放设备 PMU 状态时，任何未完成的时钟和外部资源请求将被丢弃。

`bhnd_enable_clocks` 函数用于请求代表设备 `dev` 上电并将 `clocks` 路由到底板。这将为任何所需的时钟源（如 XTAL、PLL 等）上电，并等待直到请求的时钟稳定。如果请求成功，`dev` 发出的任何先前时钟请求将被丢弃。

支持以下时钟，可使用按位 OR 组合以请求多个时钟：

**`BHND_CLOCK_DYN`** 根据连接到父 [bhnd(4)](../man4/bhnd.4.md) 总线的任何设备的所有未完成时钟请求动态选择适当的时钟源。

**`BHND_CLOCK_ILP`** 空闲低功率（ILP）时钟。如果不需要寄存器访问，或可接受长请求延迟时使用。

**`BHND_CLOCK_ALP`** 活动低功率（ALP）时钟。支持低延迟寄存器访问和低速率 DMA。

**`BHND_CLOCK_HT`** 高吞吐量（HT）时钟。支持高总线吞吐量和最低延迟寄存器访问。

`bhnd_request_clock` 函数用于请求将 `clock`（或更快的时钟）上电并路由到设备 `dev`。

`bhnd_get_clock_freq` 函数用于请求 `clock` 的当前时钟频率，将频率（以 Hz 为单位）写入 `freq`。

`bhnd_get_clock_latency` 函数用于确定 `clock` 所需的转换延迟，将延迟（以微秒为单位）写入 `latency`。`BHND_CLOCK_HT` 延迟值适合用作 D11 Wi-Fi 核的 *fastpwrup_dly* 值。

`bhnd_request_ext_rsrc` 函数用于请求上电分配给设备 `dev` 的、由设备特定标识符 `rsrc` 标识的外部 PMU 管理资源。

`bhnd_release_ext_rsrc` 函数释放设备 `dev` 对由设备特定标识符 `rsrc` 标识的 PMU 管理资源的任何未完成请求。如果外部资源由多个设备共享，则在所有设备请求释放之前不会断电。

### 服务提供者函数

`bhnd_register_provider` 函数用于将设备 `dev` 注册为父 [bhnd(4)](../man4/bhnd.4.md) 总线的平台 `service` 提供者。

支持以下服务类型：

**`BHND_SERVICE_CHIPC`** ChipCommon 服务。提供设备必须实现 bhnd_chipc 接口。

**`BHND_SERVICE_PWRCTL`** 传统 PWRCTL 服务。提供设备必须实现 bhnd_pwrctl 接口。

**`BHND_SERVICE_PMU`** PMU 服务。提供设备必须实现 bhnd_pmu 接口。

**`BHND_SERVICE_NVRAM`** NVRAM 服务。提供设备必须实现 bhnd_nvram 接口。

**`BHND_SERVICE_GPIO`** GPIO 服务。提供设备必须实现标准 [gpio(4)](../man4/gpio.4.md) 接口。

**`BHND_SERVICE_ANY`** 匹配任何服务类型。可与 `bhnd_deregister_provider` 一起使用以删除设备的所有服务提供者注册。

`bhnd_deregister_provider` 函数尝试删除设备 `dev` 和 `service` 的提供者注册。如果指定 `BHND_SERVICE_ANY` 作为 `service` 参数，此函数将尝试删除 `dev` 的所有服务提供者注册。

`bhnd_retain_provider` 函数保留并返回注册到设备 `dev` 的父 [bhnd(4)](../man4/bhnd.4.md) 总线的 `service` 提供者引用（如果可用）。成功时，调用者负责使用 `bhnd_release_provider` 释放此提供者引用。保证服务提供者在提供者引用释放之前保持可用。

`bhnd_release_provider` 函数释放设备 `dev` 先前使用 `bhnd_retain_provider` 保留的 `service` 的 `provider` 引用。

### 工具函数

`bhnd_driver_get_erom_class` 函数返回 [bhnd(4)](../man4/bhnd.4.md) 总线驱动程序实例 `driver` 使用的设备枚举表格式的 [bhnd_erom(9)](bhnd_erom.9.md) 类。如果驱动程序不支持 [bhnd_erom(9)](bhnd_erom.9.md) 设备枚举，返回 `NULL`。

`bhnd_find_core_class` 函数查找 BHND 供应商 ID `vendor` 和设备 ID `device` 的 BHND 类（如果已知）。

`bhnd_find_core_name` 函数用于获取 BHND 核的供应商 ID 为 `vendor`、设备 ID 为 `device` 的人类可读名称（如果已知）。

`bhnd_core_class` 和 `bhnd_core_name` 函数是 `bhnd_find_core_class` 和 `bhnd_find_core_name` 的便利包装器，使用核信息结构 `ci` 的 `vendor` 和 `device` 字段。

`bhnd_format_chip_id` 函数将 BHND `chip_id` 值的 NUL 终止人类可读表示写入指定的 `buffer`（容量为 `size`）。写入不超过 `size-1` 个字符，第 `size` 个字符设置为 '\0'。`BHND_CHIPID_MAX_NAMELEN` 的缓冲区大小足以容纳使用 `bhnd_format_chip_id` 生成的任何字符串表示。

`bhnd_set_custom_core_desc` 函数使用 `dev` 的 [bhnd(4)](../man4/bhnd.4.md) 设备标识，用指定的 `dev_name` 覆盖核名称，通过 [device_set_desc(9)](device_set_desc.9.md) 填充设备的详细描述。

`bhnd_set_default_core_desc` 函数使用 `dev` 的 [bhnd(4)](../man4/bhnd.4.md) 设备标识通过 [device_set_desc(9)](device_set_desc.9.md) 填充设备的详细描述。

`bhnd_vendor_name` 函数返回 JEP-106、ARM 4 位续位编码制造商 ID `vendor` 的人类可读名称（如果已知）。

## 返回值

### 总线资源函数

`bhnd_activate_resource`、`bhnd_alloc_resources`、`bhnd_deactivate_resource` 和 `bhnd_release_resource` 函数成功时返回 0，否则返回适当的错误代码。

`bhnd_alloc_resource` 和 `bhnd_alloc_resource_any` 函数成功时返回指向 `struct resource` 的指针，否则返回空指针。

### 设备配置函数

`bhnd_read_config` 和 `bhnd_write_config` 函数成功时返回 0，错误时返回以下值之一：

**`EINVAL`** 设备不是 [bhnd(4)](../man4/bhnd.4.md) 总线的直接子设备

**`EINVAL`** 请求的宽度不是 1、2 或 4 字节。

**`ENODEV`** 不支持访问设备的代理/配置空间。

**`EFAULT`** 请求的偏移量或宽度超出映射代理/配置空间的边界。

`bhnd_read_ioctl`、`bhnd_write_ioctl`、`bhnd_read_iost`、`bhnd_reset_hw` 和 `bhnd_suspend_hw` 函数成功时返回 0，否则返回适当的错误代码。

### 设备信息函数

`bhnd_read_board_info` 函数成功时返回 0，否则返回适当的错误代码。

### DMA 地址转换函数

`bhnd_get_dma_translation` 函数成功时返回 0，错误时返回以下值之一：

**`ENODEV`** 不支持 DMA。

**`ENOENT`** 没有匹配请求地址宽度和转换标志的 DMA 转换可用。

如果获取请求的 DMA 地址转换以其他方式失败，将返回适当的错误代码。

### 中断函数

`bhnd_get_intr_ivec` 函数成功时返回 0，如果请求的中断线超过分配给设备的中断线数量则返回 `ENXIO`。

`bhnd_map_intr` 函数成功时返回 0，否则返回适当的错误代码。

### NVRAM 函数

`bhnd_nvram_getvar` 系列函数成功时返回 0，错误时返回以下值之一：

**`ENODEV`** 如果总线未注册 NVRAM 提供者。

**`ENOENT`** 未找到请求的变量。

**`ENOMEM`** 如果大小缓冲区太小而无法容纳请求的值。

**`EOPNOTSUPP`** 如果值的本机类型不兼容且无法强制转换为请求的类型。

**`ERANGE`** 如果值强制转换将溢出（或下溢）请求的类型

如果读取变量以其他方式失败，将返回适当的错误代码。

### 端口/区域函数

`bhnd_decode_port_rid` 函数成功时返回 0，如果未找到匹配的端口/区域则返回适当的错误代码。

`bhnd_get_port_rid` 函数返回请求端口和区域的资源 ID，如果端口或区域无效或没有分配的资源 ID 则返回 -1。

`bhnd_get_region_addr` 函数成功时返回 0，如果未找到匹配的端口/区域则返回适当的错误代码。

### PMU 函数

`bhnd_alloc_pmu` 函数成功时返回 0，否则返回适当的错误代码。

`bhnd_release_pmu` 函数成功时返回 0，否则返回适当的错误代码，核状态将保持不变。

`bhnd_enable_clocks` 和 `bhnd_request_clock` 函数成功时返回 0，错误时返回以下值之一：

**`ENODEV`** 请求了不支持的时钟。

**`ENXIO`** 总线未注册 PMU 或 PWRCTL 提供者。

`bhnd_get_clock_freq` 函数成功时返回 0，如果指定时钟的频率不可用则返回 `ENODEV`。

`bhnd_get_clock_latency` 函数成功时返回 0，如果指定时钟的转换延迟不可用则返回 `ENODEV`。

`bhnd_request_ext_rsrc` 和 `bhnd_release_ext_rsrc` 函数成功时返回 0，否则返回适当的错误代码。

### 服务提供者函数

`bhnd_register_provider` 函数成功时返回 0，如果 service 的条目已存在则返回 `EEXIST`，如果服务注册以其他方式失败则返回适当的错误代码。

`bhnd_deregister_provider` 函数成功时返回 0，如果存在对服务提供者的活动引用则返回 `EBUSY`。

`bhnd_retain_provider` 函数成功时返回指向 `device_t` 的指针，如果请求的提供者未注册则返回空指针。

### 工具函数

`bhnd_format_chip_id` 函数成功时返回写入的总字节数，失败时返回负整数。

## 参见

[bhnd(4)](../man4/bhnd.4.md), [bhnd_erom(9)](bhnd_erom.9.md)

## 作者

`bhnd` 驱动程序编程接口和本手册页由 Landon Fuller <landonf@FreeBSD.org> 编写。
