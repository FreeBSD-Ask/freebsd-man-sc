# devstat.9

`devstat` — 用于保持设备统计信息的内核接口

## 名称

`devstat`, `devstat_end_transaction`, `devstat_end_transaction_bio`, `devstat_end_transaction_bio_bt`, `devstat_new_entry`, `devstat_remove_entry`, `devstat_start_transaction`, `devstat_start_transaction_bio`

## 概要

```c
#include <sys/devicestat.h>

struct devstat *
devstat_new_entry(const void *dev_name, int unit_number, uint32_t block_size,
    devstat_support_flags flags, devstat_type_flags device_type,
    devstat_priority priority);

void
devstat_remove_entry(struct devstat *ds);

void
devstat_start_transaction(struct devstat *ds, const struct bintime *now);

void
devstat_start_transaction_bio(struct devstat *ds, struct bio *bp);

void
devstat_end_transaction(struct devstat *ds, uint32_t bytes,
    devstat_tag_type tag_type, devstat_trans_flags flags,
    const struct bintime *now, const struct bintime *then);

void
devstat_end_transaction_bio(struct devstat *ds, const struct bio *bp);

void
devstat_end_transaction_bio_bt(struct devstat *ds, const struct bio *bp,
    const struct bintime *now);
```

## 描述

devstat 子系统顾名思义是一个用于记录设备统计信息的接口。其设计理念是在使用最少 CPU 时间记录统计信息的同时，保持较为详细的统计数据。因此，`devstat` 代码的内核部分实际上不执行任何统计计算，而是将计算留给用户程序处理。

历史上的旧式 `devstat` 模型假设每个设备仅有一个活动的 IO 操作，这对于 2000 年代及以后的大多数类磁盘驱动程序来说是不准确的。该接口的新使用者几乎肯定应该只使用 start 和 end transaction 例程的 "bio" 变体。

`devstat_new_entry` 分配并初始化 `devstat` 结构，返回指向它的指针。`devstat_new_entry` 接受几个参数：

**dev_name** 设备名称，例如 da、cd、sa。

**unit_number** 设备单元号。

**block_size** 设备的块大小（若支持）。如果设备不支持块大小，或在设备被添加到 `devstat` 列表时块大小未知，应设置为 0。

**flags** 指示设备支持或不支持哪些操作的标志。详见下文。

**device_type** 设备类型。分为三个部分：基本设备类型（例如，直接访问、CDROM、顺序访问）、接口类型（IDE、SCSI 或其他），以及用于指示 pass-through 设备的 pass-through 标志。完整类型列表见下文。

**priority** 设备优先级。优先级用于确定设备在 `devstat` 设备列表中的排序方式。设备首先按优先级排序（从高到低），然后按 attach 顺序排序。可用优先级的完整列表见下文。

`devstat_remove_entry` 从 `devstat` 子系统中移除一个设备。它以相关设备的 devstat 结构作为参数。`devstat` 生成号会递增，设备数量会递减。

`devstat_start_transaction` 向 `devstat` 子系统注册一个事务的开始。可选地，如果调用者已有可用的 `binuptime` 值，可以通过 `*now` 传入。通常调用者可以为 `now` 传入 `NULL`，例程会自行收集当前的 `binuptime`。每次事务开始时 busy 计数会递增。当设备从空闲转为 busy 时，系统正常运行时间会被记录到 `devstat` 结构的 `busy_from` 字段中。

`devstat_start_transaction_bio` 将 `binuptime` 记录到所提供 bio 的 `bio_t0` 中，然后调用 `devstat_start_transaction`。

`devstat_end_transaction` 向 `devstat` 子系统注册一个事务的结束。它接受六个参数：

**ds** 相关设备的 `devstat` 结构。

**bytes** 本次事务传输的字节数。

**tag_type** 事务标签类型。标签类型见下文。

**flags** 事务标志，指示事务是读取、写入，还是未传输任何数据。

**now** 事务结束时的 `binuptime`，或 `NULL`。

**then** 事务开始时的 `binuptime`，或 `NULL`。

若 `now` 为 `NULL`，会从 `binuptime` 收集当前时间。若 `then` 为 `NULL`，该操作不会在 `devstat` 的 `duration` 表中跟踪。

`devstat_end_transaction_bio` 是 `devstat_end_transaction_bio_bt` 的薄封装，`now` 参数为 `NULL`。

`devstat_end_transaction_bio_bt` 是 `devstat_end_transaction` 的封装，从由 `devstat_start_transaction_bio` 准备的 `struct bio` 中提取所有所需信息。该 bio 必须已准备好供 `biodone` 使用（即 `bio_bcount` 和 `bio_resid` 必须被正确初始化）。

