# pkru(3)

`Protection` — 为页面提供快速的由用户管理的基于密钥的访问控制

## 名称

`Protection`

## 库

libc

## 概要

```c
#include <machine/sysarch.h>

int
x86_pkru_get_perm(unsigned int keyidx, int *access, int *modify);

int
x86_pkru_set_perm(unsigned int keyidx, int access, int modify);

int
x86_pkru_protect_range(void *addr, unsigned long len,
    unsigned int keyidx, int flag);

int
x86_pkru_unprotect_range(void *addr, unsigned long len);
```

## 描述

保护密钥（protection keys）特性提供了一种额外的机制，用于控制对用户态地址的访问，此机制独立于由 mmap(2) 和 mprotect(2) 所建立的常规页面权限。该机制提供了可用于避免对敏感内存的意外读取或修改的安全措施，也可作为调试特性。由于权限可由用户控制，它无法防范蓄意的访问。

如果硬件支持，每个已映射的用户线性地址都有一个关联的 4 位保护密钥。一个新的每线程 PKRU 硬件寄存器为每个保护密钥决定，具有该保护密钥的用户态地址是否可被读取或写入。

一个给定范围在同一时间只能应用一个密钥。默认保护密钥索引为零，即使未向地址显式分配密钥或密钥已被移除，也会使用该索引。

如果用户应用程序尝试执行被 PKRU 寄存器禁止的内存访问，违规线程将收到一个同步 `SIGSEGV` 信号，其 `si_code` 设置为 `SEGV_PKUERR`。在处理系统调用时，PKRU 保护可能会阻止内核访问受保护的用户地址，但这不受保证，不应依赖于此。

64 位和 32 位应用程序均可使用保护密钥。有关该硬件特性的更多信息，请参阅 Intel 公司出版的 IA32 软件开发者手册。

写入页表项的密钥索引由 sysarch 系统调用管理。每个密钥的权限使用用户态指令 *RDPKRU* 和 *WRPKRU* 管理。系统为该系统调用和这些指令提供了便捷的库辅助函数，如下所述。

`x86_pkru_protect_range` 函数将密钥 `keyidx` 分配给从 `addr` 开始、长度为 `len` 的范围。起始地址向下截断到页面起始处，末尾向上取整到页面末尾。成功调用后，该范围已分配指定的密钥，即使密钥为零且未改变页表项。

`flags` 参数取以下值的逻辑或：

**`AMD64_PKRU_EXCL`** 仅当该范围未分配任何其他密钥（包括零密钥）时才分配该密钥。必须先使用 `x86_pkru_unprotect_range` 移除任何现有密钥，此请求才能成功。如果未指定 `AMD64_PKRU_EXCL` 标志，`x86_pkru_protect_range` 将替换任何现有密钥。

**`AMD64_PKRU_PERSIST`** 分配给该范围的密钥是持久的。当当前映射被销毁且在指定范围的任何子范围中创建新映射时，这些密钥会被重新建立。必须使用 `x86_pkru_unprotect_range` 调用来遗忘该密钥。

`x86_pkru_unprotect_range` 函数移除分配给指定范围的所有密钥。现有映射在页表项中改为使用密钥索引零。对于使用 `AMD64_PKRU_EXCL` 标志的 `x86_pkru_protect_range` 而言，该范围内所有映射的密钥不再被视为已安装。

`x86_pkru_get_perm` 函数返回由 `keyidx` 参数指定的密钥的访问权限。如果调用后 `access` 所指向的值为零，则对分配了密钥 `keyidx` 的映射不授予读或写权限。如果 `access` 非零，则允许读访问。`modify` 参数所指向变量的非零值表示允许写访问。

反之，`x86_pkru_set_perm` 按其参数为给定密钥索引设置访问和修改权限。

## 返回值

如果成功，返回零；否则返回一个错误号以指示错误。

## 错误

**`[EOPNOTSUPP]`** 硬件不支持保护密钥。

**`[EINVAL]`** 所提供的密钥索引无效（大于 15）。

**`[EINVAL]`** 为 `x86_pkru_protect_range` 提供的 `flags` 参数设置了保留位。

**`[EINVAL]`** 请求的范围部分覆盖了由 shm_create_largepage(3) 创建的对象映射。

**`[EFAULT]`** 所提供的地址范围未完全落入用户管理的地址范围内。

**`[ENOMEM]`** 内存不足导致操作无法完成。

**`[EBUSY]`** 为 `x86_pkru_protect_range` 指定了 `AMD64_PKRU_EXCL` 标志，且该范围已有已定义的保护密钥。

## 参见

mmap(2), mprotect(2), munmap(2), sysarch(2)

## 标准

`Protection` 函数是非标准的，首次出现于 FreeBSD 13.0。
