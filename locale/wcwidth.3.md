# wcwidth(3)

`wcwidth` — 宽字符码的列位置数

## 名称

`wcwidth`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft int Fn wcwidth wchar_t wc`

## 描述

`wcwidth` 函数确定显示宽字符 `wc` 所需的列位置数。

## 返回值

`wcwidth` 函数在 `wc` 参数为空宽字符（`L'\0'`）时返回 0，若 `wc` 不可打印则返回 -1，否则返回该字符占据的列位置数。

## 实例

此代码片段从标准输入读取文本，并将超过 20 列位置宽的行断开，类似于 fold(1) 工具：

```c
wint_t ch;
int column, w;
column = 0;
while ((ch = getwchar()) != WEOF) {
	w = wcwidth(ch);
	if (w > 0 && column + w >= 20) {
		putwchar(L'\n');
		column = 0;
	}
	putwchar(ch);
	if (ch == L'\n')
		column = 0;
	else if (w > 0)
		column += w;
}
```

## 参见

iswprint(3), [wcswidth(3)](../string/wcswidth.3.md)

## 标准

`wcwidth` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。
