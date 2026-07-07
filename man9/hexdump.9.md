# hexdump(9)

`hexdump` — 以十六进制形式将字节块转储到控制台

## 名称

`hexdump`

## 概要

```c
#include <sys/systm.h>
```

```c
void
hexdump(void *ptr, int length, const char *hdr, int flags)
```

## 描述

`hexdump` 函数以十六进制形式将字节数组打印到控制台，如果可能，还会打印字节的 ASCII 表示。默认情况下，每行输出以偏移计数开始，后跟 16 个十六进制值，再后跟 16 个 ASCII 字符。

**位 0-7** 每行显示字节数的整数值。值为 0 表示使用默认值 16。

**位 8-15** 用作十六进制输出分隔符的字符 ASCII 值。值为 0 表示使用默认值 32（ASCII 空格）。

**`HD_OMIT_COUNT`** 不在每行开头打印偏移列。

**`HD_OMIT_HEX`** 不在每行打印十六进制值。

**`HD_OMIT_CHARS`** 不在每行打印字符值。

**`ptr`** 指向要打印的字节数组的指针。不需要 `NUL` 终止。

**`length`** 要打印的字节数。

**`hdr`** 指向 `NUL` 终止字符串的指针，将前置于每行输出。值为 `NULL` 表示不打印标题。

**`flags`** 用于控制输出格式的标志。

## 参见

[ascii(7)](../man7/ascii.7.md)

## 作者

本手册页由 Scott Long 编写。
