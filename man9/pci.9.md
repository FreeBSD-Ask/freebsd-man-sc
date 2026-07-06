# pci.9

`pci` — PCI 总线接口

## 名称

`pci`, `is_pci_device`, `pci_alloc_msi`, `pci_alloc_msix`, `pci_clear_pme`, `pci_disable_busmaster`, `pci_disable_io`, `pci_enable_busmaster`, `pci_enable_io`, `pci_enable_pme`, `pci_find_bsf`, `pci_find_cap`, `pci_find_dbsf`, `pci_find_device`, `pci_find_extcap`, `pci_find_htcap`, `pci_find_next_cap`, `pci_find_next_extcap`, `pci_find_next_htcap`, `pci_find_pcie_root_port`, `pci_get_id`, `pci_get_max_payload`, `pci_get_max_read_req`, `pci_get_powerstate`, `pci_get_vpd_ident`, `pci_get_vpd_readonly`, `pci_has_pm`, `pci_iov_attach`, `pci_iov_attach_name`, `pci_iov_detach`, `pci_msi_count`, `pci_msix_count`, `pci_msix_pba_bar`, `pci_msix_table_bar`, `pci_pending_msix`, `pci_read_config`, `pci_release_msi`, `pci_remap_msix`, `pci_restore_state`, `pci_save_state`, `pci_set_max_read_req`, `pci_set_powerstate`, `pci_write_config`, `pcie_adjust_config`, `pcie_flr`, `pcie_get_max_completion_timeout`, `pcie_read_config`, `pcie_wait_for_pending_transactions`, `pcie_write_config`

## 概要

```c
#include <sys/bus.h>
```

```c
#include <dev/pci/pcireg.h>
```

```c
#include <dev/pci/pcivar.h>
```

```c
bool
is_pci_device(device_t dev)

int
pci_alloc_msi(device_t dev, int *count)

int
pci_alloc_msix(device_t dev, int *count)

void
pci_clear_pme(device_t dev)

int
pci_disable_busmaster(device_t dev)

int
pci_disable_io(device_t dev, int space)

int
pci_enable_busmaster(device_t dev)

int
pci_enable_io(device_t dev, int space)

void
pci_enable_pme(device_t dev)

device_t
pci_find_bsf(uint8_t bus, uint8_t slot, uint8_t func)

int
pci_find_cap(device_t dev, int capability, int *capreg)

device_t
pci_find_dbsf(uint32_t domain, uint8_t bus, uint8_t slot, uint8_t func)

device_t
pci_find_device(uint16_t vendor, uint16_t device)

int
pci_find_extcap(device_t dev, int capability, int *capreg)

int
pci_find_htcap(device_t dev, int capability, int *capreg)

int
pci_find_next_cap(device_t dev, int capability, int start, int *capreg)

int
pci_find_next_extcap(device_t dev, int capability, int start, int *capreg)

int
pci_find_next_htcap(device_t dev, int capability, int start, int *capreg)

device_t
pci_find_pcie_root_port(device_t dev)

int
pci_get_id(device_t dev, enum pci_id_type type, uintptr_t *id)

int
pci_get_max_payload(device_t dev)

int
pci_get_max_read_req(device_t dev)

int
pci_get_powerstate(device_t dev)

int
pci_get_vpd_ident(device_t dev, const char **identptr)

int
pci_get_vpd_readonly(device_t dev, const char *kw, const char **vptr)

bool
pci_has_pm(device_t dev)

int
pci_msi_count(device_t dev)

int
pci_msix_count(device_t dev)

int
pci_msix_pba_bar(device_t dev)

int
pci_msix_table_bar(device_t dev)

int
pci_pending_msix(device_t dev, u_int index)

uint32_t
pci_read_config(device_t dev, int reg, int width)

int
pci_release_msi(device_t dev)

int
pci_remap_msix(device_t dev, int count, const u_int *vectors)

void
pci_restore_state(device_t dev)

void
pci_save_state(device_t dev)

int
pci_set_max_read_req(device_t dev, int size)

int
pci_set_powerstate(device_t dev, int state)

void
pci_write_config(device_t dev, int reg, uint32_t val, int width)

uint32_t
pcie_adjust_config(device_t dev, int reg, uint32_t mask, uint32_t val,
    int width)

bool
pcie_flr(device_t dev, u_int max_delay, bool force)

int
pcie_get_max_completion_timeout(device_t dev)

uint32_t
pcie_read_config(device_t dev, int reg, int width)

bool
pcie_wait_for_pending_transactions(device_t dev, u_int max_delay)

void
pcie_write_config(device_t dev, int reg, uint32_t val, int width)

void
pci_event_fn(void *arg, device_t dev)

EVENTHANDLER_REGISTER(pci_add_device, pci_event_fn)
EVENTHANDLER_DEREGISTER(pci_delete_resource, pci_event_fn)
```

