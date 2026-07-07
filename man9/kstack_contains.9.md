# kstack_contains(9)

`kstack_contains` — 确定地址范围是否位于线程的内核栈内

## 名称

`kstack_contains`

## 概要

```c
#include <machine/stack.h>

bool
kstack_contains(struct thread *td, vm_offset_t va, size_t len)
```

## 描述

此函数可用于确定给定地址范围是否落在 `td` 所指向线程的内核栈内。

## 返回值

`kstack_contains` 函数如果地址范围 [`va`..(`va`+`len`-1)]（两个地址均含）位于参数 `td` 所指向线程的内核栈内，则返回 `true`，否则返回 `false`。

## 错误

此函数不返回错误。

## 参见

[kproc(9)](kproc.9.md), [kthread(9)](kthread.9.md)
