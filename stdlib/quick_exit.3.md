# quick\_exit.3

`quick_exit` — 快速退出程序，执行最少的清理

## 名称

`quick_exit`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
_Noreturn void
quick_exit(int status);
```

## 描述

`quick_exit` 函数快速退出程序，调用通过 [at_quick_exit(3)](at_quick_exit.3.md) 注册的任何清理函数，但不调用任何 C++ 析构函数或通过 [atexit(3)](atexit.3.md) 注册的清理代码。[stdio(3)](../stdio/stdio.3.md) 文件缓冲区不会被刷新。

当通过 [at_quick_exit(3)](at_quick_exit.3.md) 注册的函数是 *async-signal safe*（异步信号安全）时，`quick_exit` 函数也是 *async-signal safe* 的。

## 返回值

`quick_exit` 函数不返回。

## 参见

[at_quick_exit(3)](at_quick_exit.3.md), [exit(3)](exit.3.md)

## 标准

`quick_exit` 函数遵循 ISO/IEC 9899:2011 ("ISO C11")。
