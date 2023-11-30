  PMCCONTROL(8)  

PMCCONTROL(8)

FreeBSD System Manager's Manual

PMCCONTROL(8)

[名称](#__u540D___u79F0_)
=======================

`pmccontrol` —

控制硬件性能监控计数器

[概要](#__u6982___u8981_)
=======================

`pmccontrol` \[`-c` cpu | `-d` pmc | `-e` pmc\] ... `pmccontrol` `-l` `pmccontrol` `-L` `pmccontrol` `-s`

[描述](#__u63CF___u8FF0_)
=======================

`pmccontrol` 实用程序控制系统硬件性能监视计数器的操作。

[选项](#__u9009___u9879_)
=======================

`pmccontrol` 实用程序按命令行顺序处理选项，因此后面的选项会修改前面选项的效果。 可以使用以下选项：

[`-c`](#c) cpu

随后的启用和禁用选项会影响由参数 参数 cpu 表示的 CPU。 cpu 是一个数字，表示系统中的 CPU，或 “`*`” ，表示系统中所有未暂停的 CPU。

[`-d`](#d) pmc

在由 `-c` 指定的 CPU 上禁用 PMC 编号 pmc ，以防止在随后重新启用之前使用它。 参数 pmc-
是一个数字，表示特定的 PMC，或 “`*`” 表示指定 CPU 上的所有 PMC。

只有空闲的 PMC 可以被禁用。

[`-e`](#e) pmc

在 `-c` 指定的 CPU 上启用 PMC 编号 pmc ，以便将来使用。 参数 pmc 是一个数字，表示特定的 PMC，或 “`*`” 表示指定 CPU 上的所有 PMC。 如果 PMC pmc 已启用，则此选项无效。

[`-l`](#l)

列出可用的硬件性能计数器及其当前配置。

[`-L`](#L)

列出可用的硬件性能计数器类及其支持的事件名称。

[`-s`](#s)

由 hwpmc(4) 维护的打印驱动程序统计信息。

[实例](#__u5B9E___u4F8B_)
=======================

要禁用所有 CPU 上的所有 PMC，请使用以下命令：

`pmccontrol -d*`

要在所有 CPU 上启用所有 PMC，请使用：

`pmccontrol -e*`

要禁用 CPU 2 上的 PMC 0 和 1，请使用：

`pmccontrol -c2 -d0 -d1`

要仅禁用 CPU 0 的 PMC 0，并在所有其他 CPU 上启用所有其他 PMCS，请使用：

`pmccontrol -c* -e* -c0 -d0`

[诊断](#__u8BCA___u65AD_)
=======================

The `pmccontrol` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

pmc(3), pmclog(3), hwpmc(4), pmcstat(8), sysctl(8)

[历史](#__u5386___u53F2_)
=======================

`pmccontrol` 实用程序首次出现在 FreeBSD 6.0 中。

[作者](#__u4F5C___u8005_)
=======================

Joseph Koshy <[jkoshy@FreeBSD.org](mailto:jkoshy@FreeBSD.org)\>

November 9, 2008

FreeBSD 13.1-RELEASE