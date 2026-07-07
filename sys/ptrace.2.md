# ptrace(2)

`ptrace` — 进程跟踪与调试

## 名称

`ptrace`

## 库

Lb libc

## 概要

```c
#include <sys/types.h>
#include <sys/ptrace.h>

int
ptrace(int request, pid_t pid, caddr_t addr, int data);
```

## 描述

`ptrace()` 系统调用提供跟踪和调试功能。它允许一个进程（**跟踪**进程）控制另一个进程（**被跟踪**进程）。跟踪进程必须先附加到被跟踪进程，然后发出一系列 `ptrace()` 系统调用来控制进程的执行，以及访问进程内存和寄存器状态。在跟踪会话期间，被跟踪进程将被"重新设置父进程"，其父进程 ID（及相应行为）更改为跟踪进程。允许跟踪进程同时附加到多个其他进程。当跟踪进程完成工作后，必须分离被跟踪进程；如果跟踪进程退出时未先分离所有已附加的进程，这些进程将被杀死。

大多数时候，被跟踪进程正常运行，但当它收到信号（参见 [sigaction(2)](sigaction.2.md)）时会停止。跟踪进程应通过 [wait(2)](wait.2.md) 或 `SIGCHLD` 信号的传递来注意到这一点，检查停止进程的状态，并使其终止或视情况继续。该信号可以是正常的进程信号，由被跟踪进程行为或使用 [kill(2)](kill.2.md) 系统调用产生；也可以由跟踪设施因附加、跟踪进程单步执行或被跟踪进程中的事件而产生。跟踪进程可选择拦截信号以观察进程行为（如 `SIGTRAP`），或在适当时将信号转发给进程。`ptrace()` 系统调用是实现这一切的机制。

被跟踪进程可能报告与被跟踪进程中事件对应的额外信号停止。这些额外信号停止报告为 `SIGTRAP` 或 `SIGSTOP` 信号。跟踪进程可使用 `PT_LWPINFO` 请求确定哪些事件与 `SIGTRAP` 或 `SIGSTOP` 信号关联。注意，多个事件可能与单个信号关联。例如，由 `PL_FLAG_BORN`、`PL_FLAG_FORKED` 和 `PL_FLAG_EXEC` 标志指示的事件也作为系统调用退出事件（`PL_FLAG_SCX`）报告。通过 `PTRACE_FORK` 启用的新子进程的信号停止将报告 `SIGSTOP` 信号。所有其他额外信号停止使用 `SIGTRAP`。

## 分离与终止

通常，退出的跟踪进程应等待所有待处理的调试事件，然后使用 `PT_DETACH` 请求从所有存活的被跟踪进程分离后再退出。如果跟踪进程未分离即退出（例如因异常终止），被跟踪子进程的命运由 `kern.kill_on_debugger_exit` sysctl 控制。

如果该控制设置为默认值 1，此类被跟踪进程将被终止。如果设置为零，内核隐式分离被跟踪进程。被跟踪进程在需要时被解除停止，然后继续执行而不被跟踪。内核丢弃排队到被跟踪子进程的任何 `SIGTRAP` 信号，这些信号可能由尚未消费的调试事件或其他方式生成（后者本不应发生）。

## 选择目标

调用的 `pid` 参数指定执行请求操作的目标。对于影响全局进程状态的操作，通常传递进程 ID。类似地，对于仅影响线程的操作，需传递线程 ID。

对于全局操作，任何线程的 ID 都可用作目标，系统将在拥有该线程的进程上执行请求。如果线程操作获得进程 ID 作为 `pid`，系统从该进程拥有的线程中随机选择一个线程。对于单线程进程，指定进程 ID 或线程 ID 作为目标没有区别。

## 禁用 ptrace

`ptrace` 子系统提供丰富的设施来操作其他进程的状态。有时可能需要完全禁止它或限制其范围。为此提供以下控制：

**`security.bsd.allow_ptrace`** 将此 sysctl 设置为零使 `ptrace()` 始终返回 ENOSYS，如同内核未实现该系统调用。

**`security.bsd.unprivileged_proc_debug`** 将此 sysctl 设置为零禁止非特权进程使用 `ptrace()`。

**`security.bsd.see_other_uids`** 将此 sysctl 设置为零阻止 `ptrace()` 请求以与调用者不同的真实用户 ID 的进程为目标。这些请求将以 ESRCH 错误失败。

**`security.bsd.see_other_gids`** 将此 sysctl 设置为零禁止与目标进程无公共组（考虑其真实组和补充组集合）的进程发起 `ptrace()` 请求。这些请求将以 ESRCH 错误失败。

