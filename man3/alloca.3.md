# alloca.3

`alloca` — 内存分配器

## 名称

`alloca`

## 概要

`#include <stdlib.h>`

```c
void *alloca(size_t size);
```

## 描述

`alloca` 函数或宏在调用者的栈帧中分配 `size` 字节的空间。此临时空间在返回时自动释放。

## 返回值

`alloca` 返回指向所分配空间起始位置的指针。

## 参见

brk(2), calloc(3), getpagesize(3), malloc(3), realloc(3)

## 历史

`alloca` 出现于 Version 32V AT&T UNIX。

## 缺陷

`alloca` 依赖于机器和编译器；不鼓励使用。

`alloca` 略有不安全，因为它无法保证返回的指针指向有效且可用的内存块。所作分配可能超出栈的边界，甚至进一步侵入内存中的其他对象，而 `alloca` 无法检测此类错误。避免在大型无界分配中使用 `alloca`。

在同一函数中同时使用 C99 变长数组与 `alloca` 会导致 `alloca` 存储的生命周期被限制在包含 `alloca` 的代码块内。例如，在以下片段中，`p` 的生命周期不会延伸到该代码块之外，而如果未定义 `vla` 或将其定义为定长数组，则本应延伸至代码块之外：

```c
char *p;
{
	const int n = 100;
	int vla[n];
	p = alloca(32);
	strcpy(p, "Hello, world!");
	printf("Inside: %s\n", p); /* 有效。 */
}
printf("Outside: %s\n", p); /* 未定义。 */
```
