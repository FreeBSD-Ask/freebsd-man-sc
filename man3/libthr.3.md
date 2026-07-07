# libthr(3)

`libthr` — 1:1 POSIX 线程库

## 名称

`libthr`

## 库

Lb libthr

## 概要

`#include <pthread.h>`

## 描述

`libthr` 库为应用程序线程提供了 [pthread(3)](pthread.3.md) 库接口的 1:1 实现。它针对期望系统范围线程语义的应用程序进行了优化。

该库与运行时链接编辑器 ld-elf.so.1(1) 以及 Lb libc 紧密集成；这三个组件必须从同一源代码树构建。它们共同构成 FreeBSD 的基础 C 运行时环境，运行于 FreeBSD 内核之上。

不支持混用来自不同 FreeBSD 版本的 `libc` 和 `libthr` 库。运行时链接器 ld-elf.so.1(1) 包含一些代码以确保与旧版 `libthr` 的向后兼容性。

本手册页记录了 `libthr` 的特殊行为和可调参数。当使用 `-lpthread` 链接时，运行时依赖 `libthr.so.3` 会被记录在生成的目标文件中。

## 互斥锁获取

已锁定的互斥锁（参见 [pthread_mutex_lock(3)](pthread_mutex_lock.3.md)）由 `lwpid_t` 类型的 volatile 变量表示，该变量记录持有锁的线程的全局系统标识符。`libthr` 分三个阶段执行竞争互斥锁的获取，每个阶段比前一个阶段消耗更多资源。前两个阶段仅适用于 `PTHREAD_MUTEX_ADAPTIVE_NP` 类型和 `PTHREAD_PRIO_NONE` 协议的互斥锁（参见 [pthread_mutexattr(3)](pthread_mutexattr.3.md)）。

首先，在 SMP 系统上，执行自旋循环，库尝试通过 [atomic(9)](../man9/atomic.9.md) 操作获取锁。循环次数由 `LIBPTHREAD_SPINLOOPS` 环境变量控制，默认值为 2000。

如果自旋循环未能获取互斥锁，则执行让步循环，执行与自旋循环相同的 [atomic(9)](../man9/atomic.9.md) 获取尝试，但每次尝试后通过 [sched_yield(2)](../sys/sched_yield.2.md) 系统调用让出线程的 CPU 时间。默认情况下不执行让步循环。这由 `LIBPTHREAD_YIELDLOOPS` 环境变量控制。

如果自旋和让步循环均未能获取锁，则线程被移出 CPU 并通过 [_umtx_op(2)](../sys/_umtx_op.2.md) 系统调用在内核中休眠。当锁可用时，内核唤醒线程并将锁的所有权移交给被唤醒的线程。

## 线程栈

每个线程都有一个私有的用户态栈区域，供 C 运行时使用。主（初始）线程栈的大小由内核设置，并受 `RLIMIT_STACK` 进程资源限制控制（参见 [getrlimit(2)](../sys/getrlimit.2.md)）。

默认情况下，主线程的栈大小等于该进程的 `RLIMIT_STACK` 值。如果进程环境中存在 `LIBPTHREAD_SPLITSTACK_MAIN` 环境变量（其值无关紧要），则在线程库初始化时，主线程的栈在 64 位体系结构上缩减为 4MB，在 32 位体系结构上缩减为 2MB。在这种情况下，内核为初始进程栈保留的地址空间区域的其余部分用于非初始线程栈。`LIBPTHREAD_BIGSTACK_MAIN` 环境变量的存在会覆盖 `LIBPTHREAD_SPLITSTACK_MAIN`；保留它是为了向后兼容。

通过 [pthread_create(3)](pthread_create.3.md) 调用在运行时创建的线程的栈大小由线程属性控制：参见 [pthread_attr(3)](pthread_attr.3.md)，特别是 pthread_attr_setstacksize(3)、pthread_attr_setguardsize(3) 和 pthread_attr_setstackaddr(3) 函数。如果未指定线程栈大小的属性，则默认的非初始线程栈大小在 64 位体系结构上为 2MB，在 32 位体系结构上为 1MB。

## 运行时设置

`libthr` 识别以下环境变量，并在运行时调整库的操作：

**`LIBPTHREAD_BIGSTACK_MAIN`** 禁用由 `LIBPTHREAD_SPLITSTACK_MAIN` 启用的初始线程栈缩减。

**`LIBPTHREAD_SPLITSTACK_MAIN`** 导致初始线程栈缩减，如“线程栈”一节所述。这是 FreeBSD 11.0 之前 `libthr` 的默认行为。

**`LIBPTHREAD_SPINLOOPS`** 该变量的整数值覆盖互斥锁获取过程中 `spin loop` 的默认迭代次数。默认次数为 2000，由 `libthr` 源代码中的 `MUTEX_ADAPTIVE_SPINS` 常量设置。

**`LIBPTHREAD_YIELDLOOPS`** 非零整数值在互斥锁获取过程中启用让步循环。该值为循环操作次数。

**`LIBPTHREAD_QUEUE_FIFO`** 该变量的整数值指定阻塞线程被插入到睡眠队列头部而非尾部的频率。较大的值会降低 FIFO 策略的频率。该值必须介于 0 和 255 之间。

**`LIBPTHREAD_UMTX_MIN_TIMEOUT`** 线程为指定超时的 pthread 操作所需休眠的最短时间（以纳秒为单位）。如果操作请求的超时小于所提供的值，则会静默地增加到该值。值为零表示没有最小值（默认）。

以下 `sysctl` MIB 影响库的操作：

