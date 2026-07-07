# iwlwifi(4)

`iwlwifi` — Intel IEEE 802.11a/b/g/n/ac/ax/be 无线网络驱动

## 名称

`iwlwifi`

## 概要

`如果 devmatch(8) 已在 rc.conf(5) 中启用，该驱动将无需任何用户干预即可自动加载。`

`仅当自动加载被显式禁用时，才在 rc.conf(5) 中加入以下行，以在引导时手动以模块形式加载该驱动：`

```sh
kld_list="${kld_list} if_iwlwifi"
```

`该驱动会自动加载特定芯片组所需的任何 iwlwififw(4) 固件。有关如何安装固件，请参见下文的 Sx FILES 部分。`

`无法从 loader(8) 加载此驱动。`

## 描述

`iwlwifi` 驱动为 Intel 无线网络设备提供支持。

`iwlwifi` 派生自 Intel 的 Linux iwlwifi 驱动，基于 Linux 7.0 版本。[iwm(4)](iwm.4.md) 和 [iwx(4)](iwx.4.md) 驱动合起来大致等同于 Intel 的 Linux iwlwifi/mvm 驱动。

此外，`iwlwifi` 支持基于 Intel Linux iwlwifi/mld 驱动的芯片组。

`iwlwifi` 仍补充 [iwn(4)](iwn.4.md) 驱动，后者支持较旧的芯片组，相当于 Intel 的 Linux iwlwifi/dvm，而 `iwlwifi` 不支持此部分。

该驱动使用 [linuxkpi_wlan(4)](linuxkpi_wlan.4.md) 和 [linuxkpi(4)](linuxkpi.4.md) 兼容框架在 Linux 与原生 FreeBSD 驱动代码之间，以及与原生 [net80211(4)](net80211.4.md) 无线栈之间进行桥接。

## 硬件

`iwlwifi` 驱动支持来自 **mvm** 子驱动程序的以下芯片组世代的 PCIe 设备：

- 7000
- 8000
- 9000
- 22000
- AX210

`iwlwifi` 驱动支持来自 **mld** 子驱动程序的以下芯片组世代的 PCIe 设备：

- BZ
- SC

这些芯片组世代对应以下常见设备名称：

- Intel(R) Dual Band Wireless AC 7260
- Intel(R) Dual Band Wireless N 7260
- Intel(R) Wireless N 7260
- Intel(R) Dual Band Wireless AC 3160
- Intel(R) Wireless N 3160
- Intel(R) Dual Band Wireless N 3160
- Intel(R) Dual Band Wireless-AC 3165
- Intel(R) Dual Band Wireless-AC 3168
- Intel(R) Dual Band Wireless-AC 7265
- Intel(R) Dual Band Wireless-N 7265
- Intel(R) Wireless-N 7265
- Intel(R) Dual Band Wireless-AC 8260
- Intel(R) Dual Band Wireless-N 8260
- Intel(R) Dual Band Wireless-AC 4165
- Intel(R) Dual Band Wireless-AC 8265
- Intel(R) Dual Band Wireless-AC 8275
- Killer(R) Wireless-AC 1435i Wireless Network Adapter (8265D2W)
- Killer(R) Wireless-AC 1435-KIX Wireless Network Adapter (8265NGW)
- Intel(R) Wireless-AC 9461 160MHz
- Intel(R) Wireless-AC 9461
- Intel(R) Wireless-AC 9462 160MHz
- Intel(R) Wireless-AC 9462
- Intel(R) Wireless-AC 9260 160MHz
- Intel(R) Wireless-AC 9260
- Intel(R) Wireless-AC 9560 160MHz
- Intel(R) Wireless-AC 9560
- Intel(R) Wi-Fi 6 AX201 160MHz
- Intel(R) Wi-Fi 6 AX101
- Intel(R) Wi-Fi 6 AX203
- Intel(R) Wi-Fi 6 AX200 160MHz
- Intel(R) Wi-Fi 6E AX211 160MHz
- Intel(R) Wi-Fi 6E AX411 160MHz
- Intel(R) Wi-Fi 6E AX210 160MHz
- Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz
- Killer(R) Wireless-AC 1550s Wireless Network Adapter (9560D2W) 160MHz
- Killer(R) Wireless-AC 1550i Wireless Network Adapter (9560NGW) 160MHz
- Killer(R) Wi-Fi 6 AX1650s 160MHz Wireless Network Adapter (201D2W)
- Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW)
- Killer(R) Wi-Fi 6E AX1675s 160MHz Wireless Network Adapter (211D2W)
- Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW)
- Killer(R) Wi-Fi 6E AX1675w 160MHz Wireless Network Adapter (210D2W)
- Killer(R) Wi-Fi 6E AX1675x 160MHz Wireless Network Adapter (210NGW)
- Killer(R) Wi-Fi 6E AX1690s 160MHz Wireless Network Adapter (411D2W)
- Killer(R) Wi-Fi 6E AX1690i 160MHz Wireless Network Adapter (411NGW)
- Killer(R) Wi-Fi 6 AX1650w 160MHz Wireless Network Adapter (200D2W)
- Killer(R) Wi-Fi 6 AX1650x 160MHz Wireless Network Adapter (200NGW)
- Intel(R) Wi-Fi 7 BE201 320MHz
- Intel(R) Wi-Fi 7 BE401 320MHz
- Intel(R) Wi-Fi 7 BE200 320MHz
- Intel(R) Wi-Fi 7 BE202 160MHz
- Killer(R) Wi-Fi 7 BE1750s 320MHz Wireless Network Adapter (BE201D2W)
- Killer(R) Wi-Fi 7 BE1750i 320MHz Wireless Network Adapter (BE201NGW)
- Killer(R) Wi-Fi 7 BE1790s 320MHz Wireless Network Adapter (BE401D2W)
- Killer(R) Wi-Fi 7 BE1790i 320MHz Wireless Network Adapter (BE401NGW)
- Killer(TM) Wi-Fi 7 BE1750w 320MHz Wireless Network Adapter (BE200D2W)
- Killer(TM) Wi-Fi 7 BE1750x 320MHz Wireless Network Adapter (BE200NGW)
- Intel(R) Wi-Fi 7 BE211 320MHz
- Intel(R) Wi-Fi 6E AX221 160MHz
- Intel(R) Wi-Fi 7 BE213 160MHz
- Intel(R) Wi-Fi 8 BN201
- Intel(R) Wi-Fi 7 BE223
- Intel(R) Wi-Fi 8 BN203
- Killer(R) Wi-Fi 7 BE1775s 320MHz Wireless Network Adapter (BE211D2W)
- Killer(R) Wi-Fi 7 BE1775i 320MHz Wireless Network Adapter (BE211NGW)
- Killer(R) Wi-Fi 8 BN1850w2 320MHz Wireless Network Adapter (BN201.D2W)
- Killer(R) Wi-Fi 8 BN1850i 320MHz Wireless Network Adapter (BN201.NGW)

