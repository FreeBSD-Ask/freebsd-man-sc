# err(3)

`err` — 格式化错误消息

## 名称

`err`, `verr`, `errc`, `verrc`, `errx`, `verrx`, `warn`, `vwarn`, `warnc`, `vwarnc`, `warnx`, `vwarnx`, `err_set_exit`, `err_set_file`

## 库

Lb libc

## 概要

`#include <err.h>`

```c
void
err(int eval, const char *fmt, ...);

void
err_set_exit(void (*exitf)(int));

void
err_set_file(void *vfp);

void
errc(int eval, int code, const char *fmt, ...);

void
errx(int eval, const char *fmt, ...);

void
warn(const char *fmt, ...);

void
warnc(int code, const char *fmt, ...);

void
warnx(const char *fmt, ...);
```

`#include <stdarg.h>`

```c
void
verr(int eval, const char *fmt, va_list args);

void
verrc(int eval, int code, const char *fmt, va_list args);

void
verrx(int eval, const char *fmt, va_list args);

void
vwarn(const char *fmt, va_list args);

void
vwarnc(int code, const char *fmt, va_list args);

void
vwarnx(const char *fmt, va_list args);
```

## 描述

`err` 和 `warn` 系列函数在标准错误输出上显示格式化的错误消息，或在使用 `err_set_file` 函数指定的另一个文件上显示。在所有情况下，都会输出程序名的最后一个组件、一个冒号和一个空格。如果 `fmt` 参数不是 NULL，则输出类似 [printf(3)](../stdio/printf.3.md) 的格式化错误消息。输出以换行符终止。

`err`、`errc`、`verr`、`verrc`、`warn`、`warnc`、`vwarn` 和 `vwarnc` 函数会附加从 [strerror(3)](../string/strerror.3.md) 获取的错误消息，该消息基于提供的错误代码值或全局变量 `errno`，除非 `fmt` 参数为 `NULL`，否则在前面加一个冒号和空格。

如果内核除了 `errno` 代码外还返回了扩展错误字符串，`err` 函数会打印该字符串并插入参数的值，如对相应 EXTERROR(9) 调用所提供的那样。如果未提供扩展错误字符串，但提供了扩展错误信息，或者即使提供了字符串且 `EXTERROR_VERBOSE` 环境变量存在，则会打印附加报告。该报告至少包括错误的类别、源文件名（如果所用版本的 libc 已知）、源行号和参数。如果 `EXTERROR_VERBOSE` 环境变量存在且设置为 "brief"，则报告仅添加源文件名（如果所用版本的 libc 已知）和源行号。打印字符串的格式不是契约性的，可能会更改。

对于 `errc`、`verrc`、`warnc` 和 `vwarnc` 函数，`code` 参数用于查找错误消息。

`err`、`verr`、`warn` 和 `vwarn` 函数使用全局变量 `errno` 查找错误消息。

`errx` 和 `warnx` 函数不附加错误消息。

`err`、`verr`、`errc`、`verrc`、`errx` 和 `verrx` 函数不返回，而是以参数 `eval` 的值退出。建议 `eval` 的值使用 [sysexits(3)](../man3/sysexits.3.md) 中定义的标准值。`err_set_exit` 函数可用于指定一个在 [exit(3)](../stdlib/exit.3.md) 之前调用的函数，以执行任何必要的清理工作；为 `exitf` 传递空函数指针会将钩子重置为无操作。`err_set_file` 函数设置其他函数使用的输出流。其 `vfp` 参数必须是指向打开流的指针（可能已转换为 void *）或空指针（在这种情况下，输出流设置为标准错误）。

## 实例

显示当前 errno 信息字符串并退出：

```c
if ((p = malloc(size)) == NULL)
	err(EX_OSERR, NULL);
if ((fd = open(file_name, O_RDONLY, 0)) == -1)
	err(EX_NOINPUT, "%s", file_name);
```

显示错误消息并退出：

```c
if (tm.tm_hour < START_TIME)
	errx(EX_DATAERR, "too early, wait until %s",
	    start_time_string);
```

警告错误：

```c
if ((fd = open(raw_device, O_RDONLY, 0)) == -1)
	warnx("%s: %s: trying the block device",
	    raw_device, strerror(errno));
if ((fd = open(block_device, O_RDONLY, 0)) == -1)
	err(EX_OSFILE, "%s", block_device);
```

在不使用全局变量 `errno` 的情况下警告错误：

```c
error = my_function();	/* 返回 <errno.h> 中的值 */
if (error != 0)
	warnc(error, "my_function");
```

## 参见

[exit(3)](../stdlib/exit.3.md), [fmtmsg(3)](fmtmsg.3.md), [printf(3)](../stdio/printf.3.md), [strerror(3)](../string/strerror.3.md), [sysexits(3)](../man3/sysexits.3.md)

## 标准

`err` 和 `warn` 系列函数是 BSD 扩展。因此，不应在真正需要可移植性的代码中使用它们。请改用 `strerror` 或类似函数。

## 历史

`err` 和 `warn` 函数首次出现于 4.4BSD。`err_set_exit` 和 `err_set_file` 函数首次出现于 FreeBSD 2.1。`errc` 和 `warnc` 函数首次出现于 FreeBSD 3.0。