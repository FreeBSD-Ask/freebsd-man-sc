# strsep(3)

`strsep` — 分割字符串

## 名称

`strsep`

## 库

Lb libc

## 概要

`#include <string.h>`

```c
char *
strsep(char **stringp, const char *delim);
```

## 描述

`strsep` 函数在 `*stringp` 所引用的字符串中，定位字符串 `delim` 中任意字符（或结尾的 **`\0`** 字符）首次出现的位置，并将其替换为 **`\0`**。分隔字符之后的下一个字符的位置（若到达字符串末尾则为 `NULL`）存储到 `*stringp` 中。返回 `*stringp` 的原始值。

可以通过比较返回指针所引用位置与 **`\0`** 来检测“空”字段（即字符串 `delim` 中的字符作为 `*stringp` 的第一个字符出现的情况）。

若 `*stringp` 初始为 `NULL`，`strsep` 返回 `NULL`。

## 实例

以下示例使用 `strsep` 解析字符串，并将每个 token 输出到单独的行：

```c
char *token, *string, *tofree;

tofree = string = strdup("abc,def,ghi");
if (string == NULL)
	err(1, "strdup");
while ((token = strsep(&string, ",")) != NULL)
	printf("%s\n", token);

free(tofree);
```

以下示例使用 `strsep` 将包含以空白字符分隔的 token 的字符串解析为参数向量：

```c
char **ap, *argv[10], *inputstring;

for (ap = argv; (*ap = strsep(&inputstring, " \t")) != NULL;)
	if (**ap != '\0')
		if (++ap >= &argv[10])
			break;
```

## 参见

[memchr(3)](memchr.3.md), [strchr(3)](strchr.3.md), strcspn(3), [strpbrk(3)](strpbrk.3.md), strrchr(3), [strspn(3)](strspn.3.md), [strstr(3)](strstr.3.md), [strtok(3)](strtok.3.md)

## 历史

`strsep` 函数旨在替代 `strtok` 函数。虽然出于可移植性考虑应优先使用 `strtok` 函数（它遵循 ISO/IEC 9899:1990 ("ISO C89")），但它无法处理空字段，即无法检测由两个相邻分隔字符界定的字段，也无法同时对多个字符串进行操作。`strsep` 函数首次出现于 4.4BSD。
