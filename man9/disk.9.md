# disk(9)

`disk` — 内核磁盘存储 API

## 名称

`disk`

## 概要

```c
#include <geom/geom_disk.h>

struct disk *
disk_alloc(void);

void
disk_create(struct disk *disk, int version);

void
disk_gone(struct disk *disk);

void
disk_destroy(struct disk *disk);

int
disk_resize(struct disk *disk, int flags);

void
disk_add_alias(struct disk *disk, const char *alias);
```

## 描述

磁盘存储 API 允许提供对类磁盘存储设备访问的内核设备驱动程序向其他内核组件（包括 [GEOM(4)](../man4/geom.4.md) 和 [devfs(4)](../man4/devfs.4.md)）通告该设备。

每个磁盘设备由一个 `struct disk` 结构描述，其中包含磁盘设备的各种参数、可在设备上执行的各种方法的函数指针，以及设备驱动程序的私有数据存储。此外，某些字段保留供 GEOM 用于管理对设备的访问及其统计信息。

GEOM 拥有 `struct disk` 的所有权，驱动程序必须使用 `disk_alloc` 函数为其分配存储，填充各字段，并在设备准备好服务请求时调用 `disk_create`。`disk_add_alias` 为磁盘添加别名，必须在 `disk_create` 之前调用，但可以多次调用。对于添加的每个别名，将使用 [make_dev_alias(9)](make_dev_alias.9.md) 创建一个设备节点，方式与使用 [make_dev(9)](make_dev.9.md) 为 `d_name` 和 `d_unit` 创建主设备节点相同。应注意确保只有 一个驱动程序为任何给定名称创建别名。驱动程序在修改 `d_mediasize` 后可以调用 `disk_resize` 通知 GEOM 磁盘容量变化。`flags` 字段应设置为 M_WAITOK 或 M_NOWAIT。`disk_gone` 孤立与驱动器关联的所有 provider，在每个 provider 中设置 ENXIO 错误条件。此外，如果 provider 中已设置错误条件，它还会阻止在最后一次关闭写入时重新 taste。调用 `disk_destroy` 后，设备驱动程序不得再访问 `struct disk` 的内容。

`disk_create` 函数接受第二个参数 `version`，必须始终传入 `DISK_VERSION`。如果 GEOM 检测到驱动程序是针对不支持的版本编译的，它会忽略该设备并在控制台上打印警告。

### 描述性字段

以下字段标识由该结构实例描述的磁盘设备，必须在将结构提交给 `disk_create` 之前填入，且之后不得更改：

**`u_int`** `d_flags` 可选标志，向存储框架指示存储设备驱动程序支持哪些可选特性或描述。目前支持的标志有 `DISKFLAG_OPEN`（由存储框架维护）、`DISKFLAG_CANDELETE`（由设备驱动程序维护）和 `DISKFLAG_CANFLUSHCACHE`（由设备驱动程序维护）。

**`const char *`** `d_name` 持有存储设备类的名称，例如 "`ahd`"。此值通常唯一标识一个特定的驱动程序设备，且不得与其他设备驱动程序服务的设备冲突。

**`u_int`** `d_unit` 持有存储设备类的实例，例如 "`4`"。此命名空间由设备驱动程序管理，单元号的分配可能是探测顺序的属性，或在某些情况下是拓扑的属性。`d_name` 和 `d_unit` 的值一起唯一标识一个磁盘存储设备。

### 磁盘设备方法

以下字段标识各种磁盘设备方法（若实现）：

**`disk_open_t *`** `d_open` 可选：在磁盘设备被打开时调用。若未提供方法，open 将始终成功。

**`disk_close_t *`** `d_close` 可选：在磁盘设备被关闭时调用。虽然可以返回错误码，但该调用应始终终止由相应 open 方法调用建立的任何状态。

**`disk_strategy_t *`** `d_strategy` 必需：在磁盘设备上要启动新的 `struct bio` 时调用。

