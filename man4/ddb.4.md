# ddb.4

`ddb` — 交互式内核调试器

## 名称

`ddb`

## 概要

`若要启用内核调试功能，请包含：`

> options KDB
> options DDB

`为防止在内核 panic(9) 时激活调试器：`

> options KDB_UNATTENDED

`为在 panic 时于控制台打印当前线程的栈跟踪：`

> options KDB_TRACE

`为除符号表示外还打印符号的数值，请定义：`

> options DDB_NUMSYM

`为启用 gdb(4) 后端以便使用 kgdb(1)（ports/devel/gdb）进行远程调试，请包含：`

> options GDB

## 描述

`ddb` 内核调试器是一个交互式调试器，其语法受 gdb(1)（`ports/devel/gdb`）启发。如果链接到运行中的内核，可通过 `debug` keymap(5) 动作（通常映射到 Ctrl+Alt+Esc）在本地调用，或者通过将 `debug.kdb.enter` sysctl 设置为 1 来调用。如果 `debug.debugger_on_panic` [sysctl(8)](../man8/sysctl.8.md) MIB 变量设置为非零值（除非指定 `KDB_UNATTENDED` 选项，否则这是默认值），则也会在内核 [panic(9)](../man9/panic.9.md) 时调用调试器。类似地，如果 `debug.debugger_on_recursive_panic` 变量设置为 `1`，则会在递归内核 panic 时调用调试器。此变量的默认值为 `0`，并且如果 `debug.debugger_on_panic` 已设置为非零值，则无效果。

当前位置称为 `dot`。`dot` 以十六进制格式显示在提示符处。命令 `examine` 和 `write` 将 `dot` 更新为最后检查行的地址或最后修改的位置，并将 `next` 设置为下一个要检查或更改的位置的地址。其他命令不更改 `dot`，并将 `next` 设置为与 `dot` 相同。

通用命令语法为：`command`[`/``modifier`] [`addr` ][,`count`]]

空行以 `next` 地址为起点重复上一条命令，计数为 1，无修饰符。指定 `addr` 会将 `dot` 设置为该地址。省略 `addr` 则使用 `dot`。对于打印命令，缺少 `count` 时取 1，对于栈跟踪取无穷大。`count` 为 -1 等同于缺少 `count`。已提供但给定 `command` 不支持的选项通常被忽略。

`ddb` 调试器具有分页器功能（类似 [more(1)](../man1/more.1.md) 命令）用于输出。如果输出行数超过 `lines` 变量中设置的数字，则显示“`--More--`”并等待响应。有效的响应为：

**`SPC`** 再显示一页
**`RET`** 再显示一行
**`q`** 中止当前命令，并返回到命令输入模式

最后，`ddb` 提供了一个小型（当前为 10 项）的命令历史，并提供简单的 `emacs` 风格命令行编辑功能。除了 `emacs` 控制键外，还可使用常规的 ANSI 方向键浏览历史缓冲区，并在当前行内移动光标。

## 命令

### 通用调试器命令

**`b`** 按字节（8 位）查看
**`h`** 按半字（16 位）查看
**`l`** 按长字（32 位）查看
**`g`** 按四字（64 位）查看
**`a`** 打印正在显示的位置
**`A`** 尽可能打印带行号的位置
**`x`** 以无符号十六进制显示
**`z`** 以有符号十六进制显示
**`o`** 以无符号八进制显示
**`d`** 以有符号十进制显示
**`u`** 以无符号十进制显示
**`r`** 以当前基数显示，有符号
**`c`** 将低 8 位显示为字符。非打印字符以八进制转义码显示（例如 `e000 ）`。
**`s`** 显示位于该位置的以空字符结尾的字符串。非打印字符以八进制转义显示。
**`m`** 以无符号十六进制显示，每行末尾附字符转储。位置也以十六进制显示在每行开头。
**`i`** 显示为反汇编指令
****** 显示为反汇编指令，根据机器可能有替代格式。在 i386 上，这会选择指令解码的替代格式（32 位代码段中的 16 位，反之亦然）。
**`S`** 显示存储在该地址的指针的符号名称

```sh
print/x "eax = " $eax "enecx = " $ecx "en"
```

```sh
eax = xxxxxx
ecx = yyyyyy
```

