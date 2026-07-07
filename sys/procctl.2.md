# procctl(2)

`procctl` — 控制进程

## 名称

`procctl`

## 库

Lb libc

## 概要

`#include <sys/procctl.h>`

```c
int
procctl(idtype_t idtype, id_t id, int cmd, void *data);
```

## 描述

`procctl()` 系统调用提供对进程的控制。`idtype` 和 `id` 参数指定要控制的进程集合。如果多个进程匹配该标识符，`procctl` 会“尽力”控制尽可能多的所选进程。仅当没有所选进程成功完成请求时才返回错误。支持以下标识符类型：

**`P_PID`** 控制进程 ID 为 `id` 的进程。`id` 为零是调用进程 ID 的快捷方式。

**`P_PGID`** 控制属于 ID 为 `id` 的进程组的进程。

要执行的控制请求由 `cmd` 参数指定。

所有更改状态的请求（`*_CTL`）要求调用者有权调试目标。所有查询状态的请求（`*_STATUS`）要求调用者有权观察目标。

支持以下命令：

**`PROC_ASLR_FORCE_ENABLE`** 请求在执行后启用 ASLR，即使系统范围内禁用。

**`PROC_ASLR_FORCE_DISABLE`** 请求在执行后禁用 ASLR，即使系统范围内启用。

**`PROC_ASLR_NOFORCE`** 对 ASLR 使用系统范围内配置的策略。

**`PROC_ASLR_FORCE_ENABLE`**

**`PROC_ASLR_FORCE_DISABLE`**

**`PROC_ASLR_NOFORCE`**

**`PROC_LOGSIGEXIT_CTL_FORCE_ENABLE`** 启用对因通常会导致 core dump 的信号而退出的日志记录。日志通过 log(9) 写入，日志级别为 `LOG_INFO`。

**`PROC_LOGSIGEXIT_CTL_FORCE_DISABLE`** 禁用对因通常会导致 core dump 的信号而退出的日志记录。

**`PROC_LOGSIGEXIT_CTL_NOFORCE`** 日志行为委托给 [sysctl(3)](../man3/sysctl.3.md) MIB 变量 `kern.logsigexit`。

**`PROC_LOGSIGEXIT_CTL_FORCE_ENABLE`**

**`PROC_LOGSIGEXIT_CTL_FORCE_DISABLE`**

**`PROC_LOGSIGEXIT_CTL_NOFORCE`**

**`PROC_PROTMAX_FORCE_ENABLE`** 将 `prot` 中的权限作为隐式最大保护，即使 sysctl `vm.imply_prot_max` 请求 RWX 权限。

**`PROC_PROTMAX_FORCE_DISABLE`** 使用 RWX 作为隐式最大保护，即使 sysctl `vm.imply_prot_max` 请求受限权限。

**`PROC_PROTMAX_NOFORCE`** 对隐式 PROT_MAX 控制使用系统范围内配置的策略。

**`PROC_PROTMAX_FORCE_ENABLE`**

**`PROC_PROTMAX_FORCE_DISABLE`**

**`PROC_PROTMAX_NOFORCE`**

**`PPROT_SET`** 将所选进程标记为受保护。

**`PPROT_CLEAR`** 清除所选进程的受保护状态。

**`PPROT_DESCEND`** 除每个所选进程外，还对该进程的所有子进程执行所请求的操作。

**`PPROT_INHERIT`** 与 `PPROT_SET` 一起使用时，将每个所选进程的所有未来子进程标记为受保护。未来的子进程也会将其所有未来子进程标记为受保护。

```c
struct procctl_reaper_status {
	u_int	rs_flags;
	u_int	rs_children;
	u_int	rs_descendants;
	pid_t	rs_reaper;
	pid_t	rs_pid;
};
```

**`REAPER_STATUS_OWNED`** 指定的进程是 reaper。当返回此标志时，指定的进程 `id`（pid）标识一个 reaper；否则结构的 `rs_reaper` 字段设置为指定进程 id 对应 reaper 的 pid。

**`REAPER_STATUS_REALINIT`** 指定的进程是 reaper 树的根，即 [init(8)](../man8/init.8.md)。

```c
struct procctl_reaper_pids {
	u_int	rp_count;
	struct procctl_reaper_pidinfo *rp_pids;
};
```

```c
struct procctl_reaper_pidinfo {
	pid_t	pi_pid;
	pid_t	pi_subtree;
	u_int	pi_flags;
};
```

