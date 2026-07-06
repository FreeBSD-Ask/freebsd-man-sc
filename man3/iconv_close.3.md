# iconv_close.3

`iconv_open` — 代码集转换函数

## 名称

`iconv_open`, `iconv_open_into`, `iconv_close`, `iconv`

## 库

Lb libc

## 概要

`#include <iconv.h>`

`Ft iconv_t Fn iconv_open const char *dstname const char *srcname Ft int Fn iconv_open_into const char *dstname const char *srcname iconv_allocation_t *ptr Ft int Fn iconv_close iconv_t cd Ft size_t Fn iconv iconv_t cd char ** restrict src size_t * restrict srcleft char ** restrict dst size_t * restrict dstleft Ft size_t Fn __iconv iconv_t cd char ** restrict src size_t * restrict srcleft char ** restrict dst size_t * restrict dstleft uint32_t flags size_t * invalids`

## 描述

`iconv_open` 函数打开从代码集 `srcname` 到代码集 `dstname` 的转换器，并返回其描述符。`srcname` 和 `dstname` 参数接受 "" 和 "char"，它们指向当前 locale 编码。

`iconv_open_into` 在预分配的空间上创建转换描述符。`iconv_allocation_t` 在分配此类空间时用作占位类型。`dstname` 和 `srcname` 参数与 `iconv_open` 中相同。`ptr` 参数是指向预分配空间的 `iconv_allocation_t` 指针。

`iconv_close` 函数关闭指定的转换器 `cd`。

`iconv` 函数转换 `*src` 缓冲区中长度为 `*srcleft` 字节的字符串，并将转换后的字符串存储到大小为 `*dstleft` 字节的 `*dst` 缓冲区中。调用 `iconv` 后，`src`、`srcleft`、`dst` 和 `dstleft` 所指向的值按如下方式更新：

***src** 指向已取出的最后一个字符之后那个字节的指针。

***srcleft** 源缓冲区中剩余的字节数。

***dst** 指向已存储的最后一个字符之后那个字节的指针。

***dstleft** 目标缓冲区中剩余的字节数。

若 `*src` 所指向的字符串包含在源代码集中不是合法字符的字节序列，转换在最后一次成功转换之后停止。若输出缓冲区太小而无法存储转换后的字符，转换也以同样方式停止。这些情况下，`src`、`srcleft`、`dst` 和 `dstleft` 所指向的值会更新为最后一次成功转换之后的状态。

若 `*src` 所指向的字符串包含在源代码集下合法但无法转换到目标代码集的字符，该字符会被“无效字符”替换（取决于目标代码集，如 ‘?’），转换继续进行。`iconv` 返回此类“无效转换”的次数。

`iconv` 有两种特殊情况：

**src** == NULL || *src == NULL 若源和/或目标代码集是有状态的，`iconv` 将其置为初始状态。若 `dst` 和 `*dst` 均非 `NULL`，`iconv` 将目标切换到初始状态的移位序列存储到 `*dst` 所指向的缓冲区中。缓冲区大小由 `dstleft` 所指向的值指定，如上所述。若缓冲区太小而无法存储移位序列，`iconv` 将失败。另一方面，`dst` 或 `*dst` 可以为 `NULL`。此情况下，目标切换到初始状态的移位序列被丢弃。

`__iconv` 函数工作方式与 `iconv` 相同，但若 `iconv` 失败，无效字符计数会丢失。这不是 bug，而是 IEEE Std 1003.1-2008 ("POSIX.1") 的限制，因此提供 `__iconv` 作为替代的非标准接口。它还有一个 flags 参数，目前可传递以下标志：

**__ICONV_F_HIDE_INVALID** 跳过无效字符，而不是返回错误。

## 返回值

`iconv_open` 成功完成时返回转换描述符。否则，`iconv_open` 返回 (iconv_t)-1 并设置 errno 以指示错误。

`iconv_open_into` 成功完成时返回 0。否则，`iconv_open_into` 返回 -1，并设置 errno 以指示错误。

`iconv_close` 成功完成时返回 0。否则，`iconv_close` 返回 -1 并设置 errno 以指示错误。

`iconv` 成功完成时返回“无效”转换的次数。否则，`iconv` 返回 (size_t)-1 并设置 errno 以指示错误。

## 错误

`iconv_open` 函数可能在以下情况下导致错误：

**[Er** ENOMEM] 内存耗尽。

**[Er** EINVAL] 不存在由 `srcname` 和 `dstname` 指定的转换器。

`iconv_open_into` 函数可能在以下情况下导致错误：

**[Er** EINVAL] 不存在由 `srcname` 和 `dstname` 指定的转换器。

`iconv_close` 函数可能在以下情况下导致错误：

**[Er** EBADF] `cd` 指定的转换描述符无效。

`iconv` 函数可能在以下情况下导致错误：

**[Er** EBADF] `cd` 指定的转换描述符无效。

**[Er** EILSEQ] `*src` 所指向的字符串包含不描述源代码集合法字符的字节序列。

**[Er** E2BIG] `*dst` 所指向的输出缓冲区太小，无法存储结果字符串。

**[Er** EINVAL] `*src` 所指向的字符串以不完整的字符或移位序列结束。

## 参见

iconv(1), mkcsmapper(1), mkesdb(1), [__iconv_get_list(3)](__iconv_get_list.3.md), [iconv_canonicalize(3)](iconv_canonicalize.3.md), [iconvctl(3)](iconvctl.3.md), [iconvlist(3)](iconvlist.3.md)

## 标准

`iconv_open`、`iconv_close` 和 `iconv` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

`iconv_open_into` 函数是 GNU 特定扩展，不属于任何标准，因此使用它可能破坏可移植性。`__iconv` 函数是自有扩展，不属于任何标准，因此使用它可能破坏可移植性。
