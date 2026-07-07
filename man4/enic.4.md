# enic(4)

`enic` — VIC 以太网 NIC 驱动

## 名称

`enic`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device iflib
> device enic

`若要在运行时以模块形式加载此驱动，请以 root 身份运行以下命令：`

```sh
kldload if_enic
```

`若要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
if_enic_load="YES"
```

## 描述

`enic` 驱动为 Cisco 虚拟接口卡（Virtual Interface Card）提供支持。支持仅限于基本网络连接。媒体由 NIC 自身控制，因为可能向 PCI 总线暴露多个虚拟 PCI NIC 设备。

## 硬件

`enic` 驱动应支持所有已知的 Cisco VIC 卡。

## 配置

`enic` 网络接口使用 [ifconfig(8)](../man8/ifconfig.8.md) 和位于 `dev.enic.<N>` 的 [sysctl(8)](../man8/sysctl.8.md) 树进行配置。所有可配置条目同时也是可调参数，可直接放入 loader.conf(5) 以实现持久配置。

## 参见

[ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`enic` 设备驱动首次出现于 FreeBSD 14.0。

## 作者

`enic` 驱动由 Cisco UCS 团队基于 DPDK 驱动编写。
