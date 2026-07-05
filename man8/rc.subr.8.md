# rc.subr.8

`rc.subr` — 系统脚本使用的函数

## 名称

`rc.subr`

## 概要

`. /etc/rc.subr`

`backup_file action file current backup`

`checkyesno var`

`check_pidfile pidfile procname [interpreter]`

`check_process procname [interpreter]`

`DebugOn tag ...`

`DebugOff tag ...`

`debug message`

`dot file ...`

`err exitval message`

`force_depend name`

`info message`

`is_verified file`

`load_kld [-e regex] [-m module] file`

`load_rc_config [flag] [service]`

`load_rc_config_var name var`

`mount_critical_filesystems type`

`rc_log message`

`rc_trace level message`

`rc_usage command ...`

`reverse_list item ...`

`run_rc_command argument`

`run_rc_script file argument`

`run_rc_scripts [options] file ...`

`safe_dot file ...`

`sdot file ...`

`startmsg [-n] message`

`vdot file ...`

`wait_for_pids [pid ...]`

`warn message`

## 描述

`rc.subr` 脚本包含常用 shell 脚本函数和变量定义，被各种脚本（如 [rc(8)](rc.8.md)）使用。**/usr/local/etc/rc.d** 中 Ports 所需的脚本最终也将被重写以使用它。

`rc.subr` 函数大部分从 NetBSD 导入。

通过将 **/etc/rc.subr** source 到当前 shell 中来访问这些函数。

以下 shell 函数可用：

**`backup_file`** `action file current backup` 将 `file` 备份复制到 `current`。将 `current` 的先前版本保存为 `backup`。

`action` 参数可以是以下之一：

- `add` `file` 现在正在被此备份机制备份或可能重新进入此备份机制。创建 `current`。
- `update` `file` 已更改，需要备份。如果 `current` 存在，将其复制到 `backup`，然后将 `file` 复制到 `current`。
- `remove` `file` 不再被此备份机制跟踪。`current` 被移动到 `backup`。

**`checkyesno`** `var` 如果 `var` 定义为 “`YES`”、“`TRUE`”、“`ON`” 或 `1`，则返回 0。如果 `var` 定义为 “`NO`”、“`FALSE`”、“`OFF`” 或 `0`，则返回 1。否则，警告 `var` 未正确设置。这些值大小写不敏感。*注意：* `var` 应为变量名，而非其值；`checkyesno` 会自行展开变量。

**`check_pidfile`** `pidfile procname` [`interpreter`] 解析 `pidfile` 第一行的第一个字以获取 PID，并确保具有该 PID 的进程正在运行且其第一个参数匹配 `procname`。如果成功则打印匹配的 PID，否则不打印任何内容。如果提供 `interpreter`，解析 `procname` 的第一行，确保该行的形式为：

```sh
#! interpreter [...]
```

并使用 `interpreter` 及其可选参数和追加的 `procname` 作为要搜索的进程字符串。

**`check_process`** `procname` [`interpreter`] 打印任何正在运行且第一个参数匹配 `procname` 的进程的 PID。`interpreter` 的处理与 `check_pidfile` 相同。

**`DebugOn`** `tag ...` 如果尚未启用跟踪，且任何 `tag` 在 `DEBUG_SH`（逗号分隔的标签列表）中找到，则启用跟踪。

将导致启用它的 `tag` 记录到 `DEBUG_ON` 中，将 `DEBUG_DO` 设置为空，将 `DEBUG_SKIP` 设置为 **:**。

更多细节参见 [debug.sh(8)](debug.sh.8.md)。

**`DebugOff`** `tag ...` 如果已启用跟踪且任何 `tag` 匹配 `DEBUG_ON`，则禁用跟踪，这意味着它是启用跟踪的原因。

将 `DEBUG_DO` 设置为 **:**，将 `DEBUG_ON`、`DEBUG_SKIP` 设置为空。

