# aue(4)

`aue` — ADMtek AN986 Pegasus USB 快速以太网驱动

## 名称

`aue`

## 概要

要将此驱动编译进内核，请将以下行放入内核配置文件中：

> device uhci
> device ohci
> device usb
> device miibus
> device uether
> device aue

或者，要在引导时以模块形式加载该驱动，请在 [loader.conf(5)](../man5/loader.conf.5.md) 中加入以下行：

```sh
if_aue_load="YES"
```

## 描述

`aue` 驱动为基于 ADMtek AN986 Pegasus 芯片组的 USB 快速以太网适配器提供支持。

包含 AN986 Pegasus 芯片组的 LinkSys USB10T 适配器将以 100Base-TX 和全双工模式运行。

Pegasus 包含带 MII 接口的 10/100 以太网 MAC，设计用于与以太网和 HomePNA 收发器配合工作。虽然设计用于与 100Mbps 外设接口，但现有 USB 标准规定的最大传输速率为 12Mbps。因此用户不应期望这些设备实际达到 100Mbps 的速度。

Pegasus 支持 64 位多播哈希表、用于站地址的单一完美过滤条目和混杂模式。数据包通过独立的 USB 批量传输端点接收和发送。

`aue` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择。用户可通过在 **/etc/rc.conf** 文件中添加媒体选项来手动覆盖自动选择的模式。

**10baseT/UTP** 设置 10Mbps 操作。也可使用 `mediaopt` 选项启用 `full-duplex` 操作。未指定 `full duplex` 意味着 `half-duplex` 模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。也可使用 `mediaopt` 选项启用 `full-duplex` 操作。未指定 `full duplex` 意味着 `half-duplex` 模式。

`aue` 驱动支持以下媒体选项：

**full-duplex** 强制全双工操作。如果未指定此媒体选项，接口将以半双工模式运行。

有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`aue` 驱动支持以下基于 ADMtek AN986 Pegasus 芯片组的 USB 快速以太网适配器：

- Abocom UFE1000、DSB650TX_NA
- Accton USB320-EC、SpeedStream
- ADMtek AN986、AN8511
- Billionton USB100、USB100LP、USB100EL、USBE100
- Corega Ether FEther USB-T、FEther USB-TX、FEther USB-TXS
- D-Link DSB-650、DSB-650TX、DSB-650TX-PNA
- Elecom LD-USBL/TX
- Elsa Microlink USB2Ethernet
- HP hn210e
- I-O Data USB ETTX
- Kingston KNU101TX
- LinkSys USB10T adapters that contain the AN986 Pegasus chipset、USB10TA、USB10TX、USB100TX、USB100H1
- MELCO LUA-TX、LUA2-TX
- Netgear FA101
- Planex UE-200TX
- Sandberg USB to Network Link（型号 133-06）
- Siemens Speedstream
- SmartBridges smartNIC
- SMC 2202USB
- SOHOware NUB100

## 诊断

- aue%d: watchdog timeout：数据包已排队等待发送且已发出发送命令，但设备在超时前未能确认传输。
- aue%d: no memory for rx list：驱动无法为接收环分配 mbuf。

## 参见

[altq(4)](altq.4.md), arp(4), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

> “ADMtek AN986 data sheet”。

## 历史

`aue` 设备驱动首次出现于 FreeBSD 4.0。

## 作者

`aue` 驱动由 Bill Paul <wpaul@ee.columbia.edu> 编写。
