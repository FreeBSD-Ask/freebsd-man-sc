# syscall(2)

`syscall` — 间接系统调用

## 名称

`syscall`, `__syscall`

## 库

Lb libc

## 概要

`#include <sys/syscall.h>`

`#include <unistd.h>`

```c
int
syscall(int number, ...);

off_t
__syscall(quad_t number, ...);
```

## 描述

`syscall()` 函数执行汇编语言接口具有指定 `number` 且带指定参数的系统调用。系统调用的符号常量可在头文件 `<sys/syscall.h>` 中找到。

当一个或多个参数是 64 位参数时，应使用 `__syscall()` 形式以确保参数对齐正确。此系统调用对于测试在 C 库中没有对应条目的新系统调用很有用。

## 返回值

返回值由所调用的系统调用定义。通常，返回值 0 表示成功。返回值 -1 表示出错，错误码存储在 `errno` 中。

## 历史

`syscall()` 函数出现于 4.0BSD。

## 缺陷

无法模拟具有多个返回值的系统调用，例如 [pipe(2)](pipe.2.md)。