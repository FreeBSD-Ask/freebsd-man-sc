# ubser(4)

`ubser` — BWCT 控制台串行适配器的 USB 支持

## 名称

`ubser`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device usb
> device ucom
> device ubser

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
ubser_load="YES"
```

## 硬件

`ubser` 驱动提供对 BWCT 控制台管理串行适配器的支持。

## 文件

**`/dev/ttyU*.*`** 用于呼入端口
**`/dev/ttyU*.*.init`**
**`/dev/ttyU*.*.lock`** 相应的呼入初始状态和锁定状态设备
**`/dev/cuaU*.*`** 用于呼出端口
**`/dev/cuaU*.*.init`**
**`/dev/cuaU*.*.lock`** 相应的呼入初始状态和锁定状态设备

## 参见

[tty(4)](tty.4.md), [ucom(4)](ucom.4.md), [usb(4)](usb.4.md)

## 历史

`ubser` 驱动出现于 FreeBSD 5.2。
