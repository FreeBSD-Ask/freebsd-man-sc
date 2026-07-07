# aw_sid(4)

`aw_sid` — Allwinner SoC 中 SID 控制器驱动

## 名称

`aw_sid`

## 描述

`aw_sid` 设备驱动为 Allwinner SID（Security ID，安全 ID）控制器提供支持。此控制器提供根安全密钥，可用作设备唯一 ID 或用于生成 MAC 地址。

## 硬件

`aw_sid` 驱动支持具有以下兼容字符串之一的 SID 控制器：

- allwinner,sun4i-a10-sid
- allwinner,sun7i-a20-sid
- allwinner,sun50i-a64-sid
- allwinner,sun8i-a83t-sid
- allwinner,sun8i-h3-sid
- allwinner,sun50i-h5-sid
- allwinner,sun20i-d1-sid

## SYSCTL 变量

以下只读变量可通过 [sysctl(8)](../man8/sysctl.8.md) 访问：

**`dev.aw_sid.rootkey`** 此设备的根安全密钥。

## 历史

`aw_sid` 设备驱动首次出现于 FreeBSD 11.0。

## 作者

`aw_sid` 设备驱动由 Jared McNeill <jmcneill@invisible.ca> 编写。本手册页由 Kyle Evans <kevans@FreeBSD.org> 编写。