**`debug`** `message` 向 `stderr` 显示调试消息，使用 [logger(1)](../man1/logger.1.md) 将其记录到系统日志，并返回调用者。错误消息由脚本名（来自 `$0`）、后跟 “: DEBUG: ”、然后是 `message` 组成。此函数旨在供开发者用作调试脚本的辅助工具。可通过 [rc.conf(5)](../man5/rc.conf.5.md) 变量 `rc_debug` 开启或关闭。

**`dot`** `file ...` 用于读取未验证的文件。

确保 shell `verify` 选项关闭。此选项仅在 [mac_veriexec(4)](../man4/mac_veriexec.4.md) 活动时才有意义。

如果每个 `file` 存在则读取它。

恢复 `verify` 选项的先前状态。

**`err`** `exitval message` 向 `stderr` 显示错误消息，使用 [logger(1)](../man1/logger.1.md) 将其记录到系统日志，并以退出值 `exitval` 退出。错误消息由脚本名（来自 `$0`）、后跟 “: ERROR: ”、然后是 `message` 组成。

**`force_depend`** `name` 输出建议性消息并强制 `name` 服务启动。`name` 参数是位于 **/etc/rc.d** 的脚本的路径的 [basename(1)](../man1/basename.1.md) 组件（存储在其他位置（如 **/usr/local/etc/rc.d**）的脚本目前无法用 `force_depend` 控制）。如果脚本因任何原因失败，它将输出警告并以返回值 1 返回。如果成功则返回 0。

**`is_verified`** `file` 如果 [veriexec(8)](veriexec.8.md) 不存在，或 [mac_veriexec(4)](../man4/mac_veriexec.4.md) 未活动，则直接返回成功。否则使用 [veriexec(8)](veriexec.8.md) 检查 `file` 是否已验证。如果未验证，返回码将为 80（EAUTH）。

**`info`** `message` 向 `stdout` 显示信息消息，并使用 [logger(1)](../man1/logger.1.md) 将其记录到系统日志。消息由脚本名（来自 `$0`）、后跟 “: INFO: ”、然后是 `message` 组成。此信息输出的显示可通过 [rc.conf(5)](../man5/rc.conf.5.md) 变量 `rc_info` 开启或关闭。

**`load_kld`** [`-e` `regex`] [`-m` `module`] `file` 将 `file` 作为内核模块加载，除非它已加载。为了检查模块状态，可使用 `-m` 指定确切的模块名，或通过 `-e` 提供匹配模块名的 [egrep(1)](../man1/egrep.1.md) 正则表达式。默认情况下，假定模块与 `file` 同名，但并非总是如此。

**`load_rc_config`** [`flag`] [`service`] source `service` 的配置文件。如果未指定 `service`，仅加载全局配置文件。首先，如果 **/etc/rc.conf** 尚未被读取，则 source 它。然后，如果 **/etc/rc.conf.d/**`service` 是存在的文件，则 source 它。后者也可包含其他变量赋值以覆盖调用脚本定义的 `run_rc_command` 参数，为管理员提供一种简便机制来覆盖给定 [rc.d(8)](rc.d.8.md) 脚本的行为而无需编辑该脚本。

由 `load_rc_config_reader`（默认为 `dot`）命名的函数用于读取配置，除非 `flag` 为：

- `-s` 使用 `sdot` 读取配置，因为我们要读取已验证的配置，或使用 `safe_dot` 读取未验证的配置。
- `-v` 使用 `vdot` 仅在配置已验证时读取。

`DebugOn` 将以从 `name` 派生的标签调用，如果任何标签出现在 `DEBUG_SH` 中则启用跟踪。

**`load_rc_config_var`** `name` `var` 使用 `load_rc_config` 在子 shell 中读取 `name` 的 [rc.conf(5)](../man5/rc.conf.5.md) 变量 `var` 并在当前 shell 中设置，以防止其他变量赋值产生不需要的副作用。

**`mount_critical_filesystems`** `type` 遍历关键文件系统列表（如 [rc.conf(5)](../man5/rc.conf.5.md) 变量 `critical_filesystems_` `type` 中所列），挂载每个当前未挂载的文件系统。

**`rc_log`** `message` 输出带时间戳的 `message`，时间戳既易于人类阅读又易于后处理解析，使用：

```sh
date "+@ %s [%Y-%m-%d %H:%M:%S %Z] $*"
```

**`rc_trace`** `level` `message` 如果文件 **/etc/rc.conf.d/rc_trace** 存在且非空，尝试根据其内容设置 `RC_LEVEL`。如果文件为空或不包含 `RC_LEVEL` 的值，将其设置为 `0`。

