# PCI\_IOV\_UNINIT.9

`PCI_IOV_UNINIT` — 在 PF 设备上禁用 SR-IOV

## 名称

`PCI_IOV_UNINIT`

## 概要

```c
#include <sys/bus.h>
#include <dev/pci/pci_iov.h>

void
PCI_IOV_UNINIT(device_t dev)
```

## 描述

`PCI_IOV_UNINIT` 方法在用户请求在物理功能（PF）上禁用 SR-IOV 时由 PCI 单根 I/O 虚拟化（SR-IOV）基础设施调用。调用此方法时，PF 驱动程序必须释放其分配的所有与 SR-IOV 相关的资源，并禁用设备中任何设备特定的 SR-IOV 配置。

此方法仅会在成功调用 [PCI_IOV_INIT(9)](PCI_IOV_INIT.9.md) 之后被调用。不保证在调用 [PCI_IOV_INIT(9)](PCI_IOV_INIT.9.md) 之后和调用 `PCI_IOV_UNINIT` 之前，已对任何虚拟功能（VF）调用过 [PCI_IOV_ADD_VF(9)](PCI_IOV_ADD_VF.9.md)。

## 参见

[pci(9)](pci.9.md), [PCI_IOV_ADD_VF(9)](PCI_IOV_ADD_VF.9.md), [PCI_IOV_INIT(9)](PCI_IOV_INIT.9.md)

## 作者

本手册页由 Ryan Stone <rstone@FreeBSD.org> 编写。