```c
#include <dev/pci/pci_iov.h>
```

```c
int
pci_iov_attach(device_t dev, nvlist_t *pf_schema, nvlist_t *vf_schema)

int
pci_iov_attach_name(device_t dev, nvlist_t *pf_schema,
    nvlist_t *vf_schema, const char *fmt, ...)

int
pci_iov_detach(device_t dev)
```

## 描述

`pcie_write_config` 系列函数用于管理 PCI 设备。这些函数分为几组：原始配置访问、定位设备、设备信息、设备配置和消息信号中断。

`is_pci_device` 函数可用于确定 `dev` 是否为 PCI 设备。

### 原始配置访问

`pci_read_config` 函数用于从设备 `dev` 的 PCI 配置空间读取数据，偏移量为 `reg`，`width` 指定访问的大小。

`pci_write_config` 函数用于将值 `val` 写入设备 `dev` 的 PCI 配置空间，偏移量为 `reg`，`width` 指定访问的大小。

`pcie_adjust_config` 函数用于修改设备 `dev` 的 PCI-express 能力寄存器集中寄存器的值。偏移量 `reg` 指定寄存器集中的相对偏移量，`width` 指定访问的大小。寄存器的新值通过将 `mask` 中设置的位修改为 `val` 中的值来计算。未在 `mask` 中指定的任何位都被保留。返回寄存器的先前值。

`pcie_read_config` 函数用于读取设备 `dev` 的 PCI-express 能力寄存器集中寄存器的值。偏移量 `reg` 指定寄存器集中的相对偏移量，`width` 指定访问的大小。

`pcie_write_config` 函数用于将值 `val` 写入设备 `dev` 的 PCI-express 能力寄存器集中的寄存器。偏移量 `reg` 指定寄存器集中的相对偏移量，`width` 指定访问的大小。

*注意：* 设备驱动程序应仅将这些函数用于无法通过其他 `pci` 函数使用的功能。

### 定位设备

`pci_find_bsf` 函数根据 PCI 设备的 `bus`、`slot` 和 `func` 查找其 `device_t`。`slot` 号实际上是指设备在总线上的编号，不一定表示其在物理插槽方面的地理位置。注意，如果系统有多个 PCI 域，`pci_find_bsf` 函数只搜索第一个域。实际上，它等同于：

```sh
pci_find_dbsf(0, bus, slot, func);
```

`pci_find_dbsf` 函数根据 PCI 设备的 `domain`、`bus`、`slot` 和 `func` 查找其 `device_t`。`slot` 号实际上是指设备在总线上的编号，不一定表示其在物理插槽方面的地理位置。

`pci_find_device` 函数根据 PCI 设备的 `vendor` 和 `device` ID 查找其 `device_t`。注意，此搜索可能有多个匹配项；此函数仅返回第一个匹配的设备。

### 设备信息

`pci_find_cap` 函数用于定位设备 `dev` 的第一个 PCI 能力寄存器集实例。要定位的能力通过 `capability` 以 ID 指定。标准能力 ID 的形式为 `PCIY_xxx` 的常量宏定义在

```c
#include <dev/pci/pcireg.h>
```

