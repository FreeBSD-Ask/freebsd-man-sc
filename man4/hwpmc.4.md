# hwpmc(4)

`hwpmc` — 硬件性能监控计数器支持

## 名称

`hwpmc`

## 概要

`内核配置文件中必须存在以下选项：`

> options HWPMC_HOOKS

`此外，对于 i386 系统：`

> device apic

`要在引导时以模块形式加载此驱动：`

```sh
sysrc kld_list+=hwpmc
```

`或者，要将此驱动编译进内核：`

> device hwpmc

`要启用调试功能（参见 Sx DEBUGGING ）`

> options KTR
> options KTR_COMPILE=(KTR_SUBSYS)
> options KTR_MASK=(KTR_SUBSYS)
> options HWPMC_DEBUG

## 描述

`hwpmc` 驱动虚拟化现代 CPU 中的硬件性能监控设施，并支持从用户级进程使用这些设施。

该驱动支持多处理器系统。

PMC 通过 `PMC_OP_PMCALLOCATE` 请求分配。成功的 `PMC_OP_PMCALLOCATE` 请求将向请求进程返回一个句柄。对已分配 PMC 的后续操作使用此句柄来表示特定的 PMC。成功分配了 PMC 的进程称为"所有者进程"。

PMC 可以以进程或系统作用域分配。

***进程作用域*** PMC 仅在其附加到的进程的线程被调度到 CPU 上时才处于活动状态。

***系统作用域*** PMC 独立于进程运行，测量系统整体的硬件事件。

PMC 可以分配用于计数或采样：

***计数*** 在计数模式下，PMC 计数硬件事件。这些计数可在所有架构上通过 `PMC_OP_PMCREAD` 系统调用检索。某些架构提供更快的读取这些计数的方法。

***采样*** 在采样模式下，PMC 被配置为在观察到可配置数量的硬件事件后，对 CPU 指令指针进行采样（并可选地捕获导致采样指令指针的调用链）。指令指针采样和调用链记录通常被定向到日志文件以供后续分析。

作用域和操作模式是正交的；因此，PMC 可配置为以以下四种模式之一运行：

**进程作用域，** 计数 这些 PMC 在其附加进程中的线程被调度到 CPU 上时计数硬件事件。这些 PMC 通常从零开始计数，但可使用 `PMC_OP_SETCOUNT` 操作设置初始计数。应用程序可随时使用 `PMC_OP_PMCRW` 操作读取 PMC 的值。

**进程作用域，** 采样 这些 PMC 在观察到配置数量的硬件事件后，对目标进程的指令指针进行采样。PMC 仅在其附加进程的线程处于活动状态时计数事件。所需采样频率在启动 PMC 前使用 `PMC_OP_SETCOUNT` 操作设置。日志文件通过 `PMC_OP_CONFIGURELOG` 操作配置。

**系统作用域，** 计数 这些 PMC 计数其观察到的硬件事件，与正在执行的进程无关。这些 PMC 的当前计数可通过 `PMC_OP_PMCRW` 请求读取。这些 PMC 通常从零开始计数，但可使用 `PMC_OP_SETCOUNT` 操作设置初始计数。

**系统作用域，** 采样 这些 PMC 将定期对其分配所在 CPU 的指令指针进行采样，并将采样写入日志以供进一步处理。所需采样频率在启动 PMC 前使用 `PMC_OP_SETCOUNT` 操作设置。日志文件通过 `PMC_OP_CONFIGURELOG` 操作配置。全系统统计采样只能由具有超级用户权限的进程启用。

允许进程在硬件和当前操作条件允许的范围内分配任意数量的 PMC。进程可以混合分配全系统 PMC 和进程私有 PMC。多个进程可以同时使用 PMC。

已分配的 PMC 使用 `PMC_OP_PMCSTART` 操作启动，使用 `PMC_OP_PMCSTOP` 操作停止。只要所有者进程持有有效的 PMC 句柄，就允许随时停止和启动 PMC。

