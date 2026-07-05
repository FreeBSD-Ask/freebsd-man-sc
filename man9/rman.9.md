# rman.9

`rman` — 资源管理函数

## 名称

`rman`, `rman_activate_resource`, `rman_adjust_resource`, `rman_deactivate_resource`, `rman_fini`, `rman_init`, `rman_init_from_resource`, `rman_is_region_manager`, `rman_manage_region`, `rman_first_free_region`, `rman_last_free_region`, `rman_release_resource`, `rman_reserve_resource`, `rman_make_alignment_flags`, `rman_get_start`, `rman_get_end`, `rman_get_device`, `rman_get_size`, `rman_get_flags`, `rman_set_mapping`, `rman_get_mapping`, `rman_set_virtual`, `rman_get_virtual`, `rman_set_bustag`, `rman_get_bustag`, `rman_set_bushandle`, `rman_get_bushandle`, `rman_set_rid`, `rman_get_rid`, `rman_set_type`, `rman_get_type`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/rman.h>
```

```c
int
rman_activate_resource(struct resource *r)

int
rman_adjust_resource(struct resource *r, rman_res_t start, rman_res_t end)

int
rman_deactivate_resource(struct resource *r)

int
rman_fini(struct rman *rm)

int
rman_init(struct rman *rm)

int
rman_init_from_resource(struct rman *rm, struct resource *r)

int
rman_is_region_manager(struct resource *r, struct rman *rm)

int
rman_manage_region(struct rman *rm, rman_res_t start, rman_res_t end)

int
rman_first_free_region(struct rman *rm, rman_res_t *start, rman_res_t *end)

int
rman_last_free_region(struct rman *rm, rman_res_t *start, rman_res_t *end)

int
rman_release_resource(struct resource *r)

struct resource *
rman_reserve_resource(struct rman *rm, rman_res_t start, rman_res_t end, rman_res_t count, u_int flags, device_t dev)

uint32_t
rman_make_alignment_flags(uint32_t size)

rman_res_t
rman_get_start(struct resource *r)

rman_res_t
rman_get_end(struct resource *r)

device_t
rman_get_device(struct resource *r)

rman_res_t
rman_get_size(struct resource *r)

u_int
rman_get_flags(struct resource *r)

void
rman_set_mapping(struct resource *r, struct resource_map *map)

void
rman_get_mapping(struct resource *r, struct resource_map *map)

void
rman_set_virtual(struct resource *r, void *v)

void *
rman_get_virtual(struct resource *r)

void
rman_set_bustag(struct resource *r, bus_space_tag_t t)

bus_space_tag_t
rman_get_bustag(struct resource *r)

void
rman_set_bushandle(struct resource *r, bus_space_handle_t h)

bus_space_handle_t
rman_get_bushandle(struct resource *r)

void
rman_set_rid(struct resource *r, int rid)

int
rman_get_rid(struct resource *r)

void
rman_set_type(struct resource *r, int type)