**`security.bsd.see_jail_proc`** 将此 sysctl 设置为零禁止属于与目标进程不同 Jail 的进程发起 `ptrace()` 请求，即使请求进程的 Jail 是目标进程 Jail 的祖先。这些请求将以 ESRCH 错误失败。

**`securelevel` 和 init** 只有 securelevel 为零时才能用 `ptrace` 跟踪 init(1) 进程。

**[procctl(2)](procctl.2.md) `PROC_TRACE_CTL`** 进程可通过 [procctl(2)](procctl.2.md) `PROC_TRACE_CTL` 请求拒绝跟踪自身的尝试。此时请求返回 EPERM 错误。

## 跟踪事件

每个被跟踪进程都有一个跟踪事件掩码。被跟踪进程中的事件只有在跟踪事件掩码中设置了相应标志时才报告信号停止。当前跟踪事件标志集包括：

**`PTRACE_EXEC`** 报告成功调用 [execve(2)](execve.2.md) 时的停止。此事件由 `struct ptrace_lwpinfo` 的 `pl_flags` 成员中的 `PL_FLAG_EXEC` 标志指示。

**`PTRACE_SCE`** 报告每次系统调用进入时的停止。此事件由 `struct ptrace_lwpinfo` 的 `pl_flags` 成员中的 `PL_FLAG_SCE` 标志指示。

**`PTRACE_SCX`** 报告每次系统调用退出时的停止。此事件由 `struct ptrace_lwpinfo` 的 `pl_flags` 成员中的 `PL_FLAG_SCX` 标志指示。

**`PTRACE_SYSCALL`** 报告系统调用进入和退出的停止。

**`PTRACE_FORK`** 此事件标志控制被跟踪进程的新子进程的跟踪。当此事件标志启用时，新子进程将启用跟踪并在执行其第一条指令前停止。新子进程将在 `struct ptrace_lwpinfo` 的 `pl_flags` 成员中包含 `PL_FLAG_CHILD` 标志。被跟踪进程将报告包含 `PL_FLAG_FORKED` 标志的停止。新子进程的进程 ID 也将出现在 `struct ptrace_lwpinfo` 的 `pl_child_pid` 成员中。如果新子进程通过 [vfork(2)](vfork.2.md) 创建，被跟踪进程的停止还将包含 `PL_FLAG_VFORKED` 标志。注意，新子进程将以默认跟踪事件掩码附加；它们不继承被跟踪进程的事件掩码。当此事件标志未启用时，新子进程将在未启用跟踪的情况下执行。

**`PTRACE_LWP`** 此事件标志控制 LWP（内核线程）创建和销毁的跟踪。当此事件启用时，新 LWP 将在执行其第一条指令前停止并报告设置了 `PL_FLAG_BORN` 的事件，退出的 LWP 将在完成终止前停止并报告设置了 `PL_FLAG_EXITED` 的事件。注意，新进程不报告其初始线程创建的事件，退出的进程不报告最后一个线程终止的事件。

**`PTRACE_VFORK`** 报告父进程在 [vfork(2)](vfork.2.md) 后恢复时的停止事件。当被跟踪进程中的线程通过 [vfork(2)](vfork.2.md) 创建新子进程时，报告 `PL_FLAG_FORKED` 和 `PL_FLAG_SCX` 的停止发生在子进程创建之后、线程等待子进程停止共享进程内存之前。如果调试器未跟踪新子进程，则必须在从新子进程分离之前确保共享进程内存中没有启用的断点。这意味着父进程中也没有启用的断点。`PTRACE_VFORK` 标志启用一个新的停止，指示新子进程何时停止共享父进程的进程内存。调试器可在此事件响应中在父进程中重新插入断点并恢复它。此事件通过设置 `PL_FLAG_VFORK_DONE` 标志来指示。

通过 `PT_ATTACH`、`PT_TRACE_ME` 或 `PTRACE_FORK` 附加到进程时的默认跟踪事件掩码仅包含 `PTRACE_EXEC` 事件。所有其他事件标志均被禁用。

## ptrace 请求

`request` 参数指定正在执行的操作；其余参数的含义取决于操作，但除下文提到的一个特殊情况外，所有 `ptrace()` 调用都由跟踪进程发起，`pid` 参数指定被跟踪进程的进程 ID 或对应的线程 ID。`request` 参数可以是：