**`REAPER_PIDINFO_VALID`** 设置以指示 `procctl_reaper_pidinfo` 结构已由内核填充。将 `rp_pids` 数组零初始化并测试 `REAPER_PIDINFO_VALID` 标志可使调用者检测返回数组的末尾。

**`REAPER_PIDINFO_CHILD`** `pi_pid` 字段标识 reaper 的直接子进程。

**`REAPER_PIDINFO_REAPER`** 所报告的进程本身是 reaper。下属 reaper 的后代不会被报告。

**`REAPER_PIDINFO_ZOMBIE`** 所报告的进程处于僵尸状态，准备好被回收。

**`REAPER_PIDINFO_STOPPED`** 所报告的进程被 SIGSTOP/SIGTSTP 信号停止。

**`REAPER_PIDINFO_EXITING`** 所报告的进程正在退出过程中（但尚未成为僵尸）。

```c
struct procctl_reaper_kill {
	int	rk_sig;
	u_int	rk_flags;
	pid_t	rk_subtree;
	u_int	rk_killed;
	pid_t	rk_fpid;
};
```

**`REAPER_KILL_CHILDREN`** 仅将指定信号传递给 reaper 的直接子进程。

**`REAPER_KILL_SUBTREE`** 仅将指定信号传递给由 `rk_subtree` 字段中指定 pid 的直接子进程派生的后代。

**`PROC_TRACE_CTL_ENABLE`** 在被 `PROC_TRACE_CTL_DISABLE` 禁用后启用跟踪。仅允许对自身使用。

**`PROC_TRACE_CTL_DISABLE`** 对指定进程禁用跟踪。当进程通过 [execve(2)](execve.2.md) 系统调用更改正在执行的程序时，跟踪重新启用。子进程在 [fork(2)](fork.2.md) 时从父进程继承跟踪设置。

**`PROC_TRACE_CTL_DISABLE_EXEC`** 与 `PROC_TRACE_CTL_DISABLE` 相同，但该设置即使在 [execve(2)](execve.2.md) 之后也会为进程保留。

**`PROC_TRAPCAP_CTL_ENABLE`** 在 capability 模式访问违规时启用 `SIGTRAP` 信号传递。启用的模式由进程的子进程继承，并在 fexecve(2) 调用后保留。

**`PROC_TRAPCAP_CTL_DISABLE`** 在 capability 模式访问违规时禁用 `SIGTRAP` 信号传递。注意，全局 sysctl `kern.trap_enotcap` 可能仍会导致信号被传递。参见 [capsicum(4)](../man4/capsicum.4.md)。

**`PROC_STACKGAP_ENABLE`** 此标志仅为与 `PROC_STACKGAP_STATUS` 一致而接受。如果栈间隙已启用，该标志被忽略。如果栈间隙已禁用，请求以 `EINVAL` 失败。在进程中禁用间隙后，只能通过执行 [execve(2)](execve.2.md) 重新启用。

**`PROC_STACKGAP_DISABLE`** 对进程禁用栈间隙。对于已存在的栈，间隙不再保留，可在访问时由内存填充。

**`PROC_STACKGAP_ENABLE_EXEC`** 对指定进程未来任何 [execve(2)](execve.2.md) 构建的新地址空间启用栈间隙。

**`PROC_STACKGAP_DISABLE_EXEC`** 在 [execve(2)](execve.2.md) 之后继承已禁用的栈间隙状态。换言之，如果当前执行的程序已禁用栈间隙，则在 exec 后保持禁用。如果间隙已启用，则在 exec 后保持启用。

**`PROC_STACKGAP_ENABLE`** 栈间隙已启用。

**`PROC_STACKGAP_DISABLE`** 栈间隙已禁用。

**`PROC_STACKGAP_ENABLE_EXEC`** 进程在 [execve(2)](execve.2.md) 之后栈间隙已启用。

**`PROC_STACKGAP_DISABLE_EXEC`** 进程在 [execve(2)](execve.2.md) 之后栈间隙已禁用。

**`PROC_NO_NEW_PRIVS_ENABLE`** 请求忽略 set-user-ID 和 set-group-ID 位。

**`PROC_NO_NEW_PRIVS_ENABLE`**

**`PROC_NO_NEW_PRIVS_DISABLE`**

**`PROC_WX_MAPPINGS_PERMIT`** 允许在指定进程当前及未来的地址空间中创建同时具有写和执行权限的映射。

