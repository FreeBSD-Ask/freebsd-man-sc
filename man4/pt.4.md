# pt(4)

`pt` — SCSI 处理器类型驱动程序

## 名称

`pt`

## 概要

`device pt`

## 描述

`pt` 驱动程序为 SCSI 处理器类型设备提供支持。这类设备通常是扫描仪以及其他使用 SCSI 链路作为通信接口、将设备特定命令嵌入数据流的设备。

在使用此驱动程序之前，必须单独将 SCSI 适配器配置到系统中。

此设备支持 read(2) 和 write(2)，以及下文所述的 ioctl(2) 调用。

## IOCTLS

`pt` 驱动程序支持以下 ioctl(2) 调用。它们定义于头文件：

`#include <sys/ptio.h>`

**PTIOCGETTIMEOUT** 此 ioctl 允许用户态应用程序获取当前 `pt` 驱动程序的读写超时。返回值以秒为单位。

**PTIOCSETTIMEOUT** 此 ioctl 允许用户态应用程序设置当前 `pt` 驱动程序的读写超时。值以秒为单位。

## 文件

**`/dev/pt`** `N` 第 `N` 个处理器设备。

## 参见

cam(4)

## 历史

`pt` 驱动程序出现于 FreeBSD 2.1。
