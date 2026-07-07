# copy(9)

`copy` — 异构地址空间复制函数

## 名称

`copy`, `copyin`, `copyin_nofault`, `copyinptr`, `copyinptr_nofault`, `copyout`, `copyout_nofault`, `copyoutptr`, `copyoutptr_nofault`, `copystr`, `copyinstr`

## 概要

```c
#include <sys/types.h>
#include <sys/systm.h>

int
copyin(const void *uaddr, void *kaddr, size_t len)

int
copyin_nofault(const void *uaddr, void *kaddr, size_t len)

int
copyinptr(const void *uaddr, void *kaddr, size_t len)

int
copyinptr_nofault(const void *uaddr, void *kaddr, size_t len)

int
copyout(const void *kaddr, void *uaddr, size_t len)

int
copyout_nofault(const void *kaddr, void *uaddr, size_t len)

int
copyoutptr(const void *kaddr, void *uaddr, size_t len)

int
copyoutptr_nofault(const void *kaddr, void *uaddr, size_t len)

int __deprecated
copystr(const void *kfaddr, void *kdaddr, size_t len, size_t *done)

int
copyinstr(const void *uaddr, void *kaddr, size_t len, size_t *done)
```

## 描述

`copy` 函数旨在将连续数据从一个地址空间复制到另一个地址空间。

`copystr` 已弃用，应替换为 [strlcpy(3)](../man3/strlcpy.3.md)，后者有一个内核到内核的版本。它将从 FreeBSD 16 中移除。

`copyin` 和 `copyin_nofault` 函数从用户空间地址 `uaddr` 复制 `len` 字节数据到内核空间地址 `kaddr`，不保留所复制对象中指针的来源（更多信息参见 [memory_model(7)](../man7/memory_model.7.md)）。`copyinptr` 和 `copyinptr_nofault` 函数执行相同操作，但保留所复制的指向用户空间的指针的来源。

`copyout` 和 `copyout_nofault` 函数从内核空间地址 `kaddr` 复制 `len` 字节数据到用户空间地址 `uaddr`，不保留所复制对象中指针的来源。`copyoutptr` 和 `copyoutptr_nofault` 函数执行相同操作，但保留所复制的指向用户空间的指针的来源。

`copyin_nofault`、`copyinptr_nofault`、`copyout_nofault` 和 `copyoutptr_nofault` 函数要求内核空间和用户空间数据可访问且不会引发页错误。源地址和目标地址必须分别物理映射以供读取和写入访问，且源地址和目标地址都不可分页。

`copyinptr`、`copyinptr_nofault`、`copyoutptr` 和 `copyoutptr_nofault` 函数必须在复制可能包含指针的数据时使用，但应仅在必要时使用，以限制可能在地址空间之间泄漏指针的代码路径数量。

`copystr` 函数从内核空间地址 `kfaddr` 复制最多 `len` 字节的以 NUL 结尾的字符串到内核空间地址 `kdaddr`。实际复制的字节数（包括终止的 NUL）在 `*done` 中返回（如果 `done` 非 `NULL`）。

`copyinstr` 函数从用户空间地址 `uaddr` 复制最多 `len` 字节的以 NUL 结尾的字符串到内核空间地址 `kaddr`。实际复制的字节数（包括终止的 NUL）在 `*done` 中返回（如果 `done` 非 `NULL`）。

## 返回值

`copy` 函数成功时返回 0。除 `copystr` 外的所有函数在遇到错误地址时返回 `EFAULT`。如果发生页错误，`copyin_nofault` 和 `copyout_nofault` 函数返回 `EFAULT`。如果字符串长度超过 `len` 字节，`copystr` 和 `copyinstr` 函数返回 `ENAMETOOLONG`。

## 参见

[fetch(9)](fetch.9.md), [store(9)](store.9.md)
