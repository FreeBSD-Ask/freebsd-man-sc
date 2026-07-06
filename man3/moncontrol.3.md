# moncontrol(3)

`moncontrol` — 控制执行性能分析

## 名称

`moncontrol`, `monstartup`

## 库

Lb libc

## 概要

`#include <sys/types.h>`

`#include <sys/gmon.h>`

```c
void
moncontrol(int mode);

void
monstartup(u_long lowpc, u_long highpc);
```

## 描述

使用 [cc(1)](../man1/cc.1.md) 的 `-pg` 选项编译的可执行程序会自动包含用于为 gprof(1) 调用图执行性能分析器收集统计信息的调用。在典型操作中，性能分析从程序启动时开始，到程序调用 exit 时结束。程序退出时，性能分析数据将写入文件 `progname``.gmon`，其中 progname 是程序的名称，随后可使用 gprof(1) 查看结果。

`moncontrol` 函数有选择地控制程序内的性能分析。程序启动时即开始分析。要停止收集直方图时钟滴答和调用计数，使用 `moncontrol(0)`；要恢复收集直方图时钟滴答和调用计数，使用 `moncontrol(1)`。此功能允许测量特定操作的开销。注意，无论 `moncontrol` 处于何种状态，程序退出时都会生成输出文件。

未使用 `-pg` 加载的程序可通过调用 `monstartup` 并指定要进行性能分析的地址范围来有选择地收集性能分析统计信息。`lowpc` 和 `highpc` 参数指定要采样的地址范围；采样的最低地址为 `lowpc`，最高地址恰好在 `highpc` 之下。只有该范围内使用 [cc(1)](../man1/cc.1.md) 的 `-pg` 选项编译的函数才会出现在输出的调用图部分；然而，该地址范围内的所有函数都会测量其执行时间。性能分析从 `monstartup` 返回时开始。

## 环境变量

以下环境变量影响 `monstartup` 的执行：

**PROFIL_USE_PID** 如果设置，进程的 pid 将被插入到文件名中。

## 文件

**`progname.gmon`** 执行数据文件

## 参见

[cc(1)](../man1/cc.1.md), gprof(1), [profil(2)](../man2/profil.2.md), [clocks(7)](../man7/clocks.7.md)
