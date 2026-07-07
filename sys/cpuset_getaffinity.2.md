# cpuset_getaffinity(2)

`cpuset_getaffinity` — 管理 CPU 亲和性

## 名称

`cpuset_getaffinity`, `cpuset_setaffinity`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/cpuset.h>`

```c
int
cpuset_getaffinity(cpulevel_t level, cpuwhich_t which, id_t id,
    size_t setsize, cpuset_t *mask);

int
cpuset_setaffinity(cpulevel_t level, cpuwhich_t which, id_t id,
    size_t setsize, const cpuset_t *mask);
```

## 描述

`cpuset_getaffinity()` 和 `cpuset_setaffinity()` 允许操作可用于进程、线程、中断、Jail 和其他资源的 CPU 集合。这些函数可以操作包含许多进程的 CPU 集合，或者仅影响单个对象的每对象匿名掩码。

`level` 和 `which` 参数的有效值记录在 [cpuset(2)](cpuset.2.md) 中。这些参数指定我们所引用的对象以及该对象的哪个集合。并非所有可能的组合都有效。例如，只有进程可以属于通过 `level` 参数为 `CPU_LEVEL_CPUSET` 所访问的编号集合。然而，所有资源都有一个可以通过 `CPU_LEVEL_WHICH` 操作的掩码。

`cpuset_t` 类型的掩码使用 `CPU_SET` 宏组成。如果用户提供的掩码不够大，无法容纳所有匹配的 CPU，`cpuset_getaffinity()` 将失败并返回 `ERANGE`。对 `cpuset_setaffinity()` 的调用容忍任何大小的掩码，没有限制。内核使用掩码中有意义的部分，其上界是系统中存在的最大 CPU id。如果为不存在的 CPU 设置了位，对 `cpuset_setaffinity()` 的调用将失败并返回 `EINVAL`。

提供的掩码大小应为 `setsize` 字节。此大小通常通过调用 `sizeof(mask)` 获得，最终由 `sys/cpuset.h` 中定义的 `CPU_SETSIZE` 的值决定。

`cpuset_getaffinity()` 从由 `level`、`which` 和 `id` 指定的对象中检索掩码，并将其存储在 `mask` 所提供的空间中。

`cpuset_setaffinity()` 尝试将由 `level`、`which` 和 `id` 指定的对象的掩码设置为 `mask` 中的值。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

以下错误码可能会设置在 `errno` 中：

**[`EINVAL`]** `level` 或 `which` 参数不是有效值。

**[`EINVAL`]** 调用 `cpuset_setaffinity()` 时指定的 `mask` 参数不是有效值。

**[`EDEADLK`]** `cpuset_setaffinity()` 调用会使某线程没有有效的 CPU 可运行，因为该集合与线程的匿名掩码不重叠。

**[`EFAULT`]** 传入的 mask 指针无效。

**[`ESRCH`]** 无法找到由 `id` 和 `which` 参数指定的对象。

**[`ERANGE`]** `cpusetsize` 小于容纳所有匹配 CPU 所需的大小。

**[`EPERM`]** 调用进程没有完成该操作所需的凭证。

**[`ECAPMODE`]** 调用进程在 capability 模式下试图对非自身的进程进行操作。参见 [capsicum(4)](../man4/capsicum.4.md)。

## 参见

[cpuset(1)](../man1/cpuset.1.md), [cpuset(2)](cpuset.2.md), [cpuset_getdomain(2)](cpuset_getdomain.2.md), [cpuset_getid(2)](cpuset.2.md), [cpuset_setdomain(2)](cpuset_getdomain.2.md), [cpuset_setid(2)](cpuset.2.md), [pthread_affinity_np(3)](../man3/pthread_affinity_np.3.md), [pthread_attr_affinity_np(3)](../man3/pthread_attr_affinity_np.3.md), [capsicum(4)](../man4/capsicum.4.md), [cpuset(9)](../man9/cpuset.9.md)

## 历史

`cpuset_setaffinity` 系列系统调用首次出现于 FreeBSD 7.1。

## 作者

Jeffrey Roberson <jeff@FreeBSD.org>