**`PT_TRACE_ME`** 此请求是被跟踪进程唯一使用的请求；它声明该进程期望被其父进程跟踪。所有其他参数被忽略。（如果父进程不期望跟踪子进程，可能会对结果感到困惑；一旦被跟踪进程停止，除了通过 `ptrace()` 外无法使其继续。）当进程使用此请求并调用 [execve(2)](execve.2.md) 或基于它的任何例程（如 [execv(3)](../gen/exec.3.md)）时，它将在执行新映像的第一条指令前停止。此外，正在执行的可执行文件上的任何 setuid 或 setgid 位将被忽略。如果子进程由 [vfork(2)](vfork.2.md) 系统调用或带 `RFMEM` 标志的 [rfork(2)](rfork.2.md) 调用创建，调试事件仅在 [execve(2)](execve.2.md) 执行后才报告给父进程。

**`PT_READ_I`**, **`PT_READ_D`** 这些请求从被跟踪进程的地址空间读取单个 `int` 数据。传统上，`ptrace()` 允许具有不同指令和数据地址空间的机器，因此有两个请求：概念上，`PT_READ_I` 从指令空间读取，`PT_READ_D` 从数据空间读取。在当前 FreeBSD 实现中，这两个请求完全相同。`addr` 参数指定（在被跟踪进程的虚拟地址空间中）要进行读取的地址。此地址不需要满足任何对齐约束。读取的值作为 `ptrace()` 的返回值返回。

**`PT_WRITE_I`**, **`PT_WRITE_D`** 这些请求与 `PT_READ_I` 和 `PT_READ_D` 对应，但它们是写入而非读取。`data` 参数提供要写入的值。

**`PT_IO`** 此请求允许在被跟踪进程的地址空间中读写任意数量的数据。`addr` 参数指定指向 `struct ptrace_io_desc` 的指针，定义如下：

```c
struct ptrace_io_desc {
        int     piod_op;        /* I/O 操作 */
        void    *piod_offs;     /* 子进程偏移 */
        void    *piod_addr;     /* 父进程偏移 */
        size_t  piod_len;       /* 请求长度 */
};

/*
 * piod_op 中的操作。
 */
#define PIOD_READ_D     1       /* 从 D 空间读取 */
#define PIOD_WRITE_D    2       /* 写入 D 空间 */
#define PIOD_READ_I     3       /* 从 I 空间读取 */
#define PIOD_WRITE_I    4       /* 写入 I 空间 */
```

`data` 参数被忽略。实际读写的字节数在返回时存储在 `piod_len` 中。

**`PT_CONTINUE`** 被跟踪进程继续执行。`addr` 参数是指定恢复执行位置的地址（程序计数器的新值），或 `(caddr_t)1` 表示从其离开处继续执行。`data` 参数提供在恢复执行时传递给被跟踪进程的信号编号，若不发送信号则为 0。

**`PT_STEP`** 被跟踪进程单步执行一条指令。`addr` 参数应传递 `(caddr_t)1`。`data` 参数提供在恢复执行时传递给被跟踪进程的信号编号，若不发送信号则为 0。

**`PT_KILL`** 被跟踪进程终止，如同使用 `PT_CONTINUE` 并以 `SIGKILL` 作为传递信号。

**`PT_ATTACH`** 此请求允许一个进程获得对另一个不相关进程的控制并开始跟踪它。它不需要被跟踪进程的任何配合。此时，`pid` 指定要跟踪的进程的进程 ID，其他两个参数被忽略。此请求要求目标进程必须与跟踪进程具有相同的真实 UID，且不得正在执行 setuid 或 setgid 可执行文件。（如果跟踪进程以 root 身份运行，这些限制不适用。）跟踪进程将看到新被跟踪的进程停止，然后可以像一直被跟踪一样控制它。

**`PT_DETACH`** 此请求类似于 PT_CONTINUE，但不允许指定继续执行的替代位置，成功后被跟踪进程不再被跟踪并正常继续执行。无论进程在对应 `PT_ATTACH` 请求之前是否处于停止状态，被跟踪进程的父进程都将被发送 `SIGCHLD` 以指示进程已从停止状态继续。对被跟踪进程的 [wait(2)](wait.2.md) 将指示它已被继续。

**`PT_GETREGS`** 此请求将被跟踪进程的机器寄存器读取到 `addr` 所指向的 `struct reg`（定义在 `machine/reg.h` 中）。

**`PT_SETREGS`** 此请求与 `PT_GETREGS` 相反；它从 `addr` 所指向的 `struct reg`（定义在 `machine/reg.h` 中）加载被跟踪进程的机器寄存器。

**`PT_GETFPREGS`** 此请求将被跟踪进程的浮点寄存器读取到 `addr` 所指向的 `struct fpreg`（定义在 `machine/reg.h` 中）。

