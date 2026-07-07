# localeconv(3)

`localeconv` — C 的自然语言格式化

## 名称

`localeconv`

## 库

Lb libc

## 概要

`#include <locale.h>`

`Ft struct lconv * Fn localeconv void`

`#include <xlocale.h>`

`Ft struct lconv * Fn localeconv_l locale_t locale`

## 描述

`localeconv` 函数返回一个指向结构的指针，该结构提供用于格式化数字（尤其是货币值）的参数：

```c
struct lconv {
	char	*decimal_point;
	char	*thousands_sep;
	char	*grouping;
	char	*int_curr_symbol;
	char	*currency_symbol;
	char	*mon_decimal_point;
	char	*mon_thousands_sep;
	char	*mon_grouping;
	char	*positive_sign;
	char	*negative_sign;
	char	int_frac_digits;
	char	frac_digits;
	char	p_cs_precedes;
	char	p_sep_by_space;
	char	n_cs_precedes;
	char	n_sep_by_space;
	char	p_sign_posn;
	char	n_sign_posn;
	char	int_p_cs_precedes;
	char	int_n_cs_precedes;
	char	int_p_sep_by_space;
	char	int_n_sep_by_space;
	char	int_p_sign_posn;
	char	int_n_sign_posn;
};
```

各字段的含义如下：

**`decimal_point`** 小数点字符（货币值除外），不能为空字符串。

**`thousands_sep`** 小数点前数字组的分隔符（货币值除外）。

**`grouping`** 数字组的大小（货币值除外）。这是一个指向整数向量的指针，每个整数的大小为 `char`，表示从低位数字组到高位（从右到左）的组大小。列表可以以 0 或 `CHAR_MAX` 终止。如果列表以 0 终止，0 之前的最后一个组大小会重复使用以处理所有数字。如果列表以 `CHAR_MAX` 终止，则不再进行分组。

**`int_curr_symbol`** 标准化的国际货币符号。

**`currency_symbol`** 本地货币符号。

**`mon_decimal_point`** 货币值的小数点字符。

**`mon_thousands_sep`** 货币值数字组的分隔符。

**`mon_grouping`** 类似 `grouping`，但用于货币值。

**`positive_sign`** 用于表示非负货币值的字符，通常为空字符串。

**`negative_sign`** 用于表示负货币值的字符，通常为减号。

**`int_frac_digits`** 国际风格货币值中小数点后的数字位数。

**`frac_digits`** 本地风格货币值中小数点后的数字位数。

**`p_cs_precedes`** 若货币符号在非负货币值之前则为 1，若在其之后则为 0。

**`p_sep_by_space`** 若在货币符号与非负货币值之间插入空格则为 1，否则为 0。

**`n_cs_precedes`** 类似 `p_cs_precedes`，但用于负值。

**`n_sep_by_space`** 类似 `p_sep_by_space`，但用于负值。

**`p_sign_posn`** `positive_sign` 相对于非负数量和 `currency_symbol` 的位置，编码如下：

**`0`** 整个字符串两边加括号。

**`1`** 字符串之前。

**`2`** 字符串之后。

**`3`** 紧邻 `currency_symbol` 之前。

**`4`** 紧邻 `currency_symbol` 之后。

**`n_sign_posn`** 类似 `p_sign_posn`，但用于负货币值。

**`int_p_cs_precedes`** 同 `p_cs_precedes`，但用于国际格式化货币量。

**`int_n_cs_precedes`** 同 `n_cs_precedes`，但用于国际格式化货币量。

**`int_p_sep_by_space`** 同 `p_sep_by_space`，但用于国际格式化货币量。

**`int_n_sep_by_space`** 同 `n_sep_by_space`，但用于国际格式化货币量。

**`int_p_sign_posn`** 同 `p_sign_posn`，但用于国际格式化货币量。

**`int_n_sign_posn`** 同 `n_sign_posn`，但用于国际格式化货币量。

除非上文另有说明，字段的值为空字符串表示零长度结果或当前 locale 中不存在的值。`CHAR_MAX` 结果同样表示不可用的值。

`localeconv_l` 函数接受一个显式的 locale 参数。更多信息请参见 [xlocale(3)](xlocale.3.md)。

## 返回值

`localeconv` 函数返回一个指向静态对象的指针，该对象可能被后续对 [setlocale(3)](setlocale.3.md) 或 `localeconv` 的调用所修改。`localeconv_l` 的返回值与 locale 一起存储。它将保持有效，直到后续调用 [freelocale(3)](freelocale.3.md)。如果线程本地 locale 生效，则 `localeconv` 的返回值将保持有效，直到该 locale 被销毁。

## 错误

未定义错误。

## 参见

[setlocale(3)](setlocale.3.md), strfmon(3)

## 标准

`localeconv` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。

## 历史

`localeconv` 函数首次出现于 4.4BSD。
