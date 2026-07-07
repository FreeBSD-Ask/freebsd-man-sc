# devstat(3)

`devstat` — 设备统计实用程序库

## 名称

`devstat`, `devstat_getnumdevs`, `devstat_getgeneration`, `devstat_getversion`, `devstat_checkversion`, `devstat_getdevs`, `devstat_selectdevs`, `devstat_buildmatch`, `devstat_compute_statistics`, `devstat_compute_etime`

## 库

libdevstat

## 概要

`#include <devstat.h>`

```c
int
devstat_getnumdevs(kvm_t *kd);

long
devstat_getgeneration(kvm_t *kd);

int
devstat_getversion(kvm_t *kd);

int
devstat_checkversion(kvm_t *kd);

int
devstat_getdevs(kvm_t *kd, struct statinfo *stats);

int
devstat_selectdevs(struct device_selection **dev_select, int *num_selected,
    int *num_selections, long *select_generation, long current_generation,
    struct devstat *devices, int numdevs, struct devstat_match *matches,
    int num_matches, char **dev_selections, int num_dev_selections,
    devstat_select_mode select_mode, int maxshowdevs, int perf_select);

int
devstat_buildmatch(char *match_str, struct devstat_match **matches,
    int *num_matches);

int
devstat_compute_statistics(struct devstat *current, struct devstat *previous,
    long double etime, ...);

long double
devstat_compute_etime(struct bintime *cur_time, struct bintime *prev_time);
```

## 描述

`devstat` 库是用于处理内核 [devstat(9)](../man9/devstat.9.md) 接口的辅助函数库，用户可通过 [sysctl(3)](../gen/sysctl.3.md) 和 [kvm(3)](kvm.3.md) 访问该接口。所有以 `kvm_t *` 作为第一个参数的函数都可以传递 `NULL` 而不是 kvm 句柄作为此参数，这将导致通过 [sysctl(3)](../gen/sysctl.3.md) 读取数据。否则，使用提供的句柄通过 [kvm(3)](kvm.3.md) 读取。`devstat_checkversion()` 函数应该对每个将要使用的 kvm 句柄调用一次（如果使用 [sysctl(3)](../gen/sysctl.3.md) 则传递 `NULL`）。

`devstat_getnumdevs()` 函数返回内核中向 `devstat` 子系统注册的设备数量。

`devstat_getgeneration()` 函数返回内核中 `devstat` 设备列表的当前世代号。

`devstat_getversion()` 函数返回当前内核的 `devstat` 版本。

`devstat_checkversion()` 函数将用户空间的 `devstat` 版本与内核的 `devstat` 版本进行比较。如果两者相同，返回零。否则，在 `devstat_errbuf` 中打印适当的错误消息并返回 -1。

`devstat_getdevs()` 函数将当前设备列表和统计信息提取到提供的 `statinfo` 结构中。`statinfo` 结构可以在

`#include <devstat.h>`

```c
struct statinfo {
	long            cp_time[CPUSTATES];
	long            tk_nin;
	long            tk_nout;
	struct devinfo  *dinfo;
	long double     snap_time;
};
```

中找到。`devstat_getdevs()` 函数期望 `statinfo` 结构已被分配，并且期望 `dinfo` 子元素在首次调用 `devstat_getdevs()` 之前已被分配并清零。`dinfo` 子元素用于在调用之间存储状态，在首次调用 `devstat_getdevs()` 之后不应修改。`dinfo` 子元素包含以下成员：

```c
struct devinfo {
	struct devstat	*devices;
	uint8_t		*mem_ptr;
	long		generation;
	int		numdevs;
};
```

`kern.devstat.all` [sysctl(8)](../man8/sysctl.8.md) 变量包含一个 `devstat` 结构数组，但在数组头部是当前 `devstat` 世代号。世代号位于缓冲区头部的原因是，访问 `devstat` 统计信息的用户空间软件可以原子性地同时获取统计信息和相应的世代号。如果客户端软件被迫通过单独的 [sysctl(8)](../man8/sysctl.8.md) 变量（为方便起见而提供）获取世代号，则设备列表可能会在客户端获取世代号和获取设备列表之间发生变化。

