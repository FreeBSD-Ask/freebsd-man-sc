  COLRM(1)  

COLRM(1)

FreeBSD General Commands Manual

COLRM(1)

[名称](#__u540D___u79F0_)
=======================

`colrm` —

从文件中删除列

[概要](#__u6982___u8981_)
=======================

`colrm` \[start \[stop\]\]

[描述](#__u63CF___u8FF0_)
=======================

`colrm` 实用程序从文件的行中删除选定的列。 列定义为一行中的单个字符。 从标准输入读取输入。 输出被写入标准输出。

如果只指定了 start 列，则将写入编号小于 start 列的列。 如果同时指定了 start 列和 stop 列，则将写入编号小于 start 列或大于 stop 列的列。 列编号从一开始，而不是零。

制表符将列计数增加到下一个八的倍数。 退格字符将列计数减一。

[环境](#__u73AF___u5883_)
=======================

`LANG 、 LC_ALL` 和 `LC_CTYPE` 环境变量会影响 `colrm` 的执行，如 environ(7) 中所述。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `colrm` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示低于 3 (c) 和高于 5 (e) 的列：

$ echo -e "abcdefgh\\n12345678" | colrm 3 5 abfgh 12678 

允许指定大于文件中列数的起始列并显示所有列：

$ echo "abcdefgh" | colrm 100 abcdefgh 

使用 1 作为开始列将不显示任何内容：

$ echo "abcdefgh" | colrm 1 

[参见](#__u53C2___u89C1_)
=======================

awk(1), column(1), cut(1), paste(1)

[历史](#__u5386___u53F2_)
=======================

`colrm` 实用程序首先出现在 1BSD 中。

[作者](#__u4F5C___u8005_)
=======================

Jeff Schriebman 于 1974 年 11 月编写了 `colrm` 的原始版本。

June 23, 2020

FreeBSD 13.1-RELEASE