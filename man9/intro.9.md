# intro(9)

`intro` — 内核编程接口介绍

## 名称

`intro`

## 描述

欢迎阅读 FreeBSD 内核文档。除了源代码本身之外，这组 [man(1)](../man1/man.1.md) 手册页是了解内核中众多编程接口使用方法的主要资源。在某些情况下，它也是特定子系统或代码段背后实现细节和/或设计决策的事实来源。

本文档的目标读者是开发者，主要作者也是开发者。其编写假设读者对常见的编程或操作系统级概念和实践有一定了解。但是，本文档也应尝试提供足够的背景信息，使首次接触特定子系统或接口的读者能够理解。

为了进一步设定预期，我们承认内核文档和源代码一样，永远都是进行中的工作。代码库中会有大部分文档已经或多或少地过时，或者完全缺失。本文档是源代码的补充，不能总是按字面意思理解。

在最佳情况下，第 9 节文档会提供对特定代码段的描述，配合其实现，向读者充分传达预期和实际的效果。

本节的 [man(1)](../man1/man.1.md) 手册页最常描述函数，但也可以描述类型、全局变量、宏或高级概念。

## 编码指南

为 FreeBSD 内核编写的代码应遵循既定的风格和编码约定。详细规则和指南请参阅 [style(9)](style.9.md)。

## 概览

下面介绍各个子系统。

### 数据结构

内核中有许多知名数据结构的实现。

**[bitstring(3)](../man3/bitstring.3.md)** 简单位图实现。

**[counter(9)](counter.9.md)** SMP 安全的通用计数器实现。

**[hash(9)](hash.9.md)** 哈希映射实现。

**[nv(9)](nv.9.md)** 名称/值对。

**[queue(3)](../man3/queue.3.md)** 单链表、双链表和队列。

**[refcount(9)](refcount.9.md)** SMP 安全的引用计数实现。

**[sbuf(9)](sbuf.9.md)** 动态字符串组合。

**[sglist(9)](sglist.9.md)** 分散/聚集列表实现。

### 实用函数

通用或便利的函数或设施。另请参阅下面的测试和调试工具或杂项小节。

格式化输出和日志函数由 [printf(9)](printf.9.md) 描述。

字节序交换函数：[byteorder(9)](byteorder.9.md)。

十六进制格式的数据输出：[hexdump(9)](hexdump.9.md)。

一组用于声明 [sysctl(8)](../man8/sysctl.8.md) 变量和函数的丰富宏由 [sysctl(9)](sysctl.9.md) 描述。

内核中的不可恢复错误应触发 [panic(9)](panic.9.md)。运行时断言可以使用 [KASSERT(9)](kassert.9.md) 宏进行验证。编译时断言应使用 `_Static_assert`。

SYSINIT 框架提供了用于声明在启动和关闭期间执行的函数的宏；参见 [SYSINIT(9)](sysinit.9.md)。

弃用消息可以使用 [gone_in(9)](gone_in.9.md) 发出。

单元号设施由 [unr(9)](unr.9.md) 提供。

### 同步原语

[locking(9)](locking.9.md) 手册页概述了内核中可用的各种锁类型及其使用建议。

原子原语由 [atomic(9)](atomic.9.md) 描述。

[epoch(9)](epoch.9.md) 和 [smr(9)](smr.9.md) 设施用于创建无锁数据结构。此外还有 [seqc(9)](seqc.9.md)。

### 内存管理

内核内的动态内存分配通常使用 [malloc(9)](malloc.9.md)。频繁分配的对象可能更倾向于使用 uma(9)。

虚拟内存系统的大部分操作在 `vm_page_t` 结构上进行。以下函数已有文档：

> vm_page_advise(9),
> [vm_page_aflag(9)](vm_page_aflag.9.md),
> [vm_page_alloc(9)](vm_page_alloc.9.md),
> [vm_page_bits(9)](vm_page_bits.9.md),
> [vm_page_busy(9)](vm_page_busy.9.md),
> [vm_page_deactivate(9)](vm_page_deactivate.9.md),
> [vm_page_free(9)](vm_page_free.9.md),
> [vm_page_grab(9)](vm_page_grab.9.md),
> [vm_page_insert(9)](vm_page_insert.9.md),
> [vm_page_lookup(9)](vm_page_lookup.9.md),
> [vm_page_rename(9)](vm_page_rename.9.md),
> vm_page_sbusy(9),
> [vm_page_wire(9)](vm_page_wire.9.md)

虚拟地址空间映射通过 [vm_map(9)](vm_map.9.md) API 管理。

虚拟内存栈的机器相关部分是 [pmap(9)](pmap.9.md) 模块。

NUMA 内存域的分配策略通过 [domainset(9)](domainset.9.md) API 管理。

### 文件系统

