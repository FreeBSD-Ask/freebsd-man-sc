# rc.local(8)

`rc` — 自动重启和守护进程启动的命令脚本

## 名称

`rc`

## 概要

`rc rc.conf rc.conf.local rc.d/ rc.firewall rc.local rc.resume rc.shutdown rc.subr rc.suspend`

## 描述

`rc` 工具是控制自动引导过程的命令脚本，由 [init(8)](init.8.md) 调用。`rc.local` 脚本包含仅与特定站点相关的命令。如今通常使用 **/usr/local/etc/rc.d/** 机制替代 `rc.local`，但如果你想使用 `rc.local`，仍然受支持。在这种情况下，它应当 source **/etc/rc.conf** 并包含系统额外的自定义启动代码。然而，处理 `rc.local` 的最佳方式是将其拆分为 `rc.d/` 风格的脚本，放置在 **/usr/local/etc/rc.d/** 下。`rc.conf` 文件包含启动脚本引用的全局系统配置信息，而 `rc.conf.local` 包含本地系统配置。更多信息请参见 [rc.conf(5)](../man5/rc.conf.5.md)。

`rc.d/` 目录包含将在引导时和关机时自动执行的脚本。

[service(8)](service.8.md) 命令提供了管理 rc.d 服务的便捷接口。

[sysrc(8)](sysrc.8.md) 命令提供了修改系统配置文件的脚本接口。

### rc 的操作

- 验证 **/dev/null** 存在且为字符设备。如果不是，`rc` 打印错误消息并终止。这通常是由于忘记在 jail 配置中启用 devfs(5) 引起的。
- 如果是自动引导，设置 `autoboot`=`yes` 并启用一个标志（`rc_fast`=`yes`），该标志阻止 `rc.d/` 脚本执行对已在运行进程的检查（从而加速引导过程）。当 `rc` 在退出单用户 shell 后启动时，不会发生此 `rc_fast`=`yes` 加速。
- 判断系统是否正在无盘引导，如果是，则运行 **/etc/rc.initdiskless** 脚本。
- source **/etc/rc.subr** 以加载各种 [rc.subr(8)](rc.subr.8.md) shell 函数以供使用。
- 加载配置文件（重新加载见下文）。
- 判断是否在 jail 中引导，并将 “`nojail`”（不允许 jail）或 “`nojailvnet`”（仅允许启用 vnet 的 jail）添加到 [rcorder(8)](rcorder.8.md) 中要跳过的 KEYWORDS 列表中。
- 如果文件 `${firstboot_sentinel}` 不存在，将 “`firstboot`” 添加到 [rcorder(8)](rcorder.8.md) 中要跳过的 KEYWORDS 列表中。
- 调用 [rcorder(8)](rcorder.8.md) 对 **/etc/rc.d/** 中没有 “`nostart`” KEYWORD 的文件进行排序（参见 [rcorder(8)](rcorder.8.md) 的 `-s` 标志）。
- 调用 `run_rc_scripts()` 并传入要运行的脚本列表。对于每个脚本，将调用 `run_rc_script()`（两个函数均来自 [rc.subr(8)](rc.subr.8.md)），该函数将 `$1` 设置为 “`start`”，并在子 shell 中 source 该脚本。当作为 `$early_late_divider` 值的脚本运行后，停止处理。
- 再次检查文件 `${firstboot_sentinel}` 是否存在（以防它位于新挂载的文件系统上），并相应调整要跳过的 KEYWORDS 列表。
- 重新运行 [rcorder(8)](rcorder.8.md)，这次包括 `$local_startup` 目录中的脚本。用新的脚本列表再次调用 `run_rc_scripts()`。它将跳过已运行的脚本，并按上述方式执行其余脚本。
- 如果文件 `${firstboot_sentinel}` 存在，删除它。如果文件 `${firstboot_sentinel}-reboot` 也存在（因为它是被某个脚本创建的），则删除它并重启。

### rc.shutdown 的操作

- 将 `rc_shutdown` 设置为传递给 `rc.shutdown` 的第一个参数的值，如果未传递参数，则设置为 “`unspecified`”。
- source **/etc/rc.subr** 以加载各种 [rc.subr(8)](rc.subr.8.md) shell 函数以供使用。
- 加载配置文件。
- 调用 [rcorder(8)](rcorder.8.md) 对 **/etc/rc.d/** 和 `$local_startup` 目录中具有 “`shutdown`” KEYWORD 的文件进行排序（参见 [rcorder(8)](rcorder.8.md) 的 `-k` 标志），反转该顺序，并将结果赋值给一个变量。
- 使用 `run_rc_script()`（来自 [rc.subr(8)](rc.subr.8.md)）依次调用每个脚本，该函数将 `$1` 设置为 “`faststop`”，并在子 shell 中 source 该脚本。

### rc.d/ 的内容

`rc.d/` 位于 **/etc/rc.d/**。`rc.d/` 中当前使用以下文件命名约定：

`ALLUPPERCASE` 作为“占位符”的脚本，用于确保某些操作在其他操作之前执行。按启动顺序，这些是：

- `FILESYSTEMS` 确保根文件系统和其他关键文件系统已挂载。这是默认的 `$early_late_divider`。
- `NETWORKING` 确保基本网络服务正在运行，包括一般网络配置。
- `SERVERS` 确保为早期启动的服务（如 `nisdomain`）提供基本服务，因为下面的 `DAEMON` 需要它们。
- `DAEMON` 在所有通用守护进程（如 `lpd` 和 `ntpd`）之前的检查点。
- `LOGIN` 在用户登录服务（`inetd` 和 `sshd`）以及可能以用户身份运行命令的服务（`cron` 和 `sendmail`）之前的检查点。

`bar` 在子 shell 中 source 的脚本。如果此类脚本以非零状态终止，引导不会停止，但脚本在必要时可通过调用 `stop_boot()` 函数（来自 [rc.subr(8)](rc.subr.8.md)）来停止引导。

每个脚本都应包含 [rcorder(8)](rcorder.8.md) 关键字，特别是适当的 “`PROVIDE`” 条目，必要时还需 “`REQUIRE`” 和 “`BEFORE`” 关键字。

每个脚本预期至少支持以下参数，如果使用 `run_rc_command()` 函数，这些参数将自动受支持：

`start` 启动服务。这应当检查服务是否按 [rc.conf(5)](../man5/rc.conf.5.md) 的指定启动。还会检查服务是否已在运行，如果是则拒绝启动。如果系统直接启动到多用户模式，标准 FreeBSD 脚本不执行后一项检查，以加速引导过程。如果给定 `forcestart`，则忽略 [rc.conf(5)](../man5/rc.conf.5.md) 检查并强制启动。

`stop` 如果服务按 [rc.conf(5)](../man5/rc.conf.5.md) 的指定启动，则停止服务。这应当检查服务是否正在运行，如果不是则发出抱怨。如果给定 `forcestop`，则忽略 [rc.conf(5)](../man5/rc.conf.5.md) 检查并尝试停止。

`restart` 执行 `stop` 然后执行 `start`。

`status` 如果脚本启动一个进程（而非执行一次性操作），则显示进程的状态。否则无需支持此参数。默认显示程序的进程 ID（如果正在运行）。

`enable` 在 [rc.conf(5)](../man5/rc.conf.5.md) 中启用服务。

`disable` 在 [rc.conf(5)](../man5/rc.conf.5.md) 中禁用服务。

`delete` 从 [rc.conf(5)](../man5/rc.conf.5.md) 中移除服务。如果 `service_delete_empty` 设置为 “`YES`”，**/etc/rc.conf.d/$servicename** 在修改后如果为空将被删除。

