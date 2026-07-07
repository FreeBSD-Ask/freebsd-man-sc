# nl_langinfo(3)

`nl_langinfo` — 语言信息

## 名称

`nl_langinfo`

## 库

Lb libc

## 概要

`#include <langinfo.h>`

`Ft char * Fn nl_langinfo nl_item item Ft char * Fn nl_langinfo_l nl_item item locale_t loc`

## 描述

`nl_langinfo` 函数返回一个指针，指向包含与程序或线程的 locale 中所定义的特定语言或文化区域相关信息的字符串；对于 `nl_langinfo_l`，则指向作为第二个参数传入的 locale 中所定义的相关信息。

以与 `item` 类别相对应的类别，或以 `LC_ALL` 类别调用 `setlocale`，可能覆盖返回值所指向的缓冲区。

`item` 的常量名和值定义在

`#include <langinfo.h>`

中。以下标准常量被识别：

| **常量** | **类别** | **描述** |
| --- | --- | --- |
| `CODESET` | `LC_CTYPE` | 代码集名称 |
| `D_T_FMT` | `LC_TIME` | 用于格式化日期和时间的字符串 |
| `D_FMT` | `LC_TIME` | 日期格式字符串 |
| `T_FMT` | `LC_TIME` | 时间格式字符串 |
| `T_FMT_AMPM` | `LC_TIME` | a.m. 或 p.m. 时间格式字符串 |
| `AM_STR` | `LC_TIME` | 上午前缀 |
| `PM_STR` | `LC_TIME` | 下午前缀 |
| `DAY_1` | `LC_TIME` | 一周第一天的名称 |
| `DAY_2` | `LC_TIME` | 一周第二天的名称 |
| `DAY_3` | `LC_TIME` | 一周第三天的名称 |
| `DAY_4` | `LC_TIME` | 一周第四天的名称 |
| `DAY_5` | `LC_TIME` | 一周第五天的名称 |
| `DAY_6` | `LC_TIME` | 一周第六天的名称 |
| `DAY_7` | `LC_TIME` | 一周第七天的名称 |
| `ABDAY_1` | `LC_TIME` | 一周第一天的缩写名称 |
| `ABDAY_2` | `LC_TIME` | 一周第二天的缩写名称 |
| `ABDAY_3` | `LC_TIME` | 一周第三天的缩写名称 |
| `ABDAY_4` | `LC_TIME` | 一周第四天的缩写名称 |
| `ABDAY_5` | `LC_TIME` | 一周第五天的缩写名称 |
| `ABDAY_6` | `LC_TIME` | 一周第六天的缩写名称 |
| `ABDAY_7` | `LC_TIME` | 一周第七天的缩写名称 |
| `MON_1` | `LC_TIME` | 第一月的名称 |
| `MON_2` | `LC_TIME` | 第二月的名称 |
| `MON_3` | `LC_TIME` | 第三月的名称 |
| `MON_4` | `LC_TIME` | 第四月的名称 |
| `MON_5` | `LC_TIME` | 第五月的名称 |
| `MON_6` | `LC_TIME` | 第六月的名称 |
| `MON_7` | `LC_TIME` | 第七月的名称 |
| `MON_8` | `LC_TIME` | 第八月的名称 |
| `MON_9` | `LC_TIME` | 第九月的名称 |
| `MON_10` | `LC_TIME` | 第十月的名称 |
| `MON_11` | `LC_TIME` | 第十一月的名称 |
| `MON_12` | `LC_TIME` | 第十二月的名称 |
| `ABMON_1` | `LC_TIME` | 第一月的缩写名称 |
| `ABMON_2` | `LC_TIME` | 第二月的缩写名称 |
| `ABMON_3` | `LC_TIME` | 第三月的缩写名称 |
| `ABMON_4` | `LC_TIME` | 第四月的缩写名称 |
| `ABMON_5` | `LC_TIME` | 第五月的缩写名称 |
| `ABMON_6` | `LC_TIME` | 第六月的缩写名称 |
| `ABMON_7` | `LC_TIME` | 第七月的缩写名称 |
| `ABMON_8` | `LC_TIME` | 第八月的缩写名称 |
| `ABMON_9` | `LC_TIME` | 第九月的缩写名称 |
| `ABMON_10` | `LC_TIME` | 第十月的缩写名称 |
| `ABMON_11` | `LC_TIME` | 第十一月的缩写名称 |
| `ABMON_12` | `LC_TIME` | 第十二月的缩写名称 |
| `ERA` | `LC_TIME` | 纪元描述段 |
| `ERA_D_FMT` | `LC_TIME` | 纪元日期格式字符串 |
| `ERA_D_T_FMT` | `LC_TIME` | 纪元日期和时间格式字符串 |
| `ERA_T_FMT` | `LC_TIME` | 纪元时间格式字符串 |
| `ALT_DIGITS` | `LC_TIME` | 数字的替代符号 |
| `RADIXCHAR` | `LC_NUMERIC` | 基数字符 |
| `THOUSEP` | `LC_NUMERIC` | 千位分隔符 |
| `YESEXPR` | `LC_MESSAGES` | 肯定响应扩展正则表达式 |
| `NOEXPR` | `LC_MESSAGES` | 否定响应扩展正则表达式 |
| `CRNCYSTR` | `LC_MONETARY` | 本地货币符号；若符号应出现在值之前则前缀 '-'，若符号应出现在值之后则前缀 '+'，若符号应替换基数字符则前缀 '.'；若本地货币符号为空字符串，实现可返回空字符串 |

