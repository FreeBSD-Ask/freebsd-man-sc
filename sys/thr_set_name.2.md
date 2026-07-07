# thr_set_name(2)

`thr_set_name` — 设置用户可见的线程名称

## 名称

`thr_set_name`

## 库

Lb libc

## 概要

```c
#include <sys/thr.h>

int
thr_set_name(long id, const char *name);
```

## 描述

`thr_set_name()` 系统调用将当前进程中标识符为 `id` 的线程的用户可见名称设置为以 NUL 结尾的字符串 `name`。该名称将被静默截断以适应 `MAXCOMLEN + 1` 字节的缓冲区。线程名称可以在 [ps(1)](../man1/ps.1.md) 和 [top(1)](../man1/top.1.md) 命令的输出中、内核调试器和内核追踪设施的输出中，以及用户态调试器和程序核心转储文件中作为注释看到。

## 返回值

如果成功，`thr_set_name()` 返回零；否则返回 -1，并设置 `errno` 以指示错误。

## 错误

`thr_set_name()` 系统调用可能返回以下错误：

**[`EFAULT`]** `name` 参数指向的内存无效。

**[`ESRCH`]** 当前进程中不存在标识符为 `id` 的线程。

## 参见

[ps(1)](../man1/ps.1.md), [_umtx_op(2)](_umtx_op.2.md), [thr_exit(2)](thr_exit.2.md), [thr_kill(2)](thr_kill.2.md), thr_kill2(2), [thr_new(2)](thr_new.2.md), [thr_self(2)](thr_self.2.md), [pthread_set_name_np(3)](../man3/pthread_set_name_np.3.md), [ddb(4)](../man4/ddb.4.md), [ktr(9)](../man9/ktr.9.md)

## 标准

`thr_set_name()` 系统调用是非标准的，由 Lb libthr 使用。

## 历史

`thr_set_name()` 系统调用首次出现于 FreeBSD 5.2。
