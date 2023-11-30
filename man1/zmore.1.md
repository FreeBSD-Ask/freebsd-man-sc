  ZMORE(1)  

ZMORE(1)

FreeBSD General Commands Manual

ZMORE(1)

[名称](#__u540D___u79F0_)
=======================

`zmore`, `zless` —

查看压缩文件

[概要](#__u6982___u8981_)
=======================

`zmore` \[flags\] \[file ...\] `zless` \[flags\] \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`zmore` 是一个过滤器，允许查看使用 Lempel-Ziv 编码压缩的文件。 此类文件通常具有 “Z” 或 “gz” 扩展名（同时支持 compress(1) 和 gzip(1) 格式）。 指定的任何 flags 都将传递给用户首选的 `PAGER` （默认为 /usr/bin/more )。

`zless` 等价于 `zmore` ，但使用 less(1) 作为寻呼机而不是 more(1) 。

当指定多个文件时， `zmore` 将在每个文件的末尾暂停并向用户显示以下提示：

prev\_file (END) - Next: next\_file 

其中 **prev\_file** 是刚刚显示的文件， **next\_file** 是下一个要显示的文件。 提示符下会识别以下键：

[`e`](#e) 或 `q`

退出 `zmore` 。

[`s`](#s)

跳过下一个文件（如果下一个文件是最后一个文件，则退出）。

如果没有指定文件， `zmore` 将从标准输入读取。 在这种模式下， `zmore` 将假设 gzip(1) 风格的压缩，因为没有后缀可以做出决定。

[环境](#__u73AF___u5883_)
=======================

[`PAGER`](#PAGER)

用于显示文件的程序。 如果未设置，则使用 /usr/bin/more (`zmore`) 或 /usr/bin/less (`zless`) 。

[参见](#__u53C2___u89C1_)
=======================

compress(1), less(1), more(1)

October 22, 2014

FreeBSD 13.1-RELEASE