# gjournal(8)

`gjournal` — 日志设备的控制工具

## 名称

`gjournal`

## 概要

`gjournal label [-cfhv] [-s jsize] dataprov [jprov]`

`gjournal stop [-fv] name ...`

`gjournal sync [-v]`

`gjournal clear [-v] prov ...`

`gjournal dump prov ...`

`gjournal list`

`gjournal status`

`gjournal load`

`gjournal unload`

## 描述

`gjournal` 工具用于在指定 GEOM provider 上配置日志。日志和数据可以存储在同一个 provider 上，也可以存储在两个独立的 provider 上。这是块级别的日志记录，而非文件系统级别的日志记录，这意味着所有内容都会被记录，例如对于文件系统，它会同时记录数据和元数据。`gjournal` GEOM 类可以与文件系统通信，这允许使用 `gjournal` 进行文件系统日志记录，并使文件系统保持一致状态。目前仅支持 UFS 文件系统。

使用 `gjournal` 在 UFS 文件系统上配置日志记录时，应首先使用 `gjournal` 工具创建一个 `gjournal` provider，然后在其上运行 newfs(8) 或 tunefs(8) 并加上 `-J` 标志，指示 UFS 与下方的 `gjournal` provider 协同工作。日志化 UFS 的工作方式有重要差异。最重要的是，[sync(2)](../man2/sync.2.md) 和 [fsync(2)](../man2/fsync.2.md) 系统调用不再按预期工作。要确保数据已存储到数据 provider 上，应在调用 [sync(2)](../man2/sync.2.md) 之后使用 `gjournal` 的 `sync` 命令。为获得最佳性能，使用 `gjournal` 时应禁用 soft-updates。同时使用 `async` [mount(8)](mount.8.md) 选项也是安全且推荐的。

当 `gjournal` 配置在 gmirror(8) 或 graid3(8) provider 之上时，它也会使它们保持一致状态，因此可以在这些 provider 上禁用断电或系统崩溃时的自动同步。

`gjournal` 工具使用存储在 provider 最后一个扇区中的磁盘上元数据来存储所有必要信息。当现有文件系统转换为使用 `gjournal` 时，这可能会产生问题。

`gjournal` 的第一个参数表示要执行的操作：

**`label`** 在给定 provider 上配置 `gjournal`。如果只给出一个 provider，数据和日志都存储在同一 provider 上。如果给出两个 provider，第一个将用作数据 provider，第二个将用作日志 provider。附加选项包括：

**`-c`** 对日志记录进行校验。

**`-f`** 可用于将现有文件系统转换为使用 `gjournal`，但前提是日志将配置在独立的 provider 上，且数据 provider 的最后一个扇区未被现有文件系统使用。如果 `gjournal` 检测到最后一个扇区已被使用，它将拒绝覆盖并返回错误。此行为可通过使用 `-f` 标志强制执行，该标志会强制 `gjournal` 覆盖最后一个扇区。

**`-h`** 在元数据中硬编码 provider 名称。

**`-s`** `jsize` 当数据和日志共用同一个 provider 时，指定日志的大小。默认为一吉字节。大小应根据 provider 的负载而非其容量来选择；建议的最小值为已安装物理内存大小的两倍。不建议将 `gjournal` 用于小型文件系统（例如仅有几吉字节大小）。

**`clear`** 清除给定 provider 上的元数据。

**`stop`** 停止给定的 provider。附加选项包括：

**`-f`** 即使给定 provider 已被打开也停止它。

**`sync`** 触发日志切换并强制将数据发送到数据 provider。

**`dump`** 转储给定 provider 上存储的元数据。

**`list`** 参见 geom(8)。

**`status`** 参见 geom(8)。

**`load`** 参见 geom(8)。

**`unload`** 参见 geom(8)。

附加选项包括：

**`-v`** 输出更详细的信息。

## 退出状态

成功时退出状态为 0，命令失败时为 1。

## 实例

创建基于 `gjournal` 的 UFS 文件系统并挂载：

```sh
gjournal load
gjournal label da0
newfs -J /dev/da0.journal
mount -o async /dev/da0.journal /mnt
```

