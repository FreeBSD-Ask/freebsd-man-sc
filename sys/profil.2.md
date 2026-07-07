# profil(2)

`profil` — 控制进程性能分析

## 名称

`profil`

## 库

Lb libc

## 概要

`#include <unistd.h>`

```c
int
profil(char *samples, size_t size, vm_offset_t offset, int scale);
```

## 描述

`profil()` 系统调用启用或禁用当前进程的程序计数器性能分析。如果启用性能分析，则在每个性能分析时钟滴答时，内核会更新 `samples` 缓冲区中的相应计数。性能分析时钟的频率记录在性能分析输出文件头中。

缓冲区 `samples` 包含 `size` 字节，并被划分为一系列 16 位的 bin。每个 bin 统计在启用性能分析期间，当性能分析时钟滴答发生时，程序计数器处于进程中特定地址范围内的次数。对于给定的程序计数器地址，对应 bin 的编号由以下关系给出：

```c
[(pc - offset) / 2] * scale / 65536
```

`offset` 参数是内核采集程序计数器样本的最低地址。`scale` 参数范围为 1 到 65536，可用于改变 bin 的跨度。scale 为 65536 时，每个 bin 映射到 2 字节的地址范围；scale 为 32768 时为 4 字节，16384 时为 8 字节，以此类推。中间值提供近似的中间范围。`scale` 值为 0 时禁用性能分析。

## 返回值

成功完成后返回 0；否则返回 -1，并设置 `errno` 以指示错误。

## 文件

**/usr/lib/gcrt0.o** 性能分析 C 运行时启动文件

`gmon.out` 性能分析输出文件的惯例名称

## 错误

可能报告以下错误：

**[`EFAULT`]** 缓冲区 `samples` 包含无效地址。

## 参见

gprof(1)

## 历史

`profil()` 功能首次出现于 Version 3 AT&T UNIX。

## 缺陷

此例程应命名为 `profile`。

`samples` 参数实际上应为 `unsigned short` 类型的向量。

gmon.out 文件的格式未文档化。
