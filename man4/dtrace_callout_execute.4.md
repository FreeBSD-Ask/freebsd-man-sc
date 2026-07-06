# dtrace_callout_execute.4

`dtrace_callout_execute` — 用于 callout API 的 DTrace 提供者

## 名称

`dtrace_callout_execute`

## 概要

`callout_execute:kernel::callout_start callout_execute:kernel::callout_end`

## 描述

`callout_execute` 提供者允许跟踪 [callout(9)](../man9/callout.9.md) 机制。

`callout_execute``:kernel::callout_start` 探测在 callout 开始之前触发。

`callout_execute``:kernel::callout_end` 探测在 callout 结束之后立即触发。

`callout_execute` 探测的唯一参数 `args[0]` 是被调用 callout 的 callout 处理程序 Ft struct callout *。

## 实例

### 实例 1：Callout 执行时间图

以下 [d(7)](../man7/d.7.md) 脚本生成 [callout(9)](../man9/callout.9.md) 执行时间的分布图：

```sh
callout_execute:::callout_start
{
    self->cstart = timestamp;
}
callout_execute:::callout_end
{
    @length = quantize(timestamp - self->cstart);
}
```

## 参见

[dtrace(1)](../man1/dtrace.1.md), [tracing(7)](../man7/tracing.7.md), [callout(9)](../man9/callout.9.md), [SDT(9)](../man9/sdt.9.md)

## 作者

`callout_execute` 提供者由 Robert N. M. Watson <rwatson@FreeBSD.org> 编写。

本手册页由 Mateusz Piotrowski <0mp@FreeBSD.org> 编写。