`devinfo` 结构的 `mem_ptr` 子元素是由 `devstat_getdevs()` 分配并在必要时调整大小的内存指针。`devinfo` 结构的 devices 子元素基本上是指向 `kern.devstat.all` [sysctl(8)](../man8/sysctl.8.md) 变量（或通过 [kvm(3)](kvm.3.md) 读取的相应值）中 devstat 结构数组开头的指针。`devinfo` 结构的 generation 子元素包含相应的世代号。`devinfo` 结构的 `numdevs` 子元素包含当前向内核 `devstat` 子系统注册的设备数量。

`devstat_selectdevs()` 函数根据多种条件选择要显示的设备：

**指定的**设备 指定的设备是第一选择优先级。这些通常是用户按名称指定的设备，例如 `da0`, `da1`, `cd0`。

**匹配**模式 这些是由 `devstat_buildmatch()` 从用户输入生成的模式匹配表达式。

**性能** 如果启用了性能模式，设备将根据传递给 `devstat_selectdevs()` 的 `device_selection` 结构中的 `bytes` 字段排序。`bytes` 值目前必须由用户维护。将来，这可能会在 `devstat` 库例程中为用户完成。如果没有按名称或模式选择设备，性能跟踪代码将选择系统中的每个设备，并按性能排序。如果已按名称或模式选择设备，性能跟踪代码将遵守这些选择，仅在所选设备中排序。

**devstat 列表中的**顺序 如果选择模式设置为 `DS_SELECT_ADD`，并且所选设备仍少于 `maxshowdevs` 个，`devstat_selectdevs()` 将自动选择最多 `maxshowdevs` 个设备。

`devstat_selectdevs()` 函数以四种不同模式执行选择：

**`DS_SELECT_ADD`** 在“添加”模式下，`devstat_selectdevs()` 将选择按名称或匹配模式指定的任何未选设备。它还会按 devstat 列表顺序选择更多设备，直到所选设备数量等于 `maxshowdevs` 或所有设备都被选中。

**`DS_SELECT_ONLY`** 在“仅”模式下，`devstat_selectdevs()` 将清除所有当前选择，并仅选择按名称或匹配模式指定的设备。

**`DS_SELECT_REMOVE`** 在“移除”模式下，`devstat_selectdevs()` 将移除按名称或匹配模式指定的设备。它不会选择任何额外设备。

**`DS_SELECT_ADDONLY`** 在“仅添加”模式下，`devstat_selectdevs()` 将选择按名称或匹配模式指定的任何未选设备。在此方面，它与“添加”模式相同。但是，它不会选择指定设备以外的任何设备。

在所有选择模式下，`devstat_selectdevs()` 不会选择超过 `maxshowdevs` 个设备。一个例外是当你处于“top”模式且未选择任何设备时。在这种情况下，`devstat_selectdevs()` 将选择系统中的每个设备。客户端程序在决定是否关注特定设备时必须注意选择顺序。这可能是错误的行为，可能需要进一步思考。

`devstat_selectdevs()` 函数处理客户端传入的 `dev_select` 结构的分配和调整大小。`devstat_selectdevs()` 函数使用 `numdevs` 和 `current_generation` 字段来跟踪当前 `devstat` 世代号和设备数量。如果 `num_selections` 与 `numdevs` 不同，或者 `select_generation` 与 `current_generation` 不同，`devstat_selectdevs()` 将根据需要调整选择列表的大小，并重新初始化选择数组。

`devstat_buildmatch()` 函数接受以逗号分隔的匹配字符串，并将其编译为 `devstat_selectdevs()` 能理解的 `devstat_match` 结构。匹配字符串格式如下：

> `device`,`type`,`if`

`devstat_buildmatch()` 函数负责根据需要分配和重新分配匹配列表。当前已知的匹配类型包括：

**`da`** 直接访问设备

**`sa`** 顺序访问设备

**`printer`** 打印机

**`proc`** 处理器设备

**`worm`** 写一次读多次设备

**`cd`** CD 设备

**`scanner`** 扫描仪设备

**`optical`** 光存储设备

**`changer`** 介质更换器设备

**`comm`** 通信设备

**`array`** 存储阵列设备

**`enclosure`** 机箱服务设备

**`floppy`** 软盘设备

**`IDE`** 集成驱动电子设备

**`SCSI`** 小型计算机系统接口设备

**`NVME`** NVM Express 接口设备

**`other`** 任何其他设备接口

**`pass`** 直通设备

**设备类型：**

**接口：**

**直通：**

