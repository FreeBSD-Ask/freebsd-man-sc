# pmcstat(8)

`pmcstat` — 使用性能监控硬件进行性能测量

## 名称

`pmcstat`

## 概要

`pmcstat [-A] [-C] [-D pathname] [-E] [-F pathname] [-G pathname] [-I] [-L] [-M mapfilename] [-N] [-O logfilename] [-P event-spec] [-R logfilename] [-S event-spec] [-T] [-U] [-W] [-a pathname] [-c cpu-spec] [-d] [-e] [-f pluginopt] [-g] [-i lwp] [-l secs] [-m pathname] [-n rate] [-o outputfile] [-p event-spec] [-q] [-r fsroot] [-s event-spec] [-t process-spec] [-u event-spec] [-v] [-w secs] [-z graphdepth] [command [args]]`

## 描述

`pmcstat` 工具使用 [hwpmc(4)](../man4/hwpmc.4.md) 提供的功能来测量系统性能。

`pmcstat` 工具既可以测量系统整体所看到的硬件事件，也可以测量指定进程集合在系统 CPU 上执行时所看到的事件。如果针对特定的进程集合进行测量（例如指定了 `-t` `process-spec` 选项，或使用 `command` 指定了命令行），则测量将持续到 `command` 退出，或所有由 `-t` `process-spec` 选项指定的目标进程退出，或 `pmcstat` 工具被用户中断。如果未针对特定的进程集合进行测量，`pmcstat` 将进行系统范围的测量，直到被用户中断。

给定的一次 `pmcstat` 调用可以混合分配系统模式和进程模式的 PMC，包括计数和采样两种类型。所有计数 PMC 的值会以人类可读的形式定期打印。`pmcstat` 的人类可读文本输出格式并不稳定，将来可能发生变化。采样 PMC 的输出可以配置为发送到日志文件以供后续离线分析，或者以更高的开销配置为即时以文本形式打印。

要测量的硬件事件通过事件说明符字符串 `event-spec` 指定给 `pmcstat`。这些事件说明符的语法与机器相关，详见 pmc(3)。

进程模式 PMC 可以配置为由目标进程的当前和未来子进程继承。

## 选项

可用选项如下：

**`-A`** 跳过符号查找，改为显示地址。

**`-C`** 在为命令行上后续指定的计数模式 PMC 显示累积计数或增量计数之间切换。默认为显示增量计数。

**`-D`** `pathname` 在由 `pathname` 命名的目录中创建包含各程序采样的文件。默认在当前目录中创建这些文件。

**`-E`** 在为命令行上后续指定的进程模式 PMC 跟踪的进程退出时，切换显示每个进程的计数。此选项与 `-d` 选项结合使用时，对于映射复杂进程管道的性能特征很有用。默认不启用每进程跟踪。

**`-F`** `pathname` 将调用树（Kcachegrind）信息打印到文件 `pathname`。如果参数 `pathname` 为“`-`”，此信息将发送到由 `-o` 选项指定的输出文件。

**`-G`** `pathname` 将调用链信息打印到文件 `pathname`。如果参数 `pathname` 为“`-`”，此信息将发送到由 `-o` 选项指定的输出文件。

**`-I`** 显示指令指针在符号中的偏移量。

**`-L`** 列出所有事件名称。

**`-M`** `mapfilename` 将事件日志中遇到的可执行对象与 gprof(1) 配置文件所使用的缩写路径名之间的映射写入文件 `mapfilename`。如果未指定此选项，则不写入映射信息。参数 `mapfilename` 可以为“`-`”，此时此映射信息将发送到由 `-o` 选项配置的输出文件。

**`-N`** 为后续的采样 PMC 切换是否捕获调用链信息。默认情况下，采样 PMC 会捕获调用链信息。

**`-O`** `logfilename` 将日志输出发送到文件 `logfilename`。如果 `logfilename` 的形式为 `hostname`:`port`，其中 `hostname` 不以 `.` 或 `/` 开头，则 `pmcstat` 将打开到主机 `hostname` 的 `port` 端口的网络套接字。如果未指定 `-O` 选项但请求了某个日志记录选项，`pmcstat` 会将日志事件的文本形式打印到配置的输出文件。

**`-P`** `event-spec` 分配一个进程模式采样 PMC，测量 `event-spec` 中指定的硬件事件。

**`-R`** `logfilename` 使用文件 `logfilename` 中的采样数据进行离线分析。每条解码记录打印为单行，包含以下字段：记录类型（例如“callchain”、“initlog”）、类型特定数据，以及一个尾部的 20 位原始 TSC 值，记录事件发生时的 CPU 周期。“initlog”记录还会打印“`tsc_freq=<hz>`”，即内核在启动时测量的 TSC 时钟频率（以 Hz 为单位）。要将 TSC 增量转换为纳秒：

