# gdb(4)

`gdb` — 外部内核调试器

## 名称

`gdb`

## 概要

`makeoptions DEBUG=-g options DDB`

## 描述

`gdb` 内核调试器是 gdb(1)（`ports/devel/gdb`）的一个变体，它理解 FreeBSD 内核环境的某些方面。可以通过多种方式使用：

- 可用于检查运行所在处理器的内存。
- 可用于分析 panic 之后的处理器转储。
- 可通过串行或 firewire 链路交互式调试另一系统。在此模式下，可以停止处理器并单步执行。
- 通过 firewire 链路，可以在不参与远程系统的情况下检查远程系统的内存。在此模式下，无法停止处理器并单步执行，但当远程系统已崩溃且不再响应时可能有用。

用于远程调试时，`gdb` 需要存在 [ddb(4)](ddb.4.md) 内核调试器。可在 `gdb` 和 [ddb(4)](ddb.4.md) 之间切换的命令是存在的。

## 调试准备

调试内核时，构建带调试符号的内核几乎是必需的（`makeoptions DEBUG=-g`）。最简单的方法是从内核构建目录执行操作，默认为 **/usr/obj/usr/src/sys/GENERIC**。

首先，确保你在此目录中有调试宏的副本：

```sh
make gdbinit
```

此命令对 **/usr/src/tools/debugscripts** 中安装的宏执行一些转换，使其适应当地环境。

### 检查本机环境

要查看和更改你正在运行的系统的内存内容：

```sh
gdb -k -wcore kernel.debug /dev/mem
```

在此模式下，你需要 `-k` 标志以向 gdb(1)（`ports/devel/gdb`）指示“转储文件” **/dev/mem** 是内核数据文件。你可以查看实时数据，如果包含 `-wcore` 选项，还可以自行承担风险更改数据。系统不会停止（显然），因此有些操作无法工作。你可以设置断点，但不能“继续”执行，所以它们不会起作用。

### 调试崩溃转储

默认情况下，崩溃转储存储在目录 **/var/crash** 中。从内核构建目录检查它们：

```sh
gdb -k kernel.debug /var/crash/vmcore.29
```

在此模式下，系统显然已停止，因此你只能查看。

### 通过远程链路调试活动系统

在下文的讨论中，“本地系统”指运行调试器的系统，“远程系统”指被调试的活动系统。

要通过远程链路调试活动系统，内核必须使用 `options DDB` 选项编译。`options BREAK_TO_DEBUGGER` 选项使调试方机器在连接建立后能够通过按 `^C` 停止被调试机器。

### 通过远程串行链路调试活动系统

在 i386 平台上使用串行端口作为远程链路时，必须通过为指定接口设置标志位 `0x80` 来标识该串行端口。通常，此端口也将用作串行控制台（标志位 `0x10`），因此 **/boot/device.hints** 中的条目应为：

```sh
hint.sio.0.flags="0x90"
```

### 通过远程 firewire 链路调试活动系统

与串行调试一样，要通过 firewire 链路调试活动系统，内核必须使用 `options DDB` 选项编译。

设置 firewire 链路需要执行若干步骤：

```sh
kldload firewire
```

```sh
kldload dcons
kldload dcons_crom
```

```sh
fwohci0: BUS reset
fwohci0: node_id=0x8800ffc0, gen=2, non CYCLEMASTER mode
firewire0: 2 nodes, maxhop <= 1, cable IRM = 1
firewire0: bus manager 1
firewire0: New S400 device ID:00c04f3226e88061
dcons_crom0: <dcons configuration ROM> on firewire0
dcons_crom0: bus_addr 0x22a000
```

```sh
dcons_crom_enable="YES"
```

```sh
firewire_enable="YES"
```

```sh
# fwcontrol
2 devices (info_len=2)
node        EUI64        status
   1  0x00c04f3226e88061      0
   0  0x000199000003622b      1
```

