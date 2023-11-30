  NEWALIASES(1)  

NEWALIASES(1)

FreeBSD General Commands Manual

NEWALIASES(1)

[名称](#__u540D___u79F0_)
=======================

newaliases - 为邮件别名文件重建数据库

[概要](#__u6982___u8981_)
=======================

**newaliases**

[描述](#__u63CF___u8FF0_)
=======================

**Newaliases** 为邮件别名文件 /etc/mail/aliases。重建随机访问数据库。每次更改此文件时都必须运行它才能使更改生效。

**Newaliases** 与 \`\`sendmail -bi'' 相同。

The **newaliases** 实用程序在成功时退出 0 ，如果发生错误则 > 0。

注意： **不要** 使用 **makemap** 创建别名数据库，因为 **newaliases** 会在数据库中放入 **sendmail 所需的特殊标记。**

[文件](#__u6587___u4EF6_)
=======================

/etc/mail/aliases

邮件别名文件

[参见](#__u53C2___u89C1_)
=======================

aliases(5), sendmail(8)

[历史](#__u5386___u53F2_)
=======================

The **newaliases** 命令出现在 4.0BSD 中。

$Date: 2013-11-22 20:51:56 $