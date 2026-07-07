# linuxkpi_wlan(4)

`linuxkpi_wlan` — LinuxKPI 802.11 支持

## 名称

`linuxkpi_wlan`

## 描述

`linuxkpi_wlan` 内核模块提供一个 802.11 兼容层，用于在 Linux 802.11 驱动和原生 net80211 无线协议栈之间进行转换。目前支持基于 *mac80211* 的驱动。*cfg80211* 的部分功能已实现，但 net80211 中尚无代码来驱动它。

`linuxkpi_wlan` 目前支持以下 *wlanmode* 工作模式：

**`sta`** 基础设施 BSS（IBSS）中的客户端站点。

802.11n（HT）和 802.11ac（VHT）的兼容代码已实现，但由于不同驱动使用的 KPI 不同，支持程度可能因驱动而异。

硬件加速的加密支持需要通过 `compat.linuxkpi.80211.hw_crypto` 可调参数启用。支持的密码套件如下：

**`tkip`** 对 [wlan_tkip(4)](wlan_tkip.4.md) 的支持需通过 `compat.linuxkpi.80211.tkip` 可调参数手动启用。
**`ccmp`** 支持 [wlan_ccmp(4)](wlan_ccmp.4.md)。
**`gcmp`** 支持 [wlan_gcmp(4)](wlan_gcmp.4.md)。

当 [net80211(4)](net80211.4.md) 增加对更多密码套件的支持后，相应的支持也将随之实现。虽然实现 [wlan_wep(4)](wlan_wep.4.md) 支持是可行的，但考虑到 *Wired Equivalent Privacy（WEP）* 自 2004 年起已被弃用，决定不予实现。

支持的驱动列表包括 [iwlwifi(4)](iwlwifi.4.md)、[rtw88(4)](rtw88.4.md) 和 [rtw89(4)](rtw89.4.md)。

## SYSCTL 变量与加载器可调参数

`linuxkpi_wlan` 模块支持以下 [loader(8)](../man8/loader.8.md) 可调参数和只读 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`compat.linuxkpi.80211.hw_crypto`** 开启硬件加密卸载支持。默认为 `0`。

**`compat.linuxkpi.80211.tkip`** 开启 [wlan_tkip(4)](wlan_tkip.4.md) 卸载支持。默认为 `0`。

`linuxkpi_wlan` 模块支持以下 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`compat.linuxkpi.80211.debug`** 如果内核编译时启用了 `IEEE80211_DEBUG` 或手动启用了 `LINUXKPI_DEBUG_80211`，该 sysctl 是一个位掩码，用于开启各类调试消息。详情参见 `sys/compat/linuxkpi/common/src/linux_80211.h`。

**`compat.linuxkpi.80211.suspend_type`** 目前此变量用于启用/禁用挂起/恢复。默认值为 1，表示启用正常的挂起/恢复。设为 0 可禁用所有挂起/恢复。其他值将来可能启用特定功能。

**`compat.linuxkpi.80211.IF.dump_stas`** 打印指定已关联 [wlan(4)](wlan.4.md) 接口的统计信息；通常 IF 为 *wlan0*。

**`compat.linuxkpi.80211.IF.dump_stas_queues`** 类似于 `compat.linuxkpi.80211.IF.dump_stas`，但还会打印队列统计信息。此 sysctl 是“隐藏”的，通常仅用于调试目的。

## 参见

[iwlwifi(4)](iwlwifi.4.md), [linuxkpi(4)](linuxkpi.4.md), [rtw88(4)](rtw88.4.md), [rtw89(4)](rtw89.4.md), [wlan(4)](wlan.4.md)

## 历史

`linuxkpi_wlan` 模块首次出现于 FreeBSD 13.1。`linuxkpi_wlan` 对 IEEE 802.11n 和 802.11ac 的支持首次出现于 FreeBSD 14.3。

## 作者

LinuxKPI 802.11 支持由 Bjoern A. Zeeb 在 FreeBSD 基金会赞助下开发。
