# rgephy.4

`rgephy` — Realtek RTL8168/8169/8110/8211 系列 10/100/1000 千兆以太网 PHY 驱动

## 名称

`rgephy`

## 概要

`要将所有可用的 PHY 驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device miibus

`或者，要有选择地将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device mii
> device rgephy

## 描述

`rgephy` 驱动支持 Realtek RTL8168、RTL8169、RTL8110 和 RTL8211 系列集成 10/100/1000 千兆以太网 PHY。

要获取 `rgephy` 驱动某个特定实例所支持的介质类型和选项列表，请在其父 MAC 驱动的实例上运行 `ifconfig -m`。

此外，`rgephy` 驱动还支持以下特殊介质选项：

**`flag0`** 通过 [ifconfig(8)](../man8/ifconfig.8.md) 手动设置介质类型和选项时，`rgephy` 驱动默认还会触发一次通告所选介质的自动协商。这样做是为了在某些场景下绕过硬件问题。一般认为此行为总体上不会造成损害，但在边缘情况下确实可能产生不良影响。为了在手动设置介质类型和选项时不触发自动协商，`rgephy` 驱动允许通过 `flag0` 介质选项关闭此行为。

注意，即使设置了此特殊介质选项，它也不会出现在 [ifconfig(8)](../man8/ifconfig.8.md) 的输出中。

## 实例

手动设置 100BASE-TX 全双工，且不触发自动协商：

```sh
ifconfig re0 media 100baseTX mediaopt full-duplex,flag0
```

## 参见

[intro(4)](intro.4.md), [miibus(4)](miibus.4.md), [ifconfig(8)](../man8/ifconfig.8.md)
