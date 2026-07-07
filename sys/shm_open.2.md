# shm_open(2)

`shm_open` — 共享内存对象操作

## 名称

`memfd_create`, `shm_create_largepage`, `shm_open`, `shm_rename`, `shm_unlink`

## 库

Lb libc

## 概要

```c
#include <sys/types.h>
#include <sys/mman.h>
#include <fcntl.h>

int
memfd_create(const char *name, unsigned int flags);

int
shm_create_largepage(const char *path, int flags, int psind,
    int alloc_policy, mode_t mode);

int
shm_open(const char *path, int flags, mode_t mode);

int
shm_rename(const char *path_from, const char *path_to, int flags);

int
shm_unlink(const char *path);
```

## 描述

`shm_open()` 函数打开（或可选地创建）名为 `path` 的 POSIX 共享内存对象。`flags` 参数包含 [open(2)](open.2.md) 所使用标志的子集。`flags` 中必须包含 `O_RDONLY` 或 `O_RDWR` 访问模式之一。还可以指定可选标志 `O_CREAT`、`O_EXCL`、`O_TRUNC` 和 `O_CLOFORK`。

如果指定了 `O_CREAT`，则当名为 `path` 的共享内存对象不存在时将创建一个新的共享内存对象。在这种情况下，共享内存对象以模式 `mode` 创建，并受进程的 umask 值约束。如果同时指定了 `O_CREAT` 和 `O_EXCL` 标志，且名为 `path` 的共享内存对象已存在，则 `shm_open()` 将失败并返回 `EEXIST`。

新创建的对象初始大小为零。如果以 `O_RDWR` 打开现有的共享内存对象并指定了 `O_TRUNC` 标志，则该共享内存对象将被截断为零大小。对象的大小可以通过 ftruncate(2) 调整，并通过 fstat(2) 查询。

新描述符被设置为在 [execve(2)](execve.2.md) 系统调用期间关闭；参见 [close(2)](close.2.md) 和 [fcntl(2)](fcntl.2.md)。

常量 `SHM_ANON` 可用作 `shm_open()` 的 `path` 参数。在这种情况下，将创建一个匿名的、未命名的共享内存对象。由于该对象没有名称，无法通过后续调用 `shm_unlink()` 来移除，也无法通过调用 `shm_rename()` 来移动。相反，当对共享内存对象的最后一个引用被移除时，该共享内存对象将被垃圾回收。可以通过 [fork(2)](fork.2.md) 或 sendmsg(2) 共享文件描述符来与其他进程共享该共享内存对象。尝试以 `O_RDONLY` 打开匿名共享内存对象将失败并返回 `EINVAL`。所有其他标志将被忽略。

`shm_create_largepage()` 函数的行为类似于 `shm_open()`，不同之处在于隐式指定了 `O_CREAT` 标志，并且返回的“largepage”对象始终由对齐的、物理连续的内存块支持。这确保了该对象可以使用所谓的“超级页”进行映射，在某些工作负载中，通过减少访问对象映射所需的转换后备缓冲器（TLB）条目数量，以及减少访问映射时发生的缺页次数，可以提高应用程序性能。这对所有 largepage 对象自动发生。

可以使用 `shm_open()` 函数打开现有的 largepage 对象。Largepage 共享内存对象的行为与非 largepage 对象略有不同：

- largepage 对象的内存是在使用 ftruncate(2) 系统调用扩展对象时分配的，而常规共享内存对象的内存是惰性分配的，并且在未使用时可以被换出到交换设备。
- largepage 对象映射的大小必须是底层大页大小的倍数。此类映射的大多数属性只能以大页大小的粒度进行修改。例如，当使用 [munmap(2)](munmap.2.md) 取消映射 largepage 对象映射的一部分时，或者当使用 [mprotect(2)](mprotect.2.md) 调整 largepage 对象映射的保护属性时，起始地址必须是大页大小对齐的，且操作的长度必须是大页大小的倍数。否则，相应的系统调用将失败并将 `errno` 设置为 `EINVAL`。

`shm_create_largepage()` 的 `psind` 参数指定用于支持对象的大页大小。此参数是 [getpagesizes(3)](../man3/getpagesizes.3.md) 返回的页大小数组的索引。特别地，支持 largepage 对象的所有大页必须具有相同的大小。例如，在具有 2MB 和 1GB 大页大小的系统上，一个 2GB 的 largepage 对象将由 1024 个 2MB 页或 2 个 1GB 页组成，具体取决于 `psind` 参数指定的值。`alloc_policy` 参数指定当尝试使用 ftruncate(2) 为对象分配内存失败时会发生什么。接受以下值：

**`SHM_LARGEPAGE_ALLOC_DEFAULT`** 如果（非阻塞）内存分配因空闲连续内存不足而失败，内核将尝试对物理内存进行碎片整理并再次尝试分配。后续分配可能成功也可能失败。如果此后续分配也失败，ftruncate(2) 将失败并将 `errno` 设置为 `ENOMEM`。

