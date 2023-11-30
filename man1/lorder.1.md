  LORDER(1)  

LORDER(1)

FreeBSD General Commands Manual

LORDER(1)

[名称](#__u540D___u79F0_)
=======================

`lorder` —

列出目标文件的依赖关系

[概要](#__u6982___u8981_)
=======================

`lorder` file ...

[描述](#__u63CF___u8FF0_)
=======================

`lorder` 实用程序使用 nm(1) 来确定在命令行中指定的目标文件和库归档列表中的相互依赖关系。 `lorder` 实用程序输出文件名列表，其中第一个文件包含由第二个文件定义的符号。

当创建库以确定目标模块的最佳顺序时，输出通常与 tsort(1) 一起使用，以便可以在加载器的单次传递中解析所有引用。

链接静态二进制文件时，可以使用 `lorder` 和 tsort(1) 自动正确排序库存档。

[环境](#__u73AF___u5883_)
=======================

[`NM`](#NM)

nm(1) 二进制文件的路径，默认为 “`nm`” 。

[`NMFLAGS`](#NMFLAGS)

传递给 nm(1) 的标志。

[实例](#__u5B9E___u4F8B_)
=======================

ar cr library.a \`lorder ${OBJS} | tsort\` cc -o foo ${OBJS} \`lorder ${STATIC\_LIBS} | tsort\` 

[参见](#__u53C2___u89C1_)
=======================

ar(1), ld(1), nm(1), ranlib(1), tsort(1)

[历史](#__u5386___u53F2_)
=======================

在 Version 7 AT&T UNIX 中出现了一个 `lorder` 实用程序。

August 14, 2015

FreeBSD 13.1-RELEASE