  RC(8)  

RC(8)

FreeBSD System Manager's Manual

RC(8)

[名称](#__u540D___u79F0_)
=======================

`rc` —

自动重启和守护进程启动的命令脚本

[概要](#__u6982___u8981_)
=======================

`rc` `rc.conf` `rc.conf.local` `rc.d/` `rc.firewall` `rc.local` `rc.resume` `rc.shutdown` `rc.subr`

[描述](#__u63CF___u8FF0_)
=======================

`rc` 实用程序是在被 init(8) 调用后控制自动引导过程的命令脚本。 `rc.local` 脚本包含仅与特定站点相关的命令。 通常，现在使用 /usr/local/etc/rc.d/ 机制代替 `rc.local` ，但如果您想使用 `rc.local` ，它仍然受支持。 在这种情况下，它应该来自 /etc/rc.conf 并包含您系统的额外自定义启动代码。 然而，处理 `rc.local` 的最佳方法是将其分离为 `rc.d/` 样式的脚本，并将它们放在 /usr/local/etc/rc.d/ 下。 `rc.conf` 文件包含启动脚本引用的全局系统配置信息，而 `rc.conf.local` 包含本地系统配置。有关详细信息，请参阅 rc.conf(5) 。

`rc.d/` 目录包含将在启动时和关机时自动执行的脚本。

service(8) 命令提供了一个方便的接口来管理 rc.d 服务。

sysrc(8) 命令提供了一个脚本接口来修改系统配置文件。

`操作`
----

1.  如果是自动引导，设置 autoboot\=`yes` 并启用一个标志 (rc\_fast\=`yes`), 它可以防止 `rc.d/` 脚本对已经运行的进程进行检查（从而加快引导过程）。 在退出单用户 shell 后启动 `rc` 时，不会发生此 rc\_fast\=`yes` 加速。
2.  确定系统是否在无盘引导，如果是，则运行 /etc/rc.initdiskless 脚本。
3.  来源 /etc/rc.subr 以加载各种 rc.subr(8) 函数以使用。
4.  加载配置文件。
5.  确定是否在监狱中启动，并将 “`nojail`” （不允许监狱）或 “`nojailvnet`” （仅允许启用 vnet 的监狱）添加到要在 rcorder(8) 中跳过的关键字列表中。
6.  如果文件 ${firstboot\_sentinel} 不存在，请在 rcorder(8) 中将 “`firstboot`” 添加到要跳过的关键字列表中。
7.  调用 rcorder(8) 对 /etc/rc.d/ 中没有 “`nostart`” 关键字的文件进行排序（参考 rcorder(8) 的 `-s` 标志）。
8.  使用 `run_rc_script`() (来自 rc.subr(8)) 依次调用每个脚本，将 $1 设置为 “`start`”, 并在子 shell 中获取脚本。 当作为 $early\_late\_divider 值的脚本运行时停止处理。
9.  再次检查文件 ${firstboot\_sentinel} 是否存在（如果它位于新安装的文件系统上）并调整关键字列表以适当跳过。
10.  重新运行 rcorder(8), 这次包括 $local\_startup 目录中的脚本。 忽略 $early\_late\_divider 之前的所有内容，然后开始执行上述脚本。
11.  如果文件 ${firstboot\_sentinel} 存在，请将其删除。 如果文件 ${firstboot\_sentinel}-reboot 也存在（因为它是由脚本创建的），则将其删除并重新启动。

`rc.shutdown 操作`
----------------

1.  将 rc\_shutdown 设置为传递给 `rc.shutdown` 的第一个参数的值，如果没有传递任何参数，则设置为 “`unspecified`” 。
2.  来源 /etc/rc.subr 以加载各种 rc.subr(8) shell 函数以使用。
3.  加载配置文件。
4.  调用 rcorder(8) 对 /etc/rc.d/ 和 $local\_startup 目录中具有 “`shutdown`” 关键字的文件进行排序（参考 rcorder(8) 的 `-k` 标志），颠倒该顺序，并分配结果为一个变量。
5.  使用 `run_rc_script`() (来自 rc.subr(8)) 依次调用每个脚本，将 $1 设置为 “`faststop`” ，并在子 shell 中获取脚本。

`rc.d/ 内容`
----------

`rc.d/` 位于 /etc/rc.d/ 。当前在 `rc.d/` 中使用以下文件命名约定：

ALLUPPERCASE

作为 “placeholders” 的脚本，以确保某些操作在其他操作之前执行。 按照启动顺序，这些是：

FILESYSTEMS

确保安装了根文件系统和其他关键文件系统。 这是默认的 $early\_late\_divider 。

NETWORKING

确保基本网络服务正在运行，包括一般网络配置。

SERVERS

确保早期启动的服务（例如 nisdomain ）存在基本服务，因为下面的 DAEMON 需要这些服务。

DAEMON

在所有通用守护进程（如 lpd 和 ntpd ）之前检查点。

LOGIN

用户登录服务 (inetd 和 sshd) 之前的检查点，以及可能以用户身份运行命令的服务 (cron 和 sendmail) 。

bar

源自子外壳的脚本。 如果这样的脚本以非零状态终止，则引导不会停止，但如果需要，脚本可以通过调用 `stop_boot`() 函数（来自 rc.subr(8)) 来停止引导。

每个脚本都应包含 rcorder(8) 关键字，尤其是适当的 “`PROVIDE`” 条目，以及必要时的 “`REQUIRE`” 和 “`BEFORE`” 关键字。

每个脚本都应至少支持以下参数，如果它使用 `run_rc_command`() 函数，则会自动支持这些参数：

[`start`](#start)

启动服务。 这应该检查服务是否按照 rc.conf(5)-
的规定启动。 还检查服务是否已经在运行，如果是则拒绝启动。 如果系统直接启动到多用户模式，则标准 FreeBSD 脚本不会执行后一种检查，以加快启动过程。 如果给出了 `forcestart` ，忽略 rc.conf(5) 检查并继续启动。

[`stop`](#stop)

如果要按照 rc.conf(5) 的规定启动服务，请停止服务。 这应该检查服务是否正在运行，如果没有运行则抱怨。 如果给出 `forcestop` ，忽略 rc.conf(5) 检查并尝试停止。

[`restart`](#restart)

执行 `stop` 然后 `start` 。

[`status`](#status)

如果脚本启动一个进程（而不是执行一次性操作），则显示该进程的状态。 否则没有必要支持这个论点。 默认显示程序的进程 ID（如果正在运行）。

[`enable`](#enable)

在 rc.conf(5) 中启用该服务。

[`disable`](#disable)

在 rc.conf(5) 中禁用该服务。

[`delete`](#delete)

从 rc.conf(5) 中删除该服务。如果 ‘``` `service_delete_empty` ```’ 设置为 “`YES`” ，修改后 /etc/rc.conf.d/$servicename 为空会被删除。

[`describe`](#describe)

打印脚本功能的简短描述。

[`extracommands`](#extracommands)

打印脚本的非标准命令。

[`poll`](#poll)

如果脚本启动一个进程（而不是执行一次性操作），请等待命令退出。 否则没有必要支持这个论点。

[`enabled`](#enabled)

如果服务启用则返回 0，否则返回 1。 此命令不打印任何内容。

[`rcvar`](#rcvar)

显示哪些 rc.conf(5) 变量用于控制服务的启动（如果有）。

如果脚本必须实现额外的命令，它可以在 extra\_commands 变量中列出它们，并在由命令名称构造的变量中定义它们的操作（参见 [示例](#__u793A___u4F8B_) 部分）。

以下关键点适用于 /usr/local/etc/rc.d/ 中的旧式脚本：

*   只有当它们的 basename(1) 与 shell globbing 模式 \*.sh 匹配并且它们是可执行的时，才会执行脚本。 目录中存在的任何其他文件或目录都将被静默忽略。
*   当一个脚本在启动时执行时，它会传递字符串 “`start`” 作为它的第一个也是唯一的参数。 在关机时，它被传递字符串 “`stop`” 作为它的第一个也是唯一的参数。 所有 `rc.d/` 脚本都应该适当地处理这些参数。 如果在给定时间（启动时间或关闭时间）不需要采取任何操作，则脚本应该成功退出并且不会产生错误消息。
*   每个目录中的脚本按字典顺序执行。 如果需要特定的顺序，可以使用数字作为现有文件名的前缀，例如 100.foo 将在 200.bar; 之前执行；如果没有数字前缀，则相反。
*   每个脚本的输出通常是一个空格字符，后跟正在启动或关闭的软件包的名称，后面 _没有_ 换行符。

[感兴趣的脚本](#__u611F___u5174___u8DA3___u7684___u811A___u672C_)
===========================================================

当自动重启正在进行时，使用参数 `autoboot` 调用 `rc` 。 从 /etc/rc.d/ 运行的脚本之一是 /etc/rc.d/fsck 。 此脚本使用选项 `-p` 和 `-F` 运行 fsck(8) ，以 “preen” 上次系统关闭导致的所有轻微不一致的磁盘。 如果此操作失败，则将在引导过程结束时在后台执行由硬件或软件故障引起的严重不一致的检查/修复。 如果未设置 `autoboot` ，例如从单用户模式转到多用户模式时，脚本不会执行任何操作。

/etc/rc.d/local 脚本可以从多个 `rc.d/` 目录执行脚本。 默认位置包括 /usr/local/etc/rc.d/ ，但这些可能会被 local\_startup rc.conf(5) 变量覆盖。

/etc/rc.d/serial 脚本用于设置串行设备的任何特殊配置。

`rc.firewall` 脚本用于为基于内核的防火墙服务配置规则。它有几个可能的选项：

[`open`](#open)

将允许任何人进入

[`client`](#client)

将尝试仅保护这台机器

[`simple`](#simple)

将尝试保护整个网络

[`closed`](#closed)

完全禁用 IP 服务，除了通过 lo0 接口

[`UNKNOWN`](#UNKNOWN)

禁用加载防火墙规则

filename

将加载给定文件名中的规则（需要完整路径）。

大多数守护进程，包括网络相关的守护进程，在 /etc/rc.d/ 中都有自己的脚本，可用于启动、停止和检查服务的状态。

任何体系结构特定的脚本，例如 /etc/rc.d/apm ，在启动守护程序之前专门检查它们是否在该体系结构上。

按照传统，所有启动文件都驻留在 /etc 中。

[文件](#__u6587___u4EF6_)
=======================

/etc/rc

/etc/rc.conf

/etc/rc.conf.local

/etc/rc.d/

/etc/rc.firewall

/etc/rc.local

/etc/rc.shutdown

/etc/rc.subr

/var/run/dmesg.boot

dmesg(8) 会在 `rc` 进程开始后立即生成。 当内核中的 dmesg(8) 缓冲区不再具有此信息时很有用。

[实例](#__u5B9E___u4F8B_)
=======================

以下是一个最小的 `rc.d/` 样式脚本。 大多数脚本只需要以下内容。

#!/bin/sh # # PROVIDE: foo # REQUIRE: bar\_service\_required\_to\_precede\_foo . /etc/rc.subr name="foo" rcvar=foo\_enable command="/usr/local/bin/foo" load\_rc\_config $name run\_rc\_command "$1" 

某些脚本可能希望提供增强的功能。 用户可以通过附加命令访问此功能。该脚本可以根据需要列出和定义任意数量的命令。

#!/bin/sh # # PROVIDE: foo # REQUIRE: bar\_service\_required\_to\_precede\_foo # BEFORE: baz\_service\_requiring\_foo\_to\_precede\_it . /etc/rc.subr name="foo" rcvar=foo\_enable command="/usr/local/bin/foo" extra\_commands="nop hello" hello\_cmd="echo Hello World." nop\_cmd="do\_nop" do\_nop() { echo "I do nothing." } load\_rc\_config $name run\_rc\_command "$1" 

由于所有进程在关闭时都会被 init(8) 杀死，因此显式 kill(1) 是不必要的，但通常会包含在内。

[参见](#__u53C2___u89C1_)
=======================

kill(1), rc.conf(5), init(8), rc.resume(8), rc.subr(8), rcorder(8), reboot(8), savecore(8), service(8), sysrc(8)

[历史](#__u5386___u53F2_)
=======================

`rc` 实用程序出现在 4.0BSD 中。

October 6, 2020

FreeBSD 13.1-RELEASE