# proc_rwmem(9)

`proc_rwmem` — 读取或写入进程地址空间

## 名称

`proc_rwmem`, `proc_readmem`, `proc_writemem`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/ptrace.h>
```

```c
int
proc_rwmem(struct proc *p, struct uio *uio)

ssize_t
proc_readmem(struct thread *td, struct proc *p, vm_offset_t va, void *buf, size_t len)

ssize_t
proc_writemem(struct thread *td, struct proc *p, vm_offset_t va, void *buf, size_t len)
```

## 描述

这些函数用于读取或写入进程 `p` 的地址空间。`proc_rwmem` 函数要求调用者使用 [uio(9)](uio.9.md) 中描述的 `struct uio` 指定 I/O 参数。`proc_readmem` 和 `proc_writemem` 函数提供了更简单、更少通用的接口，允许调用者从 `p` 地址空间中偏移量为 `va` 的内存读取到内核缓冲区 `buf`（大小为 `len`）或从该缓冲区写入。该操作代表线程 `td` 执行，大多数情况下为当前线程。

这些函数可能会休眠，因此不能在持有任何不可休眠锁时调用。进程 `p` 必须由调用者使用 [PHOLD(9)](phold.9.md) 持有。

## 返回值

`proc_rwmem` 函数成功时返回 `0`。如果指定的用户地址无效，返回 `EFAULT`；如果由于资源短缺而无法将目标页面换入，返回 `ENOMEM`。

`proc_readmem` 和 `proc_writemem` 函数分别返回读取或写入的字节数。这可能小于请求的字节数，例如，如果请求跨越进程地址空间中的多个页面，且其中第一个之后的某个页面未映射。否则，返回 -1。

## 参见

[copyin(9)](copy.9.md), [locking(9)](locking.9.md), [PHOLD(9)](phold.9.md), [uio(9)](uio.9.md)

## 作者

本手册页由 Mark Johnston <markj@FreeBSD.org> 编写。
