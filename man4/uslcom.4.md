# uslcom(4)

`uslcom` — 基于 Silicon Laboratories CP2101/CP2102/CP2103/CP2104/CP2105 的 USB 串口适配器

## 名称

`uslcom`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device uslcom

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uslcom_load="YES"
```

## 描述

`uslcom` 驱动支持基于 Silicon Laboratories CP2101/CP2102/CP2103/CP2104/CP2105 的 USB 串口适配器。

CP2101/CP2102/CP2103 的数据手册将最大支持波特率列为 921,600。经验测试表明，1,228,800 和 1,843,200 的速率也可工作（至少在某些硬件上），因此该驱动允许设置这些速率。

## 硬件

以下设备应能与 `uslcom` 驱动配合工作：

- AC-Services CAN、CIS-IBUS、IBUS 和 OBD 接口
- Aerocomm 电台
- AKTACOM ACE-1001 电缆
- AMBER Wireless AMB2560
- Arkham DS-101 适配器
- Argussoft ISP
- Arygon Technologies Mifare RFID 读卡器
- AVIT Research USB-TTL 接口
- B&G H3000 数据电缆
- Balluff RFID 读卡器
- Baltech 读卡器
- BEI USB VCP 传感器
- Burnside Telecom Desktop Mobile
- chip45.com Crumb128 模块
- Clipsal 5000CT2、5500PACA、5500PCU、560884、5800PC、C5000CT2 和 L51xx C-Bus 家庭自动化产品
- Commander 2 EDGE（GSM）调制解调器
- Cygnal Fasttrax GPS 和调试适配器
- DataApex MultiCOM USB 转 RS232 转换器
- Degree Controls USB 适配器
- DekTec DTA Plus VHF/UHF 增强器
- Dell DW700 GPS 接收器
- Digianswer ZigBee/802.15.4 MAC
- Dynastream ANT 开发套件
- Elan USBcount50、USBscope50、USBpulse100 和 USBwave12
- ELV USB-I2C 接口
- EMS C1007 HF RFID 控制器
- Festo CPX-USB 和 CMSP 接口
- Gemalto Prox-PU/CU 非接触式读卡器
- Helicomm IP-Link 1220-DVM
- IMS USB-RS422 适配器
- Infinity GPS-MIC-1 无线单声道耳机
- INSYS 调制解调器
- IRZ SG-10 和 MC35pu GSM/GPRS 调制解调器
- Jablotron PC-60B
- Kamstrup M-Bus Master MultiPort 250D 和 Optical Eye/3 线公用事业仪表接口
- Kyocera GPS
- Link Instruments MS-019 和 MS-028 示波器/逻辑分析仪/模式发生器
- Lipowsky Baby-JTAG、Baby-LIN 和 HARP-1
- MEI CashFlow SC 和 Series 2000 纸币接收器
- MJS USB-TOSLINK 适配器
- MobiData GPRS USB 调制解调器
- MSD DashHawk
- Multiplex RC 适配器
- Optris MSpro LT 温度计
- Owen AC4 USB-RS485 转换器
- Pirelli DP-L10 SIP 电话
- PLX CA-42 电话电缆
- Pololu USB 转串口
- Procyon AVS Mind Machine
- Renesas RX-Stick for RX610
- Siemens MC60 电缆
- Silicon Laboratories 通用 CP2101/CP2102/CP2103/CP2104/CP2105 芯片
- Software Bisque Paramount ME
- SPORTident BSM7-D USB
- Suunto 运动仪器
- Syntech CipherLab USB 条码扫描器
- T-Com TC 300 SIP 电话
- Tams Master Easy Control
- Telegesis ETRX2USB
- Timewave HamLinkUSB
- Tracient RFID 读卡器
- Track Systems Traqmate
- Vaisala USB 仪器电缆
- VStabi 控制器
- WAGO 750-923 USB 服务电缆
- WaveSense Jazz 血糖仪
- WIENER Plein & Baus CML 数据记录器、RCM 遥控器以及 PL512 和 MPOD PSU
- WMR RIGblaster Plug&Play 和 RIGtalk RT1
- Zephyr Bioharness

## 文件

**`/dev/ttyU*`** 用于呼入端口
**`/dev/ttyU*.init`**
**`/dev/ttyU*.lock`** 对应的呼入初始状态和锁定状态设备
**`/dev/cuaU*`** 用于呼出端口
**`/dev/cuaU*.init`**
**`/dev/cuaU*.lock`** 对应的呼出初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`uslcom` 设备驱动首次出现于 OpenBSD 4.0。首个包含它的 FreeBSD 版本为 FreeBSD 7.1。

## 作者

`uslcom` 驱动由 Jonathan Gray <jsg@openbsd.org> 编写。
