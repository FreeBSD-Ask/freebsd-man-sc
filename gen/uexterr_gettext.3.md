# uexterr_gettext(3)

`uexterr_gettext` — 获取当前扩展错误的字符串表示

## 名称

`uexterr_gettext`

## 库

Lb libc

## 概要

`#include <exterr.h>`

```c
int
uexterr_gettext(char *buffer, size_t buffer_size);
```

## 描述

`uexterr_gettext` 函数用格式化的、以 null 结尾的扩展错误字符串填充 `buffer` 指针所指向的缓冲区，该字符串由返回扩展错误的系统调用的最后一次错误所报告。所传递缓冲区的容量为 `buffer_size` 字节。

通常，应用程序应使用 [err(3)](err.3.md) 系列函数来显示系统调用错误。如果不方便或甚至不可能这样做（例如对于具有高级用户界面的应用程序），可以使用 `uexterr_gettext` 函数来获取包含扩展错误的字符串。

注意，扩展错误的大部分内容直接由内核提供，因此无法进行本地化。

有关扩展错误设施的描述，请参见 [exterror(9)](../man9/exterror.9.md)。

## 返回值

该函数返回零。目前没有为该函数定义错误，但未来可能会改变。

如果添加任何错误条件，将通过返回 -1 并将 `errno` 设置为相应值来报告。

## 参见

[err(3)](err.3.md), errno(3), [exterror(9)](../man9/exterror.9.md)

## 标准

`uexterr_gettext` 是 FreeBSD 扩展，首次出现于 FreeBSD 15.0。