**`help`** 打印可用命令和命令缩写的简短摘要。
**Xo** `examine`[`/``AISabcdghilmorsuxz ...`] [`addr` ][,`count`]] Xc
**Xo** `x`[`/``AISabcdghilmorsuxz ...`] [`addr` ][,`count`]] Xc 根据修饰符中的格式显示寻址的位置。多个修饰符格式显示多个位置。如果未指定格式，则使用此命令最后指定的格式。格式字符为：
**`xf`** 向前检查：使用上次指定的参数执行 `examine` 命令，但使用其显示的下一个地址作为起始地址。
**`xb`** 向后检查：使用上次指定的参数执行 `examine` 命令，但使用上次的起始地址减去其显示的大小作为起始地址。
**`print`** [`/``acdoruxz`]
**`p`** [`/``acdoruxz`] 根据修饰符字符（如上文 `examine ）`所述）打印 `addr`。有效格式为：`a , x , z , o , d , u , r` 和 `c`。如果未指定修饰符，则使用上次为其指定的修饰符。参数 `addr` 可以是字符串，在这种情况下按原样打印。例如：将打印如下：
**`pprint`** [`/``d depth` ][`name` ]]] 使用 CTF 调试数据美化打印由 `name` 指定的符号。适用于内核和已加载内核模块导出的所有符号。如果指定了 `d` 修饰符，嵌套至 `depth` 层的结构内容也将包含在输出中。
**`pprint struct`** [`/``d depth` ][`name` ][`addr`]]] 将 `addr` 处的内存作为结构 `name` 打印。适用于内核和已加载内核模块定义的所有结构。如果指定了 `d` 修饰符，嵌套至 `depth` 层的结构内容也将包含在输出中。
**Xo** `write`[`/``bhl`] `addr expr1` [`expr2 ...`] Xc
**Xo** `w`[`/``bhl`] `addr expr1` [`expr2 ...`] Xc 将命令行上 `addr` 之后指定的表达式写入从 `addr` 开始的后续位置。写入单位大小可在修饰符中用字母 `b`（字节）、`h`（半字）或 `l`（长字）指定。如果省略，则假定为长字。**警告：** 由于表达式之间没有分隔符，可能会发生奇怪的情况。最好将每个表达式括在括号中。
**`set`** `$``variable` [`=` ]`expr`] 用 `expr` 的值设置指定变量或寄存器。有效的变量名见下文。
**`break`** [`/``u` ][`addr` ][,`count`]]]
**`b`** [`/``u` ][`addr` ][,`count`]]] 在 `addr` 处设置断点。如果提供了 `count`，则 `continue` 命令在前 `count` - 1 次命中此断点时不会停止。如果设置了断点，则会用 `#` 打印断点号。此号码可用于删除断点或向其添加条件。如果指定了 `u` 修饰符，此命令在用户地址空间设置断点。不带 `u` 选项时，地址被视为内核空间，错误的空域地址将以错误消息拒绝。仅当机器相关例程支持时才能使用此修饰符。**警告：** 如果用户文本被普通用户空间调试器遮蔽，用户空间断点可能无法正常工作。在低级代码路径上设置断点也可能导致奇怪的行为。
**`delete`** [`addr`]
**`d`** [`addr`]
**`delete`** `#``number`
**`d`** `#``number` 删除指定的断点。可通过带 `#` 的断点号、使用原始 `break` 命令中指定的相同 `addr`，或省略 `addr` 以获取 `dot` 的默认地址来指定断点。
**`halt`** 停止系统。
**`watch`** [`addr` ][,`size`]] 为某区域设置监视点。当尝试修改该区域时，执行停止。`size` 参数默认为 4。如果指定了错误的空域地址，请求将以错误消息拒绝。**警告：** 在某些系统（如 i386）上，尝试监视连接的内核内存可能导致不可恢复的错误。对用户地址的监视点效果最佳。
**`hwatch`** [`addr` ][,`size`]] 如果架构支持，为某区域设置硬件监视点。当尝试修改该区域时，执行停止。`size` 参数默认为 4。**警告：** 硬件调试设施没有像 watch 命令那样的独立地址空间概念。仅对内核地址位置设置监视点时使用 `hwatch`，避免在用户模式地址空间使用。
**`dhwatch`** [`addr` ][,`size`]] 删除指定的硬件监视点。
**`kill`** `sig pid` 向进程 `pid` 发送信号 `sig`。信号在从调试器返回时生效。此命令可用于在系统挂起时杀死引起资源争用的进程。信号列表见 signal(3)。注意，参数相对于 kill(2) 是颠倒的。
**`step`** [`/``p` ][,`count`]]
**`s`** [`/``p` ][,`count`]] 单步执行 `count` 次。如果指定了 `p` 修饰符，则在每一步打印每条指令。否则仅打印最后一条指令。**警告：** 根据机器类型，可能无法单步执行某些低级代码路径或用户空间代码。在具有软件模拟单步执行的机器上（例如 pmax），单步执行中断处理程序执行的代码可能会做错事。
**`continue`** [`/``c`]
**`c`** [`/``c`] 继续执行直到断点或监视点。如果指定了 `c` 修饰符，则在执行时计数指令。某些机器（例如 pmax）还计数加载和存储。**警告：** 计数时，调试器实际上是静默地单步执行。这意味着在低级代码上单步执行可能会导致奇怪的行为。
**`until`** [`/``p`] 在下一条调用或返回指令处停止。如果指定了 `p` 修饰符，则在每个调用或返回处打印调用嵌套深度和累计指令计数。否则仅在命中匹配的返回时打印。
**`next`** [`/``p`]
**`match`** [`/``p`] 在匹配的返回指令处停止。如果指定了 `p` 修饰符，则在每个调用或返回处打印调用嵌套深度和累计指令计数。否则仅在命中匹配的返回时打印。
**Xo** `trace`[`/``u`] [`pid | tid`] [,`count`] Xc
**Xo** `t`[`/``u`] [`pid | tid`] [,`count`] Xc
**Xo** `where`[`/``u`] [`pid | tid`] [,`count`] Xc
**Xo** `bt`[`/``u`] [`pid | tid`] [,`count`] Xc 栈跟踪。`u` 选项跟踪用户空间；如果省略，`trace` 仅跟踪内核空间。可选参数 `count` 是要跟踪的帧数。如果省略 `count`，则打印所有帧。**警告：** 用户空间栈跟踪仅在机器相关代码支持时有效。
**Xo** `search`[`/``bhl`] `addr` `value` [`mask`] [,`count`] Xc 在内存中搜索 `value`。可选的 `count` 参数限制搜索范围。
**Xo** `reboot`[`/``s`] [`seconds`] Xc
**Xo** `reset`[`/``s`] [`seconds`] Xc 硬重置系统。如果给出了可选参数 `seconds`，调试器将在重新引导前等待这么长时间，最多一周。当给出 `s` 修饰符时，命令将跳过运行任何已注册的关机处理程序，并尝试最基本的重置。
**`thread`** `addr | tid` 如果参数是十进制数字，则将调试器切换到 ID 为 `tid` 的线程，否则切换到地址为 `addr` 的线程。
**`watchdog`** [`exp`] 编程 [watchdog(4)](watchdog.4.md) 定时器在 2^`exp` 秒后触发。如果未提供参数，则禁用 watchdog 定时器。