如果 `level` 大于或等于 `RC_LEVEL`，将 `message` 传递给 `rc_log`。

**`rc_usage`** `command ...` 打印 `$0` 的用法消息，`commands` 为有效参数列表，前缀为 “[`fast | force | one | quiet`]”。

**`reverse_list`** `item ...` 以相反顺序打印 `items` 列表。

**`run_rc_command`** `argument` 基于各种 shell 变量的设置，为当前 [rc.d(8)](rc.d.8.md) 脚本运行 `argument` 方法。`run_rc_command` 极其灵活，允许以少量 shell 代码实现功能完整的 [rc.d(8)](rc.d.8.md) 脚本。

`argument` 在支持的命令列表中搜索，可以是以下之一：

- `start` 启动服务。这应当检查服务是否按 [rc.conf(5)](../man5/rc.conf.5.md) 的指定启动。还会检查服务是否已在运行，如果是则拒绝启动。如果系统直接启动到多用户模式，标准 FreeBSD 脚本不执行后一项检查，以加速引导过程。
- `stop` 如果服务按 [rc.conf(5)](../man5/rc.conf.5.md) 的指定启动，则停止服务。这应当检查服务是否正在运行，如果不是则发出抱怨。
- `restart` 执行 `stop` 然后执行 `start`。默认显示程序的进程 ID（如果正在运行）。
- `enabled` 如果服务已启用则返回 0，否则返回 1。此命令不打印任何内容。
- `rcvar` 显示哪些 [rc.conf(5)](../man5/rc.conf.5.md) 变量用于控制服务的启动（如果有）。

如果设置了 `pidfile` 或 `procname`，还支持：

- `poll` 等待命令退出。
- `status` 显示进程的状态。

其他支持的命令列在可选变量 `extra_commands` 中。

`argument` 可具有以下前缀之一，以改变其操作：

- `fast` 跳过对现有运行进程的检查，并设置 `rc_fast`=`YES`。
- `force` 跳过 `rcvar` 设置为 “`YES`” 的检查，并设置 `rc_force`=`YES`。这忽略 `argument``_precmd` 返回非零，并忽略任何 `required_*` 测试失败，并始终返回零退出状态。
- `one` 跳过 `rcvar` 设置为 “`YES`” 的检查，但执行所有其他先决条件测试。
- `quiet` 抑制一些详细诊断。目前，这包括消息 "Starting ${name}"（由 `rc.subr` 内的 `check_startmsgs` 检查）以及关于使用未在 [rc.conf(5)](../man5/rc.conf.5.md) 中启用的服务的错误。此前缀还设置 `rc_quiet`=`YES`。*注意：* `rc_quiet` 旨在不完全屏蔽所有调试和警告消息，而仅屏蔽某些小类别的消息。

`run_rc_command` 使用以下 shell 变量控制其行为。除非另有说明，这些变量都是可选的。