`describe` 打印脚本功能的简短描述。

`extracommands` 打印脚本的非标准命令。

`poll` 如果脚本启动一个进程（而非执行一次性操作），则等待命令退出。否则无需支持此参数。

`enabled` 如果服务已启用则返回 0，否则返回 1。此命令不打印任何内容。

`rcvar` 显示哪些 [rc.conf(5)](../man5/rc.conf.5.md) 变量用于控制服务的启动（如果有）。

如果脚本必须实现额外命令，可以在 `extra_commands` 变量中列出它们，并在由命令名构造的变量中定义其行为（参见 实例 章节）。

配置文件通常在引导序列开始时只读取一次；如果某个脚本需要 `enable` 或 `disable` 序列中稍后运行的任何其他脚本，它必须向 rc 进程（由 `$RC_PID` 标识）发送 `SIGALRM` 信号，使其重新读取文件。

以下要点适用于 **/usr/local/etc/rc.d/** 中的旧式脚本：

- 脚本仅在其 [basename(1)](../man1/basename.1.md) 匹配 shell 通配模式 `*.sh` 且可执行时才被执行。目录中存在的任何其他文件或目录都将被静默忽略。
- 在引导时执行脚本时，将字符串 “`start`” 作为其第一个且唯一的参数传递。在关机时，将字符串 “`stop`” 作为其第一个且唯一的参数传递。所有 `rc.d/` 脚本预期都能适当处理这些参数。如果在给定时间（引导时或关机时）无需采取任何操作，脚本应当成功退出且不产生错误消息。
- 每个目录中的脚本按字典顺序执行。如果需要特定顺序，可在现有文件名前使用数字作为前缀，例如 `100.foo` 将在 `200.bar` 之前执行；不带数字前缀时则相反。
- 每个脚本的传统输出是一个空格字符，后跟正在启动或关闭的软件包名称，*不带* 末尾换行符。

## 相关脚本

当自动重启进行时，`rc` 以 `autoboot` 参数调用。从 **/etc/rc.d/** 运行的脚本之一是 **/etc/rc.d/fsck**。此脚本运行 fsck(8)，带 `-p` 和 `-F` 选项，以“清理”（preen）所有磁盘因上次系统关机造成的轻微不一致。如果失败，则由硬件或软件故障引起的严重不一致的检查/修复将在引导过程结束时在后台执行。如果未设置 `autoboot`，例如从单用户模式转到多用户模式时，脚本不执行任何操作。

