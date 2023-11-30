  CRASHINFO(8)  

CRASHINFO(8)

FreeBSD System Manager's Manual

CRASHINFO(8)

[名称](#__u540D___u79F0_)
=======================

`crashinfo` —

分析操作系统的核心转储

[概要](#__u6982___u8981_)
=======================

`crashinfo` \[`-d` crashdir\] \[`-n` dumpnr\] \[`-k` kernel\] \[core\]

[描述](#__u63CF___u8FF0_)
=======================

`crashinfo` 实用程序分析由 savecore(8) 保存的核心转储。 它会在与核心转储相同的目录中生成一个包含分析的文本文件。 对于名为 vmcore.XX 的给定核心转储文件，生成的文本文件将命名为 core.txt.XX

默认情况下， `crashinfo` 分析核心转储目录中最新的核心转储。 可以通过 core 或 dumpnr-
参数指定特定的核心转储。 一旦 `crashinfo` 找到核心转储，它就会分析核心转储以确定生成核心的内核的确切版本。 然后它会在 /boot 的每个子目录下查找匹配的内核文件。 内核文件的位置也可以通过 kernel 参数显式提供。

一旦 `crashinfo` 找到核心转储和内核，它就会使用几个实用程序来分析核心，包括 dmesg(8), fstat(1), iostat(8), ipcs(1), kgdb(1), netstat(1), nfsstat(1), ps(1), pstat(8) 和 vmstat(8) 。请注意，kgdb 必须从 devel/gdb 端口或 gdb 包安装。

选项如下：

[`-b`](#b)

以批处理模式运行。 将大多数消息写入 core.txt.XX 文件而不是终端。 在引导期间运行 `crashinfo` 时使用此标志。

[`-d`](#d) crashdir

指定备用核心转储目录。 默认的故障转储目录是 /var/crash 。

[`-n`](#n) dumpnr

使用保存在 vmcore.dumpnr 中的核心转储，而不是核心转储目录中的最新核心。

[`-k`](#k) kernel

指定显式内核文件。

[参见](#__u53C2___u89C1_)
=======================

textdump(4), savecore(8)

[历史](#__u5386___u53F2_)
=======================

`crashinfo` 实用程序出现在 FreeBSD 6.4 中。

December 2, 2020

FreeBSD 13.1-RELEASE