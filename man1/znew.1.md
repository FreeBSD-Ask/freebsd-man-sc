  ZNEW(1)  

ZNEW(1)

FreeBSD General Commands Manual

ZNEW(1)

[名称](#__u540D___u79F0_)
=======================

`znew` —

将压缩文件转换为 gzip 文件

[概要](#__u6982___u8981_)
=======================

`znew` \[`-ftv9K`\] file ...

[描述](#__u63CF___u8FF0_)
=======================

`znew` 实用程序解压缩由 compress(1) 压缩的文件并使用 gzip(1) 重新压缩它们。

选项如下：

[`-f`](#f)

覆盖现有的 ‘.gz’ 文件。除非指定此选项，否则, `znew` 拒绝覆盖现有文件。

[`-t`](#t)

在删除原始文件之前测试 gzip 压缩文件的完整性。如果完整性检查失败，原始的 ‘.Z’ 文件不会被删除。

[`-v`](#v)

打印一份报告，指定达到的压缩率。

[`-9`](#9)

使用 gzip(1) 的 -9 模式，以降低执行速度为代价实现更好的压缩。

[`-K`](#K)

如果它使用的磁盘块少于 gzip 压缩的文件，则保留原始的 ‘.Z’ 文件。一个磁盘块是 1024 字节。

[参见](#__u53C2___u89C1_)
=======================

gzip(1)

[警告](#__u8B66___u544A_)
=======================

`znew` 实用程序尝试保持原始文件的文件模式。如果原始文件不可写，则无法执行此操作，并且 `znew` 将打印警告。

January 26, 2007

FreeBSD 13.1-RELEASE