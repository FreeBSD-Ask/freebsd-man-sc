  RWHO(1)  

RWHO(1)

FreeBSD General Commands Manual

RWHO(1)

[名称](#__u540D___u79F0_)
=======================

`rwho` —

谁在本地机器上登录

[概要](#__u6982___u8981_)
=======================

`rwho` \[`-a`\]

[描述](#__u63CF___u8FF0_)
=======================

`rwho` 命令产生类似于 who(1) 的输出，但针对本地网络上的所有机器。 如果 11 分钟内没有收到来自机器的报告，则 `rwho`-
假定该机器已关闭，并且不报告最后已知登录该机器的用户。

如果用户一分钟或更长时间没有向系统键入内容，则 `rwho` 会报告此空闲时间。

以下选项可用：

[`-a`](#a)

包括所有用户。 默认情况下，如果用户一小时或更长时间未向系统输入内容，则输出中将省略该用户。

[文件](#__u6587___u4EF6_)
=======================

/var/rwho/whod.\*

关于其他机器的信息

[参见](#__u53C2___u89C1_)
=======================

ruptime(1), who(1), rwhod(8)

[历史](#__u5386___u53F2_)
=======================

`rwho` 命令出现在 4.3BSD 中。

[缺陷](#__u7F3A___u9677_)
=======================

当本地网络上的机器数量很大时，这很不方便。

August 8, 2017

FreeBSD 13.1-RELEASE