### 专用辅助命令

**`class`** ：锁的类。可能的类型包括 [mutex(9)](../man9/mutex.9.md)、[rmlock(9)](../man9/rmlock.9.md)、[rwlock(9)](../man9/rwlock.9.md)、[sx(9)](../man9/sx.9.md)。

**`name`** ：锁的名称。

**`flags`** ：传递给锁初始化函数的标志。*flags* 值特定于锁类。

**`state`** ：锁的当前状态。*state* 值特定于锁类。

**`owner`** ：锁的所有者。

**`Type`** 指定内存的类型。它与使用 MALLOC_DECLARE(9) 定义给定内存类型时使用的描述字符串相同。
**`InUse`** 给定类型的内存分配数，尚未调用 free(9)。
**`MemUse`** 给定分配类型消耗的总内存。
**`Requests`** 给定内存类型的内存分配请求数。

**`cpuid`** 处理器标识符。
**`curthread`** 线程指针、进程标识符和进程名称。
**`curpcb`** 控制块指针。
**`fpcurthread`** FPU 线程指针。
**`idlethread`** 空闲线程指针。
**`APIC ID`** 来自 APIC 的 CPU 标识符。
**`currentldt`** LDT 指针。
**`spin locks held`** 持有的自旋锁名称。

**`第一列`** 线程标识符（TID）
**`第二列`** 线程结构地址
**`第三列`** 回溯。

**`Zone`** UMA 区域的名称。与作为第一个参数传递给 uma_zcreate(9) 的字符串相同。
**`Size`** 给定内存对象（slab）的大小。
**`Used`** 当前正在使用的 slab 数。
**`Free`** UMA 区域内空闲 slab 数。
**`Requests`** 对给定区域的分配请求数。
**`Total Mem`** 区域正在使用的总内存（已分配或空闲），以字节为单位。
**`XFree`** UMA 区域内与分配时不同的 NUMA 域上释放的空闲 slab 数。（`Free` 列中的计数包含 `XFree 。`）

