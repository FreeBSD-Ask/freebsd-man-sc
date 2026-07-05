# rtw89.4

`rtw89` — Realtek IEEE 802.11ax 无线网络驱动

## 名称

`rtw89`

## 概要

`如果已在 rc.conf(5) 中启用 devmatch(8)，驱动将自动加载，无需任何用户交互。`

`仅在显式禁用自动加载时，才需要在 rc.conf(5) 中加入以下行以在引导时手动加载驱动模块：`

```sh
kld_list="${kld_list} if_rtw89"
```

`无法从 loader(8) 加载此驱动。`

## 描述

`rtw89` 驱动源自 Realtek 的 Linux rtw89 驱动，基于 Linux 7.0 版本。

此驱动需要先加载固件才能工作。在加载驱动之前，需要安装来自 `ports/net/wifi-firmware-rtw89-kmod` port 的 `wifi-firmware-rtw89-kmod` 软件包。否则无法使用 [ifconfig(8)](../man8/ifconfig.8.md) 创建 [wlan(4)](wlan.4.md) 接口。可使用 fwget(8) 安装正确的固件包。

驱动使用 [linuxkpi_wlan(4)](linuxkpi_wlan.4.md) 和 [linuxkpi(4)](linuxkpi.4.md) 兼容框架在 Linux 与原生 FreeBSD 驱动代码之间，以及与原生 [net80211(4)](net80211.4.md) 无线协议栈之间进行桥接。

## 硬件

`rtw89` 驱动支持具有以下芯片组的 PCIe 设备：

- Realtek 8851BE Wi-Fi 6 (RTL8851BE)
- Realtek 8852AE Wi-Fi 6 (RTL8852AE)
- Realtek 8852BE Wi-Fi 6 (RTL8852BE)
- Realtek 8852BTE Wi-Fi 6 (RTL8852BE-VT)
- Realtek 8852CE Wi-Fi 6E (RTL8852CE)
- Realtek 8922AE Wi-Fi 7 (RTL8922AE)

## 加载器可调参数

**`compat.linuxkpi.skb.mem_limit`** 如果你运行的是主存超过 4GB 的 64 位系统，需要在 loader.conf(5) 中将此可调参数设置为 **1** 并重启一次以使其生效。此可调参数可解决 DMA 相关问题，将网络缓冲区内存的分配限制在物理内存的低 32 位区域，使驱动正常工作。

## 参见

[linuxkpi(4)](linuxkpi.4.md), [linuxkpi_wlan(4)](linuxkpi_wlan.4.md), [wlan(4)](wlan.4.md), [networking(7)](../man7/networking.7.md), fwget(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`rtw89` 驱动最早出现在 FreeBSD 14.2 中。

## 缺陷

确实如此。

在主存超过 4GB 的机器上似乎（可靠地）无法工作。参见上文加载器可调参数一节。

我们观察到在当前的芯片组上，至少在与 [linuxkpi_wlan(4)](linuxkpi_wlan.4.md) 结合使用时，存在各种稳定性问题，导致驱动崩溃和内核 panic。

虽然 `rtw89` 支持 802.11a/b/g/n/ac/ax 模式，但兼容代码目前仅支持 802.11a/b/g 模式。802.11n/ac/ax 的支持尚待实现。
