# dtrace_profile(4)

`dtrace_profile` — 在给定时间间隔触发探测的 DTrace 提供者

## 名称

`dtrace_profile`

## 概要

`profile:::profile-rate[unit] profile:::tick-rate[unit]`

## 描述

`profile` 提供者实现了三个与 DTrace 程序自身生命周期相关的特殊探测。

### 探测

`profile`:::profile 探测在所有 CPU 上触发，适合定期测量整个系统。

`profile`:::tick 探测在单个 CPU 上触发，每次可能是不同的 CPU。例如，它们可用于定期打印部分结果。

### 速率与时间单位

`profile` 提供者探测将按指定 `rate` 触发。

默认单位为 `hz`。`profile` 提供者支持以下时间单位：

| **时间单位** | **定义** |
| ------------ | -------- |
| `ns , nsec` | 纳秒 |
| `us , usec` | 微秒 |
| `ms , msec` | 毫秒 |
| `s , sec` | 秒 |
| `m , min` | 分钟 |
| `h , hour` | 小时 |
| `d , day` | 天 |
| `hz` | 赫兹（每秒频率） |

### 探测参数

`profile` 提供者探测的参数为：

**`arg0`** 探测触发时内核中的 PC（程序计数器），若进程当时不在内核中则为 0。

**`arg1`** 探测触发时用户进程中的 PC，若进程当时在内核中则为 0。

使用参数 `arg0` 和 `arg1` 可判断 `profile` 提供者探测是在内核还是用户态上下文中触发。

## 实现说明

[sysctl(8)](../man8/sysctl.8.md) 变量 `kern.dtrace.profile.aframes` 控制 `profile` 提供者跳过的人工帧数。

## 实例

### 实例 1：分析 CPU 上的内核栈回溯

以下 DTrace 单行命令使用 `profile` 提供者收集 60 秒内的栈回溯。

```sh
dtrace -x stackframes=100 -n 'profile-197 /arg0/ {@[stack()] = count();} tick-60s {exit(0);}
```

系统以 197 Hz 进行采样，以避免与其他周期性活动同步采样。这种非自然频率可最大程度降低与其他事件重叠的概率。

选项 `-x` `stackframes=100` 增加 Fn stack 期间展开的内核栈帧的最大数量。

检查 `arg0` 是否非零可确保仅在程序处于内核上下文时进行分析。

参见 Lk <https://www.brendangregg.com/flamegraphs.html> 了解如何从所获栈回溯生成火焰图。

## 参见

[dtrace(1)](../man1/dtrace.1.md), [tracing(7)](../man7/tracing.7.md)

> *The illumos Dynamic Tracing Guide*, 2008, Chapter dtrace Provider.

> Brendan Gregg, Jim Mauro, *DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X and FreeBSD*, pp. pp. 24-25, Prentice Hall, 2011.

## 作者

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