如果找到能力，则 `*capreg` 设置为能力寄存器集在配置空间中的偏移量，`pci_find_cap` 返回零。如果未找到能力或设备不支持能力，`pci_find_cap` 返回错误。`pci_find_next_cap` 函数用于定位设备 `dev` 的下一个 PCI 能力寄存器集实例。`start` 应为先前 `pci_find_cap` 或 `pci_find_next_cap` 返回的 `*capreg`。当没有更多实例时，`pci_find_next_cap` 返回错误。

`pci_has_pm` 函数如果 `dev` 支持电源管理则返回 true。

`pci_find_extcap` 函数用于定位设备 `dev` 的第一个 PCI-express 扩展能力寄存器集实例。要定位的扩展能力通过 `capability` 以 ID 指定。标准扩展能力 ID 的形式为 `PCIZ_xxx` 的常量宏定义在

```c
#include <dev/pci/pcireg.h>
```

如果找到扩展能力，则 `*capreg` 设置为扩展能力寄存器集在配置空间中的偏移量，`pci_find_extcap` 返回零。如果未找到扩展能力或设备不是 PCI-express 设备，`pci_find_extcap` 返回错误。`pci_find_next_extcap` 函数用于定位设备 `dev` 的下一个 PCI-express 扩展能力寄存器集实例。`start` 应为先前 `pci_find_extcap` 或 `pci_find_next_extcap` 返回的 `*capreg`。当没有更多实例时，`pci_find_next_extcap` 返回错误。

`pci_find_htcap` 函数用于定位设备 `dev` 的第一个 HyperTransport 能力寄存器集实例。要定位的能力通过 `capability` 以类型指定。标准 HyperTransport 能力类型的形式为 `PCIM_HTCAP_xxx` 的常量宏定义在

```c
#include <dev/pci/pcireg.h>
```

如果找到能力，则 `*capreg` 设置为能力寄存器集在配置空间中的偏移量，`pci_find_htcap` 返回零。如果未找到能力或设备不是 HyperTransport 设备，`pci_find_htcap` 返回错误。`pci_find_next_htcap` 函数用于定位设备 `dev` 的下一个 HyperTransport 能力寄存器集实例。`start` 应为先前 `pci_find_htcap` 或 `pci_find_next_htcap` 返回的 `*capreg`。当没有更多实例时，`pci_find_next_htcap` 返回错误。

`pci_find_pcie_root_port` 函数沿 PCI 设备层次结构向上查找 `dev` 上游的 PCI-express 根端口。如果未找到根端口，`pci_find_pcie_root_port` 返回 `NULL`。

`pci_get_id` 函数用于从设备读取标识符。`type` 标志用于指定要读取的标识符。支持以下标志：

**`PCI_ID_RID`** 读取设备的路由标识符。

**`PCI_ID_MSI`** 读取 MSI 路由 ID。某些中断控制器需要它来路由 MSI 和 MSI-X 中断。

`pci_get_vpd_ident` 函数用于获取设备的 Vital Product Data（VPD）标识符字符串。如果设备 `dev` 支持 VPD 并提供标识符字符串，则 `*identptr` 设置为指向标识符字符串的只读、以 null 结尾的副本，`pci_get_vpd_ident` 返回零。如果设备不支持 VPD 或不提供标识符字符串，`pci_get_vpd_ident` 返回错误。

`pci_get_vpd_readonly` 函数用于获取设备 `dev` 的单个 VPD 只读关键字的值。要获取的关键字由两个字符的字符串 `kw` 标识。如果设备支持 VPD 并为请求的关键字提供只读值，则 `*vptr` 设置为指向该值的只读、以 null 结尾的副本，`pci_get_vpd_readonly` 返回零。如果设备不支持 VPD 或不提供请求的关键字，`pci_get_vpd_readonly` 返回错误。

`pcie_get_max_completion_timeout` 函数返回为设备 `dev` 配置的最大完成超时（以微秒为单位）。如果 `dev` 设备不是 PCI-express 设备，`pcie_get_max_completion_timeout` 返回零。当 `dev` 禁用完成超时时，此函数返回如果启用超时将使用的最大超时。

