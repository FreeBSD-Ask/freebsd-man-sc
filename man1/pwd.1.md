  PWD(1)  

PWD(1)

FreeBSD General Commands Manual

PWD(1)

[名称](#__u540D___u79F0_)
=======================

`pwd` —

return working directory name

[概要](#__u6982___u8981_)
=======================

`pwd` \[`-L` | `-P`\]

[描述](#__u63CF___u8FF0_)
=======================

`pwd` 实用程序将当前工作目录的绝对路径名写入标准输出。

某些 shell 可能提供与此实用程序类似或相同的内置 `pwd` 命令。 请参阅 builtin(1) 手册页。

选项如下：

[`-L`](#L)

显示逻辑当前工作目录。

[`-P`](#P)

显示当前的物理工作目录（所有符号链接都已解析）。

如果未指定任何选项，则假定使用 `-P` 选项。

[环境](#__u73AF___u5883_)
=======================

`pwd` 使用的环境变量：

[`PWD`](#PWD)

逻辑当前工作目录。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `pwd` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示已解析符号链接的当前工作目录：

$ /bin/pwd /usr/home/fernape 

显示逻辑当前目录。然后使用 file(1) 检查 /home 目录：

$ /bin/pwd -L /home/fernape $ file /home /home: symbolic link to usr/home 

[参见](#__u53C2___u89C1_)
=======================

builtin(1), cd(1), csh(1), realpath(1), sh(1), getcwd(3)

[标准](#__u6807___u51C6_)
=======================

`pwd` 实用程序符合 IEEE Std 1003.1-2001 (“POSIX.1”) 。

[历史](#__u5386___u53F2_)
=======================

`pwd` 命令出现在 Version 5 AT&T UNIX 中。

[缺陷](#__u7F3A___u9677_)
=======================

在 csh(1) 中，命令 `dirs` 总是更快，因为它内置在该 shell 中。 但是，在 shell 下降到当前目录或包含目录之后移动的极少数情况下，它可以给出不同的答案。

除非 shell 导出 `PWD` 环境变量，否则 `-L` 选项不起作用。

October 24, 2020

FreeBSD 13.1-RELEASE