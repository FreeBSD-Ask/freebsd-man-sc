  INIT(8)  

INIT(8)

FreeBSD System Manager's Manual

INIT(8)

[名称](#__u540D___u79F0_)
=======================

`init` —

进程控制初始化

[概要](#__u6982___u8981_)
=======================

`init` `init` \[`0` | `1` | `6` | `c` | `q`\]

[描述](#__u63CF___u8FF0_)
=======================

`init` 实用程序是引导过程的最后阶段。 它通常运行 rc(8) 中描述的自动重启序列，如果成功，则开始多用户操作。 如果重新启动脚本失败， `init` 通过在控制台上为超级用户提供一个 shell 来开始单用户操作。 可以从引导程序向 `init` 实用程序传递参数，以防止系统进入多用户状态，而是在不启动正常守护程序的情况下执行单用户 shell。 然后系统处于静止状态以进行维护工作，稍后可以通过退出单用户 shell（使用 ^D）进入多用户。 这会导致 `init` 在快速启动模式下运行 /etc/rc 启动命令文件（跳过磁盘检查）。

如果 ttys(5) 文件中的 _console_ 条目被标记为 “insecure”, 那么 `init` 将要求在系统启动单用户 shell 之前输入超级用户密码。 如果 _console_ 标记为 “secure” ，则跳过密码检查。 请注意，密码检查不能防止从 loader(8) 命令行设置的变量，例如 init\_script ；请参阅 loader(8) 的 [SECURITY](#SECURITY) 部分。

如果系统安全级别（参见 security(7) ）最初为非零，则 `init` 保持不变。 否则， `init` 在第一次进入多用户之前将级别提高到 1。 由于无法降低级别，因此后续操作至少为1，即使返回单用户。 如果在运行多用户时需要高于 1 的级别，可以在进入多用户之前设置它，例如，通过启动脚本 rc(8), 使用 sysctl(8) 将 kern.securelevel 变量设置为所需安全级别。

如果 `init` 在 jail 中运行， “host system” 的安全级别不会受到影响。 在内核中设置的支持 jail 的部分信息是每个 jail 的安全级别。 这允许在 jail 内运行比主机系统更高的安全级别。 有关 jail 的更多信息，请参阅 jail(8) 。

在多用户操作中， `init` 为文件 ttys(5) 中的终端端口维护进程。 `init` 实用程序读取此文件并执行在第二个字段中找到的命令，除非第一个字段引用 /dev 中未配置的设备。 第一个字段作为命令的最后一个参数提供。 这个命令通常是 getty(8); `getty` 打开并初始化 tty 行并执行 login(1) 程序。 当有效用户登录时， `login` 程序会为该用户执行一个 shell。 当这个 shell 死掉时，无论是因为用户注销还是发生异常终止（信号），循环都会通过为该行执行一个新的 `getty` 来重新启动。

`init` 实用程序也可用于保持任意守护程序运行，如果它们死亡则自动重新启动它们。 在这种情况下， ttys(5) 文件中的第一个字段不得引用配置的设备节点的路径，并将作为其命令行上的最后一个参数传递给守护程序。 这类似于 AT&T System V UNIX /etc/inittab 中提供的功能。

通过使用命令 “`kill -HUP 1`” 向 `init` 发送信号 `SIGHUP` ，可以在 ttys(5) 文件中更改线路状态（开、关、安全、getty 或窗口信息），而无需重新启动。 收到此信号后， `init` 会重新读取 ttys(5) 文件。 当一条线路在 ttys(5) 中关闭时， `init` 将向与线路关联的会话的控制进程发送一个 SIGHUP 信号。 对于之前在 ttys(5) 文件中关闭但现在打开的任何行， `init` 执行在第二个字段中指定的命令。 如果某行的命令或窗口字段发生更改，则更改在当前登录会话结束时生效（例如，下次 `init` 在该行上启动进程时）。 如果一行被注释掉或从 ttys(5) 中删除， `init` 不会对该行做任何事情。

如果发送终止 (`TERM`) 信号，例如 “`kill -TERM 1`” ， `init` 实用程序将终止多用户操作并恢复单用户模式。 如果有未完成的进程死锁（由于硬件或软件故障）， `init` 不会等待它们全部死亡（这可能需要永远），而是会在 30 秒后超时并打印一条警告消息。

如果向 `init` 实用程序发送终端停止 (`TSTP`) 信号，即 “`kill -TSTP 1`” ， `init` 实用程序将停止创建新进程并让系统慢慢消失。 稍后的挂断将恢复完整的多用户操作，或者终止将启动单用户 shell。 这个钩子被 reboot(8) 和 halt(8) 使用。

如果发送中断 (`INT`) 信号，即 “`kill -INT 1`” ， `init` 实用程序将终止所有可能的进程（同样，它不会等待死锁进程）并重新启动机器。 这对于在机器似乎挂起时从内核内部或从 X 彻底关闭机器很有用。

`init` 实用程序将执行相同的操作，但如果发送用户定义的信号 1 (`USR1`), 它将停止机器，或者如果发送用户定义的信号 2 (`USR2`) ，它将停止并关闭电源（如果硬件允许）。

关闭机器时， `init` 会尝试运行 /etc/rc.shutdown 脚本。 此脚本可用于干净地终止特定程序，例如 `innd` （InterNetNews 服务器）。 如果此脚本在 120 秒内没有终止， `init` 将终止它。 可以通过 sysctl(8) 变量 kern.init\_shutdown\_timeout 配置超时。

如果请求返回单用户模式， `init` 将 “`single`” 作为参数传递给关闭脚本。否则，使用 “`reboot`” 参数。

`init` 的作用非常关键，如果它死了，系统会自动重启。 如果在引导时无法定位 `init` 进程，系统将恐慌并显示消息 “panic: init died (signal %d, exit %d)” 。

如果作为用户进程运行，如第二个概要行所示， `init` 将模拟 AT&T System V UNIX 行为，即超级用户可以在命令行上指定所需的 _run-level_ ，并且 `init` 将发出原始信号（PID 1）初始化如下：

**运行级信号动作**

[`0`](#0)

[`SIGUSR1`](#SIGUSR1)

停止

[`0`](#0_2)

[`SIGUSR2`](#SIGUSR2)

停止并关闭电源

[`0`](#0_3)

[`SIGWINCH`](#SIGWINCH)

停止并关闭电源，然后重新打开

[`1`](#1)

[`SIGTERM`](#SIGTERM)

进入单用户模式

[`6`](#6)

[`SIGINT`](#SIGINT)

重启机器

[`c`](#c)

[`SIGTSTP`](#SIGTSTP)

阻止进一步登录

[`q`](#q)

[`SIGHUP`](#SIGHUP)

重新扫描 ttys(5) 文件

[内核环境变量](#__u5185___u6838___u73AF___u5883___u53D8___u91CF_)
===========================================================

以下 kenv(2) 变量可用作 loader(8) 可调参数：

init\_chroot

如果设置为根文件系统中的有效目录，它会导致 `init` 对该目录执行 chroot(2) 操作，使其成为新的根目录。 这发生在进入单用户模式或多用户模式之前（但如果启用，则在执行 init\_script 之后）。 此功能通常已因重新启动而黯然失色。 有关详细信息，请参见 reboot(8) `-r` 。

init\_exec

如果设置为根文件系统中的有效文件名，则指示 `init` 作为第一个操作直接执行该文件，将 `init` 替换为 PID 1。

init\_script

如果设置为根文件系统中的有效文件名，则指示 `init` 在执行任何其他操作之前运行该脚本作为第一个操作。 信号处理和退出代码解释类似于运行 /etc/rc 脚本。 特别是，如果脚本以非零退出代码终止，或者如果将 SIGTERM 传递给 `init` 进程 (PID 1)，则会强制执行单用户操作。 此功能通常已因重新启动而黯然失色。 有关详细信息，请参见 reboot(8) `-r` 。

init\_shell

定义用于执行各种 shell 脚本的 shell 二进制文件。 默认为 “`/bin/sh`” 。 它用于运行 init\_exec 或 init\_script （如果已设置）以及 /etc/rc 和 /etc/rc.shutdown 脚本。 每次 `init` 调用 shell 脚本时都会评估相应的 kenv(2) 量的值，因此可以稍后使用 kenv(1) 实用程序更改它。 特别是，如果使用非默认 shell 运行 init\_script ，则可能需要让该脚本将 init\_shell 的值重置为默认值，以便 /etc/rc 脚本执行标准 shell /bin/sh 。

[文件](#__u6587___u4EF6_)
=======================

/dev/console

系统控制台设备

/dev/tty\*

在 ttys(5) 中找到的终端端口

/etc/ttys

终端初始化信息文件

/etc/rc

系统启动命令

/etc/rc.shutdown

系统关闭命令

/var/log/init.log

如果系统控制台设备不可用，则 rc(8) 输出的日志

[诊断](#__u8BCA___u65AD_)
=======================

getty repeating too quickly on port %s, sleeping.

每次启动时，正在为线路提供服务的进程都会快速退出。 这通常是由振铃或嘈杂的终端线路引起的。

Init 将休眠 30 秒，然后继续尝试启动该进程。

some processes would not die; ps axl advised.

系统关闭时，进程挂起并且无法终止。 这种情况通常是由由于持续的设备错误情况而卡在设备驱动程序中的进程引起的。

[参见](#__u53C2___u89C1_)
=======================

kill(1), login(1), sh(1), ttys(5), security(7), getty(8), halt(8), jail(8), rc(8), reboot(8), shutdown(8), sysctl(8)

[历史](#__u5386___u53F2_)
=======================

Version 1 AT&T UNIX 中出现了一个 `init` 实用程序。

[注意事项](#__u6CE8___u610F___u4E8B___u9879_)
=========================================

没有 sysctl(8) 的系统表现得好像它们的安全级别为 -1。

在引导顺序中过早将安全级别设置为高于 1 会阻止 fsck(8) 修复不一致的文件系统。 设置安全级别的首选位置是在所有多用户启动操作完成后 /etc/rc 的末尾。

August 6, 2019

FreeBSD 13.1-RELEASE