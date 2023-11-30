  IDENT(1)  

IDENT(1)

FreeBSD General Commands Manual

IDENT(1)

[名称](#__u540D___u79F0_)
=======================

`ident` —

识别文件中的 RCS 关键字字符串

[概要](#__u6982___u8981_)
=======================

`ident` \[`-q`\] \[`-V`\] \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`ident` 实用程序在 files 中搜索模式 ‘$keyword: text$’ 的所有实例。

如果没有传递参数，则 `ident` 解析标准输入。

_keyword_ 只能由 C 语言环境中的字母数字值组成，后跟 ‘:’ 和一个空格。

支持这些选项：

[`-q`](#q)

安静模式：如果没有找到模式，则禁止警告。

[`-V`](#V)

什么都不做，为了与 GNU ident 兼容而添加。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `ident` utility exits 0 on success, and >0 if an error occurs.

[作者](#__u4F5C___u8005_)
=======================

此版本的 `ident` 实用程序由 Baptiste Daroussin <[bapt@FreeBSD.org](mailto:bapt@FreeBSD.org)\> 编写。

July 25, 2015

FreeBSD 13.1-RELEASE