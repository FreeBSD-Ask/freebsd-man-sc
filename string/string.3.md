# string(3)

`string` — 字符串相关函数

## 名称

`stpcpy`, `strcat`, `strncat`, `strchr`, `strrchr`, `strcmp`, `strncmp`, `strcasecmp`, `strncasecmp`, `strcpy`, `strncpy`, `strerror`, `strlen`, `strpbrk`, `strsep`, `strspn`, `strcspn`, `strstr`, `strtok`, `index`, `rindex`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft char * Fn stpcpy char *dst const char *src Ft char * Fn strcat char *s const char * append Ft char * Fn strncat char *s const char *append size_t count Ft char * Fn strchr const char *s int c Ft char * Fn strrchr const char *s int c Ft int Fn strcmp const char *s1 const char *s2 Ft int Fn strncmp const char *s1 const char *s2 size_t count Ft int Fn strcasecmp const char *s1 const char *s2 Ft int Fn strncasecmp const char *s1 const char *s2 size_t count Ft char * Fn strcpy char *dst const char *src Ft char * Fn strncpy char *dst const char *src size_t count Ft char * Fn strerror int errno Ft size_t Fn strlen const char *s Ft char * Fn strpbrk const char *s const char *charset Ft char * Fn strsep char **stringp const char *delim Ft size_t Fn strspn const char *s const char *charset Ft size_t Fn strcspn const char *s const char *charset Ft char * Fn strstr const char *big const char *little Ft char * Fn strtok char *s const char *delim Ft char * Fn index const char *s int c Ft char * Fn rindex const char *s int c`

## 描述

字符串函数用于操作以空字节结尾的字符串。

更多信息参见各自的手册页面。若要操作变长通用对象（作为字节字符串，不检查空字节），参见 [bstring(3)](bstring.3.md)。

除各自手册页面中特别说明外，字符串函数不会对目标缓冲区进行大小限制检查。

## 参见

[bstring(3)](bstring.3.md), [index(3)](index.3.md), rindex(3), stpcpy(3), [strcasecmp(3)](strcasecmp.3.md), [strcat(3)](strcat.3.md), [strchr(3)](strchr.3.md), [strcmp(3)](strcmp.3.md), [strcpy(3)](strcpy.3.md), strcspn(3), [strerror(3)](strerror.3.md), [strlen(3)](strlen.3.md), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strsep(3)](strsep.3.md), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md), [strtok(3)](strtok.3.md), [simd(7)](../man7/simd.7.md)

## 标准

`strcat`、`strncat`、`strchr`、`strrchr`、`strcmp`、`strncmp`、`strcpy`、`strncpy`、`strerror`、`strlen`、`strpbrk`、`strspn`、`strcspn`、`strstr` 和 `strtok` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。
