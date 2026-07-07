# ntb_hw_amd(4)

`ntb_hw_amd` — AMD 非透明桥接驱动

## 名称

`ntb_hw_amd`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device ntb
> device ntb_hw_amd

`或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ntb_hw_amd_load="YES"
```

`此驱动支持以下 sysctl`

`读取此 sysctl 将给出基本信息，例如本地主机上 NTB 暴露的内存窗口、scratchpad 和 doorbell 数量，用于访问桥接另一端的设备。它还提供有关被屏蔽的 doorbell、每个暴露的内存窗口的转换地址和大小限制以及链路状态信息的详情。`

**dev.ntb_hw.X.info**

## 描述

`ntb_hw_amd` 驱动为 AMD EPYC 处理器系列中的非透明桥接（NTB）硬件提供支持。非透明桥接看起来不像普通 PCI 桥，而是作为 PCI 端点设备出现，隐藏其后的设备。该驱动隐藏另一端硬件的细节，但通过硬件无关的 KPI 向 [ntb(4)](ntb.4.md) 子系统暴露内存窗口、scratchpad 和 doorbell 以访问另一端。

硬件提供 2 个（均为 64 位）或 3 个（一个 32 位加两个 64 位）内存窗口访问另一系统的内存，最多 16 个 scratchpad 寄存器和 16 个 doorbell，分别用于与另一系统通信和中断。

## 配置

NTB 配置应由 BIOS 设置。这包括启用 NTB、选择拓扑（目前仅支持 NTB-to-Root Port 模式）以及主机在拓扑中的角色。这需要在两个系统上都进行设置。

内存窗口的 BAR 大小默认配置为 1 MiB。

## 参见

[if_ntb(4)](if_ntb.4.md), [ntb(4)](ntb.4.md), [ntb_transport(4)](ntb_transport.4.md)

## 作者

`ntb_hw_amd` 驱动由 AMD 开发，最初由 Rajesh Kumar <rajesh1.kumar@amd.com> 编写。由 Alexander Motin <mav@FreeBSD.org>、Conrad E. Meyer <cem@FreeBSD.org> 和 Warner Losh <imp@FreeBSD.org> 审阅。
