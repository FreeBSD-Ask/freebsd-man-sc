# cpuset_getdomain(2)

`cpuset_getdomain` — 管理内存域策略

## 名称

`cpuset_getdomain`, `cpuset_setdomain`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/domainset.h>`

```c
int
cpuset_getdomain(cpulevel_t level, cpuwhich_t which, id_t id,
    size_t setsize, domainset_t *mask, int *policy);

int
cpuset_setdomain(cpulevel_t level, cpuwhich_t which, id_t id,
    size_t setsize, const domainset_t *mask, int policy);
```

## 描述

`cpuset_getdomain()` 和 `cpuset_setdomain()` 允许操作可用于进程、线程、Jail 和其他资源的内存域集合及分配策略。这些函数可以操作包含许多进程的内存域集合，或者仅影响单个对象的每对象匿名掩码。

`level` 和 `which` 参数的有效值记录在 [cpuset(2)](cpuset.2.md) 中。这些参数指定我们所引用的对象以及该对象的哪个集合。并非所有可能的组合都有效。例如，只有进程可以属于通过 `level` 参数为 `CPU_LEVEL_CPUSET` 所访问的编号集合。然而，所有资源都有一个可以通过 `CPU_LEVEL_WHICH` 操作的掩码。

`domainset_t` 类型的掩码使用 `DOMAINSET` 宏组成。内核容忍大的集合，只要集合中指定的所有域都存在。小于内核使用的集合在对 `cpuset_getdomain()` 的调用上会产生错误，即使结果集合可以放入用户提供的集合中。对 `cpuset_setdomain()` 的调用容忍小的集合，没有限制。

提供的掩码大小应为 `setsize` 字节。此大小通常通过调用 `sizeof(mask)` 获得，最终由 `sys/domainset.h` 中定义的 `DOMAINSET_SETSIZE` 的值决定。

`cpuset_getdomain()` 从由 `level`、`which` 和 `id` 指定的对象中检索掩码和策略，并将其存储在 `mask` 和 `policy` 提供的空间中。

`cpuset_setdomain()` 尝试将由 `level`、`which` 和 `id` 指定的对象的掩码和策略设置为 `mask` 和 `policy` 中的值。

## 分配策略

有效的策略值如下：

**`DOMAINSET_POLICY_ROUNDROBIN`** 通过循环 `mask` 中的每个域，以轮询方式分配内存。

**`DOMAINSET_POLICY_FIRSTTOUCH`** 在请求线程运行的 CPU 本地域上分配内存。从此域分配失败时将回退到轮询。

**`DOMAINSET_POLICY_PREFER`** 优先从掩码中指定的单个域分配内存。如果内存不可用，将按轮询顺序访问父 cpuset 中列出的域。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 错误

以下错误码可能会设置在 `errno` 中：

**[`EINVAL`]** `level` 或 `which` 参数不是有效值。

**[`EINVAL`]** 调用 `cpuset_setdomain()` 时指定的 `mask` 或 `policy` 参数不是有效值。

**[`EDEADLK`]** `cpuset_setdomain()` 调用会使某线程没有有效的 CPU 可运行，因为该集合与线程的匿名掩码不重叠。

**[`EFAULT`]** 传入的 mask 指针无效。

**[`ESRCH`]** 无法找到由 `id` 和 `which` 参数指定的对象。

**[`ERANGE`]** `domainsetsize` 过大或小于内核集合大小。

**[`EPERM`]** 调用进程没有完成该操作所需的凭证。

**[`ECAPMODE`]** 调用进程在 capability 模式下试图对非自身的进程进行操作。参见 [capsicum(4)](../man4/capsicum.4.md)。

## 参见

[cpuset(1)](../man1/cpuset.1.md), [cpuset(2)](cpuset.2.md), [cpuset_getaffinity(2)](cpuset_getaffinity.2.md), [cpuset_getid(2)](cpuset_getid.2.md), [cpuset_setaffinity(2)](cpuset_setaffinity.2.md), [cpuset_setid(2)](cpuset_setid.2.md), [capsicum(4)](../man4/capsicum.4.md), [cpuset(9)](../man9/cpuset.9.md)

## 历史

`cpuset_setdomain` 系列系统调用首次出现于 FreeBSD 12.0。

## 作者

Jeffrey Roberson <jeff@FreeBSD.org>