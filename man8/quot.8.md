  QUOT(8)  

QUOT(8)

FreeBSD System Manager's Manual

QUOT(8)

[名称](#__u540D___u79F0_)
=======================

`quot` —

显示每个用户占用的磁盘空间

[概要](#__u6982___u8981_)
=======================

`quot` \[`-acfhknv`\] \[filesystem ...\]

[描述](#__u63CF___u8FF0_)
=======================

`quot` 实用程序用于收集有关每个本地用户的磁盘使用情况的统计信息。

可以使用以下选项：

[`-a`](#a)

包括所有已安装文件系统的统计信息。

[`-c`](#c)

显示三列，其中包含每个文件的块数、此类别中的文件数以及具有此或更低大小的文件中的总块数。

[`-f`](#f)

对于每个用户，显示文件数和占用空间。

[`-h`](#h)

根据每个文件的大小估计每个文件中的块数。尽管这并没有给出正确的结果（它没有考虑文件中的漏洞），但这个选项并没有更快，因此不鼓励。

[`-k`](#k)

强制以千字节计数报告数字。默认情况下，所有大小都以 512 字节块计数报告。

[`-n`](#n)

给定标准输入中的 inode 列表（加上每行上的一些可选数据），为每个文件打印出所有者（加上输入行的其余部分）。这传统上用于管道：

ls -i | sed -e 's,^ \*,,' | sort -k 1n | quot -n filesystem 

获取文件及其所有者的报告。

[`-v`](#v)

除默认输出外，还显示 30、60 和 90 天内未访问的文件数。

[环境](#__u73AF___u5883_)
=======================

[`BLOCKSIZE`](#BLOCKSIZE)

如果设置了环境变量 `BLOCKSIZE` 并且未指定 `-k` 选项，则块计数将以该大小块为单位显示。

[参见](#__u53C2___u89C1_)
=======================

df(1), quota(1), getmntinfo(3), fstab(5), mount(8)

[历史](#__u5386___u53F2_)
=======================

`quot` 的实现由 Wolfgang Solfrank / TooLs GmbH 提供。

[缺陷](#__u7F3A___u9677_)
=======================

在 FreeBSD 中不存在 ncheck （这将比 `ls` `-i` 在上面的示例中更有用）。

February 8, 1994

FreeBSD 13.1-RELEASE