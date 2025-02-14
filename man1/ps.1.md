  PS(1)  

PS(1)

FreeBSD General Commands Manual

PS(1)

[名称](#__u540D___u79F0_)
=======================

`ps` —

process status

[概要](#__u6982___u8981_)
=======================

`ps` \[`--libxo`\] \[`-aCcdefHhjlmrSTuvwXxZ`\] \[`-O` fmt | `-o` fmt\] \[`-G` gid\[,gid...\]\] \[`-J` jid\[,jid...\]\] \[`-M` core\] \[`-N` system\] \[`-p` pid\[,pid...\]\] \[`-t` tty\[,tty...\]\] \[`-U` user\[,user...\]\] `ps` \[`--libxo`\] \[`-L`\]

[描述](#__u63CF___u8FF0_)
=======================

`ps` 实用程序显示一个标题行，然后是包含有关具有控制终端的所有进程的信息的行。 如果指定了 `-x` 选项， `ps` 还将显示没有控制终端的进程。

通过使用 `-a` `-、` `-G` `-、` `-J` `-、` `-p` `-、` `-T` `-、` `-t` 和 `-U` 选项的任意组合，可以选择不同的进程集进行显示。 如果给出了这些选项中的一个以上，则 `ps` 将选择与至少一个给定选项匹配的所有进程。

对于已选择显示的进程， `ps` 通常每个进程显示一行。 `-H` 选项可能会导致某些进程有多个输出行（每个线程一行）。 默认情况下，所有这些输出行首先按控制终端排序，然后按进程 ID。 `-m` `-、` `-r` `-、` `-u` 和 `-v` 选项将更改排序顺序。 如果给出了多个排序选项，则所选进程将按指定的最后一个排序选项排序。

对于已选择显示的进程，要显示的信息是根据一组关键字选择的（请参阅 `-L` `-、` `-O` 和 `-o`-
选项）。 对于每个进程，默认输出格式包括进程的 ID、控制终端、状态、CPU 时间（包括用户和系统时间）和相关命令。

如果 `ps` 进程与终端关联，则默认输出宽度为终端宽度；否则输出宽度是无限的。 另请参见 `-w` 选项。

选项如下：

[`--libxo`](#-libxo)

通过 libxo(3) 以不同的人类和机器可读格式生成输出。 有关命令行参数的详细信息，请参阅 xo\_parse\_args(3) 。

[`-a`](#a)

显示有关其他用户进程以及您自己进程的信息。 如果 security.bsd.see\_other\_uids 设置为零，则仅当用户的 UID 为 0 时才使用此选项。

[`-c`](#c)

将 “command” 列输出更改为仅包含可执行文件名称，而不是完整的命令行。

[`-C`](#C)

通过使用忽略 “resident” 时间的 “raw” CPU 计算更改 CPU 百分比的计算方式（这通常无效）。

[`-d`](#d)

将进程排列成后代顺序，并在每个命令前加上缩进文本，将兄弟关系和父/子关系显示为树。 如果还使用了 `-m` 和 `-r` 选项中的任何一个，它们将控制兄弟进程相对于彼此的排序方式。 请注意，如果 “command” 列不是显示的最后一列，则此选项无效。

[`-e`](#e)

也显示环境。

[`-f`](#f)

显示有关换出进程的命令行和环境信息。 仅当用户的 UID 为 0 时才使用此选项。

[`-G`](#G)

显示有关使用指定实际组 ID 运行的进程的信息。

[`-H`](#H)

显示与每个进程关联的所有线程。

[`-h`](#h)

尽可能频繁地重复信息标题，以保证每页信息有一个标题。

[`-j`](#j)

打印与以下关键字相关的信息： `user 、 pid 、 ppid 、 pgid 、 sid 、 jobc 、 state 、 tt 、 time` 和 `command` 。

[`-J`](#J)

显示有关与指定 jail  ID 匹配的进程的信息。 这可能是 jail 的 `jid` 或 `name` 。 使用 `-J` **0** 仅显示主机进程。默认情况下，此标志暗示 `-x` 。

[`-L`](#L)

列出可用于 `-O` 和 `-o` 选项的一组关键字。

[`-l`](#l)

显示与以下关键字相关的信息： `uid 、 pid 、 ppid 、 cpu 、 pri 、 nice 、 vsz 、 rss 、 mwchan 、 state 、` `tt 、 time` 和 `command` 。

[`-M`](#M)

从指定的核心而不是当前运行的系统中提取与名称列表关联的值。

[`-m`](#m)

按内存使用情况排序，而不是控制终端和进程 ID 的组合。

[`-N`](#N)

从指定系统中提取名称列表，而不是从默认系统中引导的内核映像。

[`-O`](#O)

在默认信息显示中，在进程 ID 之后添加与指定的空格或逗号分隔的关键字列表相关的信息。 关键字可以附加等号 (‘`=`’) 和字符串。 这会导致打印的标题使用指定的字符串而不是标准标题。

[`-o`](#o)

显示与指定的空格或逗号分隔的关键字列表相关的信息。 列表中的最后一个关键字可以附加一个等号 (‘`=`’) 和一个跨越参数其余部分的字符串，并且可以包含空格和逗号字符。 这会导致打印的标题使用指定的字符串而不是标准标题。 多个关键字也可以以多个 `-o` 选项的形式给出。 因此可以更改多个关键字的标题文本。 如果所有关键字的标题文本为空，则不写入标题行。

[`-p`](#p)

显示有关与指定进程 ID 匹配的进程的信息。

[`-r`](#r)

按当前 CPU 使用率排序，而不是控制终端和进程 ID 的组合。

[`-S`](#S)

更改进程时间的方式，即 cputime、systime 和 usertime，通过将所有退出的子进程与其父进程相加来计算。

[`-T`](#T)

显示有关连接到与标准输入关联的设备的进程的信息。

[`-t`](#t)

显示附加到指定终端设备的进程信息。 可以指定完整的路径名以及缩写（参见 `tt` 关键字的解释）。

[`-U`](#U)

显示属于指定用户名的进程。

[`-u`](#u)

显示与以下关键字相关的信息： `user 、 pid 、 %cpu 、 %mem 、 vsz 、 rss 、 tt 、 state 、 start 、 time` 和 `command` 。 `-u` 选项意味着 `-r` 选项。

[`-v`](#v)

显示与以下关键字相关的信息： `pid 、 state 、 time 、 sl 、 re 、 pagein 、 vsz 、 rss 、 lim 、 tsiz 、` `%cpu 、 %mem` 和 `command` 。 `-v` 选项意味着 `-m` 选项。

[`-w`](#w)

如果 `ps` 与终端相关联，则使用至少 132 列来显示信息，而不是默认的窗口大小。 如果多次指定 `-w` 选项， `ps` 将根据需要使用尽可能多的列，而不考虑窗口大小。 请注意，如果 “command” 列不是显示的最后一列，则此选项无效。

[`-X`](#X)

显示与其他选项匹配的进程时，跳过任何没有控制终端的进程。这是默认行为。

[`-x`](#x)

显示与其他选项匹配的进程时，包括没有控制终端的进程。 这与 `-X` 选项相反。 如果在同一命令中同时指定了 `-X` 和 `-x` ，则 `ps` 将使用最后指定的那个。

[`-Z`](#Z)

将 mac(4) 标签添加到 `ps` 将显示信息的关键字列表中。

下面列出了可用关键字的完整列表。其中一些关键字进一步指定如下：

[`%cpu`](#_cpu)

进程的CPU利用率；这是之前（实际）时间最多一分钟的衰减平均值。 由于计算它的时间基数不同（因为进程可能非常年轻），所有 `%cpu` 字段的总和可能超过 100%。

[`%mem`](#_mem)

此进程使用的实际内存百分比。

[`class`](#class)

与进程关联的登录类。

[`flags`](#flags)

与包含文件 `<sys/proc.h>` 中的进程关联的标志：

[`P_ADVLOCK`](#P_ADVLOCK)

[0x00001](#0x00001)

进程可能持有 POSIX 咨询锁

[`P_CONTROLT`](#P_CONTROLT)

[0x00002](#0x00002)

有控制终端

[`P_KPROC`](#P_KPROC)

[0x00004](#0x00004)

内核进程

[`P_PPWAIT`](#P_PPWAIT)

[0x00010](#0x00010)

父母正在等待孩子执行/退出

[`P_PROFIL`](#P_PROFIL)

[0x00020](#0x00020)

已开始分析

[`P_STOPPROF`](#P_STOPPROF)

[0x00040](#0x00040)

有线程请求停止教授

[`P_HADTHREADS`](#P_HADTHREADS)

[0x00080](#0x00080)

有线程（没有清理快捷方式）

[`P_SUGID`](#P_SUGID)

[0x00100](#0x00100)

自上次执行以来已设置 id 权限

[`P_SYSTEM`](#P_SYSTEM)

[0x00200](#0x00200)

系统进程：没有 sigs、stats 或 swapping

[`P_SINGLE_EXIT`](#P_SINGLE_EXIT)

[0x00400](#0x00400)

挂起的线程应该退出，而不是等待

[`P_TRACED`](#P_TRACED)

[0x00800](#0x00800)

被调试的进程被跟踪

[`P_WAITED`](#P_WAITED)

[0x01000](#0x01000)

有人在等我们

[`P_WEXIT`](#P_WEXIT)

[0x02000](#0x02000)

正在退出

[`P_EXEC`](#P_EXEC)

[0x04000](#0x04000)

进程调用 exec

[`P_WKILLED`](#P_WKILLED)

[0x08000](#0x08000)

已终止，应尽快进入内核/用户边界

[`P_CONTINUED`](#P_CONTINUED)

[0x10000](#0x10000)

Proc 从停止状态继续

[`P_STOPPED_SIG`](#P_STOPPED_SIG)

[0x20000](#0x20000)

由于 SIGSTOP/SIGTSTP 而停止

[`P_STOPPED_TRACE`](#P_STOPPED_TRACE)

[0x40000](#0x40000)

由于跟踪而停止

[`P_STOPPED_SINGLE`](#P_STOPPED_SINGLE)

[0x80000](#0x80000)

只有一个线程可以继续

[`P_PROTECTED`](#P_PROTECTED)

[0x100000](#0x100000)

不要在内存过量使用时终止

[`P_SIGEVENT`](#P_SIGEVENT)

[0x200000](#0x200000)

处理未决信号已更改

[`P_SINGLE_BOUNDARY`](#P_SINGLE_BOUNDARY)

[0x400000](#0x400000)

线程应该在用户边界挂起

[`P_HWPMC`](#P_HWPMC)

[0x800000](#0x800000)

进程正在使用 HWPMC

[`P_JAILED`](#P_JAILED)

[0x1000000](#0x1000000)

进程在 jail 中

[`P_TOTAL_STOP`](#P_TOTAL_STOP)

[0x2000000](#0x2000000)

因系统挂起而停止

[`P_INEXEC`](#P_INEXEC)

[0x4000000](#0x4000000)

进程在 execve(2)

[`P_STATCHILD`](#P_STATCHILD)

[0x8000000](#0x8000000)

子进程停止或退出

[`P_INMEM`](#P_INMEM)

[0x10000000](#0x10000000)

加载到内存中

[`P_SWAPPINGOUT`](#P_SWAPPINGOUT)

[0x20000000](#0x20000000)

进程正在被换出

[`P_SWAPPINGIN`](#P_SWAPPINGIN)

[0x40000000](#0x40000000)

进程正在被换入

[`P_PPTRACE`](#P_PPTRACE)

[0x80000000](#0x80000000)

Vforked child 发出 ptrace(PT\_TRACEME)

[`flags2`](#flags2)

保存在 p\_flag2 中的标志与包含文件 `<sys/proc.h>` 中的进程相关联：

[`P2_INHERIT_PROTECTED`](#P2_INHERIT_PROTECTED)

[0x00000001](#0x00000001)

新孩子获得 P\_PROTECTED

[`P2_NOTRACE`](#P2_NOTRACE)

[0x00000002](#0x00000002)

没有 ptrace(2) 附加或核心转储

[`P2_NOTRACE_EXEC`](#P2_NOTRACE_EXEC)

[0x00000004](#0x00000004)

将 P2\_NOPTRACE 保持在 execve(2)

[`P2_AST_SU`](#P2_AST_SU)

[0x00000008](#0x00000008)

处理 kthread 的 SU ast

[`P2_PTRACE_FSTP`](#P2_PTRACE_FSTP)

[0x00000010](#0x00000010)

来自 PT\_ATTACH 的 SIGSTOP 尚未处理

[`label`](#label)

进程的 MAC 标签。

[`lim`](#lim)

使用的内存的软限制，通过调用 setrlimit(2) 指定。

[`lstart`](#lstart)

命令开始的确切时间，使用 strftime(3) 中描述的 ‘`%c`’ 格式。

[`lockname`](#lockname)

进程当前被阻塞的锁的名称。 如果名称无效或未知，则 “???” 被陈列。

[`logname`](#logname)

与进程所在的会话关联的登录名（请参阅 getlogin(2) ）。

[`mwchan`](#mwchan)

如果进程被正常阻塞，则为事件名称，如果进程被锁阻塞，则为锁名称。 有关详细信息，请参阅 wchan 和 lockname 关键字。

[`nice`](#nice)

进程调度增量（请参阅 setpriority(2) ）。

[`rss`](#rss)

进程的实际内存（驻留集）大小（以 1024 字节为单位）。

[`start`](#start)

命令开始的时间。 如果命令在 24 小时前开始，则使用 strftime(3) 中描述的 “`%H:%M`” 格式显示开始时间。 如果命令在不到 7 天前开始，则使用 “`%a%H`” 格式显示开始时间。 否则，开始时间以 “`%e%b%y`” 格式显示。

[`state`](#state)

状态由一系列字符给出，例如 “`RWNA`” 。第一个字符表示进程的运行状态：

[`D`](#D)

标记一个进程在磁盘（或其他短期、不间断）等待。

[`I`](#I)

标记一个空闲的进程（睡眠时间超过大约 20 秒）。

[`L`](#L_2)

标记正在等待获取锁的进程。

[`R`](#R)

标记一个可运行的进程。

[`S`](#S_2)

标记睡眠时间少于 20 秒的进程。

[`T`](#T_2)

标记一个停止的进程。

[`W`](#W)

标记一个空闲的中断线程。

[`Z`](#Z_2)

标记一个死进程（一个 “zombie” ）。

这些后面的附加字符（如果有）表示附加状态信息：

[`+`](#+)

该进程位于其控制终端的前台进程组中。

[`<`](#_)

该进程已提高 CPU 调度优先级。

[`C`](#C_2)

该过程处于 capsicum(4) 能力模式。

[`E`](#E)

该进程正在尝试退出。

[`J`](#J_2)

标记处于 jail(2) 中的进程。 jail 的主机名可以在 /proc/⟨pid⟩/status 中找到。

[`L`](#L_3)

该进程将页面锁定在核心中（例如，用于原始 I/O）。

[`N`](#N_2)

该进程降低了 CPU 调度优先级（请参阅 setpriority(2) ）。

[`s`](#s)

该进程是会话领导者。

[`V`](#V)

进程的父进程在 vfork(2) 期间挂起，等待进程执行或退出。

[`W`](#W_2)

进程被换出。

[`X`](#X_2)

正在跟踪或调试进程。

[`tt`](#tt)

控制终端的路径名的缩写，如果有的话。 缩写由 /dev/tty 后面的三个字母组成，或者，对于伪终端，是 /dev/pts 中的相应条目。 如果进程不能再到达该控制终端（即，它已被撤销），则后面跟着一个 ‘`-`’ 。 前面没有两个字母缩写或伪终端设备号的 ‘`-`’ 表示一个从未有控制终端的进程。 控制终端的完整路径名可通过 `tty` 关键字获得。

[`wchan`](#wchan)

进程等待的事件（系统中的地址）。 当以数字方式打印时，地址的初始部分被剪掉，结果以十六进制打印，例如，0x80324000 打印为 324000。

使用 command 关键字打印时，已退出且其父进程尚未等待的进程（换句话说，僵尸进程）被列为 “`<defunct>`” ，并且在尝试执行时被阻塞的进程退出被列为 “`<exiting>`” 。 如果无法找到参数（通常是因为它尚未设置，如系统进程和/或内核线程的情况），则命令名称将打印在方括号内。 `ps` 实用程序首先尝试获取内核缓存的参数（如果它们短于 kern.ps\_arg\_cache\_limit 的值）。 该过程可以更改 setproctitle(3) 显示的参数。 否则， `ps` 通过检查内存或交换区域对创建进程时给出的文件名和参数进行有根据的猜测。 该方法本质上有些不可靠，并且在任何情况下，进程都有权销毁此信息。 但是，可以依赖 ucomm（会计）关键字。 如果参数不可用或与 ucomm 关键字不一致，则将 ucomm 关键字的值附加到括号中的参数。

[关键字](#__u5173___u952E___u5B57_)
================================

以下是可用关键字及其含义的完整列表。 其中一些有别名（关键字是同义词）。

[`%cpu`](#_cpu_2)

CPU 使用百分比（别名 `pcpu`)

[`%mem`](#_mem_2)

内存使用百分比（别名 `pmem`)

[`acflag`](#acflag)

记帐标志（别名 `acflg`)

[`args`](#args)

命令和参数

[`class`](#class_2)

登录类

[`comm`](#comm)

命令

[`command`](#command)

命令和参数

[`cow`](#cow)

写时复制错误数

[`cpu`](#cpu)

正在执行进程的处理器编号（仅在 SMP 系统上可见）。

[`dsiz`](#dsiz)

数据大小（以千字节为单位）

[`emul`](#emul)

系统调用仿真环境 (ABI)

[`etime`](#etime)

运行时间，格式 “\[days-\]\[hours:\]minutes:seconds”

[`etimes`](#etimes)

运行时间，十进制整数秒

[`fib`](#fib)

默认 FIB 编号，参见 setfib(1)

[`flags`](#flags_2)

进程标志，十六进制（别名 `f`)

[`flags2`](#flags2_2)

额外的一组进程标志，以十六进制表示（别名 `f2`)

[`gid`](#gid)

有效组 ID（别名 `egid`)

[`group`](#group)

组名（来自 egid）（别名 `egroup`)

[`inblk`](#inblk)

读取的总块数（别名 `inblock`)

[`jail`](#jail)

jail 名称

[`jid`](#jid)

jail ID

[`jobc`](#jobc)

job 控制计数

[`ktrace`](#ktrace)

跟踪标志

[`label`](#label_2)

MAC 标签

[`lim`](#lim_2)

内存使用限制

[`lockname`](#lockname_2)

当前锁定的锁定（作为符号名称）

[`logname`](#logname_2)

开始会话的用户的登录名

[`lstart`](#lstart_2)

时间开始

[`lwp`](#lwp)

线程（轻量级进程）ID（别名 `tid`)

[`majflt`](#majflt)

总页错误

[`minflt`](#minflt)

总页面回收

[`msgrcv`](#msgrcv)

收到的消息总数（从管道/套接字读取）

[`msgsnd`](#msgsnd)

发送的消息总数（写入管道/套接字）

[`mwchan`](#mwchan_2)

等待当前阻塞的通道或锁

[`nice`](#nice_2)

不错的价值（别名 `ni`)

[`nivcsw`](#nivcsw)

总非自愿上下文切换

[`nlwp`](#nlwp)

绑定到进程的线程数（轻量级进程）

[`nsigs`](#nsigs)

接收的总信号（别名 `nsignals`)

[`nswap`](#nswap)

总换入/换出

[`nvcsw`](#nvcsw)

总自愿上下文切换

[`nwchan`](#nwchan)

等待通道（作为地址）

[`oublk`](#oublk)

写入的总块数（别名 `oublock`)

[`paddr`](#paddr)

进程指针

[`pagein`](#pagein)

pageins（与 majflt 相同）

[`pgid`](#pgid)

进程组号

[`pid`](#pid)

进程号

[`ppid`](#ppid)

父进程号

[`pri`](#pri)

调度优先级

[`re`](#re)

核心驻留时间（以秒为单位；127 = 无穷大）

[`rgid`](#rgid)

真实组ID

[`rgroup`](#rgroup)

组名（来自 rgid）

[`rss`](#rss_2)

驻留集大小

[`rtprio`](#rtprio)

实时优先级（参见 rtprio(1))

[`ruid`](#ruid)

真实用户ID

[`ruser`](#ruser)

用户名（来自 ruid）

[`sid`](#sid)

会话 ID

[`sig`](#sig)

待处理信号（别名 `pending`)

[`sigcatch`](#sigcatch)

捕获的信号（别名 `caught`)

[`sigignore`](#sigignore)

被忽略的信号（别名 `ignored`)

[`sigmask`](#sigmask)

阻塞信号（别名 `blocked`)

[`sl`](#sl)

睡眠时间（以秒为单位；127 = 无穷大）

[`ssiz`](#ssiz)

堆栈大小（以千字节为单位）

[`start`](#start_2)

时间开始

[`state`](#state_2)

符号进程状态（别名 `stat`)

[`svgid`](#svgid)

从 setgid 可执行文件保存 gid

[`svuid`](#svuid)

从 setuid 可执行文件中保存的 UID

[`systime`](#systime)

累计系统CPU时间

[`tdaddr`](#tdaddr)

线程地址

[`tdname`](#tdname)

线程名称

[`tdev`](#tdev)

控制终端设备号

[`time`](#time)

累计 CPU 时间，用户 + 系统（别名 `cputime`)

[`tpgid`](#tpgid)

控制终端进程组ID

[`tracer`](#tracer)

跟踪器进程 ID

[`tsid`](#tsid)

控制终端会话 ID

[`tsiz`](#tsiz)

文本大小（以千字节为单位）

[`tt`](#tt_2)

控制终端名称（两个字母缩写）

[`tty`](#tty)

控制终端全称

[`ucomm`](#ucomm)

用于会计的名称

[`uid`](#uid)

有效用户 ID（别名 `euid`)

[`upr`](#upr)

从系统调用返回时调度优先级（别名 `usrpri`)

[`uprocp`](#uprocp)

进程指针

[`user`](#user)

用户名（来自 UID）

[`usertime`](#usertime)

累计用户 CPU 时间

[`vmaddr`](#vmaddr)

虚拟机空间指针

[`vsz`](#vsz)

以千字节为单位的虚拟大小（别名 `vsize`)

[`wchan`](#wchan_2)

等待通道（作为符号名称）

[`xstat`](#xstat)

退出或停止状态（仅对停止或僵尸进程有效）

注意，当没有指定 `-H` 选项时， `pending` 列显示进程队列中挂起的信号的位掩码，否则显示每个线程的挂起信号队列。

[环境](#__u73AF___u5883_)
=======================

以下环境变量影响 `ps` 的执行：

[`COLUMNS`](#COLUMNS)

如果设置，则指定用户在列位置中的首选输出宽度。 默认情况下， `ps` 尝试自动确定终端宽度。

[文件](#__u6587___u4EF6_)
=======================

/boot/kernel/kernel

默认系统名单

[退出状态](#__u9000___u51FA___u72B6___u6001_)
=========================================

The `ps` utility exits 0 on success, and >0 if an error occurs.

[实例](#__u5B9E___u4F8B_)
=======================

显示所有系统进程的信息：

`$ ps -auxw`

[参见](#__u53C2___u89C1_)
=======================

kill(1) 、 pgrep(1) 、 pkill(1) 、 procstat(1) 、 w(1) 、 kvm(3) 、 libxo(3) 、 strftime(3) 、 xo\_parse\_args(3) 、 mac(4) 、 procfs(5) 、 pstat(8) 、 sysctl(8) 、 mutex(9)

[标准](#__u6807___u51C6_)
=======================

由于历史原因， FreeBSD 下的 `ps` 实用程序支持一组与 IEEE Std 1003.2 (“POSIX.2”) 所描述的选项不同的选项，以及非 non-BSD 操作系统所支持的选项。

[历史](#__u5386___u53F2_)
=======================

`ps` 命令出现在 Version 3 AT&T UNIX 手册的第 8 节中。

[缺陷](#__u7F3A___u9677_)
=======================

由于 `ps` 无法比系统运行得更快，并且与任何其他计划进程一样运行，因此它显示的信息永远不会准确。

`ps` 实用程序无法正确显示包含多字节字符的参数列表。

June 27, 2020

FreeBSD 13.1-RELEASE