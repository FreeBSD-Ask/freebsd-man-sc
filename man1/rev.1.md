  REV(1)  

REV(1)

FreeBSD General Commands Manual

REV(1)

[名称](#__u540D___u79F0_)
=======================

`rev` —

反转文件的行

[概要](#__u6982___u8981_)
=======================

`rev` \[file ...\]

[描述](#__u63CF___u8FF0_)
=======================

`rev` 实用程序将指定的文件复制到标准输出，并反转每行中的字符顺序。如果没有指定文件，则读取标准输入。

[实例](#__u5B9E___u4F8B_)
=======================

从 stdin 反转文本:

$ echo -e "reverse \\t these\\ntwo lines" | rev eseht esrever senil owt 

June 27, 2020

FreeBSD 13.1-RELEASE