# strlcpy(3)

`strlcpy` — 带大小限制的字符串复制与连接

## 名称

`strlcpy`, `strlcat`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
size_t
strlcpy(char * restrict dst, const char * restrict src, size_t dstsize);

size_t
strlcat(char * restrict dst, const char * restrict src, size_t dstsize);
```

## 描述

`strlcpy` 和 `strlcat` 函数复制和连接字符串，其输入参数和输出结果与 [strcpy(3)](strcpy.3.md) 和 [strcat(3)](strcat.3.md) 相同，但提供适当的溢出保护。它们旨在作为 strncpy(3) 和 strncat(3) 的更安全、更一致、更不易出错的替代品，后两者容易被误用。

`strlcpy` 和 `strlcat` 接受目标缓冲区的完整大小，并在有空间时保证以 NUL 结尾。注意，`dstsize` 中应包含 NUL 字符的空间。

`strlcpy` 从字符串 `src` 复制至多 `dstsize` - 1 个字符到 `dst`，若 `dstsize` 不为 0 则以 NUL 结尾。

`strlcat` 将字符串 `src` 追加到 `dst` 的末尾。它最多追加 `dstsize` - strlen(dst) - 1 个字符。然后以 NUL 结尾，除非 `dstsize` 为 0 或原始 `dst` 字符串的长度大于 `dstsize`（实际上这不应发生，因为这意味着 `dstsize` 不正确或 `dst` 不是有效的字符串）。

若 `src` 和 `dst` 字符串重叠，行为未定义。

## 返回值

`strlcpy` 和 `strlcat` 函数返回其尝试创建的字符串的总长度。对于 `strlcpy`，即 `src` 的长度。对于 `strlcat`，即 `dst` 的初始长度加上 `src` 的长度。

若返回值 `>=` `dstsize`，则输出字符串已被截断。调用者有责任处理此情况。

## 实例

以下代码片段展示了简单情况：

```c
char *s, *p, buf[BUFSIZ];

...

(void)strlcpy(buf, s, sizeof(buf));
(void)strlcat(buf, p, sizeof(buf));
```

为检测截断（例如在构建路径名时），可以使用类似以下的代码：

```c
char *dir, *file, pname[MAXPATHLEN];

...

if (strlcpy(pname, dir, sizeof(pname)) >= sizeof(pname))
	goto toolong;
if (strlcat(pname, file, sizeof(pname)) >= sizeof(pname))
	goto toolong;
```

由于已知第一次复制了多少字符，可以通过使用复制而非追加来稍微加快速度：

```c
char *dir, *file, pname[MAXPATHLEN];
size_t n;

...

n = strlcpy(pname, dir, sizeof(pname));
if (n >= sizeof(pname))
	goto toolong;
if (strlcpy(pname + n, file, sizeof(pname) - n) >= sizeof(pname) - n)
	goto toolong;
```

然而，这种优化的有效性值得质疑，因为它违背了 `strlcpy` 和 `strlcat` 的初衷。事实上，本手册页的第一版就写错了。

## 参见

snprintf(3), strncat(3), strncpy(3), wcslcpy(3)

> Todd C. Miller, Theo de Raadt, "strlcpy and strlcat -- Consistent, Safe, String Copy and Concatenation", *Proceedings of the FREENIX Track: 1999 USENIX Annual Technical Conference*, USENIX Association, June 6-11, 1999.

## 历史

`strlcpy` 和 `strlcat` 函数首次出现于 OpenBSD 2.4 和 FreeBSD 3.3。
