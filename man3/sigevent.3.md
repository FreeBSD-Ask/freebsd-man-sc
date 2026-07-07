# sigevent(3)

`sigevent` — 异步事件通知

## 名称

`sigevent`

## 概要

`#include <signal.h>`

## 描述

某些操作允许线程通过 `struct sigevent` 结构请求事件的异步通知。此结构包含若干字段，描述所请求的通知：

kqueue(2) 文件描述符

回调函数指针

回调线程属性

| **类型** | **成员** | **描述** |
| --- | --- | --- |
| `int` | sigev_notify | 通知方法 |
| `int` | sigev_signo | 信号编号 |
| `union sigval` | sigev_value | 信号值 |
| `int` | sigev_notify_kqueue |  |
| `unsigned short` | sigev_notify_kevent_flags | kevent 标志 |
| `lwpid_t` | sigev_notify_thread_id | LWP ID |
| `void (*)(union sigval)` | sigev_notify_function |  |
| `pthread_attr_t *` | sigev_notify_attributes |  |

`sigev_notify` 字段指定事件触发时使用的通知方法：

**`SIGEV_NONE`** 不发送任何通知。

**`SIGEV_SIGNAL`** 信号 `sigev_signo` 作为实时信号排队到调用进程。存储在 `sigev_value` 中的值将出现在排队信号的 `siginfo_t` 结构的 `si_value` 中。

**`SIGEV_THREAD`** `sigev_notify_function` 中的通知函数在单独的线程上下文中被调用。该线程使用 `*sigev_notify_attributes` 中指定的属性创建。存储在 `sigev_value` 中的值作为唯一参数传递给 `sigev_notify_function`。如果 `sigev_notify_attributes` 为 `NULL`，则使用默认属性创建线程。

**`SIGEV_KEVENT`** 新的 kevent 被发布到 kqueue `sigev_notify_kqueue`。kevent 结构的 `udata` 成员包含存储在 `sigev_value` 中的值。kevent 中其他字段的含义特定于触发事件的类型。

**`SIGEV_THREAD_ID`** 信号 `sigev_signo` 被排队到 LWP ID 为 `sigev_notify_thread_id` 的线程。存储在 `sigev_value` 中的值将出现在排队信号的 `siginfo_t` 结构的 `si_value` 中。

## 注释

注意，希望使用 `SIGEV_THREAD` 通知的程序必须链接 Lb librt 库。

## 参见

aio_read(2), mq_notify(2), timer_create(2), [siginfo(3)](siginfo.3.md)

## 标准

`struct sigevent` 类型遵循 IEEE Std 1003.1-2004 ("POSIX.1") 标准。

## 历史

`sigevent` 结构首次出现于 FreeBSD 3.3。
