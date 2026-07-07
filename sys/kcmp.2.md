# kcmp(2)

`kcmp` — 比较两个内核对象

## 名称

`kcmp`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
kcmp(pid_t pid1, pid_t pid2, int type, uintptr_t idx1, uintptr_t idx2);
```

## 描述

`kcmp()` 系统调用允许调用者确定具有 PID `pid1` 和 `pid2` 的两个进程是否引用同一个内核对象。`type` 参数指定对象的类型，`idx1` 和 `idx2` 是分别在进程 `pid1` 和 `pid2` 上下文中引用某个对象的标识符。

可以为 `type` 指定以下值：

**`KCMP_FILE`** 比较由文件描述符 `idx1` 和 `idx2` 所引用的两个文件描述（file description）。例如，如果其中一个描述符是通过将 [dup(2)](dup.2.md) 应用于另一个描述符创建的，则它们可能是等价的。

**`KCMP_FILEOBJ`** 对由文件描述符 `idx1` 和 `idx2` 所引用的文件描述执行“深度比较”。这测试文件描述所引用的底层对象是否相同。例如，如果同一文件系统路径被打开两次，内核将创建两个独立的文件描述来支持这两个文件描述符，但它们将引用同一底层对象，即一个 [vnode(9)](../man9/vnode.9.md)。当使用 `KCMP_FILE` 类型比较时，这些描述符将是不同的，但使用 `KCMP_FILEOBJ` 类型比较时，它们将是相等的（假设路径在两次打开之间未被取消链接）。

**`KCMP_FILES`** 确定两个进程是否共享同一文件描述符表。如果一个进程是通过 [rfork(2)](rfork.2.md) 创建且未指定 `RFFDG` 标志，则属于此情况。`idx1` 和 `idx2` 参数将被忽略。

**`KCMP_SIGHAND`** 确定两个进程是否共享同一信号处理程序表。如果一个进程是使用 [rfork(2)](rfork.2.md) 的 `RFSIGSHARE` 标志创建的，则属于此情况。`idx1` 和 `idx2` 参数将被忽略。

**`KCMP_VM`** 确定两个进程是否共享虚拟内存地址空间。如果一个进程通过 [vfork(2)](vfork.2.md) 或带 `RFMEM` 标志的 [rfork(2)](rfork.2.md) 创建了另一个进程，则可能属于此情况。`idx1` 和 `idx2` 参数将被忽略。

`kcmp()` 的调用者必须有权调试这两个进程，否则系统调用将失败。

## 返回值

如果 `idx1` 和 `idx2` 引用同一对象，`kcmp()` 返回 0。如果 `pid1` 和 `idx1` 所引用的对象小于或大于 `pid2` 和 `idx2` 所引用的对象，`kcmp()` 分别返回值 1 和 2。该顺序由内核内部定义，并且在系统重新启动之前是稳定的。如果由于某种原因无法比较这两个对象，`kcmp()` 返回 3。例如，如果 `type` 为 `KCMP_FILEOBJ` 且 `idx1` 和 `idx2` 是不同的描述符类型（例如一个套接字和一个文件），则 `kcmp()` 将返回 3。

如果发生错误，返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`kcmp()` 可能因以下错误而失败：

**[`ENODEV`]** 指定了 `KCMP_FILEOBJ`，且 `idx1` 引用的文件描述符未实现比较运算符。

**[`EINVAL`]** `type` 的值无效。

**[`EBADF`]** `idx1` 或 `idx2` 所引用的某个文件描述符无效。

**[`ESRCH`]** `pid1` 或 `pid2` 所引用的某个进程不存在或不可见（例如由于 jail 限制）。

**[`EPERM`]** 调用者无权访问 `pid1` 或 `pid2` 所引用的某个进程。

## 参见

[dup(2)](dup.2.md), [fcntl(2)](fcntl.2.md), [fork(2)](fork.2.md), [rfork(2)](rfork.2.md), [vfork(2)](vfork.2.md)

## 标准

`kcmp()` 系统调用起源于 Linux。此实现旨在与 Linux 实现源码兼容。FreeBSD 仅实现了 Linux 支持的 `type` 可能值的子集。未来可能添加更多值。`KCMP_FILEOBJ` 类型是 FreeBSD 的扩展。

## 历史

`kcmp()` 函数引入于 FreeBSD 14.1。
