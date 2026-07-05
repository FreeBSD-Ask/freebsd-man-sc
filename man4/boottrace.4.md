# boottrace.4

`boottrace` — 引导时、运行时和关机时的跟踪设施

## 名称

`boottrace`

## 概要

`#include <sys/boottrace.h>`

## 描述

`boottrace` 是一个内核-用户空间接口，用于在系统引导和关机期间捕获跟踪事件（特别是单次事件）。

事件注解存在于：

- 内核中的引导和关机路径
- 一些关键系统工具（[init(8)](../man8/init.8.md)、[shutdown(8)](../man8/shutdown.8.md)、[reboot(8)](../man8/reboot.8.md)）
- [rc(8)](../man8/rc.8.md) 脚本

`boottrace` 无条件编译进内核，默认禁用。

## 事件表

事件存储在三个事件表中：引导时事件、运行时事件和关机时事件。

| **表名** | **事件描述** |
| -------- | ------------ |
| 引导时事件 | 引导、内核初始化，以及 [rc(8)](../man8/rc.8.md) 执行；直至 [init(8)](../man8/init.8.md) 转入多用户模式 |
| 运行时事件 | 从系统完成引导（包括 [rc(8)](../man8/rc.8.md) 执行）且 [init(8)](../man8/init.8.md) 转入多用户模式起，直至关机流程开始 |
| 关机时事件 | 在初始化关机、重启或内核 panic 之后 |

## 加载器可调参数

可调参数可在 [loader(8)](../man8/loader.8.md) 提示符下引导内核前设置，或存储在 loader.conf(5) 中。`boottrace` 提供以下加载器可调参数：

**`kern.boottrace.dotrace_kernel`** 设置为 `1` 以启用内核事件跟踪。默认：`1`（启用）。

**`kern.boottrace.dotrace_user`** 设置为 `1` 以启用用户空间事件跟踪。默认：`1`（启用）。

## SYSCTL 变量

以下变量同时作为 [sysctl(8)](../man8/sysctl.8.md) 变量和 [loader(8)](../man8/loader.8.md) 可调参数可用：

**`kern.boottrace.boottrace`** 创建新的跟踪事件并写入引导时表。新的跟踪事件由进程名和事件描述组成，以冒号（`:`）分隔。如果缺少冒号或提供的进程名字符串为空，则从调用进程推断进程名（即其可执行文件名）。

**`kern.boottrace.enabled`** 设置为 `1` 以启用跟踪。这是一个只读 [sysctl(8)](../man8/sysctl.8.md) 变量。默认：`0`（禁用）。

**`kern.boottrace.log`** 显示存储在引导时表和运行时表中的事件。这是一个不透明的 [sysctl(8)](../man8/sysctl.8.md) 变量。

**`kern.boottrace.runtrace`** 与 `kern.boottrace.boottrace` 相同，但写入运行时表。

**`kern.boottrace.shuttrace`** 与 `kern.boottrace.boottrace` 相同，但写入关机时表。

**`kern.boottrace.shutdown_trace`** 在系统停止之前将关机时事件记录到控制台。

**`kern.boottrace.shutdown_trace_threshold`** 设置以毫秒为单位记录关机时事件的时间阈值。如果与前一事件的时间差小于阈值，则忽略该事件。默认：`0`（记录所有事件）。

## 实例

使用 [sysctl(8)](../man8/sysctl.8.md) 创建一个进程名为“foo”、事件描述为“bar”的新跟踪事件：

```sh
sysctl kern.boottrace.boottrace="foo:bar"
```

以下是 `kern.boottrace.log` 的示例输出（为便于阅读以“[...]”省略）

```sh
CPU      msecs      delta process                  event                                      PID CPUtime IBlks OBlks
  0   44872811          0 kernel                   sysinit 0x2100001                            0    0.00     0     0
  0   44872812          1 kernel                   sysinit 0x2110000                            0    0.00     0     0
  0   44872812          0 kernel                   sysinit 0x2140000                            0    0.00     0     0
[...]
  0   44872817          0 kernel                   sysinit 0x2800000                            0    0.00     0     0
  0   44873820       1003 kernel                   sysinit 0x2880000                            0    0.00     0     0
  0   44873820          0 kernel                   sysinit 0x2888000                            0    0.00     0     0
[...]
  1   44875735          0 kernel                   sysinit 0xfffffff                            0    0.00     0     0
  1   44875735          0 swapper                  mi_startup done                              0    0.00     0     0
  0   44875750         15 init                     init(8) starting...                          1    0.00     0     0
  0   44875751          1 init                     /etc/rc starting...                          1    0.00     0     0
  0   44875831         80 boottrace                /etc/rc.d/rctl start                        26    0.00     0     0
  1   44875839          8 boottrace                /etc/rc.d/rctl done                         26    0.00     2     0
[...]
  0   44876446          0 boottrace                /etc/rc.d/netif start                      390    0.00     0     0
  1   44881116       4670 boottrace                /etc/rc.d/netif done                       390    0.12    34     0
[...]
  0   44882866          1 boottrace                /etc/rc.d/securelevel start               1679    0.00     0     0
  0   44882872          6 boottrace                /etc/rc.d/securelevel done                1679    0.00     0     0
  1   44882879          7 init                     /etc/rc finished                             1    2.22   743    15
Total measured time: 10068 msecs
CPU      msecs      delta process                  event                                      PID CPUtime IBlks OBlks
  1   44882880          0 init                     multi-user start                             1    2.22   743    15
  0   44918215      35335 kldload                  hwpmc.ko: sysinit 0xd800000               1698    0.00     0     0
Total measured time: 35335 msecs
```

## 参见

[tslog(4)](tslog.4.md), boottrace(8), [sysctl(8)](../man8/sysctl.8.md)

## 历史

NetApp 创建了 `boottrace` 用于诊断慢速设备和子系统。在上游化之后，`boottrace` 首次公开发布于 FreeBSD 14.0。

## 作者

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
