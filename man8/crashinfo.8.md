# crashinfo(8)

`crashinfo` — 分析操作系统的核心转储

## 名称

`crashinfo`

## 概要

`crashinfo [-d crashdir] [-n dumpnr] [-k kernel] [core]`

## 描述

`crashinfo` 工具分析由 savecore(8) 保存的核心转储。它在与核心转储相同的目录中生成包含分析结果的文本文件。对于名为 `vmcore.XX` 的核心转储文件，生成的文本文件将被命名为 `core.txt.XX`。

默认情况下，`crashinfo` 分析核心转储目录中最近的核心转储。可以通过 `core` 或 `dumpnr` 参数指定特定的核心转储。一旦 `crashinfo` 找到了核心转储，它会分析该核心转储以确定生成该核心的内核的确切版本。然后，它会在 **/boot** 下的每个子目录中查找匹配的内核文件。也可以通过 `kernel` 参数显式提供内核文件的位置。

一旦 `crashinfo` 找到了核心转储和内核，它会使用多个工具来分析核心，包括 [dmesg(8)](dmesg.8.md)、fstat(1)、[iostat(8)](iostat.8.md)、ipcs(1)、kgdb(1)（`ports/devel/gdb`）、[netstat(1)](../man1/netstat.1.md)、nfsstat(1)、[ps(1)](../man1/ps.1.md)、pstat(8) 和 [vmstat(8)](vmstat.8.md)。注意，kgdb 必须从 devel/gdb Port 或 gdb 包安装。

可用选项如下：

**`-b`** 以批处理模式运行。将大多数消息写入 `core.txt.XX` 文件而非终端。此标志在引导期间运行 `crashinfo` 时使用。

**`-d`** `crashdir` 指定替代的核心转储目录。默认的崩溃转储目录为 **/var/crash**。

**`-n`** `dumpnr` 使用保存在 `vmcore.dumpnr` 中的核心转储，而非核心转储目录中最新的核心。

**`-k`** `kernel` 指定显式的内核文件。

## 参见

[textdump(4)](../man4/textdump.4.md)，savecore(8)

## 历史

`crashinfo` 工具出现于 FreeBSD 6.4。