**`PT_SETFPREGS`** 此请求与 `PT_GETFPREGS` 相反；它从 `addr` 所指向的 `struct fpreg`（定义在 `machine/reg.h` 中）加载被跟踪进程的浮点寄存器。

**`PT_GETDBREGS`** 此请求将被跟踪进程的调试寄存器读取到 `addr` 所指向的 `struct dbreg`（定义在 `machine/reg.h` 中）。

**`PT_SETDBREGS`** 此请求与 `PT_GETDBREGS` 相反；它从 `addr` 所指向的 `struct dbreg`（定义在 `machine/reg.h` 中）加载被跟踪进程的调试寄存器。

**`PT_GETREGSET`** 此请求从被跟踪进程读取寄存器。`data` 参数指定要读取的寄存器集，`addr` 参数指向一个 `struct iovec`，其中 `iov_base` 字段指向用于保存寄存器的寄存器集特定结构，`iov_len` 字段持有该结构的长度。

**`PT_SETREGSET`** 此请求写入被跟踪进程的寄存器。`data` 参数指定要写入的寄存器集，`addr` 参数指向一个 `struct iovec`，其中 `iov_base` 字段指向用于保存寄存器的寄存器集特定结构，`iov_len` 字段持有该结构的长度。如果 `iov_base` 为 NULL，内核将在 `iov_len` 字段中返回寄存器集特定结构的预期长度，且不更改目标寄存器集。

**`PT_LWPINFO`** 此请求可用于获取导致被跟踪进程停止的内核线程（也称为轻量级进程）的信息。`addr` 参数指定指向 `struct ptrace_lwpinfo` 的指针，定义如下：

```c
struct ptrace_lwpinfo {
        lwpid_t pl_lwpid;
        int     pl_event;
        int     pl_flags;
        sigset_t pl_sigmask;
        sigset_t pl_siglist;
        siginfo_t pl_siginfo;
        char    pl_tdname[MAXCOMLEN + 1];
        pid_t   pl_child_pid;
        u_int   pl_syscall_code;
        u_int   pl_syscall_narg;
};
```

`data` 参数应设置为调用者已知的结构大小。这允许结构增长而不影响旧程序。`struct ptrace_lwpinfo` 中的字段含义如下：

**`pl_lwpid`** 线程的 LWP ID

**`pl_event`** 导致停止的事件。当前定义的事件有：
- `PL_EVENT_NONE`：未给出原因
- `PL_EVENT_SIGNAL`：线程因待处理信号而停止

**`pl_flags`** 指定观察到的停止的额外细节的标志。当前定义的标志有：
- `PL_FLAG_SCE`：线程因系统调用进入而停止，紧接在进入内核之后。调试器可根据当前进程的 ABI 检查存储在内存和寄存器中的系统调用参数，并在需要时修改它们。
- `PL_FLAG_SCX`：线程在系统调用返回用户模式之前立即停止。调试器可在 ABI 定义的寄存器和/或内存中检查系统调用返回值。
- `PL_FLAG_EXEC`：当设置了 `PL_FLAG_SCX` 时，此标志可能被额外指定，以通知被调试进程执行的程序已通过成功执行 `execve(2)` 系列系统调用而更改。
- `PL_FLAG_SI`：指示 `struct ptrace_lwpinfo` 的 `pl_siginfo` 成员包含有效信息。
- `PL_FLAG_FORKED`：指示进程正从创建新子进程的 [fork(2)](fork.2.md) 调用返回。新进程的进程标识符可在 `struct ptrace_lwpinfo` 的 `pl_child_pid` 成员中获取。
- `PL_FLAG_CHILD`：此标志在启用 `PTRACE_FORK` 时自动附加的新子进程报告的第一个事件中设置。
- `PL_FLAG_BORN`：此标志在启用 `PTRACE_LWP` 时新 LWP 报告的第一个事件中设置。它与 `PL_FLAG_SCX` 一起报告。
- `PL_FLAG_EXITED`：此标志在启用 `PTRACE_LWP` 时退出的 LWP 报告的最后一个事件中设置。注意，当进程中最后一个 LWP 退出时不报告此事件。最后一个线程的终止通过正常的进程退出事件报告。
- `PL_FLAG_VFORKED`：指示线程正从创建新子进程的 [vfork(2)](vfork.2.md) 调用返回。此标志在 `PL_FLAG_FORKED` 之外额外设置。
- `PL_FLAG_VFORK_DONE`：指示线程在通过 [vfork(2)](vfork.2.md) 创建的子进程停止与被跟踪进程共享地址空间后已恢复。

