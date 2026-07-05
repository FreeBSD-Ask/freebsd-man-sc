# dtrace_dtrace.4

`dtrace_dtrace` — 用于 BEGIN、END 和 ERROR 探测的 DTrace 提供者

## 名称

`dtrace_dtrace`

## 概要

`dtrace:::BEGIN dtrace:::END dtrace:::ERROR`

## 描述

`dtrace` 提供者实现了三个与 DTrace 程序自身生命周期相关的特殊探测。

### dtrace:::BEGIN

`dtrace``:::BEGIN` 探测在 [dtrace(1)](../man1/dtrace.1.md) 程序开始时、跟踪开始之前触发。它为初始化变量和打印列标题提供了方便的位置。

在 `dtrace``:::BEGIN` 探测的执行上下文中，不能依赖 `stack` 或 `execname` 等变量。

### dtrace:::END

`dtrace``:::END` 探测在 [dtrace(1)](../man1/dtrace.1.md) 程序结束时、所有跟踪都已停止时触发。

### dtrace:::ERROR

`dtrace``:::ERROR` 探测在另一个探测中发生意外运行时错误时触发。

下表描述了 `dtrace``:::ERROR` 的参数。

发生运行时错误的探测

`arg4` 为错误类型 `DTRACEFLT_BADADDR , DTRACEFLT_BADALIGN , DTRACEFLT_KPRIV` 或 `DTRACEFLT_UPRIV`

| **参数** | **定义** |
| --- | --- |
| `arg1` | 已启用的探测标识符（EPID） |
| `arg2` | 导致错误的动作语句索引 |
| `arg3` | 动作中的 DIF 偏移（如果可用，否则为 -1） |
| `arg4` | 错误类型 |
| `arg5` | 被访问的地址（如不适用则为 0） |

错误类型包括：

**`DTRACEFLT_UNKNOWN`** 未知错误
**`DTRACEFLT_BADADDR`** 错误地址
**`DTRACEFLT_BADALIGN`** 错误对齐
**`DTRACEFLT_ILLOP`** 非法操作
**`DTRACEFLT_DIVZERO`** 除以零
**`DTRACEFLT_NOSCRATCH`** 暂存空间不足
**`DTRACEFLT_KPRIV`** 非法内核访问
**`DTRACEFLT_UPRIV`** 非法用户访问
**`DTRACEFLT_TUPOFLOW`** 元组栈溢出
**`DTRACEFLT_BADSTACK`** 错误栈

## 文件

**sys/dtrace.h** 包含 DTrace 错误类型定义的头文件。

## 实例

### 实例 1：自定义列标题

以下脚本使用 `dtrace``:::BEGIN` 探测打印列标题。注意 pragma 行将 `quiet` 选项设为禁用默认列标题。

```sh
#pragma D option quiet
dtrace:::BEGIN
{
    printf("   %12s %-20s    %-20s %sen",
        "DELTA(us)", "OLD", "NEW", "TIMESTAMP");
}
```

### 实例 2：使用 dtrace:::ERROR 处理运行时错误

以下脚本通过在 `BEGIN` 探测中解引用地址 Ad 19930908 上的指针来导致运行时错误。结果，`ERROR` 探测触发并打印"Oops"以及探测参数。此时程序结束并触发 `END` 探测。

```sh
ERROR
{
    printf("Oopsen");
    printf("EPID (arg1): %den", arg1);
    printf("Action index (arg2): %den", arg2);
    printf("DIF offset (arg3): %den", arg3);
    printf("Fault type (arg4): %den", arg4);
    printf("Accessed address (arg5): %Xen", arg5);
    exit(1);
}
BEGIN
{
    *(int *)0x19931101;
}
END {
    printf("Bye");
}
```

此脚本将产生以下输出：

```sh
CPU     ID                    FUNCTION:NAME
  2      3                           :ERROR Oops
EPID (arg1): 2
Action index (arg2): 1
DIF offset (arg3): 16
Fault type: 1
arg5: 19931101
dtrace: error on enabled probe ID 2 (ID 1: dtrace:::BEGIN): invalid address (0x19931101) in action #1 at DIF offset 16
  2      2                             :END Bye
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [tracing(7)](../man7/tracing.7.md)

> *The illumos Dynamic Tracing Guide*, 2008, Chapter dtrace Provider.

## 作者

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。

## 注意事项

`dtrace``:::ERROR` 探测参数不能通过带类型的 `args[]` 数组访问。

[dtrace(1)](../man1/dtrace.1.md) 不会递归触发 `dtrace``:::ERROR` 探测。如果 `dtrace``:::ERROR` 的某个动作语句中发生错误，[dtrace(1)](../man1/dtrace.1.md) 将中止对 `dtrace``:::ERROR` 探测动作的进一步处理。
