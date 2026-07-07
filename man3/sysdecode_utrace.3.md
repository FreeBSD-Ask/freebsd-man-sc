# sysdecode_utrace(3)

`sysdecode_utrace` — 生成 utrace 记录的文本描述

## 名称

`sysdecode_utrace`

## 库

Lb libsysdecode

## 概要

`#include <sysdecode.h>`

`int sysdecode_utrace(FILE *fp, void *buf, size_t len, int decimal)`

## 描述

`sysdecode_utrace` 函数将由 `buf` 和 `len` 标识的 [utrace(2)](../sys/utrace.2.md) 记录的文本表示输出到输出流 `fp`。

该函数仅为某些类型的记录输出表示。如果记录被识别，函数将输出描述并返回非零值。如果记录未被识别，函数不输出任何内容并返回零。`sysdecode_utrace` 函数目前识别由 malloc(3) 和 [rtld(1)](../man1/rtld.1.md) 生成的 [utrace(2)](../sys/utrace.2.md) 记录。

## 返回值

`sysdecode_utrace` 函数在识别 [utrace(2)](../sys/utrace.2.md) 记录时返回非零值；否则返回零。

## 参见

[utrace(2)](../sys/utrace.2.md), sysdecode(3)