**`PROC_WX_MAPPINGS_DISALLOW_EXEC`** 在未来调用 [execve(2)](execve.2.md) 创建的新地址空间中，不允许创建同时具有写和执行权限的映射。

**`PROC_WX_MAPPINGS_PERMIT`** 允许创建同时可写和可执行的映射；否则，进程不能创建此类映射。

**`PROC_WX_MAPPINGS_DISALLOW_EXEC`** 在 [execve(2)](execve.2.md) 之后，新地址空间将不允许创建同时可写和可执行的映射。

**`PROC_ASLR_CTL`** 控制由指定进程或其不更改控制也不通过其他方式修改的后代进程中 [execve(2)](execve.2.md) 创建的程序镜像中的地址空间布局随机化（ASLR）。`data` 参数必须指向一个整型变量，其中包含以下值之一：注意 elfctl(1) “noaslr”标志优先于此控制。执行设置了此标志的二进制文件永远不会使用 ASLR。类似地，执行 set-user-ID 或 set-group-ID 二进制文件会忽略此控制，仅遵循 elfctl(1) 标志和系统范围内策略。

**`PROC_ASLR_STATUS`** 返回目标进程的 ASLR 启用当前状态。`data` 参数必须指向一个整型变量，其中写入以下值之一：如果进程本身当前执行的镜像启用了 ASLR，则 `PROC_ASLR_ACTIVE` 标志与上述值按位或后写入。

**`PROC_LOGSIGEXIT_CTL`** 控制对因通常会导致 core dump 的信号而退出的日志记录。`arg` 参数必须指向一个整型变量，其中包含以下值之一：

**`PROC_LOGSIGEXIT_STATUS`** 返回目标进程的日志记录当前状态。`arg` 参数必须指向一个整型变量，其中写入以下值之一：

**`PROC_PROTMAX_CTL`** 控制目标进程中未通过 `PROT_MAX` 在 `prot` 参数中显式指定最大保护的 [mmap(2)](mmap.2.md) 请求所使用的最大保护。最大保护限制 [mprotect(2)](mprotect.2.md) 可为映射分配的权限。如果未提供显式最大保护，新映射的最大保护设置为 `PROT_READ | PROT_WRITE | PROT_EXEC`（RWX）或 `prot` 中指定的保护。`prot` 设置为 `PROT_NONE` 创建的映射始终使用 RWX 最大保护。`data` 参数必须指向一个整型变量，其中包含以下值之一：注意 elfctl(1) “noprotmax”标志优先于此控制。执行设置了此标志的二进制文件将始终使用 RWX 作为隐式最大保护。

**`PROC_PROTMAX_STATUS`** 返回目标进程的隐式 PROT_MAX 控制当前状态。`data` 参数必须指向一个整型变量，其中写入以下值之一：如果进程本身当前执行的镜像启用了隐式 PROT_MAX 控制，则 `PROC_PROTMAX_ACTIVE` 标志与上述值按位或后写入。

**`PROC_SPROTECT`** 设置进程保护状态。用于将进程标记为受保护，使其在系统耗尽可用内存和交换空间时不被杀死。`data` 参数必须指向一个包含操作和零个或多个可选标志的整数。支持以下操作：支持以下可选标志：

**`PROC_REAP_ACQUIRE`** 为当前进程的未来子进程启用孤儿进程回收。如果父进程在其一个或多个子进程之前退出，剩余的子进程成为孤儿。当孤儿进程退出时，它被重新归属到负责通过 [wait(2)](wait.2.md) 收割已终止进程的 reaper 进程。启用此控制后，当前进程成为未来子进程及其后代的 reaper 进程。现有子进程继续使用其在通过 [fork(2)](fork.2.md) 创建时分配的 reaper。如果 reaper 进程退出，其作为 reaper 的所有进程将重新分配给该 reaper 进程的 reaper。系统初始化后，[init(8)](../man8/init.8.md) 是默认 reaper。

**`PROC_REAP_RELEASE`** 对当前进程禁用孤儿进程回收。当前进程作为 reaper 的所有进程将重新分配给当前进程的 reaper。