**Xo** `findstack` `addr` Xc 如果内核模式栈中包含 `addr`，则打印该线程的地址。
**`show`** `active trace`
**`acttrace`** 显示每个在 CPU 上运行的线程的栈跟踪。
**`show`** `all procs`[`/``a`]
**`ps`** [`/``a`] 显示所有进程信息。如果机器不支持，或者目标进程栈底当时不在主内存中，则可能不显示进程信息。`a` 修饰符将为每个进程打印命令行参数。
**`show`** `all tcpcbs`[`/``b``i``l`] 显示与 "show tcpcb" 相同的输出，但针对系统中的所有 TCP 控制块。`b` 修饰符将请求打印 BBLog 条目。如果提供 `i` 修饰符，还将显示相应的 IP 控制块。使用 `l` 修饰符将输出限制为已锁定的 TCP 控制块。
**`show`** `all trace`
**`alltrace`** 显示系统中每个线程的栈跟踪。
**`show`** `all ttys` 显示系统中的所有 TTY。输出类似于 pstat(8)，但还包括 TTY 结构的地址。
**`show`** `all vnets` 显示与 "show vnet" 相同的输出，但列出系统中的所有虚拟化网络栈。
**`show`** `allchains` 显示与 "show lockchain" 相同的信息，但针对系统中的每个线程。
**`show`** `alllocks` 显示当前持有的所有锁。此命令仅在内核中包含 [witness(4)](witness.4.md) 时可用。
**`show`** `allpcpu` 与 "show pcpu" 相同，但针对系统中的每个 CPU。
**`show`** `allrman` 显示与资源管理相关的信息，包括中断请求线、DMA 请求线、I/O 端口、I/O 内存地址和资源 ID。
**`show`** `apic` 转储有关 APIC IDT 向量映射的数据。
**`show`** `badstacks` 遍历 [witness(4)](witness.4.md) 图并打印任何锁顺序违规。此命令仅在内核中包含 [witness(4)](witness.4.md) 时可用。
**`show`** `breaks` 显示用 "break" 命令设置的断点。
**`show`** `bio` `addr` 显示有关位于 `addr` 的 bio 结构 `struct bio` 的信息。有关结构字段确切含义的更多细节，请参见 `sys/bio.h` 头文件和 [g_bio(9)](../man9/g_bio.9.md)。
**`show`** `buffer` `addr` 显示有关位于 `addr` 的 buf 结构 `struct buf` 的信息。有关结构字段确切含义的更多细节，请参见 `sys/buf.h` 头文件。
**`show`** `callout` `addr` 显示有关位于 `addr` 的 callout 结构 `struct callout` 的信息。
**`show`** `cdev` [`addr`] 显示位于 `addr` 的 cdev 结构的内部 devfs 状态。如果未提供参数，则显示所有已创建 cdev 的列表，包括 devfs 节点名称和 `struct cdev` 地址。
**`show`** `conifhk` 列出当前在 Fn run_interrupt_driven_config_hooks 中等待完成的钩子。
**`show`** `cpusets` 打印带编号的根 CPU 亲和性集和已分配的 CPU 亲和性集。更多细节见 cpuset(2)。
**`show`** `cyrixreg` 显示 Cyrix 处理器特定的寄存器。
**`show`** `devmap` 打印静态设备映射表的内容。目前仅在 ARM 架构上可用。
**`show`** `domain` `addr` 打印地址 `addr` 处的协议域结构 `struct domain`。有关结构字段确切含义的更多细节，请参见 `sys/domain.h` 头文件。
**`show`** `ffs` [`addr`] 如果给出了参数，则显示有关地址 `addr` 处 ffs 挂载的简要信息。否则提供每个 ffs 挂载的摘要。
**`show`** `file` `addr` 显示有关位于地址 `addr` 的文件结构 `struct file` 的信息。
**`show`** `files` 显示系统中每个文件结构的信息。
**`show`** `freepages` 显示每个空闲列表中的物理页数。
**`show`** `geom` [`addr`] 如果未给出 `addr` 参数，则显示整个 GEOM 拓扑。如果给出 `addr`，则显示给定 GEOM 对象（类、geom、提供者或消费者）的详细信息。
**`show`** `idt` 显示 IDT 布局。第一列指定 IDT 向量。第二列是中断/陷阱处理程序的名称。这些函数是机器相关的。
**`show`** `igi_list` `addr` 显示有关位于 `addr` 的 IGMP 结构 `struct igmp_ifsoftc` 的信息。
**`show`** `iosched` `addr` 显示有关位于 `addr` 的 I/O 调度器 `struct cam_iosched_softc` 的信息。
**`show`** `inodedeps` [`addr`] 显示每个 inodedep 结构的简要信息。如果给出 `addr`，则仅显示属于位于所提供地址的文件系统的 inodedeps。
**`show`** `inpcb` `addr` 显示有关位于 `addr` 的 IP 控制块 `struct in_pcb` 的信息。
**`show`** `intr` 转储有关中断处理程序的信息。
**`show`** `intrcnt` 转储中断统计信息。
**`show`** `irqs` 显示中断线及其各自的内核线程。
**`show`** `ktr`[`/``a``v``V`] 打印 [ktr(4)](ktr.4.md) 跟踪缓冲区的内容。`v` 修饰符将请求完全详细的输出，为每个跟踪条目打印文件、行号和时间戳。`V` 修饰符将仅请求打印时间戳。`a` 修饰符将请求输出不分页。
**`show`** `lapic` 显示此 CPU 的本地 APIC 寄存器信息。
**`show`** `lock` `addr` 显示锁结构。输出格式如下：
**`show`** `lockchain` `addr` 基于非自旋锁显示位于地址 `addr` 的特定线程所等待的所有线程。
**`show`** `lockedbufs` 显示与 "show buf" 相同的信息，但针对每个已锁定的 `struct buf` 对象。
**`show`** `lockedvnods` 列出系统中所有已锁定的 vnode。
**`show`** `locks` 打印当前已获取的所有锁。此命令仅在内核中包含 [witness(4)](witness.4.md) 时可用。
**`show`** `locktree`
**`show`** `malloc`[`/``i`] 打印 [malloc(9)](../man9/malloc.9.md) 内存分配器统计信息。如果指定了 `i` 修饰符，则将输出格式化为机器可分析的逗号分隔值（"CSV"）。输出列如下：可在用户空间中使用“`vmstat` `-m`”收集相同信息。
**`show`** `map`[`/``f` ]`addr`] 打印位于 `addr` 的 VM 映射。如果指定了 `f` 修饰符，则打印完整映射。
**`show`** `msgbuf` 打印系统消息缓冲区。与“`dmesg`”情况下的输出相同。如果你遇到内核 panic、连接了串行线缆到机器并希望获取系统挂起之前的引导消息，则很有用。
**`show`** `mount` [`addr`] 显示有关位于 `addr` 的挂载点的详细信息。如果未指定 `addr`，则显示所有当前已挂载文件系统的简短信息。
**`show`** `object`[`/``f` ]`addr`] 打印位于 `addr` 的 VM 对象。如果指定了 `f` 选项，则打印完整对象。
**`show`** `panic` 打印 panic 消息（如果已设置）。
**`show`** `page` 显示 VM 页面的统计信息。
**`show`** `pageq` 显示 VM 页面队列的统计信息。
**`show`** `pciregs` 打印 PCI 总线寄存器。可在用户空间中通过运行“`pciconf` `-lv`”收集相同信息。
**`show`** `pcpu` 打印当前处理器状态。输出格式如下：
**`show`** `pgrpdump` 转储系统中存在的进程组。
**`show`** `preload` 美化打印由 [loader(8)](../man8/loader.8.md) 传递给内核的元数据。
**`show`** `prison` [`addr`] 显示位于 `addr` 的 prison 结构。如果未指定 `addr` 参数，则显示系统中所有 prison 的信息。
**`show`** `proc` [`addr`] 显示有关位于地址 `addr` 的进程结构的信息，如果未指定参数，则显示当前进程的信息。
**`show`** `procvm` [`addr`] 显示位于 `addr` 的进程的进程虚拟内存布局，如果未指定参数，则显示当前进程的信息。
**`show`** `protosw` `addr` 打印地址 `addr` 处的协议切换结构 `struct protosw`。
**`show`** `registers`[`/``u`] 显示寄存器集。如果指定了 `u` 修饰符，则改为显示线程上一个 trapframe 的寄存器内容。通常，这对应用户空间保存的状态。
**`show`** `rman` `addr` 显示地址 `addr` 处的资源管理器对象 `struct rman`。可使用 "show allrman" 命令收集特定指针的地址。
**`show`** `route` `addr` 显示目标 `addr` 的路由表结果。此时支持 INET 和 INET6 格式的地址。
**`show`** `routetable` [`af` ]] 显示完整路由表。如果指定了 `af`，则仅显示给定数字地址族的路由。如果未指定参数，则转储所有地址族的路由表。
**`show`** `rtc` 显示实时时钟值。对于长时间调试会话很有用。
**`show`** `sleepchain` 已弃用。现在是 `show` `lockchain` 的别名。
**`show`** `sleepq` `addr`
**`show`** `sleepqueue` `addr` 显示位于 `addr` 的 [sleepqueue(9)](../man9/sleepqueue.9.md) 结构。
**`show`** `sockbuf` `addr` 显示位于 `addr` 的套接字缓冲区 `struct sockbuf`。
**`show`** `socket` `addr` 显示位于 `addr` 的套接字对象 `struct socket`。
**`show`** `sysregs` 显示系统寄存器（例如 i386 上的 `cr0-4`。）某些平台上不可用。
**`show`** `tcpcb`[`/``b``i` ]`addr`] 打印位于地址 `addr` 的 TCP 控制块 `struct tcpcb`。有关输出的确切解释，请访问 `netinet/tcp.h` 头文件。`b` 修饰符将请求打印 BBLog 条目。如果提供 `i` 修饰符，还将显示相应的 IP 控制块。
**`show`** `thread` [`addr | tid`] 如果未指定 `addr` 或 `tid`，则显示当前线程的详细信息。否则，打印 ID 为 `tid` 或内核地址 `addr` 的线程信息。（如果参数是十进制数字，则假定为 tid。）
**`show`** `threads` 显示系统中的所有线程。输出格式如下：
**`show`** `tty` `addr` 以可读形式显示 TTY 结构的内容。
**`show`** `turnstile` `addr` 显示地址 `addr` 处的 turnstile `struct turnstile` 结构。turnstile 是 FreeBSD 内核中用于实现同步原语的结构，在持有特定类型的锁时不能睡眠或切换到另一线程。目前这些是：[mutex(9)](../man9/mutex.9.md)、[rwlock(9)](../man9/rwlock.9.md)、[rmlock(9)](../man9/rmlock.9.md)。
**`show`** `uma`[`/``i`] 显示 UMA 分配器统计信息。如果指定了 `i` 修饰符，则将输出格式化为机器可分析的逗号分隔值（"CSV"）。输出包含以下列：可在用户空间中借助“`vmstat` `-z`”收集相同信息。
**`show`** `unpcb` `addr` 显示位于地址 `addr` 的 UNIX 域套接字专用控制块 `struct unpcb`。
**`show`** `vmochk` 打印内部 VM 对象是否在某映射中且没有零引用计数。
**`show`** `vmopag` 遍历系统中的 VM 对象列表，打印属于每个对象的 VM 页面的索引和物理地址。
**`show`** `vnet` `addr` 打印位于地址 `addr` 的虚拟化网络栈 `struct vnet` 结构。
**`show`** `vnode` `addr` 打印位于 `addr` 的 vnode `struct vnode` 结构。有关输出的确切解释，请查看 `sys/vnode.h` 头文件。
**`show`** `vnodebufs` `addr` 显示位于 `addr` 的 vnode 的干净/脏缓冲区列表。
**`show`** `vpath` `addr` 遍历名称缓存以查找位于 `addr` 的 vnode 的路径名。
**`show`** `watches` 显示所有监视点。显示用 "watch" 命令设置的监视点。
**`show`** `witness` 显示来自 [witness(4)](witness.4.md) 子系统的锁获取信息。

