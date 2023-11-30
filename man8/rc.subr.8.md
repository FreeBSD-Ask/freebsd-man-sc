  RC.SUBR(8)  

RC.SUBR(8)

FreeBSD System Manager's Manual

RC.SUBR(8)

[名称](#__u540D___u79F0_)
=======================

`rc.subr` —

系统 shell 脚本使用的函数

[概要](#__u6982___u8981_)
=======================

*   [`.`](#._&) /etc/rc.subr
    
*   [`backup_file`](#backup_file) action file current backup
*   [`checkyesno`](#checkyesno) var
*   [`check_pidfile`](#check_pidfile) pidfile procname \[interpreter\]
*   [`check_process`](#check_process) procname \[interpreter\]
*   [`debug`](#debug) message
*   [`err`](#err) exitval message
*   [`force_depend`](#force_depend) name
*   [`info`](#info) message
*   [`load_kld`](#load_kld) \[`-e` regex\] \[`-m` module\] file
*   [`load_rc_config`](#load_rc_config) name
*   [`load_rc_config_var`](#load_rc_config_var) name var
*   [`mount_critical_filesystems`](#mount_critical_filesystems) type
*   [`rc_usage`](#rc_usage) command ...
*   [`reverse_list`](#reverse_list) item ...
*   [`run_rc_command`](#run_rc_command) argument
*   [`run_rc_script`](#run_rc_script) file argument
*   [`wait_for_pids`](#wait_for_pids) \[pid ...\]
*   [`warn`](#warn) message

[描述](#__u63CF___u8FF0_)
=======================

`rc.subr` 脚本包含常用的 shell 脚本函数和变量定义，这些函数被各种脚本（例如 rc(8) ）使用。 /usr/local/etc/rc.d 中的端口所需的脚本最终也将被重写以使用它。

`rc.subr` 函数主要是从 NetBSD-
导入的。

通过将 /etc/rc.subr 导入当前 shell 来访问它们。

可以使用以下 shell 函数：

[`backup_file`](#backup_file_2) action file current backup

将 file 备份到 current 。 将 current 版本的先前版本保存为 backup 。

action 参数可以是以下之一：

[`add`](#add)

file 现在正在备份或可能重新进入此备份机制。 current 被创建。

[`update`](#update)

file 已更改，需要备份。 如果 current 存在，则将其复制到 backup ，然后将 file 复制到 current 。

[`remove`](#remove)

此备份机制不再跟踪 file 。 current 移动到 backup 。

[`checkyesno`](#checkyesno_2) var

如果 var 定义为 “`YES`”, “`TRUE`”, “`ON`” 或 ‘`1`’ ，则返回 0。 如果 var 定义为 “`NO`”, “`FALSE`”, “`OFF`” 或 ‘`0`’ ，则返回 0。 否则，警告 var 设置不正确。 这些值不区分大小写。 **注意**: var-
应该是一个变量名，而不是它的值； `checkyesno` 将自行扩展变量。

[`check_pidfile`](#check_pidfile_2) pidfile procname \[interpreter\]

解析 pidfile 第一行的第一个单词以获取 PID，并确保具有该 PID 的进程正在运行并且其第一个参数与 procname 匹配。 如果成功则打印匹配的 PID，否则不打印。 如果提供了 interpreter ，则解析 procname 的第一行，确保该行的格式为：

`#! interpreter [...]`

并使用带有可选参数和 procname 的 interpreter 作为要搜索的进程字符串附加。

[`check_process`](#check_process_2) procname \[interpreter\]

打印使用与 procname 匹配的第一个参数运行的任何进程的 PID。 interpreter 按 `check_pidfile` 处理。

[`debug`](#debug_2) message

向 stderr 显示调试消息，使用 logger(1) 将其记录到系统日志中，然后返回给调用者。 错误消息包含脚本名称（从 $0 开始），后跟 “`: DEBUG:` ”, 然后是 message 。 此功能旨在供开发人员用作调试脚本的辅助工具。 它可以通过 rc.conf(5) 变量 rc\_debug 打开或关闭。

[`err`](#err_2) exitval message

向 stderr 显示错误消息，使用 logger(1), 将其记录到系统日志中，并以 exitval 的退出值 `exit` 。 错误消息包含脚本名称（从 $0 开始），后跟 “`: ERROR:` ”, 然后是 message 。

[`force_depend`](#force_depend_2) name

输出一条建议消息并强制启动 name 服务。 name 参数是位于 /etc/rc.d 的脚本路径的 basename(1) ) 组件（存储在其他位置的脚本，例如 /usr/local/etc/rc.d 目前无法使用 `force_depend`-
控制）。 如果脚本因任何原因失败，它将输出警告并返回值 1。 如果成功，它将返回 0。

[`info`](#info_2) message

向 stdout 显示信息性消息，并使用 logger(1) 将其记录到系统日志中。 该消息包含脚本名称（从 $0 开始），后跟 “`: INFO:` ”, 然后是 message 。 可以通过 rc.conf(5) 变量 rc\_info 打开或关闭此信息输出的显示。

[`load_kld`](#load_kld_2) \[`-e` regex\] \[`-m` module\] file

除非已加载 file ，否则将 file 作为内核模块加载。 为了检查模块状态，可以使用 `-m` 指定确切的模块名称，或者可以通过 `-e` 提供与模块名称匹配的 egrep(1) 正则表达式。 默认情况下，假定模块与 file 同名，但并非总是如此。

[`load_rc_config`](#load_rc_config_2) name

name 的配置文件中的源。 首先，如果尚未读入 /etc/rc.conf ，则获取它。 然后，如果 /etc/rc.conf.d/name 是现有文件，则它是源文件。 后者还可能包含其他变量分配以覆盖调用脚本定义的 `run_rc_command` 参数，从而为管理员提供一种简单的机制来覆盖给定 rc.d(8) 脚本的行为，而无需编辑该脚本。

[`load_rc_config_var`](#load_rc_config_var_2) name var

读取 rc.conf(5) 变量 var 的 name 并在当前 shell 中设置，在子 shell 中使用 `load_rc_config` 以防止其他变量分配产生不必要的副作用。

[`mount_critical_filesystems`](#mount_critical_filesystems_2) type

查看 rc.conf(5) 变量 critical\_filesystems\_type 中的关键文件系统列表，安装当前未安装的每个系统。

[`rc_usage`](#rc_usage_2) command ...

打印 $0 的使用消息， commands 是前缀为 “\[`fast`|`force`|`one`|`quiet`\]”. 的有效参数列表。

[`reverse_list`](#reverse_list_2) item ...

以相反的顺序打印 items 列表。

[`run_rc_command`](#run_rc_command_2) argument

根据各种 shell 变量的设置，运行当前 rc.d(8) 脚本的 argument 方法。 `run_rc_command` 非常灵活，允许在少量 shell 代码中实现功能齐全的 rc.d(8) 脚本。

在支持的命令列表中搜索 argument ，可能是以下命令之一：

[`start`](#start)

启动服务。 这应该检查服务是否按照 rc.conf(5) 的规定启动。 还检查服务是否已经在运行，如果是则拒绝启动。 如果系统直接启动到多用户模式，则标准 FreeBSD 脚本不会执行后一种检查，以加快启动过程。

[`stop`](#stop)

如果要按照 rc.conf(5) 的规定启动服务，请停止服务。 这应该检查服务是否正在运行，如果没有运行则抱怨。

[`restart`](#restart)

执行 `stop` 然后 `start` 。 默认显示程序的进程 ID（如果正在运行）。

[`enabled`](#enabled)

如果服务启用则返回 0，否则返回 1。 此命令不打印任何内容。

[`rcvar`](#rcvar)

显示哪些 rc.conf(5) 变量用于控制服务的启动（如果有）。

如果设置了 pidfile 或 procname ，还支持：

[`poll`](#poll)

等待命令退出。

[`status`](#status)

显示进程的状态。

其他支持的命令列在可选变量 extra\_commands 中。

argument 可能具有以下前缀之一，这些前缀会改变其操作：

[`fast`](#fast)

跳过检查现有正在运行的进程，并设置 rc\_fast\=`YES` 。

[`force`](#force)

跳过检查 rcvar 是否设置为 “`YES`” ，并设置 rc\_force\=`YES` 。 这将忽略返回非零的 argument\_precmd ，并忽略任何失败的 required\_\* 测试，并始终返回零退出状态。

[`one`](#one)

跳过检查 rcvar 是否设置为 “`YES`”, 但执行所有其他先决条件测试。

[`quiet`](#quiet)

禁止一些详细的诊断。 目前，这包括消息 “Starting ${name}” （由 `rc.subr` 中的 `check_startmsgs` 检查）和有关使用 rc.conf(5) 中未启用的服务的错误。 此前缀还设置 rc\_quiet\=`YES` 。 _请注意：_ rc\_quiet 并非旨在完全屏蔽所有调试和警告消息，而只是屏蔽其中的某些小类。

`run_rc_command` 使用以下 shell 变量来控制其行为。 除非另有说明，否则这些都是可选的。

name

此脚本的名称。这不是可选的。

rcvar

使用 `checkyesno` 检查 rcvar 的值以确定是否应该运行此方法。

command

命令的完整路径。如果为每个支持的关键字定义了 argument\_cmd ，则不需要。可以被 ${name}\_program 覆盖。

command\_args

command 的可选参数和/或 shell 指令。

command\_interpreter

command 开始于：

`#! command_interpreter [...]`

这导致其 ps(1) 命令为：

`command_interpreter [...] command`

所以使用该字符串来查找正在运行的命令而不是 command 的 PID。

extra\_commands

支持额外的 commands/keywords/arguments 。

pidfile

PID 文件的路径。 用于确定运行命令的 PID。 如果设置了 pidfile ，请使用：

`check_pidfile $pidfile $procname`

找到PID。否则，如果设置了 command ，请使用：

`check_process $procname`

找到PID。

procname

要检查的进程名称。 默认为 command 的值。

required\_dirs

在运行 `start` 方法之前检查列出的目录是否存在。 在运行 start\_precmd 之前检查该列表。

required\_files

在运行 `start` 方法之前检查列出的文件的可读性。 在运行 start\_precmd 之前检查该列表。

required\_modules

确保在运行 `start` 方法之前加载列出的内核模块。 运行 start\_precmd 后检查该列表。 这是在从 start\_precmd 调用命令之后完成的，这样如果初步命令指示错误条件，就不会徒劳地加载丢失的模块。 列表中的单词可以有一个可选的 “`:`modname” 或 “`~`pattern” 后缀。 modname 或 pattern 参数分别通过 `-m` 或 `-e` 选项传递给 `load_kld` 。 详见本文档对 `load_kld` 的描述。

required\_vars

在运行 `start` 方法之前，对每个列表变量执行 `checkyesno` 。 运行 start\_precmd 后检查该列表。

${name}\_chdir

如果未提供 ${name}\_chroot ，则在运行 command 之前要 `cd` 到的目录。

${name}\_chroot

运行 command 之前 chroot(8) 的目录。仅在挂载 /usr 后支持。

${name}\_env

用于运行 command 的环境变量列表。 除非定义了 argument\_cmd ，否则这些变量将作为参数传递给 env(1) 实用程序。 在这种情况下， ${name}\_env 的内容将通过 sh(1) 的 export(1) 内置函数导出，这对变量的名称施加了一些限制（例如，变量名称不能以数字开头）。

${name}\_env\_file

用于获取环境变量以运行 command 的文件。 请注意，在此文件中分配的所有变量都将导出到 command 环境中。

${name}\_fib

用于运行 command 的 FIB Routing Table 。 有关详细信息，请参阅 setfib(1) 。

${name}\_flags

调用 command 的参数。 这通常在 rc.conf(5) 中设置，而不是在 rc.d(8) 脚本中。 环境变量 ‘`flags`’ 可以用来覆盖它。

${name}\_nice

nice(1) 级别来运行 command 。 仅在挂载 /usr 后支持。

${name}\_limits

应用于 command 的资源限制。 这将作为参数传递给 limits(1) 实用程序。 默认情况下，资源限制基于 ${name}\_login\_class 中定义的登录类。

${name}\_login\_class

与 ${name}\_limits 一起使用的登录类。 默认为 “`daemon`” 。

${name}\_oomprotect

当交换空间用完时， protect(1) command 不会被杀死。 如果使用 “`YES`” ，则没有子进程受到保护。 如果为 “`ALL`”, 则保护所有子进程。

${name}\_program

命令的完整路径。 如果两者都设置了，则覆盖 command ，但如果未设置 command ，则无效。 通常， command 应该在脚本中设置，而 ${name}\_program 应该在 rc.conf(5) 中设置。

${name}\_user

用户运行 command ，如果设置了 ${name}\_chroot ，则使用 chroot(8) ，否则使用 su(1) 。 仅在挂载 /usr 后支持。

${name}\_group

组以运行 command 命令。

${name}\_groups

以逗号分隔的补充组列表，用于运行 command 。

${name}\_prepend

要在命令之前添加的 command 。 这是 ${name}\_env, ${name}\_fib 或 ${name}\_nice 的通用版本。

argument\_cmd

覆盖 argument 的默认方法的 Shell 命令。

argument\_precmd

在运行 argument\_cmd 或 argument 的默认方法之前运行的 Shell 命令。 如果这返回非零退出代码，则不执行 main 方法。 如果正在执行默认方法，则在 required\_\* 检查和处理（不）存在检查之后执行此检查。

argument\_postcmd

如果运行 argument\_cmd 或 argument 的默认方法返回零退出代码，则要运行的 Shell 命令。

sig\_stop

在默认 `stop` 方法中发送进程停止的信号。 默认为 `SIGTERM` 。

sig\_reload

以默认 `reload` 方法发送进程以重新加载的信号。 默认为 `SIGHUP` 。

对于给定的方法 argument ，如果未定义 argument\_cmd ，则 `run_rc_command` 提供默认方法：

**Argument**

**Default method**

[`start`](#start_2)

如果 command 未运行且 `checkyesno` rcvar 成功，则启动 command 。

[`stop`](#stop_2)

使用 `check_pidfile` 或 `check_process` （根据需要）确定 command 的 PID， `kill` sig\_stop 这些 PID，并在这些 PID 上运行 `wait_for_pids` 。

[`reload`](#reload)

与 `stop` 类似，只是它使用 sig\_reload 代替，并且不运行 `wait_for_pids` 。 与 `stop` 的另一个区别是默认情况下不提供 `reload` 。 如果合适，可以通过 extra\_commands 启用它：

`extra_commands=reload`

[`restart`](#restart_2)

运行 `stop` 方法，然后运行 `start` 方法。

[`status`](#status_2)

显示 command 的 PID，或一些其他脚本特定的状态操作。

[`poll`](#poll_2)

等待 command 退出。

[`rcvar`](#rcvar_2)

显示使用了哪个 rc.conf(5)-
变量（如果有）。 即使适当的 rc.conf(5) 变量设置为 “`NO`” ，此方法也始终有效。

以下变量可用于方法（例如 argument\_cmd) 以及 `run_rc_command` 完成后：

rc\_arg

在执行快速和强制处理后，提供给 `run_rc_command` 的参数。

rc\_flags

用于启动默认命令的标志。 默认为 ${name}\_flags ，除非被环境变量 ‘`flags`’ 覆盖。 这个变量可以通过 argument\_precmd 方法改变。

rc\_service

正在执行的服务脚本的路径，以防它需要重新调用自身。

rc\_pid

command 的 PID（如果适用）。

rc\_fast

如果使用 “`fast`” 前缀，则不为空。

rc\_force

如果使用 “`force`” 前缀，则不为空。

[`run_rc_script`](#run_rc_script_2) file argument

Start the script file 使用 argument 的参数启动脚本文件，并处理脚本的返回值。

在 file 启动之前未设置各种 shell 变量：

name, command, command\_args, command\_interpreter, extra\_commands, pidfile, rcvar, required\_dirs, required\_files, required\_vars, argument\_cmd, argument\_precmd. argument\_postcmd.

file 的启动行为取决于以下检查：

1.  如果 file 以 .sh-
    结尾，则将其来源到当前 shell。
2.  如果 file 看起来是备份或临时文件（例如，带有 ~, #, .OLD 或 .orig 后缀），请忽略它。
3.  如果 file 不可执行，则忽略它。
4.  如果 rc.conf(5) 变量 rc\_fast\_and\_loose 为空，则源 file 在子 shell 中，否则源 file 到当前 shell。

[`stop_boot`](#stop_boot) \[always\]

防止引导到多用户模式。 如果 autoboot 变量设置为 ‘`yes`’ (请参阅 rc(8) 以了解有关 autoboot 的更多信息），或者 `checkyesno` 始终指示真值，则向父进程发送 `SIGTERM` 信号，假定为 rc(8) 。 否则，shell 以非零状态退出。

[`wait_for_pids`](#wait_for_pids_2) \[pid ...\]

等到所有提供的 pid 不再存在，每两秒打印一次未完成的 pid 列表。

[`warn`](#warn_2) message

向 stderr 显示警告消息并使用 logger(1) 将其记录到系统日志中。 警告消息包含脚本名称（从 $0 开始），后跟 “`: WARNING:` ”, 然后是 message 。

[文件](#__u6587___u4EF6_)
=======================

/etc/rc.subr

`rc.subr` 文件位于 /etc 中。

[参见](#__u53C2___u89C1_)
=======================

rc.conf(5), rc(8)

[历史](#__u5386___u53F2_)
=======================

`rc.subr` 脚本出现在 NetBSD 1.3 中。 rc.d(8) 支持函数出现在 NetBSD 1.5 中。 `rc.subr` 脚本最早出现在 FreeBSD 5.0 中。

July 31, 2020

FreeBSD 13.1-RELEASE