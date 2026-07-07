# init(8)

`init` — 进程控制初始化

## 名称

`init`

## 概要

`init`

`init [0 | 1 | 6 | c | q]`

## 描述

`init` 工具是引导过程的最后阶段。它通常运行 [rc(8)](rc.8.md) 中描述的自动重启序列，如果成功，则开始多用户模式运行。如果重启脚本失败，`init` 通过在控制台上为超级用户提供一个 shell 来进入单用户模式运行。`init` 可以接收来自引导程序的参数，以防止系统进入多用户模式，转而执行单用户 shell 而不启动正常的守护进程。此时系统处于静止状态以进行维护工作，之后可通过退出单用户 shell（按 ^D）使系统进入多用户模式。这会令 `init` 以 fastboot 模式（跳过磁盘检查）运行 **/etc/rc** 启动命令文件。

如果 ttys(5) 文件中的 *console* 项被标记为 “insecure”，则 `init` 会要求输入超级用户密码，然后系统才会启动单用户 shell。如果 *console* 被标记为 “secure”，则跳过密码检查。注意，此密码检查无法防止诸如 `init_script` 之类的变量从 [loader(8)](loader.8.md) 命令行设置；参见 loader(8) 的 SECURITY 一节。

如果系统安全级（参见 [security(7)](../man7/security.7.md)）初始时非零，则 `init` 保持其不变。否则，`init` 在第一次进入多用户模式之前将级别提升至 1。由于级别无法降低，因此后续操作中至少为 1，即使返回单用户模式也是如此。如果在多用户运行时希望使用高于 1 的级别，可在进入多用户模式之前设置，例如由启动脚本 [rc(8)](rc.8.md) 使用 [sysctl(8)](sysctl.8.md) 将 `kern.securelevel` 变量设置为所需的安全级别。

如果 `init` 在 jail 中运行，“宿主系统”的安全级不受影响。内核中为支持 jail 而建立的部分信息是每个 jail 独立的安全级。这使得在 jail 内部可以运行比宿主系统更高的安全级。有关 jail 的更多信息，请参见 [jail(8)](jail.8.md)。

在多用户运行模式下，`init` 维护 ttys(5) 文件中所列终端端口对应的进程。`init` 工具读取此文件并执行第二个字段中的命令，除非第一个字段引用的是 **/dev** 中未配置的设备。第一个字段作为命令的最后一个参数提供。该命令通常是 getty(8)；`getty` 打开并初始化 tty 线路，并执行 [login(1)](../man1/login.1.md) 程序。当合法用户登录时，`login` 程序为该用户执行一个 shell。当此 shell 终止时，无论是由于用户注销还是异常终止（信号），都会通过为该线路执行新的 `getty` 来重新开始循环。

`init` 工具也可用于保持任意守护进程运行，并在其终止时自动重启。在这种情况下，ttys(5) 文件中的第一个字段不得引用已配置设备节点的路径，并将作为命令行的最后一个参数传递给守护进程。这类似于 AT&T System V UNIX 中 **/etc/inittab** 提供的功能。

线路状态（on、off、secure、getty 或 window 信息）可在 ttys(5) 文件中修改而无需重启，方法是使用 “`kill -HUP 1`” 命令向 `init` 发送 `SIGHUP` 信号。收到此信号后，`init` 重新读取 ttys(5) 文件。当某条线路在 ttys(5) 中被关闭时，`init` 会向与该线路相关会话的控制进程发送 SIGHUP 信号。对于在 ttys(5) 文件中先前关闭而现在打开的任何线路，`init` 执行第二个字段中指定的命令。如果某条线路的命令或 window 字段被修改，该更改将在当前登录会话结束时（例如 `init` 下次在该线路上启动进程时）生效。如果某条线路在 ttys(5) 中被注释掉或删除，`init` 不会对该线路做任何操作。

如果向 `init` 发送终止（`TERM`）信号（例如 “`kill -TERM 1`”），它会终止多用户运行并恢复单用户模式。如果存在死锁的未完成进程（由于硬件或软件故障），`init` 不会等待它们全部终止（那可能需要永远），而是在 30 秒后超时并打印警告消息。

如果向 `init` 发送终端停止（`TSTP`）信号（即 “`kill -TSTP 1`”），它将停止创建新进程，并允许系统缓慢消亡。随后的挂起将恢复完整的多用户运行，或终止信号将启动单用户 shell。此钩子由 [reboot(8)](reboot.8.md) 和 [halt(8)](reboot.8.md) 使用。

如果向 `init` 发送中断（`INT`）信号（即 “`kill -INT 1`”），它会终止所有可能终止的进程（同样，不会等待死锁的进程）并重启机器。当机器看起来卡死时，这对于从内核内部或从 X 中干净地关闭机器很有用。

`init` 工具会做同样的操作，但如果收到用户自定义信号 1（`USR1`），它会停机；如果收到用户自定义信号 2（`USR2`），它会停机并（如果硬件允许）关闭电源。

关机时，`init` 会尝试运行 **/etc/rc.shutdown** 脚本。此脚本可用于干净地终止特定程序，例如 `innd`（InterNetNews 服务器）。如果此脚本在 120 秒内未终止，`init` 将终止它。超时时间可通过 [sysctl(8)](sysctl.8.md) 变量 `kern.init_shutdown_timeout` 配置。

如果请求返回单用户模式，`init` 将 “`single`” 作为参数传递给关机脚本。否则使用 “`reboot`” 参数。

在所有用户进程都终止之后，`init` 会尝试运行 **/etc/rc.final** 脚本。例如，此脚本可用于最终准备并卸载在关机期间可能需要的文件系统。