**`PROC_REAP_STATUS`** 提供关于指定进程的 reaper（或如果该进程本身是 reaper 则为该进程本身）的一致信息快照。`data` 参数必须指向一个 `procctl_reaper_status` 结构，该结构在成功返回时由系统调用填充。`rs_flags` 可能返回以下标志：`rs_children` 字段返回可由 reaper 回收且同时是 reaper 子进程的进程数。可能存在其 reaper 不是指定进程的子进程，因为现有子进程的 reaper 不会因 `PROC_REAP_ACQUIRE` 而改变。`rs_descendants` 字段返回可由 reaper 回收的进程总数。`rs_reaper` 字段返回 reaper 的 pid。`rs_pid` 返回某个 reaper 子进程的 pid（如果有可回收的进程）；否则设置为 -1。

**`PROC_REAP_GETPIDS`** 查询指定进程的 reaper 可回收的进程列表。此请求在 `data` 参数中接受一个指向 `procctl_reaper_pids` 结构的指针。调用时，`rp_pids` 字段必须指向一个由 `rp_count` 个 `procctl_reaper_pidinfo` 结构组成的数组。内核将用 reaper 后代的信息填充这些结构。`struct procctl_reaper_pidinfo` 结构提供 reaper 某个后代的部分信息。注意，对于非子进程的后代，可能因竞态（原始子进程退出且退出进程的 pid 被重用于无关进程）而被错误标识。`pi_pid` 字段是该后代的进程 id。`pi_subtree` 字段提供作为该后代进程（祖父）父进程的 reaper 直接子进程的 pid。`pi_flags` 字段返回以下标志，进一步描述该后代：

**`PROC_REAP_KILL`** 请求向 reaper 后代的某个子集传递信号。`data` 参数必须指向一个 `procctl_reaper_kill` 结构，该结构同时用于参数和状态返回。`rk_sig` 字段指定要传递的信号。与 [kill(2)](kill.2.md) 不同，零不是有效的信号编号。`rk_flags` 字段进一步指导操作。它由以下标志按位或组成：如果未指定 `REAPER_KILL_CHILDREN` 或 `REAPER_KILL_SUBTREE` 标志，则向 reaper 的所有当前后代传递信号。如果向任何进程传递了信号，请求的返回值为零。在这种情况下，`rk_killed` 字段标识被传递信号的进程数。`rk_fpid` 字段设置为信号传递失败的第一个进程的 pid（例如由于权限问题）。如果不存在这样的进程，`rk_fpid` 字段设置为 -1。

**`PROC_TRACE_CTL`** 根据整型参数的值启用或禁用指定进程的跟踪。跟踪包括通过 [ptrace(2)](ptrace.2.md)、[ktrace(2)](ktrace.2.md)、调试 sysctl、[hwpmc(4)](../man4/hwpmc.4.md) 或 [dtrace(1)](../man1/dtrace.1.md) 检查进程，以及转储 core。`data` 参数的可能值为：

**`PROC_TRACE_STATUS`** 在 `data` 所指向的整型变量中返回指定进程的当前跟踪状态。如果跟踪被禁用，`data` 设置为 -1。如果跟踪已启用但未通过 [ptrace(2)](ptrace.2.md) 系统调用附加调试器，`data` 设置为 0。如果已附加调试器，`data` 设置为调试器进程的 pid。

**`PROC_TRAPCAP_CTL`** 控制指定沙箱化进程在从任何以 `ENOTCAPABLE` 或 `ECAPMODE` 错误失败的系统调用返回时的 capability 模式沙箱操作。如果启用此控制且系统调用以这些错误之一失败，则在从系统调用返回之前立即向线程传递同步 `SIGTRAP` 信号。`data` 参数的可能值为：在信号传递时，`siginfo` 信号处理程序参数的 `si_errno` 成员设置为系统调用错误值，`si_code` 成员设置为 `TRAP_CAP`。系统调用编号存储在 `siginfo` 信号处理程序参数的 `si_syscall` 字段中。其他系统调用参数可从 `ucontext_t` 读取，但系统调用编号通常存储在同时包含返回值的寄存器中，因此在信号处理程序中不可用。有关 capability 模式的更多信息，请参见 [capsicum(4)](../man4/capsicum.4.md)。

**`PROC_TRAPCAP_STATUS`** 返回指定进程对 capability 模式访问违规引发 `SIGTRAP` 的当前状态。如果启用了 `SIGTRAP` 传递，`data` 参数所指向的整型值设置为 `PROC_TRAPCAP_CTL_ENABLE` 的值；否则设置为 `PROC_TRAPCAP_CTL_DISABLE`。参见上文关于 sysctl `kern.trap_enotcap` 的注释，它提供独立的信号传递全局控制。

