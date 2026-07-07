# puc(4)

`puc` — PCI“通用”通信驱动程序

## 名称

`puc` “通用”通信驱动程序

## 概要

`device pci device puc device uart device ppc`

## 描述

`puc` 驱动程序充当一个垫片，将 PCI 多端口串行和并行适配器连接到 [uart(4)](uart.4.md) 和 [ppc(4)](ppc.4.md) 驱动程序。

## 硬件

`puc` 驱动程序支持以下 PCI/PCIe 多端口串行和并行适配器：

- Instashield PCIe IX-400、IX-200、IX-100
- Instashield PCI IS-400、IS-200
- PX 系列 PCIe RS232/RS422/RS485/LPT
- UC 系列通用 PCI RS232/RS422/RS485/LPT
- UP 系列 PCI 双口 RS232

- XR17C/D152
- XR17C154
- XR17C158
- XR17V258IV
- XR17V352
- XR17V354
- XR17V358

- Tosca Console
- Tosca Secondary
- Maestro SP2
- Superdome Console
- Keystone SP2
- Everest SP2

- Dreadnought x16 Pro/Lite
- Ironclad x8 Pro
- Gunboat x4 Pro/Lite/Low Profile
- Gunboat x2 Low Profile

- Dual Serial PCI
- Quattro-PCIe
- Quattro-PCI
- Octopus-550 PCI

- Smartio CP-102E/PCIe
- Smartio CP-102EL/PCIe
- Smartio C104H/PCI
- Smartio CP-104UL/PCI
- Smartio CP-104JU/PCI
- Smartio CP-104EL/PCIe
- Smartio CP-104EL-A/PCIe
- CP-112UL PCI
- Industio CP-114
- Smartio CP-114EL/PCIe
- Smartio CP-118EL-A/PCIe
- C168H/PCI
- C168U/PCI
- CP-168EL/PCIe
- Smartio CP-168EL-A/PCIe

- OX16PCI952 UART（带并口和不带并口）
- OX16PCI954 UART
- OX9160/OX16PCI954 UART
- OX16PCI958 UART

- DSC-300/200/100 PCI
- DSCLP-300/200/100 PCI
- ESC-100/100D/100M PCI
- QSC-300/200/100 PCI
- QSCLP-100 PCI

- Cyber 2S 和 2SP1 PCI 16550
- Cyber 4 和 4S PCI 16C650（10x 系列和 20x 系列）
- Cyber I/O PCI（10x 系列和 20x 系列）
- Cyber Parallel Dual PCI（10x 系列和 20x 系列）
- Cyber Serial Dual PCI（10x 系列和 20x 系列）
- Cyber 2S1P PCI（10x 系列和 20x 系列）
- PS8000 8S PCI 16C650（20x 系列）
- Quartet Serial 850 PCI

- PCIex-800H
- PCI-200HV2
- 200Li uPCI
- PCI-800L、PCI-200L 和 PCI-100L
- PCI-800、PCI-400 和 PCI-200

- Advantech 2 端口 PCI PCI-1602/1603 Rev A/B1
- Applied Micro Circuits PCI 8 端口 UART
- Avlab Technology PCI IO 2S
- Avlab Low Profile PCI 4 Serial
- Boca Research PCI Turbo Serial 658/654
- Brainboxes：
- Comtrol RocketPort 550 PCI 16/8/4 端口
- Decision Computer PCCOM PCI 8/4/2 端口
- Digi Neo PCIe 4 和 8 端口（带和不带 RJ45）
- Digi Neo PCI 4 和 8 端口
- Dolphin Peripherals PCI 4035/4014
- Exar：
- Feasso PCI FPP-02 2S1P
- HP Diva Serial [GSP] 多端口 UART：
- I-O DATA RSA-PCI2/R
- IBM SurePOS 300 Series (481033H) 串口
- IC Book Labs：
- Kuroutoshikou SERIAL4P-LPPCI2
- Lava Computers：
- Moxa Technologies：
- NetMos NM9815 双 1284 打印端口 PCI
- NetMos NM9835 2/1 端口 UART + 1284 打印 PCI
- NetMos NM9845 4/6 端口 UART + 1284 打印 PCI
- NetMos NM9865 4/3/2 端口 UART + 1/2 端口 1284 打印 PCI
- 基于 Oxford Semiconductor 的板卡：
- Perle Ultraport4 Express PCIe 串口
- Perle Speed8/Speed4/Speed2 LE PCI 串口
- Quatech：
- SIIG Cyber 系列 UART 和并口板：
- Sun 1040 PCI 四串口
- Sunix MIO5xxxx 4/2/1 端口 UART 和 1284 打印机
- Sunix SUN1889/1888 PCI 双端口串口
- Sunix SER5xxxx 8/4/2 端口串口
- Syba Tech Ltd PCI-4S2P-550-ECP
- Systembase SB16C1054/8 4/8 端口串口
- Titan PCI-800H/PCI-200H
- VScom：

## 文件

**`sys/dev/puc/pucdata.c`** 受支持设备列表

## 参见

[ppc(4)](ppc.4.md), [uart(4)](uart.4.md)

## 历史

此驱动程序借鉴了 NetBSD `puc` 驱动程序的思想，并使用了大量相同的数据。
