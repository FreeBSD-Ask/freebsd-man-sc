  UNAME(1)  

UNAME(1)

FreeBSD General Commands Manual

UNAME(1)

[名称](#__u540D___u79F0_)
=======================

`uname` —

显示有关系统的信息

[概要](#__u6982___u8981_)
=======================

`uname` \[`-abiKmnoprsUv`\]

[描述](#__u63CF___u8FF0_)
=======================

`uname` 命令将操作系统实现的名称写入标准输出。 指定选项时，表示一个或多个系统特征的字符串将写入标准输出。

选项如下：

[`-a`](#a)

表现得好像指定了选项 `-m`, `-n`, `-r`, `-s`, 和 `-v` 。

[`-b`](#b)

将内核的链接器生成的 build-id 写入标准输出。

[`-i`](#i)

将内核标识写入标准输出。

[`-K`](#K)

编写内核的 FreeBSD 版本。

[`-m`](#m)

将当前硬件平台的类型写入标准输出。 (make(1) 使用它来设置 MACHINE 变量。)

[`-n`](#n)

将系统名称写入标准输出。

[`-o`](#o)

这是 `-s` 选项的同义词，用于与其他系统兼容。

[`-p`](#p)

将机器处理器架构的类型写入标准输出。 (make(1) 使用它来设置 MACHINE\_ARCH 变量。)

[`-r`](#r)

将操作系统的当前版本级别写入标准输出。

[`-s`](#s)

将操作系统实现的名称写入标准输出。

[`-U`](#U)

编写 FreeBSD 版本的用户环境。

[`-v`](#v)

将此版本操作系统的版本级别写入标准输出。

如果指定了 `-a` 标志，或者指定了多个标志，则所有输出都写在一行上，以空格分隔。

`-K` 和 `-U` 标志旨在用于对增量 FreeBSD 开发和用户可见更改进行细粒度区分。 请注意，当这两个选项都指定时，无论它们的顺序如何，都将首先打印内核版本，然后是用户环境版本。

[环境](#__u73AF___u5883_)
=======================

由字符串 `UNAME_` 后跟 `uname` 实用程序的任何标志（ `-a` 除外）组成的环境变量将允许将相应的数据设置为环境变量的内容。 有关详细信息，请参阅 uname(3) 。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `uname` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

硬件平台 (`-m`) 可以与机器的处理器架构 (`-p`) 不同，例如，在 64 位 PowerPC 上， `-m` 将返回 powerpc ， `-p` 将返回 powerpc64 。

[参见](#__u53C2___u89C1_)
=======================

feature\_present(3), getosreldate(3), sysctl(3), uname(3), sysctl(8)

[标准](#__u6807___u51C6_)
=======================

`uname` 命令应符合 IEEE Std 1003.2 (“POSIX.2”) 规范。

[历史](#__u5386___u53F2_)
=======================

`uname` 命令出现在 PWB UNIX 1.0 中，但是 4.4BSD 是第一个带有 `uname` 命令的 Berkeley 版本。

`-K` 和 `-U` 扩展标志出现在 FreeBSD 10.0 中。 `-b` 扩展标志出现在 FreeBSD 13.0 中。

November 13, 2020

FreeBSD 13.1-RELEASE