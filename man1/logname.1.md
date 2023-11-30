  LOGNAME(1)  

LOGNAME(1)

FreeBSD General Commands Manual

LOGNAME(1)

[名称](#__u540D___u79F0_)
=======================

`logname` —

显示用户的登录名

[概要](#__u6982___u8981_)
=======================

`logname`

[描述](#__u63CF___u8FF0_)
=======================

`logname` 实用程序将用户的登录名写入标准输出，后跟换行符。

`logname` 实用程序显式忽略 `LOGNAME` 和 `USER` 环境变量，因为环境不可信。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `logname` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

who(1), whoami(1), getlogin(2)

[标准](#__u6807___u51C6_)
=======================

`logname` 实用程序应符合 IEEE Std 1003.2 (“POSIX.2”) 。

[历史](#__u5386___u53F2_)
=======================

`logname` 命令出现在 4.4BSD 中。

June 9, 1993

FreeBSD 13.1-RELEASE