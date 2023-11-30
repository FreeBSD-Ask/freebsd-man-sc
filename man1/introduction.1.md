  INTRO(1)  

INTRO(1)

FreeBSD General Commands Manual

INTRO(1)

[名称](#__u540D___u79F0_)
=======================

`intro` —

介绍一般命令（工具和实用程序）

[描述](#__u63CF___u8FF0_)
=======================

手册的第一部分包含了构成 BSD 用户环境的大部分命令。 第一节中包含的一些命令是文本编辑器、命令 shell 解释器、搜索和排序工具、文件操作命令、系统状态命令、远程文件复制命令、邮件命令、编译器和编译器工具、格式化输出工具和行式打印机命令.

所有命令在退出时都会设置一个状态值，可以对其进行测试以查看命令是否正常完成。 传统上，值 0 表示命令成功完成，而值 > 0 表示错误。 一些命令尝试通过使用 sysexits(3) 中定义的退出代码来描述故障的性质，而其他命令只是将状态设置为任意值 >0（通常为 1）。

[参见](#__u53C2___u89C1_)
=======================

apropos(1), man(1), intro(2), intro(3), sysexits(3), intro(4), intro(5), intro(6), intro(7), security(7), intro(8), intro(9)

教程在 UNIX User's Manual Supplementary Documents 。

[历史](#__u5386___u53F2_)
=======================

`intro` 手册页出现在 Version 6 AT&T UNIX 中。

October 21, 2001

FreeBSD 13.1-RELEASE