进程私有 PMC 在使用前需要附加到目标进程。使用 `PMC_OP_PMCATTACH` 操作将进程附加到 PMC。已附加的 PMC 可使用反向的 `PMC_OP_PMCDETACH` 操作从其目标进程分离。对尚未附加的 PMC 发出 `PMC_OP_PMCSTART` 操作将导致其附加到所有者进程。以下规则确定给定进程是否可以将 PMC 附加到另一个目标进程：

- 具有超级用户权限的非 jail 进程可以附加到系统中的任何其他进程。
- 其他进程只能附加到它们能够进行调试附加的目标（由 [p_candebug(9)](../man9/p_candebug.9.md) 确定）。

PMC 通过 `PMC_OP_PMCRELEASE` 释放。成功的 `PMC_OP_PMCRELEASE` 操作后，PMC 的句柄将变为无效。

### 修饰符标志

`PMC_OP_PMCALLOCATE` 操作支持以下标志，用于修改已分配 PMC 的行为：

**`PMC_F_CALLCHAIN`** 此修饰符通知采样 PMC 在捕获采样时记录调用链。调用链记录的最大深度由 `kern.hwpmc.callchaindepth` 内核可调参数指定。

**`PMC_F_DESCENDANTS`** 此修饰符仅对以进程私有模式分配的 PMC 有效。它表示 PMC 将跟踪其目标进程及目标当前和将来后代进程的硬件事件。

**`PMC_F_LOG_PROCCSW`** 此修饰符仅对以进程私有模式分配的 PMC 有效。当存在此修饰符时，在每次上下文切换时，`hwpmc` 将记录一条包含目标进程被调度到 CPU 上时观察到的硬件事件数的记录。

**`PMC_F_LOG_PROCEXIT`** 此修饰符仅对以进程私有模式分配的 PMC 有效。存在此修饰符时，`hwpmc` 将为附加到 PMC 的每个目标进程维护每进程计数。在进程退出时，包含目标进程 PID 和该进程累积每进程计数的记录将被写入配置的日志文件。

修饰符 `PMC_F_LOG_PROCEXIT` 和 `PMC_F_LOG_PROCCSW` 可与修饰符 `PMC_F_DESCENDANTS` 组合使用，以跟踪复杂进程流水线的行为。带有 `PMC_F_LOG_PROCEXIT` 和 `PMC_F_LOG_PROCCSW` 修饰符的 PMC 在其所有者进程配置日志文件之前无法启动。

### 信号

`hwpmc` 驱动可向已分配 PMC 的进程传递信号：

**`SIGIO`** 对没有附加目标进程的进程私有 PMC 尝试了 `PMC_OP_PMCRW` 操作。

**`SIGBUS`** `hwpmc` 驱动正在从内核卸载。

### PMC 行配置

PMC 行定义为系统中各 CPU 中相同硬件地址处的 PMC 资源集合。由于进程作用域 PMC 需要跟随其目标线程在 CPU 之间移动，分配进程作用域 PMC 会保留 PMC 行中的所有 PMC 仅供进程作用域 PMC 使用。因此，PMC 行将处于以下配置之一：

**`PMC_DISP_FREE`** 此行中的硬件计数器空闲，可用于满足系统作用域或进程作用域分配请求。

**`PMC_DISP_THREAD`** 此行中的硬件计数器正被进程作用域 PMC 使用，仅可用于进程作用域分配请求。

**`PMC_DISP_STANDALONE`** 此行中的某些硬件计数器已被管理性禁用或正被系统作用域 PMC 使用。此行中未禁用的硬件计数器可用于满足系统作用域分配请求。不会有进程作用域 PMC 使用此行中的硬件计数器。

## 兼容性

本手册页中记录的 API 和 ABI 可能会在未来发生变化。此接口旨在供 pmc(3) 库使用；其他使用者不受支持。针对 PMC 的应用程序应使用 pmc(3) 库 API。

## 编程 API

`hwpmc` 驱动使用加载到内核时动态分配的系统调用号运行。

`hwpmc` 驱动支持以下操作：

