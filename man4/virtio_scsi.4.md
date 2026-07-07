# virtio_scsi(4)

`virtio_scsi` — VirtIO SCSI 驱动

## 名称

`virtio_scsi`

## 概要

`要将此驱动编译进内核，请在你的内核配置文件中加入以下行：`

> device virtio_scsi

`或者，要在引导时以模块形式加载此驱动，请在 loader.conf(5) 中加入以下行：`

```sh
virtio_scsi_load="YES"
```

## 描述

`virtio_scsi` 设备驱动为 VirtIO SCSI 设备提供支持。

## 加载器可调参数

可调参数可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符下设置，或存储在 loader.conf(5) 中。

**`hw.vtscsi.bus_reset_disable`** 在最初支持 VirtIO SCSI 的 QEMU 版本中，停止设备时未中止在途操作，导致总线复位无效。此可调参数禁用尝试发出总线复位命令。默认值为 1。

## 调试

要启用 `virtio_scsi` 驱动的调试输出，请设置

```sh
hw.vtscsi.X.debug_level
```

变量，其中 X 是适配器编号，可在 loader.conf(5) 中设置或通过 [sysctl(8)](../man8/sysctl.8.md) 设置。以下位具有所述效果：

**0x01** 启用信息性输出。

**0x02** 启用驱动错误输出。

**0x04** 启用跟踪输出。

## 参见

[virtio(4)](virtio.4.md)

## 历史

`virtio_scsi` 驱动由 Bryan Venteicher <bryanv@FreeBSD.org> 编写。最早出现于 FreeBSD 10.0。
