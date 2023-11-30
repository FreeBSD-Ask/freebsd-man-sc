  REVOKE(1)  

REVOKE(1)

FreeBSD General Commands Manual

REVOKE(1)

[名称](#__u540D___u79F0_)
=======================

`revoke` —

撤销一个字符设备

[概要](#__u6982___u8981_)
=======================

`revoke` file ...

[描述](#__u63CF___u8FF0_)
=======================

`revoke` 程序使用 revoke(2) 撤销字符设备。在TTY上使用时，像 read(2), write(2) 和 ioctl(2), 这样的调用将立即中止，从而有效地终止登录会话。

[参见](#__u53C2___u89C1_)
=======================

revoke(2)

[历史](#__u5386___u53F2_)
=======================

`revoke` 程序最早出现在 FreeBSD 8.0 中。

[作者](#__u4F5C___u8005_)
=======================

Ed Schouten <[ed@FreeBSD.org](mailto:ed@FreeBSD.org)\>

June 15, 2009

FreeBSD 13.1-RELEASE