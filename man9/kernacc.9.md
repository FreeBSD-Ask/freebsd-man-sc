# kernacc(9)

`kernacc` — 检查内存区域的可访问性

## 名称

`kernacc`, `useracc`

## 概要

```c
#include <sys/param.h>
#include <sys/proc.h>
#include <vm/vm.h>
#include <vm/vm_extern.h>

int
kernacc(void *addr, int len, int rw)

int
useracc(void *addr, int len, int rw)
```

## 描述

`kernacc` 和 `useracc` 函数检查由 `addr` 和 `len` 给定的虚拟地址范围内是否允许执行 `rw` 中指定类型的操作。`rw` 的可能值为 `VM_PROT_READ`、`VM_PROT_WRITE` 和 `VM_PROT_EXECUTE` 的任意按位组合。`kernacc` 检查内核地址空间中的地址，而 `useracc` 将 `addr` 视为用户空间地址。用于此操作的进程上下文取自全局变量 `curproc`。

## 返回值

如果允许 `rw` 指定的访问类型，两个函数都返回布尔值 true。否则返回布尔值 false。

## 缺陷

进程指针应作为参数传递给 `useracc`。
