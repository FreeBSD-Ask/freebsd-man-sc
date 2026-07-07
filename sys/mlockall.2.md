# mlockall(2)

`mlockall` — 锁定（解锁）进程的地址空间

## 名称

`mlockall`, `munlockall`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
mlockall(int flags);

int
munlockall(void);
```

## 描述

`mlockall()` 系统调用将与进程地址空间关联的物理页面锁定在内存中，直到地址空间被解锁、进程退出，或执行了另一个程序映像。

以下标志影响 `mlockall()` 的行为：

**`MCL_CURRENT`** 锁定当前映射到进程地址空间的所有页面。

**`MCL_FUTURE`** 在建立映射时，锁定将来映射到进程地址空间的所有页面。注意，如果这些映射会导致资源限制被超出，则可能导致将来的映射失败。

由于物理内存是一种潜在稀缺资源，进程可锁定的内存量受到限制。单个进程可锁定的内存量为系统级“驻留页面”限制 `vm.max_user_wired` 与每进程 `RLIMIT_MEMLOCK` 资源限制两者中的较小值。

如果 `security.bsd.unprivileged_mlock` 设置为 0，则这些调用仅对超级用户可用。如果 `vm.old_mlock` 设置为 1，则每进程 `RLIMIT_MEMLOCK` 资源限制不会应用于 `mlockall()` 调用。

`munlockall()` 调用解锁进程地址空间中所有已锁定的内存区域。在 `munlockall()` 调用之后映射的任何区域都不会被锁定。

## 返回值

返回值 0 表示调用成功，范围内的所有页面已被锁定或解锁。返回值 -1 表示发生错误，范围内所有页面的锁定状态保持不变。此时，全局变量 `errno` 被设置以指示错误。

## 错误

`mlockall()` 在以下情况下会失败：

**[`EINVAL`]** `flags` 参数为零，或包含未实现的标志。

**[`ENOMEM`]** 锁定指定范围将超过系统或每进程的锁定内存限制。

**[`EAGAIN`]** 调用时，映射到进程地址空间的部分或全部内存无法被锁定。

**[`EPERM`]** 调用进程没有执行所请求操作的适当权限。

## 参见

[mincore(2)](mincore.2.md), [mlock(2)](mlock.2.md), [mmap(2)](mmap.2.md), [munmap(2)](munmap.2.md), [setrlimit(2)](getrlimit.2.md)

## 标准

`mlockall()` 和 `munlockall()` 函数被认为符合 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`mlockall()` 和 `munlockall()` 函数首次出现于 FreeBSD 5.1。

## 缺陷

锁定内存的每进程和系统级资源限制应用于锁定的虚拟内存量，而非锁定的物理页面量。因此，同一物理页面的两个不同锁定映射在系统限制中计为 2 个页面，如果两个映射属于同一个物理映射，则也计入每进程限制。
