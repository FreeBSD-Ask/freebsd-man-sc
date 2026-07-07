# pvscsi(4)

`pvscsi` — VMware 半虚拟 SCSI 控制器

## 名称

`pvscsi`

## 概要

若要将此驱动程序编译进内核，请在你的内核配置文件中加入以下行：

> device pci
> device scbus
> device pvscsi

或者，若要在引导时以模块方式加载驱动程序，在 loader.conf(5) 中加入以下行：

```sh
pvscsi_load="YES"
```

以下可调参数可在 [loader(8)](../man8/loader.8.md) 中设置：

控制为设备请求环分配的页数。非正值将使驱动程序根据设备能力选择值。非零值将使用该数量的页，最多 32。默认设置为 0。

控制适配器的队列大小。非正值将使驱动程序根据请求环页数选择值。非零值将设置队列大小，上限为请求环页数所允许的最大值。默认为 0。

设为非零值可启用 PVSCSI 消息队列，允许磁盘热添加和移除而无需手动重新扫描。默认为 1。

设为非零值可启用 MSI 中断。默认为 1。

设为非零值可启用 MSI-X 中断。默认为 1。

设为非零值可启用请求调用阈值功能。TODO。默认为 1。

**hw.pvscsi.request_ring_pages**

**hw.pvscsi.max_queue_depth**

**hw.pvscsi.use_msg**

**hw.pvscsi.use_msi**

**hw.pvscsi.use_msix**

**hw.pvscsi.use_req_call_threshold**

## 描述

`pvscsi` 驱动程序为 VMware 虚拟机中的 VMware 半虚拟 SCSI 控制器（PVSCSI）提供支持。

## 参见

cam(4), [da(4)](da.4.md)

## 历史

`pvscsi` 驱动程序首次出现于 FreeBSD 13.0。

## 作者

Vishal Bhakta <vbhakta@vmware.com>。
