  GROWFS(8)  

GROWFS(8)

FreeBSD System Manager's Manual

GROWFS(8)

[名称](#__u540D___u79F0_)
=======================

`growfs` —

扩展现有的 UFS 文件系统

[概要](#__u6982___u8981_)
=======================

`growfs` \[`-Ny`\] \[`-s` size\] special | filesystem

[描述](#__u63CF___u8FF0_)
=======================

`growfs` 实用程序可以扩展 UFS 文件系统。 在运行 `growfs` 之前，必须使用 gpart(8) 扩展包含文件系统的分区或片。 如果你正在使用卷，你必须使用 gvinum(8) 来扩大它们。 `growfs` 实用程序在指定的特殊文件上扩展文件系统的大小。 可以使用以下选项：

[`-N`](#N)

“测试模式” 。 导致打印出新的文件系统参数而不实际扩大文件系统。

[`-y`](#y)

导致 `growfs` 假设所有操作员问题的答案是肯定的。

[`-s`](#s) size

确定扇区放大后文件系统的 size 。 Size 是 512 字节扇区的数量，除非后缀为 `b`, `k`, `m`, `g` 或 `t` ，它们分别表示字节、千字节、兆字节、千兆字节和太字节。 该值默认为 special 中指定的原始分区的大小（换句话说， `growfs` 会将文件系统扩大到整个分区的大小）。

[实例](#__u5B9E___u4F8B_)
=======================

扩展根文件系统以填满可用空间：

`growfs /`

刷新 LUN 大小，调整分区大小以使用所有可用容量，并相应地扩展文件系统：

`camcontrol reprobe da0`

`gpart recover da0`

`gpart resize -i 1 da0`

`growfs /dev/da0p1`

[参见](#__u53C2___u89C1_)
=======================

camcontrol(8), fsck(8), gpart(8), newfs(8), tunefs(8)

[历史](#__u5386___u53F2_)
=======================

`growfs` 实用程序首次出现在 FreeBSD 4.4 中。 FreeBSD 10.0 中增加了调整挂载文件系统大小的功能。

[作者](#__u4F5C___u8005_)
=======================

Christoph Herrmann <[chm@FreeBSD.org](mailto:chm@FreeBSD.org)\> Thomas-Henning von Kamptz <[tomsoft@FreeBSD.org](mailto:tomsoft@FreeBSD.org)\> The GROWFS team <[growfs@Tomsoft.COM](mailto:growfs@Tomsoft.COM)\> Edward Tomasz Napierala <[trasz@FreeBSD.org](mailto:trasz@FreeBSD.org)\>

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

当扩展以读写方式挂载的文件系统时，对该文件系统的任何写入都将被暂时挂起，直到扩展完成。

[缺陷](#__u7F3A___u9677_)
=======================

通常 `growfs` 将柱面组摘要写入磁盘并稍后再次读取以进行更多更新。 使用 `-N` 时，此读取操作将提供意外数据。 因此，这部分无法真正模拟，在测试模式下将被跳过。

December 13, 2017

FreeBSD 13.1-RELEASE