`pcie_wait_for_pending_transactions` 函数等待 `dev` 设备发起的任何挂起事务完成。该函数通过轮询 PCI-express 设备状态寄存器中的事务挂起标志来检查挂起事务。一旦事务挂起标志清除，它返回 `true`。如果在 `max_delay` 毫秒后仍有事务挂起，`pcie_wait_for_pending_transactions` 返回 `false`。如果 `max_delay` 设置为零，`pcie_wait_for_pending_transactions` 执行单次检查；否则，此函数可能在轮询事务挂起标志时休眠。如果 `dev` 不是 PCI-express 设备，`pcie_wait_for_pending_transactions` 返回 `true`。

### 设备配置

`pci_enable_busmaster` 函数通过在 `PCIR_COMMAND` 寄存器中设置 `PCIM_CMD_BUSMASTEREN` 位来为设备 `dev` 启用 PCI 总线主控。`pci_disable_busmaster` 函数清除该位。

`pci_enable_io` 函数通过适当设置 `PCIR_COMMAND` 寄存器中的 `PCIM_CMD_MEMEN` 或 `PCIM_CMD_PORTEN` 位来为设备 `dev` 启用内存或 I/O 端口地址解码。`pci_disable_io` 函数清除相应的位。`space` 参数指定受影响的资源；可以是 `SYS_RES_MEMORY` 或 `SYS_RES_IOPORT`。设备驱动程序通常不应直接使用这些例程。当通过 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 或 [bus_activate_resource(9)](bus_activate_resource.9.md) 激活 `SYS_RES_MEMORY` 或 `SYS_RES_IOPORT` 资源时，PCI 总线将自动启用解码。

`pci_get_max_payload` 函数返回 PCI-express 设备的当前最大 TLP 负载大小（以字节为单位）。如果 `dev` 设备不是 PCI-express 设备，`pci_get_max_payload` 返回零。

`pci_get_max_read_req` 函数返回 PCI-express 设备的当前最大读取请求大小（以字节为单位）。如果 `dev` 设备不是 PCI-express 设备，`pci_get_max_read_req` 返回零。

`pci_set_max_read_req` 设置 `dev` 的 PCI-express 最大读取请求大小。请求的 `size` 可能被调整，`pci_set_max_read_req` 返回实际设置的大小（以字节为单位）。如果 `dev` 设备不是 PCI-express 设备，`pci_set_max_read_req` 返回零。

`pci_get_powerstate` 函数返回设备 `dev` 的当前电源状态。如果设备不支持电源管理能力，则返回默认状态 `PCI_POWERSTATE_D0`。PCI 定义了以下电源状态：

**`PCI_POWERSTATE_D0`** 设备开启并运行的状态。它从系统接收全功率并向用户提供完整功能。

**`PCI_POWERSTATE_D1`** 类特定的低功率状态，设备上下文可能丢失也可能不丢失。在此状态下的总线无法对总线执行任何操作来强制设备丢失上下文。

**`PCI_POWERSTATE_D2`** 类特定的低功率状态，设备上下文可能丢失也可能不丢失。比 `PCI_POWERSTATE_D1` 获得更大的节能。在此状态下的总线可能导致设备丢失一些上下文。设备*必须*准备好总线处于此状态或更高状态。

**`PCI_POWERSTATE_D3_HOT`** 设备关闭且未运行的状态。设备上下文丢失，设备的电源可以（但不一定）被移除。

**`PCI_POWERSTATE_D3_COLD`** 与 `PCI_POWERSTATE_D3_HOT` 相同，只是设备的电源已被移除。

**`PCI_POWERSTATE_UNKNOWN`** 设备状态未知。

`pci_set_powerstate` 函数用于将设备 `dev` 转换到 PCI 电源状态 `state`。如果设备不支持电源管理能力或不支持特定电源状态 `state`，则函数将失败并返回 EOPNOTSUPP。

`pci_clear_pme` 函数用于清除任何挂起的 PME# 信号并禁用电源管理事件的生成。

