# strcat(3)

`strcat` — 连接字符串

## 名称

`strcat`, `strncat`

## 库

Lb libc

## 概要

`#include <string.h>`

`Ft char * Fn strcat char * restrict s const char * restrict append Ft char * Fn strncat char * restrict s const char * restrict append size_t count`

## 描述

`strcat` 和 `strncat` 函数将以 NUL 结尾的字符串 `append` 的副本追加到以 NUL 结尾的字符串 `s` 的末尾，然后添加结尾的 **`\0`**。字符串 `s` 必须有足够的空间来容纳结果。若 `s` 和 `append` 重叠，结果未定义。

`strncat` 函数从 `append` 中追加不超过 `count` 个字符，然后添加结尾的 **`\0`**。若 `s` 和 `append` 重叠，结果未定义。

## 返回值

`strcat` 和 `strncat` 函数返回指针 `s`。

## 参见

[bcopy(3)](bcopy.3.md), [memccpy(3)](memccpy.3.md), [memcpy(3)](memcpy.3.md), [memmove(3)](memmove.3.md), [strcpy(3)](strcpy.3.md), strlcat(3), [strlcpy(3)](strlcpy.3.md), wcscat(3)

## 标准

`strcat` 和 `strncat` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。

## 历史

`strcat` 函数首次出现于 Programmer's Workbench (PWB/UNIX)，并移植到 Version 7 AT&T UNIX；`strncat` 首次出现于 Version 7 AT&T UNIX。

## 安全注意事项

`strcat` 函数容易被误用，使得恶意用户能够通过缓冲区溢出攻击任意改变正在运行的程序的功能。

避免使用 `strcat`。应改用 `strncat` 或 `strlcat`，并确保复制到目标缓冲区的字符数不超过其容量。

注意，`strncat` 也可能存在问题。字符串被截断本身可能就是安全隐患。由于截断后的字符串不如原始字符串长，它可能指向完全不同的资源，使用截断后的资源可能导致非常不正确的行为。示例：

```c
void
foo(const char *arbitrary_string)
{
	char onstack[8];
#if defined(BAD)
	/*
	 * 第一个 strcat 是错误用法。不要使用 strcat！
	 */
	(void)strcat(onstack, arbitrary_string);	/* 错误！ */
#elif defined(BETTER)
	/*
	 * 以下两行演示了 strncat() 的更好用法。
	 */
	(void)strncat(onstack, arbitrary_string,
	    sizeof(onstack) - strlen(onstack) - 1);
#elif defined(BEST)
	/*
	 * 由于检测了截断情况，这些代码更加健壮。
	 */
	if (strlen(arbitrary_string) + 1 >
	    sizeof(onstack) - strlen(onstack))
		err(1, "onstack would be truncated");
	(void)strncat(onstack, arbitrary_string,
	    sizeof(onstack) - strlen(onstack) - 1);
#endif
}
```
