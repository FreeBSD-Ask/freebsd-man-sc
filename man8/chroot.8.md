  CHROOT(8)  

CHROOT(8)

FreeBSD System Manager's Manual

CHROOT(8)

[名称](#__u540D___u79F0_)
=======================

`chroot` —

更改根目录

[概要](#__u6982___u8981_)
=======================

`chroot` \[`-G` group\[`,`group ...\]\] \[`-g` group\] \[`-u` user\] newroot \[command \[arg ...\]\]

[描述](#__u63CF___u8FF0_)
=======================

`chroot` 实用程序将其当前目录和根目录更改为提供的目录 newroot ，然后使用提供的参数（如果提供）或用户登录 shell 的交互式副本执行 exec command 。

选项如下：

[`-G`](#G) group\[`,`group ...\]

以指定组的权限运行命令。

[`-g`](#g) group

以指定 group 的权限运行命令。

[`-u`](#u) user

以 user 身份运行命令。

[环境](#__u73AF___u5883_)
=======================

`chroot` 引用了以下环境变量：

[`SHELL`](#SHELL)

如果设置，则由 `SHELL` 指定的字符串被解释为要执行的 shell 的名称。 如果未设置变量 `SHELL` ，则使用 /bin/sh 。

[实例](#__u5B9E___u4F8B_)
=======================

**示例 1：进入新的根目录**

以下命令在 chroot 到标准根目录后打开 csh(1) shell 。

    #
    

**示例 2：使用更改的根目录执行命令**

以下命令使用 `chroot` 更改根目录，然后运行 ls(1) 以列出 /sbin 的内容。

    #
    

[参见](#__u53C2___u89C1_)
=======================

chdir(2), chroot(2), setgid(2), setgroups(2), setuid(2), getgrnam(3), environ(7), jail(8)

[历史](#__u5386___u53F2_)
=======================

`chroot` 实用程序首先出现在 AT&T System III UNIX 和 4.3BSD-Reno 中。

June 27, 2020

FreeBSD 13.1-RELEASE