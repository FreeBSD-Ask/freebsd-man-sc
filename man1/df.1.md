  DF(1)  

DF(1)

FreeBSD General Commands Manual

DF(1)

[名称](#__u540D___u79F0_)
=======================

`df` —

显示可用磁盘空间

[概要](#__u6982___u8981_)
=======================

`df` \[`--libxo`\] \[`-b` | `-g` | `-H` | `-h` | `-k` | `-m` | `-P`\] \[`-acilnT`\] \[`-,`\] \[`-t` type\] \[file | filesystem ...\]

[描述](#__u63CF___u8FF0_)
=======================

`df` 实用程序显示有关指定已安装 file system 或 file 系统上的可用磁盘空间量的统计信息。 默认情况下，块计数显示为假定块大小为 512 字节。 如果既没有指定文件也没有指定文件系统操作数，则显示所有已挂载文件系统的统计信息（受下面的 `-t` 选项影响）。

可以使用以下选项：

[`--libxo`](#-libxo)

通过 libxo(3) 以不同的人类和机器可读格式生成输出。 有关命令行参数的详细信息，请参阅 xo\_parse\_args(3) 。

[`-a`](#a)

显示所有挂载点，包括使用 `MNT_IGNORE` 标志挂载的那些。 这对于在命令行上指定的文件系统是隐含的。

[`-b`](#b)

显式使用 512 字节块，覆盖环境中的任何 `BLOCKSIZE` 规范。 这与 `-P` 选项相同。 `-k` 选项覆盖此选项。

[`-c`](#c)

显示总计。

[`-g`](#g)

使用 1073741824 字节（1 Gibibyte）块而不是默认值。 这会覆盖环境中的任何 `BLOCKSIZE` 规范。

[`-h`](#h)

“Human-readable” 输出。 使用单位后缀：Byte、Kibibyte、Mebibyte、Gibibyte、Tebibyte 和 Pebibyte（基于 1024 的幂），以便将位数减少到四位或更少。

[`-H`](#H), `-``-si`

与 `-h` 相同，但基于 1000 的幂。

[`-i`](#i)

包括有关空闲和已用 inode 数量的统计信息。 结合 `-h` 或 `-H` 选项，inode 的数量按 1000 的幂进行缩放。

[`-k`](#k)

使用 1024 字节（1 Kibibyte）块而不是默认值。 这会覆盖 `-P` 选项和环境中的任何 `BLOCKSIZE` 规范。

[`-l`](#l)

仅显示有关本地安装的文件系统的信息。

[`-m`](#m)

使用 1048576 字节（1 兆字节）块而不是默认值。 这会覆盖环境中的任何 `BLOCKSIZE` 规范。

[`-n`](#n)

打印出之前从文件系统中获得的统计信息。 如果一个或多个文件系统可能处于无法提供统计信息的状态，则应使用此选项。 指定此选项时， `df` 将不会从文件系统请求新的统计信息，但会以先前获得的可能陈旧的统计信息进行响应。

[`-P`](#P)

显式使用 512 字节块，覆盖环境中的任何 `BLOCKSIZE` 规范。 这与 `-b` 选项相同。 `-k` 选项覆盖此选项。

[`-t`](#t)

仅打印指定类型的文件系统的统计信息。 可以在逗号分隔的列表中指定一种以上的类型。 文件系统类型列表可以以 “no” 为前缀，以指定 _不应_ 对其采取操作的文件系统类型。 例如， `df` 命令：

df -t nonfs,nullfs 

列出除 NFS 和 NULLFS 类型之外的所有文件系统。 lsvfs(1) 命令可用于找出系统上可用的文件系统类型。

[`-T`](#T)

包括文件系统类型。

`-`,

（逗号）使用由 localeconv(3)-
返回的非货币分隔符（通常是逗号或句点）将打印尺寸分组并以千为单位分隔。 如果未设置区域设置，或者区域设置没有非货币分隔符，则此选项无效。

[环境](#__u73AF___u5883_)
=======================

[`BLOCKSIZE`](#BLOCKSIZE)

指定报告块计数的单位。 这使用 getbsize(3) ，它允许使用字母 _k_ （对于 1024 字节的倍数）、 _m_ （对于 1048576 字节的倍数）或 _g_ 对于 gibibytes）进行缩放的字节或数字单位。 允许的范围是 512 字节到 1 GB。 如果该值在外部，它将被设置为适当的限制。

[实例](#__u5B9E___u4F8B_)
=======================

显示所有挂载点的可读可用磁盘空间，包括文件系统类型：

$ df -ahT Filesystem Type Size Used Avail Capacity Mounted on /dev/ada1p2 ufs 213G 152G 44G 78% / devfs devfs 1.0K 1.0K 0B 100% /dev /dev/ada0p1 ufs 1.8T 168G 1.5T 10% /data linsysfs linsysfs 4.0K 4.0K 0B 100% /compat/linux/sys /dev/da0 msdosfs 7.6G 424M 7.2G 5% /mnt/usb 

显示以前收集的数据，包括除 devfs 或 linsysfs 文件系统之外的 inode 统计信息。 请注意， “no” 前缀会影响列表中的所有文件系统，并且 `-t` 选项只能指定一次：

$ df -i -n -t nodevfs,linsysfs Filesystem 1K-blocks Used Avail Capacity iused ifree %iused Mounted on /dev/ada1p2 223235736 159618992 45757888 78% 1657590 27234568 6% / /dev/ada0p1 1892163184 176319420 1564470712 10% 1319710 243300576 1% /data /dev/da0 7989888 433664 7556224 5% 0 0 100% /mnt/usb 

显示包含文件 /etc/rc.conf 的文件系统的人类可读信息：

$ df -h /etc/rc.conf Filesystem Size Used Avail Capacity Mounted on /dev/ada1p2 213G 152G 44G 78% / 

与上面相同，但指定了一些文件系统：

$ df -h /dev/ada1p2 Filesystem Size Used Avail Capacity Mounted on /dev/ada1p2 213G 152G 44G 78% / 

[参见](#__u53C2___u89C1_)
=======================

lsvfs(1), quota(1), fstatfs(2), getfsstat(2), statfs(2), getbsize(3), getmntinfo(3), libxo(3), localeconv(3), xo\_parse\_args(3), fstab(5), mount(8), pstat(8), quot(8), swapinfo(8)

[标准](#__u6807___u51C6_)
=======================

除大多数选项外， `df` 实用程序符合 IEEE Std 1003.1-2004 (“POSIX.1”) ，它仅定义 `-k`, `-P` 和 `-t` 选项。

[历史](#__u5386___u53F2_)
=======================

`df` 命令出现在 Version 1 AT&T UNIX 中。

[缺陷](#__u7F3A___u9677_)
=======================

如果指定了文件或文件系统，则忽略 `-n` 标志。 此外，如果用户无法访问安装点，则文件系统信息可能已过时。

`-b` 和 `-P` 选项是相同的。 前者来自 BSD 传统，后者是 IEEE Std 1003.1-2004 (“POSIX.1”) 一致性所必需的。

October 5, 2020

FreeBSD 13.1-RELEASE