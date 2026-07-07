# dtrace_syscall(4)

`dtrace_syscall` — 用于系统调用的 DTrace 提供者

## 名称

`dtrace_syscall`

## 概要

`syscall:abi:syscall:entry syscall:abi:syscall:return`

## 描述

`syscall` 提供者为系统调用提供入口和返回探测。

探测描述中的模块为 `abi`，用于指示 `syscall` 所属的系统调用 ABI。`syscall` 支持以下系统调用 ABI：

**`freebsd`** 原生 ABI。

**`freebsd32`** 非原生的 32 位 ABI。

**`linux`** 参见 [linux(4)](linux.4.md)。

**`linux32`** 参见 [linux(4)](linux.4.md)。

`entry` 探测的参数为传递给系统调用的参数。

`return` 探测将系统调用的返回值同时存储在 `arg0` 和 `arg1` 中。

检查 [d(7)](../man7/d.7.md) 中的 `errno` 变量可判断系统调用是否失败。

## 实例

### 实例 1：统计系统调用次数

以下脚本跟踪所有系统调用，并对系统中每个进程进行计数。

```sh
syscall:::entry {
    @[execname, pid] = count();
}
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), intro(2), [tracing(7)](../man7/tracing.7.md)

> *The illumos Dynamic Tracing Guide*, 2008, Chapter syscall Provider.

> Brendan Gregg, Jim Mauro, *DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and FreeBSD*, pp. pp. 315-327, Prentice Hall, 2011, Chapter Syscall Provider.

## 作者

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
