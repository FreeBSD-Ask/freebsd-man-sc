# axe.4

`axe` — ASIX Electronics AX88x7x/760 USB 以太网驱动

## 名称

`axe`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device ehci
> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device axe

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_axe_load="YES"
```

## 描述

`axe` 驱动为基于 ASIX Electronics AX88172、AX88178、AX88772、AX88772A、AX88772B 和 AX88760 USB 2.0 芯片组的 USB 以太网适配器提供支持。

AX88172、AX88772、AX88772A、AX88772B 和 AX88760 包含带 MII 接口的 10/100 以太网 MAC，设计用于与以太网和 HomePNA 收发器配合工作。AX88178 具有带 GMII/RGMII 接口的 10/100/1000 以太网 MAC，用于与千兆以太网 PHY 接口。

这些设备可与 USB 1.x 和 USB 2.0 控制器一起工作，但使用 1.x 控制器时性能受限，因为 USB 1.x 标准规定的最大传输速率为 12Mbps。因此使用 USB 1.x 控制器的用户不应期望这些设备实际达到 100Mbps 的速度。

所有芯片组都支持 64 位多播哈希表、用于站地址的单一完美过滤条目、全多播模式和混杂模式。数据包通过独立的 USB 批量传输端点接收和发送。

`axe` 驱动支持以下媒体类型：

**`autoselect`** 启用媒体类型和选项的自动选择。用户可通过在 [rc.conf(5)](../man5/rc.conf.5.md) 中添加媒体选项来手动覆盖自动选择的模式。

**`10baseT/UTP`** 设置 10Mbps 操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`100baseTX`** 设置 100Mbps（快速以太网）操作。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**`1000baseT`** 设置 1000Mbps（千兆以太网）操作（仅 AX88178）。也可使用 [ifconfig(8)](../man8/ifconfig.8.md) 的 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

`axe` 驱动支持以下媒体选项：

**`full-duplex`** 强制全双工操作。

**`half-duplex`** 强制半双工操作。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`axe` 驱动支持基于 ASIX Electronics AX88172/AX88178/AX88772/AX88772A/AX88772B/AX88760 的 USB 以太网适配器，包括：

AX88172：

- AboCom UF200
- Acer Communications EP1427X2
- ASIX AX88172
- ATen UC210T
- Billionton SnapPort
- Billionton USB2AR
- Buffalo（Melco Inc.）LUA-U2-KTX
- Corega USB2_TX
- D-Link DUBE100
- Goodway GWUSB2E
- JVC MP_PRX1
- LinkSys USB200M
- Netgear FA120
- Sitecom LN-029
- System TALKS Inc. SGC-X2UL

AX88178：

- ASIX AX88178
- Belkin F5D5055
- Logitec LAN-GTJ/U2A
- Buffalo（Melco Inc.）LUA3-U2-AGT
- Planex Communications GU1000T
- Sitecom Europe LN-028

AX88772：

- ASIX AX88772
- Buffalo（Melco Inc.）LUA3-U2-ATX
- D-Link DUBE100B1
- Planex UE-200TX-G
- Planex UE-200TX-G2

AX88772A：

- ASIX AX88772A
- Cisco-Linksys USB200Mv2

AX88772B：

- ASIX AX88772B
- Lenovo USB 2.0 Ethernet

AX88760：

- ASIX AX88760

## 诊断

- axe%d: watchdog timeout：数据包已排队等待发送且已发出发送命令，但设备在超时前未能确认传输。
- axe%d: no memory for rx list：驱动无法为接收环分配 mbuf。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [rgephy(4)](rgephy.4.md), [vlan(4)](vlan.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> “ASIX AX88x7x and AX88760 data sheets”。

## 历史

`axe` 设备驱动首次出现于 FreeBSD 5.0。

## 作者

`axe` 驱动由 Bill Paul <wpaul@windriver.com> 编写。
