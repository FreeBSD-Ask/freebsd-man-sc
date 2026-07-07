# usb_template(4)

`usb_template` — USB 设备端模板

## 名称

`usb_template`

## 概要

要将此模块编译进内核，请将以下行加入你的内核配置文件：

> device usb_template

要在引导时以模块方式加载该模块，请将以下行加入 loader.conf(5)：

```sh
usb_template_load="YES"
```

## 描述

`usb_template` 模块实现编程 USB 设备端驱动时所需的各种 USB 模板。USB 模板由一个 USB 设备描述符、一个或多个 USB 配置描述符、一个或多个 USB 接口描述符、一个或多个 USB 端点描述符、USB 字符串和附加 USB 描述符组成。USB 模板通过 `hw.usb.template` sysctl 和可调参数选择，或使用 usbconfig(8) 的 `set_template` 子命令选择。更改 `hw.usb.template` sysctl 会触发 USB 主机重新枚举；对其他 sysctl 的更改在重新枚举之前可能对主机不可见。

可用模板为：

[cfumass(4)](cfumass.4.md)

[cdce(4)](cdce.4.md)

[umodem(4)](umodem.4.md)

[cdceem(4)](cdceem.4.md)

| *值* | *描述* |
| --- | --- |
| `0` | USB 大容量存储，参见 |
| `1` | CDC 以太网，参见 |
| `2` | 媒体传输协议（MTP） |
| `3` | USB 串口，参见 |
| `4` | USB 音频 |
| `5` | USB 键盘 |
| `6` | USB 鼠标 |
| `7` | USB 电话 |
| `8` | CDC 以太网和串口 |
| `9` | USB MIDI |
| `10` | CDC 以太网、串口和存储 |
| `11` | CDC 以太网仿真模型，参见 |

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`hw.usb.template`** 当前选择的模板。设置为 -1 可使设备从 USB 主机视角消失。

**`hw.usb.template_power`** 5V 时的 USB 总线功耗（单位为 mA）。必须在 0 到 500 之间。设置为 0 标记设备为自供电。默认为 500mA。

**`hw.usb.templates.N`** 模板编号 `N` 的配置。

**`hw.usb.templates.N.vendor_id`** 16 位厂商标识符（VID），通常由 USB-IF 分配。

**`hw.usb.templates.N.product_id`** 16 位产品标识符（PID）。

**`hw.usb.templates.N.manufacturer`** 包含人类可读制造商名称的字符串。

**`hw.usb.templates.N.product`** 包含人类可读产品名称的字符串。

## 参见

[cfumass(4)](cfumass.4.md), [usb(4)](usb.4.md), [usfs(4)](usfs.4.md), usbconfig(8)

## 标准

`usb_template` 模块符合 USB 1.0、2.0 和 3.0 标准。

## 历史

`usb_template` 模块由 Hans Petter Selasky <hselasky@FreeBSD.org> 编写。
