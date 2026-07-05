# pmccontrol.8

`pmccontrol` — 控制硬件性能监控计数器

## 名称

`pmccontrol`

## 概要

`pmccontrol [-c cpu | -d pmc | -e pmc] ...` `pmccontrol -l` `pmccontrol -L` `pmccontrol -s`

## 描述

`pmccontrol` 工具控制系统的硬件性能监控计数器的操作。

## 选项

`pmccontrol` 工具按命令行顺序处理选项，因此后面的选项会修改前面选项的效果。可用选项如下：

**`-c`** `cpu` 后续的启用和禁用选项影响由参数 `cpu` 表示的 CPU。参数 `cpu` 是表示系统中某个 CPU 的数字，或“`*`”，表示系统中所有未停机的 CPU。

**`-d`** `pmc` 在由 `-c` 指定的 CPU 上禁用编号为 `pmc` 的 PMC，阻止其被使用，直到随后重新启用。参数 `pmc` 是表示特定 PMC 的数字，或“`*`”表示指定 CPU 上的所有 PMC。仅空闲的 PMC 可以被禁用。

**`-e`** `pmc` 在由 `-c` 指定的 CPU 上启用编号为 `pmc` 的 PMC，允许其将来被使用。参数 `pmc` 是表示特定 PMC 的数字，或“`*`”表示指定 CPU 上的所有 PMC。如果 PMC `pmc` 已经启用，此选项无效。

**`-l`** 列出可用的硬件性能计数器及其当前状态。

**`-L`** 列出可用的硬件性能计数器类别及其支持的事件名称。

**`-s`** 打印由 [hwpmc(4)](../man4/hwpmc.4.md) 维护的驱动程序统计信息。

## 实例

要禁用所有 CPU 上的所有 PMC，使用命令：

```sh
pmccontrol -d*
```

要启用所有 CPU 上的所有 PMC，使用：

```sh
pmccontrol -e*
```

要禁用 CPU 2 上的 PMC 0 和 1，使用：

```sh
pmccontrol -c2 -d0 -d1
```

要仅禁用 CPU 0 的 PMC 0，并启用所有其他 CPU 上的所有其他 PMC，使用：

```sh
pmccontrol -c* -e* -c0 -d0
```

## 诊断

`pmccontrol` 工具成功时退出值为 0，发生错误时大于 0。

## 参见

pmc(3), pmclog(3), [hwpmc(4)](../man4/hwpmc.4.md), [pmcstat(8)](pmcstat.8.md), [sysctl(8)](sysctl.8.md)

## 历史

`pmccontrol` 工具首次出现在 FreeBSD 6.0 中。

## 作者

Joseph Koshy <jkoshy@FreeBSD.org>
