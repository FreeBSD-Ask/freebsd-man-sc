  UNIQ(1)  

UNIQ(1)

FreeBSD General Commands Manual

UNIQ(1)

[名称](#__u540D___u79F0_)
=======================

`uniq` —

报告或过滤掉文件中的重复行

[概要](#__u6982___u8981_)
=======================

`uniq` \[`-c` | `-d` | `-D` | `-u`\] \[`-i`\] \[`-f` num\] \[`-s` chars\] \[input\_file \[output\_file\]\]

[描述](#__u63CF___u8FF0_)
=======================

`uniq` 实用程序读取指定的 input\_file 比较相邻行，并将每个唯一输入行的副本写入 output\_file 。 如果 input\_file 是单个破折号 (‘`-`’) 或不存在，则读取标准输入。 如果 output\_file 不存在，则使用标准输出进行输出。 不写入相同相邻输入行的第二个和后续副本。 如果输入中的重复行不相邻，则不会检测到它们，因此可能需要先对文件进行排序。

可以使用以下选项：

[`-c`](#c), `--count`

在每个输出行之前加上该行在输入中出现的次数，后跟一个空格。

[`-d`](#d), `--repeated`

输出在输入中重复的每一行的单个副本。

[`-D`](#D), `--all-repeated` \[septype\]

输出所有重复的行（如 `-d`, 但重复行的每个副本都被写入）。 可选的 septype 参数控制如何分隔输出中的重复行组；它必须是以下值之一：

none

不要分隔行组（这是默认设置）。

prepend

在每组行之前输出一个空行。

separate

在每组行之后输出一个空行。

[`-f`](#f) num, `--skip-fields` num

进行比较时忽略每个输入行中的第一个 num 字段。 字段是由空格与相邻字段分隔的非空白字符串。 字段编号是基于一的，即第一个字段是字段一。

[`-i`](#i), `--ignore-case`

不区分大小写的行比较。

[`-s`](#s) chars, `--skip-chars` chars

进行比较时忽略每个输入行中的第一个 chars 字符。 如果与 `-f`, `--unique` 选项一起指定，则第一个 num 字段之后的第一个 chars 字符将被忽略。 字符编号是基于一的，即第一个字符是字符一。

[`-u`](#u), `--unique`

仅输出在输入中不重复的行。

[环境](#__u73AF___u5883_)
=======================

`LANG`, `LC_ALL`, `LC_COLLATE` 和 `LC_CTYPE` 环境变量会影响 `uniq` 的执行，如 environ(7) 中所述。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `uniq` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

假设一个名为 city.txt 的文件具有以下内容：

Madrid Lisbon Madrid 

以下命令报告三个不同的行，因为相同的元素不相邻：

$ uniq -u cities.txt Madrid Lisbon Madrid 

对文件进行排序并计算相同行的数量：

$ sort cities.txt | uniq -c 1 Lisbon 2 Madrid 

假设文件 city.txt 的内容如下：

madrid Madrid Lisbon 

显示忽略大小写的重复行：

$ uniq -d -i cities.txt madrid 

与上面相同，但显示了整组重复行：

$ uniq -D -i cities.txt madrid Madrid 

报告忽略每行的第一个字符的相同行数：

$ uniq -s 1 -c cities.txt 2 madrid 1 Lisbon 

[兼容性](#__u517C___u5BB9___u6027_)
================================

历史上的 `+`number 和 `-`number 选项已被弃用，但在此实现中仍受支持。

[参见](#__u53C2___u89C1_)
=======================

sort(1)

[标准](#__u6807___u51C6_)
=======================

`uniq` 实用程序符合经 Cor 修订的 IEEE Std 1003.1-2001 (“POSIX.1”) as amended by Cor. 1-2002。

[历史](#__u5386___u53F2_)
=======================

`uniq` 命令出现在 Version 3 AT&T UNIX 中。

June 7, 2020

FreeBSD 13.1-RELEASE