**/etc/rc.d/serial** 脚本用于设置串行设备的任何特殊配置。

`rc.firewall` 脚本用于配置基于内核的防火墙服务的规则。它有以下几种可能的选项：

`open` 允许任何人进入

`client` 尝试仅保护本机

`simple` 尝试保护整个网络

`closed` 完全禁用 IP 服务，通过 `lo0` 接口除外

`UNKNOWN` 禁用防火墙规则的加载

`filename` 将加载指定文件名中的规则（需要完整路径）。

大多数守护进程（包括网络相关守护进程）在 **/etc/rc.d/** 中都有自己的脚本，可用于启动、停止和检查服务状态。

任何架构特定的脚本，例如 **/etc/rc.d/apm**，在启动守护进程之前会专门检查它们是否在该架构上运行。

按照传统，所有启动文件都位于 **/etc**。

## 文件

**/etc/rc**

**/etc/rc.conf**

**/etc/rc.conf.local**

**/etc/rc.d/**

**/etc/rc.firewall**

**/etc/rc.local**

**/etc/rc.shutdown**

**/etc/rc.subr**

**/var/run/dmesg.boot** [dmesg(8)](dmesg.8.md) 结果，`rc` 进程开始后不久生成。当内核中的 [dmesg(8)](dmesg.8.md) 缓冲区不再有此信息时很有用。

## 实例

以下是一个最小的 `rc.d/` 风格脚本。大多数脚本所需的不多于此。

```sh
#!/bin/sh
#
# PROVIDE: foo
# REQUIRE: bar_service_required_to_precede_foo
. /etc/rc.subr
name="foo"
rcvar=foo_enable
command="/usr/local/bin/foo"
load_rc_config $name
run_rc_command "$1"
```

某些脚本可能希望提供增强功能。用户可通过附加命令访问此功能。脚本可按需列出和定义任意多的命令。

```sh
#!/bin/sh
#
# PROVIDE: foo
# REQUIRE: bar_service_required_to_precede_foo
# BEFORE:  baz_service_requiring_foo_to_precede_it
. /etc/rc.subr
name="foo"
rcvar=foo_enable
command="/usr/local/bin/foo"
extra_commands="nop hello"
hello_cmd="echo Hello World."
nop_cmd="do_nop"
do_nop()
{
	echo "I do nothing."
}
load_rc_config $name
run_rc_command "$1"
```

由于所有进程在关机时都被 [init(8)](init.8.md) 终止，显式的 [kill(1)](../man1/kill.1.md) 是不必要的，但通常会包含。

## 参见

[kill(1)](../man1/kill.1.md), [rc.conf(5)](../man5/rc.conf.5.md), [init(8)](init.8.md), [rc.resume(8)](rc.resume.8.md), [rc.subr(8)](rc.subr.8.md), [rcorder(8)](rcorder.8.md), [reboot(8)](reboot.8.md), savecore(8), [service(8)](service.8.md), [sysrc(8)](sysrc.8.md)

> "Practical rc.d scripting in BSD"：<https://docs.freebsd.org/en/articles/rc-scripting/>

## 历史

`rc` 工具出现在 4.0BSD 中。