### 离线调试命令

**`dump`** 向 dumpon(8) 配置的设备发起内核核心转储。
**`gdb`** 切换到远程 GDB 模式。在远程 GDB 模式下，需要另一台机器运行 gdb(1)（`ports/devel/gdb`）使用远程调试功能，并连接到目标机器的串行控制台端口。
**`netdump`** `-s` `server` [`-g` `gateway` `-c` `client` `-i` `iface` ]] 使用提供的参数配置 [netdump(4)](netdump.4.md)，并立即执行 netdump。存在一些已知限制。主要是 [netdump(4)](netdump.4.md) 目前仅支持 IPv4。`netdump` 命令的地址参数必须是点分十进制 IPv4 地址。（不支持主机名。）目前，该命令仅在机器处于 panic 状态时才有效。最后，`vmstat` `netdump` 命令不提供任何配置压缩或加密的方法。
**`netgdb`** `-s` `server` [`-g` `gateway` `-c` `client` `-i` `iface` ]] 使用提供的参数发起 [netgdb(4)](netgdb.4.md) 会话。`netgdb` 具有与 `netdump` 相同的限制。
**`capture on`**
**`capture off`**
**`capture reset`**
**`capture status`** `vmstat` 支持基本的输出捕获设施，可用于使用 sysctl(3) 从用户空间检索调试命令的结果。`capture on` 启用输出捕获；`capture off` 禁用捕获。`capture reset` 将清除捕获缓冲区并禁用捕获。`capture status` 将报告当前缓冲区使用情况、缓冲区大小和输出捕获的处理方式。用户空间进程可使用 [sysctl(8)](../man8/sysctl.8.md) 检查和管理 `vmstat` 捕获状态：`debug.ddb.capture.bufsize` 可用于查询或设置当前捕获缓冲区大小。`debug.ddb.capture.maxbufsize` 可用于查询编译时对捕获缓冲区大小的限制。`debug.ddb.capture.bytes` 可用于查询当前捕获缓冲区中的输出字节数。`debug.ddb.capture.data` 将缓冲区内容作为字符串返回给具有适当权限的进程。此设施与脚本和 [textdump(4)](textdump.4.md) 设施配合使用特别有用，允许脚本化的调试输出被捕获并作为 textdump 的一部分提交到磁盘以供日后分析。还可使用 kgdb(1)（`ports/devel/gdb`）在内核核心转储中检查捕获缓冲区的内容。
**`run`**
**`script`**
**`scripts`**
**`unscript`** 运行、定义、列出和删除脚本。有关脚本设施的更多信息，请参见 Sx SCRIPTING 节。
**`textdump dump`**
**`textdump set`**
**`textdump status`**
**`textdump unset`** 使用 `textdump dump` 命令立即执行 textdump。更多信息可在 [textdump(4)](textdump.4.md) 中找到。`textdump set` 命令可用于强制将下一个内核核心转储设为 textdump 而非传统内存转储或小转储。`textdump status` 报告是否已计划 textdump。`textdump unset` 取消将 textdump 作为下一个内核核心转储执行的请求。