**`kern.ipc.umtx_vnode_persistent`** 默认情况下，由内存中映射文件支持的共享锁在对应文件页面的最后一次取消映射时自动销毁，这符合 POSIX 规定。将 sysctl 设置为 1 会使此类共享锁对象持续存在，直到虚拟文件系统回收该 vnode。注意，如果文件未被打开且未被映射，内核可能随时回收它，使此 sysctl 不如听起来有用。

**`kern.ipc.umtx_max_robust`** 一个线程允许的健壮互斥锁的最大数量。内核不会解锁超过指定数量的互斥锁，更多详情参见 [_umtx_op(2)](../sys/_umtx_op.2.md)。默认值对于大多数有用的应用程序来说已足够大。

**`debug.umtx.robust_faults_verbose`** 非零值使内核在检测到某些不一致后过早中止健壮互斥锁解锁时发出一些诊断信息，作为防止内存损坏的措施。

`RLIMIT_UMTXP` 限制（参见 [getrlimit(2)](../sys/getrlimit.2.md)）定义了给定用户可同时创建的共享锁数量。

## 与运行时链接器的交互

加载时，`libthr` 将插入处理程序安装到 `libc` 导出的钩子中。这些插入程序为 `libc` 中单线程进程的存根提供真正的锁定实现，提供取消支持，并对信号操作进行一些修改。

`libthr` 无法卸载；当使用 `libthr` 的句柄调用 dlclose(3) 函数时不执行任何操作。原因之一是 `libc` 函数的内部插入无法撤销。

## 信号

该实现会插入用户安装的 [signal(3)](../gen/signal.3.md) 处理程序。执行此插入是为了将信号传递推迟到进入（libthr 内部）临界区的线程，在临界区中调用用户提供的信号处理程序是不安全的。一种此类情况是持有内部库锁。当信号在无法安全调用信号处理程序时被传递，调用会被推迟，并在退出临界区之后执行。在解释 [ktrace(1)](../man1/ktrace.1.md) 日志时应考虑这一点。

`libthr` 库使用 `SIGTHR` 信号进行内部操作，特别是用于取消请求。该信号的屏蔽和处置由库控制，用户程序不应尝试修改它们。该库会插入控制信号的函数，以防止无意修改并保护可移植代码免受 `SIGTHR` 的影响。

注意：类似地，`SIGLIBRT` 信号保留供 Lb librt 使用，用户不应修改。

## 进程共享同步对象

在 `libthr` 实现中，所有同步对象（如 pthread_mutex_t）的用户可见类型都是指向内部结构的指针，这些内部结构由相应的 `pthread_<objtype>_init` 方法调用分配，或在指定静态初始化程序时在首次使用时隐式分配。进程私有锁定对象的初始实现使用了带有内部分配的此模型，并且进程共享对象的添加方式不会破坏应用程序二进制接口。

对于进程私有对象，内部结构使用 malloc(3) 分配，或者对于 [pthread_mutex_init(3)](pthread_mutex_init.3.md)，使用 `libthr` 中实现的内部内存分配器分配。互斥锁的内部分配器用于避免许多需要工作互斥锁才能运行的 malloc(3) 实现中的引导问题。出于同样的原因，相同的分配器用于线程特定数据，参见 [pthread_setspecific(3)](pthread_setspecific.3.md)。

对于进程共享对象，内部结构的创建首先使用 [_umtx_op(2)](../sys/_umtx_op.2.md) 操作 `UMTX_OP_SHM` 分配共享内存段，然后使用 [mmap(2)](../sys/mmap.2.md) 以 `MAP_SHARED` 标志将其映射到进程地址空间。POSIX 标准要求：

```sh
只有进程共享同步对象本身可用于执行同步。
它无需在用于初始化它的地址处被引用
（即，可以使用同一对象的另一个映射）。
```

在 FreeBSD 实现中，进程共享对象需要在每个使用它们的进程中初始化。特别是，如果你映射包含已在不同进程中初始化的进程共享对象的用户部分的共享内存，锁定函数将无法在其上工作。

另一种损坏情况是 fork 出的子进程在与父进程共享的内存中创建对象，而父进程无法使用它。注意，进程在 [fork(2)](../sys/fork.2.md) 之后本就不应使用非异步信号安全的函数。

## 参见

[ktrace(1)](../man1/ktrace.1.md), ld-elf.so.1(1), [_umtx_op(2)](../sys/_umtx_op.2.md), errno(2), [getrlimit(2)](../sys/getrlimit.2.md), [thr_exit(2)](../sys/thr_exit.2.md), [thr_kill(2)](../sys/thr_kill.2.md), thr_kill2(2), [thr_new(2)](../sys/thr_new.2.md), [thr_self(2)](../sys/thr_self.2.md), [thr_set_name(2)](../sys/thr_set_name.2.md), dlclose(3), [dlopen(3)](../gen/dlopen.3.md), [getenv(3)](../stdlib/getenv.3.md), [pthread_attr(3)](pthread_attr.3.md), pthread_attr_setstacksize(3), [pthread_create(3)](pthread_create.3.md), [signal(3)](../gen/signal.3.md), [atomic(9)](../man9/atomic.9.md)

## 历史

`libthr` 库首次出现在 FreeBSD 5.2 中。

## 作者

`libthr` 库最初由 Jeff Roberson <jeff@FreeBSD.org> 创建，并由 Jonathan Mini <mini@FreeBSD.org> 和 Mike Makonnen <mtm@FreeBSD.org> 增强。David Xu <davidxu@FreeBSD.org> 对其进行了大量重写和优化。
