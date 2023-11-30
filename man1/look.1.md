  LOOK(1)  

LOOK(1)

FreeBSD General Commands Manual

LOOK(1)

[名称](#__u540D___u79F0_)
=======================

`look` —

显示以给定字符串开头的行

[概要](#__u6982___u8981_)
=======================

`look` \[`-df`\] \[`-t` termchar\] string \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`look` 实用程序显示 file 中包含 string 作为前缀的任何行。 由于 `look` 执行二进制搜索，因此必须对文件 file 中的行进行排序。

如果未指定 file ，则使用文件 /usr/share/dict/words ，仅比较字母数字字符，忽略字母字符的大小写。

可以使用以下选项：

[`-d`](#d), `--alphanum`

字典字符集和顺序，即只比较字母数字字符。

[`-f`](#f), `--ignore-case`

忽略字母字符的大小写。

[`-t`](#t), `--terminate` termchar

指定一个字符串终止字符，即只比较 string 中直到并包括第一次出现 termchar 的字符。

[环境](#__u73AF___u5883_)
=======================

`LANG 、 LC_ALL` 和 `LC_CTYPE` 环境变量会影响 `look` 实用程序的执行。 在 environ(7) 中描述了它们的效果。

[文件](#__u6587___u4EF6_)
=======================

/usr/share/dict/words

词典

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

如果找到并显示一行或多行， `look` 实用程序退出 0，如果未找到任何行，则退出 1，如果发生错误，则退出 >1。

[实例](#__u5B9E___u4F8B_)
=======================

在文件 /usr/share/dict/words 中查找以 ‘`xylene`’ 开头的行：

$ look xylen xylene xylenol xylenyl 

与上面相同，但不考虑 string 中第一个 ‘`e`’ 之外的任何字符。 请注意， `-f` 是隐含的，因为我们正在搜索默认文件 /usr/share/dict/words:

$ look -t e xylen Xyleborus xylem xylene xylenol xylenyl xyletic 

[兼容性](#__u517C___u5BB9___u6027_)
================================

原始手册页指出，当指定 `-d` 选项时，制表符和空白字符参与比较。 这是不正确的，当前的手册页与历史实现相匹配。

出于兼容性考虑，忽略 `-a` 和 `--alternative` 标志。

[参见](#__u53C2___u89C1_)
=======================

grep(1), sort(1)

[历史](#__u5386___u53F2_)
=======================

在 Version 7 AT&T UNIX 中出现了 `look` 实用程序。

[缺陷](#__u7F3A___u9677_)
=======================

行不根据当前语言环境的整理顺序进行比较。 输入文件必须在 `LC_COLLATE` 设置为 ‘`C`’ 的情况下进行排序。

December 29, 2020

FreeBSD 13.1-RELEASE