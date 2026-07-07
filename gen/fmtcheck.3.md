# fmtcheck(3)

`fmtcheck` — 净化用户提供的 [printf(3)](../stdio/printf.3.md) 风格格式字符串

## 名称

`fmtcheck`

## 库

Lb libc

## 概要

`#include <stdio.h>`

```c
const char *
fmtcheck(const char *fmt_suspect, const char *fmt_default);
```

## 描述

`fmtcheck()` 函数扫描 `fmt_suspect` 和 `fmt_default`，以确定 `fmt_suspect` 是否会消耗与 `fmt_default` 相同的参数类型，并确保 `fmt_suspect` 是有效的格式字符串。

[printf(3)](../stdio/printf.3.md) 函数族无法在运行时验证所传递参数的类型。在某些情况下（如 catgets(3)），使用用户提供的格式字符串是有用或必要的，但无法保证该格式字符串与指定的参数匹配。

`fmtcheck()` 函数正是为这些情况而设计的，例如：

```c
printf(fmtcheck(user_format, standard_format), arg1, arg2);
```

在检查过程中，字段宽度、填充符、精度等会被忽略（除非字段宽度或精度是星号 `*` 而非数字字符串）。此外，除格式说明符之外的任何文本都将被完全忽略。

## 返回值

如果 `fmt_suspect` 是有效的格式且消耗与 `fmt_default` 相同的参数类型，则 `fmtcheck()` 返回 `fmt_suspect`。否则，返回 `fmt_default`。

## 参见

[printf(3)](../stdio/printf.3.md)

## 缺陷

`fmtcheck()` 函数无法识别位置参数。

## 安全注意事项

注意，只要格式接受相同的参数，它们可以截然不同。例如，“`%p %o %30s %#llx %-10.*e %n`”与“`This number %lu %d%% and string %s has %qd numbers and %.*g floats (%n)`”是兼容的。但是，“`%o`”不等价于“`%lx`”，因为前者需要整数而后者需要 long 类型。
