# getbsize(3)

`getbsize` — 获取首选块大小

## 名称

`getbsize`

## 库

Lb libc

## 概要

`#include <stdlib.h>`

```c
char *
getbsize(int *headerlenp, long *blocksizep);
```

## 描述

`getbsize()` 函数根据 `BLOCKSIZE` 环境变量的值，返回系统工具 [df(1)](../man1/df.1.md)、[du(1)](../man1/du.1.md) 和 [ls(1)](../man1/ls.1.md) 用于报告的首选块大小。`BLOCKSIZE` 可以直接以字节为单位指定，也可以通过在数字后跟“`K`”或“`k`”指定为千字节的倍数、后跟“`M`”或“`m`”指定为兆字节的倍数、后跟“`G`”或“`g`”指定为吉字节的倍数。倍数必须是整数。

`BLOCKSIZE` 的有效值为 512 字节到 1 GB。小于 512 字节的值会向上取整为 512 字节，大于 1 GB 的值会向下取整为 1 GB。在每种情况下，`getbsize()` 都会通过 warnx(3) 产生警告消息。

`getbsize()` 函数返回一个指向以 NUL 结尾的字符串的指针，该字符串描述块大小，类似于“`1K-blocks`”。`headerlenp` 所指向的内存被填充为字符串的长度（不包括终止的 NUL 字符）。`blocksizep` 所指向的内存被填充为块大小（以字节为单位）。

## 参见

[df(1)](../man1/df.1.md), [du(1)](../man1/du.1.md), [ls(1)](../man1/ls.1.md), [systat(1)](../man1/systat.1.md), [environ(7)](../man7/environ.7.md)

## 历史

`getbsize()` 函数首次出现在 4.4BSD 中。