- `name` 此脚本的名称。此项不是可选的。
- `rcvar` `rcvar` 的值通过 `checkyesno` 检查，以确定是否应运行此方法。
- `command` 命令的完整路径。如果为每个支持的关键字定义了 `argument``_cmd`，则不需要。可被 `${name}_program` 覆盖。
- `command_args` `command` 的可选参数和/或 shell 指令。
- `command_interpreter` `command` 以下列方式启动：

  ```sh
  #! command_interpreter [...]
  ```

  这导致其 [ps(1)](../man1/ps.1.md) 命令为：

  ```sh
  command_interpreter [...] command
  ```

  因此使用该字符串来查找运行中命令的 PID，而不是 `command`。

- `extra_commands` 支持的额外命令/关键字/参数。
- `pidfile` PID 文件的路径。用于确定运行中命令的 PID。如果设置了 `pidfile`，使用：

  ```sh
  check_pidfile $pidfile $procname
  ```

  来查找 PID。否则，如果设置了 `command`，使用：

  ```sh
  check_process $procname
  ```

  来查找 PID。

- `procname` 要检查的进程名。默认为 `command` 的值。
- `required_dirs` 在运行 `start` 方法之前检查所列目录是否存在。此列表在运行 `start_precmd` 之前检查。
- `required_files` 在运行 `start` 方法之前检查所列文件的可读性。此列表在运行 `start_precmd` 之前检查。
- `required_modules` 在运行 `start` 方法之前确保所列内核模块已加载。此列表在运行 `start_precmd` 之后检查。这在调用 `start_precmd` 中的命令之后进行，以便如果预备命令指示错误条件，不会徒劳加载缺失的模块。列表中的单词可具有可选的 “`:`”`modname` 或 “`~`”`pattern` 后缀。`modname` 或 `pattern` 参数分别通过 `-m` 或 `-e` 选项传递给 `load_kld`。详情参见本文档中 `load_kld` 的描述。
- `required_vars` 在运行 `start` 方法之前对每个列表变量执行 `checkyesno`。此列表在运行 `start_precmd` 之后检查。
- `${name}_chdir` 在运行 `command` 之前要 `cd` 到的目录，如果未提供 `${name}_chroot`。
- `${name}_chroot` 在运行 `command` 之前要 [chroot(8)](chroot.8.md) 到的目录。仅在 **/usr** 挂载后支持。
- `${name}_env` 运行 `command` 的环境变量列表。除非定义了 `argument``_cmd`，否则这些变量将作为参数传递给 [env(1)](../man1/env.1.md) 工具。在这种情况下，`${name}_env` 的内容将通过 [sh(1)](../man1/sh.1.md) 的 export(1) 内建命令导出，这对变量名有一些限制（例如，变量名不能以数字开头）。
- `${name}_env_file` 用于 source 环境变量以运行 `command` 的文件。*注意：* 此文件中所有被赋值的变量都将导出到 `command` 的环境中。
- `${name}_fib` 运行 `command` 的 FIB `Routing Table` 号。更多细节参见 [setfib(1)](../man1/setfib.1.md)。
- `${name}_flags` 调用 `command` 的参数。这通常在 [rc.conf(5)](../man5/rc.conf.5.md) 中设置，而不在 [rc.d(8)](rc.d.8.md) 脚本中。环境变量 ‘`flags`’ 可用于覆盖此项。
- `${name}_nice` 运行 `command` 的 [nice(1)](../man1/nice.1.md) 级别。仅在 **/usr** 挂载后支持。
- `${name}_limits` 应用于 `command` 的资源限制。这将作为参数传递给 [limits(1)](../man1/limits.1.md) 工具。默认情况下，资源限制基于 `${name}_login_class` 中定义的登录类。
- `${name}_login_class` 与 `${name}_limits` 一起使用的登录类。默认为 “`daemon`”。
- `${name}_offcmd` 在服务未启用时启动期间运行的 shell 命令。
- `${name}_oomprotect` 当交换空间耗尽时，[protect(1)](../man1/protect.1.md) `command` 免于被终止。如果使用 “`YES`”，不保护任何子进程。如果为 “`ALL`”，保护所有子进程。
- `${name}_program` 命令的完整路径。如果两者都设置，则覆盖 `command`，但如果 `command` 未设置则无效。原则上，`command` 应在脚本中设置，而 `${name}_program` 应在 [rc.conf(5)](../man5/rc.conf.5.md) 中设置。
- `${name}_user` 运行 `command` 的用户，如果设置了 `${name}_chroot`，则使用 [chroot(8)](chroot.8.md)，否则使用 [su(1)](../man1/su.1.md)。仅在 **/usr** 挂载后支持。
- `${name}_group` 运行 chroot 后的 `command` 的组。
- `${name}_groups` 运行 chroot 后的 `command` 的补充组的逗号分隔列表。
- `${name}_prepend` 要前置于 `command` 的命令。这是 `${name}_env`、`${name}_fib` 或 `${name}_nice` 的通用版本。
- `${name}_setup` 在 `start`、`restart` 和 `reload` 期间在各自的 `argument``_precmd` 之前运行的可选命令。如果命令因任何原因失败，它将输出警告，但执行将继续。
- `argument``_cmd` 覆盖 `argument` 默认方法的 shell 命令。
- `argument``_precmd` 在运行 `argument``_cmd` 或 `argument` 的默认方法之前运行的 shell 命令。如果这返回非零退出码，则不执行主方法。如果正在执行默认方法，此检查在 `required_*` 检查和进程（非）存在性检查之后进行。
- `argument``_postcmd` 如果运行 `argument``_cmd` 或 `argument` 的默认方法返回零退出码，则运行的 shell 命令。
- `sig_stop` 在默认 `stop` 方法中发送给进程以停止的信号。默认为 `SIGTERM`。
- `sig_reload` 在默认 `reload` 方法中发送给进程以重新加载的信号。默认为 `SIGHUP`。

