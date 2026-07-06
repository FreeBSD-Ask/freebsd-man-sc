# umass.4

`umass` — USB 大容量存储设备驱动

## 名称

`umass`

## 概要

`device da device scbus device pass device usb device umass`

在 loader.conf(5) 中：`umass_load`

## 描述

`umass` 驱动为连接到 USB 接口的大容量存储设备提供支持。

若检测到相应硬件，该驱动会由 [devmatch(8)](../man8/devmatch.8.md) 自动加载。若要在引导时手动加载该驱动，请在 [loader(8)](../man8/loader.8.md) 提示符下使用 `umass_load` 命令，或将其加入 loader.conf(5)。

要在自定义内核中使用此驱动，内核中必须配置 [usb(4)](usb.4.md) 和 [uhci(4)](uhci.4.md)、[ohci(4)](ohci.4.md)、[ehci(4)](ehci.4.md) 或 [xhci(4)](xhci.4.md) 中的至少一个。此外，由于 `umass` 使用 SCSI 子系统且有时充当 SCSI 设备，因此内核中还需包含 [da(4)](da.4.md) 和 scbus(4)。

## 硬件

`umass` 驱动支持以下 USB 大容量存储设备：

- USB 闪存盘
- USB 硬盘驱动器
- USB 软盘驱动器

`umass` 驱动尽力避免驱动器问题，但并非所有问题都能自动处理，因此可能需要使用 quirks。有关驱动器的 quirks，请参见 [usb_quirk(4)](usb_quirk.4.md) 的 *USB 大容量存储 quirks* 部分。usbconfig(8) 的 `add_dev_quirk_vplh` 和 `add_quirk` 命令可动态管理这些 quirks。quirks 也可通过可调参数指定，详见 [usb_quirk(4)](usb_quirk.4.md)。

## 实例

重新扫描多插槽读卡器上的所有插槽，其中插槽映射到单个 SCSI ID 上的不同 LUN：

```sh
camcontrol rescan 0:0:0
camcontrol rescan 0:0:1
camcontrol rescan 0:0:2
camcontrol rescan 0:0:3
```

通常引导时仅启用第一个插槽。此示例假设读卡器是系统中第一个 SCSI 总线且具有 4 个插槽。

## 参见

[cfumass(4)](cfumass.4.md), [ehci(4)](ehci.4.md), [ohci(4)](ohci.4.md), [uhci(4)](uhci.4.md), [usb(4)](usb.4.md), [usb_quirk(4)](usb_quirk.4.md), [xhci(4)](xhci.4.md), [camcontrol(8)](../man8/camcontrol.8.md), usbconfig(8)。

## 历史

`umass` 驱动出现于 FreeBSD 4.3。

## 作者

`umass` 驱动由 MAEKAWA Masahide <bishop@rr.iij4u.or.jp> 和 Nick Hibma <n_hibma@FreeBSD.org> 编写。

本手册页由 Nick Hibma <n_hibma@FreeBSD.org> 编写。