`devstat` 结构由以下字段组成：

**sequence0**, **sequence1** 用于收集一致设备统计快照的实现细节。

**start_count** 已开始的操作数。

**end_count** 已完成的操作数。"busy_count" 可以通过从 `start_count` 减去 `end_count` 计算得到。（`sequence0` 和 `sequence1` 用于获取一致的快照。）这是该设备当前未完成事务的数量。该值不应低于零，空闲设备上应为零。若上述任一条件不成立，则表明存在问题。每个事务应有一个且仅有一个事务开始事件和一个事务结束事件。

**dev_links** 每个 `devstat` 结构在注册时会被放入一个链表。`dev_links` 字段包含指向 `devstat` 结构列表中下一个条目的指针。

**device_number** 设备号是每个设备的唯一标识符。每注册一个新设备，设备号就递增一次。设备号目前只是一个 32 位整数，但如果某人的系统有超过四十亿次设备到达事件，可以对其进行扩展。

**device_name** 设备名是由注册驱动程序给出的用于标识自身的文本字符串。（例如 "da"、"cd"、"sa" 等。）

**unit_number** 单元号标识所讨论的外设驱动程序的特定实例。

**bytes[4]** 此数组包含已读取（索引 `DEVSTAT_READ`）、写入（索引 `DEVSTAT_WRITE`）、释放或擦除（索引 `DEVSTAT_FREE`）或其他（索引 `DEVSTAT_NO_DATA`）的字节数。所有值均为无符号 64 位整数。

**operations[4]** 此数组包含已执行的给定类型的操作数。索引与上述 `bytes` 的索引相同。`DEVSTAT_NO_DATA` 或 "其他" 表示既不是读取、写入也不是释放的事务数。例如，SCSI 驱动程序经常向 SCSI 设备发送 test unit ready 命令。test unit ready 命令不读取或写入任何数据，只是让设备返回其状态。

**duration[4]** 此数组包含与已完成给定类型操作相对应的总 bintime。索引与上述 `bytes` 的索引相同。（使用历史 `devstat_end_transaction` API 完成且未提供非 NULL `then` 的操作不计入。）

**busy_time** 设备 busy 计数大于零的总时间。仅在 busy 计数归零时更新。

**creation_time** 由 `getmicrotime` 报告的设备注册时间。

**block_size** 设备的块大小（若设备有块大小）。

**tag_types** 这是一个计数器数组，用于记录发送到设备的各种标签类型的数量。标签类型列表见下文。

**busy_from** 若设备不 busy，这是上一个事务完成的时间。若设备 busy，这是设备变为 busy 的时间或上一个事务完成的时间中较近的一个。

**flags** 这些标志指示特定设备支持哪些统计测量。这些标志主要用作解读统计信息的用户态程序的辅助。

**device_type** 这是设备类型。它由三部分组成：设备类型（例如，直接访问、CDROM、顺序访问等）、接口（IDE、SCSI 或其他）以及所讨论的设备是否为 pass-through 驱动程序。完整设备类型列表见下文。

**priority** 这是优先级。这是用于确定在 `devstat` 列表中插入设备位置的第一个参数。第二个参数是 attach 顺序。可用优先级列表见下文。

**id** GEOM 节点的标识。

每个设备都被赋予一个设备类型。Pass-through 设备具有与其所提供接口的设备相同的基础设备类型和接口，但它们还设置了 pass-through 标志。基本设备类型与 SCSI 设备类型号相同，因此对于 SCSI 外设，从 inquiry 返回的设备类型通常会与 SCSI 接口类型和（如果适用）pass-through 标志进行 OR 运算。设备类型标志如下：