## 加载器可调参数

`iwlwifi` 驱动支持以下 [loader(8)](../man8/loader.8.md) 可调参数和只读 [sysctl(8)](../man8/sysctl.8.md) 变量：

**`compat.linuxkpi.iwlwifi_11n_disable`** 关闭驱动中的 802.11n 支持。默认为 `1`。

**`compat.linuxkPI.iwlwifi_disable_11ac`** 关闭驱动中的 802.11ac 支持。默认为 `1`。

这些可调参数的名称派生自 Linux iwlwifi 驱动模块参数，由 **linuxkpi** 自动映射。未作调整以保持与上游 Linux 一致，例如便于查阅文档和调查问题。这使得这些名称彼此之间以及与 FreeBSD 风格都不一致。

这些可调参数会由固件包为可启用 11n 和 11ac 的芯片组自动调整。如遇问题，用户可能希望在 **/boot/loader.conf.local** 中以默认值覆盖所提供的值。

## 文件

`iwlwifi` 驱动需要 `ports/net/wifi-firmware-iwlwifi-kmod` 中的固件。如果安装或运行时检测到相应硬件，此固件包将通过 fwget(8) 自动安装。

作为引导时的最后手段，可以手动下载单个固件文件，例如在另一台计算机上下载，然后通过 [umass(4)](umass.4.md) 设备传输。固件文件可从 Lk git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git 获取，文件名按驱动要求命名。副本应放置在 **/boot/firmware** 目录中。

## 参见

[iwlwififw(4)](iwlwififw.4.md), [iwm(4)](iwm.4.md), [iwn(4)](iwn.4.md), [iwx(4)](iwx.4.md), [linuxkpi(4)](linuxkpi.4.md), [linuxkpi_wlan(4)](linuxkpi_wlan.4.md), [wlan(4)](wlan.4.md), [networking(7)](../man7/networking.7.md), fwget(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`iwlwifi` 驱动最早出现于 FreeBSD 13.1。22000 及以后芯片组世代的 802.11n 和 802.11ac 支持最早出现于 FreeBSD 14.3。

## 缺陷

Lk <https://bugs.freebsd.org/bugzilla/showdependencytree.cgi?id=iwlwifi> iwlwifi 已知缺陷

虽然 `iwlwifi` 支持 802.11a/b/g/n/ac/ax/be 模式，但兼容代码当前仅支持 802.11a/b/g/n/ac 模式。802.11n/ac 仅在 22000 及以后芯片组世代上可用。802.11ax/be 和 6GHz 支持已计划。
