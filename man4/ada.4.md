# ada.4

`ada` — ATA 直接访问设备驱动

## 名称

`ada`

## 概要

`device ada`

## 描述

`ada` 驱动支持直接访问设备，这些设备实现 ATA 命令协议，并通过 CAM 子系统支持的主机适配器连接到系统。

在配置 ATA 直接访问设备之前，主机适配器也必须单独配置进系统。

## 命令排队

命令排队允许设备并发处理多个事务，通常会重新排序以减少寻道次数和长度。ATA 定义了两种排队类型：TCQ（Tagged Command Queuing，PATA 传统方式）和 NCQ（Native Command Queuing，SATA）。`ada` 设备驱动在受支持时充分利用 NCQ。距离当前磁头位置较远的介质区域的访问可能因持续处理更近的请求而无限期推迟。为确保此类访问及时完成，设备连续运行期间每 7 秒发送一个有序事务。

## 缓存效果

许多直接访问设备配备了读缓存和/或写缓存。影响设备缓存的参数保存在设备 IDENTIFY 数据中，可通过 [camcontrol(8)](../man8/camcontrol.8.md) 工具查看和修改。

读缓存用于存储设备发起的预读操作数据以及常用数据。读缓存对用户透明，启用不会产生任何不良影响。大多数带读缓存的设备出厂时即已启用。

写缓存可大幅降低写操作延迟，并允许设备重新组织写入以提高效率和性能。这种性能提升是有代价的。如果设备在缓存中仍包含未提交的写操作时断电，这些写入将丢失。写事务丢失对文件系统的影响不确定，可能导致损坏。大多数设备会对写事务进行老化处理，将风险限制在最近报告为完成的少数事务上，但仍然建议启用写缓存设备的系统配备不间断电源（UPS）。`ada` 设备驱动确保在设备最终关闭或意外关机（panic）事件时缓存和介质同步。这样一旦操作系统报告已停止，即可安全断电。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`kern.cam.ada.retry_count`** 此变量决定 `ada` 驱动对 READ 或 WRITE 命令重试的次数。这不影响探测期间或 `ada` 驱动转储例程使用的重试次数。此值当前默认为 4。

**`kern.cam.ada.default_timeout`** 此变量决定 `ada` 驱动在使未完成命令超时之前等待的时间。此值的单位为秒，当前默认为 30 秒。

**`kern.cam.ada.spindown_shutdown`** 此变量决定关机时是否停转磁盘。设置为 1 启用停转，0 禁用。当前默认启用。

**`kern.cam.sort_io_queue`**

**`kern.cam.ada.`** `X``.sort_io_queue` 这些变量决定是否对请求队列进行排序以尝试优化磁头寻道。设置为 1 启用排序，0 禁用，-1 保持原样。默认对 HDD 启用排序，对 SSD 禁用。

**`kern.cam.ada.read_ahead`**

**`kern.cam.ada.`** `X``.read_ahead`

**`kern.cam.ada.write_cache`**

**`kern.cam.ada.`** `X``.write_cache` 这些变量决定是全局、按设备启用还是禁用设备预读和写缓存。设置为 1 启用写缓存，0 禁用，-1 保持原样。运行时修改的值仅在设备重置后生效（使用 [camcontrol(8)](../man8/camcontrol.8.md) 的 reset 子命令）。因此，此设置应在 **`/boot/loader.conf`** 而非 **`/etc/sysctl.conf`** 中更改。全局默认当前为 1。按设备默认为保持原样（遵循全局设置）。

## 文件

**`/dev/ada*`** ATA 设备节点

## 参见

[ahci(4)](ahci.4.md), cam(4), [da(4)](da.4.md), [mvs(4)](mvs.4.md), [nda(4)](nda.4.md), [siis(4)](siis.4.md)

## 历史

`ada` 驱动首次出现于 FreeBSD 8.0。

## 作者

Alexander Motin <mav@FreeBSD.org>
