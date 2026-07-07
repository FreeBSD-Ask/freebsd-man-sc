# cpuset(2)

`cpuset` — 管理 CPU 亲和性集合

## 名称

`cpuset`, `cpuset_getid`, `cpuset_setid`

## 库

Lb libc

## 概要

`#include <sys/param.h>`

`#include <sys/cpuset.h>`

```c
int
cpuset(cpusetid_t *setid);

int
cpuset_setid(cpuwhich_t which, id_t id, cpusetid_t setid);

int
cpuset_getid(cpulevel_t level, cpuwhich_t which, id_t id,
    cpusetid_t *setid);
```

## 描述

`cpuset_setid` 系列系统调用允许应用程序控制处理器和内存域的集合，并将进程和线程分配到这些集合中。处理器集合包含成员可以运行的 CPU 和域列表，并且只有在某个进程是集合成员时才存在。系统中的所有进程都有一个已分配的集合。系统中所有进程的默认集合是编号为 1 的集合。线程属于包含它们的进程所在的同一集合，但是，它们可以通过匿名每线程掩码进一步限制其集合，以绑定到特定的 CPU 或 CPU 和内存域的子集。

集合通过 `cpuset_id_t` 类型的编号引用。每个线程都有一个根集合、一个已分配的集合和一个匿名掩码。只有根集合和已分配集合是编号的。根集合是系统或线程运行所在的系统分区中所有可用 CPU 和内存域的集合。已分配集合是根集合的子集，可以按进程进行管理分配。许多进程和线程可以是编号集合的成员。

匿名集合是对已分配集合的进一步线程特定细化。管理员可以使用 cpuset(1) 操作编号集合，而应用程序开发者可以使用 cpuset_setaffinity(2) 和 cpuset_setdomain(2) 操作匿名集合。

为了选择正确的集合，使用 `cpulevel_t` 类型的值。`level` 支持以下值：

| `CPU_LEVEL_ROOT` | 根集合 |
| --- | --- |
| `CPU_LEVEL_CPUSET` | 已分配集合 |
| `CPU_LEVEL_WHICH` | 由 which 参数指定的集合 |

`which` 参数决定 `id` 值的解释方式，其类型为 `cpuwhich_t`。`which` 参数可以有以下值：

| `CPU_WHICH_TID` | id 是 lwpid_t（线程 id） |
| --- | --- |
| `CPU_WHICH_PID` | id 是 pid_t（进程 id） |
| `CPU_WHICH_TIDPID` | id 是线程或进程 id |
| `CPU_WHICH_JAIL` | id 是 jid（jail id） |
| `CPU_WHICH_CPUSET` | id 是 cpusetid_t（cpuset id） |
| `CPU_WHICH_IRQ` | id 是 irq 编号 |
| `CPU_WHICH_INTRHANDLER` | id 是中断处理程序的 irq 编号 |
| `CPU_WHICH_ITHREAD` | id 是 ithread 的 irq 编号 |
| `CPU_WHICH_DOMAIN` | id 是 NUMA 域 |

`id` 为 '-1' 时可以与 `which` 为 `CPU_WHICH_TID`、`CPU_WHICH_PID`、`CPU_WHICH_TIDPID` 或 `CPU_WHICH_CPUSET` 一起使用，表示当前线程、进程或当前线程的 cpuset。所有 cpuset 系统调用都允许这种用法。

`level` 参数为 `CPU_LEVEL_WHICH` 且 `which` 参数不为 `CPU_WHICH_CPUSET` 时，引用的是对象的匿名掩码。此掩码没有 id，只能通过 cpuset_setaffinity(2) 操作。

`cpuset()` 创建一个包含与当前进程根集合相同 CPU 的新集合，并将其 id 存储在 `setid` 提供的空间中。成功完成后，调用进程加入该集合并且是唯一的成员。子进程在调用 [fork(2)](fork.2.md) 后继承此集合。

`cpuset_setid()` 尝试设置由 `which` 参数指定的对象的 id。目前 `CPU_WHICH_PID` 是 which 的唯一可接受值，因为线程没有与其进程不同的 id，并且 API 不允许更改现有集合的 id。成功完成后，目标进程中的所有线程将在集合允许的 CPU 上运行。