**`PMC_OP_CONFIGURELOG`** 为需要日志文件的 PMC 配置日志文件。`hwpmc` 驱动将异步写入日志数据到此文件。如果遇到错误，将停止日志记录，遇到的错误代码将被保存以供后续 `PMC_OP_FLUSHLOG` 请求检索。

**`PMC_OP_FLUSHLOG`** 将 `hwpmc` 内部缓冲的日志数据传输到配置的输出文件。此操作在写操作返回后返回给调用者。返回的错误代码反映 `hwpmc` 内部的任何待处理错误状态。

**`PMC_OP_GETCAPS`** 检索与特定 PMC 计数器关联的功能。某些功能可能仅限于特定索引（即并非在某个类中的所有计数器上都可用）。

**`PMC_OP_GETCPUINFO`** 检索有关系统最高可能 CPU 编号以及每个 CPU 可用的硬件性能监控计数器数量的信息。

**`PMC_OP_GETDRIVERSTATS`** 检索模块统计信息（用于分析 `hwpmc` 自身的行为）。

**`PMC_OP_GETMODULEVERSION`** 检索 API 的版本号。

**`PMC_OP_GETPMCINFO`** 检索给定 CPU 上 PMC 的当前状态信息。

**`PMC_OP_PMCADMIN`** 设置 `hwpmc` 驱动管理的硬件 PMC 的管理状态（即启用或禁用）。调用进程需要具有 `PRIV_PMC_MANAGE` 权限。

**`PMC_OP_PMCALLOCATE`** 分配和配置 PMC。成功分配后，返回 PMC 的句柄（32 位值）。

**`PMC_OP_PMCATTACH`** 将进程模式 PMC 附加到目标进程。当目标进程中的线程被调度到 CPU 上时，PMC 将处于活动状态。如果在 PMC 分配时指定了 `PMC_F_DESCENDANTS` 标志，则 PMC 将附加到目标进程的所有当前和将来后代进程。

**`PMC_OP_PMCDETACH`** 从目标进程分离 PMC。

**`PMC_OP_PMCRELEASE`** 释放 PMC。

**`PMC_OP_PMCRW`** 读写 PMC。此操作仅对以计数模式配置的 PMC 有效。

**`PMC_OP_SETCOUNT`** 设置初始计数（用于计数模式 PMC）或所需采样率（用于采样模式 PMC）。

**`PMC_OP_PMCSTART`** 启动 PMC。

**`PMC_OP_PMCSTOP`** 停止 PMC。

**`PMC_OP_WRITELOG`** 向日志文件中插入带时间戳的用户记录。

### i386 专用 API

某些 i386 系列 CPU 支持 RDPMC 指令，允许用户进程读取 PMC 值而无需调用 `PMC_OP_PMCRW` 操作。在此类 CPU 上，与已分配 PMC 关联的机器地址可通过 `PMC_OP_PMCX86GETMSR` 系统调用检索。

**`PMC_OP_PMCX86GETMSR`** 检索与给定 PMC 句柄关联的 MSR（机器特定寄存器）号。PMC 需要处于进程私有模式，分配时不带 `PMC_F_DESCENDANTS` 修饰符标志，且在调用时应仅附加到其所有者进程。

### amd64 专用 API

AMD64 CPU 支持 RDPMC 指令，允许用户进程读取 PMC 值而无需调用 `PMC_OP_PMCRW` 操作。与已分配 PMC 关联的机器地址可通过 `PMC_OP_PMCX86GETMSR` 系统调用检索。

**`PMC_OP_PMCX86GETMSR`** 检索与给定 PMC 句柄关联的 MSR（机器特定寄存器）号。PMC 需要处于进程私有模式，分配时不带 `PMC_F_DESCENDANTS` 修饰符标志，且在调用时应仅附加到其所有者进程。

## SYSCTL 变量和加载器可调参数

`hwpmc` 的行为受以下 [sysctl(8)](../man8/sysctl.8.md) 和 [loader(8)](../man8/loader.8.md) 可调参数影响：