**`pl_sigmask`** LWP 的当前信号掩码

**`pl_siglist`** LWP 的当前待处理信号集。注意，传递给进程的信号在线程被选为传递目标之前不会出现在 LWP siglist 上。

**`pl_siginfo`** 伴随待处理信号的 siginfo。仅在设置了 `pl_flags` 中 `PL_FLAG_SI` 的 `PL_EVENT_SIGNAL` 停止时有效。

**`pl_tdname`** 线程名。

**`pl_child_pid`** 新子进程的进程标识符。仅在设置了 `pl_flags` 中 `PL_FLAG_FORKED` 的 `PL_EVENT_SIGNAL` 停止时有效。

**`pl_syscall_code`** 当前系统调用的 ABI 特定标识符。注意，对于间接系统调用，此字段报告被间接的系统调用。仅在设置了 `pl_flags` 中 `PL_FLAG_SCE` 或 `PL_FLAG_SCX` 时有效。

**`pl_syscall_narg`** 传递给当前系统调用的参数数量（不包含系统调用标识符）。注意，对于间接系统调用，此字段报告传递给被间接的系统调用的参数。仅在设置了 `pl_flags` 中 `PL_FLAG_SCE` 或 `PL_FLAG_SCX` 时有效。

**`PT_GETNUMLWPS`** 此请求返回与被跟踪进程关联的内核线程数。

**`PT_GETLWPLIST`** 此请求可用于获取当前线程列表。应在 `addr` 中传递类型为 `lwpid_t` 的数组指针，数组大小由 `data` 指定。`ptrace()` 的返回值是填充的数组条目数。

**`PT_SETSTEP`** 此请求将打开指定进程的单步执行。当捕获到单步陷阱时自动禁用单步。

**`PT_CLEARSTEP`** 此请求将关闭指定进程的单步执行。

**`PT_SUSPEND`** 此请求将挂起指定线程。

**`PT_RESUME`** 此请求将恢复指定线程。

**`PT_TO_SCE`** 此请求将设置 `PTRACE_SCE` 事件标志以跟踪所有未来的系统调用进入并继续进程。`addr` 和 `data` 参数的使用与 `PT_CONTINUE` 相同。

**`PT_TO_SCX`** 此请求将设置 `PTRACE_SCX` 事件标志以跟踪所有未来的系统调用退出并继续进程。`addr` 和 `data` 参数的使用与 `PT_CONTINUE` 相同。

**`PT_SYSCALL`** 此请求将设置 `PTRACE_SYSCALL` 事件标志以跟踪所有未来的系统调用进入和退出并继续进程。`addr` 和 `data` 参数的使用与 `PT_CONTINUE` 相同。

**`PT_GET_SC_ARGS`** 对于在 `PL_FLAG_SCE` 或 `PL_FLAG_SCX` 状态（即系统调用进入或退出）下停止的线程，此请求获取系统调用参数。参数按顺序复制到 `addr` 指针所指向的缓冲区中。每个系统调用参数以机器字存储。内核复制出系统调用接受的参数数量（参见 `struct ptrace_lwpinfo` 的 `pl_syscall_narg` 成员），但复制总数不超过 `data` 字节。

**`PT_GET_SC_RET`** 在系统调用退出时获取系统调用返回值。此请求仅在系统调用退出停止（`PL_FLAG_SCX` 状态）的线程上有效。`addr` 参数指定指向 `struct ptrace_sc_ret` 的指针，定义如下：

```c
struct ptrace_sc_ret {
        register_t      sr_retval[2];
        int             sr_error;
};
```

`data` 参数设置为结构大小。如果系统调用成功完成，`sr_error` 设置为零，系统调用的返回值保存在 `sr_retval` 中。如果系统调用执行失败，`sr_error` 字段设置为正的 errno(2) 值。如果系统调用以异常方式完成，`sr_error` 设置为负值：
- `ERESTART`：系统调用将被重启。
- `EJUSTRETURN`：系统调用成功完成但未设置返回值（例如 setcontext(2) 和 [sigreturn(2)](sigreturn.2.md)）。

**`PT_FOLLOW_FORK`** 此请求控制被跟踪进程的新子进程的跟踪。如果 `data` 非零，在被跟踪进程的事件跟踪掩码中设置 `PTRACE_FORK`。如果 `data` 为零，从被跟踪进程的事件跟踪掩码中清除 `PTRACE_FORK`。

