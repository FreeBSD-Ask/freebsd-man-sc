  INTRO(8)  

INTRO(8)

FreeBSD System Manager's Manual

INTRO(8)

[名称](#__u540D___u79F0_)
=======================

`intro` —

系统维护程序和命令介绍

[描述](#__u63CF___u8FF0_)
=======================

本节包含与系统操作和维护相关的信息。

它描述了用于创建新文件系统 (newfs(8)), 验证文件系统完整性 (fsck(8)), 控制磁盘使用 (edquota(8)), 维护系统备份 (dump(8)), 并在磁盘过早死亡时恢复文件 (restore(8)) 。 还描述了与网络相关的服务，如 inetd(8) 和 ftpd(8) 。

所有命令都设置退出状态。 可以测试其值以查看命令是否正常完成。 除非另有说明（罕见），否则值 0 表示命令成功完成，而值 >0 表示错误。 一些命令试图通过使用 sysexits(3) 中定义的错误代码来描述故障的性质，或者将状态设置为 >0 的任意值（通常为 1），但是手册中没有描述许多这样的值。

本节中的许多页面描述了一般系统管理主题。

例如， boot(8) 手册页描述了系统引导过程， diskless(8) 手册页描述了如何通过网络引导系统。 应查阅 crash(8) 手册页以了解如何解释系统故障转储。

[历史](#__u5386___u53F2_)
=======================

`intro` 部分的手册页出现在 4.2BSD 中。

October 22, 2006

FreeBSD 13.1-RELEASE