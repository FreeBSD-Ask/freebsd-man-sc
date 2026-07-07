# tws(4)

`tws` — 3ware 9750 SATA+SAS 6Gb/s RAID 控制卡驱动

## 名称

`tws`

## 概要

`若要将此驱动编译进内核，请在内核配置文件中加入以下行：`

> device scbus
> device tws

`或者，要在引导时以模块形式加载驱动，请在 loader.conf(5) 中加入以下行：`

```sh
tws_load="YES"
```

## 描述

`tws` 驱动提供对 LSI 3ware 9750 SATA+SAS 6Gb/s RAID 控制卡的支持。

这些控制器采用 LSISAS2108 6Gb/s SAS ROC（片上 RAID）芯片，提供 4 端口和 8 端口两种配置，支持 RAID 0、1、5、6、10、50 及单盘级别，最多可连接 96 个 SATA 和/或 SAS 硬盘和 SSD。

有关硬件的更多信息，参见 `http://www.lsi.com/.`

## 硬件

`tws` 驱动支持以下 SATA/SAS RAID 控制器：

- LSI 3ware SAS 9750 系列

## 加载器可调参数

可在引导内核前于 [loader(8)](../man8/loader.8.md) 提示符处设置可调参数，或存储在 loader.conf(5) 中。

**`hw.tws.cam_depth`** 单个控制器排队的最大 CAM SIM 请求数。默认值为 256。

**`hw.tws.enable_msi`** 此可调参数设为非零值时在控制器上启用 MSI 支持。默认值为 0。

**`hw.tws.queue_depth`** 单个控制器排队的最大请求数。

**`hw.tws.use_32bit_sgls`** 限制驱动仅使用 32 位 SG 元素，无论操作系统是否以 64 位模式运行。默认值为 0。

## 文件

**`/dev/da?`** 阵列/逻辑磁盘接口
**`/dev/tws?`** 管理接口

## 诊断

当驱动遇到命令失败时，会以如下格式打印错误代码：“” `ERROR: (<error source>: <error code>):`，后跟错误的文本描述。根据所遇错误的类型，驱动还会打印其他错误消息和警告。如果驱动编译时定义了 `TWS_DEBUG`，它会打印大量调试消息。

## 参见

[da(4)](da.4.md), [scsi(4)](scsi.4.md)

## 作者

`tws` 驱动由 Manjunath Ranganathaiah 为 LSI 编写，本 man 页面由 Xin LI <delphij@FreeBSD.org> 为 iXsystems, Inc. 编写。
