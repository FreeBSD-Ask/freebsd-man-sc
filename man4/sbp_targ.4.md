# sbp_targ(4)

`sbp_targ` — Serial Bus Protocol 2 (SBP-2) 目标模式设备驱动

## 名称

`sbp_targ`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device sbp_targ
> device firewire
> device scbus
> device targ

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
firewire_load="YES"
cam_load="YES"
sbp_targ_load"YES"
```

## 描述

`sbp_targ` 驱动提供对 SBP-2 目标模式的支持。此驱动应与 cam(4)、[targ(4)](targ.4.md) 和 [firewire(4)](firewire.4.md) 一起工作。你还需要使用 scsi_target(8)，可在 **`/usr/share/examples/scsi_target`** 中找到，以提供实际设备。

## 实例

```sh
# mdconfig -a -t malloc -s 10m
md0
# scsi_target 0:0:0 /dev/md0
（假设 sbp_targ0 在 scbus0 上）
```

## 参见

cam(4), [firewire(4)](firewire.4.md), [targ(4)](targ.4.md), [camcontrol(8)](../man8/camcontrol.8.md), fwcontrol(8), [kldload(8)](../man8/kldload.8.md), scsi_target(8)

## 作者

`sbp_targ` 驱动由 Hidetoshi Shimokawa 编写。

## 缺陷

此驱动尚不可用。在多发起方环境中或总线拓扑更改后无法正确工作。
