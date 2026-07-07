# pthread_attr_affinity_np(3)

`pthread_attr_getaffinity_np` — 管理线程属性对象中的 CPU 亲和性

## 名称

`pthread_attr_getaffinity_np`, `pthread_attr_setaffinity_np`

## 库

Lb libpthread

## 概要

`#include <pthread_np.h>`

`Ft int Fn pthread_attr_getaffinity_np const pthread_attr_t *pattr size_t cpusetsize cpuset_t *cpusetp Ft int Fn pthread_attr_setaffinity_np pthread_attr_t *pattr size_t cpusetsize const cpuset_t *cpusetp`

## 描述

`Fn pthread_attr_getaffinity_np` 和 `Fn pthread_attr_setaffinity_np` 函数用于操作指定线程属性对象可用的 CPU 集合。

类型为 `Ft cpuset_t` 的掩码通过 `CPU_SET` 宏构成。如果用户提供的掩码不足以容纳所有匹配的 CPU，`Fn pthread_attr_getaffinity_np` 将失败并返回 Er ERANGE 。调用 `Fn pthread_attr_setaffinity_np` 时可接受任意大小的掩码，无限制。`Fn pthread_attr_setaffinity_np` 仅使用掩码的有效部分，其上界为系统中存在的最大 CPU id。如果为不存在的 CPU 设置了位，调用 `Fn pthread_attr_setaffinity_np` 将失败并返回 Er EINVAL 。

所提供的掩码大小应为 `cpusetsize` 字节。该大小通常通过调用 `sizeof(cpuset_t)` 获得，最终由以下文件中定义的 `CPU_SETSIZE` 值决定：

`#include <sys/cpuset.h>`

`Fn pthread_attr_getaffinity_np` 从 `pattr` 指定的线程属性对象中获取掩码，并将其存储到 `cpusetp` 提供的空间中。

`Fn pthread_attr_setaffinity_np` 将 `pattr` 指定的线程属性对象的掩码设置为 `cpusetp` 中的值。

## 返回值

若成功，`Fn pthread_attr_getaffinity_np` 和 `Fn pthread_attr_setaffinity_np` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`Fn pthread_attr_getaffinity_np` 函数在以下情况下会失败：

**[Er** EINVAL] `pattr` 或其指定的属性为 `NULL`。

**[Er** ERANGE] `cpusetsize` 过小。

`Fn pthread_attr_setaffinity_np` 函数在以下情况下会失败：

**[Er** EINVAL] `pattr` 或其指定的属性为 `NULL`。

**[Er** EINVAL] `cpusetp` 指定了内核所支持集合之外的 CPU。

**[Er** ENOMEM] 没有足够的内存来存储 cpuset 掩码。

## 参见

cpuset(1), cpuset(2), cpuset_getid(2), cpuset_setid(2), pthread_getaffinity_np(3), [pthread_np(3)](pthread_np.3.md), pthread_setaffinity_np(3)

## 标准

`pthread_attr_getaffinity_np` 和 `pthread_attr_setaffinity_np` 函数是非标准的 FreeBSD 扩展，在其他操作系统上可能不可用。

## 历史

`pthread_attr_getaffinity_np` 和 `pthread_attr_setaffinity_np` 函数首次出现于 FreeBSD 7.2。

## 作者

`pthread_attr_getaffinity_np` 和 `pthread_attr_setaffinity_np` 函数由 David Xu <davidxu@FreeBSD.org> 编写，本手册页由 Xin LI <delphij@FreeBSD.org> 编写。
