# sysarch(2)

`sysarch` — 依赖于体系结构的系统调用

## 名称

`sysarch`

## 库

Lb libc

## 概要

`#include <machine/sysarch.h>`

```c
int
sysarch(int number, void *args)
```

## 描述

`sysarch()` 系统调用执行由 `number` 指定的依赖于体系结构的功能，参数由 `args` 指针指定。`args` 参数是指向结构的指针，该结构定义了函数的实际参数。依赖于体系结构的功能的符号常量和参数结构可在以下头文件中找到：

`#include <machine/sysarch.h>`

`sysarch()` 系统调用不应由用户程序直接调用。相反，它们应使用依赖于体系结构的库来访问其功能。

## 返回值

有关其返回值的信息，请参见特定于体系结构的系统调用的手册页。

## 参见

[i386_get_ioperm(2)](i386_get_ioperm.2.md), [i386_get_ldt(2)](i386_get_ldt.2.md), [i386_vm86(2)](i386_vm86.2.md)

## 历史

本手册页取自 NetBSD。
