# xpt.4

`xpt` — CAM 传输层接口

## 名称

`xpt`

## 概要

`无。`

## 描述

`xpt` 驱动为用户空间应用程序提供向内核发出某些 CAM CCB 的方式。

由于 `xpt` 驱动允许直接访问 CAM 子系统，系统管理员在授予对此驱动的访问权限时应谨慎行事。如果使用不当，此驱动可能允许用户空间应用程序导致机器崩溃或数据丢失。

## 内核配置

`xpt` 驱动无需内核配置。当内核中启用 SCSI 支持时，它即被启用。每个 CAM 传输层实例对应一个 xpt 驱动实例。由于目前只有一个 CAM 传输层，因此此驱动只有一个实例。

## IOCTLS

**XPT_SCAN_BUS**
**XPT_RESET_BUS**
**XPT_SCAN_LUN**
**XPT_ENG_INQ**
**XPT_ENG_EXEC**
**XPT_DEBUG**
**XPT_DEV_MATCH**
**XPT_PATH_INQ**

**CAMIOCOMMAND** 此 ioctl 接受某些类型的 CAM CCB 并将其传递给 CAM 传输层执行。仅支持以下 CCB 类型：上述 CCB 是唯一受支持的，因为通过通用 pass-through 设备发送它们比通过绑定到特定底层 SCSI 设备的 pass-through 设备更有意义。

**CAMGETPASSTHRU** 此 ioctl 接受一个 XPT_GDEVLIST CCB，并返回与相关设备对应的 pass-through 设备。

## 文件

**`/dev/xpt0`** `xpt` 驱动的字符设备节点。

## 诊断

无。

## 参见

cam(3), cam_cdbparse(3), [pass(4)](pass.4.md), [camcontrol(8)](../man8/camcontrol.8.md)

## 历史

CAM 传输层驱动首次出现于 FreeBSD 3.0。

## 作者

Kenneth Merry <ken@FreeBSD.org>
