# bcopy.9

`bcopy` — 复制对象中的字节

## 名称

`bcopy`

## 概要

```c
#include <sys/systm.h>
```

```c
void
bcopy(const void *src, void *dst, size_t len)
```

## 描述

`bcopy` 函数从对象 `src` 复制 `len` 字节到对象 `dst`，保留复制对象中指针的来源（参见 [memory_model(7)](../man7/memory_model.7.md)）。这两个对象可以重叠。如果 `len` 为零，则不复制任何字节。

`bcopy` 函数已弃用，新代码应适当使用 `memcpy` 或 `memmove`。

## 参见

[memcpy(9)](memcpy.9.md), [memmove(9)](memmove.9.md)

## 历史

`bcopy` 函数出现于 4.2BSD。

IEEE Std 1003.1-2008 ("POSIX.1") 移除了 `bcopy` 的规范，在 IEEE Std 1003.1-2004 ("POSIX.1") 中标记为 LEGACY。新程序应使用 memmove(3)。如果输入和输出缓冲区不重叠，则 memcpy(3) 更高效。注意，`bcopy` 的 `src` 和 `dst` 参数顺序与 `memmove` 和 `memcpy` 相反。实际上，

```c
#include <sys/systm.h>
```

自 FreeBSD 12.0 起，将 `bcopy` 定义为调用 `memmove` 的宏。
