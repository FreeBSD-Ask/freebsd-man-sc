# rtprio(2)

`rtprio` — 检查或修改实时或空闲优先级

## 名称

`rtprio`, `rtprio_thread`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/rtprio.h>`

```c
int
rtprio(int function, pid_t pid, struct rtprio *rtp);

int
rtprio_thread(int function, lwpid_t lwpid, struct rtprio *rtp);
```

## 描述

`rtprio()` 系统调用用于查找或更改进程或调用线程的实时或空闲优先级。`rtprio_thread()` 系统调用用于查找或更改线程的实时或空闲优先级。

`function` 参数指定要执行的操作。`RTP_LOOKUP` 用于查找当前优先级，`RTP_SET` 用于设置优先级。

对于 `rtprio()` 系统调用，`pid` 参数指定要操作的进程，0 表示调用线程。当 `pid` 非零时，根据 `function` 参数的值，系统调用报告进程中的最高优先级，或设置进程中所有线程的优先级。

对于 `rtprio_thread()` 系统调用，`lwpid` 指定要操作的线程，0 表示调用线程。

`*rtp` 参数是指向 struct rtprio 的指针，用于指定优先级和优先级类型。该结构的形式如下：

```c
struct rtprio {
	u_short	type;
	u_short prio;
};
```

`type` 字段的值可以为 `RTP_PRIO_REALTIME`（实时优先级）、`RTP_PRIO_NORMAL`（普通优先级）和 `RTP_PRIO_IDLE`（空闲优先级）。`prio` 字段指定的优先级范围在 0 到 `RTP_PRIO_MAX`（通常为 31）之间。0 是最高优先级。

实时和空闲优先级通过 `fork()` 和 `exec()` 继承。

实时线程只能被同等或更高优先级的线程或中断抢占；空闲优先级线程仅在没有其他实时/普通优先级线程可运行时才会运行。更高实时/空闲优先级的线程抢占更低实时/空闲优先级的线程。同等实时/空闲优先级的线程按轮转方式运行。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`rtprio()` 和 `rtprio_thread()` 系统调用在以下情况下会失败：

**[`EFAULT`]** 传递给 `rtprio()` 或 `rtprio_thread()` 的 `rtp` 指针无效。

**[`EINVAL`]** 指定的 `prio` 超出范围。

**[`EPERM`]** 调用线程不允许设置优先级。只有 root 才能更改任何线程的实时或空闲优先级。可通过 [mac_priority(4)](../man4/mac_priority.4.md) 策略以及 realtime 和 idletime 用户组授予例外权限。[sysctl(8)](../man8/sysctl.8.md) 变量 `security.bsd.unprivileged_idprio` 已弃用。如果设为非零值，允许任何用户更改其拥有的线程的空闲优先级。

**[`ESRCH`]** 指定的进程或线程未找到或不可见。

## 参见

[nice(1)](../man1/nice.1.md), [ps(1)](../man1/ps.1.md), rtprio(1), setpriority(2), [nice(3)](../gen/nice.3.md), [mac_priority(4)](../man4/mac_priority.4.md), [renice(8)](../man8/renice.8.md), [p_cansee(9)](../man9/p_cansee.9.md)

## 作者

原作者为 Henrik Vestergaard Draboel <hvd@terry.ping.dk>。FreeBSD 中的此实现由 David Greenman 大幅重写。`rtprio_thread()` 系统调用由 David Xu 实现。
