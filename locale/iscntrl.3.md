# iscntrl(3)

`iscntrl` — 控制字符测试

## 名称

`iscntrl`, `iscntrl_l`

## 库

Lb libc

## 概要

`#include <ctype.h>`

`Ft int Fn iscntrl int c Ft int Fn iscntrl_l int c locale_t loc`

## 描述

`iscntrl` 和 `iscntrl_l` 函数测试任何控制字符。参数的值必须可表示为 `unsigned char` 或 `EOF` 的值。

在 ASCII 字符集中，这包含以下字符（数值以八进制表示）：

| `000 NUL` | `001 SOH` | `002 STX` | `003 ETX` | `004 EOT` |
| --------- | --------- | --------- | --------- | --------- |
| `005 ENQ` | `006 ACK` | `007 BEL` | `010 BS` | `011 HT` |
| `012 NL` | `013 VT` | `014 NP` | `015 CR` | `016 SO` |
| `017 SI` | `020 DLE` | `021 DC1` | `022 DC2` | `023 DC3` |
| `024 DC4` | `025 NAK` | `026 SYN` | `027 ETB` | `030 CAN` |
| `031 EM` | `032 SUB` | `033 ESC` | `034 FS` | `035 GS` |
| `036 RS` | `037 US` | `177 DEL` | | |

`iscntrl_l` 函数接受一个显式的 locale 参数，而 `iscntrl` 函数使用当前的全局或每线程 locale。

## 返回值

`iscntrl` 和 `iscntrl_l` 函数在字符测试为假时返回零，在字符测试为真时返回非零。

## 兼容性

在具有大字符集的 locale 中接受超出 `unsigned char` 类型范围的参数的 4.4BSD 扩展被认为过时，可能在未来的版本中不再支持。应改用 `iswcntrl` 或 `iswcntrl_l` 函数。

## 参见

[ctype(3)](ctype.3.md), [ctype_l(3)](ctype_l.3.md), iswcntrl(3), iswcntrl_l(3), [xlocale(3)](xlocale.3.md), [ascii(7)](../man7/ascii.7.md)

## 标准

`iscntrl` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`iscntrl_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`iscntrl` 函数首次出现于 Version 7 AT&T UNIX。