**`PROC_PDEATHSIG_CTL`** 请求在调用进程的父进程退出时传递信号。`idtype` 必须为 `P_PID`，`id` 必须为调用者的 pid 或零，两者效果相同。该值在子进程中以及在执行 set-user-ID 或 set-group-ID 二进制文件时被清除。`data` 必须指向一个 `int` 类型的值，指示应传递给调用者的信号。使用零可取消先前请求的信号传递。

**`PROC_PDEATHSIG_STATUS`** 查询在调用进程的父进程退出时将传递的当前信号编号。`idtype` 必须为 `P_PID`，`id` 必须为调用者的 pid 或零，两者效果相同。`data` 必须指向一个能容纳 `int` 类型值的内存位置。如果未请求信号传递，返回时将包含零。

**`PROC_STACKGAP_CTL`** 控制指定进程中的栈间隙。栈间隙是 `MAP_STACK` 映射增长区域末尾的一个或多个虚拟内存页面，被保留且永远不会由内存支持。相反，进程保证对间隙中页面的每次访问都收到同步 `SIGSEGV` 信号。为每个栈保留的页面数由 sysctl `security.bsd.stack_guard_page` 设置。间隙通过防止栈溢出破坏与栈相邻的内存来保护。`data` 参数必须指向一个包含标志的整型变量。允许以下标志：栈间隙状态在 [fork(2)](fork.2.md) 时从父进程继承。

**`PROC_STACKGAP_STATUS`** 返回指定进程的当前栈间隙状态。`data` 必须指向一个整型变量，用于返回由以下标志组成的位掩码：注意 elfctl(1) “nostackgap”标志对单个进程地址空间优先于此设置。执行设置了此标志的二进制文件永远不会在 [execve(2)](execve.2.md) 构建的地址空间中使用栈间隙。但是，控制值仍可由子进程继承，执行未设置此标志的二进制文件将恢复到控制指定的行为。

**`PROC_NO_NEW_PRIVS_CTL`** 允许在指定进程及其未来后代中忽略由 [execve(2)](execve.2.md) 激活的程序镜像上的 set-user-ID 和 set-group-ID 位。`data` 参数必须指向一个整型变量，其中包含以下值：一旦启用此控制，无法禁用。

**`PROC_NO_NEW_PRIVS_STATUS`** 返回目标进程的 set-ID 位启用当前状态。`data` 参数必须指向一个整型变量，其中写入以下值之一：

**`PROC_WXMAP_CTL`** 控制在进程地址空间中创建同时具有写和执行权限的映射。`data` 参数必须指向一个整型变量，其中包含以下值之一：如果两个标志都设置，`PROC_WX_MAPPINGS_DISALLOW_EXEC` 在 [execve(2)](execve.2.md) 期间优先。如果两个标志都未设置，仅当 `kern.elf{32/64}.allow_wx` sysctl 非零或在 ELF 控制注释中设置了 elfctl(1) “wxneeded”标志时，才允许具有写和执行权限的映射。一旦为进程启用了可写和可执行映射的创建，就无法（也毫无意义）禁用。在给定进程中启用此类映射后，确保不存在此类映射的唯一方法是设置 `PROC_WX_MAPPINGS_DISALLOW_EXEC` 标志并 [execve(2)](execve.2.md) 一个镜像。

**`PROC_WXMAP_STATUS`** 返回指定进程的关于创建同时具有写和执行权限映射的控制的当前状态。`data` 参数必须指向一个整型变量，其中写入以下值之一：此外，如果进程的地址空间不允许创建同时可写和可执行的映射，且保证自地址空间创建以来未创建此类映射，则返回值中设置 `PROC_WXORX_ENFORCE` 标志。

## x86 机器相关请求

**`PROC_KPTI_CTL_ENABLE_ON_EXEC`** 在 [execve(2)](execve.2.md) 之后启用 KPTI。

**`PROC_KPTI_CTL_DISABLE_ON_EXEC`** 在 [execve(2)](execve.2.md) 之后禁用 KPTI。仅 root 或具有 `PRIV_IO` 特权的进程可使用此选项。

**`PROC_KPTI_CTL_ENABLE_ON_EXEC`**

**`PROC_KPTI_CTL_DISABLE_ON_EXEC`**

