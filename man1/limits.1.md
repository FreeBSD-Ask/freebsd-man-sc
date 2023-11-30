  LIMITS(1)  

LIMITS(1)

FreeBSD General Commands Manual

LIMITS(1)

[名称](#__u540D___u79F0_)
=======================

`limits` —

设置或显示进程资源限制

[概要](#__u6982___u8981_)
=======================

`limits` \[`-C` class | `-P` pid | `-U` user\] \[`-SHB`\] \[`-ea`\] \[`-bcdfklmnopstuvw` \[val\]\] `limits` \[`-C` class | `-U` user\] \[`-SHB`\] \[`-bcdfklmnopstuvw` \[val\]\] \[`-E`\] \[\[name\=value ...\] command\]

[描述](#__u63CF___u8FF0_)
=======================

`limits` 实用程序打印或设置内核资源限制，并且可以选择设置环境变量，如 env(1) 并使用选定的资源运行程序。 `limits` 实用程序的三种用途是可能的：

`limits` \[limitflags\] \[name\=value ...\] command

此用法根据 limitflags 设置限制，可选择设置以 name\=value 对形式给出的环境变量，然后运行指定的 command 。

`limits` \[limitflags\]

此用法根据 limitflags 确定资源设置的值，不尝试设置它们并将这些值输出到标准输出。 默认情况下，这将输出调用进程的当前内核资源设置。 使用 `-C` class 或 `-U` user 用户选项，您还可以显示由 login.conf(5) 登录功能数据库中适当的登录类资源限制条目修改的当前资源设置。

`limits` `-e` \[limitflags\]

此用法根据 limitflags 确定资源设置的值，但不设置它们。 与前面的用法一样，它将这些值输出到标准输出，除了它将以 `eval` 格式发出它们，适用于调用 shell。 如果 shell 是已知的（即它是 `sh`, `csh`, `bash`, `tcsh`, `ksh`, `pdksh` 或 `rc` 之一）， `limits` 会以该 shell 理解的格式发出 `limit` 或 `ulimit` 命令。 如果无法确定 shell 的名称，则使用 sh(1) 使用的 `ulimit` 格式。

这对于设置脚本使用的限制，或预先启动具有特定资源限制设置的守护程序和其他后台任务非常有用，并且通过在登录类数据库中维护一个中央设置数据库来提供允许全局配置最大资源使用的好处.

在shell脚本中， `limits` 通常会与eval一起使用，如下所示:

```eval `limits -e -C daemon` ```

它导致当前 shell 计算和设置 `limits` 的输出。

上面指定的 limitflags 值包含以下一个或多个选项：

[`-C`](#C) class

使用当前资源值，由适用于登录类 class 的资源条目修改。

[`-U`](#U) user

使用当前资源值，由适用于 user 所属登录类的资源条目修改。 如果用户不属于任何类，则使用 “`default`” 类的资源能力（如果存在），或者如果用户是超级用户帐户，则使用 “`root`” 类。

[`-P`](#P) pid

为 pid 标识的进程选择或设置限制。

[`-S`](#S)

选择 “soft” （或当前）资源限制的显示或设置。 如果特定限制设置遵循此开关，则只有软限制会受到影响，除非稍后使用 `-H` 或 `-B` 选项覆盖。

[`-H`](#H)

选择 “hard” （或最大）资源限制的显示或设置。 如果特定限制设置遵循此开关，则只有硬限制会受到影响，直到稍后使用 `-S` 或 `-B` 选项覆盖。

[`-B`](#B)

选择显示或设置 “soft” （当前）或 “hard” （最大）资源限制。 如果特定限制设置遵循此开关，则软限制和硬限制都会受到影响，直到稍后使用 `-S` 或 `-H` 选项覆盖。

[`-e`](#e)

选择 “eval mode” 格式输出。 这仅在显示模式下有效，不能在运行命令时使用。 用于输出的确切语法取决于调用 `limits` 的 shell 类型。

[`-b`](#b) \[val\]

选择或设置 sbsize 资源限制。

[`-c`](#c) \[val\]

选择或设置（如果指定了 val ) coredumpsize 资源限制。值 0 禁用核心转储。

[`-d`](#d) \[val\]

选择或设置（如果指定了 val ) datasize 资源限制。

[`-f`](#f) \[val\]

选择或设置 filesize 资源限制。

[`-k`](#k) \[val\]

选择或设置 kqueues 资源限制。

[`-l`](#l) \[val\]

选择或设置 memorylocked 资源限制。

[`-m`](#m) \[val\]

选择或设置 memoryuse 大小限制。

[`-n`](#n) \[val\]

选择或设置 openfiles 资源限制。 可以通过检查 kern.maxfilesperproc sysctl(8) 变量来查看每个进程的最大打开文件数的系统范围限制。 整个系统中同时打开的文件总数限制为 kern.maxfiles sysctl(8) 变量显示的值。

[`-o`](#o) \[val\]

选择或设置 umtxp 资源限制。 该限制决定了用户拥有的进程可以同时创建的进程共享锁的最大数量，请参见 pthread(3) 。

[`-p`](#p) \[val\]

选择或设置 pseudoterminals 资源限制。

[`-s`](#s) \[val\]

选择或设置 stacksize 资源限制。

[`-t`](#t) \[val\]

选择或设置 cputime 资源限制。

[`-u`](#u) \[val\]

选择或设置 maxproc 资源限制。 可以通过检查 kern.maxprocperuid sysctl(8) 变量来查看每个 UID 允许的最大进程数的系统范围限制。 整个系统中可以同时运行的最大进程数限制为 kern.maxproc sysctl(8) 变量的值。

[`-v`](#v) \[val\]

选择或设置 virtualmem 资源限制。此限制包含用户进程的整个 VM 空间，包括文本、数据、bss、堆栈、 brk(2) 、 sbrk(2) 和 mmap(2) 的空间。

[`-w`](#w) \[val\]

选择或设置 swapuse 资源限制。

上述选项集中 val 的有效值由字符串 “`infinity 、`” “`inf 、`” “`unlimited`” 或 “`unlimit`” 组成，表示无限（或内核定义的最大值）限制，或者可选地后跟一个数字值后缀。 与大小相关的值默认为以字节为单位的值，或者可以使用以下后缀之一作为乘数：

[`b`](#b_2)

512 字节块。

[`k`](#k_2)

千字节（1024 字节）。

[`m`](#m_2)

兆字节（1024\*1024 字节）。

[`g`](#g)

千兆字节。

[`t`](#t_2)

太字节。

cputime 资源默认为秒数，但可以使用乘数，并且与大小值一样，由有效后缀分隔的多个值相加：

[`s`](#s_2)

秒。

[`m`](#m_3)

分钟。

[`h`](#h)

小时。

[`d`](#d_2)

天。

[`w`](#w_2)

周。

[`y`](#y)

365 天年。

[`-E`](#E)

导致 `limits` 完全忽略它继承的环境。

[`-a`](#a)

强制显示所有资源设置，即使已指定其他特定资源设置。 例如，如果您希望在启动 Usenet News 系统时禁用核心转储，但又希望设置适用于 “`news`” 帐户的所有其他资源设置，您可以使用：

```eval `limits -U news -aBec 0` ```

与 setrlimit(2) 调用一样，只有超级用户可以提高进程 “hard” 资源限制。 但是，非 root 用户可以降低它们或将 “soft” 资源限制更改为低于硬限制的任何值。当被调用来执行程序时， `limits` 未能提高硬限制将被认为是致命错误。

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

如果使用不正确， `limits` 实用程序会以 `EXIT_FAILURE` 退出；即，在同一调用中选择了无效选项或设置/显示选项，在运行程序时使用 `-e` 等。 在显示或评估模式下运行时， `limits` 以 `EXIT_SUCCESS` 状态退出。 当以命令模式运行并且命令执行成功时，退出状态将是执行程序返回的任何内容。

[实例](#__u5B9E___u4F8B_)
=======================

显示当前堆栈大小限制：

$ limits -s Resource limits (current): stacksize 524288 kB 

尝试以 1 字节的 datasize 限制运行 ls(1) :

$ limits -d 1b ls Data segment size exceeds process limit Abort trap 

产生 ‘`eval mode`’ 输出以将 sbsize 限制为 1 字节。 从 sh(1) 运行命令时获得的输出：

$ limits -e -b 1b ulimit -b 512; 

同上 csh(1)

% limits -e -b 1b limit -h sbsize 512; limit sbsize 512; 

[参见](#__u53C2___u89C1_)
=======================

csh(1), env(1), limit(1), sh(1), getrlimit(2), setrlimit(2), login\_cap(3), login.conf(5), rctl(8), sysctl(8)

[历史](#__u5386___u53F2_)
=======================

`limits` 实用程序首次出现在 FreeBSD 2.1.7 中。

[作者](#__u4F5C___u8005_)
=======================

`limits` 实用程序由 David Nugent <[davidn@FreeBSD.org](mailto:davidn@FreeBSD.org)\> 编写。

[缺陷](#__u7F3A___u9677_)
=======================

由于显而易见的原因， `limits` 实用程序不处理名称中带有等号 (‘`=`’) 的命令。

`limits` 实用程序不努力确保发出或显示的资源设置有效且可由当前用户设置。 只有超级用户帐户可以提高硬限制，如果给定的值太高， FreeBSD 内核会默默地将限制降低到小于指定的值。

June 25, 2020

FreeBSD 13.1-RELEASE