**`kern.hwpmc.callchaindepth`**（整数，只读）每次采样捕获的最大调用链记录数。默认为 8。

**`kern.hwpmc.debugflags`**（字符串，读写）（仅当 `hwpmc` 驱动以 `-DDEBUG -` 编译时可用）控制 `hwpmc` 驱动调试消息的详细程度。

**`kern.hwpmc.hashsize`**（整数，只读）用于跟踪所有者和目标进程的哈希表行数。默认为 16。

**`kern.hwpmc.logbuffersize`**（整数，只读）`hwpmc` 日志功能使用的每个日志缓冲区的大小（千字节）。默认缓冲区大小为 256KB。最大值为 16MB。

**`kern.hwpmc.mincount`**（整数，读写）采样模式 PMC 的最小采样率。默认计数为 1000 个事件。

**`kern.hwpmc.mtxpoolsize`**（整数，只读）PMC 驱动使用的自旋互斥锁池大小。默认为 32。

**`kern.hwpmc.nbuffers_pcpu`**（整数，只读）`hwpmc` 用于日志记录的每 CPU 日志缓冲区数量。默认为 32。`kern.hwpmc.nbuffers_pcpu` 和 `kern.hwpmc.logbuffersize` 的乘积不得超过每 CPU 32MB。

**`kern.hwpmc.nsamples`**（整数，只读）采样期间使用的每 CPU 环形缓冲区中的条目数。默认为 512。

**`security.bsd.unprivileged_syspmcs`**（布尔值，读写）如果设置为非零值，允许非特权进程分配全系统 PMC。默认值为 0。

**`security.bsd.unprivileged_proc_debug`**（布尔值，读写）如果设置为 0，`hwpmc` 驱动将仅允许特权进程将 PMC 附加到其他进程。

这些变量可在 `hwpmc` 加载前使用 [kenv(1)](../man1/kenv.1.md) 在内核环境中设置。

## 实现说明

### SMP 对称性

内核驱动要求 SMP 系统中的所有物理 CPU 具有相同的性能监控计数器硬件。

### 稀疏 CPU 编号

在对 CPU 进行稀疏编号且支持 CPU 热插拔的平台上，指定不存在或已禁用 CPU 的请求将失败并返回错误。分配系统作用域 PMC 的应用程序需要了解这种临时故障的可能性。

### x86 TSC 处理

历史上，在 x86 架构上，FreeBSD 允许在处理器 CPL 为 3 下运行的用户进程使用 RDTSC 指令读取 TSC。`hwpmc` 驱动保留了此行为。

### Intel P4/HTT 处理

在支持 HTT 的 CPU 上，Intel P4 PMC 只能按逻辑 CPU 限定硬件事件的子集。因此，如果在具有 Intel Pentium P4 PMC 的系统上启用了 HTT，则 `hwpmc` 驱动将拒绝为请求计数无法按每个逻辑 CPU 单独计数的硬件事件的进程私有 PMC 分配请求。

## 诊断

- hwpmc: [class/npmc/capabilities]... 宣告存在 `npmc` 个类为 `class` 的 PMC，功能由位字符串 `capabilities` 描述。
- hwpmc: kernel version (0x%x) does not match module version (0x%x). 模块加载过程失败，因为检测到当前执行的内核与正在加载的模块之间存在版本不匹配。
- hwpmc: this kernel has not been compiled with 'options HWPMC_HOOKS'. 模块加载过程失败，因为当前执行的内核未配置所需的配置选项 `HWPMC_HOOKS`。
- hwpmc: tunable hashsize=%d must be greater than zero. 为可调参数 `kern.hwpmc.hashsize` 提供了负值。
- hwpmc: logbuffersize=%d must be greater than zero and less than or equal to %d, resetting to %d. 为可调参数 `kern.hwpmc.logbuffersize` 提供了负值。
- hwpmc: nbuffers_pcpu=%d must be greater than zero, resetting to %d. 为可调参数 `kern.hwpmc.nbuffers_pcpu` 提供了负值。
- hwpmc: tunable nsamples=%d out of range. 可调参数 `kern.hwpmc.nsamples` 的值为负或大于 65535。
- hwpmc: nbuffers_pcpu=%d *logbuffersize=%d exceeds %dMB per CPU limit, resetting to defaults (%d* %d). 可调参数 `kern.hwpmc.nbuffers_pcpu` 和 `kern.hwpmc.logbuffersize` 的乘积超过了每 CPU 最大内存限制。两个可调参数都重置为编译默认值。

