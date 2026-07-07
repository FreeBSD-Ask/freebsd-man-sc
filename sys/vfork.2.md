# vfork(2)

`vfork` — 创建不复制地址空间的新进程

## 名称

`vfork`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
pid_t
vfork(void);
```

## 描述

由于此函数在应用软件中难以正确使用，建议改用 [posix_spawn(3)](../gen/posix_spawn.3.md) 或 [fork(2)](fork.2.md)。

`vfork()` 系统调用可用于创建新进程而无需完整复制原进程的地址空间，这在分页环境下效率低下。当 [fork(2)](fork.2.md) 的目的是为 [execve(2)](execve.2.md) 创建新的系统上下文时，`vfork()` 很有用。`vfork()` 系统调用与 [fork(2)](fork.2.md) 的不同之处在于，子进程借用父进程的地址空间和调用线程的栈，直到调用 [execve(2)](execve.2.md) 或退出（通过调用 [_exit(2)](_exit.2.md) 或异常退出）。子进程使用其资源时，调用线程会被挂起。其他线程继续运行。

`vfork()` 系统调用在子进程上下文中返回 0，在父进程上下文中（稍后）返回子进程的 PID。

用 `vfork()` 替代 [fork(2)](fork.2.md) 时可能出现许多问题。例如，在子进程上下文中从调用 `vfork()` 的过程中返回是不行的，因为 `vfork()` 最终返回时会返回到一个不再存在的栈帧。此外，更改部分在用户空间实现进程状态（例如使用 `libthr(3)` 的信号处理程序）会破坏父进程的状态。

如果不能调用 [execve(2)](execve.2.md)，还需注意要调用 [_exit(2)](_exit.2.md) 而非 [exit(3)](../stdlib/exit.3.md)，因为 [exit(3)](../stdlib/exit.3.md) 会刷新并关闭标准 I/O 通道，从而搞乱父进程的标准 I/O 数据结构。（即使使用 [fork(2)](fork.2.md)，调用 [exit(3)](../stdlib/exit.3.md) 也是错误的，因为缓冲数据会被刷新两次。）

## 返回值

与 [fork(2)](fork.2.md) 相同。

## 参见

[_exit(2)](_exit.2.md), [execve(2)](execve.2.md), [fork(2)](fork.2.md), [rfork(2)](rfork.2.md), [sigaction(2)](sigaction.2.md), [wait(2)](wait.2.md), [exit(3)](../stdlib/exit.3.md), [posix_spawn(3)](../gen/posix_spawn.3.md)

## 历史

`vfork()` 系统调用出现于 3BSD。

## 缺陷

为避免可能的死锁情况，处于 `vfork()` 中间的子进程永远不会被发送 `SIGTTOU` 或 `SIGTTIN` 信号；相反，输出或 [ioctl(2)](ioctl.2.md) 调用被允许，而输入尝试会导致文件结束指示。