在现有文件系统上配置日志记录，但仅在 `gjournal` 允许的情况下（即最后一个扇区尚未被文件系统使用）：

```sh
umount /dev/da0s1d
gjournal label da0s1d da0s1e && e
    tunefs -J enable -n disable da0s1d.journal && e
    mount -o async /dev/da0s1d.journal /mnt || e
    mount /dev/da0s1d /mnt
```

## SYSCTLS

Gjournal 添加了 sysctl 层级 kern.geom.journal。可用的字符串和整数信息详见下文。Changeable 列显示具有适当权限的进程是否可以更改该值。

| **sysctl name** | **Type** | **Changeable** |
| --- | --- | --- |
| debug | integer | yes |
| switch_time | integer | yes |
| force_switch | integer | yes |
| parallel_flushes | integer | yes |
| accept_immediately | integer | yes |
| parallel_copies | integer | yes |
| record_entries | integer | yes |
| optimize | integer | yes |

**`debug`** 设置非零值可在不同级别启用调试。调试级别 1 会记录日志级别的操作，涉及日志切换、元数据更新等。调试级别 2 会记录更高层次的操作，涉及日志中的条目数量、访问请求等。调试级别 3 会记录详细细节，包括 I/O 插入日志的过程。

**`switch_time`** 日志在被切换到新日志之前允许保持打开的最大秒数。

**`force_switch`** 当日志使用超过空闲日志空间的 N% 时，强制进行日志切换。

**`parallel_flushes`** 将日志刷新到数据 provider 时并行发送的刷新 I/O 请求数量。

**`accept_immediately`** 同时接受的最大 I/O 请求数量。

**`parallel_copies`** 并行发送的复制 I/O 请求数量。

**`record_entries`** 单个日志中允许的最大记录条目数。

**`optimize`** 控制是否通过将重叠的 I/O 合并为单个 I/O 并重新排序日志中的条目来优化日志中的条目。可通过将 sysctl 设置为 0 来禁用。

### cache

cache 层级可用的字符串和整数信息详见下文。Changeable 列显示具有适当权限的进程是否可以更改该值。

| **sysctl name** | **Type** | **Changeable** |
| --- | --- | --- |
| used | integer | no |
| limit | integer | yes |
| divisor | integer | no |
| switch | integer | yes |
| misses | integer | yes |
| alloc_failures | integer | yes |

**`used`** 当前分配给缓存的字节数。

**`limit`** 可分配给缓存的最大字节数。

**`divisor`** 将缓存大小设置为 kmem_size 的一部分。值为 2（默认值）时，缓存大小将设置为 kmem_size 的 1/2。

**`switch`** 当缓存的使用达到此百分比时强制进行日志切换。

**`misses`** 缓存未命中的次数，即已读取数据但在缓存中未找到的次数。

**`alloc_failures`** 因达到缓存上限而无法为缓存分配内存的次数。

### stats

statistics 层级可用的字符串和整数信息详见下文。Changeable 列显示具有适当权限的进程是否可以更改该值。

| **sysctl name** | **Type** | **Changeable** |
| --- | --- | --- |
| skipped_bytes | integer | yes |
| combined_ios | integer | yes |
| switches | integer | yes |
| wait_for_copy | integer | yes |
| journal_full | integer | yes |
| low_mem | integer | yes |

**`skipped_bytes`** 跳过的字节数。

**`combined_ios`** 通过日志优化合并的 I/O 数量。

**`switches`** 日志切换的次数。

**`wait_for_copy`** 日志切换过程不得不等待前一次日志复制完成的次数。

**`journal_full`** 日志几乎已满、强制进行日志切换的次数。

**`low_mem`** low_mem 钩子被调用的次数。

## 参见

[geom(4)](../man4/geom.4.md), geom(8), [mount(8)](mount.8.md), newfs(8), tunefs(8), [umount(8)](umount.8.md)

## 历史

`gjournal` 工具出现在 FreeBSD 7.0 中。

## 作者

Pawel Jakub Dawidek <pjd@FreeBSD.org>
