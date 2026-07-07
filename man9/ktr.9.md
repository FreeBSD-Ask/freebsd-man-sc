# ktr(9)

`CTR0` — 内核跟踪设施

## 名称

`CTR0`

## 概要

```c
#include <sys/param.h>

#include <sys/ktr.h>

extern int ktr_cpumask;
extern int ktr_entries;
extern int ktr_extend;
extern int ktr_mask;
extern int ktr_verbose;
extern struct ktr_entry ktr_buf[];

void
CTR(u_int mask, char *format, ...)

void
CTR0(u_int mask, char *format)

void
CTR1(u_int mask, char *format, arg1)

void
CTR2(u_int mask, char *format, arg1, arg2)

void
CTR3(u_int mask, char *format, arg1, arg2, arg3)

void
CTR4(u_int mask, char *format, arg1, arg2, arg3, arg4)

void
CTR5(u_int mask, char *format, arg1, arg2, arg3, arg4, arg5)

void
CTR6(u_int mask, char *format, arg1, arg2, arg3, arg4, arg5, arg6)
```

## 描述

KTR 提供一个事件循环缓冲区，可以以 [printf(9)](printf.9.md) 风格记录事件。这些事件随后可通过 [ddb(4)](../man4/ddb.4.md)、gdb(1)（`ports/devel/gdb`）或 ktrdump(8) 转储。

事件通过 `CTR` 和 `CTR``x` 宏在内核中创建和记录。第一个参数是以下文件中定义的事件类型掩码（`KTR_*`）：

```c
#include <sys/ktr_class.h>
```

仅当 `mask` 中指定的任何事件类型在存储于 `ktr_mask` 的全局事件掩码中启用时，事件才被记录。`format` 参数是用于构建事件日志消息文本的 [printf(9)](printf.9.md) 风格格式字符串。格式字符串之后是零到六个由 `format` 引用的参数。每个事件除日志消息外，还记录有发起 CTR 调用的文件名和源代码行号以及时间戳。

事件按提供的参数原样存储在循环缓冲区中，格式化在转储时完成。不要使用指向生命周期有限的对象的指针，例如字符串，因为在打印缓冲区时指针可能已失效。

`CTR``x` 宏仅在各自接受的参数数量上不同，如名称所示。

`ktr_entries` 变量包含 `ktr_buf` 数组中的条目数。这些变量主要用于事后崩溃转储工具定位循环跟踪缓冲区的基址和长度。

`ktr_mask` 变量包含要记录的事件的运行时掩码。

CPU 事件掩码存储在 `ktr_cpumask` 变量中。

`ktr_verbose` 变量存储详细标志，控制事件是否除事件缓冲区外还记录到控制台。

## 实例

此示例演示了在 `KTR_PROC` 记录级别使用跟踪点。

```c
void
mi_switch()
{
	...
	/*
	 * 选择新当前进程并记录其开始时间。
	 */
	...
	CTR3(KTR_PROC, "mi_switch: old proc %p (pid %d)", p, p->p_pid);
	...
	cpu_switch();
	...
	CTR3(KTR_PROC, "mi_switch: new proc %p (pid %d)", p, p->p_pid);
	...
}
```

## 参见

[ktr(4)](../man4/ktr.4.md), ktrdump(8)

## 历史

KTR 内核跟踪设施首次出现于 BSD/OS，并导入 FreeBSD 5.0。

接受可变数量参数的 `CTR` 宏首次出现于 FreeBSD 14.0。

## 缺陷

目前所有 CPU 共享一个全局缓冲区。在某个时刻，使用每 CPU 缓冲区可能更有利，这样如果一个 CPU 停止或开始自旋，它在停止或自旋之前发出的日志消息不会被其他 CPU 的事件淹没。

`CTR``x` 宏中给出的参数以 `u_long` 存储，因此不要传递大于 `u_long` 类型大小的参数。例如，在 32 位架构上传递 64 位参数会产生不正确的结果。
