# strptime.3

`strptime` — 解析日期和时间字符串

## 名称

`strptime`

## 库

Lb libc

## 概要

`#include <time.h>`

`Ft char * Fo strptime const char * restrict buf const char * restrict format struct tm * restrict timeptr Fc`

`#include <time.h>`

`#include <xlocale.h>`

`Ft char * Fn strptime_l const char * restrict buf const char * restrict format struct tm * restrict timeptr locale_t loc`

## 描述

`strptime` 函数按照 `format` 所指向的字符串解析缓冲区 `buf` 中的字符串，并填充 `timeptr` 所指向结构的元素。结果值相对于本地时区。因此，可视为 [strftime(3)](strftime.3.md) 的逆操作。`strptime_l` 函数与 `strptime` 功能相同，但使用显式指定的 locale 而非当前 locale。

`format` 字符串由零个或多个转换说明和普通字符组成。所有普通字符与缓冲区精确匹配，格式字符串中的空白字符可匹配缓冲区中任意数量的空白字符。所有转换说明与 [strftime(3)](strftime.3.md) 中描述的相同。

两位数的年份值（包括 `%y` 和 `%D` 格式）按 POSIX 要求解释为始于 1969 年。69-00 的年份解释为 20 世纪（1969-2000），01-68 的年份解释为 21 世纪（2001-2068）。`%U` 和 `%W` 格式说明符接受 00 到 53 范围内的任意值。

若 `format` 字符串未包含足够的转换说明来完整指定结果 `struct tm`，则 `timeptr` 中未指定的成员保持不变。例如，若 `format` 为“`%H:%M:%S`”，仅修改 `tm_hour`、`tm_sec` 和 `tm_min`。若需要相对于今天的时间，在传递给 `strptime` 之前，应使用今天的日期初始化 `timeptr` 结构。

## 返回值

成功完成时，`strptime` 返回指向 `buf` 中第一个无需用于满足 `format` 中指定转换的字符的指针。若其中一个转换失败，返回 `NULL`。`strptime_l` 返回与 `strptime` 相同的值。

## 参见

[date(1)](../man1/date.1.md), [scanf(3)](scanf.3.md), [strftime(3)](strftime.3.md)

## 历史

`strptime` 函数出现于 FreeBSD 3.0。

## 作者

`strptime` 函数由 Powerdog Industries 贡献。

本手册页由 J(:org Wunsch 编写。

## 注意事项

`strptime` 函数假定使用格里高利历（公历），对其引入之前的日期会产生错误结果。

## 缺陷

当预期值仅包含单个数字且该数字后紧随另一个数字时，`%e` 和 `%l` 格式说明符可能错误地多扫描一位数字。这两个说明符都接受零填充值，即使它们都被定义为接受未填充值。

`%p` 格式说明符仅在小时相关说明符*之后*解析时才有效。指定 `%l` 而不带 `%p` 会产生未定义结果。注意 12AM（ante meridiem）视为午夜，12PM（post meridiem）视为正午。

`%Z` 格式说明符仅接受本地时区的时区缩写，以及 "GMT"、"UTC" 或 "Z"。此限制是因为时区缩写重载导致的歧义。例如 `EST` 既表示美国东部标准时间，也表示澳大利亚东部夏令时。

`strptime` 函数不能正确处理 `format` 参数中的多字节字符。