**`disk_ioctl_t *`** `d_ioctl` 可选：在磁盘设备上启动 I/O 控制操作时调用。请注意，出于安全原因，这些操作不应能够影响执行操作设备以外的其他设备。

**`dumper_t *`** `d_dump` 可选：如果通过 [dumpon(8)](../man8/dumpon.8.md) 配置，此函数在内核 panic 后从非常受限的系统状态中被调用，以将系统 RAM 的副本记录到磁盘。

**`disk_getattr_t *`** `d_getattr` 可选：如果提供此方法，它使磁盘驱动程序有机会覆盖 GEOM 对 BIO_GETATTR 请求的默认响应。如果未处理该属性，此函数应返回 -1；如果已处理该属性，返回 0；或返回一个 errno 传递给 `g_io_deliver`。

**`disk_gone_t *`** `d_gone` 可选：如果提供此方法，它将在调用 `disk_gone` 后、GEOM 完成其清理过程后被调用。一旦调用此回调，磁盘驱动程序就可以安全地释放其所有资源，因为它不会再从 GEOM 接收进一步的调用。

### 必需的介质属性

以下字段标识磁盘设备的大小和粒度。这些字段从驱动程序 open 方法返回到 close 方法被调用期间必须保持稳定，但在 open 方法返回之前修改它们是完全合法的。

**`u_int`** `d_sectorsize` 磁盘设备的扇区大小（字节）。

**`off_t`** `d_mediasize` 磁盘设备的大小（字节）。

**`u_int`** `d_maxsize` I/O 请求的最大支持大小（字节）。大于此大小的请求会被 GEOM 切分。

### 可选介质属性

这些可选字段可以提供有关磁盘设备的额外信息。如果字段/概念不适用，请勿初始化这些字段。这些字段从驱动程序 open 方法返回到 close 方法被调用期间必须保持稳定，但在 open 方法返回之前修改它们是完全合法的。

**`u_int`** `d_fwsectors`, **`u_int`** `d_fwheads` 固件或 BIOS 在磁盘设备上通告的扇区数和磁头数。这些值几乎普遍是虚假的，但在某些架构上对于正确计算磁盘分区是必要的。

**`u_int`** `d_stripeoffset`, **`u_int`** `d_stripesize` 这两个字段可用于描述大多数磁盘技术的自然性能边界的宽度和位置。详见 `src/sys/geom/notes`。

**`char`** `d_ident[DISK_IDENT_SIZE]` 如果上面描述的 d_getattr 方法未实现，或不支持 GEOM::ident 属性，此字段可以也应该用于存储磁盘序列号。

**`char`** `d_descr[DISK_IDENT_SIZE]` 此字段可用于存储磁盘供应商和产品描述。

**`uint16_t`** `d_hba_vendor` 此字段可用于存储连接到磁盘的 HBA 的 PCI 供应商 ID。

**`uint16_t`** `d_hba_device` 此字段可用于存储连接到磁盘的 HBA 的 PCI 设备 ID。

**`uint16_t`** `d_hba_subvendor` 此字段可用于存储连接到磁盘的 HBA 的 PCI 子供应商 ID。

**`uint16_t`** `d_hba_subdevice` 此字段可用于存储连接到磁盘的 HBA 的 PCI 子设备 ID。

### 驱动程序私有数据

此字段可由设备驱动程序用于存储指向私有数据的指针，以实现磁盘服务。

**`void *`** `d_drv1` 私有数据指针。通常用于存储指向此磁盘设备驱动程序 `softc` 结构的指针。

## 参见

[devfs(4)](../man4/devfs.4.md), [GEOM(4)](../man4/geom.4.md)

## 历史

`kernel` 磁盘存储 API 最早出现于 FreeBSD 4.9。

## 作者

本手册页由 Robert Watson 编写。

## 缺陷

磁盘别名不是一种通用别名机制，仅用于简化从一个名称到另一个名称的过渡。它们可用于确保 nvd0 和 nda0 是同一个东西。它们不能用于实现 macOS 中的 diskX 概念。