`init` 的角色至关重要，如果它终止，系统将自动重启。如果在引导时无法找到 `init` 进程，系统将 panic 并显示消息 “panic: init died (signal %d, exit %d)”。

如果按第二行概要所示作为用户进程运行，`init` 将模拟 AT&T System V UNIX 的行为，即超级用户可在命令行上指定所需的 *运行级别*（run-level），`init` 将向原始（PID 1）的 `init` 发送如下信号：

| 运行级别 | 信号 | 动作 |
| :--- | :--- | :--- |
| `0` | `SIGUSR1` | 停机 |
| `0` | `SIGUSR2` | 停机并关闭电源 |
| `0` | `SIGWINCH` | 停机、关闭电源然后再打开 |
| `1` | `SIGTERM` | 进入单用户模式 |
| `6` | `SIGINT` | 重启机器 |
| `c` | `SIGTSTP` | 阻止进一步登录 |
| `q` | `SIGHUP` | 重新扫描 ttys(5) 文件 |

## 内核环境变量

以下 kenv(2) 变量可作为 [loader(8)](loader.8.md) 可调参数使用：

**`init_chroot`** 如果设置为根文件系统中的有效目录，会使 `init` 对该目录执行 chroot(2) 操作，使其成为新的根目录。这发生在进入单用户模式或多用户模式之前（但如果启用了 `init_script`，则在执行 `init_script` 之后）。此功能通常已被 rerooting 取代。详见 [reboot(8)](reboot.8.md) 的 `-r` 选项。

**`init_exec`** 如果设置为根文件系统中的有效文件名，指示 `init` 将直接执行该文件作为第一个动作，替换 `init` 作为 PID 1。

**`init_script`** 如果设置为根文件系统中的有效文件名，指示 `init` 在做任何其他事情之前首先运行该脚本。信号处理和退出代码解释与运行 **/etc/rc** 脚本类似。特别是，如果脚本以非零退出代码终止，或向 `init` 进程（PID 1）发送 SIGTERM，则强制单用户运行。此功能通常已被 rerooting 取代。详见 [reboot(8)](reboot.8.md) 的 `-r` 选项。

**`init_shell`** 定义用于执行各种 shell 脚本的 shell 二进制文件。默认值为 “`/bin/sh`”。它用于运行 `init_exec` 或 `init_script`（如果已设置），以及 **/etc/rc**、**/etc/rc.shutdown** 和 **/etc/rc.final** 脚本。对应的 kenv(2) 变量的值会在 `init` 每次调用 shell 脚本时重新求值，因此可稍后使用 [kenv(1)](../man1/kenv.1.md) 工具更改。特别是，如果使用非默认 shell 运行 `init_script`，可能希望该脚本将 `init_shell` 的值重置为默认值，以便 **/etc/rc** 脚本使用标准 shell **/bin/sh** 执行。

**`init_rc`** 如果设置为根文件系统中的有效文件名，将覆盖 [rc(8)](rc.8.md) 的默认路径（**/etc/rc**）。这对于在不修改默认 **/etc/rc** 的情况下测试替代服务管理器很有用。

**`init_path`** 指定用于搜索 init 二进制文件的路径。字符串中可列出多个二进制文件，候选文件名以 “`:`” 分隔符分割。每个名称按顺序打开，直到找到有效的可执行文件。

## 恢复

如果 **/sbin/init** 二进制文件损坏或无法由当前内核执行，恢复需要控制台访问权限。然后，可使用 `init_path` loader 可调参数指定替代的 `init` 位置。

默认情况下，系统安装会在 **/sbin/init.bak** 留下先前 `init` 二进制文件的副本，此路径被设置为默认 `init_path` 的一个组成部分。

如果无法运行 `init`，FreeBSD 版本的 [sh(1)](../man1/sh.1.md) 对作为 PID 1 运行有特殊规定。如果 shell 检测到自己作为 init 运行，它会打开 **/dev/console** 作为标准输入和输出，并进入命令循环。

应使用 `reboot` `-q` 或 exec 修复后的 `init` 退出会话，因为正常退出会导致内核 panic。

## 文件

**`/dev/console`** 系统控制台设备

**`/dev/tty*`** ttys(5) 中的终端端口

**`/etc/ttys`** 终端初始化信息文件

**`/etc/rc`** 系统启动命令

**`/etc/rc.shutdown`** 系统关机命令

**`/etc/rc.final`** 系统关机命令（在进程终止后）

**`/var/log/init.log`** 当系统控制台设备不可用时 [rc(8)](rc.8.md) 输出的日志

## 诊断

- “getty repeating too quickly on port %s, sleeping.” 为某条线路服务的进程每次启动时都快速退出。这通常由振铃或嘈杂的终端线路引起。*init 将睡眠 30 秒，然后继续尝试启动该进程。*
- “some processes would not die; ps axl advised.” 某个进程挂起且在系统关机时无法被杀死。这种情况通常由进程因持续的设备错误状况而卡在设备驱动程序中引起。

## 参见

[kill(1)](../man1/kill.1.md), [login(1)](../man1/login.1.md), [sh(1)](../man1/sh.1.md), ttys(5), [security(7)](../man7/security.7.md), getty(8), [halt(8)](reboot.8.md), [jail(8)](jail.8.md), [rc(8)](rc.8.md), [reboot(8)](reboot.8.md), [shutdown(8)](shutdown.8.md), [sysctl(8)](sysctl.8.md)

## 历史

`init` 工具出现于 Version 1 AT&T UNIX。

## 注意事项

没有 [sysctl(8)](sysctl.8.md) 的系统表现为安全级 -1。

在引导序列中过早地将安全级设置为高于 1 可能会阻止 fsck(8) 修复不一致的文件系统。设置安全级的首选位置是在所有多用户启动动作完成之后的 **/etc/rc** 末尾。
