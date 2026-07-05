# pass.4

`pass` — CAM 应用程序直通驱动

## 名称

`pass`

## 概要

`device pass`

## 描述

`pass` 驱动为用户态应用程序提供了一种向内核发送 CAM CCB 的方式。

由于 `pass` 驱动允许直接访问 CAM 子系统，系统管理员在授予对此驱动的访问权限时应格外谨慎。如果使用不当，此驱动可能允许用户态应用程序使机器崩溃或导致数据丢失。

`pass` 驱动附加到系统中找到的每个 SCSI 和 ATA 设备。由于它附加到每个设备，因此提供了一种访问 SCSI 和 ATA 设备的通用方式，并允许用户访问没有与之关联的“标准”外设驱动程序的设备。

## 内核配置

内核中只需配置一个 `pass` 设备；`pass` 设备会在发现 SCSI 和 ATA 设备时自动分配。

## IOCTLS

**CAMIOCOMMAND** union ccb * 此 ioctl 接受大多数类型的 CAM CCB，并将它们传递给 CAM 传输层执行。注意，某些 CCB 类型不允许通过直通设备，必须通过 [xpt(4)](xpt.4.md) 设备发送。一些仅限 xpt 的 CCB 例子包括 XPT_SCAN_BUS、XPT_DEV_MATCH、XPT_RESET_BUS、XPT_SCAN_LUN、XPT_ENG_INQ 和 XPT_ENG_EXEC。这些 CCB 类型具有各种属性，使得通过直通接口为它们提供服务不合逻辑或不可能。如果用户希望内核进行错误恢复，必须在 CCB 上设置 `CAM_PASS_ERR_RECOVER` 标志，并将 retry_count 字段设置为重试次数。

**CAMGETPASSTHRU** union ccb * 此 ioctl 接受一个 XPT_GDEVLIST CCB，并返回与所讨论设备对应的直通设备。虽然此 ioctl 可通过 `pass` 驱动使用，但用途有限，因为如果调用者发出此 ioctl，他们必须已经知道所讨论的设备是直通设备。通过 [xpt(4)](xpt.4.md) 设备发出此 ioctl 可能更有用。

**CAMIOQUEUE** union ccb * 将 CCB 排队到 `pass` 驱动以异步执行。调用者可使用 select(2)、poll(2) 或 kevent(2) 在 CCB 完成时接收通知。此 ioctl 接受大多数 CAM CCB，但某些 CCB 类型不允许通过 pass 设备，必须通过 [xpt(4)](xpt.4.md) 设备发送。一些仅限 xpt 的 CCB 例子包括 XPT_SCAN_BUS、XPT_DEV_MATCH、XPT_RESET_BUS、XPT_SCAN_LUN、XPT_ENG_INQ 和 XPT_ENG_EXEC。这些 CCB 类型具有各种属性，使得通过直通接口为它们提供服务不合逻辑或不可能。虽然 `CAMIOQUEUE` ioctl 未定义为接受参数，但它确实需要一个指向 union ccb 的指针。不定义为接受参数是为了避免在通用 ioctl(2) 处理程序中进行额外的 malloc 和复制。已完成的 CCB 将通过 `CAMIOGET` ioctl 返回。仅当为请求分配内存或从用户态复制内存出错时，才会从 `CAMIOQUEUE` ioctl 返回错误。所有其他错误将作为标准 CAM CCB 状态错误报告。由于在 `CAMIOQUEUE` ioctl 中 CCB 不会从 pass 驱动复制回用户进程，因此用户传入的 CCB 不会被修改。即使对于立即 CCB 也是如此。相反，必须通过 `CAMIOGET` ioctl 检索已完成的 CCB 并检查其状态。任意时刻都可以通过 `CAMIOQUEUE` ioctl 排队多个 CCB，它们的完成顺序可能与提交顺序不同。调用者必须采取措施识别已排队和已完成的 CCB。struct ccb_hdr 内的 `periph_priv` 结构可供用户态在 `CAMIOQUEUE` 和 `CAMIOGET` ioctl 中使用，并会在调用间保留。此外，struct ccb_hdr 内的 periph_links 链表指针可供用户态在 `CAMIOQUEUE` 和 `CAMIOGET` ioctl 中使用，并会在调用间保留。如果用户希望内核进行错误恢复，必须在 CCB 上设置 `CAM_PASS_ERR_RECOVER` 标志，并将 retry_count 字段设置为重试次数。

**CAMIOGET** union ccb * 检索通过 `CAMIOQUEUE` ioctl 排队的已完成 CAM CCB。仅当 `pass` 驱动无法将数据复制到用户进程或没有可检索的已完成 CCB 时，才会从 `CAMIOGET` ioctl 返回错误。如果没有可检索的 CCB，errno 将设为 `ENOENT`。所有其他错误将作为标准 CAM CCB 状态错误报告。虽然 `CAMIOGET` ioctl 未定义为接受参数，但它确实需要一个指向 union ccb 的指针。不定义为接受参数是为了避免在通用 ioctl(2) 处理程序中进行额外的 malloc 和复制。当 CCB 完成时，pass 驱动将通过 select(2)、poll(2) 或 kevent(2) 报告。每次 `CAMIOGET` 调用可检索一个 CCB。CCB 的返回顺序可能与提交顺序不同。因此，调用者应使用 CCB 头中的 `periph_priv` 区域存储指向标识信息的指针。

## 文件

**`/dev/pass`** `n` `pass` 驱动的字符设备节点。通过 CAM 子系统访问的每个设备都应有一个对应的节点。

## 诊断

无。

## 参见

kqueue(2), poll(2), select(2), cam(3), cam_cdbparse(3), cam(4), [cd(4)](cd.4.md), [ctl(4)](ctl.4.md), [da(4)](da.4.md), [sa(4)](sa.4.md), [xpt(4)](xpt.4.md), [camcontrol(8)](../man8/camcontrol.8.md), camdd(8)

## 历史

CAM 直通驱动最早出现于 FreeBSD 3.0。

## 作者

Kenneth Merry <ken@FreeBSD.org>
