# wcstok(3)

`wcstok` — 将宽字符字符串分割为 token

## 名称

`wcstok`

## 库

Lb libc

## 概要

`#include <wchar.h>`

```c
wchar_t *
wcstok(wchar_t * restrict str, const wchar_t * restrict sep,
    wchar_t ** restrict last);
```

## 描述

`wcstok` 函数用于在以 NUL 结尾的宽字符字符串 `str` 中提取连续的 token。这些 token 在字符串中由 `sep` 中的至少一个字符分隔。首次调用 `wcstok` 时应指定 `str`；后续调用若要从同一字符串获取更多 token，应改为传递空指针。分隔字符串 `sep` 每次调用时都必须提供，且可在调用之间更改。上下文指针 `last` 每次调用时都必须提供。

`wcstok` 函数是 `strtok_r` 函数的宽字符版本。

## 返回值

`wcstok` 函数返回指向字符串中每个后续 token 开头的指针，此前会将 token 本身替换为空的宽字符（**`L'\0'`**）。当没有更多 token 时，返回空指针。

## 实例

以下代码片段以 ASCII 空格、制表符和换行符分割宽字符字符串，并将 token 写入标准输出：

```c
const wchar_t *seps = L" \t\n";
wchar_t *last, *tok, text[] = L" \none\ttwo\t\tthree  \n";

for (tok = wcstok(text, seps, &last); tok != NULL;
    tok = wcstok(NULL, seps, &last))
	wprintf(L"%ls\n", tok);
```

## 兼容性

`wcstok` 的一些早期实现省略了上下文指针参数 `last`，而是像 `strtok` 那样在静态变量中跨调用维护状态。

## 参见

[strtok(3)](strtok.3.md), wcschr(3), wcscspn(3), wcspbrk(3), wcsrchr(3), wcsspn(3)

## 标准

`wcstok` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
