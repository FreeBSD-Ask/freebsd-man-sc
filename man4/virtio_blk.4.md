# virtio_blk(4)

`virtio_blk` — VirtIO 块设备驱动

## 名称

`virtio_blk`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device virtio_blk

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
virtio_blk_load="YES"
```

## 描述

`virtio_blk` 设备驱动为 VirtIO 块设备提供支持。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.vtblk.no_ident`**

**`hw.vtblk.`** `X``.no_ident` 这些可调参数可全局或按设备禁用从 hypervisor 获取设备标识字符串。默认值为 0。

**`hw.vtblk.writecache_mode`**

**`hw.vtblk.`** `X``.writecache_mode` 这些可调参数可全局或按设备确定写入缓存模式。仅当协商了 ConfigWCE 特性时才能更改模式。设置为 0 表示 writethrough 模式，1 表示 writeback 模式，-1 表示保持原样。默认值为保持原样。

## SYSCTL 变量

以下变量作为 [sysctl(8)](../man8/sysctl.8.md) 变量可用。

**`dev.vtblk.`** `X``.writecache_mode` 设备的写入缓存模式可为 writethrough（0）或 writeback（1）。若协商了 ConfigWCE 特性，可在 writethrough 与 writeback 之间切换写入缓存模式。

## 参见

[virtio(4)](virtio.4.md)

## 历史

`virtio_blk` 驱动由 Bryan Venteicher <bryanv@FreeBSD.org> 编写。最早出现于 FreeBSD 9.0。
