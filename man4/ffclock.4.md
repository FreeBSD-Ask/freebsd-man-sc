# ffclock(4)

`FFCLOCK` — 前馈系统时钟

## 名称

`FFCLOCK`

## 概要

`options FFCLOCK`

## 描述

多年来，ntpd(8) 守护进程一直是系统时钟同步的主流解决方案，这反过来也影响了系统时钟的设计。ntpd 守护进程实现了反馈控制算法，已证明在常见使用场景下表现不佳。

由合适的守护进程实现的前馈时钟同步算法，配合 `FFCLOCK` 内核支持，已被证明能够提供高度稳健且精确的时钟同步。除了计时功能外，`FFCLOCK` 内核机制还提供了新的时间戳功能以及使用专用时钟的能力。前馈同步也非常适合虚拟化环境，可减少客户机中的计时开销，并确保在客户机实时迁移期间系统时钟持续平稳运行。

`FFCLOCK` 内核支持在内核中提供前馈时间戳函数，并提供系统调用以支持前馈同步守护进程（参见 ffclock(2)）。

### 内核选项

以下内核配置选项与 `FFCLOCK` 相关：

**`FFCLOCK`** 启用前馈时钟支持。

### 配置

当内核中编译了前馈时钟支持后，将有多个系统时钟可供选择。可以通过 `kern.sysclock` [sysctl(8)](../man8/sysctl.8.md) 树配置系统时钟，该树提供以下变量：

**`kern.sysclock.active`** 当前活动的系统时钟名称，用于提供时间。设置为 `kern.sysclock.available` 中的某个名称即可更改默认的活动系统时钟。

**`kern.sysclock.available`** 列出可用系统时钟的名称（只读）。

可以通过 `kern.sysclock.ffclock` sysctl 树配置前馈系统时钟，该树提供以下变量：

**`kern.sysclock.ffclock.version`** 前馈时钟内核版本（只读）。

**`kern.sysclock.ffclock.ffcounter_bypass`** 使用可靠硬件时间计数器作为前馈计数器。最终将用于像 [xen(4)](xen.4.md) 这样的虚拟化环境，但目前无任何作用。

## 参见

clock_gettime(2), ffclock(2), [bpf(4)](bpf.4.md), [timecounters(4)](timecounters.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

前馈时钟支持首次出现于 FreeBSD 10.0。

## 作者

前馈时钟支持由 Julien Ridoux <jridoux@unimelb.edu.au> 与 Darryl Veitch <dveitch@unimelb.edu.au> 在墨尔本大学合作编写，由 FreeBSD 基金会赞助。

本手册页由 Julien Ridoux <jridoux@unimelb.edu.au> 和 Lawrence Stewart <lstewart@FreeBSD.org> 编写。