`pci_enable_pme` 函数用于在挂起设备之前启用电源管理事件的生成。

`pci_iov_attach` 函数用于声明给定设备（及关联的设备驱动程序）支持 PCI 单根 I/O 虚拟化（SR-IOV）。支持 SR-IOV 的驱动程序必须实现 [PCI_IOV_INIT(9)](pci_iov_init.9.md)、[PCI_IOV_ADD_VF(9)](pci_iov_add_vf.9.md) 和 [PCI_IOV_UNINIT(9)](pci_iov_uninit.9.md) 方法。此函数应在 [DEVICE_ATTACH(9)](device_attach.9.md) 方法期间调用。如果此函数返回错误，建议设备驱动程序仍然成功附加，但禁用 SR-IOV 运行。`pf_schema` 和 `vf_schema` 参数用于分别定义为物理功能（PF）和单个虚拟功能（VF）启用 SR-IOV 时设备驱动程序接受的设备特定配置参数。有关如何构建架构的详细信息，请参见 [pci_iov_schema(9)](pci_iov_schema.9.md)。如果 `pf_schema` 或 `vf_schema` 无效或指定的参数名称与已使用的参数名称冲突，`pci_iov_attach` 将返回错误，PF 设备上将不可用 SR-IOV。如果驱动程序不接受 PF 设备或 VF 设备的配置参数，驱动程序必须为该设备传递空架构。SR-IOV 基础设施取得 `pf_schema` 和 `vf_schema` 的所有权，并负责释放它们。驱动程序绝不能自行释放架构。

`pci_iov_attach_name` 函数是 `pci_iov_attach` 的变体，允许 **`/dev/iov`** 中关联字符设备的名称由 `fmt` 指定。`pci_iov_attach` 函数使用 `dev` 的名称作为设备名称。

`pci_iov_detach` 函数用于通知 SR-IOV 基础设施给定设备的驱动程序正在尝试分离，并且必须释放该设备的所有 SR-IOV 资源。如果在设备上成功调用了 `pci_iov_attach` 且随后未在设备上调用 `pci_iov_detach` 并返回无错误，则必须在 [DEVICE_DETACH(9)](device_detach.9.md) 方法期间调用此函数。如果此函数返回错误，[DEVICE_DETACH(9)](device_detach.9.md) 方法必须失败并返回错误，因为在 VF 设备活动时分离 PF 驱动程序会导致系统不稳定。如果 `pci_iov_attach` 先前在给定设备上失败并返回错误，或从未在设备上调用 `pci_iov_attach`，则此函数调用是安全的并将始终成功。

`pci_save_state` 和 `pci_restore_state` 函数可供设备驱动程序用于保存和恢复标准 PCI 配置寄存器。必须在设备具有有效状态时调用 `pci_save_state` 函数，然后才能使用 `pci_restore_state`。如果调用 `pci_restore_state` 时设备未处于完全加电状态（`PCI_POWERSTATE_D0`），则在恢复任何配置寄存器之前，设备将被转换到 `PCI_POWERSTATE_D0`。

`pcie_flr` 函数请求对 `dev` 进行功能级重置（FLR）。如果 `dev` 不是 PCI-express 设备或不支持通过 PCI-express 设备控制寄存器进行功能级重置，则返回 `false`。在重置设备之前，通过禁用总线主控并调用 `pcie_wait_for_pending_transactions` 来排空挂起事务。`max_delay` 参数指定等待挂起事务的最大超时，如 `pcie_wait_for_pending_transactions` 所述。如果 `pcie_wait_for_pending_transactions` 因超时失败且 `force` 为 `false`，则重新启用总线主控并返回 `false`。如果 `pcie_wait_for_pending_transactions` 因超时失败且 `force` 为 `true`，则不顾超时重置设备。请求重置后，`pcie_flr` 休眠至少 100 毫秒后返回 `true`。注意，`pcie_flr` 不会在重置前后保存和恢复任何状态。调用者应根据需要保存和恢复状态。

### 消息信号中断