int
rman_get_type(struct resource *r)
```

## 描述

`rman` 系列函数提供了灵活的资源管理抽象。它被总线管理代码广泛使用。它实现了区域和资源的抽象。区域描述符用于管理区域；这可以是内存或某种其他形式的总线空间。

每个区域都有一组边界。在这些边界内，可以驻留已分配的段。每个段（称为资源）有几个属性，由 16 位标志寄存器表示，如下所示。

```c
#define RF_ALLOCATED    0x0001 /* 资源已被预留 */
#define RF_ACTIVE       0x0002 /* 资源分配已被激活 */
#define RF_SHAREABLE    0x0004 /* 资源允许同时共享 */
#define RF_FIRSTSHARE   0x0020 /* 共享列表中的第一个 */
#define RF_PREFETCHABLE 0x0040 /* 资源可预取 */
#define RF_UNMAPPED     0x0100 /* 激活时不映射资源 */
```

标志寄存器的第 15:10 位用于表示资源在区域内的所需对齐方式。

`rman_init` 函数初始化由 `rm` 参数指向的区域描述符，以供资源管理函数使用。在调用 `rman_init` 之前，必须设置 `struct rman` 的 `rm_type` 和 `rm_descr` 字段。`rm_type` 字段应设置为 `RMAN_ARRAY`。`rm_descr` 字段应设置为描述要管理的资源的字符串。`rm_start` 和 `rm_end` 字段可以设置以限制可接受的资源地址范围。如果未设置这些字段，`rman_init` 将初始化它们以允许整个资源地址范围。它还初始化与该结构关联的任何互斥锁。如果 `rman_init` 未能初始化互斥锁，它将返回 `ENOMEM`；否则返回 0，`rm` 将被初始化。

`rman_fini` 函数释放与 `rm` 参数指向的结构关联的任何结构。如果受管区域内的任何资源设置了 `RF_ALLOCATED` 标志，它将返回 `EBUSY`；否则，与该结构关联的任何互斥锁将被释放和销毁，函数返回 0。

`rman_manage_region` 函数建立受 `rman` 控制的区域概念。`rman` 参数指向区域描述符。`start` 和 `end` 参数指定区域的边界。如果成功，`rman_manage_region` 返回 0。如果区域与现有区域重叠，返回 `EBUSY`。如果区域的任何部分落在 `rm` 的有效地址范围之外，返回 `EINVAL`。当 `rman_manage_region` 未能为区域分配内存时，返回 `ENOMEM`。

`rman_init_from_resource` 函数是一个包装例程，用于创建由现有资源支持的资源管理器。它使用 `rman_init` 初始化 `rm`，然后通过 `rman_manage_region` 将与分配给 `r` 的地址范围对应的区域添加到 `rm` 中。

`rman_first_free_region` 和 `rman_last_free_region` 函数可用于查询资源管理器的第一个（或最后一个）未分配区域。如果 `rm` 不包含空闲区域，这些函数返回 `ENOENT`。否则，`*start` 和 `*end` 设置为空闲区域的边界，返回零。

`rman_reserve_resource` 函数是 `rman` 大部分逻辑所在之处。它尝试在指定区域 `rm` 中为设备 `dev` 的使用预留连续范围。调用者可以指定可接受范围的 `start` 和 `end`、所需对齐方式，代码将尝试找到适合的空闲段。`start` 参数是资源的最低可接受起始值。`end` 参数是资源的最高可接受结束值。因此，`start` + `count` - 1 必须 <= `end` 才能进行任何分配。对齐要求（如果有）在 `flags` 中指定。通常使用 `RF_ALIGNMENT_LOG2` 宏指定 2 的幂次大小对齐，或使用 `rman_make_alignment_flags` 在运行时计算 `flags` 值。如果设置了 `RF_SHAREABLE` 标志，将分配共享段，否则将分配独占段。如果此共享段已存在，调用者的设备将添加到消费者列表中。

`rman_make_alignment_flags` 函数返回与所需对齐 `size` 对应的标志掩码。这应在调用 `rman_reserve_resource_bound` 时使用。

`rman_is_region_manager` 函数在已分配的资源 `r` 是从 `rm` 分配时返回 true。否则返回 false。

`rman_adjust_resource` 函数用于调整已分配资源的预留地址范围，以预留从 `start` 到 `end` 的范围。它可用于增长或收缩资源范围的一端或两端。当前实现不支持完全重定位资源，如果新资源范围与旧资源范围不重叠，将失败并返回 `EINVAL`。如果资源范围的任一端增长且新资源范围会与另一个已分配资源冲突，函数将失败并返回 `EBUSY`。`rman_adjust_resource` 函数不支持调整共享资源的资源范围，此类尝试将失败并返回 `EINVAL`。成功时，资源 `r` 的起始地址将为 `start`，结束地址将为 `end`，函数返回零。注意，`rman_adjust_resource` 不检查原始分配请求的任何约束（如对齐或边界限制）。强制执行任何此类要求是调用者的责任。

`rman_release_resource` 函数释放预留的资源 `r`。它可能尝试合并相邻的空闲资源。

`rman_activate_resource` 函数通过设置 `RF_ACTIVE` 标志将资源标记为活动。如果这是分时共享资源，且调用者尚未获取该资源，函数返回 `EBUSY`。

`rman_deactivate_resource` 函数通过清除 `RF_ACTIVE` 标志将资源 `r` 标记为非活动。如果其他消费者正在等待此范围，它将唤醒它们的线程。

`rman_get_start`、`rman_get_end`、`rman_get_size` 和 `rman_get_flags` 函数返回先前预留的资源 `r` 的边界、大小和标志。

`rman_set_bustag` 函数将 `bus_space_tag_t` `t` 与资源 `r` 关联。`rman_get_bustag` 函数用于在设置后检索此标签。

`rman_set_bushandle` 函数将 `bus_space_handle_t` `h` 与资源 `r` 关联。`rman_get_bushandle` 函数用于在设置后检索此句柄。

`rman_set_virtual` 函数用于将内核虚拟地址与资源 `r` 关联。`rman_get_virtual` 函数可用于在设置后检索 KVA。

`rman_set_mapping` 函数用于将资源映射与资源 `r` 关联。映射必须覆盖整个资源。设置映射会为 `r` 设置关联的 [bus_space(9)](bus_space.9.md) 句柄和标签，以及内核虚拟地址（如果映射包含）。这些单独的值可以通过 `rman_get_bushandle`、`rman_get_bustag` 和 `rman_get_virtual` 检索。

`rman_get_mapping` 函数可用于在设置后检索关联的资源映射。

`rman_set_rid` 函数将资源标识符与资源 `r` 关联。`rman_get_rid` 函数检索此 RID。

`rman_set_type` 函数将资源类型与资源 `r` 关联。`rman_get_type` 函数检索此类型。

`rman_get_device` 函数返回指向预留资源 `r` 的设备的指针。

## 参见

[bus_activate_resource(9)](bus_activate_resource.9.md), [bus_adjust_resource(9)](bus_adjust_resource.9.md), [bus_alloc_resource(9)](bus_alloc_resource.9.md), [bus_map_resource(9)](bus_map_resource.9.md), [bus_release_resource(9)](bus_release_resource.9.md), [bus_set_resource(9)](bus_set_resource.9.md), [bus_space(9)](bus_space.9.md), [mutex(9)](mutex.9.md)

## 作者

本手册页由 Bruce M Simpson <bms@spc.org> 编写。
