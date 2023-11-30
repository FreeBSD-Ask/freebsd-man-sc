  AUTOUNMOUNTD(8)  

AUTOUNMOUNTD(8)

FreeBSD System Manager's Manual

AUTOUNMOUNTD(8)

[名称](#__u540D___u79F0_)
=======================

`autounmountd` —

卸载自动挂载文件系统的守护进程

[概要](#__u6982___u8981_)
=======================

`autounmountd` \[`-d`\] \[`-r` time\] \[`-t` time\] \[`-v`\]

[描述](#__u63CF___u8FF0_)
=======================

`autounmountd` 守护进程负责卸载由 automountd(8) 挂载的文件系统。 启动时， `autounmountd` 检索具有 `automounted` 挂载选项集的文件系统列表。 每次挂载或卸载文件系统时都会更新该列表。 经过指定的时间后， `autounmountd` 会尝试卸载文件系统，如有必要，会在一段时间后重试。

这些选项可用：

[`-d`](#d)

调试模式：增加详细程度并且不守护进程。

[`-r`](#r)

在上一次尝试失败后尝试卸载过期文件系统之前等待的秒数，可能是由于文件系统正忙。 默认值为 600 或十分钟。

[`-t`](#t)

尝试卸载文件系统之前等待的秒数。 默认值为 600 或十分钟。

[`-v`](#v)

增加详细程度。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `autounmountd` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

auto\_master(5), autofs(5), automount(8), automountd(8)

[历史](#__u5386___u53F2_)
=======================

`autounmountd` 守护进程出现在 FreeBSD 10.1 中。

[作者](#__u4F5C___u8005_)
=======================

`autounmountd` 由 Edward Tomasz Napierala <[trasz@FreeBSD.org](mailto:trasz@FreeBSD.org)\>-
在 FreeBSD 基金会的赞助下开发。

December 13, 2014

FreeBSD 13.1-RELEASE