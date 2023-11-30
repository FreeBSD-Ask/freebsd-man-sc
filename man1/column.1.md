  COLUMN(1)  

COLUMN(1)

FreeBSD General Commands Manual

COLUMN(1)

[名称](#__u540D___u79F0_)
=======================

`column` —

columnate lists

[概要](#__u6982___u8981_)
=======================

`column` \[`-tx`\] \[`-c` columns\] \[`-s` sep\] \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`column` 实用程序将其输入格式化为多个列。行在列之前填充。 输入来 file 操作数，或者默认情况下来自标准输入。 空行被忽略。

选项如下：

[`-c`](#c)

输出格式化为显示 columns 宽。

[`-s`](#s)

为 `-t` 选项指定一组用于分隔列的字符。

[`-t`](#t)

确定输入包含的列数并创建一个表。 默认情况下，列使用空格或使用 `-s` 选项提供的字符分隔。 对于漂亮的打印显示很有用。

[`-x`](#x)

在填充行之前填充列。

[环境](#__u73AF___u5883_)
=======================

`COLUMNS 、 LANG 、 LC_ALL` 和 `LC_CTYPE` 环境变量会影响 `column` 的执行，如 environ(7) 中所述。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `column` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

`(printf "PERM LINKS OWNER GROUP SIZE MONTH DAY " ; \`

`printf "HH:MM/YEAR NAME\n" ; \`

`ls -l | sed 1d) | column -t`

[参见](#__u53C2___u89C1_)
=======================

colrm(1), ls(1), paste(1), sort(1)

[历史](#__u5386___u53F2_)
=======================

`column` 命令出现在 4.3BSD-Reno 中。

[缺陷](#__u7F3A___u9677_)
=======================

输入行的长度限制为 `LINE_MAX` (2048) 个字节。

July 29, 2004

FreeBSD 13.1-RELEASE