# udl.4

`udl` — DisplayLink DL-120 / DL-160 USB 显示设备驱动

## 名称

`udl`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device udl
> device videomode

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
udl_load="YES"
```

## 硬件

`udl` 驱动支持基于 DisplayLink DL-120 和 DL-160 图形芯片的 USB 显示设备，包括：

- Century Corp. Japan Plus One LCD-8000U
- Century Corp. Japan Plus One LCD-4300U
- DisplayLink USB to DVI
- ForwardVideo EasyCAP008 USB to DVI
- HP USB 2.0 Docking Station (FQ834)
- HP USB Graphics Adapter (NL571)
- IOGEAR USB 2.0 External DVI (GUC2020)
- Koenig CMP-USBVGA10 和 CMP-USBVGA11
- Lenovo 45K5296 USB to DVI
- Lenovo ThinkVision LT1421
- Lilliput UM-70
- Nanovision MiMo UM-710 和 UM-740
- Rextron VCUD60 USB to DVI
- Samsung LD220
- StarTech CONV-USB2DVI
- Sunweit USB to DVI
- Unitek Y-2240 USB to DVI
- VideoHome NBdock1920
- i-tec USB 2.0 Docking Station (USBDVIDOCK)

## 参见

[usb(4)](usb.4.md)

## 历史

`udl` 驱动出现于 OpenBSD 4.6 和 FreeBSD 11.0。
