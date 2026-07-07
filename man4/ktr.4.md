# ktr(4)

`ktr` — 内核追踪设施

## 名称

`ktr`

## 概要

`options KTR options ALQ options KTR_ALQ options KTR_COMPILE=(KTR_LOCK|KTR_INTR|KTR_PROC) options KTR_CPUMASK=0x3 options KTR_ENTRIES=8192 options KTR_MASK=(KTR_INTR|KTR_PROC) options KTR_VERBOSE`

## 描述

`ktr` 设施允许在内核执行时记录内核事件，以便稍后调试时检查。启用 `ktr` 的唯一必需选项是“`options KTR`”。

`KTR_ENTRIES` 选项设置事件缓冲区大小。当前运行内核中的缓冲区大小可通过 sysctl `debug.ktr.entries` 查询。默认情况下，缓冲区包含 1024 个条目。

### 事件屏蔽

可启用或禁用事件级别以减少过多和过于详细的日志记录。首先，在编译时通过 `KTR_COMPILE` 选项指定事件掩码，以限制实际编译到内核中的事件。此选项的默认值是启用所有事件。

其次，内核运行时记录的实际事件可通过运行时事件掩码进一步屏蔽。`KTR_MASK` 选项设置运行时事件掩码的默认值。运行时事件掩码也可由 [loader(8)](../man8/loader.8.md) 通过 `debug.ktr.mask` 环境变量设置。还可在引导后通过 `debug.ktr.mask` sysctl 检查和设置。默认情况下，运行时掩码设置为阻止任何追踪。事件掩码位的定义可在以下文件中找到：

`#include <sys/ktr_class.h>`

此外，还有一个 CPU 事件掩码，其默认值可通过 `KTR_CPUMASK` 选项更改。当 `KTR_CPUMASK` 使用两个或更多参数时，请注意它们不能用空格分隔。CPU 必须在此位掩码中设置其逻辑 ID 对应的位，才能记录其上发生的事件。此掩码可由 [loader(8)](../man8/loader.8.md) 通过 `debug.ktr.cpumask` 环境变量设置。还可在引导后通过 `debug.ktr.cpumask` sysctl 检查和设置。默认情况下，仅 `KTR_CPUMASK` 中指定的 CPU 将记录事件。更多信息请参见 `sys/conf/NOTES`。

### 详细模式

默认情况下，事件仅记录到内部缓冲区以供稍后检查，但如果设置了详细标志，则它们还会输出到内核控制台。此标志也可从加载器通过 `debug.ktr.verbose` 环境变量设置，或在引导后通过 `debug.ktr.verbose` sysctl 检查和设置。如果标志设置为零（默认值），则禁用详细输出。如果标志设置为一，则日志消息的内容和 CPU 编号将打印到内核控制台。如果标志大于一，则除日志消息和 CPU 编号外，还将事件的文件名和行号输出到控制台。`KTR_VERBOSE` 选项将标志设置为一。

### 检查事件

可在 [ddb(4)](ddb.4.md) 中通过 `show ktr` [`/vV`] 命令检查 KTR 缓冲区。此命令一次显示一页追踪缓冲区的内容。在“`--more--`”提示下，按 Enter 键显示一个更多条目并再次提示。空格键显示另一页条目。任何其他键退出。默认情况下，每个日志条目不显示时间戳、文件名和行号。如果指定 `/v` 修饰符，则在正常输出之外显示它们。如果指定 `/V` 修饰符，则除正常输出外仅显示时间戳。注意，事件以反向时间顺序显示。即最新的事件首先显示。

### 将 ktr 记录到磁盘

`KTR_ALQ` 选项可用于将 `ktr` 条目记录到磁盘以供 ktrdump(8) 工具进行后分析。此选项依赖于 `ALQ` 选项。由于追踪消息可能数量巨大，应仔细选择追踪掩码。此功能通过一组 sysctl 配置。

**`debug.ktr.alq_file`** 显示或设置 `ktr` 将记录到的文件。默认值为 **/tmp/ktr.out**。如果在 `ktr` 启用时更改文件名，则要等到下次调用才会生效。

**`debug.ktr.alq_enable`** 设置为一时启用将 `ktr` 条目记录到磁盘。将此值设置为 0 将终止记录到磁盘并恢复为记录到正常的 ktr 环形缓冲区。记录到磁盘时数据不会发送到环形缓冲区。

**`debug.ktr.alq_max`** 将记录到磁盘的最大条目数，或 0 表示无限。这有助于限制记录的高频条目数量。

**`debug.ktr.alq_depth`** 决定写入缓冲区中的条目数。这是在写入磁盘之前保存条目的缓冲区，默认为 `KTR_ENTRIES` 选项的值。

**`debug.ktr.alq_failed`** 记录由于写入缓冲区溢出而无法写入条目的次数。如果记录的 `ktr` 消息频率超过队列深度，可能会发生此情况。

**`debug.ktr.alq_cnt`** 记录当前已写入磁盘的条目数。

## 参见

ktrdump(8), alq(9), ktr(9)

## 历史

KTR 内核追踪设施最早出现于 BSD/OS，并导入到 FreeBSD 5.0。
