# d.7

`D` — DTrace 脚本语言概述

## 名称

`D`

## 概要

`provider : module : function : name [] [] /predicate /] {action} ]`

## 描述

`D` 是 [dtrace(1)](../man1/dtrace.1.md) 脚本语言。本手册提供 `D` 语言和脚本的简要参考。

本手册页作为语言的简短参考。完整参考请参阅 Sx SEE ALSO 中列出的书籍。

## 宏变量

通过 `-p` 标志指定或通过 `-c` 标志创建。

| **名称** | **描述** |
| --- | --- |
| `$1 , $2 , $3 , ...` | 宏参数 |
| `$egid` | 有效组 ID（getegid(2)） |
| `$euid` | 有效用户 ID（geteuid(2)） |
| `$gid` | 实际组 ID（getgid(2)） |
| `$pid` | 进程 ID（getpid(2)） |
| `$pgid` | 进程组 ID（getpgrp(2)） |
| `$ppid` | 父进程 ID（getppid(2)） |
| `$sid` | 会话 ID（getsid(2)） |
| `$target` | 进程的目标进程 ID |
| `$uid` | 实际用户 ID（getuid(2)） |

宏参数对应命令行操作数。根据上下文，它们扩展为整数、标识符或字符串。在宏参数前加额外美元符号（`$`）可强制字符串扩展。

例如，

dtrace -n 'syscall::fstatat: /execname == $$1/ {}' -- ls

使用 `$$1` 而非 `$1` 以扩展为字符串而非全局变量标识符。

## 探针描述

探针描述由四个元素组成：

> `provider``:``module` `:` `function` `:` `name`

`module`、`function` 和 `name` 的确切含义取决于 `provider`。

## 用户定义变量类型

| **类型** | **语法** |
| --- | --- |
| 全局 | `variable_name` |
| 聚合 | **@**`variable_name` |
| 线程本地 | **self->**`variable_name` |
| 子句本地 | **this->**`variable_name` |

*提示：*

- 始终使用具有最小作用域的变量类型以最小化处理开销。
- 尽可能使用聚合变量而非全局变量。与全局变量不同，聚合变量是多 CPU 安全的。

## 内置变量

### 探针参数

**`args[]`** 类型化探针参数数组。

**`arg0 , ... , arg9`** 表示为 64 位无符号整数的无类型探针参数。仅前十个参数可通过此方式使用。

### 探针信息

**`epid`** 已启用探针 ID，唯一标识已启用探针。已启用探针由其探针 ID、谓词和操作定义。

**`id`** 探针 ID，唯一标识 DTrace 可用的探针。

**`probeprov`** 探针描述中的 `provider`（`provider` `:` `module` `:` `function` `:` `name`）

**`probemod`** 探针描述中的 `module`（`provider` `:` `module` `:` `function` `:` `name`）

**`probefunc`** 探针描述中的 `function`（`provider` `:` `module` `:` `function` `:` `name`）

**`probename`** 探针描述中的 `name`（`provider` `:` `module` `:` `function` `:` `name`）

### 进程信息

**`execargs`** 进程参数。等效于 `curthread->td_proc->p_args`。

**`execname`** 当前进程的名称。等效于 `curthread->td_proc->p_comm`。

**`gid`** 当前进程的组 ID。

**`pid`** 当前进程的进程 ID。

**`ppid`** 当前进程的父进程 ID。

**`uid`** 当前进程的用户 ID。

### 线程信息

`#include <sys/proc.h>`

**`uregs[]`** 保存的用户模式寄存器值。

**`cpu`** 当前 CPU 的 ID。

**`stackdepth`** 内核栈帧深度。

**`ustackdepth`** `stackdepth` 的用户空间对应物。

**`tid`** 线程 ID。根据上下文，可以是内核线程 ID 或用户进程中的线程 ID。

**`errno`** 当前线程执行的最后一个系统调用的 errno(2) 值。

**`curlwpsinfo`** 指向当前线程的 `lwpsinfo_t` 表示的指针。更多细节参见 [dtrace_proc(4)](../man4/dtrace_proc.4.md)。

**`curpsinfo`** 指向当前进程的 `psinfo_t` 表示的指针。更多细节参见 [dtrace_proc(4)](../man4/dtrace_proc.4.md)。