## 调试

`hwpmc` 模块可配置为使用 [ktr(4)](ktr.4.md) 接口记录跟踪条目。这对于调试驱动功能很有用，主要用于开发期间。此调试功能默认未启用，需要在内核配置中添加以下内容后重新编译内核和 `hwpmc` 模块：

```sh
`options KTR`
`options KTR_COMPILE=(KTR_SUBSYS)`
`options KTR_MASK=(KTR_SUBSYS)`
`options HWPMC_DEBUG`
```

仅此一项不足以启用跟踪；还必须配置 `kern.hwpmc.debugflags` [sysctl(8)](../man8/sysctl.8.md) 变量，该变量提供对哪些类型的事件被记录到跟踪缓冲区的细粒度控制。

`hwpmc` 跟踪事件按"主要"和"次要"标志类型分组。主要标志名称如下：

**cpu** CPU 事件
**csw** 上下文切换事件
**logging** 日志事件
**md** 机器相关/类相关事件
**module** 杂项事件
**owner** PMC 所有者事件
**pmc** PMC 管理事件
**process** 进程事件
**sampling** 采样事件

每个主要标志组的次要标志可能不同。各个次要标志名称为：

> allocaterow,
> allocate,
> attach,
> bind,
> config,
> exec,
> exit,
> find,
> flush,
> fork,
> getbuf,
> hook,
> init,
> intr,
> linktarget,
> mayberemove,
> ops,
> read,
> register,
> release,
> remove,
> sample,
> scheduleio,
> select,
> signal,
> swi,
> swo,
> start,
> stop,
> syscall,
> unlinktarget,
> write

`kern.hwpmc.debugflags` 变量是具有自定义格式的字符串。该字符串应包含以空格分隔的事件说明符列表。每个事件说明符由主要标志名称、后跟等号（=）、后跟以逗号分隔的次要事件类型列表组成。要跟踪主要组的所有事件，可使用星号（*）代替次要事件名称。

例如，要跟踪所有分配和释放事件，按如下方式设置 `debugflags`：

```sh
kern.hwpmc.debugflags="pmc=allocate,release md=allocate,release"
```

要跟踪 process 和 context switch 主要标志组中的所有事件：

```sh
kern.hwpmc.debugflags="process=* csw=*"
```

要禁用所有跟踪事件，将变量设置为空字符串。

```sh
kern.hwpmc.debugflags=""
```

跟踪事件由 [ktr(4)](ktr.4.md) 记录，可在运行时使用 ktrdump(8) 工具检查，或在崩溃后通过 [ddb(4)](ddb.4.md) 提示符使用 'show ktr' 命令检查。

## 错误

向 `hwpmc` 驱动发出的命令可能因以下错误而失败：

**[EAGAIN]** 由于内核中临时资源不足，`PMC_OP_CONFIGURELOG` 请求的辅助进程创建失败。

**[EBUSY]** 在现有日志处于活动状态时请求了 `PMC_OP_CONFIGURELOG` 操作。

**[EBUSY]** 对当前用于进程私有 PMC 的硬件资源集请求使用 `PMC_OP_PMCADMIN` 的 DISABLE 操作。

**[EBUSY]** 对活动系统模式 PMC 请求了 `PMC_OP_PMCADMIN` 操作。

**[EBUSY]** 对已有另一个使用相同硬件资源的 PMC 附加到的目标进程请求了 `PMC_OP_PMCATTACH` 操作。

**[EBUSY]** 对处于活动状态的 PMC 发出了写入新值的 `PMC_OP_PMCRW` 请求。