对于给定方法 `argument`，如果未定义 `argument``_cmd`，则 `run_rc_command` 提供默认方法：

| `Argument` | `Default method` |
| ---------- | ---------------- |
| `start` | 如果 `command` 未运行且 `checkyesno` `rcvar` 成功，则启动 `command`。 |
| `stop` | 用 `check_pidfile` 或 `check_process`（视情况而定）确定 `command` 的 PID，向这些 PID 发送 `kill` `sig_stop`，并对这些 PID 运行 `wait_for_pids`。 |
| `reload` | 类似于 `stop`，不同之处在于它使用 `sig_reload`，且不运行 `wait_for_pids`。与 `stop` 的另一个区别是 `reload` 默认不提供。如果合适，可通过 `extra_commands` 启用：`extra_commands=reload` |
| `restart` | 运行 `stop` 方法，然后运行 `start` 方法。 |
| `status` | 显示 `command` 的 PID，或某个其他脚本特定的状态操作。 |
| `poll` | 等待 `command` 退出。 |
| `rcvar` | 显示使用哪个 [rc.conf(5)](../man5/rc.conf.5.md) 变量（如果有）。此方法始终有效，即使相应的 [rc.conf(5)](../man5/rc.conf.5.md) 变量设置为 “`NO`”。 |

以下变量对方法（如 `argument``_cmd`）以及 `run_rc_command` 完成后可用：

- `rc_arg` 提供给 `run_rc_command` 的参数，在执行 fast 和 force 处理之后。
- `rc_flags` 启动默认命令的标志。默认为 `${name}_flags`，除非被环境变量 ‘`flags`’ 覆盖。此变量可由 `argument``_precmd` 方法更改。
- `rc_service` 正在执行的服务脚本的路径，以防它需要重新调用自身。
- `rc_pid` `command` 的 PID（如果适用）。
- `rc_fast` 如果使用了 “`fast`” 前缀则非空。
- `rc_force` 如果使用了 “`force`” 前缀则非空。

