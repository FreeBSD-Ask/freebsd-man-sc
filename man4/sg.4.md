# sg.4

`sg` — 兼容 Linux ioctl 的 SCSI 直通设备

## 名称

`sg`

## 概要

`device sg device scbus`

## 描述

`sg` 驱动提供一个兼容 Linux 的 SCSI 直通设备。此驱动附加到所有 cam(4) 外设。它类似于 [pass(4)](pass.4.md) 设备，但使用 Linux 接口而非 FreeBSD CAM 接口。

## IOCTL

实现了以下 Linux sg ioctl 接口的子集：

**`SG_SET_TIMEOUT`** `u_int to` 设置超时时间（毫秒）。

**`SG_GET_TIMEOUT`** 获取超时时间（毫秒）。

**`SG_GET_RESERVED_SIZE`** `u_int` 返回可对此设备执行的 I/O 大小。

**`SG_GET_SCSI_ID`** `struct sg_scsi_id` 返回 SCSI 设备的总线号、通道、SCSI 总线 ID 号、lun 及其他信息。

**`SG_GET_SG_TABLESIZE`** `u_int` 返回表大小，但硬编码为 0。

**`SG_GET_VERSION_NUM`** `u_int` 返回所实现的版本号。

**`SG_IO`** `struct sg_io_hdr`

所有其他 ioctl 接口返回 `ENODEV`。

## 文件

**`/dev/sg*`** 直通设备。

## 参见

cam(4), [pass(4)](pass.4.md)

## 历史

`sg` 驱动最早出现于 FreeBSD 7.0。
