# strfmon.3

`strfmon` — 将货币值转换为字符串

## 名称

`strfmon`, `strfmon_l`

## 库

Lb libc

## 概要

`#include <monetary.h>`

```c
ssize_t
strfmon(char * restrict s, size_t maxsize,
    const char * restrict format, ...);
```

`#include <monetary.h>`

`#include <xlocale.h>`

```c
ssize_t
strfmon_l(char * restrict s, size_t maxsize, locale_t loc,
    const char * restrict format, ...);
```

## 描述

`strfmon` 函数根据 `format` 所指字符串的控制，将字符放入 `s` 所指向的数组中。放入数组的字节数不超过 `maxsize`。

`strfmon_l` 函数接受一个显式的 locale 参数，而 `strfmon` 函数使用当前的全局或每线程 locale。

格式字符串由零个或多个指令组成：普通字符（非 `%`），原样复制到输出流中；以及转换规范，每个转换规范导致提取零个或多个后续参数。每个转换规范以 `%` 字符引入。在 `%` 之后，按顺序出现以下内容：

- 零个或多个以下标志：
  - **`=`** `f` —— 一个 `=` 字符后跟另一个字符 `f`，用作数字填充字符。
  - **`^`** 不使用分组字符，无论当前 locale 默认设置如何。
  - **`+`** 通过为正值添加正号前缀、为负值添加负号前缀来表示。这是默认行为。
  - **`(`** 将负值用括号括起。
  - **`!`** 输出中不包含货币符号。
  - **`-`** 左对齐结果。仅在指定了字段宽度时有效。
- 一个可选的以十进制数表示的最小字段宽度。默认情况下没有最小宽度。
- 一个 `#` 符号后跟一个十进制数，指定 radix 字符之前预期的最大位数。使用此选项时，不超过指定位数的值会被格式化，使其与使用相同格式打印的其他值正确对齐。这包括始终为可能的符号指示符留出空间，即使特定值并不需要。
- 一个 `.` 字符后跟一个十进制数，指定 radix 字符之后的位数。
- 以下转换说明符之一：
  - **`i`** `double` 参数被格式化为国际货币金额。
  - **`n`** `double` 参数被格式化为本国货币金额。
  - **`%`** 写入一个 `%` 字符。

## 返回值

若结果字节总数（包括终止的 `NUL` 字节）不超过 `maxsize`，`strfmon` 和 `strfmon_l` 返回放入 `s` 所指数组中的字节数（不包括终止的 `NUL` 字节）。否则，返回 -1，数组内容不确定，并设置 `errno` 以指示错误。

## 实例

以下示例将值 `1234567.89` 格式化为字符串 `$1,234,567.89`：

```c
#include <stdio.h>
#include <monetary.h>
#include <locale.h>
int
main(void)
{
	char string[100];
	double money = 1234567.89;
	if (setlocale(LC_MONETARY, "en_US.UTF-8") == NULL) {
		fprintf(stderr, "Unable to setlocale().\n");
		return (1);
	}
	strfmon(string, sizeof(string) - 1, "%n", money);
	printf("%s\n", string);
	return (0);
}
```

## 错误

`strfmon` 函数在以下情况下将失败：

**[`E2BIG`]** 因缓冲区空间不足而停止转换。

**[`EINVAL`]** 格式字符串无效。

**[`EINVAL`]** 转换规范中包含 `+` 标志，且 locale 的 `positive_sign` 和 `negative_sign` 值经 [localeconv(3)](../locale/localeconv.3.md) 返回时均为空字符串。

**[`ENOMEM`]** 临时缓冲区内存不足。

## 参见

[localeconv(3)](../locale/localeconv.3.md), [xlocale(3)](../locale/xlocale.3.md)

## 标准

`strfmon` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。`strfmon_l` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 作者

`strfmon` 函数由 Alexey Zelkin <phantom@FreeBSD.org> 实现。

本手册页由 Jeroen Ruigrok van der Werven <asmodai@FreeBSD.org> 基于标准文本编写。

## 缺陷

`strfmon` 函数不能正确处理 `format` 参数中的多字节字符。
