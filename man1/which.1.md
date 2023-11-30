  WHICH(1)  

WHICH(1)

FreeBSD General Commands Manual

WHICH(1)

[名称](#__u540D___u79F0_)
=======================

`which` —

在用户路径中找到一个程序文件

[概要](#__u6982___u8981_)
=======================

`which` \[`-as`\] program ...

[描述](#__u63CF___u8FF0_)
=======================

`which` utility 实用程序获取一个命令名称列表，并搜索在实际调用这些命令时将运行的每个可执行文件的路径。

可以使用以下选项：

[`-a`](#a)

列出找到的所有可执行文件实例（而不仅仅是每个实例的第一个）。

[`-s`](#s)

没有输出，如果找到所有可执行文件，则返回 0，如果没有找到，则返回 1。

某些 shell 可能会提供与此实用程序相似或相同的内置 `which` 命令。 请参阅 builtin(1) 手册页。

[实例](#__u5B9E___u4F8B_)
=======================

找到 ls(1) 和 cp(1) 命令：

$ /usr/bin/which ls cp /bin/ls /bin/cp 

与上面相同的特定 `PATH` 并显示所有出现：

$ PATH=/bin:/rescue /usr/bin/which -a ls cp /bin/ls /rescue/ls /bin/cp /rescue/cp 

如果多次找到相同的可执行文件， `which` 将显示重复的结果:

$ PATH=/bin:/bin /usr/bin/which -a ls /bin/ls /bin/ls 

不显示输出。 只需使用适当的返回码退出：

$ /usr/bin/which -s ls cp $ echo $? 0 $ /usr/bin/which -s fakecommand $ echo $? 1 

[参见](#__u53C2___u89C1_)
=======================

builtin(1), csh(1), find(1), locate(1), whereis(1)

[历史](#__u5386___u53F2_)
=======================

`which` 命令最早出现在 FreeBSD 2.1 中。

[作者](#__u4F5C___u8005_)
=======================

`which` 实用程序最初是用 Perl 编写的，由 Wolfram Schneider <[wosch@FreeBSD.org](mailto:wosch@FreeBSD.org)\>. 贡献。 `which` 的当前版本是由 Daniel Papasian <[dpapasia@andrew.cmu.edu](mailto:dpapasia@andrew.cmu.edu)\> 用C重写的。

September 24, 2020

FreeBSD 13.1-RELEASE