以下非标准 FreeBSD 扩展也被识别：

| **常量** | **类别** | **描述** |
| --- | --- | --- |
| `D_MD_ORDER` | `LC_TIME` | 月/日顺序 |
| `ALTMON_1` | `LC_TIME` | 第一月的独立名称 |
| `ALTMON_2` | `LC_TIME` | 第二月的独立名称 |
| `ALTMON_3` | `LC_TIME` | 第三月的独立名称 |
| `ALTMON_4` | `LC_TIME` | 第四月的独立名称 |
| `ALTMON_5` | `LC_TIME` | 第五月的独立名称 |
| `ALTMON_6` | `LC_TIME` | 第六月的独立名称 |
| `ALTMON_7` | `LC_TIME` | 第七月的独立名称 |
| `ALTMON_8` | `LC_TIME` | 第八月的独立名称 |
| `ALTMON_9` | `LC_TIME` | 第九月的独立名称 |
| `ALTMON_10` | `LC_TIME` | 第十月的独立名称 |
| `ALTMON_11` | `LC_TIME` | 第十一月的独立名称 |
| `ALTMON_12` | `LC_TIME` | 第十二月的独立名称 |
| `YESSTR` | `LC_MESSAGES` | 肯定响应字符串 |
| `NOSTR` | `LC_MESSAGES` | 否定响应字符串 |

## 返回值

在未定义 langinfo 数据的 locale 中，`nl_langinfo` 返回指向 POSIX locale 中对应字符串的指针。`nl_langinfo_l` 返回与 `nl_langinfo` 相同的值。在所有 locale 中，若 `item` 包含无效设置，`nl_langinfo` 返回指向空字符串的指针。

## 实例

例如：

```c
nl_langinfo(ABDAY_1)
```

若所识别的语言为葡萄牙语，将返回指向字符串 `Dom` 的指针；若所识别的语言为英语，将返回指向字符串 `Sun` 的指针。

## 参见

[setlocale(3)](setlocale.3.md)

## 标准

`nl_langinfo` 函数遵循 Version 2 of the Single UNIX Specification ("SUSv2")。`nl_langinfo_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`nl_langinfo` 函数首次出现于 FreeBSD 4.6。
