# backlight(8)

`backlight` — 配置背光硬件

## 名称

`backlight`

## 概要

`backlight [-q] [-f device]` `backlight [-q] [-f device] -i` `backlight [-f device] value` `backlight [-f device] incr|+ [value]` `backlight [-f device] decr|- [value]`

## 描述

`backlight` 工具可用于配置已注册背光的亮度级别。

不带任何参数调用时，它将打印第一个已注册背光的当前亮度级别。

选项如下：

**`-f`** `device` 要操作的设备。如果未指定，则使用 **`/dev/backlight/backlight0`**。如果提供了不带路径的名称，将自动添加 **`/dev/backlight/`** 前缀。

**`-i`** 查询有关背光的信息（名称、类型）。

**`-q`** 查询亮度级别时仅打印数值。

**`value`** 将亮度级别设置为此值，必须介于 0 和 100 之间。尾部可以加“%”。

**`incr`**|`+` [`value`] 增加背光级别。如果未指定值，则默认使用 10 个百分点。

**`decr`**|`-` [`value`] 降低背光级别。如果未指定值，则默认使用 10 个百分点。

## 实例

显示当前亮度级别：

```sh
$ backlight -f /dev/backlight/backlight0
brightness: 98
```

## 参见

[backlight(9)](../man9/backlight.9.md)

## 历史

`backlight` 工具出现于 FreeBSD 13.0。

## 作者

`backlight` 工具及本手册页由 Emmanuel Vadot <manu@FreeBSD.org> 编写。
