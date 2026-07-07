# i386_set_watch(3)

`i386_clr_watch` — 管理 i386 调试寄存器值

## 名称

`i386_clr_watch`, `i386_set_watch`

## 库

libc

## 概要

```c
#include <machine/reg.h>
#include <machine/sysarch.h>

int
i386_clr_watch(int watchnum, struct dbreg *d);

int
i386_set_watch(int watchnum, unsigned int watchaddr, int size,
    int access, struct dbreg *d);
```

## 描述

`i386_clr_watch` 函数在指定的调试寄存器集中禁用所指示的监视点。

`i386_set_watch` 函数按参数指示设置指定的调试寄存器。`watchnum` 参数指定使用哪个监视寄存器，取值为 0、1、2、3 或 -1。如果 `watchnum` 为 -1，则查找并使用一个空闲的监视寄存器。如果没有空闲的监视寄存器，返回错误码 -1。`watchaddr` 参数指定监视地址，`size` 指定要监视区域的大小（以字节为单位，取 1、2 或 4 字节），`access` 指定监视点的类型：

**`DBREG_DR7_EXEC`** 执行断点。

**`DBREG_DR7_WRONLY`** 仅当监视区域被写入时中断。

**`DBREG_DR7_RDWR`** 当监视区域被读取或写入时中断。

注意，这些函数实际上并不设置或清除断点；它们操作所指示的调试寄存器集。你必须使用 ptrace(2) 来检索并为进程安装调试寄存器值。

## 返回值

成功时，`i386_clr_watch` 函数返回 0。出错时返回 -1，表示 `watchnum` 无效（不在 0-3 范围内）。如果指定的 watchnum 已经被禁用，不返回错误。

成功时，`i386_set_watch` 函数返回 `watchnum` 参数，或在指定 `watchnum` 为 -1 的情况下返回实际使用的 watchnum。出错时，`i386_set_watch` 函数返回 -1，表示无法建立监视点，原因可能是没有更多可用的监视点，或 `watchnum`、`size` 或 `access` 无效。

## 参见

ptrace(2), [procfs(4)](../man4/procfs.4.md)

## 作者

本手册页由 Brian S. Dean 编写。
