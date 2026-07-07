# PCI_IOV_ADD_VF(9)

`PCI_IOV_ADD_VF` — 通知 PF 驱动程序正在创建 VF

## 名称

`PCI_IOV_ADD_VF`

## 概要

```c
#include <sys/bus.h>
#include <sys/stdarg.h>
#include <sys/nv.h>
#include <dev/pci/pci_iov.h>

int
PCI_IOV_ADD_VF(device_t dev, uint16_t vfnum, const nvlist_t *vf_config)
```

## 描述

`PCI_IOV_ADD_VF` 方法由 PCI 单根 I/O 虚拟化（SR-IOV）基础设施在初始化一个新的虚拟功能（VF）作为给定物理功能（PF）设备的子设备时调用。在成功调用 [PCI_IOV_INIT(9)](pci_iov_init.9.md) 之前不会调用此方法。不保证在成功调用 [PCI_IOV_INIT(9)](pci_iov_init.9.md) 之后一定会调用此方法。如果基础设施在调用 [PCI_IOV_INIT(9)](pci_iov_init.9.md) 之后遇到资源分配失败，VF 的创建将被中止，并且将立即调用 [PCI_IOV_UNINIT(9)](pci_iov_uninit.9.md)，而不会在此之前调用任何 `PCI_IOV_ADD_VF`。

正在初始化的 VF 的索引通过 `vfnum` 参数传递。VF 始终从 0 开始按顺序编号。

如果驱动程序在其对 pci_iov_attach(9) 的调用中通过 VF 模式请求了设备特定的配置参数，这些参数将包含在 `vf_config` 参数中。在 VF 模式中设置为必需参数或设置了默认值的所有配置参数都保证存在于 `vf_config` 中。既未设置为必需也未设置默认值的配置参数是可选的，可能存在于 `vf_config` 中，也可能不存在。`vf_config` 不会包含未在 VF 模式中指定的任何配置参数。所有配置参数都将具有正确的类型，并且位于模式中指定的有效值范围内。

注意，用户可能会在同一 PF 的不同 VF 子设备上设置不同的配置值。PF 驱动程序不得缓存先前对其他 VF 调用 `PCI_IOV_ADD_VF` 时传递的配置参数，并将这些参数应用于当前 VF。

在未先依次调用 [PCI_IOV_UNINIT(9)](pci_iov_uninit.9.md) 和 [PCI_IOV_INIT(9)](pci_iov_init.9.md) 的情况下，不会对同一 PF 设备上的同一 `vf_num` 调用此函数两次。

## 返回值

此方法成功时返回 0，否则返回适当的错误。如果此方法返回错误，则当前 VF 设备将被销毁，但其余 VF 设备将被创建，并且将在 PF 上启用 SR-IOV。

## 参见

[nv(9)](nv.9.md), [pci(9)](pci.9.md), [PCI_IOV_INIT(9)](pci_iov_init.9.md), [pci_iov_schema(9)](pci_iov_schema.9.md), [PCI_IOV_UNINIT(9)](pci_iov_uninit.9.md)

## 作者

本手册页由 Ryan Stone <rstone@FreeBSD.org> 编写。
