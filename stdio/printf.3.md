# printf(3)

`printf` — 格式化输出转换

## 名称

`printf`, `fprintf`, `sprintf`, `snprintf`, `asprintf`, `dprintf`, `vprintf`, `vfprintf`, `vsprintf`, `vsnprintf`, `vasprintf`, `vdprintf`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft int Fn printf const char * restrict format ... Ft int Fn fprintf FILE * restrict stream const char * restrict format ... Ft int Fn sprintf char * restrict str const char * restrict format ... Ft int Fn snprintf char * restrict str size_t size const char * restrict format ... Ft int Fn asprintf char **ret const char *format ... Ft int Fn dprintf int fd const char * restrict format ...`

`#include <stdarg.h>`

`Ft int Fn vprintf const char * restrict format va_list ap Ft int Fn vfprintf FILE * restrict stream const char * restrict format va_list ap Ft int Fn vsprintf char * restrict str const char * restrict format va_list ap Ft int Fn vsnprintf char * restrict str size_t size const char * restrict format va_list ap Ft int Fn vasprintf char **ret const char *format va_list ap Ft int Fn vdprintf int fd const char * restrict format va_list ap`

## 描述

`printf` 函数族根据下文所述的 `format` 产生输出。`printf` 和 `vprintf` 函数将输出写入 `stdout`（标准输出流）；`fprintf` 和 `vfprintf` 将输出写入给定的输出 `stream`；`dprintf` 和 `vdprintf` 将输出写入给定的文件描述符；`sprintf`、`snprintf`、`vsprintf` 和 `vsnprintf` 写入字符串 `str`；`asprintf` 和 `vasprintf` 通过 malloc(3) 动态分配新字符串。

这些函数在 `format` 字符串的控制下写入输出，该字符串指定后续参数（或通过 stdarg(3) 的变长参数机制访问的参数）如何转换为输出。

`asprintf` 和 `vasprintf` 函数将 `*ret` 设置为指向一个足以容纳格式化字符串的缓冲区。不再需要时，应将该指针传递给 free(3) 以释放分配的存储空间。如果无法分配足够空间，`asprintf` 和 `vasprintf` 将返回 -1，并将 `ret` 设置为 `NULL` 指针。

`snprintf` 和 `vsnprintf` 函数最多将 `size`-1 个打印字符写入输出字符串（第 `size` 个字符为终止符 `'\0'`）；如果返回值大于或等于 `size` 参数，说明字符串太短，部分打印字符被丢弃。除非 `size` 为 0，否则输出始终以 null 结尾。

`sprintf` 和 `vsprintf` 函数实际上假定 `size` 为 `INT_MAX + 1`。

格式字符串由零个或多个指令组成：普通字符（非 `%`），原样复制到输出流；以及转换说明，每个转换说明都会取出零个或多个后续参数。每个转换说明以 `%` 字符引入。参数必须（在类型提升后）与转换说明符正确对应。`%` 之后按顺序出现以下内容：

- 一个可选字段，由一个十进制数字字符串后跟 `$` 组成，指定下一个要访问的参数。如果未提供此字段，将使用上次访问参数之后的下一个参数。参数编号从 `1` 开始。如果格式字符串中未访问的参数与已访问的参数交替出现，结果将不确定。
- 零个或多个以下标志：
  - **`#`**  值应转换为"替代形式"。对于 `c`、`d`、`i`、`n`、`p`、`s` 和 `u` 转换，此选项无效。对于 `b` 和 `B` 转换，非零结果会在前面加上字符串 `0b`（或 `B` 转换的 `0B`）。对于 `o` 转换，会增加数字的精度以强制输出字符串的首字符为零。对于 `x` 和 `X` 转换，非零结果会在前面加上字符串 `0x`（或 `X` 转换的 `0X`）。对于 `a`、`A`、`e`、`E`、`f`、`F`、`g` 和 `G` 转换，结果始终包含小数点，即使其后没有数字（通常，只有当后面跟有数字时，这些转换的结果中才会出现小数点）。对于 `g` 和 `G` 转换，不会像通常那样移除结果中的尾随零。
  - **`0`**  零填充。对于除 `n` 外的所有转换，转换后的值在左侧用零而非空格填充。如果对数值转换（`b`、`B`、`d`、`i`、`o`、`u`、`i`、`x` 和 `X`）指定了精度，则忽略 `0` 标志。
  - **`-`**  负的字段宽度标志；转换后的值在字段边界上左对齐。除 `n` 转换外，转换后的值在右侧用空格填充，而非在左侧用空格或零填充。如果同时给出了 `-` 和 `0`，则 `-` 优先。
  - **空格**  对于带符号转换（`a`、`A`、`d`、`e`、`E`、`f`、`F`、`g`、`G` 或 `i`）产生的正数，其前应保留一个空格。
  - **`+`**  带符号转换产生的数字前必须始终放置符号。如果同时使用 `+` 和空格，则 `+` 优先。
  - **`'`**  十进制转换（`d`、`u` 或 `i`）或浮点转换（`f` 或 `F`）的整数部分应使用 localeconv(3) 返回的非货币分隔符进行千位分组和分隔。
