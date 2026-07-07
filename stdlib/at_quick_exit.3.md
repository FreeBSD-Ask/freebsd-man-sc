# at_quick_exit.3

`at_quick_exit` — 注册在快速退出时运行的清理函数

## 名称

`at_quick_exit`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
int
at_quick_exit(void (*func)(void));
```

## 描述

`at_quick_exit` 函数注册一个清理函数，该函数在程序因调用 [quick_exit(3)](quick_exit.3.md) 而退出时被调用。清理函数按相反顺序调用；若程序通过调用 [exit(3)](exit.3.md)、_Exit(3) 或 [abort(3)](abort.3.md) 退出，则不会调用这些清理函数。

## 返回值

`at_quick_exit` 函数成功时返回 0，失败时返回非零值。

## 参见

[exit(3)](exit.3.md), [quick_exit(3)](quick_exit.3.md)

## 标准

`at_quick_exit` 函数遵循 ISO/IEC 9899:2011 ("ISO C11")。