```sh
elapsed_ns = (tsc_end - tsc_start) * 1e9 / tsc_freq
```

基于 TSC 的时间戳和“`tsc_freq`”仅在 x86 架构（amd64 和 i386）上有意义。在所有其他架构（包括 arm64 和 powerpc）上，“`tsc_freq`”字段将为零。

**`-S`** `event-spec` 分配一个系统模式采样 PMC，测量 `event-spec` 中指定的硬件事件。

**`-T`** 对采样 PMC 使用类似 [top(1)](../man1/top.1.md) 的模式。可以使用以下热键：

**`A`** 切换符号解析
**`Ctrl + a`** 切换到累积模式
**`Ctrl + d`** 切换到增量模式
**`f`** 将阈值以下的“f”开销表示为点（仅调用树）
**`I`** 切换显示符号内的偏移量
**`m`** 合并 PMC
**`n`** 切换视图
**`p`** 显示下一个 PMC
**`q`** 退出
**`Space`** 暂停

**`-U`** 切换在内核模式下是否捕获用户空间调用跟踪。默认情况下，采样 PMC 在用户空间模式下捕获用户空间调用链信息，在内核模式下捕获内核调用链信息。

**`-W`** 切换是否在跟踪进程的线程每次被调度到 CPU 上时记录其看到的增量计数。这是一个实验性功能，旨在帮助分析系统中进程的动态行为。启用时可能产生大量开销。默认情况下此功能被禁用。

**`-a`** `pathname` 对每个调用图中的每个地址执行符号和 file:line 查找，并将输出保存到 `pathname`。与仅解析图中第一个符号的 `-m` 不同，此选项解析调用图中的每个节点，如果没有查找信息则打印地址。此选项需要 `-R` 选项来读取先前用 `-O` 选项收集和保存的采样。

**`-c`** `cpu-spec` 将命令行上后续指定的系统模式 PMC 的 CPU 设置为 `cpu-spec`。参数 `cpu-spec` 是以逗号分隔的 CPU 编号列表，或字面值‘*’表示所有可用 CPU。默认在所有可用 CPU 上分配系统模式 PMC。

**`-d`** 在进程模式 PMC 测量目标进程的当前和未来子进程的事件，或仅测量目标进程的事件之间切换。默认为仅测量目标进程的事件。（它必须在命令行中先于 `-p`、`-s`、`-P` 或 `-S` 传递。）

**`-e`** 指定 gprof 配置文件将使用宽历史计数器。这些文件以兼容 gprof(1) 的格式生成。但是，无法完全解析 BSD 风格 gmon 头的其他工具可能无法正确解析这些文件。

**`-f`** `pluginopt` 将选项字符串传递给活动插件。
threshold=<float> 不显示低于指定值的开销（Top）。
skiplink=0|1 将开销低于阈值的节点替换为点（Top）。

**`-g`** 以兼容 gprof(1) 的格式生成配置文件。为遇到的每个可执行对象生成单独的配置文件。配置文件放在以其 PMC 事件名称命名的子目录中。

**`-i`** `lwp` 按线程 ID `lwp` 进行过滤，可从 [ps(1)](../man1/ps.1.md) `-o` `lwp` 获取。

**`-l`** `secs` 设置系统范围性能测量的持续时间为 `secs` 秒。参数 `secs` 可以为小数值。

**`-m`** `pathname` 打印采样的 PC 及其所在函数的名称、起始和结束地址。`pathname` 参数是必需的，指示信息存储的位置。如果参数 `pathname` 为“`-`”，此信息将发送到由 `-o` 选项指定的输出文件。此选项需要 `-R` 选项来读取先前用 `-O` 选项收集和保存的采样。

**`-n`** `rate` 为命令行上后续指定的采样模式 PMC 设置默认采样率。默认情况下，PMC 配置为每 65536 个事件采样一次 CPU 的指令指针。

**`-o`** `outputfile` 将计数器读数和日志数据的文本表示发送到文件 `outputfile`。默认情况下，收集实时数据时输出发送到 `stderr`，处理预先存在的日志文件时输出发送到 `stdout`。

**`-p`** `event-spec` 分配一个进程模式计数 PMC，测量 `event-spec` 中指定的硬件事件。

**`-q`** 降低详细程度。

