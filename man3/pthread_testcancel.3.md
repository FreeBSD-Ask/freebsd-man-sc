# pthread_testcancel.3

`pthread_setcancelstate` — 设置可取消状态

## 名称

`pthread_setcancelstate`, `pthread_setcanceltype`, `pthread_testcancel`

## 库

Lb libpthread

## 概要

`#include <pthread.h>`

```c
int
pthread_setcancelstate(int state, int *oldstate);

int
pthread_setcanceltype(int type, int *oldtype);

void
pthread_testcancel(void);
```

## 描述

`pthread_setcancelstate()` 函数原子地将调用线程的可取消状态设置为指定的 `state`，并在 `oldstate` 不为 `NULL` 时，将先前的可取消状态返回到 `oldstate` 所引用的位置。`state` 的合法值为 `PTHREAD_CANCEL_ENABLE` 和 `PTHREAD_CANCEL_DISABLE`。该函数是异步信号安全的。

`pthread_setcanceltype()` 函数原子地将调用线程的可取消类型设置为指定的 `type`，并在 `oldtype` 不为 `NULL` 时，将先前的可取消类型返回到 `oldtype` 所引用的位置。`type` 的合法值为 `PTHREAD_CANCEL_DEFERRED` 和 `PTHREAD_CANCEL_ASYNCHRONOUS`。

任何新建线程（包括首次调用 `main()` 的线程）的可取消状态和类型分别为 `PTHREAD_CANCEL_ENABLE` 和 `PTHREAD_CANCEL_DEFERRED`。

`pthread_testcancel()` 函数在调用线程中创建一个取消点。如果可取消功能被禁用，`pthread_testcancel()` 函数没有任何效果。

### 可取消状态

线程的可取消状态决定了接收到取消请求时采取的操作。线程可以通过多种方式控制取消。

每个线程维护自己的"可取消状态"，可以用两个位编码：

***可取消**启用* 当可取消状态为 `PTHREAD_CANCEL_DISABLE` 时，针对目标线程的取消请求会被挂起保留。

***可取消**类型* 当可取消功能已启用且可取消类型为 `PTHREAD_CANCEL_ASYNCHRONOUS` 时，新的或挂起的取消请求可以在任何时候执行。当可取消功能已启用且可取消类型为 `PTHREAD_CANCEL_DEFERRED` 时，取消请求会被挂起保留，直到到达取消点（见下文）。如果可取消功能被禁用，可取消类型的设置不会立即生效，因为所有取消请求都会被挂起保留；但是，一旦再次启用可取消功能，新类型就会生效。

### 取消点

当线程正在执行以下函数时，会出现取消点：

`accept()`, `accept4()`, `aio_suspend()`, `connect()`, `clock_nanosleep()`, `close()`, `creat()`, `fcntl()`（当 `cmd` 为 `F_SETLKW` 时，`fcntl()` 函数是取消点）, `fdatasync()`, `fsync()`, `kevent()`（当可能阻塞时，例如 `nevents` 参数不为零时，`kevent()` 函数是取消点）, `mq_receive()`, `mq_send()`, `mq_timedreceive()`, `mq_timedsend()`, `msync()`, `nanosleep()`, `open()`, `openat()`, `pause()`, `poll()`, `ppoll()`, `pselect()`, `pthread_cond_timedwait()`, `pthread_cond_wait()`, `pthread_join()`, `pthread_testcancel()`, `read()`, `readv()`, `recv()`, `recvfrom()`, `recvmsg()`, `select()`, `sem_timedwait()`, `sem_clockwait_np()`, `sem_wait()`, `send()`, `sendmsg()`, `sendto()`, `sigsuspend()`, `sigtimedwait()`, `sigwaitinfo()`, `sigwait()`, `sleep()`, `system()`, `tcdrain()`, `usleep()`, `wait()`, `wait3()`, `wait4()`, `wait6()`, `waitid()`, `waitpid()`, `write()`, `writev()`

## 注释

`pthread_setcancelstate()` 和 `pthread_setcanceltype()` 函数用于控制线程可能被异步取消的点。为了使取消控制能够以模块化方式使用，必须遵循一些规则。

在本讨论中，将对象视为过程的泛化。对象是一组作为一个单元编写的过程和全局变量，由未知的客户端调用。对象可能依赖于其他对象。

首先，进入对象时应仅禁用可取消功能，绝不应显式启用。退出对象时，可取消状态应始终恢复为进入对象时的值。

这源自模块化论证：如果对象的客户端（或使用该对象的另一个对象的客户端）已禁用可取消功能，是因为客户端不想担心线程在执行某些操作序列时被取消而需要进行的清理工作。如果在此状态下调用对象并启用了可取消功能，而该线程有待处理的取消请求，那么线程将被取消，这与禁用可取消功能的客户端的意愿相违背。

其次，进入对象时可取消类型可以显式设置为*延迟*或*异步*。但与可取消状态一样，退出对象时可取消类型应始终恢复为进入对象时的值。

最后，只有取消安全的函数才能从可异步取消的线程中调用。

## 返回值

如果成功，`pthread_setcancelstate()` 和 `pthread_setcanceltype()` 函数将返回零。否则，应返回一个错误号以指示错误。

## 错误

`pthread_setcancelstate()` 函数可能因以下原因失败：

**[`EINVAL`]** 指定的状态不是 `PTHREAD_CANCEL_ENABLE` 或 `PTHREAD_CANCEL_DISABLE`。

`pthread_setcanceltype()` 函数可能因以下原因失败：

**[`EINVAL`]** 指定的状态不是 `PTHREAD_CANCEL_DEFERRED` 或 `PTHREAD_CANCEL_ASYNCHRONOUS`。

## 参见

[pthread_cancel(3)](pthread_cancel.3.md)

## 标准

`pthread_testcancel()` 函数遵循 ISO/IEC 9945-1:1996 ("POSIX.1") 标准。该标准允许实现将更多函数设为取消点。

`pthread_setcancelstate()` 函数按 -p1003.1-2024 标准要求是异步信号安全的。

## 作者

本手册页由 David Leonard <d@openbsd.org> 为 OpenBSD 的 [pthread_cancel(3)](pthread_cancel.3.md) 实现编写。
