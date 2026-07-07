# stpcpy(3)

`stpcpy` — 复制字符串

## 名称

`stpcpy`, `stpncpy`, `strcpy`, `strncpy`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft char * Fn stpcpy char * restrict dst const char * restrict src Ft char * Fn stpncpy char * restrict dst const char * restrict src size_t len Ft char * Fn strcpy char * restrict dst const char * restrict src Ft char * Fn strncpy char * restrict dst const char * restrict src size_t len`

## 描述

`strcpy` 和 `stpcpy` 函数将字符串 `src` 复制到 `dst`（包括终止的 **`\0`** 字符）。

`strncpy` 和 `stpncpy` 函数从 `src` 复制至多 `len` 个字符到 `dst`。若 `src` 的长度小于 `len` 个字符，`dst` 的剩余部分以 **`\0`** 字符填充。否则，`dst` *不会*被终止。

对于 `strcpy`、`strncpy`、`stpcpy` 和 `stpncpy`，若 `src` 和 `dst` 重叠，结果未定义。

## 返回值

`strcpy` 和 `strncpy` 函数返回 `dst`。`stpcpy` 和 `stpncpy` 函数返回指向 `dst` 终止 **`\0`** 字符的指针。若 `stpncpy` 未以 `NUL` 字符终止 `dst`，则返回指向 `dst[n]` 的指针（该指针不一定指向有效的内存位置）。

## 实例

以下将 `chararray` 设置为 “`abc\0\0\0`”：

```c
char chararray[6];
(void)strncpy(chararray, "abc", sizeof(chararray));
```

以下将 `chararray` 设置为 “`abcdef`”：

```c
char chararray[6];
(void)strncpy(chararray, "abcdefgh", sizeof(chararray));
```

注意，它*不会*以 NUL 终止 `chararray`，因为源字符串的长度大于或等于长度参数。

以下将 `input` 中尽可能多的字符复制到 `buf`，并以 NUL 终止结果。由于 `strncpy` *不*保证以 NUL 终止字符串本身，必须显式完成此操作。

```c
char buf[1024];
(void)strncpy(buf, input, sizeof(buf) - 1);
buf[sizeof(buf) - 1] = '\0';
```

使用 [strlcpy(3)](strlcpy.3.md) 可以更好地实现此目的，如下例所示：

```c
(void)strlcpy(buf, input, sizeof(buf));
```

## 参见

[bcopy(3)](bcopy.3.md), [memccpy(3)](memccpy.3.md), [memcpy(3)](memcpy.3.md), [memmove(3)](memmove.3.md), [strlcpy(3)](strlcpy.3.md), wcscpy(3)

## 标准

`strcpy` 和 `strncpy` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。`stpcpy` 和 `stpncpy` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1")。

## 历史

`stpcpy` 函数首次出现于 FreeBSD 4.4，`stpncpy` 在 FreeBSD 8.0 中添加。

## 安全注意事项

本手册页中记录的所有函数都很容易被误用，使得恶意用户能够通过缓冲区溢出攻击任意更改运行中程序的功能。

在几乎所有情况下，强烈建议使用 `strlcpy` 函数。

对于某些（但并非全部）固定长度记录，未终止的字符串可能既有效又合乎需要。在这种特定情况下，`strncpy` 函数可能是最合适的。
