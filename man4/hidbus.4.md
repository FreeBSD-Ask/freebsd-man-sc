# hidbus(4)

`hidbus` — 通用 HID 总线驱动

## 名称

`hidbus`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device hidbus
> device hid

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
hidbus_load="YES"
```

## 描述

`hidbus` 驱动提供对单个 HID 传输后端附加多个 HID 驱动的支持。参见 [iichid(4)](iichid.4.md) 或 [usbhid(4)](usbhid.4.md)。

每个 HID 设备可有多个组件，例如键盘和鼠标。这些组件使用不同的报告标识符（一个字节）组合成称为集合的组，以区分数据来自哪个组件。`hidbus` 驱动上附加了其他处理特定类型设备的驱动，`hidbus` 将数据广播给所有这些驱动。

## SYSCTL 变量

以下变量既是 [sysctl(8)](../man8/sysctl.8.md) 变量，也是 [loader(8)](../man8/loader.8.md) 可调参数：

**`hw.hid.hidbus.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

## 参见

[hconf(4)](hconf.4.md), [hcons(4)](hcons.4.md), [hgame(4)](hgame.4.md), [hidraw(4)](hidraw.4.md), [hkbd(4)](hkbd.4.md), [hms(4)](hms.4.md), [hmt(4)](hmt.4.md), [hpen(4)](hpen.4.md), [hsctrl(4)](hsctrl.4.md), hskbd(4), [iichid(4)](iichid.4.md), [usbhid(4)](usbhid.4.md)

## 历史

`hidbus` 驱动首次出现于 FreeBSD 13.0。

## 作者

`hidbus` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
