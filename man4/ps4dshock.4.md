# ps4dshock.4

`ps4dshock` — Sony PlayStation 4 Dualshock 4 游戏手柄驱动程序

## 名称

`ps4dshock`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device ps4dshock
> device hid
> device hidbus
> device hidmap
> device evdev

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
ps4dshock_load="YES"
```

## 描述

`ps4dshock` 驱动程序为 Sony PlayStation 4 Dualshock 4 游戏手柄提供支持。

**`/dev/input/event*`** 设备将游戏控制器呈现为 `evdev` 类型设备。*games* 组的成员可以访问它。

## SYSCTL 变量

以下参数可作为 [sysctl(8)](../man8/sysctl.8.md) 变量使用。Debug 参数也可作为 [loader(8)](../man8/loader.8.md) 可调参数使用。

**`dev.p4dshock.*.led_state`** LED 状态：0 - 关闭，1 - 开启，2 - 闪烁。

**`dev.p4dshock.*.led_color_r`** LED 颜色。红色分量。

**`dev.p4dshock.*.led_color_g`** LED 颜色。绿色分量。

**`dev.p4dshock.*.led_color_b`** LED 颜色。蓝色分量。

**`dev.p4dshock.*.led_delay_on`** LED 闪烁。点亮时长，毫秒。

**`dev.p4dshock.*.led_delay_off`** LED 闪烁。熄灭时长，毫秒。

**`hw.hid.ps4dshock.debug`** 调试输出级别，0 表示禁用调试，更大的值提高调试消息的详尽程度。默认为 0。

## 文件

**`/dev/input/event*`** 输入事件设备节点。

## 缺陷

`ps4dshock` 不支持力反馈事件。

## 历史

`ps4dshock` 驱动程序首次出现于 FreeBSD 13.0。

## 作者

`ps4dshock` 驱动程序由 Vladimir Kondratyev <wulf@FreeBSD.org> 编写。
