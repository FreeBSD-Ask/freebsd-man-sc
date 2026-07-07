# atexit.3

`atexit` — 注册在程序退出时调用的函数

## 名称

`atexit`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
atexit(void (*function)(void));

int
atexit_b(void (^function)(void));
```

## 描述

`atexit` 函数注册给定的 `function`，使其在程序退出时被调用，无论退出是通过 [exit(3)](exit.3.md) 还是从程序的 `main` 函数返回。如此注册的函数按相反顺序调用；不传递任何参数。

这些函数不得调用 `exit`；若在此类函数中需要终止进程，应使用 [_exit(2)](../sys/_exit.2.md) 函数。（或者，该函数可通过调用 [abort(3)](abort.3.md) 等方式引发异常进程终止。）

至少总能注册 32 个函数，只要能分配到足够内存，允许注册更多。

`atexit_b` 函数的行为与 `atexit` 相同，区别在于它接受一个 block 而非函数指针。

## 返回值

成功完成时，`atexit` 函数返回 0。否则返回非零值，并设置全局变量 `errno` 以指示错误。

## 错误

**[`ENOMEM`]** 没有可用内存将函数添加到列表中。现有的函数列表不受影响。

**[`ENOSYS`]** `atexit_b` 函数被未提供 `_Block_copy` 实现的程序调用。

## 参见

[_exit(2)](../sys/_exit.2.md), [at_quick_exit(3)](at_quick_exit.3.md), [exit(3)](exit.3.md)

## 标准

`atexit` 函数遵循 ISO/IEC 9899:1990 ("ISO C89")。
