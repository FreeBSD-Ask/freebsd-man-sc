  PMCSTAT(8)  

PMCSTAT(8)

FreeBSD System Manager's Manual

PMCSTAT(8)

[名称](#__u540D___u79F0_)
=======================

`pmcstat` —

使用性能监控硬件进行性能测量

[概要](#__u6982___u8981_)
=======================

`pmcstat` \[`-A`\] \[`-C`\] \[`-D` pathname\] \[`-E`\] \[`-F` pathname\] \[`-G` pathname\] \[`-I`\] \[`-L`\] \[`-M` mapfilename\] \[`-N`\] \[`-O` logfilename\] \[`-P` event-spec\] \[`-R` logfilename\] \[`-S` event-spec\] \[`-T`\] \[`-U`\] \[`-W`\] \[`-a` pathname\] \[`-c` cpu-spec\] \[`-d`\] \[`-e`\] \[`-f` pluginopt\] \[`-g`\] \[`-i` lwp\] \[`-k` kerneldir\] \[`-l` secs\] \[`-m` pathname\] \[`-n` rate\] \[`-o` outputfile\] \[`-p` event-spec\] \[`-q`\] \[`-r` fsroot\] \[`-s` event-spec\] \[`-t` process-spec\] \[`-u` event-spec\] \[`-v`\] \[`-w` secs\] \[`-z` graphdepth\] \[command \[args\]\]

[描述](#__u63CF___u8FF0_)
=======================

`pmcstat` 实用程序使用 hwpmc(4) 提供的工具测量系统性能。

`pmcstat` 实用程序可以测量整个系统看到的硬件事件，以及在系统 CPU 上执行指定的一组进程时看到的硬件事件。 如果以特定进程集为目标（例如，如果指定了 `-t` process-spec 选项，或者如果使用 command 指定了命令行），则测量会一直进行，直到 command 退出，或者直到由 `-t` process-spec 选项退出，或直到 `pmcstat` 实用程序被用户中断。 如果一组特定的进程不是测量的目标，那么 `pmcstat` 将执行系统范围的测量，直到被用户中断。

对 `pmcstat` 的给定调用可以混合分配系统模式和进程模式 PMC，包括计数和采样风格。 `pmcstat` 定期以人类可读的形式打印所有计数 PMC 的值。 采样 PMC 的输出可以配置为进入日志文件以进行后续离线分析，或者以更大的开销为代价，可以配置为以文本形式即时打印。

使用事件说明符字符串 event-spec 将要测量的硬件事件指定给 `pmcstat` 。 这些事件说明符的语法取决于机器，并记录在 pmc(3) 中。

进程模式 PMC 可以配置为可由目标进程的当前和未来子进程继承。

[选项](#__u9009___u9879_)
=======================

可以使用以下选项：

[`-A`](#A)

跳过符号查找并改为显示地址

[`-C`](#C)

在显示命令行上指定的后续计数模式 PMC 的累积或增量计数之间切换。 默认是显示增量计数。

[`-D`](#D) pathname

在 pathname 命名的目录中创建包含每个程序示例的文件。 默认是在当前目录中创建这些文件。

[`-E`](#E)

在命令行上指定的后续进程模式 PMC 的跟踪进程退出时切换显示每个进程的计数。 当与 `-d` 选项结合使用时，此选项对于映射复杂流程管道的性能特征非常有用。 默认是不启用每进程跟踪。

[`-F`](#F) pathname

将调用树 (Kcachegrind) 信息打印到文件 pathname 。 如果参数 pathname 是 “`-`” ，则此信息将发送到 `-o` 选项指定的输出文件。

[`-G`](#G) pathname

将调用链信息打印到文件 pathname 。 如果参数 pathname 是 “`-`” ，则此信息将发送到 `-o` 选项指定的输出文件。

[`-I`](#I)

显示指令指针在符号中的偏移量。

[`-L`](#L)

列出所有事件名称。

[`-M`](#M) mapfilename

将事件日志中遇到的可执行对象与用于 gprof(1) 配置文件的缩写路径名之间的映射写入文件 mapfilename 。 如果未指定此选项，则不写入映射信息。 参数 mapfilename 可以是 “`-`” ，在这种情况下，此映射信息将发送到 `-o` 选项配置的输出文件。

[`-N`](#N)

切换为后续采样 PMC 捕获调用链信息。 默认是对 PMC 进行采样以捕获调用链信息。

[`-O`](#O) logfilename

将日志输出发送到文件 logfilename 。 如果 logfilename 的格式为 hostname:port, 其中 hostname 不以 ‘`.`’ 开头 或 ‘`/`’, 然后 `pmcstat` 将打开一个网络套接字以在端口 port 上托管 hostname 。

如果未指定 `-O` 选项并且请求了其中一个日志记录选项，则 `pmcstat` 会将已记录事件的文本形式打印到配置的输出文件中。

[`-P`](#P) event-spec

分配一个过程模式采样 PMC 测量 event-spec 中指定的硬件事件。

[`-R`](#R) logfilename

使用文件 logfilename 中的采样数据执行离线分析。

[`-S`](#S) event-spec

分配系统模式采样 PMC 测量 event-spec 中指定的硬件事件。

[`-T`](#T)

使用类似 top(1) 的模式对 PMC 进行采样。可以使用以下热键：

[`A`](#A_2)

切换符号分辨率

[`Ctrl+a`](#Ctrl_+_a)

切换到累积模式

[`Ctrl+d`](#Ctrl_+_d)

切换到增量模式

[`f`](#f)

将阈值下的 “f” 成本表示为一个点（仅限调用树）

[`I`](#I_2)

切换显示符号的偏移量

[`m`](#m)

合并 PMC

[`n`](#n)

更改视图

[`p`](#p)

显示下一个 PMC

[`q`](#q)

退出

[`Space`](#Space)

暂停

[`-U`](#U)

在内核模式下切换捕获用户空间调用跟踪。 默认情况下，采样 PMC 在用户空间模式下捕获用户空间调用链信息，在内核模式下捕获内核调用链信息。

[`-W`](#W)

切换记录被跟踪进程的线程每次在 CPU 上调度时看到的增量计数。 这是一项实验性功能，旨在帮助分析系统中进程的动态行为。 如果启用，它可能会产生大量开销。 默认情况下禁用此功能。

[`-a`](#a) pathname

对每个调用图中的每个地址执行符号和文件：行查找并将输出保存到 pathname 。 与 `-m` 仅解析图中的第一个符号不同，这会解析调用图中的每个节点，或者如果没有可用的查找信息则打印出地址。 此选项需要 `-R` 选项才能读入先前使用 `-O` 选项收集和保存的样本。

[`-c`](#c) cpu-spec

将命令行中指定的后续系统模式 PMC 的 cpu 设置为 cpu-spec 。参数 cpu-spec 是一个逗号分隔的 CPU 编号列表，或文字 ‘\*’ 表示所有可用的 CPU。 默认是在所有可用 CPU 上分配系统模式 PMC。

[`-d`](#d)

在进程模式 PMC 之间切换，该 PMC 测量目标进程当前和未来子进程的事件，或者仅测量目标进程的事件。 默认是单独测量目标进程的事件。 （它必须在 `-p`, `-s`, `-P` 或 `-S` 之前在命令行中传递）。

[`-e`](#e)

指定 gprof 配置文件将使用宽历史计数器。 这些文件以与 gprof(1) 兼容的格式生成。 但是，其他无法完全解析 BSD 样式的 gmon 标头的工具可能无法正确解析这些文件。

[`-f`](#f_2) pluginopt

将选项字符串传递给活动插件。-
threshold=<float> 不显示低于指定值的成本（顶部）。-
skiplink=0|1 用一个点（顶部）替换成本低于阈值的节点。

[`-g`](#g)

以与 gprof(1) 兼容的格式生成配置文件。 为遇到的每个可执行对象生成一个单独的配置文件。 配置文件放置在以其 PMC 事件名称命名的子目录中。

[`-i`](#i) lwp

过滤线程 ID lwp, 可以从 ps(1) `-o` `lwp` 获得。

[`-k`](#k) kerneldir

将内核目录的路径名设置为参数 kerneldir 。 此目录指定 `pmcstat` 应在何处查找内核及其模块。 默认是使用从 kern.bootfile 获得的运行内核的路径。 如果在 kerneldir 中找不到模块，也会在 /boot/modules 中搜索模块。

[`-l`](#l) secs

将系统范围的性能测量持续时间设置为 secs 秒。 参数 secs 可以是小数值。

[`-m`](#m_2) pathname

打印采样 PC 的名称、函数的起始地址和结束地址。 pathname 参数是必需的，它指示信息将存储在哪里。 如果 pathname 是 “`-`” ，则此信息将发送到 `-o` 选项指定的输出文件。 此选项需要 `-R` 选项才能读入先前使用 `-O` 选项收集和保存的样本。

[`-n`](#n_2) rate

为命令行指定的后续采样模式 PMC 设置默认采样率。 默认配置 PMC 以每 65536 个事件对 CPU 的指令指针进行采样。

[`-o`](#o) outputfile

将记录数据的计数器读数和文本表示发送到文件 outputfile 。 默认设置是在收集实时数据时将输出发送到 stderr ，在处理预先存在的日志文件时将输出发送到 stdout 。

[`-p`](#p_2) event-spec

分配一个过程模式计数 PMC 测量在 event-spec 中指定的硬件事件。

[`-q`](#q_2)

减少冗长。

[`-r`](#r) fsroot

将可执行文件所在的文件系统层次结构的顶部设置为参数 fsroot 。默认为 / 。

[`-s`](#s) event-spec

分配一个系统模式计数 PMC 测量在 event-spec 中指定的硬件事件。

[`-t`](#t) process-spec

将进程模式 PMC 附加到由参数 process-spec 命名的进程。 参数 process-spec 可以是表示特定进程 id 的非负整数，也可以是用于根据命令名称选择进程的正则表达式。

[`-u`](#u) event-spec

提供事件的简短描述。

[`-v`](#v)

增加详细程度。

[`-w`](#w) secs

每隔 secs 秒打印所有计数模式 PMC 或顶部模式的采样模式 PMC 的值。 参数 secs 可以是小数值。 默认间隔为 5 秒。

[`-z`](#z) graphdepth

打印系统范围的调用图时，将调用图限制为参数 graphdepth 指定的深度。

如果指定了 command ，则使用 execvp(3) 执行。

[实例](#__u5B9E___u4F8B_)
=======================

要在 AMD Athlon CPU 上执行系统范围的统计采样，每执行 32768 条指令后进行一次采样，并将数据采样到文件 sample.stat ，请使用：

`pmcstat -O sample.stat -n 32768 -S k7-retired-instructions`

要在 AMD Athlon 上每 12 秒执行一次 `firefox` 并测量其及其子代遭受的数据缓存未命中次数，请使用：

`pmcstat -d -w 12 -p k7-dc-misses firefox`

要测量所有名为 “emacs” 的进程退出的指令，请使用：

`pmcstat -t '^emacs$' -p instructions`

要测量名为 “emacs” 的进程停用 10 秒的指令，请使用：

`pmcstat -t '^emacs$' -p instructions sleep 10`

要计算 Intel Pentium Pro/Pentium III SMP 系统上 CPU 0 和 2 上的指令 tlb-misses，请使用：

`pmcstat -c 0,2 -s p6-itlb-miss`

要根据 pid 1234 看到的指令缓存未命中来收集特定进程的分析信息，请使用：

`pmcstat -P ic-misses -t 1234 -O /tmp/sample.out`

要根据已停用的处理器指令对所有已配置的处理器执行系统范围的采样，请使用：

`pmcstat -S instructions -O /tmp/sample.out`

如果不需要调用图捕获，请使用：

`pmcstat -N -S instructions -O /tmp/sample.out`

要将生成的事件日志发送到远程机器，请使用：

`pmcstat -S instructions -O remotehost:port`

在远程机器上，可以使用 nc(1) 收集示例日志：

`nc -l remotehost port > /tmp/sample.out`

要从示例文件生成 gprof(1) 兼容配置文件，请使用：

`pmcstat -R /tmp/sample.out -g`

要使用调用图将系统范围的配置文件打印到文件 foo.graph ，请使用：

`pmcstat -R /tmp/sample.out -G foo.graph`

[诊断](#__u8BCA___u65AD_)
=======================

如果指定了选项 `-v` ， `pmcstat` 可能会发出以下诊断消息：

#callchain/dubious-frames

返回地址具有 “impossible” 值的调用链记录数。

#exec handling errors

日志文件中命名为无法分析的可执行文件的 exec(2) 事件数。

#exec/elf

命名为 ELF 可执行文件的 exec(2) 事件数。

#exec/unknown

使用无法识别的格式命名可执行文件的 exec(2) 事件数。

#samples/total

日志文件中的样本总数。

#samples/unclaimed

无法与已知可执行对象（即可执行文件、共享库、内核或运行时加载程序）相关联的样本数。

#samples/unknown-object

与具有无法识别的对象格式的可执行文件关联的样本数。

-
The `pmcstat` utility exits 0 on success, and >0 if an error occurs.

[兼容性](#__u517C___u5BB9___u6027_)
================================

由于 gmon.out 文件格式的限制，由 `-g` 选项生成的 gprof(1) 兼容配置文件不包含有关跨越可执行边界的调用的信息。 生成的 gmon.out 文件也只对本机可执行文件有意义。

[参见](#__u53C2___u89C1_)
=======================

gprof(1), nc(1), execvp(3), pmc(3), pmclog(3), hwpmc(4), pmccontrol(8), sysctl(8)

[历史](#__u5386___u53F2_)
=======================

`pmcstat` 实用程序首先出现在 FreeBSD 6.0 中。它目前正在开发中。 currently under development.

[作者](#__u4F5C___u8005_)
=======================

Joseph Koshy <[jkoshy@FreeBSD.org](mailto:jkoshy@FreeBSD.org)\>

[缺陷](#__u7F3A___u9677_)
=======================

`pmcstat` 实用程序还不能分析由非本地架构生成的 hwpmc(4) 日志。

August 17, 2020

FreeBSD 13.1-RELEASE