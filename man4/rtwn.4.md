# rtwn(4)

`rtwn` — Realtek IEEE 802.11n/ac 无线网络驱动

## 名称

`rtwn`

## 概要

`options RTWN_DEBUG options RTWN_WITHOUT_UCODE`

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device rtwn
> device rtwnfw
> device rtwn_usb
> device rtwn_pci
> device wlan
> device firmware

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
if_rtwn_pci_load="YES"
if_rtwn_usb_load="YES"
```

## 描述

`rtwn` 驱动为 [rtwn_pci(4)](rtwn_pci.4.md) 和 [rtwn_usb(4)](rtwn_usb.4.md) 提供的 802.11n/ac 无线网络 PHY 提供支持。

`rtwn` 驱动支持 `station`、`adhoc`、`hostap` 和 `monitor` 模式操作。`monitor` 模式虚拟接口数量没有限制；除任意其他虚拟接口外，还可添加一个 `station` 接口（注：RTL8821AU 同时支持两个非 monitor 模式接口）。

所有芯片均有硬件支持 WEP、AES-CCM 和 TKIP 加密。

`rtwn` 驱动可在运行时通过 [ifconfig(8)](../man8/ifconfig.8.md) 进行配置。

## 硬件

`rtwn` 驱动支持具有以下芯片组的 USB 和 PCI 设备：

- Realtek 802.11n wireless 8188e (RTL8188E)
- Realtek 802.11n wireless 8192c (RTL8192C)
- Realtek 802.11n wireless 8192e (RTL8192E)
- Realtek 802.11ac wireless 8812a (RTL8812A)
- Realtek 802.11ac wireless 8821a (RTL8821A)

具体设备参见 [rtwn_pci(4)](rtwn_pci.4.md) 和 [rtwn_usb(4)](rtwn_usb.4.md)。

## 文件

**`/usr/share/doc/legal/realtek.LICENSE`** `rtwn` 固件许可证

驱动（若未使用 `options RTWN_WITHOUT_UCODE` 编译）可能使用以下固件文件，这些文件在接口启用时加载：

**`/boot/kernel/rtwn-rtl8188eefw.ko`**
**`/boot/kernel/rtwn-rtl8188eufw.ko`**
**`/boot/kernel/rtwn-rtl8192cfwE_B.ko`**
**`/boot/kernel/rtwn-rtl8192cfwE.ko`**
**`/boot/kernel/rtwn-rtl8192cfwT.ko`**
**`/boot/kernel/rtwn-rtl8192cfwU.ko`**
**`/boot/kernel/rtwn-rtl8192eufw.ko`**
**`/boot/kernel/rtwn-rtl8812aufw.ko`**
**`/boot/kernel/rtwn-rtl8821aufw.ko`**

## 实例

加入现有的 BSS 网络（即连接到接入点）：

```sh
ifconfig wlan create wlandev rtwn0 inet 192.0.2.20/24
```

加入网络名为 `my_net` 的特定 BSS 网络：

```sh
ifconfig wlan create wlandev rtwn0 ssid my_net up
```

加入使用 64 位 WEP 加密的特定 BSS 网络：

```sh
ifconfig wlan create wlandev rtwn0 ssid my_net e
    wepmode on wepkey 0x1234567890 weptxkey 1 up
```

在通道 4 上创建使用 128 位 WEP 加密的 IBSS 网络：

```sh
ifconfig wlan create wlandev rtwn0 wlanmode adhoc ssid my_net e
    wepmode on wepkey 0x01020304050607080910111213 weptxkey 1 e
    channel 4
```

加入/创建网络名为 `my_net` 的 802.11b IBSS 网络：

```sh
ifconfig wlan0 create wlandev rtwn0 wlanmode adhoc
ifconfig wlan0 inet 192.0.2.20/24 ssid my_net mode 11b
```

创建基于主机的接入点：

```sh
ifconfig wlan0 create wlandev rtwn0 wlanmode hostap
ifconfig wlan0 inet 192.0.2.20/24 ssid my_ap
```

## 加载器可调参数

可在引导内核前在 [loader(8)](../man8/loader.8.md) 提示符下设置可调参数，或存储在 loader.conf(5) 中。

**`dev.rtwn.%d.hwcrypto`** 此可调参数控制密钥槽的分配方式：0 - 禁用硬件加密支持。需要访问帧内容的功能（如 TCP/UDP/IP Rx 校验验证）将无法工作；1 - 仅对成对密钥使用硬件加密支持；2 - 对所有密钥使用硬件加密支持；在多 vap 配置下可能无法工作。默认值为 1。

**`dev.rtwn.%d.ratectl`** 此可调参数在速率控制实现之间切换：0 - 无速率控制；1 - 驱动向 net80211 发送“tx complete”报告；算法由 net80211 控制；2 - 基于固件的速率控制。默认值为 1；但驱动可在该算法未实现时选择其他算法。当前选定的算法通过只读 OID `dev.rtwn.%d.ratectl_selected` 报告。

**`dev.rtwn.%d.rx_buf_size`** （仅 USB）控制临时 Rx 缓冲区大小；较小的缓冲区大小可能增加中断次数。

## 诊断

- rtwn%d: could not read efuse byte at address 0x%x
- rtwn%d: %s: cannot read rom, error %d 读取 ROM 时发生错误；设备附加将被中止。这不应发生。
- rtwn%d: failed loadfirmware of file %s 由于某种原因，驱动无法从文件系统读取微代码文件。文件可能缺失或损坏。驱动将禁用依赖固件的功能。
- rtwn%d: wrong firmware size (%zu)
- rtwn%d: %s: failed to upload firmware %s (error %d)
- rtwn%d: timeout waiting for firmware readiness 固件上传失败；文件可能已损坏。驱动将禁用依赖固件的功能。这不应发生。
- rtwn%d: device timeout 派发到硬件进行发送的帧未能在时间内完成。驱动将重置硬件。这不应发生。

## 参见

[intro(4)](intro.4.md), [netintro(4)](netintro.4.md), [rtwn_pci(4)](rtwn_pci.4.md), [rtwn_usb(4)](rtwn_usb.4.md), [rtwnfw(4)](rtwnfw.4.md), [wlan(4)](wlan.4.md), [wlan_amrr(4)](wlan_amrr.4.md), [wlan_ccmp(4)](wlan_ccmp.4.md), [wlan_tkip(4)](wlan_tkip.4.md), [wlan_wep(4)](wlan_wep.4.md), [wlan_xauth(4)](wlan_xauth.4.md), [networking(7)](../man7/networking.7.md), hostapd(8), [ifconfig(8)](../man8/ifconfig.8.md), wpa_supplicant(8)

## 历史

`urtwn` 驱动最早出现于 OpenBSD 4.9 和 FreeBSD 10.0；`rtwn` 驱动最早出现于 OpenBSD 5.8 和 FreeBSD 11.0。

## 作者

`rtwn` 驱动最初由 Stefan Sperling <stsp@openbsd.org> 编写，并由 Kevin Lo <kevlo@freebsd.org> 移植。它基于由 Damien Bergamini <damien.bergamini@free.fr> 编写的 `urtwn` 驱动。

## 缺陷

`rtwn` 驱动目前未实现基于固件的速率控制。