## 变量

调试器以 `$``name` 的形式访问寄存器和变量。寄存器名称与“`show` `registers`”命令中的相同。某些变量后缀有数字，并可能在变量名之后紧跟冒号后有某些修饰符。例如，寄存器变量可以有 `u` 修饰符以指示用户寄存器（例如“`$eax:u`）”。

当前支持的内置变量有：

**`radix`** 输入和输出基数。
**`maxoff`** 地址以“`symbol``+``offset`”形式打印，除非 `offset` 大于 `maxoff`。
**`maxwidth`** 显示行的宽度。
**`lines`** 行数。由内置分页器使用。设置为 0 可禁用分页。
**`tabstops`** 制表位宽度。
**`work`** `xx` 工作变量；`xx` 可取 0 到 31 的值。

## 表达式

支持 C 中的大多数表达式运算符，但不支持 `~`、`^` 和一元 `&`。`vmstat` 中的特殊规则：

**标识符** 符号的名称转换为该符号的值，即相应对象的地址。`.` 和 `:` 可用于标识符。如果对象格式相关例程支持，则 [`filename`: ]`func : lineno`,] [`filename`: ]`variable`,] 和 [`filename`: ]`lineno`] 可作为符号接受。

**数字** 基数由前两个字母确定：`0x`：十六进制，`0o`：八进制，`0t`：十进制；否则遵循当前基数。

