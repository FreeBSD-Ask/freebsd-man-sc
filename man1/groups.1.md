  GROUPS(1)  

GROUPS(1)

FreeBSD General Commands Manual

GROUPS(1)

[名称](#__u540D___u79F0_)
=======================

`groups` —

show group memberships

[概要](#__u6982___u8981_)
=======================

`groups` \[user\]

[描述](#__u63CF___u8FF0_)
=======================

The `groups`-
实用程序已被 id(1) 实用程序淘汰，相当于 “`id` `-Gn` \[user\]” 。 建议将命令 “`id` `-p`” 用于正常的交互使用。

`groups` 实用程序显示您（或可选指定的用户）所属的组。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `groups` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示 root 用户所属的组：

$ groups root wheel operator 

[参见](#__u53C2___u89C1_)
=======================

id(1)

June 6, 1993

FreeBSD 13.1-RELEASE