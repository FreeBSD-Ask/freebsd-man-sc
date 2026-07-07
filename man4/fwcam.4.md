# fwcam(4)

`fwcam` — IIDC FireWire 数码相机驱动程序

## 名称

`fwcam`

## 概要

`device firewire device fwcam`

## 描述

`fwcam` 驱动程序为通过 IEEE 1394（FireWire）连接的 IIDC（Instrumentation and Industrial Digital Camera）v1.30 相机提供支持。

视频帧通过同步 DMA 通道接收，并通过字符设备暴露给应用程序。应用程序从 **/dev/fwcamX** 读取原始帧，并通过 ioctl(2) 配置相机。

本驱动程序支持 Format_0（VGA 非压缩）视频，包含以下模式：

**Mode** 0 160x120 YUV444（每帧 57,600 字节）
**Mode** 1 320x240 YUV422（每帧 153,600 字节）
**Mode** 2 640x480 YUV411（每帧 460,800 字节）
**Mode** 3 640x480 YUV422（每帧 614,400 字节）
**Mode** 4 640x480 RGB8（每帧 921,600 字节）
**Mode** 5 640x480 Mono8（每帧 307,200 字节）

相机功能（亮度、增益、快门、对焦等）通过 `FWCAM_GFEAT` 和 `FWCAM_SFEAT` ioctl 查询和设置。

## 硬件

`fwcam` 驱动程序支持任何符合 IIDC 1394-based Digital Camera Specification v1.30 的相机。已测试硬件：

- Apple iSight（FireWire 圆柱形），EUI-64 000a270004135e5d，Format_0 模式 1-3

## IOCTL

**`FWCAM_GMODE`** （`struct fwcam_mode`）获取当前的视频格式、模式和帧率。`frame_size` 字段将填入计算出的帧大小（以字节为单位）。

**`FWCAM_SMODE`** （`struct fwcam_mode`）设置视频格式、模式和帧率。如果流处于活动状态，将重启流。

**`FWCAM_GFEAT`** （`struct fwcam_feature`）获取功能能力和当前值。调用者将 `id` 设置为 `FWCAM_FEAT_*` 常量之一；驱动程序填充 `flags`、`min`、`max` 和 `value`。

**`FWCAM_SFEAT`** （`struct fwcam_feature`）设置功能值。

**`FWCAM_GINFO`** （`struct fwcam_info`）返回相机能力、当前设置和流统计信息，包括丢帧数和活动 ISO 通道。

## SYSCTL

**`hw.firewire.fwcam.iso_channel`** 同步接收通道（默认 0）。可在 loader.conf(5) 中作为可调参数设置。

## 文件

**/dev/fwcamX** 相机字符设备。读取以获取原始视频帧。

## 参见

[firewire(4)](firewire.4.md), [fwohci(4)](fwohci.4.md)

IIDC 1394-based Digital Camera Specification v1.30, 1394 Trade Association Document 1999023.

## 历史

`fwcam` 驱动程序首次出现于 FreeBSD 16.0。

## 作者

Abdelkader Boudih <freebsd@seuros.com>
