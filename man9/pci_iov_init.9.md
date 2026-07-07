# PCI_IOV_INIT(9)

`PCI_IOV_INIT` — 在 PF 设备上启用 SR-IOV

## 名称

`PCI_IOV_INIT`

## 概要

```c
#include <sys/bus.h>
#include <sys/stdarg.h>
#include <sys/nv.h>
#include <dev/pci/pci_iov.h>

int
PCI_IOV_INIT(device_t dev, uint16_t num_vfs, const nvlist_t *pf_config)
```

## 描述

`PCI_IOV_INIT` 方法在用户请求在物理功能（PF）上启用 SR-IOV 时由 PCI 单根 I/O 虚拟化（SR-IOV）基础设施调用。将要创建的虚拟功能（VF）数量通过 `num_vfs` 参数传递给此方法。

如果驱动程序在其对 pci_iov_attach(9) 的调用中通过 PF 模式请求了设备特定的 PF 配置参数，这些参数将在 `pf_config` 参数中可用。在 PF 模式中设置为必需参数或设置了默认值的所有配置参数都保证存在于 `pf_config` 中。既未设置为必需也未设置默认值的配置参数是可选的，可能存在于 `pf_config` 中，也可能不存在。`pf_config` 不会包含未在 PF 模式中指定的任何配置参数。所有配置参数都将具有正确的类型，并位于模式中指定的有效值范围内。

如果此方法成功返回，则在此方法再次被调用之前（直到调用 [PCI_IOV_UNINIT(9)](pci_iov_uninit.9.md) 之后），不会在同一设备上再次调用此方法。

## 返回值

成功时返回 0，否则返回适当的错误。如果此方法返回错误，则 SR-IOV 配置将被中止，不会创建任何 VF。

## 参见

[nv(9)](nv.9.md), [pci(9)](pci.9.md), [PCI_IOV_ADD_VF(9)](pci_iov_add_vf.9.md), [pci_iov_schema(9)](pci_iov_schema.9.md), [PCI_IOV_UNINIT(9)](pci_iov_uninit.9.md)

## 作者

本手册页由 Ryan Stone <rstone@FreeBSD.org> 编写。
