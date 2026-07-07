# inet6_opt_init(3)

`inet6_opt_init` — IPv6 逐跳与目的地选项操作

## 名称

`inet6_opt_init`, `inet6_opt_append`, `inet6_opt_finish`, `inet6_opt_set_val`, `inet6_opt_next`, `inet6_opt_find`, `inet6_opt_get_val`

## 库

libc

## 概要

`#include <netinet/in.h>`

```c
int
inet6_opt_init(void *extbuf, socklen_t extlen);

int
inet6_opt_append(void *extbuf, socklen_t extlen, int offset, uint8_t type,
    socklen_t len, uint8_t align, void **databufp);

int
inet6_opt_finish(void *extbuf, socklen_t extlen, int offset);

int
inet6_opt_set_val(void *databuf, int offset, void *val, socklen_t vallen);

int
inet6_opt_next(void *extbuf, socklen_t extlen, int offset, uint8_t *typep,
    socklen_t *lenp, void **databufp);

int
inet6_opt_find(void *extbuf, socklen_t extlen, int offset, uint8_t type,
    socklen_t *lenp, void **databufp);

int
inet6_opt_get_val(void *databuf, int offset, void *val, socklen_t vallen);
```

## 描述

构建和解析逐跳与目的地选项较为复杂。高级套接字 API 定义了一组函数，帮助应用程序创建和操作逐跳与目的地选项。本手册页描述了 IETF 草案 RFC 3542 中规定的函数。这些函数使用 RFC 2460 附录 B 中规定的格式规则，即最大的字段放在选项的最后。这些函数的函数原型都包含在

`#include <netinet/in.h>`

头文件中。

### inet6_opt_init

`inet6_opt_init` 函数返回空扩展头（即不含任何选项的扩展头）所需的字节数。如果 `extbuf` 参数指向一段有效的内存，`inet6_opt_init` 函数还会初始化扩展头的长度字段。当尝试初始化传入 `extbuf` 参数的扩展缓冲区时，`extlen` 必须是 8 的正整数倍，否则函数失败并向调用者返回 -1。

### inet6_opt_append

`inet6_opt_append` 函数可执行两种不同的任务。当提供有效的 `extbuf` 参数时，它会将一个选项追加到扩展缓冲区，返回更新后的总长度以及指向新创建选项的指针（通过 `databufp`）。如果 `extbuf` 的值为 `NULL`，则 `inet6_opt_append` 函数仅报告在实际追加该选项时的总长度。`len` 和 `align` 参数指定选项的长度和追加选项时必须使用的数据对齐方式。`offset` 参数应为 `inet6_opt_init` 函数或先前调用 `inet6_opt_append` 所返回的长度。

`type` 参数是 8 位的选项类型。

调用 `inet6_opt_append` 后，应用程序可以直接使用 `databufp` 所指向的缓冲区，或使用 `inet6_opt_set_val` 指定选项中要包含的数据。

选项类型 `0` 和 `1` 保留给 `Pad1` 和 `PadN` 选项。从 2 到 255 的所有其他值均可由应用程序使用。

选项数据的长度包含在一个 8 位值中，因此可以取 0 到 255 之间的任何值。

`align` 参数必须为 1、2、4 或 8，且不能超过 `len` 的值。这些对齐值分别表示无对齐、16 位、32 位和 64 位对齐。

### inet6_opt_finish

`inet6_opt_finish` 函数计算为使扩展头成为 8 字节的整数倍（IPv6 扩展头规范所要求）所需的最终填充，并返回扩展头更新后的总长度。`offset` 参数应为 `inet6_opt_init` 或 `inet6_opt_append` 返回的长度。当 `extbuf` 不为 `NULL` 时，该函数还通过插入适当长度的 Pad1 或 PadN 选项来设置填充字节。

如果扩展头太小而无法容纳所需的填充，则向调用者返回 -1 错误。

### inet6_opt_set_val

`inet6_opt_set_val` 函数将不同大小的数据项插入选项的数据部分。`databuf` 参数是指向由 `inet6_opt_append` 调用返回的内存的指针，`offset` 参数指定数据在数据缓冲区中的放置位置。`val` 参数指向包含要插入扩展头的数据的内存区域，`vallen` 参数指示要复制的数据量。

调用者应确保每个字段按其自然边界对齐，如 RFC 2460 附录 B 所述。

该函数返回下一个字段的偏移量，计算方式为 `offset` + `vallen`，在组合具有多个字段的选项时使用。

### inet6_opt_next

`inet6_opt_next` 函数解析接收到的扩展头。`extbuf` 和 `extlen` 参数指定要解析的扩展头的位置和长度。`offset` 参数对于第一个选项应为零，或者为先前调用 `inet6_opt_next` 或 `inet6_opt_find` 返回的长度值。返回值指定继续扫描扩展缓冲区的位置。选项通过参数 `typep`、`lenp` 和 `databufp` 返回，分别指向 8 位选项类型、8 位选项长度和选项数据。此函数不返回任何 PAD1 或 PADN 选项。当发生错误或没有更多选项时，返回值为 -1。

### inet6_opt_find

`inet6_opt_find` 函数在扩展缓冲区中搜索通过 `type` 参数传入的特定选项类型。如果找到该选项，则更新 `lenp` 和 `databufp` 参数，分别指向选项的长度和数据。`extbuf` 和 `extlen` 参数必须指向有效的扩展缓冲区并给出其长度。`offset` 参数可用于从扩展头中的任意位置开始搜索。

### inet6_opt_get_val

`inet6_opt_get_val` 函数从选项的数据部分提取不同大小的数据项。`databuf` 是由 `inet6_opt_next` 或 `inet6_opt_find` 函数返回的指针。`val` 参数指向提取数据存放的位置。`offset` 参数指定从选项数据部分的哪个位置提取值；选项数据的第一个字节由偏移量零指定。

每个字段应按其自然边界对齐，如 RFC 2460 附录 B 所述。

该函数通过计算 `offset` + `vallen` 返回下一个字段的偏移量，可在提取具有多个字段的选项内容时使用。健壮的接收方必须在调用此函数前验证对齐方式。

## 返回值

所有函数在出错时返回 -1。

## 实例

RFC 3542 第 22 节给出了详尽的示例。

KAME 也在其套件的 `advapitest` 目录中提供了示例。

## 参见

> W. Stevens, M. Thomas, E. Nordmark, T. Jinmei, "Advanced Sockets API for IPv6", RFC 3542, October 2002.

> S. Deering, R. Hinden, "Internet Protocol, Version 6 (IPv6) Specification", RFC 2460, December 1998.

## 标准

这些函数记录于 "Advanced Sockets API for IPv6"（RFC 3542）。

## 历史

该实现首次出现于 KAME 高级网络套件。
