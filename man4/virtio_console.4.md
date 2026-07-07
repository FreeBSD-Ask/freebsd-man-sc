# virtio_console(4)

`virtio_console` — VirtIO 控制台驱动

## 名称

`virtio_console`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device virtio_console

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
virtio_console_load="YES"
```

## 描述

`virtio_console` 设备驱动为 VirtIO 控制台设备提供支持。

控制台设备可有一个或多个端口。每个端口类似于一个简单的串行接口，每个端口都可通过 [tty(4)](tty.4.md) 访问。

## 文件

**`/dev/ttyV?.??`**

## 参见

[tty(4)](tty.4.md), [virtio(4)](virtio.4.md)

## 历史

`virtio_console` 驱动由 Bryan Venteicher <bryanv@FreeBSD.org> 编写。
