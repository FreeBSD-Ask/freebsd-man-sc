  MAN(1)  

MAN(1)

FreeBSD General Commands Manual

MAN(1)

[名称](#__u540D___u79F0_)
=======================

`man` —

显示在线手册文档页面

[概要](#__u6982___u8981_)
=======================

`man` \[`-adho`\] \[`-t` | `-w`\] \[`-M` manpath\] \[`-P` pager\] \[`-S` mansect\] \[`-m` arch\[:machine\]\] \[`-p` \[eprtv\]\] \[mansect\] page ... `man` `-f` keyword ... `man` `-k` keyword ...

[描述](#__u63CF___u8FF0_)
=======================

`man` 实用程序查找并显示在线手册文档页面。 如果提供 mansect ，则 `man` 将搜索限制在手册的特定部分。

手册的章节是：

1.  FreeBSD 通用命令手册
2.  FreeBSD 系统调用手册
3.  FreeBSD 库函数手册
4.  FreeBSD 内核接口手册
5.  FreeBSD 文件格式手册
6.  FreeBSD 游戏手册
7.  FreeBSD 杂项信息手册
8.  FreeBSD 系统管理手册
9.  FreeBSD 内核开发手册

`man` 理解的选项:

[`-M`](#M) manpath

强制使用特定的冒号分隔的手动路径而不是默认搜索路径。请参见 manpath(1) 。覆盖 `MANPATH` 环境变量。

[`-P`](#P) pager

使用指定的寻呼机。如果启用颜色支持，则默认为 “`less -sR`” 或 “`less -s 。覆盖`” `MANPAGER` 环境变量，进而覆盖 `PAGER` 环境变量。

[`-S`](#S) mansect

将搜索的手动部分限制为指定的冒号分隔列表。默认为 “`1:8:2:3:3lua:n:4:5:6:7:9:l`” 。覆盖 `MANSECT` 环境变量。

[`-a`](#a)

显示所有手册页，而不仅仅是为每个 page 参数找到的第一个。

[`-d`](#d)

打印额外的调试信息。重复以增加详细程度。不显示手册页。

[`-f`](#f)

模拟 whatis(1) 。

[`-h`](#h)

显示简短的帮助信息并退出。

[`-k`](#k)

模拟 apropos(1) 。

[`-m`](#m) arch\[:machine\]

覆盖默认架构和机器设置，允许查找其他平台特定的手册页。有关此选项如何更改默认行为的信息，请参见 [IMPLEMENTATION NOTES](#IMPLEMENTATION_NOTES) 。覆盖 `MACHINE_ARCH` 和 `MACHINE` 环境变量。

[`-o`](#o)

强制使用非本地化的手册页。有关特定于区域设置的搜索的工作方式，请参见 [IMPLEMENTATION NOTES](#IMPLEMENTATION_NOTES) 。覆盖 `LC_ALL`, `LC_CTYPE`, 和 `LANG` 环境变量。

[`-p`](#p) \[`eprtv`\]

在运行 nroff(1) 或 troff(1). 之前使用给定预处理器的列表。有效的预处理器参数：

[`e`](#e)

eqn(1)

[`p`](#p_2)

pic(1)

[`r`](#r)

refer(1)

[`t`](#t)

tbl(1)

[`v`](#v)

vgrind(1)

覆盖 `MANROFFSEQ` 环境变量。

[`-t`](#t_2)

通过 troff(1) 发送手册页源，允许将手册页转换为其他格式。

[`-w`](#w)

显示手册页的位置而不是手册页的内容。

[实现说明](#__u5B9E___u73B0___u8BF4___u660E_)
=========================================

[特定于区域设置的搜索](#__u7279___u5B9A___u4E8E___u533A___u57DF___u8BBE___u7F6E___u7684___u641C___u7D22_)
-----------------------------------------------------------------------------------------------

`man` 实用程序支持不同语言环境的手册页。搜索行为由具有非空字符串的三个环境变量中的第一个决定： `LC_ALL`, `LC_CTYPE` 或 `LANG 。` 如果设置， `man` 将使用以下逻辑搜索特定于语言环境的手册页：

*   lang\_country.charset
*   lang.charset
*   [`en`](#en).charset

例如，如果 `LC_ALL` 设置为 “`ja_JP.eucJP`”, 当考虑 /usr/share/man 中的第 1 节手册页时， `man` 将搜索以下路径：

*   /usr/share/man/ja\_JP.eucJP/man1
*   /usr/share/man/ja.eucJP/man1
*   /usr/share/man/en.eucJP/man1
*   /usr/share/man/man1

[平台特定搜索](#__u5E73___u53F0___u7279___u5B9A___u641C___u7D22_)
-----------------------------------------------------------

`man` 实用程序支持特定于平台的手册页。搜索行为由 `-m` 选项或 `MACHINE_ARCH` 和 `MACHINE` 环境变量决定。例如，如果 `MACHINE_ARCH` 设置为 “`aarch64`” 并且 `MACHINE` 设置为 “`arm64`”, 则当考虑 /usr/share/man 中的第 4 节手册页时， `man` 将搜索以下路径：

*   /usr/share/man/man4/aarch64
*   /usr/share/man/man4/arm64
*   /usr/share/man/man4

[显示特定的手动文件](#__u663E___u793A___u7279___u5B9A___u7684___u624B___u52A8___u6587___u4EF6_)
--------------------------------------------------------------------------------------

如果传递了文件的路径，只要它包含 ‘`/`’ 字符， `man` 实用程序还支持显示特定的手册页。

[环境](#__u73AF___u5883_)
=======================

以下环境变量影响 `man` 的执行：

[`LC_ALL`](#LC_ALL), `LC_CTYPE`, `LANG`

用于查找特定于语言环境的手册页。可以通过运行 locale(1) 命令找到有效值。有关详细信息，请参阅 [IMPLEMENTATION NOTES](#IMPLEMENTATION_NOTES) 。受 `-o` 选项的影响。

[`MACHINE_ARCH`](#MACHINE_ARCH), `MACHINE`

用于查找特定于平台的手册页。如果未设置，则分别使用 “`sysctl hw.machine_arch`” 和 “`sysctl hw.machine`” 的输出。有关详细信息，请参阅 [IMPLEMENTATION NOTES](#IMPLEMENTATION_NOTES) 。对应于 `-m` 选项。

[`MANPATH`](#MANPATH)

man(1) 使用的标准搜索路径可以通过在 `MANPATH` 环境变量中指定路径来更改。无效路径或没有手动数据库的路径将被忽略。被 `-M` 覆盖。如果 `MANPATH` 以冒号开头，则附加到默认列表中；如果它以冒号结尾，则添加到默认列表中；或者如果它包含两个相邻的冒号，则在冒号之间插入标准搜索路径。如果这些条件都不满足，它会覆盖标准搜索路径。

[`MANROFFSEQ`](#MANROFFSEQ)

用于在运行 nroff(1) 或 troff(1) 之前确定手动源的预处理器。如果未设置，则默认为 tbl(1) 。对应于 `-p` 选项。

[`MANSECT`](#MANSECT)

将搜索的手动部分限制为指定的冒号分隔列表。对应于 `-S` 选项。

[`MANWIDTH`](#MANWIDTH)

如果设置为数值，则应显示手册页的宽度。否则，如果设置为特殊值 “`tty`” ，并且输出到终端，则页面可能会显示在屏幕的整个宽度上。

[`MANCOLOR`](#MANCOLOR)

如果设置，则启用颜色支持。

[`MANPAGER`](#MANPAGER)

用于显示文件的程序。

如果未设置，并且启用了颜色支持，则使用 “`less -sR`” 。

如果未设置，并且禁用颜色支持，则使用 `PAGER` 。如果这也没有值，则使用 “`less -s`” 。

[文件](#__u6587___u4EF6_)
=======================

/etc/man.conf

系统配置文件。

/usr/local/etc/man.d/\*.conf

本地配置文件。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `man` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示 stat(2) 的手册页：

$ man 2 stat 

显示 ‘`stat`’ 的所有手册页。

$ man -a stat 

列出与标题或正文中的正则表达式匹配的手册页：

$ man -k '\\<copy\\>.\*archive' 

显示 ls(1) 的手册页并使用 cat(1) 作为寻呼机：

$ man -P cat ls 

显示 ls(1) 手册页的位置：

$ man -w ls 

[参见](#__u53C2___u89C1_)
=======================

apropos(1), intro(1), mandoc(1), manpath(1), whatis(1), intro(2), intro(3), intro(3lua), intro(4), intro(5), man.conf(5), intro(6), intro(7), mdoc(7), intro(8), intro(9)

January 9, 2021

FreeBSD 13.1-RELEASE