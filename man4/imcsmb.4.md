# imcsmb.4

`imcsmb` — Intel 集成内存控制器（iMC）SMBus 控制器驱动

## 名称

`imcsmb`

## 概要

`device pci device smbus device imcsmb`

或者，要在引导时以模块形式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
imcsmb_load="YES"
```

## 描述

`imcsmb` 驱动为内嵌于 Intel Sandybridge-Xeon、Ivybridge-Xeon、Haswell-Xeon 和 Broadwell-Xeon CPU 中的集成内存控制器（iMC）内的 SMBus 控制器功能提供 [smbus(4)](smbus.4.md) 支持。每颗 CPU 实现一个或多个 iMC，数量取决于核心数；每个 iMC 实现两个 SMBus 控制器（iMC-SMB）。iMC 在 POST 期间使用 iMC-SMB 从 DIMM 读取配置信息。它们也可被主板固件或 BMC 用于监测 DIMM 的温度。

iMC-SMB **并非**通用 SMBus 控制器。从其本质来说，它们只连接到 DIMM，因此仅实现与 DIMM 通信所需的 SMBus 操作。具体如下：

- READB
- READW
- WRITEB
- WRITEW

关于硬件和驱动程序架构的更详细讨论可参见 `sys/dev/imcsmb/imcsmb_pci.c` 的顶部注释。

## 警告

如上所述，固件可能使用 iMC-SMB 读取 DIMM 温度。公开的 iMC 文档并未描述任何协调机制，以防止来自不同来源的请求——例如主板固件、BMC 或操作系统——彼此干扰。

**因此，强烈建议开发者联系主板厂商，获取有关如何禁用和重新启用 DIMM 温度监测的板载专属说明。**

在从 `imcsmb_pci_request_bus` 返回之前，应当禁用 DIMM 温度监测；在从 `imcsmb_pci_release_bus` 返回之前，应当重新启用它。该驱动在相应位置包含了相应的注释。该驱动经过测试，仅需此类修改即可在某些 Intel 主板上正常工作。（遗憾的是，这些修改基于受保密协议保护的材料，因此未包含在此驱动中。）该驱动也经过测试，可在 SuperMicro 的多种主板上按原样正常工作。

[smb(4)](smb.4.md) 驱动会连接到由 `imcsmb` 创建的 [smbus(4)](smbus.4.md) 实例。然而，由于 iMC-SMB 并非通用 SMBus 控制器，不支持在这些 [smb(4)](smb.4.md) 设备上使用 smbmsg(8)。

## 参见

[jedec_dimm(4)](jedec_dimm.4.md), [smbus(4)](smbus.4.md)

## 历史

`imcsmb` 驱动首次出现于 FreeBSD 12.0。

## 作者

`imcsmb` 驱动最初由 Joe Kloss 为 Panasas 编写。随后由 Ravi Pokala <rpokala@freebsd.org> 进行了大量重构，并编写了本手册页。
