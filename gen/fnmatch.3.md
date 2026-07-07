# fnmatch.3

`fnmatch` — 测试文件名或路径名是否匹配 shell 风格的模式

## 名称

`fnmatch`

## 库

Lb libc

## 概要

`#include <fnmatch.h>`

```c
int
fnmatch(const char *pattern, const char *string, int flags);
```

## 描述

`fnmatch()` 函数按照 shell 使用的规则匹配模式。它检查 `string` 参数指定的字符串，看其是否匹配 `pattern` 参数指定的模式。

`flags` 参数修改 `pattern` 和 `string` 的解释方式。`flags` 的值是以下常量中任意多个的按位或，这些常量定义在包含文件

`#include <fnmatch.h>`

中：

**`FNM_NOESCAPE`** 通常，`pattern` 中每次出现的反斜杠 `\` 后跟一个字符时，都会被替换为该字符。这是为了取消该字符的任何特殊含义。如果设置了 `FNM_NOESCAPE` 标志，反斜杠字符将被视为普通字符。

**`FNM_PATHNAME`** `string` 中的斜杠字符必须由 `pattern` 中的斜杠显式匹配。如果未设置此标志，则斜杠被视为普通字符。

**`FNM_PERIOD`** `string` 中的前导句点必须由 `pattern` 中的句点显式匹配。如果未设置此标志，则前导句点被视为普通字符。“前导”的定义与 `FNM_PATHNAME` 的设定有关。如果句点是 `string` 中的第一个字符，则它始终是“前导”的。此外，如果设置了 `FNM_PATHNAME`，当句点紧跟在斜杠之后时也是前导的。

**`FNM_LEADING_DIR`** 在 `pattern` 成功匹配后，忽略其后的 `/*` 部分。

**`FNM_CASEFOLD`** 在 `pattern` 和 `string` 中均忽略大小写区分。

## 返回值

如果 `string` 匹配 `pattern` 指定的模式，`fnmatch()` 函数返回零；否则返回 `FNM_NOMATCH`。

## 参见

[sh(1)](../man1/sh.1.md), [glob(3)](glob.3.md), [regex(3)](../man3/regex.3.md)

## 标准

`fnmatch()` 函数的当前实现预期符合 IEEE Std 1003.2 ("POSIX.2")。

## 历史

`fnmatch()` 的前身 `gmatch()` 最早出现在 Programmer's Workbench (PWB/UNIX) 中。`fnmatch()` 函数首次出现在 4.4BSD 中。

## 缺陷

模式 `*` 匹配空字符串，即使指定了 `FNM_PATHNAME` 也是如此。
