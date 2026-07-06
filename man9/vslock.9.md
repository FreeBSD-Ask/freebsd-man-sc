# vslock.9

`vslock`, `vsunlock` — 将用户空间地址锁定/解锁在内存中

## 名称

`vslock`, `vsunlock`

## 概要

```c
#include <sys/param.h>
#include <sys/proc.h>
#include <vm/vm.h>
#include <vm/vm_extern.h>

int
vslock(void *addr, size_t len)

void
vsunlock(void *addr, size_t len)
```

## 描述

`vslock` 和 `vsunlock` 函数分别将当前运行进程拥有的地址范围锁定和解锁到内存中。实际锁定的内存量是机器页大小的倍数。起始页号通过将 `addr` 截断到最近的前一个页边界计算，并将 `addr` + `len` 向上舍入到下一个页边界。用于此操作的进程上下文取自全局变量 `curproc`。

## 返回值

`vslock` 函数成功时返回 0，否则返回以下列出的错误之一。

## 错误

`vslock` 函数在以下情况失败：

**`[EINVAL]`** `addr` 和 `len` 参数指定的内存范围环绕机器地址空间的末尾。

**`[ENOMEM]`** 指定地址范围的大小超过系统对锁定内存的限制。

**`[EFAULT]`** 指示地址范围的某些部分未分配。在页面错误/映射时出错。
