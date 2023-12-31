  LOGIN(1)  

LOGIN(1)

FreeBSD General Commands Manual

LOGIN(1)

[名称](#__u540D___u79F0_)
=======================

`login` —

登录计算机

[概要](#__u6982___u8981_)
=======================

`login` \[`-fp`\] \[`-h` hostname\] \[user\]

[描述](#__u63CF___u8FF0_)
=======================

`login` 实用程序将用户（和伪用户）登录到计算机系统中。

如果未指定用户，或者如果指定了用户并且用户身份验证失败，则 `login` 会提示输入用户名。 用户的身份验证可通过 pam(8) 进行配置。 密码验证是默认设置。

可以使用以下选项：

[`-f`](#f)

当指定用户名时，此选项表示已完成正确的身份验证并且不需要请求密码。 此选项只能由超级用户使用，或者当已经登录的用户以自己的身份登录时使用。

[`-h`](#h)

指定从其接收连接的主机。 它被各种守护进程使用，例如 telnetd(8) 。 此选项只能由超级用户使用。

[`-p`](#p)

默认情况下， `login` 会丢弃任何以前的环境。 `-p` 选项禁用此行为。

访问可以通过 login.access(5) 或 login.conf(5) 中的登录类来控制，它提供基于时间、tty 和远程主机名的允许和拒绝记录。

如果文件 /etc/fbtab 存在， `login` 会更改此文件中指定的某些设备的保护和所有权。

用户登录后， `login` 会立即显示系统版权声明、用户上次登录的日期和时间、当天的消息以及其他信息。 如果文件 .hushlogin 存在于用户的主目录中，则所有这些消息都将被禁止。 这是为了简化非人类用户的登录，例如 uucp(1) 。

`login` 实用程序将信息输入环境（请参阅 environ(7) ），指定用户的主目录 (HOME)、命令解释器 (SHELL)、搜索路径 (PATH)、终端类型 (TERM) 和用户名（LOGNAME 和 USER） . 由于登录类能力数据库中的条目，可能会为用户的系统密码记录中分配的登录类设置其他环境变量。 登录类还控制授予登录的最大和当前进程资源限制、进程优先级和用户登录环境的许多其他方面。

某些 shell 可能提供与此实用程序类似或相同的内置 `login` 命令。 请参阅 builtin(1) 手册页。

当登录成功或失败时， `login` 实用程序将提交审核记录。 无法确定当前审计状态将导致 `login` 时出错退出。

[文件](#__u6587___u4EF6_)
=======================

/etc/fbtab

更改设备保护

/etc/login.conf

登录类能力数据库

/var/run/motd

每日消息

/var/mail/user

系统邮箱

.hushlogin

让登录更安静

/etc/pam.d/login

pam(8) 配置文件

/etc/security/audit\_user

用于审核的用户标志

/etc/security/audit\_control

用于审计的全局标志

[参见](#__u53C2___u89C1_)
=======================

builtin(1), chpass(1), csh(1), newgrp(1), passwd(1), rlogin(1), getpass(3), fbtab(5), login.access(5), login.conf(5), environ(7)

[历史](#__u5386___u53F2_)
=======================

`login` 实用程序出现在 Version 6 AT&T UNIX 中。

July 20, 2019

FreeBSD 13.1-RELEASE