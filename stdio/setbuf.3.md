# setbuf(3)

`setbuf` — 流缓冲操作

## 名称

`setbuf`, `setbuffer`, `setlinebuf`, `setvbuf`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft void Fn setbuf FILE * restrict stream char * restrict buf Ft void Fn setbuffer FILE *stream char *buf int size Ft int Fn setlinebuf FILE *stream Ft int Fn setvbuf FILE * restrict stream char * restrict buf int mode size_t size`

## 描述

可用的三种缓冲类型为无缓冲、块缓冲和行缓冲。当输出流为无缓冲时，信息一经写入即出现在目标文件或终端上；当为块缓冲时，许多字符被积累后作为一个块写入；当为行缓冲时，字符被积累直到输出换行符或从任何连接到终端设备的流读取输入（通常是 `stdin`）。可使用 [fflush(3)](fflush.3.md) 函数提前强制写出块。（参见 [fclose(3)](fclose.3.md)）

通常所有文件都是块缓冲的。当文件上发生首次 I/O 操作时，调用 malloc(3) 获取大小最优的缓冲区。若流引用终端（如 `stdout` 通常所做），则为行缓冲。标准错误流 `stderr` 始终无缓冲。注意，这些默认值可使用 stdbuf(1) 工具修改。

`setvbuf` 函数可用于修改流的缓冲行为。`mode` 参数必须是以下三个宏之一：

**`_IONBF`** 无缓冲

**`_IOLBF`** 行缓冲

**`_IOFBF`** 全缓冲

`size` 参数可为零，以按通常方式获得延迟的最优大小缓冲区分配。若不为零，则除无缓冲文件外，`buf` 参数应指向至少 `size` 字节长的缓冲区；此缓冲区将替代当前缓冲区使用。若 `buf` 不是 `NULL`，调用者有责任在关闭流后用 free(3) 释放此缓冲区。（若 `size` 参数不为零但 `buf` 为 `NULL`，将立即分配指定大小的缓冲区，并在关闭时释放。这是对 ANSI C 的扩展；可移植代码应使用大小为 0 且 `buf` 为 `NULL`。）

`setvbuf` 函数可在任何时候使用，但若流处于"活动"状态，可能产生特殊的副作用（如丢弃输入或刷新输出）。可移植的应用程序应仅在任何给定流上调用一次，且在任何 I/O 操作之前调用。

其他三个调用实际上是 `setvbuf` 调用的简单别名。除无返回值外，`setbuf` 函数完全等价于调用

```sh
setvbuf(stream, buf, buf ? _IOFBF : _IONBF, BUFSIZ);
```

`setbuffer` 函数相同，区别在于缓冲区大小由调用者决定，而非由默认的 `BUFSIZ` 决定。`setlinebuf` 函数完全等价于调用：

```sh
setvbuf(stream, (char *)NULL, _IOLBF, 0);
```

## 返回值

`setvbuf` 函数成功时返回 0，若请求无法满足则返回 `EOF`（注意此情况下流仍可正常使用）。

`setlinebuf` 函数返回等价的 `setvbuf` 调用所会返回的值。

## 参见

stdbuf(1), [fclose(3)](fclose.3.md), [fopen(3)](fopen.3.md), [fread(3)](fread.3.md), malloc(3), [printf(3)](printf.3.md), puts(3)

## 标准

`setbuf` 和 `setvbuf` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。

## 历史

`setbuf` 函数首次出现于 Version 7 AT&T UNIX。`setbuffer` 函数首次出现于 4.1cBSD。`setlinebuf` 函数首次出现于 4.2BSD。`setvbuf` 函数首次出现于 4.4BSD。

## 缺陷

`setbuf` 通常使用次优的缓冲区大小，应避免使用。
