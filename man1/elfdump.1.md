  ELFDUMP(1)  

ELFDUMP(1)

FreeBSD General Commands Manual

ELFDUMP(1)

[名称](#__u540D___u79F0_)
=======================

`elfdump` —

显示有关 ELF 文件的信息

[概要](#__u6982___u8981_)
=======================

`elfdump` `-a` | `-E` | `-cdeGhinprs` \[`-w` file\] file

[描述](#__u63CF___u8FF0_)
=======================

`elfdump` 实用程序转储有关指定 ELF 文件的各种信息。

-
选项如下：

[`-a`](#a)

转储所有信息。

[`-c`](#c)

转储节标题。

[`-d`](#d)

转储动态符号。

[`-e`](#e)

转储 ELF 标头。

[`-E`](#E)

如果 file 是 ELF 文件则返回成功，否则返回失败。 此选项与其他选项互斥。

[`-G`](#G)

转储 GOT。

[`-h`](#h)

转储散列值。

[`-i`](#i)

转储动态解释器。

[`-n`](#n)

转储笔记部分。

[`-p`](#p)

转储程序头。

[`-r`](#r)

转储重定位。

[`-s`](#s)

转储符号表。

[`-w`](#w) file

将输出写 file 而不是标准输出。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `elfdump` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

以下是 `elfdump` 命令的典型用法示例：

`elfdump -a -w output /bin/ls`

[SEE ALSO](#SEE_ALSO)
=====================

objdump(1), readelf(1)

AT&T Unix 系统实验室, System V 应用程序二进制接口, [http://www.sco.com/developers/gabi/](http://www.sco.com/developers/gabi/).

[历史](#__u5386___u53F2_)
=======================

`elfdump` 实用程序首次出现在 FreeBSD 5.0 中。

[作者](#__u4F5C___u8005_)
=======================

`elfdump` 实用程序 Jake Burkholder <[jake@FreeBSD.org](mailto:jake@FreeBSD.org)\> 编写。 本手册页由 David O'Brien <[obrien@FreeBSD.org](mailto:obrien@FreeBSD.org)\> 编写。

[缺陷](#__u7F3A___u9677_)
=======================

没有完全实现 ELF gABI。

November 5, 2018

FreeBSD 13.1-RELEASE