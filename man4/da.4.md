# da(4)

`da` — SCSI 直接访问设备驱动

## 名称

`da`

## 概要

`device da`

## 描述

`da` 驱动支持所有直接访问类 SCSI 设备，这些设备通过受支持的 SCSI 主适配器连接到系统。直接访问类包括磁盘、磁光和固态设备。

在配置 SCSI 直接访问设备之前，还必须单独将 SCSI 主适配器配置到系统中。

## 缓存效果

许多直接访问设备配备有读缓存和/或写缓存。影响设备缓存的参数存储在模式页 8，即缓存控制页中。可通过 [camcontrol(8)](../man8/camcontrol.8.md) 工具检查和修改模式页。

读缓存用于存储设备发起的预读操作数据以及常用数据。读缓存对用户透明，可无不良影响地启用。大多数带读缓存的设备在出厂时即已启用。可通过在缓存控制模式页中设置 RCD（Read Cache Disable，禁用读缓存）位来禁用读缓存。

写缓存可大幅降低写操作的延迟，并允许设备重新组织写入以提高效率和性能。这种性能提升是有代价的。如果设备在缓存中包含未提交的写操作时断电，这些写入将丢失。丢失写事务对文件系统的影响不确定，可能导致损坏。大多数设备会对写事务进行老化处理，将风险限制在最近报告为完成的少数事务上，但仍建议配备写缓存设备的系统使用不间断电源（UPS）。`da` 设备驱动确保在设备最终关闭或意外关机（panic）事件时缓存和介质同步。这样一旦操作系统报告已停止，即可安全断电。可通过在缓存控制模式页中设置 WCE（Write Cache Enable，启用写缓存）位来启用写缓存。

## 标记队列

`da` 设备驱动会充分利用名为标记队列的 SCSI 特性。标记队列允许设备并发处理多个事务，并经常重新排序以减少寻道的次数和长度。介质较远部分的事务可能因服务更接近当前磁头位置的请求而无限期推迟。为确保此类事务及时完成，设备持续操作期间每 15 秒发送一个有序标记事务。

## 坏块恢复

直接访问设备能映射出缺陷介质部分。介质恢复参数位于模式页 1，即读写错误恢复模式页中。最重要的介质重映射功能是"自动写入重分配"和"自动读取重分配"，可分别通过读写错误恢复页的 AWRE 和 ARRE 位启用。许多设备在出厂时未启用这些功能。可通过 [camcontrol(8)](../man8/camcontrol.8.md) 工具检查和修改模式页。

## 内核配置

只需显式配置一个 `da` 设备；数据结构会在 SCSI 总线上发现磁盘时动态分配。

## sysctl 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**ATA_TRIM** 通过 ATA COMMAND PASS THROUGH 命令进行 ATA TRIM，

**UNMAP** UNMAP 命令，

**WS16** 带 UNMAP 标志的 WRITE SAME(16) 命令，

**WS10** 带 UNMAP 标志的 WRITE SAME(10) 命令，

**ZERO** 不带 UNMAP 标志的 WRITE SAME(10) 命令，

**DISABLE** 禁用 BIO_DELETE 支持。

**`kern.cam.da.default_timeout`** 此变量决定 `da` 驱动在超时未完成命令之前等待的时间。此值的单位为秒，当前默认为 60 秒。

**`kern.cam.da.disable_wp_protection`** 禁用写保护磁盘检测。默认为禁用（即启用写保护磁盘检测）。

**`kern.cam.da.enable_biospeedup`** 启用 `BIO_SPEEDUP` 处理。默认为启用。

**`kern.cam.da.enable_uma_ccbs`** 为 CCB 使用 UMA。默认为启用。

**`kern.cam.da.poll_period`** 介质轮询周期，单位为秒。默认为 3 秒。

**`kern.cam.da.retry_count`** 此变量决定 `da` 驱动重试 READ 或 WRITE 命令的次数。这不会影响探测期间或 `da` 驱动转储例程使用的重试次数。此值当前默认为 4。

**`kern.cam.da.send_ordered`** 发送有序标记。在关机时，遍历所有 `da` 外围驱动，如果设备仍处于打开状态，则将磁盘同步到物理介质。默认为启用。

**`kern.cam.sort_io_queue`**

**`kern.cam.da`** .`X``.sort_io_queue` 这些变量决定是否应对请求队列进行排序以优化磁头寻道。设为 1 启用排序，0 禁用，-1 保持原样。默认对 HDD 启用排序，对 SSD 禁用排序。

**`kern.cam.da`** .`X``.delete_method` 此变量指定处理 BIO_DELETE 请求的方法：

**`kern.cam.da`** .`X``.minimum_cmd_size` 此变量决定给定 `da` 单元的最小 READ/WRITE CDB 大小。有效的最小命令大小值为 6、10、12 和 16 字节。默认为 6 字节。`da` 驱动在探测时发出 CAM Path Inquiry CCB，以确定相关设备所使用的协议（如 ATAPI）是否通常不允许 6 字节命令。如果不允许，`da` 驱动将默认使用至少 10 字节的 CDB。如果 6 字节的 READ 或 WRITE 因 ILLEGAL REQUEST 错误失败，`da` 驱动将把该设备的默认 CDB 大小增加到 10 字节并重试命令。CDB 大小始终选择为能满足指定最小命令大小以及所讨论的 READ 或 WRITE 的 LBA 和长度的最小 READ/WRITE CDB。（例如，向大于 2^32 的 LBA 写入将需要 16 字节的 CDB。）

## 注释

如果设备失效（介质移除、设备变得无响应），磁盘标签和内核中保存的关于该设备的信息即作废。为避免损坏新插入的介质或替换设备，对该设备的所有访问都会丢弃，直到引用旧设备的最后一个文件描述符关闭。在此期间，所有新的打开尝试都会拒绝。

## 文件

**`/dev/da*`** SCSI 磁盘设备节点

## 诊断

无。

## 参见

[ada(4)](ada.4.md), cam(4), [geom(4)](geom.4.md), [nda(4)](nda.4.md), [gpart(8)](../man8/gpart.8.md)

## 历史

`da` 驱动由 Justin T. Gibbs 为 CAM SCSI 子系统编写。许多思想取自由 Julian Elischer 从 Mach 2.5 编写并移植的 `sd` 设备驱动。
