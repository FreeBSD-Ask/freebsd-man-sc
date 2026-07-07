# ktrace(2)

`ktrace` — 进程跟踪

## 名称

`ktrace`

## 库

Lb libc

## 概要

```c
#include <sys/param.h>
#include <sys/time.h>
#include <sys/uio.h>
#include <sys/ktrace.h>

int
ktrace(const char *tracefile, int ops, int trpoints, int pid);
```

## 描述

`ktrace()` 系统调用启用或禁用一个或多个进程的跟踪。用户只能跟踪自己的进程。只有超级用户能跟踪 setuid 或 setgid 程序。

`tracefile` 参数给出用于跟踪的文件路径名。该文件必须存在且是调用进程可写的常规文件。所有跟踪记录总是追加到文件中，因此必须将文件截断为零长度以丢弃先前的跟踪数据。如果正在禁用跟踪点（参见下文的 KTROP_CLEAR），`tracefile` 可以为 NULL。

`ops` 参数指定请求的 ktrace 操作。定义的操作如下：

| 操作 | 说明 |
| --- | --- |
| KTROP_SET | 启用 `trpoints` 中指定的跟踪点。 |
| KTROP_CLEAR | 禁用 `trpoints` 中指定的跟踪点。 |
| KTROP_CLEARFILE | 停止所有跟踪。 |
| KTRFLAG_DESCEND | 跟踪更改应应用于指定进程及其所有当前子进程。 |

`trpoints` 参数指定感兴趣的跟踪点。定义的跟踪点如下：

| 跟踪点 | 说明 |
| --- | --- |
| KTRFAC_SYSCALL | 跟踪系统调用。 |
| KTRFAC_SYSRET | 跟踪系统调用的返回值。 |
| KTRFAC_NAMEI | 跟踪名称查找操作。 |
| KTRFAC_GENIO | 跟踪所有 I/O（注意此选项可能产生大量输出）。 |
| KTRFAC_PSIG | 跟踪投递的信号。 |
| KTRFAC_CSW | 跟踪上下文切换点。 |
| KTRFAC_USER | 跟踪应用程序特定的事件。 |
| KTRFAC_STRUCT | 跟踪某些数据结构。 |
| KTRFAC_SYSCTL | 跟踪 sysctl。 |
| KTRFAC_PROCCTOR | 跟踪进程创建。 |
| KTRFAC_PROCDTOR | 跟踪进程销毁。 |
| KTRFAC_CAPFAIL | 跟踪 capability 失败。 |
| KTRFAC_FAULT | 跟踪页面错误。 |
| KTRFAC_FAULTEND | 跟踪页面错误结束。 |
| KTRFAC_STRUCT_ARRAY | 跟踪某些数据结构的数组。 |
| KTRFAC_INHERIT | 将跟踪继承到未来的子进程。 |

每个跟踪事件输出一条记录，由通用头部和随后特定于跟踪点的结构组成。通用头部为：

```c
struct ktr_header {
        int             ktr_len;                /* buf 的长度 */
        short           ktr_type;               /* 跟踪记录类型 */
        pid_t           ktr_pid;                /* 进程 ID */
        char            ktr_comm[MAXCOMLEN+1];  /* 命令名 */
        struct timeval  ktr_time;               /* 时间戳 */
        long            ktr_tid;                /* 线程 ID */
};
```

`ktr_len` 字段指定此头部之后 `ktr_type` 数据的长度。`ktr_pid` 和 `ktr_comm` 字段指定生成记录的进程和命令。`ktr_time` 字段给出记录生成的时间（微秒级分辨率）。`ktr_tid` 字段持有线程 ID。

通用头部之后是 `ktr_len` 字节的 `ktr_type` 记录。类型特定的记录定义在

```c
#include <sys/ktrace.h>
```

include 文件中。

## SYSCTL 可调参数

以下 [sysctl(8)](../man8/sysctl.8.md) 可调参数影响 `ktrace()` 的行为：

**`kern.ktrace.genio_size`** 限制单个被跟踪的 I/O 请求记录到跟踪文件中的数据量。

**`kern.ktrace.request_pool`** 限制同一时间记录的跟踪事件数。

控制进程可调试性的 sysctl 可调参数（由 [p_candebug(9)](../man9/p_candebug.9.md) 确定）也会影响 `ktrace()` 的操作。

## 返回值

成功完成时返回 0；否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`ktrace()` 系统调用在以下情况下将失败：

**[ENOTDIR]** 路径前缀的某个组件不是目录。

**[ENAMETOOLONG]** 路径名的某个组件超过 255 个字符，或整个路径名超过 1023 个字符。

**[ENOENT]** 指定的 tracefile 不存在。

**[EACCES]** 路径前缀的某个组件拒绝搜索权限。

**[ELOOP]** 在转换路径名时遇到过多的符号链接。

**[EIO]** 从文件系统读取或向文件系统写入时发生 I/O 错误。

**[EINTEGRITY]** 从文件系统读取数据时检测到损坏的数据。

**[ENOSYS]** 内核未编译 `ktrace` 支持。

由于资源的临时短缺，线程可能无法记录一个或多个跟踪事件。此情况被内核记住，下一个成功的跟踪请求将在其 `ktr_type` 字段中设置 `KTR_DROP` 标志。

## 参见

[kdump(1)](../man1/kdump.1.md), [ktrace(1)](../man1/ktrace.1.md), [utrace(2)](utrace.2.md), [sysctl(8)](../man8/sysctl.8.md), [p_candebug(9)](../man9/p_candebug.9.md)

## 历史

`ktrace()` 系统调用首次出现于 4.4BSD。