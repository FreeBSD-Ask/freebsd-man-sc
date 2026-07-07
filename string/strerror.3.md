# strerror(3)

`strerror` — 系统错误消息

## 名称

`perror`, `strerror`, `strerror_l`, `strerror_r`, `sys_errlist`, `sys_nerr`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft void Fn perror const char *string extern const char * const sys_errlist[]; extern const int sys_nerr;`

`#include <string.h>`

`Ft char * Fn strerror int errnum Ft char * Fn strerror_l int errnum locale_t Ft int Fn strerror_r int errnum char *strerrbuf size_t buflen`

## 描述

`strerror`、`strerror_l`、`strerror_r` 和 `perror` 函数查找与错误号对应的错误消息字符串。

`strerror` 函数接受错误号参数 `errnum`，返回指向当前 locale 中对应消息字符串的指针。`strerror` 不是线程安全的。它返回指向内部静态缓冲区的指针，该缓冲区可能被其他线程的 `strerror` 调用覆盖。

`strerror_l` 函数接受错误号参数 `errnum` 和 locale 句柄参数 `locale`，返回指向给定 locale 中对应错误的字符串的指针。`strerror_l` 是线程安全的，其结果仅能被当前线程的另一次 `strerror_l` 调用覆盖。

`strerror_r` 函数将相同的结果写入 `strerrbuf`，最多 `buflen` 个字符，成功时返回 0。

`perror` 函数查找与全局变量 `errno`（intro(2)）的当前值对应的错误消息，并将其后跟一个换行符写入标准错误文件描述符。若参数 `string` 非 `NULL` 且不指向空字符，则该字符串将被添加到消息字符串之前，中间以冒号和空格（`": "`）分隔；否则仅打印错误消息字符串。

若错误号无法识别，这些函数返回包含 `"Unknown error: "` 后跟十进制错误号的错误消息字符串。`strerror` 和 `strerror_r` 函数返回 `EINVAL` 作为警告。本实现可识别的错误号范围是 0 < `errnum` < `sys_nerr`。数字 0 也可识别，但利用此特性的应用程序可能使用未指定的 `errno` 值。

若 `strerrbuf` 中提供的存储空间（由 `buflen` 指定）不足以容纳错误字符串，`strerror_r` 返回 `ERANGE`，且 `strerrbuf` 将包含已截断并以 `NUL` 结尾的错误消息，以适应 `buflen` 指定的长度。

可以使用外部数组 `sys_errlist` 直接访问消息字符串。外部值 `sys_nerr` 包含 `sys_errlist` 中消息的数量。这些变量的使用已弃用；应改用 `strerror`、`strerror_l` 或 `strerror_r`。

## 实例

以下示例展示如何使用 `perror` 报告错误。

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
int
main(void)
{
	int fd;
	if ((fd = open("/nonexistent", O_RDONLY)) == -1) {
		perror("open()");
		exit(1);
	}
	printf("File descriptor: %den", fd);
	return (0);
}
```

执行时，程序将打印类似 `open(): No such file or directory` 的错误消息。

## 参见

intro(2), err(3), psignal(3)

## 标准

`perror` 和 `strerror` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。`strerror_r` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。`strerror_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`strerror` 和 `perror` 函数首次出现于 4.4BSD。`strerror_r` 函数由 Wes Peters <wes@FreeBSD.org> 在 FreeBSD 4.4 中实现。`strerror_l` 函数添加于 FreeBSD 13.0。

## 缺陷

`strerror` 函数将其结果返回在静态缓冲区中，该缓冲区将被后续调用覆盖。

使用已弃用的 `sys_errlist` 变量的程序通常无法编译，因为其声明方式不一致。`sys_errlist` 对象的大小可能在 FreeBSD 的生命周期内增加，从而破坏某些 ABI 稳定性保证。