**`PT_LWP_EVENTS`** 此请求控制 LWP 创建和销毁的跟踪。如果 `data` 非零，在被跟踪进程的事件跟踪掩码中设置 `PTRACE_LWP`。如果 `data` 为零，从被跟踪进程的事件跟踪掩码中清除 `PTRACE_LWP`。

**`PT_GET_EVENT_MASK`** 此请求将被跟踪进程的事件跟踪掩码读取到 `addr` 所指向的整数中。整数的大小必须在 `data` 中传递。

**`PT_SET_EVENT_MASK`** 此请求从 `addr` 所指向的整数设置被跟踪进程的事件跟踪掩码。整数的大小必须在 `data` 中传递。

**`PT_VM_TIMESTAMP`** 此请求将被跟踪进程内存映射的生成号或时间戳作为 `ptrace()` 的返回值返回。这为跟踪进程提供了一种低成本方式来判断自上次请求以来 VM 映射是否更改。

**`PT_VM_ENTRY`** 此请求用于遍历被跟踪进程 VM 映射的条目。`addr` 参数指定指向 `struct ptrace_vm_entry` 的指针，定义如下：

```c
struct ptrace_vm_entry {
        int             pve_entry;
        int             pve_timestamp;
        u_long          pve_start;
        u_long          pve_end;
        u_long          pve_offset;
        u_int           pve_prot;
        u_int           pve_pathlen;
        long            pve_fileid;
        uint32_t        pve_fsid;
        char            *pve_path;
};
```

通过将 `pve_entry` 设置为零返回第一个条目。通过不修改先前请求返回的 `pve_entry` 值返回后续条目。`pve_timestamp` 字段可用于在遍历条目时检测 VM 映射的更改。跟踪进程随后可采取适当操作，如重启。通过在进入时将 `pve_pathlen` 设置为非零值，如果条目由 vnode 支撑，则支撑对象的路径名将在 `pve_path` 所指向的缓冲区中返回。`pve_pathlen` 字段更新为路径名的实际长度（包括终止的 null 字符）。`pve_offset` 字段是范围开始的支撑对象内的偏移量。范围位于 VM 空间中的 `pve_start` 并延伸到 `pve_end`（含）。`data` 参数被忽略。

**`PT_COREDUMP`** 此请求为停止的程序创建核心转储。`addr` 参数指定指向 `struct ptrace_coredump` 的指针，定义如下：

```c
struct ptrace_coredump {
        int             pc_fd;
        uint32_t        pc_flags;
        off_t           pc_limit;
};
```

结构字段为：
- `pc_fd`：写入转储的文件描述符。它必须引用以写方式打开的常规文件。
- `pc_flags`：标志。定义以下标志：
  - `PC_COMPRESS`：请求压缩转储。
  - `PC_ALL`：将不可转储的条目包含到转储中。转储器忽略进程映射条目的 `MAP_NOCORE` 标志，但即使设置了 `PC_ALL`，设备映射也不会被转储。
- `pc_limit`：核心转储的最大大小。指定零表示无限制。

`struct ptrace_coredump` 的大小必须在 `data` 中传递。

**`PT_SC_REMOTE`** 请求在被跟踪进程的上下文中、在指定线程中执行系统调用。`addr` 参数必须指向 `struct ptrace_sc_remote`，它描述了请求的系统调用及其参数，并接收结果。`struct ptrace_sc_remote` 的大小必须在 `data` 中传递。

```c
struct ptrace_sc_remote {
        struct ptrace_sc_ret pscr_ret;
        u_int   pscr_syscall;
        u_int   pscr_nargs;
        u_long  *pscr_args;
};
```

`pscr_syscall` 包含要执行的系统调用号，`pscr_nargs` 是提供的参数数量，参数在 `pscr_args` 数组中提供。执行结果在 `pscr_ret` 成员中返回。注意，请求及其结果不影响当前执行的系统调用（如果有）的返回值。

## PT_COREDUMP 和 PT_SC_REMOTE 用法

在转储或发起远程系统调用之前，进程必须已停止。目标进程中的单个线程在内核中被临时取消挂起以执行操作。如果 `ptrace` 调用在线程被取消挂起之前失败，则没有可供 [waitpid(2)](wait.2.md) 等待的事件。如果线程已被取消挂起，它将在 `ptrace` 调用返回之前再次停止，必须使用 [waitpid(2)](wait.2.md) 等待进程以消费新的停止事件。由于难以推断错误发生前线程是否已被取消挂起，建议在 `PT_COREDUMP` 和 `PT_SC_REMOTE` 之后无条件执行带 `WNOHANG` 标志的 [waitpid(2)](wait.2.md)，并静默接受零结果。