文件系统的内核接口是 [VFS(9)](vfs.9.md)。文件系统实现通过 [vfsconf(9)](vfsconf.9.md) 注册自身。

[vnode(9)](vnode.9.md) 是文件、目录或其他类文件实体在内核中的抽象且独立于文件系统的表示。

文件系统访问控制列表的实现由 [acl(9)](acl.9.md) 描述。还有 [vaccess(9)](vaccess.9.md)。

### I/O 和存储

GEOM 框架使用 bio(9) 结构表示 I/O 请求。

磁盘驱动程序使用 [disk(9)](disk.9.md) API 将自身连接到 GEOM。

[devstat(9)](devstat.9.md) 设施提供了在磁盘驱动程序中记录设备统计信息的接口。

### 网络

网络栈的大部分使用 [mbuf(9)](mbuf.9.md)，这是一种灵活的内存管理单元，通常用于存储网络数据包。

网络接口使用 [ifnet(9)](ifnet.9.md) API 实现，该 API 提供了面向驱动程序和使用者的函数。

管理数据包输出队列的框架由 [altq(9)](altq.9.md) 描述。

为接收传入数据包，网络协议通过 [netisr(9)](netisr.9.md) 注册自身。

网络栈的虚拟化由 [VNET(9)](vnet.9.md) 提供。

从内核内与网络套接字接口的前端由 [socket(9)](socket.9.md) 描述。套接字实现的后端接口是 [domain(9)](domain.9.md)。

低层数据包过滤接口由 [pfil(9)](pfil.9.md) 描述。

[bpf(9)](bpf.9.md) 接口提供了将数据包重定向到用户空间的机制。

IEEE 802.11 无线网络子系统由 [ieee80211(9)](ieee80211.9.md) 描述。

模块化 TCP 实现的框架由 [tcp_functions(9)](tcp_functions.9.md) 描述。

模块化拥塞控制算法的框架由 [mod_cc(9)](mod_cc.9.md) 描述。

### 设备驱动程序

请先参阅 [device(9)](device.9.md) 和 [driver(9)](driver.9.md) 页面。

大多数驱动程序充当设备，并提供一组实现设备接口的方法。这包括 [DEVICE_PROBE(9)](device_probe.9.md)、[DEVICE_ATTACH(9)](device_attach.9.md) 和 [DEVICE_DETACH(9)](device_detach.9.md) 等方法。

除了设备之外，还有总线。总线可以有子设备，形式为设备或其他总线。总线驱动程序将实现附加方法，如 [BUS_ADD_CHILD(9)](bus_add_child.9.md)、[BUS_READ_IVAR(9)](bus_read_ivar.9.md) 或 [BUS_RESCAN(9)](bus_rescan.9.md)。

总线通常代表其子设备执行资源核算。为此有 [rman(9)](rman.9.md) API。

驱动程序可以使用以下函数集从其父设备请求和管理资源（例如内存空间或 IRQ 号）：

> [bus_alloc_resource(9)](bus_alloc_resource.9.md),
> [bus_adjust_resource(9)](bus_adjust_resource.9.md),
> [bus_get_resource(9)](bus_get_resource.9.md),
> [bus_map_resource(9)](bus_map_resource.9.md),
> [bus_release_resource(9)](bus_release_resource.9.md),
> [bus_set_resource(9)](bus_set_resource.9.md)

直接内存访问（DMA）使用 busdma(9) 框架处理。

访问总线空间（即读/写）的函数由 [bus_space(9)](bus_space.9.md) 提供。

### 时钟和计时

内核时钟频率和整体系统时间模型由 [hz(9)](hz.9.md) 描述。

一些全局时间变量，如系统正常运行时间，由 [time(9)](time.9.md) 描述。

原始 CPU 周期由 [get_cyclecount(9)](get_cyclecount.9.md) 提供。

### 用户空间内存访问

不允许从内核直接读/写用户空间内存，跨越内核/用户边界的内存事务必须通过为此任务构建的多个接口之一进行。

大多数设备驱动程序使用 uiomove(9) 例程集。

用于读/写较小内存块的更简单原语由 [casuword(9)](casuword.9.md)、[copy(9)](copy.9.md)、[fetch(9)](fetch.9.md) 和 [store(9)](store.9.md) 描述。

### 内核线程、任务和回调

内核线程和进程分别使用 [kthread(9)](kthread.9.md) 和 [kproc(9)](kproc.9.md) 接口创建。

在专用内核线程过于重量级的情况下，还有 [taskqueue(9)](taskqueue.9.md) 接口。

对于低延迟回调处理，应使用 [callout(9)](callout.9.md) 框架。

预定义事件钩子的动态处理程序使用 [EVENTHANDLER(9)](eventhandler.9.md) API 注册和调用。

### 线程切换和调度

上下文切换的机器无关接口是 [mi_switch(9)](mi_switch.9.md)。

