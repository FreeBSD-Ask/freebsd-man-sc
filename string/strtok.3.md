# strtok(3)

`strtok` — 字符串 token

## 名称

`strtok`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft char * Fn strtok char *str const char *sep Ft char * Fn strtok_r char *str const char *sep char **last`

## 描述

**此接口由 [strsep(3)](strsep.3.md) 取代。**

`strtok` 函数用于从以 NUL 结尾的字符串 `str` 中分离出连续的 token。这些 token 在字符串中由 `sep` 中的至少一个字符分隔。首次调用 `strtok` 时应指定 `str`；后续希望从同一字符串中获取更多 token 时，应改为传递空指针。分隔字符串 `sep` 在每次调用时都必须提供，且可以在不同调用之间更改。

实现的行为如同没有库函数调用 `strtok`。

`strtok_r` 函数是 `strtok` 的可重入版本。每次调用都必须提供上下文指针 `last`。`strtok_r` 函数也可用于将两个解析循环相互嵌套，只要使用不同的上下文指针即可。

## 返回值

`strtok` 和 `strtok_r` 函数在将 token 本身替换为 `NUL` 字符后，返回指向字符串中每个后续 token 开头的指针。当没有更多 token 时，返回空指针。

## 实例

以下示例使用 `strtok_r` 在不同的上下文中解析两个字符串：

```c
char test[80], blah[80];
char *sep = "ee/:;=-";
char *word, *phrase, *brkt, *brkb;
strcpy(test, "This;is.a:test:of=the/stringeetokenizer-function.");
for (word = strtok_r(test, sep, &brkt);
     word;
     word = strtok_r(NULL, sep, &brkt))
{
    strcpy(blah, "blah:blat:blab:blag");
    for (phrase = strtok_r(blah, sep, &brkb);
         phrase;
         phrase = strtok_r(NULL, sep, &brkb))
    {
        printf("So far we're at %s:%s\n", word, phrase);
    }
}
```

## 参见

[memchr(3)](memchr.3.md), [strchr(3)](strchr.3.md), strcspn(3), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strsep(3)](strsep.3.md), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md), [wcstok(3)](wcstok.3.md)

## 标准

`strtok` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`strtok_r` 函数遵循 IEEE Std 1003.1-2001 ("POSIX.1")。

## 作者

Wes Peters <wes@softweyr.com>, Softweyr LLC

基于 FreeBSD 3.0 实现。

## 缺陷

System V 的 `strtok` 在接收到仅包含分隔字符的字符串时，不会修改下一次的起始位置，因此使用不同（或空）分隔字符串调用 `strtok` 可能返回非 `NULL` 值。而本实现总是会修改下一次的起始位置，这样的调用序列将始终返回 `NULL`。