- 一个可选的十进制数字字符串，指定最小字段宽度。如果转换后的值字符数少于字段宽度，则在左侧（或右侧，如果给出了左对齐标志）用空格填充以填满字段宽度。
- 一个可选的精度，形式为句点 `.` 后跟可选的数字字符串。如果省略数字字符串，则精度取零。对于 `b`、`B`、`d`、`i`、`o`、`u`、`x` 和 `X` 转换，这指定了要出现的最小数字位数；对于 `a`、`A`、`e`、`E`、`f` 和 `F` 转换，指定了小数点后要出现的数字位数；对于 `g` 和 `G` 转换，指定了最大有效数字位数；对于 `s` 转换，指定了从字符串打印的最大字符数。
- 一个可选的长度修饰符，指定参数的大小。以下长度修饰符对 `b`、`B`、`d`、`i`、`n`、`o`、`u`、`x` 或 `X` 转换有效：

| **修饰符** | `d`, `i` | `b`, `B`, `o`, `u`, `x`, `X` | `n` |
| ---------- | -------- | ---------------------------- | --- |
| `hh` | `signed char` | `unsigned char` | `signed char *` |
| `h` | `short` | `unsigned short` | `short *` |
| `l` (ell) | `long` | `unsigned long` | `long *` |
| `ll` (ell ell) | `long long` | `unsigned long long` | `long long *` |
| `j` | `intmax_t` | `uintmax_t` | `intmax_t *` |
| `t` | `ptrdiff_t` | (见注释) | `ptrdiff_t *` |
| `w`N | `intN_t` | `uintN_t` | `intN_t *` |
| `wf`N | `int_fastN_t` | `uint_fastN_t` | `int_fastN_t *` |
| `z` | (见注释) | `size_t` | (见注释) |
| `q` *(已弃用)* | `quad_t` | `u_quad_t` | `quad_t *` |

注意：`t` 修饰符应用于 `b`、`B`、`o`、`u`、`x` 或 `X` 转换时，表示参数为大小等同于 `ptrdiff_t` 的无符号类型。`z` 修饰符应用于 `d` 或 `i` 转换时，表示参数为大小等同于 `size_t` 的有符号类型。类似地，应用于 `n` 转换时，表示参数是指向大小等同于 `size_t` 的有符号类型的指针。以下长度修饰符对 `a`、`A`、`e`、`E`、`f`、`F`、`g` 或 `G` 转换有效：

| **修饰符** | `a`, `A`, `e`, `E`, `f`, `F`, `g`, `G` |
| ---------- | -------------------------------------- |
| `l` (ell) | `double`（忽略，行为与不带该修饰符相同） |
| `L` | `long double` |

以下长度修饰符对 `c` 或 `s` 转换有效：

| **修饰符** | `c` | `s` |
| ---------- | --- | --- |
| `l` (ell) | `wint_t` | `wchar_t *` |

- 一个指定要应用的转换类型的字符。

字段宽度或精度，或两者，可以用星号 `*` 或星号后跟一个或多个十进制数字和 `$`（而非数字字符串）来表示。此时，由一个 `int` 参数提供字段宽度或精度。负的字段宽度被视为左对齐标志后跟正的字段宽度；负的精度被视为省略。如果单个格式指令混合使用位置参数（`nn$`）和非位置参数，结果未定义。

转换说明符及其含义如下：

