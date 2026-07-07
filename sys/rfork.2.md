# rfork(2)

`rfork` — 操作进程资源

## 名称

`rfork`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
rfork(int flags);
```

## 描述

fork、vfork 或 rfork 是创建新进程的唯一方式。`rfork()` 的 `flags` 参数选择调用进程（父进程）的哪些资源由新进程（子进程）共享或初始化为默认值。这些资源包括打开的文件描述符表（共享时允许进程为其他进程打开和关闭文件）以及打开的文件。`flags` 参数为 `RFSPAWN` 或以下某些子集的逻辑或：

**`RFPROC`** 如果设置，则创建新进程；否则更改影响当前进程。

**`RFNOWAIT`** 如果设置，子进程将与父进程分离。退出时，子进程不会留下状态供父进程收集。参见 [wait(2)](wait.2.md)。

**`RFFDG`** 如果设置，调用者的文件描述符表（参见 [intro(2)](intro.2.md)）被复制；否则两个进程共享一个表。

**`RFCFDG`** 如果设置，新进程以一个干净的文件描述符表启动。与 `RFFDG` 互斥。

**`RFTHREAD`** 如果设置，新进程与其父进程共享文件描述符到进程领导者表。仅在未设置 `RFFDG` 和 `RFCFDG` 时适用。

**`RFMEM`** 如果设置，内核将强制共享整个地址空间，通常通过直接共享硬件页表实现。因此，子进程将继承并共享父进程拥有的所有段，无论它们通常是否可共享。堆栈段不会被分割（父进程和子进程在同一个堆栈上返回），因此带 RFMEM 标志的 `rfork()` 通常不能直接从包括 C 在内的高级语言调用。只能在设置 `RFPROC` 时使用。提供了一个辅助函数来解决此问题，它将使新进程在提供的堆栈上运行。参见 [rfork_thread(3)](../sys-1/rfork_thread.3.md) 获取信息。注意，许多代码在此环境中无法正确运行。

**`RFSIGSHARE`** 如果设置，内核将强制在子进程和父进程之间共享 sigacts 结构。

**`RFTSIGZMB`** 如果设置，内核将在子进程退出时向父进程传递指定的信号，而非默认的 SIGCHLD。信号编号 `signum` 通过将 `RFTSIGFLAGS(signum)` 表达式按位或到 `flags` 中来指定。指定信号编号 0 将禁用子进程退出时的信号传递。

**`RFLINUXTHPN`** 如果设置，内核将在子进程的线程退出时传递 SIGUSR1 而非 SIGCHLD。这旨在模拟某些 Linux clone 行为。

共享文件描述符表中的文件描述符保持打开，直到它们被显式关闭或共享该表的所有进程退出。

如果传递 `RFSPAWN`，`rfork` 将使用 [vfork(2)](vfork.2.md) 语义，但将子进程中的所有信号操作重置为默认值。此标志由 libc 中的 [posix_spawn(3)](../gen/posix_spawn.3.md) 实现使用。

如果设置 `RFPROC`，父进程中返回的值是子进程的进程 id；子进程中返回的值为零。不设置 `RFPROC` 时，返回值为零。进程 id 的范围从 1 到最大整数（`int`）值。如有必要，`rfork()` 系统调用将休眠，直到所需的进程资源可用。

`fork()` 系统调用可以实现为对 `rfork(RFFDG | RFPROC)` 的调用，但由于向后兼容性原因并未如此实现。

## 返回值

成功完成时，`rfork()` 向子进程返回值 0，向父进程返回子进程的进程 ID。否则，向父进程返回 -1，不创建子进程，并设置全局变量 `errno` 以指示错误。

## 错误

`rfork()` 系统调用在以下情况下会失败，且不创建子进程：

**[`EAGAIN`]** 将超过系统对执行中进程总数的限制。该限制由 [sysctl(3)](../gen/sysctl.3.md) MIB 变量 `KERN_MAXPROC` 给出。（除超级用户外，实际限制比此值少十个。）

**[`EAGAIN`]** 用户不是超级用户，且将超过系统对单个用户执行中进程总数的限制。该限制由 [sysctl(3)](../gen/sysctl.3.md) MIB 变量 `KERN_MAXPROCPERUID` 给出。

**[`EAGAIN`]** 用户不是超级用户，且将超过对应于 `resource` 参数 `RLIMIT_NOFILE` 的软资源限制（参见 [getrlimit(2)](getrlimit.2.md)）。

**[`EINVAL`]** 同时指定了 RFFDG 和 RFCFDG 标志。

**[`EINVAL`]** 指定了上面未列出的任何标志。

**[`EINVAL`]** 指定了无效的信号编号。

**[`ENOMEM`]** 新进程的交换空间不足。

## 参见

[fork(2)](fork.2.md), [intro(2)](intro.2.md), [minherit(2)](minherit.2.md), [pdrfork(2)](pdfork.2.md), [vfork(2)](vfork.2.md), [pthread_create(3)](../man3/pthread_create.3.md), [rfork_thread(3)](../sys-1/rfork_thread.3.md)

## 历史

`rfork()` 函数首次出现于 Plan9。