**`PROC_KPTI_CTL`** 仅 AMD64。控制指定进程子进程的内核页表隔离（KPTI）选项。此控制仅在 KPTI 已由 `vm.pmap.kpti` 可调参数全局启用时才有意义。无法更改正在运行进程的 KPTI 设置，只能更改未来 [execve(2)](execve.2.md) 构建的新地址空间的设置。`data` 参数必须指向一个包含以下命令之一的整型变量：

**`PROC_KPTI_STATUS`** 返回指定进程的当前 KPTI 状态。`data` 必须指向一个整型变量，其中写入以下值之一：如果 KPTI 对进程的当前地址空间处于活动状态，则状态与 `PROC_KPTI_STATUS_ACTIVE` 按位或。

## 注意事项

禁用进程上的跟踪不应被视为安全功能，因为它可被内核和特权进程以及其他系统机制绕过。因此，不应利用它来可靠地保护加密密钥材料或其他机密数据。

注意，进程可以通过先将某个映射标记为可写、向其写入代码、然后移除写权限并添加执行权限来轻易绕过“不允许同时可写和可执行映射”策略。某些程序（如 JIT 编译器）可能合理地需要这样做。

## 返回值

如果发生错误，返回值为 -1，并设置 `errno` 以指示错误。

## 错误

`procctl()` 系统调用将在以下情况下失败：

**[`EFAULT`]** `data` 参数指向进程分配地址空间之外的位置。

**[`EINVAL`]** `cmd` 参数指定了不支持的命令。`idtype` 参数指定了不支持的标识符类型。

**[`EPERM`]** 调用进程没有权限对任何所选进程执行所请求的操作。

**[`ESRCH`]** 没有进程匹配所请求的 `idtype` 和 `id`。

**[`ESRCH`]** 在 `PROC_REAP_KILL` 请求中找不到匹配指定条件的后代进程。

**[`EINVAL`]** 对 `PROC_SPROTECT` 命令在 `data` 中传递了无效的操作或标志。

**[`EPERM`]** 对于 `PROC_REAP_ACQUIRE` 或 `PROC_REAP_RELEASE` 请求，`idtype` 参数不等于 `P_PID`，或 `id` 不等于调用进程的 pid。

**[`EINVAL`]** 向 `PROC_REAP_KILL` 请求传递了无效或未定义的标志。

**[`EINVAL`]** 对 `PROC_REAP_KILL` 请求指定了无效或零信号编号。

**[`EINVAL`]** 由 [init(8)](../man8/init.8.md) 进程发出 `PROC_REAP_RELEASE` 请求。

**[`EBUSY`]** 由已经是 reaper 进程的进程发出 `PROC_REAP_ACQUIRE` 请求。

**[`EBUSY`]** 对正在被跟踪的进程发出 `PROC_TRACE_CTL` 请求。

**[`EPERM`]** 重新启用进程跟踪（`PROC_TRACE_CTL_ENABLE`）或禁用 [execve(2)](execve.2.md) 上 `PROC_TRACE_CTL_DISABLE` 持久性的 `PROC_TRACE_CTL` 请求指定了非调用进程的目标进程。

**[`EINVAL`]** `PROC_TRACE_CTL` 或 `PROC_TRAPCAP_CTL` 请求的整型 `data` 参数值无效。

**[`EINVAL`]** `PROC_PDEATHSIG_CTL` 或 `PROC_PDEATHSIG_STATUS` 请求引用了不支持的 `id`、`idtype` 或无效的信号编号。

## 参见

[dtrace(1)](../man1/dtrace.1.md), elfctl(1), proccontrol(1), protect(1), [cap_enter(2)](cap_enter.2.md), [kill(2)](kill.2.md), [ktrace(2)](ktrace.2.md), [mmap(2)](mmap.2.md), [mprotect(2)](mprotect.2.md), [ptrace(2)](ptrace.2.md), [wait(2)](wait.2.md), [capsicum(4)](../man4/capsicum.4.md), [hwpmc(4)](../man4/hwpmc.4.md), [init(8)](../man8/init.8.md)

## 历史

`procctl()` 函数出现于 FreeBSD 9.3。

reaper 机制基于 Linux 和 DragonflyBSD 中的类似功能，首次出现于 FreeBSD 10.2。

`PROC_PDEATHSIG_CTL` 机制基于 Linux 中的 `prctl(PR_SET_PDEATHSIG, ...)` 功能，首次出现于 FreeBSD 11.2。

ASLR 支持为符合 checklist 而在 FreeBSD 13.0 中添加。
