# i386_get_ldt(2)

`i386_get_ldt` — 管理 i386 每进程本地描述符表条目

## 名称

`i386_get_ldt`, `i386_set_ldt`

## 库

Lb libc

## 概要

`#include <machine/segments.h>`

`#include <machine/sysarch.h>`

```c
int
i386_get_ldt(int start_sel, union descriptor *descs, int num_sels);

int
i386_set_ldt(int start_sel, union descriptor *descs, int num_sels);
```

## 描述

`i386_get_ldt()` 系统调用返回当前进程 LDT 中 i386 描述符的列表。`i386_set_ldt()` 系统调用设置当前进程 LDT 中的 i386 描述符列表。对于这两个例程，`start_sel` 指定 LDT 中开始处的选择子索引，`descs` 指向一个包含 `num_sels` 个待设置或返回描述符的数组。

`descs` 数组中的每个条目可以是 segment_descriptor 或 gate_descriptor，定义在 `#include <i386/segments.h>` 中。这些结构由架构定义为不相交的位域，因此在构造它们时必须小心。

如果 `start_sel` 为 `LDT_AUTO_ALLOC`，`num_sels` 为 1 且 `descs` 指向的描述符合法，则 `i386_set_ldt()` 将分配一个描述符并返回其选择子编号。

如果 `num_descs` 为 1，`start_sels` 有效，且 `descs` 为 NULL，则 `i386_set_ldt()` 将释放该描述符（使其可以在以后重新分配）。

如果 `num_descs` 为 0，`start_sels` 为 0 且 `descs` 为 NULL，则作为特殊情况，`i386_set_ldt()` 将释放所有描述符。

## 返回值

成功完成时，`i386_get_ldt()` 返回 LDT 中当前的描述符数量。`i386_set_ldt()` 系统调用成功时返回设置的第一个选择子。如果内核在 LDT 中分配了描述符，则返回分配的索引。否则，返回 -1，并设置全局变量 `errno` 以指示错误。

## 错误

`i386_get_ldt()` 和 `i386_set_ldt()` 系统调用在以下情况下会失败：

**[`EINVAL`]** `start_sel` 或 `num_sels` 使用了不适当的值。

**[`EACCES`]** 调用者试图使用会绕过保护或导致失败的描述符。

## 参见

i386 Microprocessor Programmer's Reference Manual, Intel

## 警告

使用此调用可能会严重损坏你的进程。