# dtrace_pid(4)

`dtrace_pid` — 基于函数边界检测的动态用户空间跟踪 DTrace 提供者

## 名称

`dtrace_pid`

## 概要

`pidPID:module:function:entry pidPID:module:function:[offset] pidPID:module:function:return`

## 描述

`pid` 提供者通过检测用户空间程序中函数的入口和返回来实现用户空间动态跟踪。有关函数边界检测的更多详情，请参见 [dtrace_fbt(4)](dtrace_fbt.4.md)。

`pid` 提供者提供以下探测：

**`pid`** `PID``:``module``:``function``:entry` 检测 `function` 的入口。

**`pid`** `PID``:``module``:``function``:`[`offset`] 检测 `function` 中位于 `offset` 字节处（以十六进制整数表示）的指令。

**`pid`** `PID``:``module``:``function``:return` 检测从 `function` 的返回。

### 探测参数

入口探测（`pid``PID``:``module``:``function``:entry`）的参数是被跟踪函数调用的参数。

| **入口探测参数** | **定义** |
| ---------------- | -------- |
| Ft uint64_t `arg0` | 函数的第一个参数 |
| Ft uint64_t `arg1` | 函数的第二个参数 |
| Ft uint64_t `arg2` | 函数的第三个参数 |
| `...` | ... |

偏移探测（`pid``PID``:``module``:``function``:`[`offset`]）不定义任何参数。使用 `uregs[]` 检查寄存器。

返回探测（`pid``PID``:``module``:``function``:return`）的参数是程序计数器和函数的返回值。

| **返回探测参数** | **定义** |
| ---------------- | -------- |
| Ft uint64_t `arg0` | 程序计数器 |
| Ft uint64_t `arg1` | 函数的返回值 |

注意，`pid` 提供者内的所有探测参数类型均为 Ft uint64_t。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_fbt(4)](dtrace_fbt.4.md), [dtrace_kinst(4)](dtrace_kinst.4.md), [elf(5)](../man5/elf.5.md), [d(7)](../man7/d.7.md), [tracing(7)](../man7/tracing.7.md)

> Brendan Gregg, Jim Mauro, *DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and FreeBSD*, Prentice Hall, 2011.

> *The illumos Dynamic Tracing Guide*, 2008, Chapter pid Provider.

## 作者

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
