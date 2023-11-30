  CONFIG(8)  

CONFIG(8)

FreeBSD System Manager's Manual

CONFIG(8)

[名称](#__u540D___u79F0_)
=======================

`config` —

构建系统配置文件

[概要](#__u6982___u8981_)
=======================

`config` \[`-CVgp`\] \[`-I` path\] \[`-d` destdir\] \[`-s` srcdir\] SYSTEM\_NAME `config` \[`-x` kernel\]

[描述](#__u63CF___u8FF0_)
=======================

`config` 实用程序从描述要配置的系统的文件 SYSTEM\_NAME 构建一组系统配置文件。 第二个文件告诉 `config` 生成系统需要哪些文件，并且可以通过配置特定文件集进行扩充，这些文件为特定机器提供备用文件（请参阅下面的 [FILES](#FILES) 部分）。

可用选项和操作数：

[`-V`](#V)

打印 `config` 版本号。

[`-C`](#C)

如果 INCLUDE\_CONFIG\_FILE 存在于配置文件中，内核映像将包含完整的配置文件（保留注释）。 保留此标志是为了向后兼容。

[`-I`](#I) path

在 path 中搜索 `include` 指令包含的任何文件。 可以多次指定此选项。

[`-d`](#d) destdir

使用 destdir 作为输出目录，而不是默认目录。 请注意， `config` 不会将 SYSTEM\_NAME 附加到给定的目录。

[`-s`](#s) srcdir

使用 srcdir 作为源目录，而不是默认目录。

[`-m`](#m)

打印此内核的 MACHINE 和 MACHINE\_ARCH 值并退出。

[`-g`](#g)

配置系统进行调试。

[`-x`](#x) kernel

打印内核配置文件嵌入到内核文件中。 仅当配置文件中存在 `options INCLUDE_CONFIG_FILE` 条目时，此选项才有意义。

[`-p`](#p)

配置系统进行分析；例如， kgmon(8) 和 gprof(1) 。 如果提供了两个或更多 `-p` 选项，则 `config` 将系统配置为进行高分辨率分析。

SYSTEM\_NAME

为一个系统配置指定包含设备规格、配置选项和其他系统参数的系统配置文件的名称。

`config` 实用程序应该从系统源代码的 conf 子目录（通常是 /sys/ARCH/conf ）运行，其中 ARCH 代表 FreeBSD 支持的架构之一。 `config` 实用程序创建目录 ../compile/SYSTEM\_NAME 或根据需要使用 `-d` 选项指定的目录，并将所有输出文件放在那里。 `config` 的输出由许多文件组成；对于 i386 ，它们是： Makefile, 由 make(1) 用于构建系统；头文件，定义将编译到系统中的各种设备的数量。

`config` 实用程序在目录 ../.. 或使用 `-s` 选项给出的内核源代码中查找内核源代码。

运行 `config` 后，需要在创建新 makefile 的目录中运行 “`make depend`” 。 `config` 实用程序在完成时会打印此提醒。

如果 `config` 产生任何其他错误消息，则应更正配置文件中的问题并再次运行 `config` 。 尝试编译具有配置错误的系统可能会失败。

[调试内核](#__u8C03___u8BD5___u5185___u6838_)
=========================================

由于在编译 “debug” 内核时系统负载过重，传统的 BSD 内核编译时没有符号。 调试内核包含所有源文件的完整符号，使有经验的内核程序员能够分析问题的原因。 4.4BSD-Lite 之前可用的调试器能够从普通内核中找到一些信息； gdb(1) 对普通内核的支持很少，任何有意义的分析都需要调试内核。

由于历史、时间和空间的原因，构建调试内核并不是 FreeBSD 的默认设置：构建调试内核需要多 30% 的时间，并且在构建目录中需要大约 30 MB 的磁盘存储空间，而在构建目录中大约需要 6 MB。非调试内核。 调试内核的大小约为 11 MB，而非调试内核的大小约为 2 MB。 这个空间在根文件系统和运行时都在内存中使用。 使用 `-g` 选项构建调试内核。 使用此选项， `config` 会在内核构建目录中构建两个内核文件：

*   kernel.debug 是完整的调试内核。
*   kernel 是去掉了调试符号的内核副本。 这相当于普通的非调试内核。

目前从调试内核安装和引导几乎没有意义，因为使用这些符号的唯一可用工具不能在线运行。 因此，安装调试内核有两种选择：

*   “`make install`” 在根文件系统中安装 kernel 。
*   “`make install.debug`” 在根文件系统中安装 kernel.debug 。

[文件](#__u6587___u4EF6_)
=======================

/sys/conf/files

通用文件系统列表是从

/sys/conf/Makefile.ARCH

ARCH 的通用 makefile

/sys/conf/files.ARCH

ARCH 特定文件列表

/sys/ARCH/compile/SYSTEM\_NAME

ARCH 上系统 SYSTEM\_NAME 的默认内核构建目录。

[参见](#__u53C2___u89C1_)
=======================

config(5)

第 4 节中每个设备的 [SYNOPSIS](#SYNOPSIS) 部分。 Building 4.3 BSD UNIX System with Config.

[历史](#__u5386___u53F2_)
=======================

`config` 实用程序出现在 4.1BSD 中。

在引入对 `-x` 的支持之前， `options INCLUDE_CONFIG_FILE` 包含了整个配置文件，该配置文件曾经嵌入到新内核中。 这意味着可以使用 strings(1) 从内核中提取它：要提取配置信息，您必须使用以下命令：

`strings -n 3 kernel | sed -n 's/^___//p'`

[缺陷](#__u7F3A___u9677_)
=======================

错误消息中报告的行号通常减一。

June 29, 2020

FreeBSD 13.1-RELEASE