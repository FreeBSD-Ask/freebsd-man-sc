# printf(9)

`printf` — 格式化输出转换

## 名称

`printf`, `uprintf`, `tprintf`, `log`

## 概要

```c
#include <sys/types.h>
```

```c
#include <sys/systm.h>
```

```c
int
printf(const char *fmt, ...)

void
tprintf(struct proc *p, int pri, const char *fmt, ...)

int
uprintf(const char *fmt, ...)

int
vprintf(const char *fmt, va_list ap)
```

```c
#include <sys/syslog.h>
```

```c
void
log(int pri, const char *fmt, ...)

void
vlog(int pri, const char *fmt, va_list ap)
```

## 描述

`log` 系列函数类似于 printf(3) 系列函数。不同函数各自使用不同的输出流。`uprintf` 函数输出到当前进程的控制终端，而 `printf` 同时写入控制台和日志设施。`tprintf` 函数输出到与进程 `p` 关联的终端，如果 `pri` 不为 -1，则同时输出到日志设施。`log` 函数将消息发送到内核日志设施，使用由 `pri` 指示的日志级别，并在尚无进程读取日志时同时发送到控制台。

这些相关函数均以与 printf(3) 相同的方式使用 `fmt` 参数。然而，`log` 添加了两个其他转换说明符，并省略了一个。

`%b` 标识符需要两个参数：一个 `int` 和一个 `char *`。它们用作寄存器值和用于解码位掩码的打印掩码。打印掩码由两部分组成：基和参数。基值是以八进制表示的输出基数（radix）；例如，\10 表示八进制，\20 表示十六进制。参数由一系列位标识符组成。每个位标识符以一个指定该标识符所描述位号（从 1 开始）的字符开头。从 \01 到 \40 的字符可用于指定 1 到 32 范围内的位号，从 \200 到 \377 的字符可用于指定 1 到 128 范围内的位号。标识符的其余部分是包含该位名称的字符串。标识符以下一个位标识符开头的位号或最后一个位标识符的 `NUL` 终止。

`%D` 标识符用于辅助十六进制转储。它需要两个参数：一个 `u_char *` 指针和一个 `char *` 字符串。指针所指向的内存以十六进制每次一字节地输出。该字符串用作各个字节之间的分隔符。如果存在宽度指令，则指定要显示的字节数。默认情况下，输出 16 字节的数据。

不支持 `%n` 转换说明符。

`log` 函数对其 `pri` 参数使用 syslog(3) 级别值 `LOG_DEBUG` 到 `LOG_EMERG`（此处被误称为“priority”）。或者，如果给定 `pri` 为 -1，则消息将追加到由先前调用 `log` 开始的最后一条日志消息中。由于这些消息由内核本身生成，因此 facility 始终为 `LOG_KERN`。

## 返回值

`printf` 和 `uprintf` 函数返回显示的字符数。

## 实例

此示例演示了 `%b` 和 `%D` 转换说明符的使用。函数

```c
void
printf_test(void)
{
	printf("reg=%b\n", 3, "\10\2BITTWO\1BITONE");
	printf("out: %4D\n", "AAZZ", ":");
}
```

将产生以下输出：

```c
reg=3<BITTWO,BITONE>
out: 41:41:5a:5a
```

以下函数将产生相同的输出：

```c
void
printf_test(void)
{
	printf("reg=%b\n", 3, "\10\201BITTWO\200BITONE");
	printf("out: %4D\n", "AAZZ", ":");
}
```

调用

```c
log(LOG_DEBUG, "%s%d: been there.\n", sc->sc_name, sc->sc_unit);
```

将以“`kern.debug`”优先级向系统日志添加相应的调试消息。

## 参见

[printf(3)](../stdio/printf.3.md), [syslog(3)](../gen/syslog.3.md)
