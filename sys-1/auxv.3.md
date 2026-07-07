# auxv(3)

`elf_aux_info` — 从当前进程的 ELF 辅助向量中提取数据

## 名称

`elf_aux_info`

## 库

libc

## 概要

```c
#include <sys/auxv.h>

int
elf_aux_info(int aux, void *buf, int buflen);
```

## 描述

`elf_aux_info` 函数获取由 `aux` 请求的辅助信息向量。如果信息能够容纳，则存入所提供的缓冲区。以下值定义在

```c
#include <sys/elf_common.h>
```

中，可被请求（相应的缓冲区大小在括号中注明）：

**AT_CANARY** SSP 的 canary 值（任意大小的缓冲区，返回能容纳的字节数，其余部分清零）。

**AT_EXECPATH** 所执行程序的路径 `(MAXPATHLEN)`。如果进程由 fexecve(2) 初始化且 namecache 中不再包含该文件名，则可能不存在此项。

**AT_HWCAP** CPU/硬件特性标志 `(sizeof(u_long))`。

**AT_HWCAP2** CPU/硬件特性标志 `(sizeof(u_long))`。

**AT_HWCAP3** CPU/硬件特性标志 `(sizeof(u_long))`。

**AT_HWCAP4** CPU/硬件特性标志 `(sizeof(u_long))`。

**AT_NCPUS** CPU 数量 `(sizeof(int))`。

**AT_OSRELDATE** 程序运行所在内核或 Jail 的 `OSRELDATE` `(sizeof(int))`。

**AT_PAGESIZES** 页面大小向量（任意大小的缓冲区，返回能容纳的 `pagesizes` 数组元素数量）。

**AT_PAGESZ** 以字节为单位的页面大小 `(sizeof(int))`。

**AT_TIMEKEEP** 指向 VDSO timehands 的指针（供库内部使用，`sizeof(void *)`）。

**AT_USRSTACKBASE** 主线程用户栈的顶部。

**AT_USRSTACKLIM** 主线程用户栈的增长上限。

## 返回值

成功时返回零，失败时返回一个错误号。

## 错误

**`[EINVAL]`** 请求了未知的项目。

**`[EINVAL]`** 所提供的缓冲区大小与所请求项目的要求不符。

**`[ENOENT]`** 所请求的项目不可用。

## 历史

`elf_aux_info` 函数出现于 FreeBSD 12.0。

## 缺陷

通过该函数仅能访问可用辅助信息向量项目中的一小部分。某些项目需要"大小正好"的缓冲区，而其他项目只需"足够大"的缓冲区。
