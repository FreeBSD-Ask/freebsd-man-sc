# clock_gettime(2)

`clock_gettime` — 获取/设置/校准日期和时间

## 名称

`clock_gettime`, `clock_settime`, `clock_getres`

## 库

Lb libc

## 概要

`#include <time.h>`

```c
int
clock_gettime(clockid_t clock_id, struct timespec *tp);

int
clock_settime(clockid_t clock_id, const struct timespec *tp);

int
clock_getres(clockid_t clock_id, struct timespec *tp);
```

## 描述

`clock_gettime()` 和 `clock_settime()` 系统调用允许调用进程获取或设置由 `clock_id` 指定的时钟所使用的值。

`clock_id` 参数可以是从 [clock_getcpuclockid(3)](../man3/clock_getcpuclockid.3.md) 或 [pthread_getcpuclockid(3)](../man3/pthread_getcpuclockid.3.md) 获取的值，也可以是以下值之一：

**`CLOCK_REALTIME`**

**`CLOCK_REALTIME_PRECISE`**

**`CLOCK_REALTIME_FAST`**

**`CLOCK_REALTIME_COARSE`** 以 SI 秒为单位递增，类似于挂钟。它使用 1970 年纪元并实现 UTC 时间尺度。自 1970 年以来物理 SI 秒的计数，通过减去正闰秒数并加上负闰秒数进行调整。任何 POSIX 标准都未定义闰秒期间的行为。

**`CLOCK_MONOTONIC`**

**`CLOCK_MONOTONIC_PRECISE`**

**`CLOCK_MONOTONIC_FAST`**

**`CLOCK_MONOTONIC_COARSE`**

**`CLOCK_BOOTTIME`** 以 SI 秒为单位递增，即使在系统挂起期间也是如此。其纪元未指定。该计数不受闰秒调整。

**`CLOCK_UPTIME`**

**`CLOCK_UPTIME_PRECISE`**

**`CLOCK_UPTIME_FAST`** 在机器运行期间以 SI 秒单调递增。该计数不受闰秒调整。其纪元未指定。

**`CLOCK_VIRTUAL`** 仅在 CPU 代表调用进程以用户模式运行时递增。

**`CLOCK_PROF`** 在 CPU 以用户模式或内核模式运行时递增。

**`CLOCK_SECOND`** 返回当前秒数，无需执行完整的时间计数器查询，使用内核中缓存的当前秒数值。

**`CLOCK_PROCESS_CPUTIME_ID`** 返回调用进程的执行时间。

**`CLOCK_THREAD_CPUTIME_ID`** 返回调用线程的执行时间。

**`CLOCK_TAI`** 以 SI 秒为单位递增，类似于挂钟。它使用 1970 年纪元并实现 TAI 时间尺度。类似于 `CLOCK_REALTIME`，但没有闰秒。在闰秒期间它会单调递增。如果当前 TAI 与 UTC 之间的偏移量未知（在启动早期、NTP 或其他时间守护进程同步之前可能如此），将返回 `EINVAL` 错误。

时钟 ID `CLOCK_BOOTTIME`、`CLOCK_REALTIME`、`CLOCK_TAI`、`CLOCK_MONOTONIC` 和 `CLOCK_UPTIME` 会执行完整的时间计数器查询。带 _FAST 后缀的时钟 ID，即 `CLOCK_REALTIME_FAST`、`CLOCK_MONOTONIC_FAST` 和 `CLOCK_UPTIME_FAST`，不执行完整的时间计数器查询，因此其精度为一个定时器滴答。类似地，`CLOCK_REALTIME_PRECISE`、`CLOCK_MONOTONIC_PRECISE` 和 `CLOCK_UPTIME_PRECISE` 用于获取尽可能精确的值，代价是执行时间。时钟 ID `CLOCK_REALTIME_COARSE` 和 `CLOCK_MONOTONIC_COARSE` 是带 _FAST 后缀的相应 ID 的别名，用于与其他系统兼容。最后，`CLOCK_BOOTTIME` 是 `CLOCK_MONOTONIC` 的别名，用于与其他系统兼容，与 `kern.boottime` [sysctl(8)](../man8/sysctl.8.md) 无关。

`tp` 所指向的结构定义在 `<sys/timespec.h>` 中，如下：

```c
struct timespec {
        time_t  tv_sec;         /* 秒 */
        long    tv_nsec;        /* 纳秒 */
};
```

只有超级用户可以设置一天的时间，且仅能使用 `CLOCK_REALTIME`。如果系统 [securelevel(7)](../man7/securelevel.7.md) 大于 1（参见 [init(8)](../man8/init.8.md)），时间只能向前调整。此限制是为了防止恶意的超级用户在文件上设置任意时间戳。即使系统处于安全模式，仍可使用 [adjtime(2)](adjtime.2.md) 系统调用向后调整系统时间。

时钟的分辨率（粒度）由 `clock_getres()` 系统调用返回。该值存放在（非 NULL 的）`*tp` 中。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

以下错误码可能被设置在 `errno` 中：

**[`EINVAL`]** `clock_id` 或 `timespec` 参数不是有效值。

**[`EPERM`]** 非超级用户试图设置时间。

## 参见

[date(1)](../man1/date.1.md), [adjtime(2)](adjtime.2.md), [clock_getcpuclockid(3)](../man3/clock_getcpuclockid.3.md), [ctime(3)](../man3/ctime.3.md), [pthread_getcpuclockid(3)](../man3/pthread_getcpuclockid.3.md)

## 标准

`clock_gettime()`、`clock_settime()` 和 `clock_getres()` 系统调用遵循 IEEE Std 1003.1-2008 ("POSIX.1")。时钟 ID `CLOCK_BOOTTIME`、`CLOCK_MONOTONIC_FAST`、`CLOCK_MONOTONIC_PRECISE`、`CLOCK_REALTIME_FAST`、`CLOCK_REALTIME_PRECISE`、`CLOCK_SECOND`、`CLOCK_TAI`、`CLOCK_UPTIME`、`CLOCK_UPTIME_FAST` 和 `CLOCK_UPTIME_PRECISE` 是 FreeBSD 对 POSIX 接口的扩展。

UTC 由 ITU-R TF.460-6《标准频率和时间信号发射》定义。然而，`time_t` 类型是一个简单的计数，不提供闰秒的唯一编码，也未规定应使用什么值来编码闰秒。

## 历史

`clock_gettime()`、`clock_settime()` 和 `clock_getres()` 系统调用首次出现于 FreeBSD 3.0。