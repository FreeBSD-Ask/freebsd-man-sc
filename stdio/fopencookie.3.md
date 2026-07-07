# fopencookie.3

`fopencookie` — 打开流

## 名称

`fopencookie`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft typedef ssize_t Fn (*cookie_read_function_t) void *cookie char *buf size_t size Ft typedef ssize_t Fn (*cookie_write_function_t) void *cookie const char *buf size_t size Ft typedef int Fn (*cookie_seek_function_t) void *cookie off64_t *offset int whence Ft typedef int Fn (*cookie_close_function_t) void *cookie`

```c
typedef struct {
	cookie_read_function_t	*read;
	cookie_write_function_t	*write;
	cookie_seek_function_t	*seek;
	cookie_close_function_t	*close;
} cookie_io_functions_t;
```

`Ft FILE * Fn fopencookie void *cookie const char *mode cookie_io_functions_t io_funcs`

## 描述

`fopencookie` 函数将流与最多四个“I/O 函数”关联。这些 I/O 函数将用于读取、写入、定位和关闭新流。

通常，省略某个函数意味着对生成的流执行相应操作的任何尝试都将失败。若省略 `write` 函数，写入流的数据会被丢弃。若省略 `close` 函数，关闭流时将刷新所有缓冲输出然后成功返回。

`read`、`write` 和 `close` 的调用约定必须分别与 [read(2)](../man2/read.2.md)、[write(2)](../man2/write.2.md) 和 [close(2)](../man2/close.2.md) 匹配，唯一区别是传递给它们的 `cookie` 参数（在 `fopencookie` 中指定）替代了传统的文件描述符参数。`seek` 函数使用 `*offset` 和 `whence` 更新当前流偏移量。若 `*offset` 非 NULL，则用当前流偏移量更新 `*offset`。

`fopencookie` 实现为 [funopen(3)](funopen.3.md) 接口的薄层封装。该接口的限制、可能性和要求同样适用于 `fopencookie`。

## 返回值

成功完成时，`fopencookie` 返回 `FILE` 指针。否则返回 `NULL`，并设置全局变量 `errno` 以指示错误。

## 错误

[`EINVAL`] 向 `fopencookie` 提供了无效的 `mode`。

[`ENOMEM`] `fopencookie` 函数可能失败并为 malloc(3) 例程指定的任何错误设置 `errno`。

## 参见

[fcntl(2)](../man2/fcntl.2.md), [open(2)](../man2/open.2.md), [fclose(3)](fclose.3.md), [fopen(3)](fopen.3.md), [fseek(3)](fseek.3.md), [funopen(3)](funopen.3.md)

## 历史

`funopen` 函数首次出现于 4.4BSD。`fopencookie` 函数首次出现于 FreeBSD 11。

## 缺陷

`fopencookie` 函数是非标准的 glibc 扩展，可能无法移植到 FreeBSD 和 Linux 以外的系统。