**`SHM_LARGEPAGE_ALLOC_NOWAIT`** 如果内存分配失败，ftruncate(2) 将失败并将 `errno` 设置为 `ENOMEM`。

**`SHM_LARGEPAGE_ALLOC_HARD`** 内核将持续尝试碎片整理直到分配成功，或者一个未阻塞的信号被传递到线程。然而，物理内存可能碎片化严重，导致分配永远无法成功。

`FIOSSHMLPGCNF` 和 `FIOGSHMLPGCNF` [ioctl(2)](ioctl.2.md) 命令可用于 largepage 共享内存对象，以获取和设置 largepage 对象参数。这两个命令操作以下结构：

```c
struct shm_largepage_conf {
	int psind;
	int alloc_policy;
};
```

`FIOGSHMLPGCNF` 命令使用这些参数的当前值填充此结构，而 `FIOSSHMLPGCNF` 命令修改 largepage 对象。目前只有 `alloc_policy` 参数可以被修改。在内部，`shm_create_largepage()` 通过使用 `shm_open()` 创建常规共享内存对象，然后使用 `FIOSSHMLPGCNF` ioctl 命令将其转换为 largepage 对象来工作。

`shm_rename()` 系统调用原子地移除名为 `path_from` 的共享内存对象，并将其重新链接到 `path_to`。如果另一个对象已经链接到 `path_to`，该对象将被取消链接，除非提供了以下标志之一：

**`SHM_RENAME_EXCHANGE`** 原子地交换 `path_from` 和 `path_to` 处的共享内存对象。

**`SHM_RENAME_NOREPLACE`** 如果 `path_to` 处已存在共享内存对象，则返回错误，而不是将其取消链接。

`shm_unlink()` 系统调用移除名为 `path` 的共享内存对象。

`memfd_create()` 函数创建一个匿名共享内存对象，与指定 `SHM_ANON` 时由 `shm_open()` 创建的对象相同。新创建的对象初始大小为零。新对象的大小必须通过 ftruncate(2) 调整。

`name` 参数不能为 `NULL`，但可以是空字符串。`name` 参数的长度不得超过 `NAME_MAX` 减去六个字符（用于将被前置的前缀“memfd:”）。`name` 参数仅用于调试目的，内核永远不会使用它来标识 memfd。因此，名称不需要唯一。

可以为 `memfd_create()` 指定以下 `flags`：

**`MFD_CLOEXEC`** 在生成的文件描述符上设置 `FD_CLOEXEC`。

**`MFD_ALLOW_SEALING`** 允许使用 `F_ADD_SEALS` [fcntl(2)](fcntl.2.md) 命令向生成的文件描述符添加封印。

**`MFD_HUGETLB`** 创建由“largepage”对象支持的 memfd。可以包含 `<sys/mman.h>` 中定义的 `MFD_HUGE_*` 标志之一来指定固定大小。如果未请求特定大小，则选择支持的最小大页大小。上文记录的 `shm_create_largepage()` `psind` 参数的行为同样适用于由 `memfd_create()` 创建的 largepage 对象，并且将始终使用 `SHM_LARGEPAGE_ALLOC_DEFAULT` 策略。

## 返回值

如果成功，`memfd_create()` 和 `shm_open()` 都返回一个非负整数，`shm_rename()` 和 `shm_unlink()` 返回零。所有函数在失败时返回 -1，并设置 `errno` 以指示错误。

## 兼容性

`shm_create_largepage()` 和 `shm_rename()` 函数是 FreeBSD 扩展，`shm_open()` 中对 `SHM_ANON` 值的支持也是 FreeBSD 扩展。

`path`、`path_from` 和 `path_to` 参数不一定表示路径名（尽管在大多数其他实现中确实如此）。当且仅当 `path` 以斜杠（`/`）字符开头时，打开相同 `path` 的两个进程才能保证访问相同的共享内存对象。

在可移植程序中只能使用 `O_RDONLY`、`O_RDWR`、`O_CREAT`、`O_EXCL` 和 `O_TRUNC` 标志。

POSIX 规范指出，对共享内存对象或 `shm_open()` 返回的描述符使用 [open(2)](open.2.md)、[read(2)](read.2.md) 或 [write(2)](write.2.md) 的结果是未定义的。然而，FreeBSD 内核实现明确包含对 [read(2)](read.2.md) 和 [write(2)](write.2.md) 的支持。

FreeBSD 还支持使用 [sendfile(2)](sendfile.2.md) 从共享内存对象进行数据的零拷贝传输。

共享内存对象及其内容都不会在重启后持久存在。

