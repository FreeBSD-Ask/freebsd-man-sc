# virtio_random.4

`virtio_random` — VirtIO 熵驱动

## 名称

`virtio_random`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device virtio_random

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
virtio_random_load="YES"
```

## 描述

`virtio_random` 设备驱动为 VirtIO 熵设备提供支持。

熵设备将来自 hypervisor 的高质量随机性提供给客户机。

## 参见

[random(4)](random.4.md), [virtio(4)](virtio.4.md)

## 历史

`virtio_random` 驱动由 Bryan Venteicher <bryanv@FreeBSD.org> 编写。
