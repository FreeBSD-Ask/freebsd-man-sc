# mlock(2)

`mlock`, `munlock` — 锁定（解锁）物理内存页

## 名称

`mlock`, `munlock`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
mlock(const void *addr, size_t len);

int
munlock(const void *addr, size_t len);
```

## 描述

`mlock()` 系统调用将从 `addr` 开始、长度为 `len` 字节的虚拟地址范围所对应的物理内存页锁定在内存中。`munlock()` 系统调用解锁此前由一次或多次 `mlock()` 调用锁定的内存页。对于两者，`addr` 参数应与页面大小的倍数对齐。如果 `len` 参数不是页面大小的倍数，将被向上取整为页面大小的倍数。整个范围必须已分配。

在 `mlock()` 系统调用之后，所指示的内存页在解锁之前将不会产生非驻留页故障或地址转换故障。在采用软件管理 TLB 的架构上，仍可能产生保护违规故障或 TLB 未命中故障。在所有锁定映射被移除之前，物理内存页将一直保留在内存中。多个进程可以通过各自的虚拟地址映射锁定相同的物理内存页。单个进程同样可以通过同一物理页面的不同虚拟映射多次锁定同一页面。解锁可通过 `munlock()` 显式执行，也可通过 `munmap()` 调用隐式执行，后者会释放未映射的地址范围。锁定的映射不会在 [fork(2)](fork.2.md) 之后被子进程继承。

由于物理内存可能是稀缺资源，进程可锁定的内存量受到限制。单个进程可通过 `mlock()` 锁定的内存量受每进程的 `RLIMIT_MEMLOCK` 资源限制和系统范围的 "wired pages"（已驻留页）限制 `vm.max_user_wired` 的双重约束。`vm.max_user_wired` 适用于整个系统，因此在任何给定时刻单个进程可用的量为 `vm.max_user_wired` 与 `vm.stats.vm.v_user_wire_count` 之差。

如果 `security.bsd.unprivileged_mlock` 设置为 0，则这些调用仅对超级用户可用。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

如果调用成功，范围内的所有内存页都将变为锁定（解锁）状态；否则范围内所有内存页的锁定状态保持不变。

## 错误

`mlock()` 系统调用在以下情况下会失败：

**[`EPERM`]** `security.bsd.unprivileged_mlock` 设置为 0，且调用者不是超级用户。

**[`EINVAL`]** 给定的地址范围环绕零值。

**[`ENOMEM`]** 所指示地址范围的某些部分未分配。在缺页/映射页面时发生错误。锁定所指示的范围将超出每进程或系统范围的锁定内存限制。

`munlock()` 系统调用在以下情况下会失败：

**[`EPERM`]** `security.bsd.unprivileged_mlock` 设置为 0，且调用者不是超级用户。

**[`EINVAL`]** 给定的地址范围环绕零值。

**[`ENOMEM`]** 由 addr 和 len 参数指定的部分或全部地址范围不对应于进程地址空间中有效的已映射页面。

**[`ENOMEM`]** 锁定由指定范围映射的页面将超出进程可锁定内存量的限制。

## 参见

[fork(2)](fork.2.md), [mincore(2)](mincore.2.md), [minherit(2)](minherit.2.md), [mlockall(2)](mlockall.2.md), [mmap(2)](mmap.2.md), [munlockall(2)](munlockall.2.md), [munmap(2)](munmap.2.md), [setrlimit(2)](setrlimit.2.md), [getpagesize(3)](../man3/getpagesize.3.md)

## 历史

`mlock()` 和 `munlock()` 系统调用首次出现于 4.4BSD。

## 缺陷

分配过多的 wired 内存可能导致内存分配死锁，需要重启才能恢复。

锁定内存的每进程和系统范围资源限制适用于锁定的虚拟内存量，而非锁定的物理页数。因此，同一物理页面的两个不同锁定映射在系统限制中计为 2 页，如果两个映射属于同一物理映射，则在每进程限制中也计为 2 页。

目前不支持每进程资源限制。
