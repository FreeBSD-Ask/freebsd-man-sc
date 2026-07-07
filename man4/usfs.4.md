# usfs(4)

`usfs` — USB 设备端仅批量传输大容量存储支持

## 名称

`usfs`

## 概要

要将此驱动编译进内核，请将以下行加入你的内核配置文件：

> device usb
> device usfs

或者，要在引导时以模块方式加载该驱动，请将以下行加入 loader.conf(5)：

```sh
usfs_load="YES"
```

## 描述

**此驱动已过时。建议用户改用 [cfumass(4)](cfumass.4.md)。**

`usfs` 驱动在 USB 协议栈以 USB 设备端模式激活时（加载 [usb_template(4)](usb_template.4.md) 模块并将 `hw.usb.template` sysctl 设置为 0）提供 USB 大容量存储设备仿真支持。

附加时，该驱动会创建一个可读写的 RAM 磁盘。

## 参见

[cfumass(4)](cfumass.4.md), [umass(4)](umass.4.md), [usb(4)](usb.4.md), [usb_template(4)](usb_template.4.md)

## 历史

`usfs` 驱动出现于 FreeBSD 8.0。
