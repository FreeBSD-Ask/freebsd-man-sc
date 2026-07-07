# strtonum.3

`strtonum` — 可靠地将字符串值转换为整数

## 名称

`strtonum`, `strtonumx`

## 概要

`#include <stdlib.h>`

```c
long long
strtonum(const char *nptr, long long minval, long long maxval,
    const char **errstr);

long long
strtonumx(const char *nptr, long long minval, long long maxval,
    const char **errstr, int base);
```

## 描述

`strtonum` 和 `strtonumx` 函数将 `nptr` 中的字符串转换为 `long long` 值。这些函数旨在实现安全、健壮的编程，并克服 [atoi(3)](atoi.3.md) 和 [strtol(3)](strtol.3.md) 系列接口的缺陷。

字符串可以以任意数量的空白字符（由 [isspace(3)](../locale/isspace.3.md) 判定）开头，后跟一个可选的 `+` 或 `-` 符号。

字符串的其余部分按十进制（`strtonum`）或给定的进制（`strtonumx`）转换为 `long long` 值。

随后将所得值与提供的 `minval` 和 `maxval` 边界进行比较。若 `errstr` 非空，`strtonum` 和 `strtonumx` 将在 `*errstr` 中存储指示失败的错误字符串。

对于 `strtonumx`，`base` 值的解释方式与 strtoll(3) 中所述相同。特别是，若 `base` 值为 0，则 `nptr` 的预期形式为十进制常量、八进制常量或十六进制常量，其中任何一个都可前缀 `+` 或 `-` 符号。

## 返回值

`strtonum` 和 `strtonumx` 函数返回转换结果，除非该值超出提供的边界或无效。发生错误时返回 0，设置 `errno`，且 `errstr` 将指向错误消息。成功时 `*errstr` 将被设置为 `NULL`；可利用这一事实区分成功的 0 返回与错误。

## 实例

正确使用 `strtonum` 和 `strtonumx` 旨在比替代函数更简单。

```c
int iterations;
const char *errstr;
iterations = strtonum(optarg, 1, 64, &errstr);
if (errstr != NULL)
	errx(1, "number of iterations is %s: %s", errstr, optarg);
```

上例将保证 iterations 的值在 1 到 64 之间（含边界）。

## 错误

**[`ERANGE`]** 给定的字符串超出范围。

**[`EINVAL`]** 给定的字符串并非完全由数字字符（`strtonum`）或给定进制中的有效字符（`strtonumx`）组成。

**[`EINVAL`]** 提供的 `minval` 大于 `maxval`。

若发生错误，`errstr` 将被设置为以下字符串之一：

**`"too large"`** 结果大于提供的最大值。

**`"too small"`** 结果小于提供的最小值。

**`"invalid"`** 字符串并非完全由指定进制（或 `strtonum` 的十进制）中的有效字符组成。

**`"unparsable; invalid base specified"`** 指定的进制超出允许范围。

## 参见

[atof(3)](atof.3.md), [atoi(3)](atoi.3.md), [atol(3)](atol.3.md), atoll(3), sscanf(3), [strtod(3)](strtod.3.md), [strtol(3)](strtol.3.md), [strtoul(3)](strtoul.3.md)

## 标准

`strtonum` 函数是 BSD 扩展。现有的替代方案（如 [atoi(3)](atoi.3.md) 和 [strtol(3)](strtol.3.md)）要么无法安全使用，要么难以安全使用。

## 历史

`strtonum` 函数首次出现于 OpenBSD 3.6。`strtonumx` 函数于 2023 年首次出现于 illumos。