**`curthread`** 指向当前在 CPU 上的线程结构的指针。例如，`curthread->td_name` 返回线程名称。该头文件记录了 `struct thread` 的所有成员。

**`caller`** 执行当前探针时内核线程指令的地址。

**`ucaller`** `caller` 的用户空间对应物。

### 时间戳

**`timestamp`** 自引导以来的纳秒数。适用于计算相对时间差和延迟。

**`vtimestamp`** 当前线程在 CPU 上花费的纳秒数。处理触发的 DTrace 探针时计数器不增加。适用于计算 CPU 时间的相对时间差。

**`walltimestamp`** 自纪元（1970-01-01T00+00:00）以来的纳秒数。适用于为日志加时间戳。

## 内置函数

strchr("abc", 'b');

strchr("abc", 'd');

strjoin("abc", "def")

strstr("abc1bc2", "bc")

strstr("abc", "xy")

strtok("abcdefg", "xyzd")

substr("abcd", 2)

substr("abcd", 2, 1)

substr("abcd", 99)

**Ft** string Fn strchr string s char c 返回 `s` 中从 `c` 第一次出现处开始的子串。如果 `c` 不在 `s` 中出现则返回 `NULL`。例如，返回 `bc`，返回 `NULL`。

**Ft** string Fn strjoin string s1 string s2 返回连接 `s1` 和 `s2` 的字符串。例如，返回 `abcdef`。

**Ft** string Fn strrchr string s char c 返回 `s` 中从 `c` 最后一次出现处开始的子串。类似 Fn strchr。

**Ft** string Fn strstr string haystack string needle 返回 `haystack` 中从 `needle` 第一次出现处开始的子串。如果 `needle` 不是 `haystack` 的子串则返回 `NULL`。例如，返回 `bc1bc2`，返回 `NULL`。

**Ft** string Fn strtok string s string separators 用 `separators` 标记化 `s`。例如，返回 `abc`。

**Ft** size_t Fn strlen string s 返回字符串 `s` 的长度。

**Ft** string Fn substr string s int position [int length] 返回字符串 `s` 从 `position` 开始的子串。子串最多 `length` 长。如果未指定 `length`，使用字符串的其余部分。如果 `position` 大于 `s` 的尺寸，返回空字符串。例如，返回 `cd`，返回 `c`，返回空字符串。

### 聚合函数

**Fn** avg value 平均值
**Fn** count 计数
**Fn** llquantize value factor low high nsteps 对数线性量化
**Fn** lquantize value low high nsteps 线性量化
**Fn** max value 最大值
**Fn** min value 最小值
**Fn** quantize value 二的幂频率分布
**Fn** stddev value 标准差
**Fn** sum value 总和

### 内核破坏性函数

默认情况下，[dtrace(1)](../man1/dtrace.1.md) 不允许使用破坏性操作。

**Fn** breakpoint 设置内核断点并将控制权转移到 [ddb(4)](../man4/ddb.4.md) 内核调试器。

**Fn** chill nanoseconds 在 CPU 上自旋指定的 `nanoseconds` 纳秒数。

**Fn** panic 使内核崩溃。

## 文件

**`/usr/share/dtrace`** FreeBSD 基本系统附带的 DTrace 脚本。

## 参见

[awk(1)](../man1/awk.1.md), [dtrace(1)](../man1/dtrace.1.md), [tracing(7)](tracing.7.md)

> *The illumos Dynamic Tracing Guide*, 2008.

> Brendan Gregg, Jim Mauro, *DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and FreeBSD*, Prentice Hall, 2011.

> George Neville-Neil, Jonathan Anderson, Graeme Jenkinson, Brian Kidney, Domagoj Stolfa, Arun Thomas, Robert N. M. Watson, "University of Cambridge Computer Laboratory", August 2018.

## 历史

本手册页首次出现于 FreeBSD 15.0。

## 作者

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。

## 缺陷

通常提供当前工作目录的 `cwd` 变量目前在 FreeBSD 上不受支持。

宏变量 `$projid` 和 `$taskid` 在 FreeBSD 上始终为 0。

函数 Fn ddi_pathname、Fn getmajor 和 Fn getminor 在 FreeBSD 上不受支持。
