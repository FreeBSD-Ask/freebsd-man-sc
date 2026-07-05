# vmx.4

`vmx` — VMware VMXNET3 虚拟接口控制器设备

## 名称

`vmx`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device iflib
> device vmx

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_vmx_load="YES"
```

## 描述

`vmx` 驱动为 VMware 虚拟机中可用的 VMXNET3 虚拟网卡提供支持。它表现为一个简单的以太网设备，但实际上是底层主机操作系统的虚拟网络接口。

此驱动支持 `VMXNET3` 驱动协议，作为 VMware 环境中也可用的模拟 le(4)、[em(4)](em.4.md) 接口的替代方案。`vmx` 驱动针对虚拟机进行了优化，可根据底层主机操作系统和主机的物理网络接口控制器提供高级功能。`vmx` 驱动支持多队列、IPv6 校验和卸载、MSI/MSI-X 支持以及 VMware 的 VLAN 客户机打标签（VGT）模式下的硬件 VLAN 打标签等功能。

`vmx` 驱动支持由以下产品提供的虚拟机硬件版本 7 或更高版本的 VMXNET3 VMware 虚拟网卡：

- VMware ESX/ESXi 4.0 及更高版本
- VMware Server 2.0 及更高版本
- VMware Workstation 6.5 及更高版本
- VMware Fusion 2.0 及更高版本

有关配置此设备的更多信息，参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 多队列

`vmx` 驱动支持多个发送和接收队列。多队列仅由某些 VMware 产品（如 ESXi）支持。分配的队列数取决于 MSI-X 的存在、已配置的 CPU 数量以及下面列出的可调参数。FreeBSD 默认不在 VMware 上启用 MSI-X 支持。必须禁用 `hw.pci.honor_msi_blacklist` 可调参数才能启用 MSI-X 支持。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.vmx.txnqueue`**

**`hw.vmx.`** `X``.txnqueue` 驱动默认分配的最大发送队列数。默认值为 8。VMXNET3 虚拟网卡支持的最大值为 8。

**`hw.vmx.rxnqueue`**

**`hw.vmx.`** `X``.rxnqueue` 驱动默认分配的最大接收队列数。默认值为 8。VMXNET3 虚拟网卡支持的最大值为 16。

**`hw.vmx.txndesc`**

**`hw.vmx.`** `X``.txndesc` 驱动分配的发送描述符数。默认值为 512。该值必须是 32 的倍数，最大为 4096。

**`hw.vmx.rxndesc`**

**`hw.vmx.`** `X``.rxndesc` 驱动为每个环分配的接收描述符数。默认值为 256。该值必须是 32 的倍数，最大为 2048。有两个环，因此实际使用量翻倍。

## 实例

必须在 VMware 配置文件中添加以下条目以提供 `vmx` 设备：

```sh
ethernet0.virtualDev = "vmxnet3"
```

## 参见

[altq(4)](altq.4.md), arp(4), [em(4)](em.4.md), [iflib(4)](iflib.4.md), le(4), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 作者

`vmx` 驱动从 OpenBSD 移植并由 Bryan Venteicher <bryanv@freebsd.org> 大幅重写。OpenBSD 驱动由 Tsubai Masanari 编写。