```sh
# fwcontrol
2 devices (info_len=2)
node        EUI64        status
   0  0x000199000003622b      0
   1  0x00c04f3226e88061      1
```

```sh
dconschat -br -G 5556 -t 0x000199000003622b
```

```sh
# gdb kernel.debug
GNU gdb 5.2.1 (FreeBSD)
*(political statements omitted)*
Ready to go.  Enter 'tr' to connect to the remote target
with /dev/cuau0, 'tr /dev/cuau1' to connect to a different port
or 'trf portno' to connect to the remote target with the firewire
interface.  portno defaults to 5556.
Type 'getsyms' after connection to load kld symbols.
If you are debugging a local system, you can use 'kldsyms' instead
to load the kld symbols.  That is a less obnoxious interface.
(gdb) trf
0xc21bd378 in ?? ()
```

```sh
dconschat -br -G 4711 -t 0x000199000003622b
```

```sh
(gdb) tr localhost:4711
0xc21bd378 in ?? ()
```

- 确保两个系统都有 [firewire(4)](firewire.4.md) 支持，并且远程系统的内核包含 [dcons(4)](dcons.4.md) 和 [dcons_crom(4)](dcons_crom.4.md) 驱动程序。如果未编译进内核，加载 KLD：仅在远程系统上：你应在远程系统的 [dmesg(8)](../man8/dmesg.8.md) 输出中看到类似以下内容：建议在引导时通过 **/boot/loader.conf** 中的以下条目加载这些模块：这确保三个模块都被加载。在本地系统上加载 [dcons(4)](dcons.4.md) 和 [dcons_crom(4)](dcons_crom.4.md) 无害，但如果你只想加载 [firewire(4)](firewire.4.md) 模块，请在 **/boot/loader.conf** 中包含以下内容：
- 接下来，使用 fwcontrol(8) 找到对应于远程机器的 firewire 节点。在本地机器上你可能看到：第一个节点始终是本地系统，因此在此情况下节点 0 是远程系统。如果有两个以上系统，请从另一端检查以找到对应远程系统的节点。在远程机器上，看起来像这样：
- 接下来，使用 dconschat(8) 建立 firewire 连接：`0x000199000003622b` 是远程节点的 EUI64 地址，由上文 fwcontrol(8) 的输出确定。以这种方式启动时，dconschat(8) 从端口 `localhost:5556` 建立到远程调试器的本地隧道连接。也可以通过在同一 dconschat(8) 调用中加 `-C` 选项建立控制台端口连接。详见 dconschat(8) 手册页。dconschat(8) 工具不会将控制权返回给用户。它显示远程系统的错误消息和控制台输出，因此最好在单独的窗口中启动它。
- 最后，建立连接：`trf` 宏假设连接端口为 5556。如果你想使用不同端口（通过更改上述 dconschat(8) 调用），请改用 `tr` 宏。例如，如果你想使用端口 4711，按如下方式运行 dconschat(8)：然后建立连接：

### 通过远程 firewire 链路非协作调试活动系统

除上文所述的常规 firewire 调试外，一旦建立了初始连接，也可以在远程系统不协作的情况下进行调试。这对应于使用 **/dev/mem** 调试本地机器。当系统崩溃且调试器不再响应时非常有用。要使用此方法，将 [sysctl(8)](../man8/sysctl.8.md) 变量 `hw.firewire.fwmem.eui64_hi` 和 `hw.firewire.fwmem.eui64_lo` 分别设置为远程系统 EUI64 ID 的高半部分和低半部分。从上例中，远程机器显示为：

```sh
# fwcontrol
2 devices (info_len=2)
node        EUI64        status
   0  0x000199000003622b      0
   1  0x00c04f3226e88061      1
```

输入：

```sh
# sysctl -w hw.firewire.fwmem.eui64_hi=0x00019900
hw.firewire.fwmem.eui64_hi: 0 -> 104704
# sysctl -w hw.firewire.fwmem.eui64_lo=0x0003622b
hw.firewire.fwmem.eui64_lo: 0 -> 221739
```