**`.`** `dot`

**`+`** `next`

**`..`** 最后检查行的起始地址。与 `dot` 或 `next` 不同，这仅由 `examine` 或 `write` 命令更改。

**`'`** 最后明确指定的地址。

**`$`** `variable` 转换为指定变量的值。其后可跟 `:` 和如上所述的修饰符。

**`a`** `#``b` 二元运算符，将左侧向上取整到右侧的下一个倍数。

**`*`** `expr` 间接。其后可跟 `:` 和如上所述的修饰符。

## 脚本

`vmstat` 支持基本的脚本设施，以允许自动化任务或对特定事件的响应。每个脚本由一系列按顺序执行的 DDB 命令组成，并被分配一个唯一的名称。某些脚本名称具有特殊含义，如果已定义了这些名称的脚本，则会在各种 `vmstat` 事件上自动运行。

`script` 命令可用于按名称定义脚本。脚本由一系列用 `;` 字符分隔的 `vmstat` 命令组成。例如：

```sh
script kdb.enter.panic=bt; show pcpu
script lockinfo=show alllocks; show lockedvnods
```

`scripts` 命令列出当前已定义的脚本。

`run` 命令按名称执行脚本。例如：

```sh
run lockinfo
```

`unscript` 命令可用于按名称删除脚本。例如：

```sh
unscript kdb.enter.panic
```

这些功能也可使用 ddb(8) 命令从用户空间执行。

如果已定义，某些脚本会在特定的 `vmstat` 事件上自动运行。当各种事件发生时，会运行以下脚本：

**`kdb.enter.acpi`** 内核调试器由于 [acpi(4)](acpi.4.md) 事件而进入。

**`kdb.enter.bootflags`** 内核调试器由于设置了调试器引导标志而在引导时进入。

**`kdb.enter.break`** 内核调试器由于串行或控制台中断而进入。

**`kdb.enter.cam`** 内核调试器由于 CAM(4) 事件而进入。

**`kdb.enter.mac`** 内核调试器由于 TrustedBSD MAC 框架的 [mac_test(4)](mac_test.4.md) 模块中的断言失败而进入。

**`kdb.enter.netgraph`** 内核调试器由于 [netgraph(4)](netgraph.4.md) 事件而进入。

**`kdb.enter.panic`** 调用了 [panic(9)](../man9/panic.9.md)。

**`kdb.enter.powerpc`** 内核调试器由于 powerpc 平台上未实现的中断类型而进入。

**`kdb.enter.sysctl`** 内核调试器由于设置了 `debug.kdb.enter` sysctl 而进入。