对于 `PT_SC_REMOTE`，所选线程必须在安全位置停止，当前定义为系统调用退出或从内核返回用户模式（基本上是信号处理程序调用位置）。如果在不安全的停止处尝试执行远程系统调用，内核返回 EBUSY 状态。

注意，`PT_SC_REMOTE` 执行系统调用期间，既不遵守 `kern.trap_enotcap` sysctl 设置，也不遵守对应的 [procctl(2)](procctl.2.md) 标志 `PROC_TRAPCAP_CTL_ENABLE`。换言之，以 capability 模式执行且违反模式访问限制的进程不会发送 `SIGTRAP` 信号。

注意，由于远程系统调用的执行模式，特别是仅允许一个线程运行的设置，系统调用可能阻塞在由挂起线程拥有的资源上。这可能导致目标进程死锁。在这种情况下，唯一的出路是杀死目标。

## ARM 机器特定请求

**`PT_GETVFPREGS`** 在 `addr` 所指向的缓冲区中返回线程的 `VFP` 机器状态。`data` 参数被忽略。

**`PT_SETVFPREGS`** 从 `addr` 所指向的缓冲区设置线程的 `VFP` 机器状态。`data` 参数被忽略。

## x86 机器特定请求

**`PT_GETXMMREGS`** 将 XMM FPU 状态复制到 `addr` 参数所指向的缓冲区。该缓冲区的布局与机器指令 `FXSAVE` 的 32 位保存缓冲区相同。此请求仅对 i386 程序有效，包括原生 32 位系统和 amd64 内核上的程序。对于 64 位 amd64 程序，XMM 状态作为 `PT_GETFPREGS` 请求返回的 FPU 状态的一部分报告。`data` 参数被忽略。

**`PT_SETXMMREGS`** 从 `addr` 参数所指向的缓冲区加载线程的 XMM FPU 状态。该缓冲区的布局与机器指令 `FXRSTOR` 的 32 位加载缓冲区相同。与 `PT_GETXMMREGS` 一样，此请求仅对 i386 程序有效。`data` 参数被忽略。

**`PT_GETXSTATE_INFO`** 报告 CPU 支持且用户空间程序允许的 XSAVE FPU 扩展。`addr` 参数必须指向 `struct ptrace_xstate_info` 类型的变量，该变量在请求返回时包含信息。`struct ptrace_xstate_info` 定义如下：

```c
struct ptrace_xstate_info {
        uint64_t        xsave_mask;
        uint32_t        xsave_len;
};
```

`xsave_mask` 字段是当前启用扩展的位掩码。位的含义在 Intel 和 AMD 处理器文档中定义。`xsave_len` 字段报告以 x86 `XSAVE` 机器指令定义的格式存储当前启用扩展的硬件状态的 XSAVE 区域长度。`data` 参数值必须等于 `struct ptrace_xstate_info` 的大小。

**`PT_GETXSTATE`** 返回线程的 XSAVE 区域内容。`addr` 参数指向内容复制到的缓冲区，`data` 参数指定缓冲区大小。内核复制出缓冲区大小所允许的内容。缓冲区布局由 `XSAVE` 机器指令的保存区域布局指定。

**`PT_SETXSTATE`** 从 `addr` 指针指定的缓冲区加载线程的 XSAVE 状态。缓冲区大小在 `data` 参数中传递。缓冲区必须至少与 `struct savefpu`（定义在 **x86/fpu.h**）一样大，以允许完整的 x87 FPU 和 XMM 状态加载。它不得大于 `PT_GETXSTATE_INFO` 请求的 `struct ptrace_xstate_info` 中 `xsave_len` 字段报告的 XSAVE 状态长度。缓冲区的布局与 `XRSTOR` 机器指令的加载区域布局相同。

**`PT_GETFSBASE`** 返回使用 %fs 段寄存器进行分段内存寻址时使用的基址值。`addr` 参数指向存储基址值的 `unsigned long` 变量。`data` 参数被忽略。

**`PT_GETGSBASE`** 类似于 `PT_GETFSBASE` 请求，但返回 %gs 段寄存器的基址。

**`PT_SETFSBASE`** 将 %fs 段寄存器的基址设置为 `addr` 参数所指向的值。`addr` 必须指向包含新基址的 `unsigned long` 变量。`data` 参数被忽略。

**`PT_SETGSBASE`** 类似于 `PT_SETFSBASE` 请求，但设置 %gs 段寄存器的基址。

## PowerPC 机器特定请求

