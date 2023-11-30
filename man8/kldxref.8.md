  KLDXREF(8)  

KLDXREF(8)

FreeBSD System Manager's Manual

KLDXREF(8)

[名称](#__u540D___u79F0_)
=======================

`kldxref` —

为内核加载器生成提示

[概要](#__u6982___u8981_)
=======================

`kldxref` \[`-Rdv`\] \[`-f` hintsfile\] path ...

[描述](#__u63CF___u8FF0_)
=======================

`kldxref` 实用程序用于生成提示文件，其中列出了模块、它们的版本号以及包含它们的文件。 内核加载程序使用这些提示来确定在哪里可以找到特定的 KLD 模块。

为包含模块的命令行上列出的每个目录生成一个单独的提示文件。 如果没有为特定目录生成提示记录，则不会创建提示文件，并且删除预先存在的提示文件（如果该目录中有提示文件）。

可以使用以下选项：

[`-R`](#R)

递归到子目录。

[`-d`](#d)

不要生成提示文件，而是在标准输出上打印模块元数据。

[`-f`](#f) hintsfile

为提示文件指定与 linker.hints 不同的名称。

[`-v`](#v)

以详细模式运行。

[实例](#__u5B9E___u4F8B_)
=======================

要为标准模块和附加模块构建提示文件：

`kldxref /boot/kernel /boot/modules`

为所有已安装的内核构建提示文件：

`kldxref -R /boot`

[S参见](#S__u53C2___u89C1_)
=========================

kld(4), kldconfig(8), kldload(8), kldstat(8), kldunload(8)

[历史](#__u5386___u53F2_)
=======================

`kldxref` 实用程序首先出现在 FreeBSD 5.0 中。

[作者](#__u4F5C___u8005_)
=======================

`kldxref` 实用程序由 Boris Popov <[bp@FreeBSD.org](mailto:bp@FreeBSD.org)\>-
实现。 本手册页由 Boris Popov <[bp@FreeBSD.org](mailto:bp@FreeBSD.org)\> 和 Dag-Erling Smørgrav <[des@FreeBSD.org](mailto:des@FreeBSD.org)\> 编写。

October 9, 2001

FreeBSD 13.1-RELEASE