```c
typedef enum {
	DEVSTAT_TYPE_DIRECT	= 0x000,
	DEVSTAT_TYPE_SEQUENTIAL	= 0x001,
	DEVSTAT_TYPE_PRINTER	= 0x002,
	DEVSTAT_TYPE_PROCESSOR	= 0x003,
	DEVSTAT_TYPE_WORM	= 0x004,
	DEVSTAT_TYPE_CDROM	= 0x005,
	DEVSTAT_TYPE_SCANNER	= 0x006,
	DEVSTAT_TYPE_OPTICAL	= 0x007,
	DEVSTAT_TYPE_CHANGER	= 0x008,
	DEVSTAT_TYPE_COMM	= 0x009,
	DEVSTAT_TYPE_ASC0	= 0x00a,
	DEVSTAT_TYPE_ASC1	= 0x00b,
	DEVSTAT_TYPE_STORARRAY	= 0x00c,
	DEVSTAT_TYPE_ENCLOSURE	= 0x00d,
	DEVSTAT_TYPE_FLOPPY	= 0x00e,
	DEVSTAT_TYPE_MASK	= 0x00f,
	DEVSTAT_TYPE_IF_SCSI	= 0x010,
	DEVSTAT_TYPE_IF_IDE	= 0x020,
	DEVSTAT_TYPE_IF_OTHER	= 0x030,
	DEVSTAT_TYPE_IF_NVME	= 0x040,
	DEVSTAT_TYPE_IF_MASK	= 0x0f0,
	DEVSTAT_TYPE_PASS	= 0x100
} devstat_type_flags;
```

设备有一个关联的优先级，大致控制其在 `devstat` 列表中的放置位置。优先级如下：

```c
typedef enum {
	DEVSTAT_PRIORITY_MIN	= 0x000,
	DEVSTAT_PRIORITY_OTHER	= 0x020,
	DEVSTAT_PRIORITY_PASS	= 0x030,
	DEVSTAT_PRIORITY_FD	= 0x040,
	DEVSTAT_PRIORITY_WFD	= 0x050,
	DEVSTAT_PRIORITY_TAPE	= 0x060,
	DEVSTAT_PRIORITY_CD	= 0x090,
	DEVSTAT_PRIORITY_DISK	= 0x110,
	DEVSTAT_PRIORITY_ARRAY	= 0x120,
	DEVSTAT_PRIORITY_MAX	= 0xfff
} devstat_priority;
```

每个设备都有关联的标志，用于指示支持或不支持哪些操作。`devstat_support_flags` 的值如下：

**DEVSTAT_ALL_SUPPORTED** 设备支持每种统计类型。

**DEVSTAT_NO_BLOCKSIZE** 此设备没有块大小。

**DEVSTAT_NO_ORDERED_TAGS** 此设备不支持 ordered 标签。

**DEVSTAT_BS_UNAVAILABLE** 此设备支持块大小，但当前不可用。此标志最常用于可移动介质驱动器。

到设备的事务分为三类，在传入 `devstat_end_transaction` 的 `flags` 中表示。事务类型如下：

```c
typedef enum {
	DEVSTAT_NO_DATA	= 0x00,
	DEVSTAT_READ	= 0x01,
	DEVSTAT_WRITE	= 0x02,
	DEVSTAT_FREE	= 0x03
} devstat_trans_flags;
#define DEVSTAT_N_TRANS_FLAGS   4
```

DEVSTAT_NO_DATA 是既非读取也非写入的设备事务类型。例如，SCSI 驱动程序经常向 SCSI 设备发送 test unit ready 命令。test unit ready 命令不读取或写入任何数据，只是让设备返回其状态。

`devstat_end_transaction` 的 `tag_type` 参数有四个可能值：

**DEVSTAT_TAG_SIMPLE** 事务带有 simple 标签。

**DEVSTAT_TAG_HEAD** 事务带有 head of queue 标签。

**DEVSTAT_TAG_ORDERED** 事务带有 ordered 标签。

**DEVSTAT_TAG_NONE** 设备不支持标签。

标签类型值对应于 SCSI 标签定义的低四位。例如在 CAM 中，CCB 的 `tag_action` 与 0xf 进行 OR 运算以确定传入 `devstat_end_transaction` 的标签类型。

`#include <sys/devicestat.h>` 中定义了一个宏 `DEVSTAT_VERSION`。这是 `devstat` 子系统的当前版本，每次做出需要重新编译访问 `devstat` 统计信息的用户态程序的更改时，都应递增此版本号。用户态程序通过 `kern.devstat.version` `sysctl` 变量使用此版本号，以确定它们是否与内核 `devstat` 结构同步。

## 参见

[systat(1)](../man1/systat.1.md), [devstat(3)](../man3/devstat.3.md), [iostat(8)](../man8/iostat.8.md), [rpc.rstatd(8)](../man8/rpc.rstatd.8.md), [vmstat(8)](../man8/vmstat.8.md)

## 历史

`devstat` 统计系统出现于 FreeBSD 3.0。

## 作者

Kenneth Merry <ken@FreeBSD.org>

## 缺陷

某些 `devstat` 列表操作代码周围可能需要 `spl` 保护，以确保例如在有人获取 `kern.devstat.all` `sysctl` 变量时设备列表不会被更改。