消息信号中断（MSI）和增强消息信号中断（MSI-X）是 PCI 能力，为 PCI 设备提供信号中断的替代方法。传统 INTx 中断可用于 PCI 设备，作为资源 ID 为零的 `SYS_RES_IRQ` 资源。MSI 和 MSI-X 中断可用于 PCI 设备，作为一个或多个资源 ID 大于零的 `SYS_RES_IRQ` 资源。驱动程序必须先使用 `pci_alloc_msi` 或 `pci_alloc_msix` 请求 PCI 总线分配 MSI 或 MSI-X 中断，然后才能使用 MSI 或 MSI-X `SYS_RES_IRQ` 资源。如果已分配 MSI 或 MSI-X 中断，则不允许驱动程序使用传统 INTx `SYS_RES_IRQ` 资源，如果驱动程序当前正在使用传统 INTx `SYS_RES_IRQ` 资源，则尝试分配 MSI 或 MSI-X 中断将失败。驱动程序只能使用 MSI 或 MSI-X 中的一种，不能同时使用两者。

`pci_msi_count` 函数返回设备 `dev` 支持的最大 MSI 消息数。如果设备不支持 MSI，`pci_msi_count` 返回零。

`pci_alloc_msi` 函数尝试为设备 `dev` 分配 `*count` 条 MSI 消息。由于各种原因，包括请求的消息数超过设备 `dev` 支持的数量，或系统可用 MSI 消息短缺，`pci_alloc_msi` 函数可能分配少于请求的消息数。成功时，`*count` 设置为分配的消息数，`pci_alloc_msi` 返回零。已分配消息的 `SYS_RES_IRQ` 资源将从一开始的资源 ID 连续可用。如果 `pci_alloc_msi` 无法分配任何消息，则返回错误。注意，MSI 仅支持 2 的幂的消息计数；请求分配非 2 的幂的消息计数将失败。

`pci_release_msi` 函数用于将任何已分配的 MSI 或 MSI-X 消息释放回系统。如果驱动程序已分配任何 MSI 或 MSI-X `SYS_RES_IRQ` 资源或已配置中断处理程序，此函数将失败并返回 EBUSY。`pci_release_msi` 函数成功时返回零，失败时返回错误。

`pci_msix_count` 函数返回设备 `dev` 支持的最大 MSI-X 消息数。如果设备不支持 MSI-X，`pci_msix_count` 返回零。

`pci_msix_pba_bar` 函数返回设备 `dev` 包含 MSI-X 挂起位数组（PBA）的基址寄存器（BAR）在配置空间中的偏移量。返回值可作为资源 ID 与 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 和 [bus_release_resource(9)](bus_release_resource.9.md) 一起使用以分配 BAR。如果设备不支持 MSI-X，`pci_msix_pba_bar` 返回 -1。

`pci_msix_table_bar` 函数返回设备 `dev` 包含 MSI-X 向量表的 BAR 在配置空间中的偏移量。返回值可作为资源 ID 与 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 和 [bus_release_resource(9)](bus_release_resource.9.md) 一起使用以分配 BAR。如果设备不支持 MSI-X，`pci_msix_table_bar` 返回 -1。

`pci_alloc_msix` 函数尝试为设备 `dev` 分配 `*count` 条 MSI-X 消息。由于各种原因，包括请求的消息数超过设备 `dev` 支持的数量，或系统可用 MSI-X 消息短缺，`pci_alloc_msix` 函数可能分配少于请求的消息数。成功时，`*count` 设置为分配的消息数，`pci_alloc_msix` 返回零。对于 MSI-X 消息，每个 `SYS_RES_IRQ` 资源的资源 ID 标识相应消息在 MSI-X 表中的索引。资源 ID 一映射到 MSI-X 表的第一个索引；资源 ID 二标识表中的第二个索引，以此类推。`pci_alloc_msix` 函数将分配的 `*count` 条消息分配给前 `*count` 个表索引。如果 `pci_alloc_msix` 无法分配任何消息，则返回错误。与 MSI 不同，MSI-X 不要求消息计数为 2 的幂。