`devstat_compute_statistics()` 函数提供完整的统计计算。有四个参数的值*必须*提供：`current`、`previous`、`etime` 和可变参数列表的终止参数 `DSM_NONE`。对于大多数应用程序，用户会希望为 `current` 和 `previous` 都提供有效的 `devstat` 结构。在某些情况下，例如计算自系统启动以来的统计信息时，用户可以为 `previous` 参数传递 `NULL` 指针。在这种情况下，`devstat_compute_statistics()` 将使用 `current` 结构中的总统计信息来计算 `etime` 期间的统计信息。对于每个要计算的统计信息，用户应提供正确的枚举类型（如下所列）和指定类型的变量。所有统计信息要么是整数值（使用 `uint64_t`），要么是浮点值（使用 `long double`）。可以计算的统计信息有：

**`DSM_NONE`** 类型：无 此*必须*是传递给 `devstat_compute_statistics()` 的最后一个参数。它是参数列表终止符。

**`DSM_TOTAL_BYTES`** 类型：`uint64_t *` 在获取 `previous` 和 `current` 之间传输的总字节数。

**`DSM_TOTAL_BYTES_READ`**

**`DSM_TOTAL_BYTES_WRITE`**

**`DSM_TOTAL_BYTES_FREE`** 类型：`uint64_t *` 在获取 `previous` 和 `current` 之间指定类型事务的总字节数。

**`DSM_TOTAL_TRANSFERS`** 类型：`uint64_t *` 在获取 `previous` 和 `current` 之间的总传输次数。

**`DSM_TOTAL_TRANSFERS_OTHER`**

**`DSM_TOTAL_TRANSFERS_READ`**

**`DSM_TOTAL_TRANSFERS_WRITE`**

**`DSM_TOTAL_TRANSFERS_FREE`** 类型：`uint64_t *` 在获取 `previous` 和 `current` 之间指定类型事务的总次数。

**`DSM_TOTAL_DURATION`** 类型：`long double *` 在获取 `previous` 和 `current` 之间事务的总持续时间（以秒为单位）。

**`DSM_TOTAL_DURATION_OTHER`**

**`DSM_TOTAL_DURATION_READ`**

**`DSM_TOTAL_DURATION_WRITE`**

**`DSM_TOTAL_DURATION_FREE`** 类型：`long double *` 在获取 `previous` 和 `current` 之间指定类型事务的总持续时间。

**`DSM_TOTAL_BUSY_TIME`** 类型：`long double *` 在获取 `previous` 和 `current` 之间设备有一个或多个未完成事务的总时间。

**`DSM_TOTAL_BLOCKS`** 类型：`uint64_t *` 在获取 `previous` 和 `current` 之间传输的总块数。此数字以设备报告的块大小为单位。如果未报告块大小（即块大小为 0），计算中将使用默认的 512 字节块大小。

**`DSM_TOTAL_BLOCKS_READ`**

**`DSM_TOTAL_BLOCKS_WRITE`**

**`DSM_TOTAL_BLOCKS_FREE`** 类型：`uint64_t *` 在获取 `previous` 和 `current` 之间指定类型的总块数。此数字以设备报告的块大小为单位。如果未报告块大小（即块大小为 0），计算中将使用默认的 512 字节块大小。

**`DSM_KB_PER_TRANSFER`** 类型：`long double *` 在获取 `previous` 和 `current` 之间每次传输的平均千字节数。

**`DSM_KB_PER_TRANSFER_READ`**

**`DSM_KB_PER_TRANSFER_WRITE`**

**`DSM_KB_PER_TRANSFER_FREE`** 类型：`long double *` 在获取 `previous` 和 `current` 之间指定类型事务的平均千字节数。

**`DSM_TRANSFERS_PER_SECOND`** 类型：`long double *` 在获取 `previous` 和 `current` 之间每秒的平均传输次数。

**`DSM_TRANSFERS_PER_SECOND_OTHER`**

**`DSM_TRANSFERS_PER_SECOND_READ`**

**`DSM_TRANSFERS_PER_SECOND_WRITE`**

**`DSM_TRANSFERS_PER_SECOND_FREE`** 类型：`long double *` 在获取 `previous` 和 `current` 之间每秒指定类型事务的平均次数。

**`DSM_MB_PER_SECOND`** 类型：`long double *` 在获取 `previous` 和 `current` 之间每秒传输的平均兆字节数。

**`DSM_MB_PER_SECOND_READ`**

**`DSM_MB_PER_SECOND_WRITE`**

**`DSM_MB_PER_SECOND_FREE`** 类型：`long double *` 在获取 `previous` 和 `current` 之间指定类型事务每秒的平均兆字节数。

