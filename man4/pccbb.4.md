# pccbb(4)

`pccbb` — CardBus 桥驱动

## 名称

`pccbb`

## 概要

`device cbb device pccard device cardbus device exca`

## 描述

`pccbb` 驱动实现了 CardBus 桥的 Yenta 规范。

支持以下 PCI cardbus 和 pcmcia 桥：

- Cirrus Logic PD6832
- Cirrus Logic PD6833
- Cirrus Logic PD6834
- O2micro OZ6812
- O2micro OZ6832
- O2micro OZ6833
- O2micro OZ6836
- O2micro OZ6860
- O2micro OZ6872
- O2micro OZ6912
- O2micro OZ6922
- O2micro OZ6933
- O2micro OZ6972
- O2Micro OZ711E1
- O2Micro OZ711M1

- Ricoh RL4C475
- Ricoh RL4C476
- Ricoh RL4C477
- Ricoh RL4C478
- TI PCI-1031
- TI PCI-1130
- TI PCI-1131
- TI PCI-1210
- TI PCI-1211
- TI PCI-1220
- TI PCI-1221
- TI PCI-1225
- TI PCI-1250
- TI PCI-1251
- TI PCI-1251B
- TI PCI-1260
- TI PCI-1260B
- TI PCI-1410
- TI PCI-1420
- TI PCI-1450
- TI PCI-1451
- TI PCI-1510
- TI PCI-1515
- TI PCI-1520
- TI PCI-1530
- TI PCI-1620
- TI PCI-4410
- TI PCI-4450
- TI PCI-4451
- TI PCI-4510
- TI PCI-4520
- TI PCI-[67]x[12]1
- TI PCI-[67]x20
- ENE CB710
- ENE CB720
- ENE CB1211
- ENE CB1255
- ENE CB1410
- ENE CB1420
- Toshiba ToPIC95
- Toshiba ToPIC95B
- Toshiba ToPIC97
- Toshiba ToPIC100

## 加载器可调参数

驱动支持以下可调参数，可添加到 **/boot/loader.conf** 或通过 [sysctl(8)](../man8/sysctl.8.md) 命令设置：

**`hw.cbb.debug`** 非零值会导致打印更详细的信息，以帮助调试桥芯片组的问题。

## 参见

[cardbus(4)](cardbus.4.md), [exca(4)](exca.4.md)