**[EBUSY]** 对处于活动状态的 PMC 发出了 `PMC_OP_PMCSETCOUNT` 请求。

**[EDOOFUS]** 对以 `PMC_F_LOG_PROCCSW` 和 `PMC_F_LOG_PROCEXIT` 修饰符分配的 PMC 请求了 `PMC_OP_PMCSTART` 操作，但未配置日志文件。

**[EDOOFUS]** 对全系统采样 PMC 请求了 `PMC_OP_PMCSTART` 操作，但未配置日志文件。

**[EEXIST]** 对已经是此 PMC 目标的目标进程重新发出了 `PMC_OP_PMCATTACH` 请求。

**[EFAULT]** 向驱动传递了错误地址。

**[EINVAL]** 指定了无效的 PMC 句柄。

**[EINVAL]** 为 `PMC_OP_GETPMCINFO` 操作传入了无效的 CPU 编号。

**[EINVAL]** `PMC_OP_CONFIGURELOG` 请求的 `pm_flags` 参数包含未知标志。

**[EINVAL]** 在未配置日志文件的情况下发出了取消配置日志文件的 `PMC_OP_CONFIGURELOG` 请求。

**[EINVAL]** 在未配置日志文件的情况下发出了 `PMC_OP_FLUSHLOG` 请求。

**[EINVAL]** 为 `PMC_OP_PMCADMIN` 操作传入了无效的 CPU 编号。

**[EINVAL]** 为 `PMC_OP_PMCADMIN` 操作传入了无效的操作请求。

**[EINVAL]** 为 `PMC_OP_PMCADMIN` 操作传入了无效的 PMC ID。

**[EINVAL]** 无法分配与传入 `PMC_OP_PMCALLOCATE` 请求的参数匹配的合适 PMC。

**[EINVAL]** 在 `PMC_OP_PMCALLOCATE` 请求期间请求了无效的 PMC 模式。

**[EINVAL]** 在 `PMC_OP_PMCALLOCATE` 请求期间指定了无效的 CPU 编号。

**[EINVAL]** 在进程私有 PMC 的 `PMC_OP_PMCALLOCATE` 请求中指定了 `PMC_CPU_ANY` 以外的 CPU。

**[EINVAL]** 在全系统 PMC 的 `PMC_OP_PMCALLOCATE` 请求中指定了 `PMC_CPU_ANY` 的 CPU 编号。

**[EINVAL]** `PMC_OP_PMCALLOCATE` 请求的 `pm_flags` 参数包含未知标志。

**[EINVAL]**（在支持 HTT 的 Intel Pentium 4 CPU 上）对不支持按逻辑 CPU 计数的事件发出了进程私有 PMC 的 `PMC_OP_PMCALLOCATE` 请求。

**[EINVAL]** 对为全系统操作分配的 PMC 指定了 `PMC_OP_PMCATTACH` 或 `PMC_OP_PMCDETACH` 请求。

**[EINVAL]** `PMC_OP_PMCATTACH` 或 `PMC_OP_PMCDETACH` 请求的 `pm_pid` 参数指定了非法的进程 ID。

**[EINVAL]** 对未附加到目标进程的 PMC 发出了 `PMC_OP_PMCDETACH` 请求。

**[EINVAL]** `PMC_OP_PMCRW` 请求的参数 `pm_flags` 包含非法标志。

**[EINVAL]** 对非进程虚拟模式的 PMC、或并非仅附加到其所有者进程的 PMC、或以 `PMC_F_DESCENDANTS` 标志分配的 PMC 请求了 `PMC_OP_PMCX86GETMSR` 操作。

**[EINVAL]** 对未配置日志文件的所有者进程发出了 `PMC_OP_WRITELOG` 请求。

**[ENOMEM]** 系统无法分配内核内存。

**[ENOSYS]**（在 i386 和 amd64 架构上）对不支持使用 RDPMC 指令直接读取 PMC 的硬件请求了 `PMC_OP_PMCX86GETMSR` 操作。