注意，变量必须以十六进制显式指定。此后，你可以通过以下输入检查远程机器的状态：

```sh
# gdb -k kernel.debug /dev/fwmem0.0
GNU gdb 5.2.1 (FreeBSD)
*(messages omitted)*
Reading symbols from /boot/kernel/dcons.ko...done.
Loaded symbols for /boot/kernel/dcons.ko
Reading symbols from /boot/kernel/dcons_crom.ko...done.
Loaded symbols for /boot/kernel/dcons_crom.ko
#0  sched_switch (td=0xc0922fe0) at /usr/src/sys/kern/sched_4bsd.c:621
0xc21bd378 in ?? ()
```

在此情况下，不必显式加载符号。远程系统继续运行。

## 命令

`gdb` 的用户界面通过 gdb(1)（`ports/devel/gdb`）实现，因此 gdb(1)（`ports/devel/gdb`）命令也有效。本节仅讨论安装到内核构建目录中的内核调试扩展。

### 调试环境

以下宏用于操作调试环境：

**`ddb`** 切换回 [ddb(4)](ddb.4.md)。此命令仅在执行远程调试时才有意义。

**`getsyms`** 显示目标机器的 `kldstat` 信息并邀请用户将其粘贴回来。这是必需的，因为 `gdb` 不允许将数据传递给 shell 脚本。远程调试和崩溃转储需要此操作；对于本地内存调试，改用 `kldsyms`。

**`kldsyms`** 读取调试机器的符号表。这对于远程调试和崩溃转储无效；改用 `getsyms`。

**`tr`** `interface` 通过指定的串行或 firewire 接口调试远程系统。

**`tr0`** 通过串行接口 **/dev/cuau0** 调试远程系统。

**`tr1`** 通过串行接口 **/dev/cuau1** 调试远程系统。

**`trf`** 通过 firewire 接口以默认端口 5556 调试远程系统。

命令 `tr0`、`tr1` 和 `trf` 是调用 `tr` 的便捷命令。

### 当前进程环境

以下宏是便捷函数，旨在使操作比标准 gdb(1)（`ports/devel/gdb`）命令更简单。

**`f0`** 选择栈帧 0 并显示汇编级细节。

**`f1`** 选择栈帧 1 并显示汇编级细节。

**`f2`** 选择栈帧 2 并显示汇编级细节。

**`f3`** 选择栈帧 3 并显示汇编级细节。

**`f4`** 选择栈帧 4 并显示汇编级细节。

**`f5`** 选择栈帧 5 并显示汇编级细节。

**`xb`** 以十六进制显示从当前 `ebp` 值开始的 12 个字。

**`xi`** 列出从当前 `eip` 值开始的下 10 条指令。

**`xp`** 显示寄存器内容和当前栈帧的前四个参数。

**`xp0`** 以多种格式显示当前栈帧的第一个参数。

**`xp1`** 以多种格式显示当前栈帧的第二个参数。

**`xp2`** 以多种格式显示当前栈帧的第三个参数。

**`xp3`** 以多种格式显示当前栈帧的第四个参数。

**`xp4`** 以多种格式显示当前栈帧的第五个参数。

**`xs`** 以十六进制显示栈上最后 12 个字。

**`xxp`** 显示寄存器内容和前十个参数。

**`z`** 单步执行 1 条指令（跳过调用）并显示下一条指令。

**`zs`** 单步执行 1 条指令（进入调用）并显示下一条指令。

### 检查其他进程

以下宏用于访问其他进程。`gdb` 调试器不理解多进程概念，因此它们实际上绕过了整个 `gdb` 环境。

**`btp`** `pid` 显示进程 `pid` 的回溯。

**`btpa`** 显示系统中所有进程的回溯。

**`btpp`** 显示先前用 `defproc` 选择的进程的回溯。