- **`bBdiouxX`**  `int`（或适当变体）参数转换为无符号二进制（`b` 和 `B`）、有符号十进制（`d` 和 `i`）、无符号八进制（`o`）、无符号十进制（`u`）或无符号十六进制（`x` 和 `X`）表示法。`x` 转换使用字母"`abcdef`"；`X` 转换使用字母"`ABCDEF`"。精度（如果有）给出了必须出现的最小数字位数；如果转换后的值需要更少的数字，则在左侧用零填充。
- **`DOU`**  `long int` 参数转换为有符号十进制、无符号八进制或无符号十进制，分别如同格式为 `ld`、`lo` 或 `lu`。这些转换字符已弃用，最终将消失。
- **`eE`**  `double` 参数经舍入后按 `[-]d.ddd e±dd` 风格转换，其中小数点字符前有一位数字，小数点后的数字位数等于精度；如果未指定精度，取为 6；如果精度为零，不出现小数点字符。`E` 转换使用字母 `E`（而非 `e`）引入指数。指数始终至少包含两位数字；如果值为零，指数为 00。对于 `a`、`A`、`e`、`E`、`f`、`F`、`g` 和 `G` 转换，使用小写转换字符时，正负无穷分别表示为 `inf` 和 `-inf`，使用大写转换字符时分别表示为 `INF` 和 `-INF`。类似地，使用小写转换时 NaN 表示为 `nan`，使用大写转换时表示为 `NAN`。
- **`fF`**  `double` 参数经舍入后按 `[-]ddd.ddd` 风格转换为十进制表示法，其中小数点字符后的数字位数等于精度规范。如果未指定精度，取为 6；如果精度显式为零，不出现小数点字符。如果出现小数点，则其前至少有一位数字。
- **`gG`**  `double` 参数按 `f` 或 `e` 风格（或 `G` 转换的 `F` 或 `E` 风格）转换。精度指定有效数字位数。如果未指定精度，取为 6 位；如果精度为零，视为 1。当转换的指数小于 -4 或大于等于精度时，使用 `e` 风格。移除结果小数部分中的尾随零；仅当其后跟至少一位数字时才出现小数点。
- **`aA`**  `double` 参数经舍入后按 `[-]0xh.hhhp±d` 风格转换为十六进制表示法，其中十六进制小数点字符后的数字位数等于精度规范。如果未指定精度，取为足以精确表示该浮点数的位数，且不进行舍入。如果精度为零，不出现十六进制小数点字符。`p` 是字面字符 `p`，指数由正负号后跟表示以 2 为底的指数的十进制数组成。`A` 转换使用前缀"`0X`"（而非"`0x`"）、字母"`ABCDEF`"（而非"`abcdef`"）表示十六进制数字，以及字母 `P`（而非 `p`）分隔尾数和指数。注意，以这种十六进制格式表示浮点数可能有多种有效方式。例如，`0x1.92p+1`、`0x3.24p+0`、`0x6.48p-1` 和 `0xc.9p-2` 都是等价的。FreeBSD 8.0 及更高版本始终使用 `1` 作为十六进制小数点前的数字来打印有限非零数。零始终以尾数 0（适当时前面加 `-`）和指数 `+0` 表示。
- **`C`**  视为带 `l` (ell) 修饰符的 `c`。
- **`c`**  `int` 参数转换为 `unsigned char`，并写入结果字符。如果使用 `l` (ell) 修饰符，`wint_t` 参数转换为 `wchar_t`，并写入表示该单个宽字符的（可能为多字节的）序列，包括任何移位序列。如果使用了移位序列，在该字符之后还将移位状态恢复为原始状态。
- **`S`**  视为带 `l` (ell) 修饰符的 `s`。
- **`s`**  `char *` 参数应为指向字符类型数组（指向字符串的指针）的指针。数组中的字符被写入，直到（但不包括）终止 `NUL` 字符；如果指定了精度，写入的字符数不超过指定数目。如果给出了精度，无需存在 null 字符；如果未指定精度，或精度大于数组大小，数组必须包含终止 `NUL` 字符。如果使用 `l` (ell) 修饰符，`wchar_t *` 参数应为指向宽字符数组（指向宽字符串的指针）的指针。对于字符串中的每个宽字符，写入表示该宽字符的（可能为多字节的）序列，包括任何移位序列。如果使用了移位序列，在该字符串之后还将移位状态恢复为原始状态。数组中的宽字符被写入，直到（但不包括）终止的宽 `NUL` 字符；如果指定了精度，写入的字节数不超过指定数目（包括移位序列）。从不写入部分字符。如果给出了精度，无需存在 null 字符；如果未指定精度，或精度大于渲染该字符串多字节表示所需的字节数，数组必须包含终止的宽 `NUL` 字符。
- **`p`**  `void *` 指针参数以十六进制打印（如同 `%#x` 或 `%#lx`）。
- **`n`**  目前已写入的字符数存储到 `int *`（或变体）指针参数所指示的整数中。不转换任何参数。
- **`m`**  打印调用开始时存储在 `errno` 变量中的错误代码的字符串表示，由 strerror(3) 返回。不取任何参数。
- **`%`**  写入一个 `%`。不转换任何参数。完整的转换说明为 `%%`。

小数点字符由程序的 locale（`LC_NUMERIC` 类别）定义。

字段宽度不存在或过小都不会导致数值字段截断；如果转换结果比字段宽度更宽，则扩展字段以容纳转换结果。

## 返回值

这些函数返回打印的字符数（不包括用于结束字符串输出的尾随 `'\0'`），但 `snprintf` 和 `vsnprintf` 除外，它们返回如果 `size` 不受限本应打印的字符数（同样不包括最后的 `'\0'`）。发生错误时这些函数返回负值。

## 实例

