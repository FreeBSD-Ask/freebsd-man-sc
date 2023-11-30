  SHUTDOWN(8)  

SHUTDOWN(8)

FreeBSD System Manager's Manual

SHUTDOWN(8)

[名称](#__u540D___u79F0_)
=======================

`shutdown`, `poweroff` —

在给定时间关闭系统

[概要](#__u6982___u8981_)
=======================

`shutdown` \[`-`\] \[`-c` | `-h` | `-p` | `-r` | `-k`\] \[`-o` \[`-n`\]\] time \[warning-message ...\] `poweroff`

[描述](#__u63CF___u8FF0_)
=======================

`shutdown` 实用程序为超级用户提供了一个自动关闭程序，以便在系统关闭时很好地通知用户，使他们免受系统管理员、黑客和专家的影响，否则他们不会为这些细节烦恼。

可以使用以下选项：

[`-c`](#c)

系统会在指定时间重新上电（关闭电源然后重新打开）。 如果硬件不支持电源循环，系统将重新启动。 目前，只有实现此功能的 ipmi(4) 驱动程序支持的 BMC 系统才支持此标志。 系统关闭的时间取决于实现此功能的设备。

[`-h`](#h)

系统在指定 time 停止。

[`-p`](#p)

系统在指定 time 停止并关闭电源（需要硬件支持，否则系统停止）。

[`-r`](#r)

系统在指定 time 重新启动。

[`-k`](#k)

把大家踢开。 `-k` 选项实际上并没有停止系统，而是让系统多用户登录禁用（除了超级用户之外的所有用户）。

[`-o`](#o)

如果指定了 `-c`, `-h`, `-p` 或 `-r` 选项之一, `shutdown` 将执行 halt(8) 或 reboot(8) ，而不是向 init(8) 发送信号。

[`-n`](#n)

如果指定了 `-o` 选项，则通过将 `-n` 传递给 halt(8) 或 reboot(8) 来防止文件系统缓存被刷新。 可能不应该使用此选项。

time

Time 是关闭将导致系统 `shutdown` 的时间，可能是不区分大小写的单词 now （表示立即关闭）或未来时间，采用以下两种格式之一： +number 或 yymmddhhmm, 其中年、月和day 可能默认为当前系统值。 第一种形式以 number 分钟数使系统停机，第二种形式在指定的绝对时间。 +number 可以通过附加相应的后缀以分钟以外的单位指定： “`s`”, “`sec`”, “`m`”, “`min`”, “`h`”, “`hour`” 。

如果指定了绝对时间，但没有指定日期，并且今天的时间已经过去， `shutdown` 将假定明天是同一时间。 （如果指定的完整日期已经过去， `shutdown` 将打印错误并退出而不关闭系统。）

warning-message

任何其他参数都包含向当前登录系统的用户广播的警告消息。

`-`

如果提供 ‘`-`’ 作为选项，则从标准输入读取警告消息。

每隔一段时间，随着世界末日的临近而变得更加频繁，并在关闭前十小时开始，警告消息会显示在所有登录用户的终端上。 关机前五分钟，或者如果关机时间少于 5 分钟，则通过创建 /var/run/nologin 并在此处复制警告消息来禁用登录。 如果用户尝试登录时该文件存在， login(1) 将打印其内容并退出。该文件在 `shutdown` 退出之前被删除。

在关机时，系统日志中会写入一条消息，其中包含关机时间、发起关机的人员和原因。 然后将相应的信号发送到 init(8) 以分别停止、重新启动或使系统进入单用户状态（取决于上述选项）。 关闭时间和警告消息放在 /var/run/nologin 中，应该用于通知用户系统何时备份以及它为什么会关闭（或其他任何东西）。

可以通过终止 `shutdown` 进程来取消计划的关闭（一个 `SIGTERM` 就足够了）。 `shutdown` 创建的 /var/run/nologin 文件将被自动删除。

不带选项运行时， `shutdown` 实用程序将在指定 time 将系统置于单用户模式。

调用 “`poweroff`” 相当于运行：

shutdown -p now 

[文件](#__u6587___u4EF6_)
=======================

/var/run/nologin

告诉 login(1) 不要让任何人登录

[实例](#__u5B9E___u4F8B_)
=======================

30分钟后重启系统，在所有当前登录用户的终端上显示警告信息：

`# shutdown -r +30 "System will reboot"`

[兼容性](#__u517C___u5BB9___u6027_)
================================

第二种时间格式的小时和分钟可以用冒号 (\`\`:'') 分隔，以实现向后兼容。

[参见](#__u53C2___u89C1_)
=======================

kill(1), login(1), wall(1), nologin(5), halt(8), init(8), reboot(8)

[历史](#__u5386___u53F2_)
=======================

`shutdown` 命令最初是由 Ian Johnstone 为 UNSW 修改后的 AT&T UNIX 6th Edn 编写的。 它经过修改，然后并入 4.1BSD 。

January 11, 2020

FreeBSD 13.1-RELEASE