**`-r`** `fsroot` 将可执行文件所在的文件系统层次结构的顶层设置为参数 `fsroot`。默认为 **/**。

**`-s`** `event-spec` 分配一个系统模式计数 PMC，测量 `event-spec` 中指定的硬件事件。

**`-t`** `process-spec` 将进程模式 PMC 附加到由参数 `process-spec` 命名的进程。参数 `process-spec` 可以是表示特定进程 ID 的非负整数，或用于根据命令名称选择进程的正则表达式。

**`-u`** `event-spec` 提供事件的简短描述。

**`-v`** 提高详细程度。

**`-w`** `secs` 每 `secs` 秒打印所有计数模式 PMC 或 top 模式采样模式 PMC 的值。参数 `secs` 可以为小数值。默认间隔为 5 秒。

**`-z`** `graphdepth` 打印系统范围调用图时，将调用图限制为由参数 `graphdepth` 指定的深度。

如果指定了 `command`，则使用 execvp(3) 执行它。

## 实例

要在 AMD Athlon CPU 上执行系统范围统计采样，每 32768 条指令退役采样一次，并将数据采样到文件 `sample.stat`，使用：

```sh
pmcstat -O sample.stat -n 32768 -S k7-retired-instructions
```

要执行 `firefox` 并测量它及其子进程每 12 秒在 AMD Athlon 上遭受的数据缓存未命中次数，使用：

```sh
pmcstat -d -w 12 -p k7-dc-misses firefox
```

要测量所有名为“emacs”的进程的指令退役数，使用：

```sh
pmcstat -t '^emacs$' -p instructions
```

要在 10 秒内测量名为“emacs”的进程的指令退役数，使用：

```sh
pmcstat -t '^emacs$' -p instructions sleep 10
```

要在 Intel Pentium Pro/Pentium III SMP 系统的 CPU 0 和 2 上计数指令 TLB 未命中，使用：

```sh
pmcstat -c 0,2 -s p6-itlb-miss
```

要基于所看到的指令缓存未命中，收集特定进程（pid 为 1234）的配置文件信息，使用：

```sh
pmcstat -P ic-misses -t 1234 -O /tmp/sample.out
```

要基于处理器指令退役，在所有已配置的处理器上执行系统范围采样，使用：

```sh
pmcstat -S instructions -O /tmp/sample.out
```

如果不希望捕获调用图，使用：

```sh
pmcstat -N -S instructions -O /tmp/sample.out
```

要将生成的事件日志发送到远程机器，使用：

```sh
pmcstat -S instructions -O remotehost:port
```

在远程机器上，可以使用 [nc(1)](../man1/nc.1.md) 收集采样日志：

```sh
nc -l remotehost port > /tmp/sample.out
```

要从采样文件生成兼容 gprof(1) 的配置文件，使用：

```sh
pmcstat -R /tmp/sample.out -g
```

要将带调用图的系统范围配置文件打印到文件 `foo.graph`，使用：

```sh
pmcstat -R /tmp/sample.out -G foo.graph
```

## 诊断

如果指定了 `-v` 选项，`pmcstat` 可能会发出以下诊断消息：

- #callchain/dubious-frames 返回地址具有“不可能”值的调用链记录数。
- #exec handling errors 日志文件中命名了无法分析的可执行文件的 execve(2) 事件数。
- #exec/elf 命名 ELF 可执行文件的 execve(2) 事件数。
- #exec/unknown 命名无法识别格式的可执行文件的 execve(2) 事件数。
- #samples/total 日志文件中的采样总数。
- #samples/unclaimed 无法与已知可执行对象（即可执行文件、共享库、内核或运行时加载器）关联的采样数。
- #samples/unknown-object 与无法识别的对象格式的可执行文件关联的采样数。

`pmcstat` 工具成功时退出值为 0，发生错误时大于 0。

## 兼容性

由于 `gmon.out` 文件格式的限制，由 `-g` 选项生成的兼容 gprof(1) 的配置文件不包含有关跨可执行边界调用的信息。生成的 `gmon.out` 文件也仅对本地可执行文件有意义。

## 参见

gprof(1), [nc(1)](../man1/nc.1.md), execvp(3), pmc(3), pmclog(3), [hwpmc(4)](../man4/hwpmc.4.md), [pmccontrol(8)](pmccontrol.8.md), [sysctl(8)](sysctl.8.md)

## 历史

`pmcstat` 工具首次出现在 FreeBSD 6.0 中。

## 作者

Joseph Koshy <jkoshy@FreeBSD.org>

## 缺陷

`pmcstat` 工具尚不能分析由非本地架构生成的 [hwpmc(4)](../man4/hwpmc.4.md) 日志。