写入不会扩展共享内存对象，因此在写入任何数据之前必须调用 ftruncate(2)。参见[实例](#实例)。

## 实例

此示例如果不调用 ftruncate(2) 将会失败：

```c
uint8_t buffer[getpagesize()];
ssize_t len;
int fd;

fd = shm_open(SHM_ANON, O_RDWR | O_CREAT, 0600);
if (fd < 0)
	err(EX_OSERR, "%s: shm_open", __func__);
if (ftruncate(fd, getpagesize()) < 0)
	err(EX_IOERR, "%s: ftruncate", __func__);
len = pwrite(fd, buffer, getpagesize(), 0);
if (len < 0)
	err(EX_IOERR, "%s: pwrite", __func__);
if (len != getpagesize())
	errx(EX_IOERR, "%s: pwrite length mismatch", __func__);
```

## 错误

`memfd_create()` 在以下条件下失败并返回这些错误代码：

**[`EBADF`]** `name` 参数为 NULL。

**[`EINVAL`]** `name` 参数过长。`flags` 中包含无效或不支持的标志。

**[`EINVAL`]** 请求了 hugetlb 映射，但 `flags` 中未指定 `MFD_HUGETLB`。

**[`EMFILE`]** 进程已达到其打开文件描述符的限制。

**[`ENFILE`]** 系统文件表已满。

**[`ENOSYS`]** `flags` 中指定了 `MFD_HUGETLB`，而此系统不支持强制 hugetlb 映射。

**[`EOPNOTSUPP`]** 此系统不支持所请求的 hugetlb 页大小。

`shm_open()` 在以下条件下失败并返回这些错误代码：

**[`EINVAL`]** `flags` 中包含 `O_RDONLY`、`O_RDWR`、`O_CREAT`、`O_EXCL` 或 `O_TRUNC` 以外的标志。

**[`EMFILE`]** 进程已达到其打开文件描述符的限制。

**[`ENFILE`]** 系统文件表已满。

**[`EINVAL`]** 通过 `SHM_ANON` 创建匿名共享内存对象时指定了 `O_RDONLY`。

**[`EFAULT`]** `path` 参数指向进程已分配地址空间之外。

**[`ENAMETOOLONG`]** 整个路径名超过 1023 个字符。

**[`EINVAL`]** `path` 不以斜杠（`/`）字符开头。

**[`ENOENT`]** 未指定 `O_CREAT` 且命名的共享内存对象不存在。

**[`EEXIST`]** 指定了 `O_CREAT` 和 `O_EXCL`，且命名的共享内存对象确实存在。

**[`EACCES`]** 所需权限（读取或读写）被拒绝。

**[`ECAPMODE`]** 进程正在能力模式下运行（参见 [capsicum(4)](../man4/capsicum.4.md)），并尝试创建命名的共享内存对象。

`shm_create_largepage()` 可能因上述列出的原因而失败。它在以下条件下还会失败并返回这些错误代码：

**[`ENOTTY`]** 内核在当前平台上不支持大页。

以下错误针对 `shm_rename()` 定义：

**[`EFAULT`]** `path_from` 或 `path_to` 参数指向进程已分配地址空间之外。

**[`ENAMETOOLONG`]** 整个路径名超过 1023 个字符。

**[`ENOENT`]** `path_from` 处的共享内存对象不存在。

**[`EACCES`]** 所需权限被拒绝。

**[`EEXIST`]** `path_to` 处已存在共享内存对象，且提供了 `SHM_RENAME_NOREPLACE` 标志。

`shm_unlink()` 在以下条件下失败并返回这些错误代码：

**[`EFAULT`]** `path` 参数指向进程已分配地址空间之外。

**[`ENAMETOOLONG`]** 整个路径名超过 1023 个字符。

**[`ENOENT`]** 命名的共享内存对象不存在。

**[`EACCES`]** 所需权限被拒绝。`shm_unlink()` 需要对共享内存对象的写权限。

## 参见

posixshmcontrol(1), [close(2)](close.2.md), fstat(2), ftruncate(2), [ioctl(2)](ioctl.2.md), [mmap(2)](mmap.2.md), [munmap(2)](munmap.2.md), [sendfile(2)](sendfile.2.md)

## 标准

`memfd_create()` 函数预计与同名 Linux 系统调用兼容。

`shm_open()` 和 `shm_unlink()` 函数被认为符合 -p1003.1b-93。

## 历史

`memfd_create()` 函数出现于 FreeBSD 13.0。

`shm_open()` 和 `shm_unlink()` 函数首次出现于 FreeBSD 4.3。这些函数在 FreeBSD 8.0 中被重新实现为直接使用共享内存对象而非文件的系统调用。

`shm_rename()` 首次出现于 FreeBSD 13.0，作为 FreeBSD 扩展。

## 作者

Garrett A. Wollman <wollman@FreeBSD.org>（C 库支持和本手册页）

Matthew Dillon <dillon@FreeBSD.org>（`MAP_NOSYNC`）

Matthew Bryan <matthew.bryan@isilon.com>（`shm_rename` 实现）