**`DSM_BLOCKS_PER_SECOND`** 类型：`long double *` 在获取 `previous` 和 `current` 之间每秒传输的平均块数。此数字以设备报告的块大小为单位。如果未报告块大小（即块大小为 0），计算中将使用默认的 512 字节块大小。

**`DSM_BLOCKS_PER_SECOND_READ`**

**`DSM_BLOCKS_PER_SECOND_WRITE`**

**`DSM_BLOCKS_PER_SECOND_FREE`** 类型：`long double *` 在获取 `previous` 和 `current` 之间指定类型事务每秒的平均块数。此数字以设备报告的块大小为单位。如果未报告块大小（即块大小为 0），计算中将使用默认的 512 字节块大小。

**`DSM_MS_PER_TRANSACTION`** 类型：`long double *` 在获取 `previous` 和 `current` 之间事务的平均持续时间。

**`DSM_MS_PER_TRANSACTION_OTHER`**

**`DSM_MS_PER_TRANSACTION_READ`**

**`DSM_MS_PER_TRANSACTION_WRITE`**

**`DSM_MS_PER_TRANSACTION_FREE`** 类型：`long double *` 在获取 `previous` 和 `current` 之间指定类型事务的平均持续时间。

**`DSM_BUSY_PCT`** 类型：`long double *` 在获取 `previous` 和 `current` 之间设备有一个或多个未完成事务的时间百分比。

**`DSM_QUEUE_LENGTH`** 类型：`uint64_t *` 在获取 `current` 时尚未完成事务的数量。

**`DSM_SKIP`** 类型：无 如果你不需要 `devstat_compute_statistics()` 的结果，只需将 `DSM_SKIP` 作为第一个（类型）参数，`NULL` 作为第二个参数。这在要计算的统计信息在运行时确定的场景中很有用。

`devstat_compute_etime()` 函数提供了一种简便的方法来计算两个 `bintime` 结构之间以秒为单位的差值。这通常与 `devstat_getdevs()` 函数每次提取当前 `devstat` 列表时记录的时间（在 `struct statinfo` 中）结合使用。

## 返回值

`devstat_getnumdevs()`、`devstat_getgeneration()` 和 `devstat_getversion()` 函数返回指定的 sysctl 变量，如果获取变量时出错则返回 -1。

`devstat_checkversion()` 函数在内核和用户空间的 `devstat` 版本匹配时返回 0。如果不匹配，返回 -1。

`devstat_getdevs()` 和 `devstat_selectdevs()` 函数在出错时返回 -1，无错误时返回 0，如果设备列表或所选设备已更改则返回 1。`devstat_getdevs()` 返回值为 1 通常提示重新运行 `devstat_selectdevs()`，因为设备列表已更改。

`devstat_buildmatch()` 函数出错时返回 -1，无错误时返回 0。

`devstat_compute_etime()` 函数返回计算出的经过时间。

`devstat_compute_statistics()` 函数出错时返回 -1，成功时返回 0。

如果从某个 `devstat` 库函数返回错误，错误原因通常会打印在全局字符串 `devstat_errbuf` 中，该字符串长度为 `DEVSTAT_ERRBUF_SIZE` 个字符。

## 参见

[systat(1)](../man1/systat.1.md), [kvm(3)](kvm.3.md), [sysctl(3)](../gen/sysctl.3.md), [iostat(8)](../man8/iostat.8.md), [rpc.rstatd(8)](../man8/rpc.rstatd.8.md), [sysctl(8)](../man8/sysctl.8.md), [vmstat(8)](../man8/vmstat.8.md), [devstat(9)](../man9/devstat.9.md)

## 历史

`devstat` 统计系统首次出现在 FreeBSD 3.0 中。新接口（以 `devstat_` 为前缀的函数）首次出现在 FreeBSD 5.0 中。

## 作者

Kenneth Merry <ken@FreeBSD.org>

## 缺陷

可能应该有一个接口来释放由 `devstat_getdevs()`、`devstat_selectdevs()` 和 `devstat_buildmatch()` 分配的内存。

`devstat_selectdevs()` 函数在“top”模式下且之前未选择任何设备时，可能不应该选择超过 `maxshowdevs` 个设备。

可能应该有函数来执行此库大多数客户端中进行的统计缓冲区交换。

`statinfo` 和 `devinfo` 结构可能应该被清理并多加思考。
