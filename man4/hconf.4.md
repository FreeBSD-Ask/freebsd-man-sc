# hconf(4)

`hconf` — MS Windows 精密触控板配置驱动

## 名称

`hconf`

## 概要

要将此驱动编译进内核，请在内核配置文件中加入以下行：

> device hconf
> device hid
> device hidbus

或者，要在引导时以模块方式加载该驱动，请在 loader.conf(5) 中加入以下行：

```sh
hconf_load="YES"
```

## 描述

`hconf` 驱动提供对通用 MS Windows 精密触控板配置集合的支持。它使主机能够配置设备的两个不同方面。一个允许主机选择输入模式，另一个允许主机选择性地决定报告内容。

## SYSCTL 变量

以下参数作为 [sysctl(8)](../man8/sysctl.8.md) 变量可用。Debug 参数也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用。

**`dev.hconf.*.input_mode`** HID 设备输入模式：0 = 鼠标，3 = 触控板。

**`dev.hconf.*.surface_switch`** 表面的启用/禁用开关：1 = 开启，0 = 关闭。

**`dev.hconf.*.buttons_switch`** 按钮的启用/禁用开关：1 = 开启，0 = 关闭。

**`hw.hid.hconf.debug`** 调试输出级别，0 表示禁用调试，更大的值会增加调试消息的详细程度。默认值为 0。

## 参见

[hms(4)](hms.4.md), [hmt(4)](hmt.4.md)

## 历史

`hconf` 驱动首次出现于 FreeBSD 13.0。

## 作者

`hconf` 驱动由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。开关参数支持由 Andriy Gapon <avg@FreeBSD.org> 添加。
