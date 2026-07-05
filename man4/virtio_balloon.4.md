# virtio_balloon.4

`virtio_balloon` — VirtIO 内存 Balloon 驱动

## 名称

`virtio_balloon`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device virtio_balloon

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
virtio_balloon_load="YES"
```

## 描述

`virtio_balloon` 设备驱动为 VirtIO 内存 balloon 设备提供支持。

内存 balloon 允许客户机在 hypervisor 的请求下，将已分配的内存归还给 hypervisor，以便将其分配给其他客户机。hypervisor 之后可通知 balloon 归还内存。

## 参见

[virtio(4)](virtio.4.md)

## 历史

`virtio_balloon` 驱动由 Bryan Venteicher <bryanv@FreeBSD.org> 编写。最早出现于 FreeBSD 9.0。
