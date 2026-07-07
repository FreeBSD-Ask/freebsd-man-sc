# udbc(4)

`udbc` — USB 调试类设备驱动

## 名称

`udbc`

## 概要

`device usb device ucom device udbc`

`在 rc.conf(5) 中：kld_list="udbc"`

## 描述

`udbc` 驱动提供对接口类为诊断类、子类为 DbC.GP 的 USB 调试类设备的支持。

USB 调试类在 USB 3.1 调试设备设备类规范中定义。这旨在为调试提供通用通信通道。它也广泛实现于 USB xHC（USB eXtensible 主机控制器）中，作为可选功能，可在许多普通计算机上找到。在 USB xHC 上启用此功能后，当连接 USB 调试电缆时，其中一个 USB 端口将表现为 USB 调试类设备而非主机端口。USB xHC 中支持的类通常是 DbC.GP，而规范定义了多种类型的调试类设备。DbC.GP 使用 IN 和 OUT 端点对，实现单一双向串行通信通道。在大多数系统（包括 FreeBSD）上，DbC.GP 被视为简单的串行设备。

大多数具有 USB xHC 的系统都可配置为提供 DbC.GP 访问。`udbc` 是连接到支持 DbC.GP 的设备的驱动，通过 [ucom(4)](ucom.4.md) 设备驱动提供 [tty(4)](tty.4.md) 设备以连接它们。

## 硬件配置

原生的 DbC.GP 设备可以以直接方式通过 `udbc` 驱动附着。

目标系统上的 USB xHC DbC.GP 设备需要特殊硬件配置，因为所有端口都假定是 USB 主机。暴露 DbC.GP 的一种方法是使用 USB 3.1 A-to-A 电缆（USB 3.1 传统电缆和连接器规范第 5.5.2 节）。当此电缆连接到目标系统的 USB 3.1 端口时，启用 DbC 的 USB xHC 会自动将该端口切换为 USB 设备。`udbc` 驱动可在该端口上找到 DbC.GP 设备。

注意，支持 USB 3.2（USB Type-C 连接器）的 USB xHC 与 USB 3.1 A-to-A 电缆不兼容。连接 USB 3.2 C-to-C 电缆或 A-to-C 电缆也不会自动工作，因为它需要端口的角色配置，而 FreeBSD 尚不支持。

## 文件

**`/dev/ttyU*.*`** 用于呼入端口
**`/dev/ttyU*.*.init`**
**`/dev/ttyU*.*.lock`** 相应的呼入初始状态和锁定状态设备
**`/dev/cuaU*.*`** 用于呼出端口
**`/dev/cuaU*.*.init`**
**`/dev/cuaU*.*.lock`** 相应的呼入初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md), [xhci(4)](xhci.4.md)

## 标准

> "eXtensible Host Controller Interface for Universal Serial Bus (XHCI)".

> "USB 3.1 Device Class Specification for Debug Devices".

> "USB 3.1 Legacy Cable and Connector Specification".

## 历史

`udbc` 驱动首次出现于 FreeBSD 15.0。

## 作者

`udbc` 驱动由 Hiroki Sato <hrs@FreeBSD.org> 编写。

## 缺陷

根据 XHCI 规范，USB 调试的主机端应能与任何 USB 3.0 端口配合工作，无论是直接连接到控制器还是中间有集线器。在某些控制器上测试时，使用集线器而非控制器上直接连接的端口时遇到了问题。
