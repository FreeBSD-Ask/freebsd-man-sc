# ath10k.4

`ath10k` — Qualcomm Atheros IEEE 802.11ac 无线网络驱动

## 名称

`ath10k`

## 概要

`如果 rc.conf(5) 中已启用 devmatch(8)，该驱动将自动加载，无需任何用户干预。`

`仅在显式禁用自动加载时，才在 rc.conf(5) 中加入以下行以在引导时手动以模块形式加载该驱动：`

```sh
kld_list="${kld_list} if_ath10k"
```

`不建议从 loader(8) 加载该驱动。`

## 描述

`ath10k` 驱动派生自 Qualcomm Atheros 的 Linux ath10k 驱动。

此驱动需要先加载固件才能工作。在加载驱动之前，需要安装来自 `ports/net/wifi-firmware-ath10k-kmod` port 的 `wifi-firmware-ath10k-kmod` 软件包。否则无法使用 [ifconfig(8)](../man8/ifconfig.8.md) 创建 [wlan(4)](wlan.4.md) 接口。该驱动使用 *linuxkpi_wlan* 和 *linuxkpi* 兼容框架在 Linux 和原生 FreeBSD 驱动代码之间以及与原生 [net80211(4)](net80211.4.md) 无线协议栈之间进行桥接。

虽然 `ath10k` 支持全部 802.11 a/b/g/n 和 ac，但兼容代码目前仅支持 802.11 a/b/g 模式。802.11 n/ac 支持即将推出。

## 硬件

`ath10k` 驱动支持具有以下芯片组的 PCIe 设备：

**QCA6174**

**QCA9377**

**QCA9887**

**QCA9888**

**QCA988X**

**QCA9984**

**QCA99X0**

## 参见

[wlan(4)](wlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`ath10k` 驱动首次出现于 FreeBSD 14.0。

## 缺陷

确实存在。