要以"`Sunday, July 3, 10:02`"的形式打印日期和时间，其中 `weekday` 和 `month` 是指向字符串的指针：

```c
#include <stdio.h>
fprintf(stdout, "%s, %s %d, %.2d:%.2d\n",
	weekday, month, day, hour, min);
```

要将 π 打印到小数点后五位：

```c
#include <math.h>
#include <stdio.h>
fprintf(stdout, "pi = %.5f\n", 4 * atan(1.0));
```

分配一个 128 字节的字符串并打印到其中：

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
char *newfmt(const char *fmt, ...)
{
	char *p;
	va_list ap;
	if ((p = malloc(128)) == NULL)
		return (NULL);
	va_start(ap, fmt);
	(void) vsnprintf(p, 128, fmt, ap);
	va_end(ap);
	return (p);
}
```

## 兼容性

转换格式 `%D`、`%O` 和 `%U` 不是标准的，仅为向后兼容而提供。转换格式 `%m` 也不是标准的，提供了来自 GNU C 库的流行扩展。

用零填充 `%p` 格式（通过 `0` 标志或指定精度），以及 `#` 标志对 `%n` 和 `%p` 转换的良性影响（即无影响），还有其他无意义的组合如 `%Ld`，都不是标准的；应避免此类组合。

## 错误

除 [write(2)](../sys/write.2.md) 系统调用文档中所述的错误外，`printf` 函数族还可能在以下情况下失败：

**`EILSEQ`** 遇到无效的宽字符代码。

**`ENOMEM`** 可用存储空间不足。

**`EOVERFLOW`** `size` 参数超过 `INT_MAX + 1`，或返回值太大而无法用 `int` 表示。

## 参见

printf(1), errno(2), fmtcheck(3), [scanf(3)](scanf.3.md), setlocale(3), strerror(3), [wprintf(3)](wprintf.3.md)

## 标准

受下文缺陷章节中所述注意事项的约束，`fprintf`、`printf`、`sprintf`、`vprintf`、`vfprintf` 和 `vsprintf` 函数遵循 ANSI X3.159-1989 ("ANSI C89") 和 ISO/IEC 9899:1999 ("ISO C99") 标准。在相同保留条件下，`snprintf` 和 `vsnprintf` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")，而 `dprintf` 和 `vdprintf` 遵循 IEEE Std 1003.1-2008 ("POSIX.1")。`asprintf` 和 `vasprintf` 函数遵循 IEEE Std 1003.1-2024 ("POSIX.1")。

## 历史

`asprintf` 和 `vasprintf` 函数首次出现于 GNU C 库。由 Peter Wemm <peter@FreeBSD.org> 在 FreeBSD 2.2 中实现，后来在 OpenBSD 2.3 中由 Todd C. Miller <Todd.Miller@courtesan.com> 替换为不同的实现。`dprintf` 和 `vdprintf` 函数添加于 FreeBSD 8.0。`%m` 格式扩展首次出现于 GNU C 库，在 FreeBSD 12.0 中实现。

## 缺陷

`vdprintf` 函数族不能正确处理 `format` 参数中的多字节字符。

## 安全注意事项

`sprintf` 和 `vsprintf` 函数容易被误用，使得恶意用户可通过缓冲区溢出攻击任意更改运行中程序的功能。由于 `sprintf` 和 `vsprintf` 假定字符串长度无限，调用者必须注意不要溢出实际空间；这通常难以保证。为安全起见，程序员应改用 `snprintf` 接口。例如：

```c
void
foo(const char *arbitrary_string, const char *and_another)
{
	char onstack[8];
#ifdef BAD
	/*
	 * 第一个 sprintf 是不良行为。不要使用 sprintf！
	 */
	sprintf(onstack, "%s, %s", arbitrary_string, and_another);
#else
	/*
	 * 以下两行展示了 snprintf() 的更好用法。
	 */
	snprintf(onstack, sizeof(onstack), "%s, %s", arbitrary_string,
	    and_another);
#endif
}
```

`printf` 和 `sprintf` 函数族也容易被误用，使得恶意用户可通过导致程序打印"留在栈上"的潜在敏感数据，或通过解引用无效指针导致程序产生内存故障或总线错误，从而任意更改运行中程序的功能。

`%n` 可用于向经过精心选择的地址写入任意数据。因此，强烈建议程序员永远不要将不可信的字符串作为 `format` 参数传递，因为攻击者可在字符串中放入格式说明符来破坏你的栈，导致可能的安全漏洞。即使字符串是使用 `snprintf` 等函数构建的也是如此，因为结果字符串仍可能包含用户提供的转换说明符，供后续 `printf` 插值。

始终使用正确的安全写法：

```c
snprintf(buffer, sizeof(buffer), "%s", string);
```
