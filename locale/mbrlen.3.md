# mbrlen(3)

`mbrlen` — 获取字符的字节数（可重启）

## 名称

`mbrlen`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft size_t Fn mbrlen const char * restrict s size_t n mbstate_t * restrict ps`

## 描述

`mbrlen` 函数检查 `s` 所指向的最多 `n` 个字节，以确定完成下一个多字节字符所需的字节数。

`mbstate_t` 参数 `ps` 用于跟踪移位状态。若为 `NULL`，`mbrlen` 使用一个内部的静态 `mbstate_t` 对象，该对象在程序启动时初始化为初始转换状态。

它等价于：

```c
mbrtowc(NULL, s, n, ps);
```

区别在于当 `ps` 为 `NULL` 指针时，`mbrlen` 使用自身的静态内部 `mbstate_t` 对象来跟踪移位状态。

## 返回值

`mbrlen` 函数返回：

**0** 接下来的 `n` 个或更少字节表示空的宽字符（`L'e0'`）。

**>0** 接下来的 `n` 个或更少字节表示一个有效字符，`mbrlen` 返回完成该多字节字符所使用的字节数。

**(`size_t`** )-2 接下来的 `n` 个字节构成但未完成一个有效的多字节字符序列，且所有 `n` 个字节都已被处理。

**(`size_t`** )-1 发生编码错误。接下来的 `n` 个或更少字节不构成有效的多字节字符。

## 实例

一个计算多字节字符串中字符数量的函数：

```c
size_t
nchars(const char *s)
{
	size_t charlen, chars;
	mbstate_t mbs;
	chars = 0;
	memset(&mbs, 0, sizeof(mbs));
	while ((charlen = mbrlen(s, MB_CUR_MAX, &mbs)) != 0 &&
	    charlen != (size_t)-1 && charlen != (size_t)-2) {
		s += charlen;
		chars++;
	}
	return (chars);
}
```

## 错误

`mbrlen` 函数在以下情况下会失败：

**[Er** EILSEQ] 检测到无效的多字节序列。

**[Er** EINVAL] 转换状态无效。

## 参见

[mblen(3)](mblen.3.md), [mbrtowc(3)](mbrtowc.3.md), [multibyte(3)](multibyte.3.md)

## 标准

`mbrlen` 函数遵循 ISO/IEC 9899:1999 ("ISO C99")。