**`PT_GETVRREGS`** 在 `addr` 所指向的缓冲区中返回线程的 `ALTIVEC` 机器状态。`data` 参数被忽略。

**`PT_SETVRREGS`** 从 `addr` 所指向的缓冲区设置线程的 `ALTIVEC` 机器状态。`data` 参数被忽略。

**`PT_GETVSRREGS`** 在 `addr` 所指向的缓冲区中返回线程 `VSX` 寄存器 VSR0-VSR31 的双字 1。`data` 参数被忽略。

**`PT_SETVSRREGS`** 从 `addr` 所指向的缓冲区设置线程 `VSX` 寄存器 VSR0-VSR31 的双字 1。`data` 参数被忽略。

此外，可能存在其他机器特定的请求。

## 返回值

大多数请求成功时返回 0，出错时返回 -1。某些请求可能导致 `ptrace()` 返回 -1 作为非错误值，其中包括 `PT_READ_I` 和 `PT_READ_D`，它们在成功时返回从进程内存读取的值。为消除歧义，可在调用前将 `errno` 设置为 0 并在之后检查。

当前 `ptrace()` 实现始终在调用内核之前将 `errno` 设置为 0，既出于历史原因，也为与其他操作系统保持一致。建议显式将 `errno` 赋值为零以保持前向兼容性。

## 错误

`ptrace()` 系统调用在以下情况下可能失败：

**[ESRCH]** 不存在具有指定进程 ID 的进程。

**[EINVAL]**
- 进程尝试对自身使用 `PT_ATTACH`。
- `request` 参数不是合法请求之一。
- `PT_CONTINUE` 的信号编号（在 `data` 中）既不是 0 也不是合法信号编号。
- 对没有有效寄存器集的进程尝试 `PT_GETREGS`、`PT_SETREGS`、`PT_GETFPREGS`、`PT_SETFPREGS`、`PT_GETDBREGS` 或 `PT_SETDBREGS`。（通常仅系统进程如此。）
- `PT_VM_ENTRY` 的 `pve_entry` 给定了无效值。这也可能由进程 VM 映射的更改导致。
- 提供给 `PT_LWPINFO` 的大小（在 `data` 中）小于等于零，或大于内核已知的 `ptrace_lwpinfo` 结构。
- 提供给 x86 特定 `PT_GETXSTATE_INFO` 请求的大小（在 `data` 中）不等于 `struct ptrace_xstate_info` 的大小。
- 提供给 x86 特定 `PT_SETXSTATE` 请求的大小（在 `data` 中）小于 x87 加 XMM 保存区域的大小。
- 提供给 x86 特定 `PT_SETXSTATE` 请求的大小（在 `data` 中）大于 `PT_GETXSTATE_INFO` 请求的 `struct ptrace_xstate_info` 中 `xsave_len` 成员返回的值。
- 提供给 amd64 特定请求 `PT_SETFSBASE` 或 `PT_SETGSBASE` 的基址值指向有效用户地址空间之外。此错误在 32 位程序中不会发生。

**[EBUSY]**
- 对已在被跟踪的进程尝试 `PT_ATTACH`。
- 请求尝试操作正被非发起请求进程的其他进程跟踪的进程。
- 请求（非 `PT_ATTACH`）指定了未停止的进程。

**[EPERM]**
- 请求（非 `PT_ATTACH`）尝试操作根本未被跟踪的进程。
- 尝试对违反上述 `PT_ATTACH` 要求的进程使用 `PT_ATTACH`。

**[ENOENT]** `PT_VM_ENTRY` 先前返回了内存映射的最后一个条目。不存在更多条目。

**[ENOMEM]** `PT_READ_I`、`PT_READ_D`、`PT_WRITE_I` 或 `PT_WRITE_D` 请求尝试访问无效地址，或访问进程内存时发生内存分配失败。

**[ENAMETOOLONG]** `PT_VM_ENTRY` 因缓冲区不够大而无法返回支撑对象的路径名。`pve_pathlen` 在返回时持有所需的最小缓冲区大小。

## 参见

[execve(2)](execve.2.md), [kill(2)](kill.2.md), [procctl(2)](procctl.2.md), setcontext(2), [sigaction(2)](sigaction.2.md), [sigreturn(2)](sigreturn.2.md), [vfork(2)](vfork.2.md), [wait(2)](wait.2.md), [execv(3)](../gen/exec.3.md), [i386_set_watch(3)](../sys-1/i386_set_watch.3.md), init(1)

## 历史

`ptrace()` 函数首次出现于 Version 6 AT&T UNIX。