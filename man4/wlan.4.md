# wlan(4)

`wlan` — 通用 WiFi 802.11 链路层支持

## 名称

`wlan`

## 概要

`device wlan`

## 描述

`wlan` 模块提供支持 802.11 驱动的通用代码。当设备不直接支持 802.11 功能时，由该层填补。所有原生 802.11 驱动都需要 `wlan` 模块。

`wlan` 支持可在 2.4GHz 和 5GHz 频段下工作的多模式设备，并支持众多 802.11 标准：802.11a、802.11b、802.11g、802.11n、802.11ac 和 802.11s（Draft 3.0）。WPA、802.11i 和 802.1x 安全协议通过内核代码和用户态应用程序的组合来支持。WME/WMM 多媒体协议完全在 `wlan` 模块内支持，但需要具有相应能力的硬件设备。同样，802.11h 规范仅由具有相应能力的设备支持。

驱动通过在运行时使用接口克隆创建的 `wlan` 接口提供 802.11 功能。这通过 [ifconfig(8)](../man8/ifconfig.8.md) `create` 命令或使用 [rc.conf(5)](../man5/rc.conf.5.md) 中的 `wlans_IFX` 变量完成。某些驱动支持创建共享同一底层设备的多个 `wlan` 接口；这是提供 ``multi-bss 支持'' 的方式，但也可用于创建 WDS 链路和其他有趣的应用。

可创建多种类型的 `wlan` 接口：

**`sta`** 基础设施 bss 中的客户端站点（即关联到接入点的站点）。

**`hostap`** 基础设施 bss 中的接入点。

**`mesh`** MBSS 网络中的 mesh 站点。

**`adhoc`** IBSS 网络中的站点。

**`ahdemo`** 以 ``adhoc demo 模式'' 工作的站点。这本质上是不使用管理帧的 IBSS 站点（例如不发送信标）。`ahdemo` 接口对于想要收发原始 802.11 数据包的应用程序特别有用。

**`monitor`** 专用于捕获 802.11 帧的接口。特别地，它被指定为具有只读属性，使其能在通常不被允许的频率上工作。

**`wds`** 为通过无线链路隧道传输流量而传递 4 地址 802.11 流量的站点。通常，此站点会与 `hostap` 接口共享同一 MAC 地址。可能在没有配套 `hostap` 接口的情况下创建 `wds` 接口，但这不保证；可能需要创建不发送信标帧的 `hostap` 接口才能创建 `wds` 接口。

注意，接口的类型在创建后无法更改。

`wlan` 定义了若干机制，通过插件模块扩展其功能。诸如 WEP、TKIP 和 AES-CCMP 等加密支持作为独立模块实现（如果未静态配置到系统中），向 `wlan` 注册。类似地，有一个用于定义 802.11 认证服务的认证器框架，以及一个用于集成特定于 802.11 协议的访问控制机制的框架。

## 调试

如果内核配置中包含 `IEEE80211_DEBUG` 选项，可使用以下命令进行调试控制：

```sh
sysctl net.wlan.X.debug=mask
```

其中 `X` 是 `wlan` 实例的编号，mask 是控制位的按位或，用于确定要启用哪些调试消息。例如，

```sh
sysctl net.wlan.0.debug=0x00200000
```

启用与扫描接入点、adhoc 邻居或作为接入点操作时未占用信道相关的调试消息。wlandebug(8) 工具提供了更友好的用户机制来完成同样的操作。注意，

```sh
sysctl net.wlan.debug=mask
```

定义每个克隆的 `wlan` 接口的调试标志初始值；这对于在接口创建期间启用调试消息很有用。

## 兼容性

`wlan` 的模块名用于与 NetBSD 兼容。

Mesh 站点遵循 802.11s Draft 3.0 规范，该规范尚未批准，可能会有变化。请注意，此规范与早期草案不兼容。实现早期草案的站点（例如 Linux）可能不兼容。

## 参见

[ath(4)](ath.4.md), [bwi(4)](bwi.4.md), [bwn(4)](bwn.4.md), [ipw(4)](ipw.4.md), [iwi(4)](iwi.4.md), [iwlwifi(4)](iwlwifi.4.md), [iwm(4)](iwm.4.md), [iwn(4)](iwn.4.md), [iwx(4)](iwx.4.md), [malo(4)](malo.4.md), [mwl(4)](mwl.4.md), [netintro(4)](netintro.4.md), [otus(4)](otus.4.md), [ral(4)](ral.4.md), [rsu(4)](rsu.4.md), [rtw88(4)](rtw88.4.md), [rtw89(4)](rtw89.4.md), [rtwn(4)](rtwn.4.md), [rum(4)](rum.4.md), [run(4)](run.4.md), [uath(4)](uath.4.md), [upgt(4)](upgt.4.md), [ural(4)](ural.4.md), [urtw(4)](urtw.4.md), [wlan_acl(4)](wlan_acl.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_gcmp(4)](wlan_gcmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), [wpi(4)](wpi.4.md), [zyd(4)](zyd.4.md)

## 标准

更多信息可在 IEEE 802.11 标准中找到。

## 历史

`wlan` 驱动最早出现在 FreeBSD 5.0 中。

## 作者

Atsushi Onoe 是最初 NetBSD 软件的作者，本项目即从该软件开始。Sam Leffler 将代码引入 FreeBSD，然后重写以支持多模式设备、802.11g、802.11n、WPA/802.11i、WME、multi-bss，并添加了加密、认证和访问控制插件的可扩展框架。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 编写。