包含 MSI-X 向量表和 PBA 的 BAR 必须在调用 `pci_alloc_msix` 之前通过 [bus_alloc_resource(9)](bus_alloc_resource.9.md) 分配，并且必须直到调用 `pci_release_msi` 之后才能释放。注意，向量表和 PBA 可能存储在同一 BAR 或不同 BAR 中。

`pci_pending_msix` 函数检查 `dev` 设备的 PBA 以确定表索引 `index` 处的 MSI-X 消息的挂起状态。如果指示的消息挂起，此函数返回非零值；否则返回零。向此函数传递无效的 `index` 将导致未定义行为。

如 `pci_alloc_msix` 的描述中所述，MSI-X 消息最初分配给前 N 个表条目。驱动程序可以通过 `pci_remap_msix` 函数使用不同的可用消息到表条目的分布。注意，此函数必须在成功调用 `pci_alloc_msix` 之后但在分配任何 `SYS_RES_IRQ` 资源之前调用。`pci_remap_msix` 函数成功时返回零，失败时返回错误。

`vectors` 数组应包含 `count` 个消息向量。该数组直接映射到 MSI-X 表，数组中的第一个条目指定用于 MSI-X 表中第一个条目的消息，数组中的第二个条目对应于 MSI-X 表中的第二个条目，以此类推。每个数组索引中的向量值可以为零以指示不应将消息分配给相应的 MSI-X 表条目，也可以是 1 到 N（其中 N 是先前调用 `pci_alloc_msix` 返回的计数）之间的数字，以指示应将哪个已分配的消息分配给相应的 MSI-X 表条目。

如果 `pci_remap_msix` 成功，每个具有非零向量的 MSI-X 表条目将有一个关联的 `SYS_RES_IRQ` 资源，其资源 ID 对应于上述 `pci_alloc_msix` 描述的表索引。向量为零的 MSI-X 表条目将没有关联的 `SYS_RES_IRQ` 资源。此外，如果 `pci_alloc_msix` 分配的任何原始消息未在新分布中用于 MSI-X 表，它们将自动释放。注意，如果驱动程序希望使用少于 `pci_alloc_msix` 分配的消息数，驱动程序必须在新分布中使用从 1 开始的单一连续消息范围。如果不满足此条件，`pci_remap_msix` 函数将失败。

### 设备事件

每次将新 PCI 设备添加到系统时都会调用 `pci_add_device` 事件处理程序。这包括通过 SR-IOV 创建虚拟功能。

每次从系统中移除 PCI 设备时都会调用 `pci_delete_device` 事件处理程序。

两个事件处理程序都将相关 PCI 设备的 `device_t` 对象作为 `dev` 传递给每个回调函数。两个事件处理程序都在 `dev` 未附加但具有有效实例变量时调用。

## 参见

[pci(4)](../man4/pci.4.md), pciconf(8), [bus_alloc_resource(9)](bus_alloc_resource.9.md), [bus_dma(9)](bus_dma.9.md), [bus_release_resource(9)](bus_release_resource.9.md), bus_setup_intr(9), bus_teardown_intr(9), [devclass(9)](devclass.9.md), [device(9)](device.9.md), [driver(9)](driver.9.md), eventhandler(9), [rman(9)](rman.9.md)

> "NewBus", *FreeBSD Developers' Handbook*.

> Shanley, Anderson, *PCI System Architecture*, 2nd Edition, Addison-Wesley, ISBN 0-201-30974-2.

## 作者

本手册页由 Bruce M Simpson <bms@FreeBSD.org> 和 John Baldwin <jhb@FreeBSD.org> 编写。

## 缺陷

内核 PCI 代码中有许多对“插槽号”的引用。这些不是指 PCI 设备的地理位置，而是指由 PCI IDSEL 机制和平台固件组合分配的设备号。在使用内核 PCI 代码时应注意这一点。

PCI 总线驱动程序应在内部根据需要分配 MSI-X 向量表和 PBA，而不是要求调用者这样做。