**`run_rc_script`** `file argument` 以参数 `argument` 启动脚本 `file`，并处理脚本的返回值。

在 `file` 启动之前，各种 shell 变量被取消设置：`name`、`command`、`command_args`、`command_interpreter`、`extra_commands`、`pidfile`、`rcvar`、`required_dirs`、`required_files`、`required_vars`、`argument``_cmd`、`argument``_precmd`、`argument``_postcmd`。

调用 `rc_trace` 以指示 `file` 将要运行。

但是，如果 `is_verified` `file` 失败，则直接返回。

`DebugOn` 将以从 `name` 和 `rc_arg` 派生的标签调用，如果任何标签出现在 `DEBUG_SH` 中则启用跟踪。

`run_rc_script` 执行 `file`，除非：

- `file` 以 `.sh` 结尾且位于 **/etc/rc.d**。
- `file` 似乎是备份或临时文件（例如，后缀为 `~`、`#`、`.OLD`、`,v` 或 `.orig`）。
- `file` 不可执行。

**`run_rc_scripts`** [`options`] `file ...` 对每个 `file` 调用 `run_rc_script`，除非它已被记录为已运行。

`options` 为：

- `--arg` `arg` 将 `arg` 传递给 `run_rc_script`，默认为由 [rc(8)](rc.8.md) 设置的 `_boot`。
- `--break` `break` 如果任何 `file` 匹配任何 `break`，则停止处理。

**`safe_dot`** `file ...` 当 [mac_veriexec(4)](../man4/mac_veriexec.4.md) 活动且 `file` 未验证时，由 `sdot` 使用。

此函数将 `file` 的输入限制为简单变量赋值，任何非字母数字字符替换为 **_**。

**`sdot`** `file ...` 用于读取配置文件。跳过不存在或为空的文件。尝试使用 `vdot`，如果失败（文件未验证），则回退到使用 `safe_dot`。

**`startmsg`** [`-n`] `message` 向 `stdout` 显示启动消息。应当使用它替代 echo(1)。如果 [rc.conf(5)](../man5/rc.conf.5.md) 变量 `rc_startmsgs` 设置为 “`NO`”，可关闭此输出的显示。

**`stop_boot`** [`always`] 阻止引导到多用户模式。如果 `autoboot` 变量设置为 `yes`（参见 [rc(8)](rc.8.md) 了解有关 `autoboot` 的更多信息），或 `checkyesno` `always` 指示真值，则向父进程（假定为 [rc(8)](rc.8.md)）发送 `SIGTERM` 信号。否则，shell 以非零状态退出。

**`vdot`** `file ...` 用于仅读取已验证的文件。

确保 shell `verify` 选项开启。此选项仅在 [mac_veriexec(4)](../man4/mac_veriexec.4.md) 活动时才有意义，否则此函数实际上与 `dot` 相同。

如果每个 `file` 存在且 `is_verfied` `file` 成功，则读取它，否则将返回码设置为 80（EAUTH）。

恢复 `verify` 选项的先前状态。

**`wait_for_pids`** [`pid ...`] 等待直到所有提供的 `pids` 不再存在，每两秒打印一次未完成的 `pids` 列表。

**`warn`** `message` 向 `stderr` 显示警告消息，并使用 [logger(1)](../man1/logger.1.md) 将其记录到系统日志。警告消息由脚本名（来自 `$0`）、后跟 “: WARNING: ”、然后是 `message` 组成。

## 文件

**/etc/rc.subr** `rc.subr` 文件位于 **/etc**。

## 参见

[rc.conf(5)](../man5/rc.conf.5.md), [debug.sh(8)](debug.sh.8.md), [rc(8)](rc.8.md)

## 历史

`rc.subr` 脚本出现在 NetBSD 1.3 中。[rc.d(8)](rc.d.8.md) 支持函数出现在 NetBSD 1.5 中。`rc.subr` 脚本首次出现在 FreeBSD 5.0 中。
