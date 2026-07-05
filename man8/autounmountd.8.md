# autounmountd.8

`autounmountd` — 卸载自动挂载文件系统的守护进程

## 名称

`autounmountd`

## 概要

`autounmountd [-d] [-r time] [-t time] [-v]`

## 描述

`autounmountd` 守护进程负责卸载由 automountd(8) 挂载的文件系统。启动时，`autounmountd` 会获取设置了 `automounted` 挂载选项的文件系统列表。每当有文件系统被挂载或卸载时，该列表都会更新。经过指定时间后，`autounmountd` 会尝试卸载文件系统，如有必要会在一段时间后重试。

可用选项如下：

**`-d`** 调试模式：增加详细输出且不转入后台运行。

**`-r`** 上一次卸载尝试失败（可能因文件系统繁忙）后，再次尝试卸载过期文件系统前等待的秒数。默认值为 600，即十分钟。

**`-t`** 尝试卸载文件系统前等待的秒数。默认值为 600，即十分钟。

**`-v`** 增加详细输出。

## 退出状态

`autounmountd` 工具成功时返回 0，发生错误时返回值大于 0。

## 参见

auto_master(5), autofs(5), automount(8), automountd(8)

## 历史

`autounmountd` 守护进程首次出现在 FreeBSD 10.1 中。

## 作者

`autounmountd` 由 Edward Tomasz Napierala <trasz@FreeBSD.org> 在 FreeBSD 基金会赞助下开发。
