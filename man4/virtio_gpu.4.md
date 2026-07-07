# virtio_gpu(4)

`virtio_gpu` — VirtIO GPU 驱动

## 名称

`virtio_gpu`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device virtio_gpu

## 描述

`virtio_gpu` 设备驱动为 VirtIO gpu 设备提供支持，以创建 [vt(4)](vt.4.md) 控制台。

## 参见

[virtio(4)](virtio.4.md), [vt(4)](vt.4.md)

## 历史

`virtio_gpu` 驱动最早出现于 FreeBSD 14.0。
