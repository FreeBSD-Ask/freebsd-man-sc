  WHOAMI(1)  

WHOAMI(1)

FreeBSD General Commands Manual

WHOAMI(1)

[名称](#__u540D___u79F0_)
=======================

`whoami` —

显示有效用户 ID

[概要](#__u6982___u8981_)
=======================

`whoami`

[描述](#__u63CF___u8FF0_)
=======================

`whoami` 实用程序已被 id(1) 实用程序淘汰，相当于 “`id` `-un` `-。`” 建议将命令 “`id` `-p`” 用于正常的交互使用。

`whoami` 实用程序将您的有效用户 ID 显示为名称。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `whoami` utility exits 0 on success, and >0 if an error occurs.

[参见](#__u53C2___u89C1_)
=======================

id(1)

June 6, 1993

FreeBSD 13.1-RELEASE