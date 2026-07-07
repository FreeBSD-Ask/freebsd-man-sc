# memalignment(3)

`memalignment` — 查找对象的内存对齐

## 名称

`memalignment`

## 概要

Lb libc

`#include <stdlib.h>`

```c
size_t
memalignment(const void *ptr);
```

## 描述

`memalignment` 函数确定 `ptr` 所指对象的对齐方式。该对齐值是 2 的幂，可能大于 **alignof** 运算符支持的范围。返回值可与 **alignof** 的结果进行比较，若大于或等于该结果，则满足操作数的对齐要求。

## 返回值

以 2 的幂的形式返回 `ptr` 的对齐值。若 `ptr` 是空指针，则返回零对齐值。零对齐值表示所测试的指针不能用于访问任何类型的对象。

## 参见

aligned_alloc(3), posix_memalign(3)

## 标准

`memalignment` 函数遵循 ISO/IEC 9899:2023 ("ISO C23")。

## 历史

`memalignment` 函数添加于 FreeBSD 15.1。

## 作者

Robert Clausecker <fuz@FreeBSD.org>
