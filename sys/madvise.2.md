# madvise(2)

`madvise` — 提供关于内存使用的建议

## 名称

`madvise`, `posix_madvise`

## 库

Lb libc

## 概要

`#include <sys/mman.h>`

```c
int
madvise(void *addr, size_t len, int behav);

int
posix_madvise(void *addr, size_t len, int behav);
```

## 描述

`madvise()` 系统调用允许了解自身内存行为的进程将其行为描述告知系统。`posix_madvise()` 接口与之相同，区别在于它在出错时返回错误码且不修改 `errno`，提供它是为了符合标准。

已知的行为如下：

**`MADV_NORMAL`** 告知系统恢复默认的页面调度行为。

**`MADV_RANDOM`** 提示页面将被随机访问，预取可能没有益处。

**`MADV_SEQUENTIAL`** 使 VM 系统在某个页面被缺页调入时，降低紧邻该页面之前的页面的优先级。

**`MADV_WILLNEED`** 使给定虚拟地址范围内的页面临时获得更高的优先级，如果它们在内存中，则降低被释放的可能性。此外，已经在内存中的页面会立即映射到进程中，从而消除经过整个缺页调入过程的不必要开销。这不会从后备存储中调入页面，而是快速将已在内存中的页面映射到调用进程。

**`MADV_DONTNEED`** 允许 VM 系统降低指定地址范围内页面在内存中的优先级。因此，未来对该地址范围的引用更可能引发缺页。

**`MADV_FREE`** 给予 VM 系统释放页面的自由，并告知系统指定页面范围内的信息不再重要。这是一种允许 [malloc(3)](../man3/malloc.3.md) 在地址空间的任何位置释放页面同时保持地址空间有效的高效方式。下次引用该页面时，该页面可能被按需置零，也可能包含 `MADV_FREE` 调用之前的数据。对该地址空间范围的引用不会使 VM 系统从后备存储中重新调入信息，直到该页面再次被修改。

**`MADV_NOSYNC`** 请求系统除非必要，否则不要将与此映射关联的数据刷新到物理后备存储。通常，这会阻止文件系统更新守护进程将 VM 系统弄脏的页面无谓地写入物理磁盘。注意，VM/文件系统的一致性始终得到维护，此功能只是确保映射数据仅在需要时才被刷新，通常由系统分页器执行。此功能通常用于你想使用文件支持的共享内存区域在进程间通信（IPC），且并不特别需要存储在该区域中的数据被物理写入磁盘的情况。借助此功能，你可以获得与 mmap 相当的性能，类似于 SysV 共享内存调用所能提供的性能，但方式更可控、限制更少。但是，请注意此功能在 UNIX 平台之间不可移植（尽管有些平台默认可能做正确的事）。更多信息请参见 [mmap(2)](mmap.2.md) 的 MAP_NOSYNC 部分。

**`MADV_AUTOSYNC`** 撤销地址范围内未来被弄脏页面的 MADV_NOSYNC 效果。对已经被弄脏页面的效果是不确定的——它们可能被恢复，也可能不被恢复。可以通过使用 [msync(2)](msync.2.md) 或 [fsync(2)](fsync.2.md) 系统调用来保证恢复。

**`MADV_NOCORE`** 该区域不包含在 core 文件中。

**`MADV_CORE`** 将该区域包含在 core 文件中。

**`MADV_PROTECT`** 通知 VM 系统当交换空间耗尽时不应终止此进程。该进程必须具有超级用户权限。这应在系统正常运行所必需的进程中谨慎使用。

调用 `posix_madvise()` 接口的可移植程序应使用别名 `POSIX_MADV_NORMAL`、`POSIX_MADV_SEQUENTIAL`、`POSIX_MADV_RANDOM`、`POSIX_MADV_WILLNEED` 和 `POSIX_MADV_DONTNEED`，而非上述标志。

## 返回值

`madvise()` 成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。`posix_madvise()` 成功时返回 0；失败时直接返回错误码，不设置 `errno`。

## 错误

`madvise()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `behav` 参数无效。

**[`ENOMEM`]** 由 `addr` 和 `len` 参数指定的虚拟地址范围无效。

**[`EPERM`]** 指定了 `MADV_PROTECT` 但进程没有超级用户权限。

## 参见

[mincore(2)](mincore.2.md), [mprotect(2)](mprotect.2.md), [msync(2)](msync.2.md), [munmap(2)](munmap.2.md), [posix_fadvise(2)](posix_fadvise.2.md)

## 标准

`posix_madvise()` 接口遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 历史

`madvise()` 系统调用首次出现于 4.4BSD。