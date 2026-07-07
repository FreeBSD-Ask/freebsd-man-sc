# u3g(4)

`u3g` — 3G 和 4G 蜂窝调制解调器的 USB 支持

## 名称

`u3g`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device usb
> device ucom
> device u3g

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
u3g_load="YES"
```

`如果上述两项都未执行，则当设备连接时，devd(8) 会自动加载此驱动。`

## 描述

`u3g` 驱动提供对许多 3G 和 4G 调制解调器暴露的 USB 转串行接口的支持。所支持的适配器为 ppp(8) 或 `net/mpd5` 连接提供必要的调制解调器端口。根据具体设备，额外端口提供其他功能，如附加命令端口、诊断端口、GPS 接收器端口或 SIM 工具包端口。

该设备通过 [ucom(4)](ucom.4.md) 驱动访问，使其行为类似 [tty(4)](tty.4.md)。

在某些适配器中，存在由 [umass(4)](umass.4.md) 驱动支持的大容量存储设备，其中包含 Windows 和 Mac OS X 驱动。设备以磁盘模式（TruInstall、ZeroCD 等）启动，需要附加命令才能切换到调制解调器模式。如果你的设备未自动切换，请尝试添加 quirks。参见 usbconfig(8) 和 [usb_quirk(4)](usb_quirk.4.md)。

## 硬件

`u3g` 驱动支持以下蜂窝调制解调器：

- Option GT 3G Fusion、GT Fusion Quad 等（仅 3G，不含 WLAN）
- Option GT 3G、GT 3G Quad 等
- Vodafone Mobile Connect Card 3G
- Vodafone Mobile Broadband K3772-Z
- Qualcomm Inc. CDMA MSM
- Qualcomm Inc. GOBI 1000、2000 和 3000 设备（采用 MDM1000 或 MDM2000 芯片组）
- QUECTEL BGX、ECX、EGX、EMX、EPX、RGX 系列
- Quectel EM160R、EM060K（参见 Sx 注意事项）
- Huawei B190、E180v、E220、E3372、E3372v153、E5573Cs322（'<Huawei Mobile>'）
- Novatel U740、MC950D、X950D 等
- Sierra MC875U、MC8775U、EM7590 等
- Panasonic CF-F9 GOBI

支持的设备更多，完整列表参见 **`/sys/dev/usb/serial/u3g.c`**。

## 文件

**`/dev/ttyU*.*`** 用于呼入端口
**`/dev/ttyU*.*.init`**
**`/dev/ttyU*.*.lock`** 相应的呼入初始状态和锁定状态设备
**`/dev/cuaU*.*`** 用于呼出端口
**`/dev/cuaU*.*.init`**
**`/dev/cuaU*.*.lock`** 相应的呼出初始状态和锁定状态设备

## 实例

使用默认配置连接到 Internet：

```sh
ppp -background u3g
```

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md), [usb_quirk(4)](usb_quirk.4.md), devd(8), ppp(8), usbconfig(8)

## 历史

`u3g` 驱动出现于 FreeBSD 7.2，基于 [uark(4)](uark.4.md) 驱动，由 Andrea Guzzo <aguzzo@anywi.com> 于 2008 年 9 月编写。

## 作者

`u3g` 驱动由 Andrea Guzzo <aguzzo@anywi.com> 和 Nick Hibma <n_hibma@FreeBSD.org> 编写。测试硬件由荷兰莱顿的 AnyWi Technologies 提供。

## 注意事项

Quectel EM160R 在 PPP 模式下未获官方支持。要在 PPP 模式下使用它，需要关闭 ctsrts 选项，例如在 **`/etc/ppp/ppp.conf`** 的相应节中加入：

```sh
set ctsrts off
```

## 缺陷

除非驱动已编译进内核或在设备连接前加载，否则从磁盘模式到调制解调器模式的自动切换无法工作。

基于 GOBI 的设备需要 `sysutils/gobi_loader` port 中提供的 gobi loader。
