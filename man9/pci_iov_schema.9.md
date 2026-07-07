# pci_iov_schema(9)

`pci_iov_schema` — PCI SR-IOV 配置架构接口

## 名称

`pci_iov_schema`, `pci_iov_schema_alloc_node`, `pci_iov_schema_add_bool`, `pci_iov_schema_add_string`, `pci_iov_schema_add_uint8`, `pci_iov_schema_add_uint16`, `pci_iov_schema_add_uint32`, `pci_iov_schema_add_uint64`, `pci_iov_schema_add_unicast_mac`

## 概要

```c
#include <sys/stdarg.h>
```

```c
#include <sys/nv.h>
```

```c
#include <sys/iov_schema.h>
```

```c
nvlist_t *
pci_iov_schema_alloc_node(void)

void
pci_iov_schema_add_bool(nvlist_t *schema, const char *name,
    uint32_t flags, int defaultVal)

void
pci_iov_schema_add_string(nvlist_t *schema, const char *name,
    uint32_t flags, const char *defaultVal)

void
pci_iov_schema_add_uint8(nvlist_t *schema, const char *name,
    uint32_t flags, uint8_t defaultVal)

void
pci_iov_schema_add_uint16(nvlist_t *schema, const char *name,
    uint32_t flags, uint16_t defaultVal)

void
pci_iov_schema_add_uint32(nvlist_t *schema, const char *name,
    uint32_t flags, uint32_t defaultVal)

void
pci_iov_schema_add_uint64(nvlist_t *schema, const char *name,
    uint32_t flags, uint64_t defaultVal)

void
pci_iov_schema_add_unicast_mac(nvlist_t *schema, const char *name,
    uint32_t flags, const uint8_t *defaultVal)
```

## 描述

PCI 单根 I/O 虚拟化（SR-IOV）配置架构是一种数据结构，描述在 PF 设备上启用 SR-IOV 时 PF 驱动程序将接受的设备特定配置参数。每个 PF 驱动程序定义两个架构实例：PF 架构和 VF 架构。PF 架构描述适用于整个 PF 设备的配置。VF 架构描述适用于单个 VF 设备的配置。不同的 VF 设备可以应用不同的配置，只要每个 VF 的配置符合 VF 架构即可。

PF 驱动程序通过首先分配架构节点，然后向架构添加配置参数规范来构建配置架构。配置参数规范由名称和值类型组成。

配置参数名称不区分大小写。指定两个或更多具有相同名称的配置参数是错误的。指定使用与 SR-IOV 基础设施使用的配置参数相同名称的配置参数也是错误的。有关 SR-IOV 基础设施使用的所有配置参数的文档，请参见 iovctl.conf(5)。

参数类型约束配置参数可能取的值。

可以通过在 `flags` 参数中设置 `IOV_SCHEMA_REQUIRED` 标志将配置参数指定为必需参数。启用 SR-IOV 时，用户必须指定必需参数。如果用户未指定必需参数，SR-IOV 基础设施将中止启用 SR-IOV 的请求并向用户返回错误。

或者，可以通过在 `flags` 参数中设置 `IOV_SCHEMA_HASDEFAULT` 标志为配置参数提供默认值。如果配置参数有默认值但用户未为该参数指定值，则 SR-IOV 基础设施将在配置传递给 PF 驱动程序之前为该参数应用 `defaultVal`。`defaultVal` 参数的值不符合指定类型的限制是错误的。如果未指定此标志，则忽略 `defaultVal` 参数。此标志与 `IOV_SCHEMA_REQUIRED` 标志不兼容；在同一参数上同时指定两者是错误的。

SR-IOV 基础设施保证所有指定为必需或给定默认值的配置参数都将出现在传递给 PF 驱动程序的配置中。既未指定为必需也未给定默认值的配置参数是可选的，可能出现在也可能不出现在传递给 PF 驱动程序的配置中。

强烈建议 PF 驱动程序将可选参数的使用保留给真正可选的配置。例如，网络接口 PF 设备可能具有将所有往返 VF 设备的流量封装在 vlan 标记中的选项。PF 驱动程序可以将该选项公开为接受指定 vlan 标记的整数参数的“vlan”参数。在这种情况下，将“vlan”参数设置为可选参数是合适的，因为将 VF 配置为完全不启用 vlan 标记是合理的。

或者，如果 PF 设备有一个控制是否允许 VF 更改其 MAC 地址的布尔选项，则不应将此参数设置为可选。PF 驱动程序必须允许或不允许 MAC 更改，因此 PF 驱动程序通过在架构中指定默认值来记录默认行为更为合适（或者可能通过将参数设置为必需来强制用户做出选择）。

具有安全影响的配置参数必须默认为可能的最安全配置。

所有设备特定的配置参数必须记录在 PF 驱动程序的手册页中，或记录在从主驱动程序手册页交叉引用的单独手册页中。

PF 驱动程序无需检查这些函数中任何一个的失败。如果发生错误，它会在架构中标记。pci_iov_attach(9) 函数检查此错误，如果架构中设置了错误，将无法在 PF 设备上初始化 SR-IOV。如果发生这种情况，建议 PF 驱动程序仍然成功附加并在设备上禁用 SR-IOV 运行。

`pci_iov_schema_alloc_node` 函数用于分配空配置架构。无需检查此函数的失败。SR-IOV 基础设施将优雅地处理分配架构失败，并简单地不在 PF 设备上启用 SR-IOV。

`pci_iov_schema_add_bool` 函数用于在给定架构中指定名为 `name` 且具有布尔类型的配置参数。布尔值只能取 true 或 false（分别为 1 或 0）。

`pci_iov_schema_add_string` 函数用于在给定架构中指定名为 `name` 且具有字符串类型的配置参数。字符串值是标准 C 字符串。

`pci_iov_schema_add_uint8` 函数用于在给定架构中指定名为 `name` 且具有 `uint8_t` 类型的配置参数。`uint8_t` 类型的值是 0 到 255（含）范围内的无符号整数。

`pci_iov_schema_add_uint16` 函数用于在给定架构中指定名为 `name` 且具有 `uint16_t` 类型的配置参数。`uint16_t` 类型的值是 0 到 65535（含）范围内的无符号整数。

`pci_iov_schema_add_uint32` 函数用于在给定架构中指定名为 `name` 且具有 `uint32_t` 类型的配置参数。`uint32_t` 类型的值是 0 到 (2\*\*32 - 1)（含）范围内的无符号整数。

`pci_iov_schema_add_uint64` 函数用于在给定架构中指定名为 `name` 且具有 `uint64_t` 类型的配置参数。`uint64_t` 类型的值是 0 到 (2\*\*64 - 1)（含）范围内的无符号整数。

`pci_iov_schema_add_unicast_mac` 函数用于在给定架构中指定名为 `name` 且具有 unicast-mac 类型的配置参数。unicast-mac 类型的值是恰好 6 字节长的二进制值。保证 MAC 地址不是多播或广播地址。

## 返回值

`pci_iov_schema_alloc_node` 函数返回指向已分配架构的指针，如果发生失败则返回 NULL。

## 参见

[pci(9)](pci.9.md), [PCI_IOV_ADD_VF(9)](pci_iov_add_vf.9.md), [PCI_IOV_INIT(9)](pci_iov_init.9.md)

## 作者

本手册页由 Ryan Stone <rstone@FreeBSD.org> 编写。
