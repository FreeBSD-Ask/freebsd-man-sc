# set_constraint_handler_s.3

`set_constraint_handler_s` — 运行时约束违规处理

## 名称

`set_constraint_handler_s`, `abort_handler_s`, `ignore_handler_s`

## 库

Lb libc

## 概要

`#define __STDC_WANT_LIB_EXT1__ 1`

`#include <stdlib.h>`

```c
constraint_handler_t
set_constraint_handler_s(constraint_handler_t handler);
```

### 处理程序原型

```c
typedef void
(*constraint_handler_t)(const char * restrict msg, void * restrict ptr,
    errno_t error);
```

### 预定义处理程序

```c
void
abort_handler_s(const char * restrict msg, void * restrict ptr,
    errno_t error);

void
ignore_handler_s(const char * restrict msg, void * restrict ptr,
    errno_t error);
```

## 描述

`set_constraint_handler_s` 函数将运行时约束违规处理程序设置为 `handler`。

运行时约束处理程序是当库函数检测到运行时约束违规时调用的回调函数。

参数如下：

**`msg`** 指向描述运行时约束违规的字符串的指针。

**`ptr`** `NULL` 指针。

**`error`** 若调用处理程序的函数的返回类型声明为 `errno_t`，则传递该函数的返回值。否则，传递一个 `errno_t` 类型的正值。

当发生运行时约束违规时，仅调用通过 `set_constraint_handler_s` 最近注册的处理程序。

若从未调用过 `set_constraint_handler_s` 函数，实现将使用默认的约束处理程序。若 `set_constraint_handler_s` 的 `handler` 参数为 `NULL` 指针，则默认处理程序成为当前约束处理程序。

`abort_handler_s` 和 `ignore_handler_s` 是 C 库提供的标准定义的运行时约束处理程序。

`abort_handler_s` 函数将包含 `msg` 的错误消息写入 `stderr`，并调用 [abort(3)](abort.3.md) 函数。`abort_handler_s` 当前是默认的运行时约束处理程序。

`ignore_handler_s` 只是返回其调用者。

## 返回值

`set_constraint_handler_s` 函数返回指向先前注册的处理程序的指针，若先前未注册任何处理程序则返回 `NULL`。

`abort_handler_s` 函数不返回其调用者。

`ignore_handler_s` 函数不返回值。

## 标准

`set_constraint_handler_s` 函数遵循 ISO/IEC 9899:2011 ("ISO C11") K.3.6.1.1。

## 作者

本手册页面由 Yuri Pankov <yuripv@yuripv.net> 编写。
