# dtrace_kinst(4)

`dtrace_kinst` — 用于跟踪给定内核函数中任意指令的 DTrace 提供者

## 名称

`dtrace_kinst`

## 概要

`kinst::<function>:<instruction>`

## 描述

DTrace `kinst` 提供者允许用户跟踪给定内核函数中的任意指令。<function> 对应要跟踪的函数，<instruction> 是到特定指令的偏移量，可使用 gdb 包中的 kgdb 从函数的反汇编中获得。

`kinst` 按需创建探测，意味着它每次运行 [dtrace(1)](../man1/dtrace.1.md) 时都会搜索并解析函数的指令，而不是在模块加载时。这与 [dtrace_fbt(4)](dtrace_fbt.4.md) 的加载时解析不同，因为 `kinst` 可能为单个函数创建数千个探测，而不是 [dtrace_fbt(4)](dtrace_fbt.4.md) 情况下最多两个（入口和返回）。因此，`dtrace -l -P kinst` 不会匹配任何探测。

## 实现说明

该提供者目前仅针对 amd64 实现。

## 实例

找到 Fn vm_fault 中第三条指令对应的偏移并跟踪它，打印 RSI 寄存器的内容：

```sh
# kgdb
(kgdb) disas /r vm_fault
Dump of assembler code for function vm_fault:
   0xffffffff80876df0 <+0>:     55      push   %rbp
   0xffffffff80876df1 <+1>:     48 89 e5        mov    %rsp,%rbp
   0xffffffff80876df4 <+4>:     41 57   push   %r15
# dtrace -n 'kinst::vm_fault:4 {printf("%#x", regs[R_RSI]);}'
  2  81500                       vm_fault:4 0x827c56000
  2  81500                       vm_fault:4 0x827878000
  2  81500                       vm_fault:4 0x1fab9bef0000
  2  81500                       vm_fault:4 0xe16cf749000
  0  81500                       vm_fault:4 0x13587c366000
  ...
```

跟踪 Fn amd64_syscall 中的所有指令：

```sh
# dtrace -n 'kinst::amd64_syscall:'
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [dtrace_fbt(4)](dtrace_fbt.4.md)

## 历史

`kinst` 提供者首次出现于 FreeBSD 14.0。

## 作者

本手册页由 Christos Margiolis <christos@FreeBSD.org> 编写。
