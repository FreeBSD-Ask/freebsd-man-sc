# fseek(3)

`fgetpos` — 重定位流

## 名称

`fgetpos`, `fseek`, `fseeko`, `fsetpos`, `ftell`, `ftello`, `rewind`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn fseek FILE *stream long offset int whence Ft long Fn ftell FILE *stream Ft void Fn rewind FILE *stream Ft int Fn fgetpos FILE * restrict stream fpos_t * restrict pos Ft int Fn fsetpos FILE *stream const fpos_t *pos`

`#include <sys/types.h>`

`Ft int Fn fseeko FILE *stream off_t offset int whence Ft off_t Fn ftello FILE *stream`

## 描述

`fseek` 函数为 `stream` 所指向的流设置文件位置指示器。新位置以字节为单位，通过将 `offset` 字节加到 `whence` 指定的位置获得。若 `whence` 设为 `SEEK_SET`、`SEEK_CUR` 或 `SEEK_END`，则偏移量分别相对于文件起始、当前位置指示器或文件末尾。成功调用 `fseek` 函数会清除该流的文件末尾指示器，并撤销 [ungetc(3)](ungetc.3.md) 和 [ungetwc(3)](ungetwc.3.md) 函数对同一流的影响。

`ftell` 函数获取 `stream` 所指向流的文件位置指示器的当前值。

`rewind` 函数将 `stream` 所指向流的文件位置指示器设置到文件起始。它等价于：

```sh
(void)fseek(stream, 0L, SEEK_SET)
```

不同之处在于流的错误指示器也会被清除（参见 clearerr(3)）。

由于 `rewind` 不返回值，希望检测错误的应用程序应先清除 `errno`，再调用 `rewind`，若 `errno` 非零则假定发生错误。

`fseeko` 函数与 `fseek` 相同，区别在于它接受 `off_t` 参数而非 `long`。同理，`ftello` 与 `ftell` 相同，区别在于返回 `off_t`。

`fgetpos` 和 `fsetpos` 函数是用于检索和设置文件当前位置的替代接口，类似于 `ftell` 和 `fseek`，区别在于当前位置存储在 `pos` 所指向的 `fpos_t` 类型不透明对象中。这些函数提供了一种可移植的方式，可定位到超过 `long int` 表示范围的偏移量。它们还可在 `fpos_t` 对象中存储额外的状态信息，以便在包含依赖状态的编码的多字节字符的文件中定位。尽管 `fpos_t` 传统上是整数类型，但应用程序不能假定它一定是；特别是，不得对此类型的对象进行算术运算。

若流是宽字符流（参见 [fwide(3)](fwide.3.md)），由 `offset` 和 `whence` 组合指定的位置必须包含多字节序列的首字节。

## 返回值

`rewind` 函数不返回值。

`fgetpos`、`fseek`、`fseeko` 和 `fsetpos` 函数成功完成时返回 0。否则返回非零值，并设置全局变量 `errno` 以指示错误。

`ftell` 和 `ftello` 成功完成时返回当前偏移量。否则返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

**`EBADF`** `stream` 参数不是可定位的流。

**`EINVAL`** `whence` 参数无效，或所得的文件位置指示器将被设置为负值。

**`EOVERFLOW`** 对于 `fseeko` 和 `ftello`，所得的文件偏移量是无法在 `off_t` 类型对象中正确表示的值；对于 `fseek` 和 `ftell`，则是无法在 `long` 类型对象中正确表示的值。

**`ESPIPE`** 流底层的文件描述符关联到管道或 FIFO，或文件位置指示器的值未指定（参见 [ungetc(3)](ungetc.3.md)）。

`fgetpos`、`fseek`、`fseeko`、`fsetpos`、`ftell`、`ftello` 和 `rewind` 函数也可能失败，并为 [fflush(3)](fflush.3.md)、fstat(2)、[lseek(2)](../man2/lseek.2.md) 和 malloc(3) 例程所指定的任何错误设置 `errno`。

## 参见

[lseek(2)](../man2/lseek.2.md), clearerr(3), [fwide(3)](fwide.3.md), [ungetc(3)](ungetc.3.md), [ungetwc(3)](ungetwc.3.md)

## 标准

`fgetpos`、`fsetpos`、`fseek`、`ftell` 和 `rewind` 函数遵循 ISO/IEC 9899:1990 ("ISO C89") 标准。

`fseeko` 和 `ftello` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1") 标准。

## 历史

`fseek`、`ftell` 和 `rewind` 函数首次出现于 Version 7 AT&T UNIX。