`cpuset_getid()` 从 `which` 指示的对象中检索集合 id，并将其存储在 `setid` 指向的空间中。检索到的 id 可以是根集合或已分配集合的 id，具体取决于 `level` 的值。`level` 应为 `CPU_LEVEL_CPUSET` 或 `CPU_LEVEL_ROOT`，以从 `id` 参数指定的进程或线程获取集合 id。不支持对进程或线程指定 `CPU_LEVEL_WHICH`，因为这引用的是未编号的匿名掩码。

集合的实际内容可以使用 [cpuset_getaffinity(2)](cpuset_getaffinity.2.md)、[cpuset_setaffinity(2)](cpuset_setaffinity.2.md)、[cpuset_getdomain(2)](cpuset_getdomain.2.md) 和 [cpuset_setdomain(2)](cpuset_setdomain.2.md) 来检索或操作。[cpuset(9)](../man9/cpuset.9.md) 宏可用于操作 `cpuset_t` 类型的掩码，并通过这些 API 进行获取和设置。详见这些手册页。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 errno 以指示错误。

## 实例

在此示例中，使用 CPU_ZERO(9) 和 CPU_SET(9)（[cpuset(9)](../man9/cpuset.9.md) 编程接口的成员）配置 CPU 集合掩码，将执行限制在第一个 CPU。然后，使用 cpuset_setaffinity(2) 将该掩码应用于与当前进程关联的新匿名 CPU 集合。此掩码将由当前进程使用，并被任何新的子进程继承。

```c
#include <sys/param.h>
#include <sys/cpuset.h>

#include <sysexits.h>

cpuset_t cpuset_mask;

/* 初始化 CPU 掩码并启用 CPU 0。 */
CPU_ZERO(&cpuset_mask);
CPU_SET(0, &cpuset_mask);

/* 为当前进程的 CPU 集合设置亲和性。 */
if (cpuset_setaffinity(CPU_LEVEL_WHICH, CPU_WHICH_PID, -1,
    sizeof(cpuset_mask), &cpuset_mask) < 0)
        err(EX_OSERR, "cpuset_setaffinity");
```

在下一个示例中，创建一个包含当前进程的命名 CPU 集合，并类似地配置其亲和性。所得的 CPU 集合 ID 随后可用于进一步外部管理该集合的亲和性。

```c
#include <sys/param.h>
#include <sys/cpuset.h>

#include <sysexits.h>

cpusetid_t cpuset_id;
cpuset_t cpuset_mask;

/* 为当前进程创建新的 cpuset。 */
if (cpuset(&cpuset_id) < 0)
        err(EX_OSERR, "cpuset");

/* 初始化 CPU 掩码并启用 CPU 0。 */
CPU_ZERO(&cpuset_mask);
CPU_SET(0, &cpuset_mask);

/* 为当前进程的 CPU 集合设置亲和性。 */
if (cpuset_setaffinity(CPU_LEVEL_SET, CPU_WHICH_CPUSET, cpuset_id,
    sizeof(cpuset_mask), &cpuset_mask) < 0)
        err(EX_OSERR, "cpuset_setaffinity");
```

## 错误

以下错误码可能会设置在 `errno` 中：

**[`EINVAL`]** `which` 或 `level` 参数不是有效值。

**[`EDEADLK`]** `cpuset_setid()` 调用会使某线程没有有效的 CPU 可运行，因为该集合与线程的匿名掩码不重叠。

**[`EFAULT`]** 传给 `cpuset_getid()` 或 `cpuset()` 的 setid 指针无效。

**[`ESRCH`]** 无法找到由 `id` 和 `which` 参数指定的对象。

**[`EPERM`]** 调用进程没有完成该操作所需的凭证。

**[`ENFILE`]** 没有可分配的 `cpusetid_t`。

## 参见

[cpuset(1)](../man1/cpuset.1.md), [cpuset_getaffinity(2)](cpuset_getaffinity.2.md), [cpuset_getdomain(2)](cpuset_getdomain.2.md), [cpuset_setaffinity(2)](cpuset_setaffinity.2.md), [cpuset_setdomain(2)](cpuset_setdomain.2.md), [pthread_affinity_np(3)](../man3/pthread_affinity_np.3.md), [pthread_attr_affinity_np(3)](../man3/pthread_attr_affinity_np.3.md), [CPU_SET(9)](../man9/CPU_SET.9.md), [CPU_ZERO(9)](../man9/CPU_ZERO.9.md), [cpuset(9)](../man9/cpuset.9.md)

## 历史

`cpuset_setid` 系列系统调用首次出现于 FreeBSD 7.1。

## 作者

Jeffrey Roberson <jeff@FreeBSD.org>