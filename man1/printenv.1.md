  PRINTENV(1)  

PRINTENV(1)

FreeBSD General Commands Manual

PRINTENV(1)

[名称](#__u540D___u79F0_)
=======================

`printenv` —

打印环境

[概要](#__u6982___u8981_)
=======================

`printenv` \[name\]

[描述](#__u63CF___u8FF0_)
=======================

`printenv` 实用程序打印出环境中变量的名称和值，每行一个名称/值对。 如果指定了 name ，则仅打印其值。

某些 shell 可能提供与此实用程序类似或相同的内置 `printenv` 命令。 请参阅 builtin(1) 手册页。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `printenv` utility exits 0 on success, and >0 if an error occurs.

[SEE ALSO](#SEE_ALSO)
=====================

csh(1), env(1), sh(1), environ(7)

[标准](#__u6807___u51C6_)
=======================

提供 `printenv` 实用程序是为了与早期的 BSD 和 FreeBSD 版本兼容，并且没有任何标准指定。 `printenv` 的功能可以通过 echo(1) 和 env(1) 实用程序来复制。

[历史](#__u5386___u53F2_)
=======================

`printenv` 命令出现在 3.0BSD 中。

May 12, 2003

FreeBSD 13.1-RELEASE