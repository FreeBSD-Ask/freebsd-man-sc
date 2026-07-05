# stats.7

`stats` — 有关各种统计实用程序的信息

## 名称

`stats`

## 描述

FreeBSD 用户空间部分包含一系列实用程序，可用于在运行时以及可选地从核心转储文件中确认系统状态。

## 命令

以下命令（按字母顺序排列）目前包含在基本系统中，并且会定期增加更多。

**`btsockstat`** 显示蓝牙套接字信息

**`ctlstat`** CAM 目标层统计实用程序

**`dtrace_mib`** 使用 DTrace 访问 MIB 统计计数器

**`dwatch`** 在进程触发特定 DTrace 探测时监视进程

**`fstat`** 识别活动文件

**`gstat`** 打印有关 GEOM 磁盘的统计信息

**`ibstat`** 显示来自 InfiniBand 驱动程序的信息

**`ifmcstat`** 转储每个接口的多播组管理统计信息

**`iostat`** 报告内核子系统 I/O 统计信息

**`ipfstat`** 显示 IPF 包过滤器和过滤列表的统计信息

**`kldstat`** 显示动态内核链接器的状态

**`lockstat`** 报告内核锁和性能分析统计信息

**`mailstats`** 显示邮件统计信息

**`netstat`** 显示网络状态和统计信息

**`nfsstat`** 显示 NFS 统计信息

**`plockstat`** 使用 DTrace 跟踪 pthread 锁统计信息

**`pmcstat`** 使用性能监控硬件进行性能测量

**`procstat`** 获取详细的进程信息

**`pstat`** 显示系统数据结构

**`sockstat`** 列出打开的套接字

**`stat`** 显示文件状态

**`systat`** 显示系统统计信息

**`vmstat`** 报告虚拟内存统计信息

**`zpool`** 报告 ZFS I/O 统计信息

## 参见

[btsockstat(1)](../man1/btsockstat.1.md), dwatch(1), fstat(1), [intro(1)](../man1/intro.1.md), [lockstat(1)](../man1/lockstat.1.md), [netstat(1)](../man1/netstat.1.md), plockstat(1), procstat(1), [sockstat(1)](../man1/sockstat.1.md), [stat(1)](../man1/stat.1.md), [systat(1)](../man1/systat.1.md), [dtrace_mib(4)](../man4/dtrace_mib.4.md), [intro(7)](intro.7.md), [tuning(7)](tuning.7.md), ctlstat(8), gstat(8), ibstat(8), ifmcstat(8), [intro(8)](../man8/intro.8.md), [iostat(8)](../man8/iostat.8.md), ipfstat(8), [kldstat(8)](../man8/kldstat.8.md), [mailstats(8)](../man8/mailstats.8.md), [pmcstat(8)](../man8/pmcstat.8.md), pstat(8), [vmstat(8)](../man8/vmstat.8.md), zpool-iostat(8)

## 历史

`zpool` 手册页首次出现于 FreeBSD 13.0。

## 作者

Daniel Ebdrup Jensen <debdrup@FreeBSD.org>
