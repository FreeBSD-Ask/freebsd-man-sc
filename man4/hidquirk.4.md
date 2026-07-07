# hidquirk(4)

`hidquirk` — HID 怪癖模块

## 名称

`hidquirk`

## 概要

要将此模块编译进内核，请在内核配置文件中加入以下行：

> device hid

或者，要在引导时以模块方式加载该模块，请在 loader.conf(5) 中加入以下行：

```sh
hidquirk_load="YES"
```

## 描述

`hidquirk` 模块提供为 HID 设备添加怪癖的支持。

**HQ_HID_IGNORE** 设备应被 hid 类忽略

**HQ_KBD_BOOTPROTO** 设备应设置引导协议

**HQ_MS_BOOTPROTO** 设备应设置引导协议

**HQ_MS_BAD_CLASS** 未能正确识别

**HQ_MS_LEADING_BYTE** 鼠标发送未知的引导字节

**HQ_MS_REVZ** 鼠标 Z 轴反向

**HQ_MS_VENDOR_BTN** 鼠标按钮位于供应商 usage page

**HQ_SPUR_BUT_UP** 虚假的鼠标按钮抬起事件

**HQ_MT_TIMESTAMP** 多点触控设备导出硬件时间戳 `0x1b5a01`

支持的全部怪癖列表请参见 **`/sys/dev/hid/hidquirk.h`**。

## 加载器可调参数

以下可调参数可在引导内核之前于 [loader(8)](../man8/loader.8.md) 提示符处设置，或存储在 loader.conf(5) 中。

```sh
“BusId VendorId ProductId LowRevision HighRevision HQ_QUIRK,... ”
```

**`hw.hid.quirk.%d`** 其值为一个字符串，格式为：为所有匹配 `BusId`、`VendorId` 和 `ProductId` 且硬件版本在 `LowRevision` 和 `HighRevision` 之间（含两端）的 HID 设备安装怪癖 `HQ_QUIRK,...`。`BusId`、`VendorId`、`ProductId`、`LowRevision` 和 `HighRevision` 都是 16 位数字，可使用十进制或十六进制表示。最多可定义 100 个变量 `hw.hid.quirk.0, .1, ..., .99`。如果在内核内部怪癖表中找到匹配条目，则会被新定义替换。否则，在怪癖表未满的情况下将创建新条目。内核从 `N = 0` 开始迭代 `hw.hid.quirk.N` 变量，并在 `N = 99` 或第一个不存在的变量处停止。

## 实例

要在引导时安装怪癖，请在 loader.conf(5) 中加入一行或多行如下内容：

```sh
hw.hid.quirk.0="0x18 0x6cb 0x1941 0 0xffff HQ_MT_TIMESTAMP"
```

## 历史

`hidquirk` 模块首次出现于 FreeBSD 13.0。

## 作者

`hidquirk` 驱动由 Hans Petter Selasky <hselasky@FreeBSD.org> 为 [usb(4)](usb.4.md) 子系统编写，并由 Vladimir Kondratyev <wulf@FreeBSD.org> 适配到 hid(4)。本手册页基于 Nick Hibma <n_hibma@FreeBSD.org> 编写的 [usb_quirk(4)](usb_quirk.4.md) 手册页。
