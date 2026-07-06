# wmemchr.3

`wmemchr` — 宽字符串操作

## 名称

`wmemchr`, `wmemcmp`, `wmemcpy`, `wmemmove`, `wmempcpy`, `wmemset`, `wcpcpy`, `wcpncpy`, `wcscasecmp`, `wcscat`, `wcschr`, `wcscmp`, `wcscpy`, `wcscspn`, `wcsdup`, `wcslcat`, `wcslcpy`, `wcslen`, `wcsncasecmp`, `wcsncat`, `wcsncmp`, `wcsncpy`, `wcsnlen`, `wcspbrk`, `wcsrchr`, `wcsspn`, `wcsstr`

## 库

Lb libc

## 概要

`#include <wchar.h>`

`Ft wchar_t * Fn wmemchr const wchar_t *s wchar_t c size_t n Ft int Fn wmemcmp const wchar_t *s1 const wchar_t *s2 size_t n Ft wchar_t * Fn wmemcpy wchar_t * restrict s1 const wchar_t * restrict s2 size_t n Ft wchar_t * Fn wmemmove wchar_t *s1 const wchar_t *s2 size_t n Ft wchar_t * Fn wmempcpy wchar_t * restrict s1 const wchar_t * restrict s2 size_t n Ft wchar_t * Fn wmemset wchar_t *s wchar_t c size_t n Ft wchar_t * Fn wcpcpy wchar_t * restrict s1 const wchar_t * restrict s2 Ft wchar_t * Fn wcpncpy wchar_t * restrict s1 const wchar_t * restrict s2 size_t n Ft int Fn wcscasecmp const wchar_t *s1 const wchar_t *s2 Ft wchar_t * Fn wcscat wchar_t * restrict s1 const wchar_t * restrict s2 Ft wchar_t * Fn wcschr const wchar_t *s wchar_t c Ft int Fn wcscmp const wchar_t *s1 const wchar_t *s2 Ft wchar_t * Fn wcscpy wchar_t * restrict s1 const wchar_t * restrict s2 Ft size_t Fn wcscspn const wchar_t *s1 const wchar_t *s2 Ft wchar_t * Fn wcsdup const wchar_t *s Ft size_t Fn wcslcat wchar_t *s1 const wchar_t *s2 size_t n Ft size_t Fn wcslcpy wchar_t *s1 const wchar_t *s2 size_t n Ft size_t Fn wcslen const wchar_t *s Ft int Fn wcsncasecmp const wchar_t *s1 const wchar_t *s2 size_t n Ft wchar_t * Fn wcsncat wchar_t * restrict s1 const wchar_t * restrict s2 size_t n Ft int Fn wcsncmp const wchar_t *s1 const wchar_t * s2 size_t n Ft wchar_t * Fn wcsncpy wchar_t * restrict s1 const wchar_t * restrict s2 size_t n Ft size_t Fn wcsnlen const wchar_t *s size_t maxlen Ft wchar_t * Fn wcspbrk const wchar_t *s1 const wchar_t *s2 Ft wchar_t * Fn wcsrchr const wchar_t *s wchar_t c Ft size_t Fn wcsspn const wchar_t *s1 const wchar_t *s2 Ft wchar_t * Fn wcsstr const wchar_t * restrict s1 const wchar_t * restrict s2`

## 描述

这些函数实现对宽字符串的字符串操作。详细描述请参阅相应的单字节对应函数的文档，例如 [memchr(3)](memchr.3.md)。

## 参见

[memchr(3)](memchr.3.md), [memcmp(3)](memcmp.3.md), [memcpy(3)](memcpy.3.md), [memmove(3)](memmove.3.md), [memset(3)](memset.3.md), stpcpy(3), stpncpy(3), [strcasecmp(3)](strcasecmp.3.md), [strcat(3)](strcat.3.md), [strchr(3)](strchr.3.md), [strcmp(3)](strcmp.3.md), [strcpy(3)](strcpy.3.md), strcspn(3), [strdup(3)](strdup.3.md), strlcat(3), [strlcpy(3)](strlcpy.3.md), [strlen(3)](strlen.3.md), strncat(3), strncmp(3), strncpy(3), strnlen(3), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md)

## 标准

这些函数遵循 ISO/IEC 9899:1999 ("ISO C99")，但 `wcpcpy`、`wcpncpy`、`wcscasecmp`、`wcsdup`、`wcsncasecmp` 和 `wcsnlen` 遵循 IEEE Std 1003.1-2008 ("POSIX.1")，而 `wcslcat`、`wcslcpy` 和 `wmempcpy` 为扩展。
