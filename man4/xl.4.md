# xl.4

`xl` — 3Com Etherlink XL 和 Fast Etherlink XL 以太网设备驱动

## 名称

`xl`

## 概要

`要将此驱动编译进内核，请将以下行放入你的内核配置文件：`

> device miibus
> device xl

`或者，要在引导时以模块形式加载驱动，请将以下行放入 loader.conf(5)：`

```sh
if_xl_load="YES"
```

## 描述

`xl` 驱动为基于 3Com “boomerang”、“cyclone”、“hurricane”和“tornado”总线主控 Etherlink XL 芯片的 PCI 以太网适配器和嵌入式控制器提供支持。

Etherlink XL 芯片支持内置的 10baseT、10base2 和 10base5 收发器，以及用于外接 PHY 收发器的 MII 总线。3c905 系列通常使用 National Semiconductor NS 83840A 10/100 PHY，在全双工或半双工下支持 10/100 Mbps。3c905B 适配器具有内置的自动协商逻辑，映射到 MII 上以与先前的驱动兼容。Fast Etherlink XL 适配器（如 3c905-TX 和 3c905B-TX）能够以全双工或半双工模式进行 10 或 100Mbps 数据速率，可以手动配置为任何支持的模式，或与链路伙伴自动协商尽可能高的模式。

`xl` 驱动支持以下媒体类型：

**autoselect** 启用媒体类型和选项的自动选择。注意此选项仅适用于带有外部 PHY 或内置自动协商逻辑的 3c905 和 3c905B 适配器。对于 3c900 适配器，驱动将选择 EEPROM 中指定的模式。用户可以通过在 **`/etc/rc.conf`** 文件中添加媒体选项来更改此设置。

**10baseT/UTP** 设置 10Mbps 操作。还可以使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**100baseTX** 设置 100Mbps（快速以太网）操作。还可以使用 `mediaopt` 选项选择 `full-duplex` 或 `half-duplex` 模式。

**10base5/AUI** 启用 AUI 收发器（仅在 COMBO 卡上可用）。

**10base2/BNC** 启用 BNC 同轴收发器（仅在 COMBO 卡上可用）。

`xl` 驱动支持以下媒体选项：

**full-duplex** 强制全双工操作。

**half-duplex** 强制半双工操作。

注意，100baseTX 媒体类型仅在适配器支持时可用。有关配置此设备的更多信息，请参见 [ifconfig(8)](../man8/ifconfig.8.md)。

## 硬件

`xl` 驱动支持以下硬件：

- 3Com 3c900-TPO
- 3Com 3c900-COMBO
- 3Com 3c905-TX
- 3Com 3c905-T4
- 3Com 3c900B-TPO
- 3Com 3c900B-TPC
- 3Com 3c900B-FL
- 3Com 3c900B-COMBO
- 3Com 3c905B-T4
- 3Com 3c905B-TX
- 3Com 3c905B-FX
- 3Com 3c905B-COMBO
- 3Com 3c905C-TX
- 3Com 3c980、3c980B 和 3c980C 服务器适配器
- 3Com 3cSOHO100-TX OfficeConnect 适配器
- 3Com 3c450 HomeConnect 适配器
- 3Com 3c555、3c556 和 3c556B mini-PCI 适配器
- 3Com 3C3SH573BT、3C575TX、3CCFE575BT、3CXFE575BT、3CCFE575CT、3CXFE575CT、3CCFEM656、3CCFEM656B 和 3CCFEM656C、3CXFEM656、3CXFEM656B 和 3CXFEM656C CardBus 适配器
- 3Com 3c905-TX、3c905B-TX 3c905C-TX、3c920B-EMB 和 3c920B-EMB-WNM 嵌入式适配器

3C656 系列 CardBus 卡和 3C556 系列 MiniPCI 卡都具有内置的专用调制解调器。`xl` 驱动和其他 FreeBSD 驱动均不支持此调制解调器。

## 诊断

- xl%d: couldn't map memory 发生了致命的初始化错误。
- xl%d: couldn't map interrupt 发生了致命的初始化错误。
- xl%d: device timeout 设备已停止响应网络，或网络连接（电缆）存在问题。
- xl%d: no memory for rx list 驱动未能为接收环分配 mbuf。
- xl%d: no memory for tx list 驱动在分配填充缓冲区或将 mbuf 链折叠到集群中时，未能为发送环分配 mbuf。
- xl%d: command never completed! 向 3c90x ASIC 发出的某些命令需要时间完成：驱动应在继续之前等待状态寄存器中的“command in progress”位清除。在极少数情况下，此位可能不会清除。为避免陷入无限等待循环，驱动只会在放弃之前轮询该位有限次数，此时发出此消息。在较慢的机器上，驱动初始化期间可能会打印此消息。如果你看到此消息但驱动继续正常工作，则可能可以忽略此消息。
- xl%d: chip is in D3 power state -- setting to D0 此消息仅适用于支持电源管理的 3c905B 适配器。某些操作系统在关闭时将 3c905B 置于低功率模式，而某些 PCI BIOS 在配置之前未能将芯片从此状态中唤醒。3c905B 在 D3 状态下会丢失其所有 PCI 配置，因此如果 BIOS 未及时将其设置回全功率模式，将无法正确配置。驱动尝试检测此情况并将适配器恢复到 D0（全功率）状态，但这可能不足以使驱动恢复到完全可操作的状态。如果你在引导时看到此消息且驱动未能将设备附加为网络接口，则需要执行第二次热启动以正确配置设备。注意，此情况仅在从其他操作系统热启动时发生。如果在引导 FreeBSD 之前关闭系统电源，则应正确配置卡。
- xl%d: WARNING: no media options bits set in the media options register! 在某些带有内置 3c905-TX 适配器的 Dell Latitude 扩展坞上使用驱动时，可能会出现此警告。无论出于何种原因，此特定设备上媒体选项寄存器中的“MII available”位未设置，尽管它应该被设置（3c905-TX 总是使用外部 PHY 收发器）。驱动将尝试根据 PCI 设备 ID 字猜测正确的媒体类型。驱动对此情况发出大量噪音，因为作者认为这是制造缺陷。
- xl%d: transmission error: %d
- xl%d: tx underrun, increasing tx start threshold to %d bytes 此消息可能在适配器在各种负载下调整其发送缓冲区时出现，基本无害。忽略它们可能是安全的。

## 参见

[altq(4)](altq.4.md), arp(4), [cardbus(4)](cardbus.4.md), [miibus(4)](miibus.4.md), [netintro(4)](netintro.4.md), [ng_ether(4)](ng_ether.4.md), [polling(4)](polling.4.md), [ifconfig(8)](../man8/ifconfig.8.md)

## 历史

`xl` 设备驱动首次出现于 FreeBSD 3.0。

## 作者

`xl` 驱动由 Bill Paul <wpaul@ctr.columbia.edu> 编写。
