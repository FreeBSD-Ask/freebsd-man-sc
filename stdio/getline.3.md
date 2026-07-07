# getline(3)

`getdelim` — 从流中获取一行

## 名称

`getdelim`, `getline`

## 库

Lb libc

## 概要

`#include <stdio.h>`

`Ft ssize_t Fn getdelim char ** restrict linep size_t * restrict linecapp int delimiter FILE * restrict stream Ft ssize_t Fn getline char ** restrict linep size_t * restrict linecapp FILE * restrict stream`

## 描述

`getdelim` 函数从 `stream` 中读取一行，以字符 `delimiter` 作为分隔符。`getline` 函数等价于以换行符作为分隔符的 `getdelim`。除非到达文件末尾，否则分隔符会包含在行中。

调用者可以在 `*linep` 中提供指向由 `malloc` 分配的缓冲区的指针，在 `*linecapp` 中提供该缓冲区的容量。这些函数会根据需要扩展缓冲区，如同通过 `realloc` 进行。如果 `linep` 指向 `NULL` 指针，将分配新的缓冲区。无论哪种情况，`*linep` 和 `*linecapp` 都会相应更新。

## 返回值

`getdelim` 和 `getline` 函数返回存储在缓冲区中的字符数，不包括终止 `NUL` 字符。如果发生错误或到达文件末尾，返回 -1。

## 实例

以下代码片段从文件中读取行并将其写入标准输出。使用 `fwrite` 函数是因为行中可能包含嵌入的 `NUL` 字符。

```c
char *line = NULL;
size_t linecap = 0;
ssize_t linelen;
while ((linelen = getline(&line, &linecap, fp)) > 0)
	fwrite(line, linelen, 1, stdout);
free(line);
```

## 错误

这些函数在以下情况下可能失败：

**`EINVAL`** `linep` 或 `linecapp` 为 `NULL`。

**`EOVERFLOW`** 在前 `SSIZE_MAX` 个字符中未找到分隔符。

这些函数也可能由于 `fgets` 和 `malloc` 所指定的任何错误而失败。

## 参见

[fgetln(3)](fgetln.3.md), [fgets(3)](fgets.3.md), malloc(3)

## 标准

`getdelim` 和 `getline` 函数遵循 IEEE Std 1003.1-2008 ("POSIX.1") 标准。

## 历史

这些例程首次出现于 FreeBSD 8.0。

## 缺陷

`getdelim` 和 `getline` 没有宽字符版本。