**`btr`** `ebp` 从指定的 `ebp` 地址显示回溯。

**`defproc`** `pid` 为本节中某些其他命令指定进程的 PID。

**`fr`** `frame` 显示先前用 `defproc` 选择的进程栈的 `frame` 帧。

**`pcb`** `proc` 显示进程 `proc` 的某些 PCB 内容。

### 检查数据结构

你可以使用标准 gdb(1)（`ports/devel/gdb`）命令查看大多数数据结构。本节的宏是便捷函数，通常以更易读的格式显示数据，或省略结构中不太重要的部分。

**`bp`** 显示当前帧中变量 `bp` 所指向的缓冲区头信息。

**`bpd`** 显示当前帧中 `bp->data` 的内容（`char *`）。

**`bpl`** 显示局部变量 `bp` 所指向的缓冲区头（`struct bp`）的详细信息。

**`bpp`** `bp` 显示参数 `bp` 所指向的缓冲区头（`struct bp`）的摘要信息。

**`bx`** 打印当前环境中指针 `bp` 所指向缓冲区头的若干字段。

**`vdev`** 显示局部变量 `vp` 所指向 `vnode` 的某些信息。

### 杂项宏

```sh
dmesg -M /var/crash/vmcore.0 -N kernel.debug
dmesg -M /dev/fwmem0.0 -N kernel.debug
```

```sh
ps -M /var/crash/vmcore.0 -N kernel.debug
ps -M /dev/fwmem0.0 -N kernel.debug
```

```sh
Redefine foo?
```

**`checkmem`** 检查未分配内存是否被修改。这假定内核已使用 `options DIAGNOSTIC` 编译。这会将空闲内存的内容设置为 `0xdeadc0de`。

**`dmesg`** 打印系统消息缓冲区。这对应于 [dmesg(8)](../man8/dmesg.8.md) 工具。此宏以前称为 `msgbuf`。通过串行线路可能需要很长时间，由于 `gdb` 中的低效，通过 firewire 或本地内存更慢。调试崩溃转储或通过 firewire 时，无需启动 `gdb` 来访问消息缓冲区：而是使用以下适当变体：

**`kldstat`** 等价于不带选项的 [kldstat(8)](../man8/kldstat.8.md) 工具。

**`pname`** 打印当前进程的命令名。

**`ps`** 显示进程状态。这在概念上（但外观上不）对应于 [ps(1)](../man1/ps.1.md) 工具。调试崩溃转储或通过 firewire 时，无需启动 `gdb` 来显示 [ps(1)](../man1/ps.1.md) 输出：而是使用以下适当变体：

**`y`** 用于编写宏的临时方案。编写宏时，将它们粘贴回 `gdb` 窗口很方便。但不幸的是，如果宏已定义，`gdb` 坚持询问“是否重定义 foo？”在你回答 `y` 之前不会放弃。此命令就是该回答。除了打印一条警告消息提醒你再次删除它之外，什么也不做。

## 参见

gdb(1)（`ports/devel/gdb`），[ps(1)](../man1/ps.1.md)，[ddb(4)](ddb.4.md)，[firewire(4)](firewire.4.md)，dconschat(8)，[dmesg(8)](../man8/dmesg.8.md)，fwcontrol(8)，[kldload(8)](../man8/kldload.8.md)

## 作者

本手册页由 Greg Lehey <grog@FreeBSD.org> 编写。

## 缺陷

gdb(1)（`ports/devel/gdb`）调试器从未被设计用于调试内核，因此并不十分契合。存在许多问题。

`gdb` 实现效率很低，许多操作都很慢。

串行调试更慢，竞态条件可能使链路难以超过 9600 bps 运行。Firewire 连接没有此问题。

调试宏“随用随长”。通常，编写它们的人在寻找特定问题时编写，因此可能不够通用，并且以非预期方式使用时可能表现不佳，即使这些方式是合理的。

这些命令中许多仅在 ia32 架构上工作。
