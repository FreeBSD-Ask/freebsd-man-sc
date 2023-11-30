  CTFDUMP(1)  

CTFDUMP(1)

FreeBSD General Commands Manual

CTFDUMP(1)

[名称](#__u540D___u79F0_)
=======================

`ctfdump` —

转储 ELF 文件的 SUNW\_ctf 部分

[概要](#__u6982___u8981_)
=======================

`ctfdump` \[`-dfhlsSt`\] `-u` file file

[描述](#__u63CF___u8FF0_)
=======================

`ctfdump` 实用程序转储 ELF 二进制文件中存在的 CTF 数据段 (SUNW\_ctf) 的内容。 此部分之前是使用 ctfconvert(1) 或 ctfmerge(1) 创建的。

可以使用以下选项：

[`-d`](#d)

显示数据对象部分。

[`-f`](#f)

显示函数部分。

[`-h`](#h)

显示标题。

[`-l`](#l)

显示标签部分。

[`-s`](#s)

显示字符串表。

[`-S`](#S)

显示统计信息。

[`-t`](#t)

显示类型部分。

[`-u`](#u) ufile

将未压缩的 CTF 数据写入名为 ufile 的原始 CTF 文件。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `ctfdump` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

ctfconvert(1), ctfmerge(1)

[历史](#__u5386___u53F2_)
=======================

`ctfdump` 实用程序首次出现在 FreeBSD 7.0 中。

[作者](#__u4F5C___u8005_)
=======================

CTF 实用程序来自 OpenSolaris。

July 7, 2010

FreeBSD 13.1-RELEASE