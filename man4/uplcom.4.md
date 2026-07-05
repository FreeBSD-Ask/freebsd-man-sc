# uplcom.4

`uplcom` — 基于 Prolific PL-2303/2303X/2303HX 串行适配器的 USB 驱动

## 名称

`uplcom`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device ucom
> device uplcom

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
uplcom_load="YES"
```

## 描述

`uplcom` 驱动为基于 Prolific PL-2303、PL-2303X 和 PL-2303HX USB 转 RS232 桥接芯片的各类串行适配器提供支持。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

## 硬件

`uplcom` 驱动支持以下设备和适配器：

- ADLINK ND-6530 USB-Serial Adapter
- Alcatel One Touch 535/735 Phone
- Alcor AU9720 USB-RS232 Serial Adapter
- AlDiga AL-11U Modem
- Alltronix ACM003U00 Modem
- Anchor Serial adapter
- ATEN UC-232A
- ATEN UC-232B
- BAFO BF-800 and BF-810
- Belkin F5U257
- BenQ S81 Phone
- Corega CG-USBRS232R Serial Adapter
- Cressi Edy (Seiko) Diving Computer
- ELECOM UC-SGT Serial Adapter
- HAL Corporation Crossam2+USB IR commander
- Hama USB RS-232 Serial Adapter
- Hamlet exaggerate XURS232
- HP LD220 Point-Of-Sale (POS) Display
- IOGEAR UC-232A
- I/O DATA USB-RSAQ, USB-RSAQ2, USB-RSAQ3 and USB-RSAQ5
- iTegno WM1080A GSM/GFPRS Modem
- iTegno WM2080A CDMA Modem
- Leadtek 9531 GPS
- Micromax 610U Modem
- Microsoft Palm 700WX
- Mobile Action MA-620 Infrared Adapter
- Motorola Cables
- Nokia CA-42 Cable
- OTI DKU-5 cable
- Panasonic TY-TP50P6-S flat screen
- PLX CA-42 Phone Cable
- PLANEX USB-RS232 URS-03
- Prolific Generic USB-Serial Adapters
- Prolific Generic USB-Serial Adapters (HXN)
- Prolific Pharos USB-Serial Adapter
- Prolific USB-Serial Controller D
- RATOC REX-USB60
- Radio Shack USB Serial Cable
- Sagem USB-Serial Adapter
- Samsung I330 Phone Cradle
- Sandberg USB to Serial Link (model number 133-08)
- Sanwa KB-USB2 Multimeter cable
- Siemens/BenQ EF81, SX1, X65 and X75 Mobile Phones
- Sitecom USB-Serial Adapter
- SMART Technologies USB-Serial Adapter
- Sony QN3 Phone Cable
- Sony Ericsson Datapilot
- Sony Ericsson DCU-10 and DCU-11 (Susteen) USB Cables
- SOURCENEXT KeikaiDenwa 8 (with and without charger)
- Speed Dragon USB-Serial Cable
- Syntech CPT-8001C Barcode Scanner
- TDK UHA6400 and UPA9664 USB-PHS Adapters
- TRENDnet USB to Serial Converter (TU-S9)
- Tripp-Lite U209-000-R USB-Serial Adapter
- UIC HCR331 Magnetic Stripe Card Reader
- UIC MSR206 Magnetic Stripe Card Reader
- Willcom W-SIM DD PHS terminal.(WS002IN)
- YC-Cable USB-Serial Adapter
- Zeagle N2iTion3 Diving Computer

## SYSCTL 变量

以下变量既可作为 [sysctl(8)](../man8/sysctl.8.md) 变量，也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用：

**`hw.usb.uplcom.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

## 文件

**/dev/ttyU\*** 用于呼入端口
**/dev/ttyU\*.init**
**/dev/ttyU\*.lock** 对应的呼入初始状态和锁定状态设备
**/dev/cuaU\*** 用于呼出端口
**/dev/cuaU\*.init**
**/dev/cuaU\*.lock** 对应的呼出初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`uplcom` 驱动出现于 NetBSD 1.6。本手册页由 Tom Rhodes <trhodes@FreeBSD.org> 于 2002 年 4 月从 NetBSD 移植。
