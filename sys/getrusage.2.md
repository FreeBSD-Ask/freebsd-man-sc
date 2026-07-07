# getrusage(2)

`getrusage` — 获取资源利用信息

## 名称

`getrusage`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/time.h>`

`#include <sys/resource.h>`

```c
#define	RUSAGE_SELF	0
#define	RUSAGE_CHILDREN	-1
#define	RUSAGE_THREAD	1

int
getrusage(int who, struct rusage *rusage);
```

## 描述

`getrusage()` 系统调用返回描述当前线程、当前进程或其所有已终止子进程所利用资源的信息。`who` 参数为 `RUSAGE_THREAD`、`RUSAGE_SELF` 或 `RUSAGE_CHILDREN`。`rusage` 所指向的缓冲区将填入以下结构：

```c
struct rusage {
        struct timeval ru_utime; /* 使用的用户时间 */
        struct timeval ru_stime; /* 使用的系统时间 */
        long ru_maxrss;          /* 最大常驻集大小 */
        long ru_ixrss;           /* 积分共享文本内存大小 */
        long ru_idrss;           /* 积分非共享数据大小 */
        long ru_isrss;           /* 积分非共享栈大小 */
        long ru_minflt;          /* 页面回收 */
        long ru_majflt;          /* 缺页次数 */
        long ru_nswap;           /* 交换次数 */
        long ru_inblock;         /* 块输入操作 */
        long ru_oublock;         /* 块输出操作 */
        long ru_msgsnd;          /* 发送的消息 */
        long ru_msgrcv;          /* 接收的消息 */
        long ru_nsignals;        /* 接收的信号 */
        long ru_nvcsw;           /* 自愿上下文切换 */
        long ru_nivcsw;          /* 非自愿上下文切换 */
};
```

各字段的解释如下：

**`ru_utime`** 在用户模式下执行所花费的总时间。

**`ru_stime`** 代表进程在系统中执行所花费的总时间。

**`ru_maxrss`** 使用的最大常驻集大小（以千字节为单位）。

**`ru_ixrss`** 一个“积分”值，指示文本段使用的且同时与其他进程共享的内存量。此值以千字节 * 执行时钟滴答为单位表示。滴答是统计时钟滴答。统计时钟的频率为每秒 `sysconf(_SC_CLK_TCK)` 次滴答。

**`ru_idrss`** 进程数据段中非共享内存量的积分值（以千字节 * 执行时钟滴答为单位表示）。

**`ru_isrss`** 进程栈段中非共享内存量的积分值（以千字节 * 执行时钟滴答为单位表示）。

**`ru_minflt`** 在没有任何 I/O 活动的情况下服务的缺页次数；此处通过从等待重新分配的页面列表中“回收”页面帧来避免 I/O 活动。

**`ru_majflt`** 需要 I/O 活动来服务的缺页次数。

**`ru_nswap`** 进程从主内存中“交换”出来的次数。

**`ru_inblock`** 文件系统必须执行输入的次数。

**`ru_oublock`** 文件系统必须执行输出的次数。

**`ru_msgsnd`** 发送的 IPC 消息数。

**`ru_msgrcv`** 接收的 IPC 消息数。

**`ru_nsignals`** 投递的信号数。

**`ru_nvcsw`** 由于进程在其时间片完成之前自愿放弃处理器（通常为了等待资源的可用性）而导致的上下文切换次数。

**`ru_nivcsw`** 由于更高优先级的进程变为可运行或当前进程超过其时间片而导致的上下文切换次数。

## 注释

`ru_inblock` 和 `ru_oublock` 数字仅计实际 I/O；由缓存机制提供的数据仅计入第一个读取或写入该数据的进程。

## 返回值

成功完成时返回值 0；否则返回值 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`getrusage()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `who` 参数不是有效值。

**[`EFAULT`]** `rusage` 参数指定的地址不在进程地址空间的有效部分。

## 参见

[gettimeofday(2)](gettimeofday.2.md), [wait(2)](wait.2.md), [clocks(7)](../man7/clocks.7.md)

## 历史

`getrusage()` 系统调用出现于 4.2BSD。`RUSAGE_THREAD` 设施首次出现于 FreeBSD 8.1。

## 缺陷

无法获取尚未终止的子进程的信息。