**`kdb.enter.unionfs`** 内核调试器由于 union 文件系统中的断言失败而进入。

**`kdb.enter.unknown`** 内核调试器已进入，但未设置原因。

**`kdb.enter.vfslock`** 内核调试器由于 VFS 锁违规而进入。

**`kdb.enter.watchdog`** 内核调试器由于 watchdog 触发而进入。

**`kdb.enter.witness`** 内核调试器由于 [witness(4)](witness.4.md) 违规而进入。

如果未找到这些脚本中的任何一个，`vmstat` 将尝试执行默认脚本：

**`kdb.enter.default`** 内核调试器已进入，但未定义与进入原因完全匹配的脚本。这可用于作为处理不特别关注的情况的全能捕获；例如，可定义 `kdb.enter.witness` 进行特殊处理，而定义 `kdb.enter.default` 简单地 panic 并重新引导。

## 提示

在具有 ISA 扩展总线的机器上，可通过在 A01 和 B01（CHCHK# 和 GND）卡指之间连接一个按钮来构建简单的 NMI 生成卡。瞬时短接这两个指可能会使桥接芯片组生成 NMI，这会导致内核将控制权传递给 `vmstat`。某些桥接芯片组不会在 CHCHK# 上生成 NMI，因此效果可能因情况而异。NMI 允许在死锁的机器上进入调试器以诊断问题。其他总线的桥接芯片组可能能够使用总线特定方法生成 NMI。有许多 PCI 和 PCIe 附加卡可生成 NMI 用于调试。现代服务器系统通常使用 IPMI 生成信号以进入调试器。可使用 `devel/ipmitool` port 发送 `chassis power diag` 命令，该命令向处理器传递 NMI。嵌入式系统通常使用 JTAG 进行调试，但很少与 `vmstat` 结合使用。

串行控制台可通过在串行线上发送 BREAK 条件来中断到调试器。这需要在内核中指定 `options BREAK_TO_DEBUGGER` 构建的内核。大多数终端仿真程序可通过特殊的按键序列或菜单选择发送中断序列。在某些设置中，发送中断可能很困难甚至偶然发生。另一种方法是构建带 `options ALT_BREAK_TO_DEBUGER` 的内核，然后 CR TILDE CTRL-B 序列进入调试器；CR TILDE CTRL-P 引起 panic；CR TILDE CTRL-R 引起立即重新引导。在所有这些序列中，CR 表示回车，通常通过按 Enter 或 Return 键发送。TILDE 是 ASCII 波浪号字符（~）。CTRL-x 是 Control x，通过按 Control 键，然后按 x，然后释放两者来发送。

可通过将 [sysctl(8)](../man8/sysctl.8.md) `debug.kdb.break_to_debugger` 设置为 1 来启用 break-to-debugger 行为。可通过将 [sysctl(8)](../man8/sysctl.8.md) `debug.kdb.alt_break_to_debugger` 设置为 1 来启用 alt-break-to-debugger 行为。可通过将 [sysctl(8)](../man8/sysctl.8.md) `debug.kdb.enter` 设置为 1 来进入调试器。

可使用控制字符 CTRL-C、CTRL-S 和 CTRL-Q 中断、暂停和恢复输出。由于这些控制字符作为带内数据从控制台接收，因此存在输入缓冲区，一旦缓冲区填满，`vmstat` 必须停止响应控制字符或在继续搜索控制字符时丢弃额外输入。此行为由可调参数 [sysctl(8)](../man8/sysctl.8.md) `debug.ddb.prioritize_control_input` 控制，默认为 1。输入缓冲区大小为 512 字节。

## 文件

本手册页中提到的头文件可在 **/usr/include** 目录下找到。

- `sys/buf.h`
- `sys/domain.h`
- `netinet/in_pcb.h`
- `sys/socket.h`
- `sys/vnode.h`

## 参见

gdb(1)（`ports/devel/gdb`）、kgdb(1)（`ports/devel/gdb`）、[acpi(4)](acpi.4.md)、CAM(4)、[gdb(4)](gdb.4.md)、[mac_ddb(4)](mac_ddb.4.md)、[mac_test(4)](mac_test.4.md)、[netgraph(4)](netgraph.4.md)、[textdump(4)](textdump.4.md)、[witness(4)](witness.4.md)、ddb(8)、[sysctl(8)](../man8/sysctl.8.md)、[panic(9)](../man9/panic.9.md)

## 历史

`vmstat` 调试器最初为 Mach 开发，并移植到 386BSD。本手册页由 Garrett Wollman 从 man(7) 宏翻译。

Robert N. M. Watson 在 FreeBSD 7.1 中添加了对 `vmstat` 输出捕获、[textdump(4)](textdump.4.md) 和脚本的支持。