**[ENXIO]** 对不存在或已禁用的 CPU 请求了 `PMC_OP_GETPMCINFO` 操作。

**[ENXIO]** `PMC_OP_PMCALLOCATE` 操作指定了在不存在或已禁用的 CPU 上分配全系统 PMC。

**[ENXIO]** 对分配在当前不存在或已禁用的 CPU 上的全系统 PMC 发出了 `PMC_OP_PMCSTART` 或 `PMC_OP_PMCSTOP` 请求。

**[EOPNOTSUPP]** 对指定 PMC 类不支持的 PMC 功能发出了 `PMC_OP_PMCALLOCATE` 请求。

**[EOPNOTSUPP]**（i386 架构）在不具备 APIC 的 CPU 上请求了采样模式 PMC。

**[EPERM]** 无超级用户权限的进程或 jail 中的超级用户进程发出了 `PMC_OP_PMCADMIN` 请求。

**[EPERM]** 对当前进程无权附加的目标进程发出了 `PMC_OP_PMCATTACH` 操作。

**[EPERM]**（i386 和 amd64 架构）对已使用 `PMC_OP_PMCX86GETMSR` 检索 MSR 的 PMC 发出了 `PMC_OP_PMCATTACH` 操作。

**[ESRCH]** 进程在未分配任何 PMC 的情况下发出了 PMC 操作请求。

**[ESRCH]** 进程在 PMC 从其所有目标进程分离后发出了 PMC 操作请求。

**[ESRCH]** `PMC_OP_PMCATTACH` 或 `PMC_OP_PMCDETACH` 请求指定了不存在的进程 ID。

**[ESRCH]** `PMC_OP_PMCDETACH` 操作的目标进程未被 `hwpmc` 监控。

## 参见

[kenv(1)](../man1/kenv.1.md), pmc(3), pmclog(3), [ddb(4)](ddb.4.md), [ktr(4)](ktr.4.md), [kldload(8)](../man8/kldload.8.md), ktrdump(8), [pmccontrol(8)](../man8/pmccontrol.8.md), [pmcstat(8)](../man8/pmcstat.8.md), [sysctl(8)](../man8/sysctl.8.md), kproc_create(9), [p_candebug(9)](../man9/p_candebug.9.md)

## 历史

`hwpmc` 驱动最早出现在 FreeBSD 6.0 中。

## 作者

`hwpmc` 驱动由 Joseph Koshy <jkoshy@FreeBSD.org> 编写。

## 缺陷

驱动在初始化时（即模块加载时）采样内核逻辑处理器支持的状态。在支持逻辑处理器的 CPU 上，如果随后在驱动处于活动状态时启用或禁用逻辑处理器，驱动可能会出现异常行为。

在 i386 架构上，驱动要求启用 CPU 上的本地 APIC 才能支持采样模式。许多单处理器主板在 BIOS 中保持 APIC 禁用；在此类系统上，`hwpmc` 将不支持采样 PMC。

## 安全注意事项

PMC 可用于监控系统在硬件上的实际行为。在此类信息泄漏构成不良情况时，可使用以下选项：

- 将 [sysctl(8)](../man8/sysctl.8.md) 可调参数 `security.bsd.unprivileged_syspmcs` 设置为 0。这确保非特权进程无法分配全系统 PMC，从而无法观察系统整体的硬件行为。此可调参数也可在引导时使用 [loader(8)](../man8/loader.8.md) 设置，或在将 `hwpmc` 驱动加载到内核前使用 [kenv(1)](../man1/kenv.1.md) 设置。
- 将 [sysctl(8)](../man8/sysctl.8.md) 可调参数 `security.bsd.unprivileged_proc_debug` 设置为 0。这将确保非特权进程无法将 PMC 附加到自身以外的任何进程，从而无法观察具有相同凭据的其他进程的硬件行为。

系统管理员应注意，在 IA-32 平台上，FreeBSD 通过 RDTSC 指令向所有进程提供 IA-32 TSC 计数器的内容。