要防止抢占，请使用 critical(9) 临界区。

要自愿让出处理器，请使用 [kern_yield(9)](kern_yield.9.md)。

故意使线程睡眠的各种函数由 [sleep(9)](sleep.9.md) 描述。睡眠线程从调度器中移除并放置在 [sleepqueue(9)](sleepqueue.9.md) 上。

### 进程和信号

要通过标识符定位进程或进程组，请使用 [pfind(9)](pfind.9.md) 和 [pgfind(9)](pgfind.9.md)。或者，[pget(9)](pget.9.md) 函数提供额外的搜索精确度。

进程的"持有计数"可以通过 [PHOLD(9)](phold.9.md) 操作。

信号的内核接口由 [signal(9)](signal.9.md) 描述。

可以使用 [psignal(9)](psignal.9.md) 描述的函数向进程或进程组发送信号。

### 安全

请参阅 [security(7)](../man7/security.7.md) 中的概述。

用户凭证的基本结构是 `struct ucred`，由 [ucred(9)](ucred.9.md) API 管理。线程凭证使用 [priv(9)](priv.9.md) 验证，以允许或拒绝某些特权操作。

受 `kern.securelevel` 影响的策略必须使用 [securelevel_gt(9)](securelevel_gt.9.md) 或 securelevel_ge(9) 函数。

强制访问控制（MAC）框架提供了广泛的钩子集，支持动态注册的安全模块；参见 [mac(9)](mac.9.md)。

加密服务由 OpenCrypto 框架提供。此 API 为使用者和加密驱动程序都提供了接口；参见 [crypto(9)](crypto.9.md)。

有关随机数生成的信息，请参阅 [random(9)](random.9.md) 和 [prng(9)](prng.9.md)。

### 内核模块

声明可加载内核模块的接口由 [module(9)](module.9.md) 描述。

### 中断

[intr_event(9)](intr_event.9.md) 描述了中断框架的机器无关部分，支持中断处理程序的注册和执行。

软件中断由 [swi(9)](swi.9.md) 提供。

设备驱动程序使用 bus_setup_intr(9) 函数注册其中断处理程序。

### 测试和调试工具

内核测试框架：[kern_testfrwk(9)](kern_testfrwk.9.md)

用于定义可配置故障点的设施由 [fail(9)](fail.9.md) 描述。

[ddb(4)](../man4/ddb.4.md) 内核调试器的命令通过 [DB_COMMAND(9)](db_command.9.md) 宏系列定义。

[ktr(4)](../man4/ktr.4.md) 跟踪设施在内核的许多区域添加静态跟踪点。这些跟踪点使用 [ktr(9)](ktr.9.md) 描述的宏定义。

DTrace 的静态探针使用 [SDT(9)](sdt.9.md) 宏定义。

堆栈跟踪可以通过 [stack(9)](stack.9.md) API 捕获和打印。

内核消毒器可以针对内存使用/访问执行额外的编译器辅助检查。这些运行时能够检测难以识别的 bug 类别，代价是较大的开销。支持内核地址消毒器 KASAN(9) 和内核内存消毒器 KMSAN(9)。

[LOCK_PROFILING(9)](lock_profiling.9.md) 内核配置选项启用额外代码以协助分析和/或调试锁性能。

### 驱动程序工具

为特定类型设备定义的函数/API。

**[iflib(9)](iflib.9.md)** 基于 [iflib(4)](../man4/iflib.4.md) 的网络驱动程序的编程接口。

**[pci(9)](pci.9.md)** 外围组件互连（PCI）和 PCI Express（PCIe）编程 API。

**[pwmbus(9)](pwmbus.9.md)** 脉宽调制（PWM）总线接口方法。

**[usbdi(9)](usbdi.9.md)** 通用串行总线编程接口。

**[superio(9)](superio.9.md)** Super I/O 控制器设备的函数。

### 杂项

动态每 CPU 变量：[dpcpu(9)](dpcpu.9.md)。

CPU 位图管理：[cpuset(9)](cpuset.9.md)。

内核环境管理：[getenv(9)](getenv.9.md)。

CPU 浮点寄存器的上下文由 [fpu_kern(9)](fpu_kern.9.md) 设施管理。

有关关闭/重启过程和可用关闭钩子的详细信息，请参阅 reboot(9)。

从内核内异步记录到文件的设施由 [alq(9)](alq.9.md) 提供。

[osd(9)](osd.9.md) 框架提供了一种以保持 KBI 的方式动态扩展核心结构的机制。有关其使用方式，请参阅 [hhook(9)](hhook.9.md) 和 [khelp(9)](khelp.9.md) API。

内核对象实现由 [kobj(9)](kobj.9.md) 描述。

## 参见

[man(1)](../man1/man.1.md), [style(9)](style.9.md)

> "The FreeBSD Architecture Handbook".
