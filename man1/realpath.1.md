  REALPATH(1)  

REALPATH(1)

FreeBSD General Commands Manual

REALPATH(1)

[名称](#__u540D___u79F0_)
=======================

`realpath` —

返回解析的物理路径

[概要](#__u6982___u8981_)
=======================

`realpath` \[`-q`\] \[path ...\]

[描述](#__u63CF___u8FF0_)
=======================

`realpath` 实用程序使用 realpath(3) 函数来解析 path 中的所有符号链接、额外的 ‘`/`’ 字符以及对 /./ 和 /../ 的引用。 如果 path 不存在，则假定为当前工作目录 (‘.’) 。

如果指定了 `-q` ，则当 realpath(3) 失败时不会打印警告。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `realpath` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示 /dev/log-
目录静默警告的物理路径（如果有）：

$ realpath -q /dev/log /var/run/log 

[参见](#__u53C2___u89C1_)
=======================

realpath(3)

[历史](#__u5386___u53F2_)
=======================

`realpath` 实用程序首次出现在 FreeBSD 4.3 中。

June 21, 2011

FreeBSD 13.1-RELEASE