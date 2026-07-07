# timer_create(2)

`timer_create` — 创建每进程定时器（REALTIME）

## 名称

`timer_create`

## 库

Lb librt

## 概要

`#include <time.h>`

`#include <signal.h>`

```c
int
timer_create(clockid_t clockid, struct sigevent *restrict evp,
    timer_t *restrict timerid);
```

## 描述

`timer_create()` 系统调用使用指定时钟 `clock_id` 作为计时基准创建一个每进程定时器。`timer_create()` 系统调用在 `timerid` 所引用的位置返回一个 `timer_t` 类型的定时器 ID，用于在定时器请求中标识该定时器。此定时器 ID 在调用进程内唯一，直到该定时器被删除。特定时钟 `clock_id` 定义于

`#include <time.h>`

返回其 ID 的定时器在从 `timer_create()` 返回时处于解除武装状态。

`evp` 参数若非 `NULL`，则指向一个 `sigevent` 结构。此结构由应用程序分配，定义定时器到期时发生的异步通知。

如果 `evp->sigev_notify` 为 `SIGEV_SIGNO` 或 `SIGEV_THREAD_ID`，则在 `evp->sigev_signo` 中指定的信号将发送给调用进程（`SIGEV_SIGNO`）或发送给 LWP ID 为 `evp->sigev_notify_thread_id` 的线程（`SIGEV_THREAD_ID`）。排队信号的信息将包含：

存储在 `evp->sigev_value` 中的值

如果定时器溢出次数为 `DELAYTIMER_MAX`（一个错误代码，定义于

`#include <errno.h>`

| **成员** | **值** |
| :------: | :----: |
| `si_code` | `SI_TIMER` |
| `si_value` | |
| `si_timerid` | 定时器 ID |
| `si_overrun` | 定时器溢出计数 |
| `si_errno` | |

如果 `evp` 参数为 `NULL`，效果等同于 `evp` 参数指向一个 `sigevent` 结构，其 `sigev_notify` 成员值为 `SIGEV_SIGNAL`，`sigev_signo` 为默认信号编号（`SIGALRM`），`sigev_value` 成员值为该定时器的 ID。

此实现支持 `CLOCK_REALTIME`、`CLOCK_TAI` 或 `CLOCK_MONOTONIC` 的 `clock_id`。

如果 `evp->sigev_notify` 为 `SIGEV_THREAD` 且 `sev->sigev_notify_attributes` 不为 `NULL`，且 `sev->sigev_notify_attributes` 所指向的属性具有通过 `pthread_attr_setstack` 或 `pthread_attr_setstackaddr` 调用指定的线程栈地址，则当信号生成不止一次时结果未指定。

## 返回值

调用成功时，`timer_create()` 返回零，并将 `timerid` 所引用的位置更新为一个 `timer_t`，可传递给每进程定时器调用。如果发生错误，系统调用返回值 -1，并设置全局变量 `errno` 以指示错误。发生错误时 `timerid` 的值未定义。

## 错误

`timer_create()` 系统调用将在以下情况下失败：

**[`EAGAIN`]** 调用进程已经创建了此实现所允许的全部定时器。

**[`EINVAL`]** 不支持指定的时钟 ID。

**[`EINVAL`]** 不支持指定的异步通知方法。

**[`EFAULT`]** 任何参数指向分配地址空间之外，或发生内存保护错误。

## 参见

`clock_getres(2)`, [timer_delete(2)](timer_delete.2.md), `timer_getoverrun(2)`, [sigevent(3)](../man3/sigevent.3.md), [siginfo(3)](../man3/siginfo.3.md)

## 标准

`timer_create()` 系统调用遵循 IEEE Std 1003.1-2004 ("POSIX.1")。

## 历史

对 POSIX 每进程定时器的支持首次出现于 FreeBSD 7.0。
