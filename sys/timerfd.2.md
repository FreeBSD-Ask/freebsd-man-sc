# timerfd(2)

`timerfd` — 具有文件描述符语义的定时器

## 名称

`timerfd`, `timerfd_create`, `timerfd_gettime`, `timerfd_settime`

## 库

Lb libc

## 概要

```c
#include <sys/timerfd.h>

int
timerfd_create(int clockid, int flags);

int
timerfd_gettime(int fd, struct itimerspec *curr_value);

int
timerfd_settime(int fd, int flags,
    const struct itimerspec *new_value, struct itimerspec *old_value);
```

## 描述

`timerfd` 系统调用操作由特殊的 `timerfd` 文件描述符标识的定时器。这些调用类似于 `timer_create()`、`timer_gettime()` 和 `timer_settime()` 每进程定时器函数，但使用 `timerfd` 描述符代替 `timerid`。

所有 `timerfd` 描述符都具有传统的文件描述符语义；它们可以传递给其他进程，在 [fork(2)](fork.2.md) 后保留，并可通过 [kqueue(2)](kqueue.2.md)、[poll(2)](poll.2.md) 或 [select(2)](select.2.md) 监视。当 `timerfd` 描述符不再需要时，可使用 [close(2)](close.2.md) 释放。

**`timerfd_create()`** 初始化一个 `timerfd` 对象并返回其文件描述符。`clockid` 参数指定用作计时基准的时钟，可以是：

**`CLOCK_REALTIME`** 像挂钟一样递增。

**`CLOCK_BOOTTIME`**

**`CLOCK_MONOTONIC`** 以 SI 秒为单位单调递增。

**`CLOCK_UPTIME`** 以 SI 秒为单位单调递增，但在系统挂起时暂停。

有关更精确的定义，参见 [clock_gettime(2)](clock_gettime.2.md)。`flags` 参数可以包含以下值按位或的结果：

**`TFD_CLOEXEC`** 新生成的文件描述符将设置为 close-on-exec。

**`TFD_NONBLOCK`** 在读/写操作时不阻塞。

**`timerfd_gettime()`** 获取由 `fd` 表示的定时器的当前状态。结果以 `struct itimerspec` 形式存储在 `curr_value` 中。`curr_value` 的 `it_value` 和 `it_interval` 成员分别表示距下次到期的相对时间和上次由 `timerfd_settime()` 设置的间隔重载值。

**`timerfd_settime()`** 使用 `new_value` 中的 `struct itimerspec` 更新由 `fd` 表示的定时器。`new_value` 的 `it_value` 成员应包含定时器到期前的时间量，若应解除定时器则为零。`it_interval` 成员应包含所需的间隔定时器的重载时间。如果 `old_value` 不为 `NULL`，先前的定时器状态将存储在 `old_value` 中。`flags` 参数可以包含以下值按位或的结果：

**`TFD_TIMER_ABSTIME`** 将在 `new_value` 中提供的绝对时间到期。通常，`new_value` 表示相对于定时器 `clockid` 时钟的相对时间。

**`TFD_TIMER_CANCEL_ON_SET`** 如果 `clockid` 设置为 `CLOCK_REALTIME` 且实时时钟经历了不连续跳变，则定时器将被取消，下一次 [read(2)](read.2.md) 将失败并返回 `ECANCELED`。

文件操作具有以下语义：

**`FIOASYNC int`** 非零输入将设置 FASYNC 标志。零输入将清除 FASYNC 标志。

**`FIONBIO int`** 非零输入将设置 FNONBLOCK 标志。零输入将清除 FNONBLOCK 标志。

**[read(2)](read.2.md)** 将自上次成功 [read(2)](read.2.md) 或 `timerfd_settime()` 以来发生的定时器到期次数传输到大小为 `uint64_t` 的输出缓冲区。如果到期计数器为零，[read(2)](read.2.md) 将阻塞直到定时器到期，除非设置了 `TFD_NONBLOCK`，此时返回 `EAGAIN`。

**[poll(2)](poll.2.md)** 当文件描述符的定时器到期计数器大于零时，该文件描述符可读。

**[ioctl(2)](ioctl.2.md)**

## 返回值

`timerfd_create()` 系统调用创建一个 `timerfd` 对象并返回其文件描述符。如果发生错误，返回 -1，并设置全局变量 `errno` 以指示错误。

`timerfd_gettime()` 和 `timerfd_settime()` 系统调用成功时返回 0。如果发生错误，返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`timerfd_create()` 系统调用在以下情况下失败：

**[`EINVAL`]** 不支持指定的 `clockid`。

**[`EINVAL`]** 提供的 `flags` 无效。

**[`EMFILE`]** 每进程描述符表已满。

**[`ENFILE`]** 系统文件表已满。

**[`ENOMEM`]** 内核无法为定时器分配足够的内存。

`timerfd_gettime()` 和 `timerfd_settime()` 系统调用在以下情况下失败：

**[`EBADF`]** 提供的 `fd` 无效。

**[`EFAULT`]** `curr_value`、`new_value` 或 `old_value` 提供的地址无效。

**[`EINVAL`]** 提供的 `fd` 有效，但并非由 `timerfd_create()` 生成。

以下错误仅适用于 `timerfd_settime()`：

**[`EINVAL`]** 提供的 `flags` 无效。

**[`EINVAL`]** `new_value` 参数中的纳秒字段指定了小于零或大于等于 10^9 的值。

**[`ECANCELED`]** 定时器使用时钟 ID `CLOCK_REALTIME` 创建，配置了 `TFD_TIMER_CANCEL_ON_SET` 标志，且系统实时时钟经历了不连续变化但未被读取。

从 `timerfd` 对象读取在以下情况下失败：

**[`EAGAIN`]** 定时器的到期计数器为零，且 `timerfd` 对象设置为非阻塞 I/O。

**[`ECANCELED`]** 定时器使用时钟 ID `CLOCK_REALTIME` 创建，配置了 `TFD_TIMER_CANCEL_ON_SET` 标志，且系统实时时钟经历了不连续变化。

**[`EINVAL`]** 读取缓冲区的大小不足以容纳 `uint64_t` 大小的定时器到期计数器。

## 参见

[eventfd(2)](eventfd.2.md), [kqueue(2)](kqueue.2.md), [poll(2)](poll.2.md), [read(2)](read.2.md), [timer_create(2)](timer_create.2.md), timer_gettime(2), [timer_settime(2)](timer_settime.2.md)

## 标准

`timerfd` 系统调用源自 Linux，是非标准的。

## 历史

`timerfd` 设施最初由 Dmitry Chagin <dchagin@FreeBSD.org> 在 FreeBSD 12.0 中移植到 FreeBSD 的 Linux 兼容层。后来由 Jake Freeland <jfree@FreeBSD.org> 在 FreeBSD 14.0 中修订并改造为原生实现。
