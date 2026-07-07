# pthread_affinity_np(3)

`pthread_getaffinity_np` — 管理 CPU 亲和性

## 名称

`pthread_getaffinity_np`, `pthread_setaffinity_np`

## 库

Lb libpthread

## 概要

`#include <pthread_np.h>`

`Ft int Fn pthread_getaffinity_np pthread_t td size_t cpusetsize cpuset_t *cpusetp Ft int Fn pthread_setaffinity_np pthread_t td size_t cpusetsize const cpuset_t *cpusetp`

## 描述

`Fn pthread_getaffinity_np` 和 `Fn pthread_setaffinity_np` 用于操作指定线程可用的 CPU 集合。

类型为 `Ft cpuset_t` 的掩码通过 `CPU_SET` 宏构成。如果用户提供的掩码不足以容纳所有匹配的 CPU，`Fn pthread_getaffinity_np` 将失败并返回 Er ERANGE 。调用 `Fn pthread_setaffinity_np` 时可接受任意大小的掩码，无限制。内核仅使用掩码的有效部分，其上界为系统中存在的最大 CPU id。如果为不存在的 CPU 设置了位，调用 `Fn pthread_setaffinity_np` 将失败并返回 Er EINVAL 。

所提供的掩码大小应为 `cpusetsize` 字节。该大小通常通过调用 `sizeof(cpuset_t)` 获得，最终由以下文件中定义的 `CPU_SETSIZE` 值决定：

`#include <sys/cpuset.h>`

`Fn pthread_getaffinity_np` 从 `td` 指定的线程获取掩码，并将其存储到 `cpusetp` 提供的空间中。

`Fn pthread_setaffinity_np` 尝试将 `td` 指定线程的掩码设置为 `cpusetp` 中的值。

## 返回值

若成功，`Fn pthread_getaffinity_np` 和 `Fn pthread_setaffinity_np` 函数将返回零。否则将返回一个错误号以指示错误。

## 错误

`Fn pthread_getaffinity_np` 和 `Fn pthread_setaffinity_np` 函数可能因以下原因失败：

**[Er** EINVAL] 调用 `Fn pthread_setaffinity_np` 时指定的 `cpusetp` 参数不是有效值。

**[Er** EDEADLK] 调用 `Fn pthread_setaffinity_np` 会导致某线程没有有效的 CPU 可运行，因为该集合与线程的匿名掩码不重叠。

**[Er** EFAULT] 传入的 `cpusetp` 指针无效。

**[Er** ESRCH] 找不到由 `td` 参数指定的线程。

**[Er** ERANGE] `cpusetsize` 小于容纳所有匹配 CPU 所需的大小。

**[Er** EPERM] 调用线程不具备完成操作所需的凭证。

## 参见

cpuset(1), cpuset(2), cpuset_getid(2), cpuset_setid(2), [pthread(3)](pthread.3.md), pthread_attr_getaffinity_np(3), pthread_attr_setaffinity_np(3), [pthread_np(3)](pthread_np.3.md)

## 标准

`pthread_getaffinity_np` 和 `pthread_setaffinity_np` 函数是非标准的 FreeBSD 扩展，在其他操作系统上可能不可用。

## 历史

`pthread_getaffinity_np` 和 `pthread_setaffinity_np` 函数首次出现于 FreeBSD 7.2。

## 作者

`pthread_getaffinity_np` 和 `pthread_setaffinity_np` 函数由 David Xu <davidxu@FreeBSD.org> 编写，本手册页由 Xin LI <delphij@FreeBSD.org> 编写。
