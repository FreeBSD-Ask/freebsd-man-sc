# ntsync.4

`ntsync` — 类 NT 同步操作设备驱动

## 名称

`ntsync`

## 概要

`#include <dev/ntsync/ntsync.h>`

## 描述

`ntsync` 设备驱动提供模仿 Windows NT 内核所提供操作的同步原语。用户空间接口复制自为 Linux 内核编写的同名驱动，目标是帮助 Wine 实现 Win32 API。

该驱动提供 `/dev/ntsync` 特殊设备节点，处理若干组的 ioctl(2) 请求：

**对象**创建：包括信号量、互斥锁和事件

**等待**操作：等待一组对象变为已触发状态，可以等待集合中的全部或任一对象

对 `/dev/ntsync` 设备的 open(2) 调用返回表示同步域的文件描述符。通过 ioctl(2) 在 ntsync 文件描述符上创建的每个对象都属于该域。等待请求不得混合属于其他域的对象。

同步对象由文件描述符表示，每个都实现类型特定的 ioctl 请求集合。

## 信号量

信号量操作通常接受

```sh
struct ntsync_sem_args {
	uint32_t count;
	uint32_t max;
}
```

作为参数。信号量请求有：

**`NTSYNC_IOC_CREATE_SEM`** 创建信号量并返回信号量文件描述符。必须在 `/dev/ntsync` 文件描述符上发起。接受 `struct ntsync_sem_args` 参数，其中 `count` 为信号量初始计数，`max` 为允许的最大计数。

**`NTSYNC_IOC_SEM_RELEASE`** 释放信号量。接受单个 `uint32_t` 值，用于递减信号量计数。当信号量计数降至零时，信号量变为已触发状态。

**`NTSYNC_IOC_SEM_READ`** 在 `struct ntsync_sem_args` 中返回信号量的当前状态。

## 互斥锁

互斥锁操作通常接受

```sh
struct ntsync_mutex_args {
	uint32_t owner;
	uint32_t count;
}
```

作为参数。

互斥锁请求有：

**`NTSYNC_IOC_CREATE_MUTEX`** 创建互斥锁并返回互斥锁文件描述符。必须在 `/dev/ntsync` 文件描述符上发起。接受 `struct ntsync_mutex_args` 作为参数。`owner` 是标识当前互斥锁所有者的抽象 32 位数字。如果 `owner` 为零，互斥锁为无主，`count` 必须为零。如果 `count` 非零表示互斥锁有主，则必须提供非零的 `owner`。

**`NTSYNC_IOC_MUTEX_UNLOCK`** 解锁互斥锁。接受 `struct ntsync_mutex_args` 参数。互斥锁必须由参数中的 `owner` 持有。成功解锁会递减互斥锁计数器，当计数器降至零时互斥锁变为已触发状态且无主。解锁前的计数器值通过参数结构体的 `count` 成员返回。

**`NTSYNC_IOC_MUTEX_KILL`** 放弃互斥锁。接受单个 32 位整数作为参数，表示当前互斥锁所有者。指定的所有者必须等于当前互斥锁所有者。然后，待等待者被唤醒，并得到 `EOWNERDEAD` 结果。互斥锁的所有者和计数器设置为零。已放弃状态由下次成功等待该互斥锁清除。

**`NTSYNC_IOC_MUTEX_READ`** 返回互斥锁的当前状态。接受 `struct ntsync_mutex_args` 参数，状态在其中返回。对于已放弃的互斥锁，除状态外还会返回 `EOWNERDEAD` 错误。

## 事件

事件操作通常接受

```sh
struct ntsync_event_args {
	uint32_t manual;
	uint32_t signaled;
}
```

事件请求有：

**`NTSYNC_IOC_CREATE_EVENT`** 创建事件并返回事件文件描述符。必须在 `/dev/ntsync` 文件描述符上发起。接受 `struct ntsync_event_args` 参数。事件可分两种类型：手动和自动。手动事件在被设置后需要通过请求重置。自动事件在等待满足后由系统重置。

**`NTSYNC_IOC_EVENT_SET`** 设置（启用）事件。接受 32 位整数参数，其中返回操作前的事件状态。

**`NTSYNC_IOC_EVENT_RESET`** 重置（禁用）事件。接受 32 位整数参数，其中返回操作前的事件状态。

**`NTSYNC_IOC_EVENT_PULSE`** 原子性地设置事件，唤醒符合条件的等待者，然后重置事件。接受 32 位整数参数，其中返回操作前的事件状态。如果手动事件被脉冲，它会唤醒所有等待者，之后被重置。而自动事件在唤醒最多一个等待者后被重置。

**`NTSYNC_IOC_EVENT_READ`** 返回事件的当前状态。接受 `struct ntsync_event_args` 参数，其中返回当前事件状态。

## 等待操作

等待操作接受

```sh
struct ntsync_wait_args {
	uint64_t timeout;
	uint64_t objs;
	uint32_t count;
	uint32_t index;
	uint32_t flags;
	uint32_t owner;
	uint32_t alert;
	uint32_t pad;
}
```

作为参数。

使等待满足的对象的已触发状态会被操作消耗，例如通过递增计数器获取信号量、锁定互斥锁，手动事件变为未触发。

`timeout` 以纳秒为单位。如果 `timeout` 为零，等待请求仅在等待条件满足或排队了信号时返回。否则，如果在指定时间后等待仍未满足，无论如何都会中止并返回 `ETIMEDOUT` 错误。

`objs` 成员指向同步对象文件描述符数组。其大小通过 `count` 成员传递。最大可为 `NTSYNC_MAX_WAIT_COUNT`，即 64。

`alert` 非零时指定事件文件描述符，其触发会终止等待，而不管 `objs` 数组中其他对象的状态。

从等待请求非错误返回时，`index` 成员包含导致等待请求满足的已触发对象的索引。如果该索引处的对象是信号量，`owner` 成员报告已触发信号量的所有者。如果 `alert` 事件被触发以中止等待，`index` 设置为 `count`。

`flags` 参数的可能取值为

**`NTSYNC_WAIT_REALTIME`** 指定的超时为 `CLOCK_REALTIME` 绝对值，否则为 `CLOCK_MONOTONIC`，参见 clock_gettime(2)。

等待请求有：

**`NTSYNC_IOC_WAIT_ANY`** 等待任一对象变为已触发。

**`NTSYNC_IOC_WAIT_ALL`** 等待所有对象变为已触发。这意味着仅当所有对象可以一起被消耗时等待才满足，此操作原子完成。`objs` 数组中不允许重复对象。`alert` 对象不允许列在 `objs` 数组中。

## 参见

有关 Linux API 参考可参见 Linux 内核源码中的 `Documentation/userspace-api/ntsync.rst` 文件，该文件用于实现 FreeBSD 驱动。

## 历史

`ntsync` 驱动和手册页首次出现于 FreeBSD 15.2。

## 作者

驱动和手册页由 Konstantin Belousov <kib@FreeBSD.org> 编写。
