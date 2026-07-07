# stdarg(3)

`stdarg` — 可变参数列表

## 名称

`stdarg`

## 概要

```c
#include <stdarg.h>
```

```c
void
va_start(va_list ap, last);

type
va_arg(va_list ap, type);

void
va_copy(va_list dest, va_list src);

void
va_end(va_list ap);
```

## 描述

函数可以被调用时带有数量和类型可变的参数。头文件

```c
#include <stdarg.h>
```

声明了一个类型（*va_list*）并定义了四个宏，用于逐步遍历参数列表，这些参数的数量和类型对被调用函数是未知的。

被调用函数必须声明一个 *va_list* 类型的对象，该对象由 `va_start()`、`va_arg()`、`va_copy()` 和 `va_end()` 宏使用。

`va_start()` 宏初始化 `ap` 以供 `va_arg()`、`va_copy()` 和 `va_end()` 后续使用，必须首先调用。

参数 `last` 是可变参数列表之前的最后一个参数的名称，即调用函数知道其类型的最后一个参数。

因为此参数的地址在 `va_start()` 宏中使用，所以它不应声明为寄存器变量、函数或数组类型。

`va_arg()` 宏展开为表达式，其类型和值为调用中的下一个参数。参数 `ap` 是由 `va_start()` 或 `va_copy()` 初始化的 *va_list* `ap`。每次调用 `va_arg()` 都会修改 `ap`，以便下次调用返回下一个参数。参数 `type` 是一个类型名，指定后只需在 `type` 后加 * 即可获得指向具有该类型对象的指针类型。

如果没有下一个参数，或者 `type` 与实际下一个参数的类型不兼容（按默认参数提升规则提升后），将发生随机错误。

在 `va_start()` 之后首次使用 `va_arg()` 宏返回 `last` 之后的参数。后续调用返回剩余参数的值。

`va_copy()` 宏将先前由 `va_start()` 初始化的可变参数列表从 `src` 复制到 `dest`。状态被保留，等效于使用与 `src` 相同的第二个参数调用 `va_start()`，并调用 `va_arg()` 与 `src` 相同的次数。

`va_end()` 宏清理与可变参数列表 `ap` 关联的任何状态。

每次调用 `va_start()` 或 `va_copy()` 都必须在同一函数中与相应的 `va_end()` 调用配对。

## 返回值

`va_arg()` 宏返回下一个参数的值。

`va_start()`、`va_copy()` 和 `va_end()` 宏不返回值。

## 实例

函数 *foo* 接受一串格式字符，并根据类型打印出与每个格式字符关联的参数。

```c
void foo(char *fmt, ...)
{
	va_list ap;
	int d;
	char c, *s;
	va_start(ap, fmt);
	while (*fmt)
		switch(*fmt++) {
		case 's':			/* 字符串 */
			s = va_arg(ap, char *);
			printf("string %s\n", s);
			break;
		case 'd':			/* 整数 */
			d = va_arg(ap, int);
			printf("int %d\n", d);
			break;
		case 'c':			/* 字符 */
			/* 注意：char 被提升为 int。 */
			c = va_arg(ap, int);
			printf("char %c\n", c);
			break;
		}
	va_end(ap);
}
```

## 兼容性

这些宏与它们替换的历史宏*不*兼容。

## 标准

`va_start()`、`va_arg()`、`va_copy()` 和 `va_end()` 宏遵循 ISO/IEC 9899:1999 ("ISO C99") 标准。

## 历史

`va_start()`、`va_arg()` 和 `va_end()` 宏在 ANSI X3.159-1989 ("ANSI C89") 中引入。`va_copy()` 宏在 ISO/IEC 9899:1999 ("ISO C99") 中引入。

## 缺陷

与 *varargs* 宏不同，`stdarg` 宏不允许程序员编写没有固定参数的函数。此问题主要在将 *varargs* 代码转换为 `stdarg` 代码时产生工作，但也给希望将其所有参数传递给接受 *va_list* 参数的函数（如 vfprintf(3)）的可变参数函数带来困难。
