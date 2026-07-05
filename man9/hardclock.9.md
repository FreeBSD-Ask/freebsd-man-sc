# hardclock.9

`hardclock` — 实时时钟

## 名称

`hardclock`

## 概要

```c
void
hardclock(int cnt, int usermode)
```

## 描述

`hardclock` 函数根据挂起的工作周期性调用。频率范围从非常繁忙系统的每秒 `hz` 次到空闲系统的每秒两次。`cnt` 参数报告自上次调用以来的 tick 数估计。在较长时间尺度上，每秒 `cnt` 的平均总和为 `hz`。有关较短时间尺度的重要细节，请参见 [hz(9)](hz.9.md)。当 `hardclock` 从中断用户模式执行的上下文中调用时，`usermode` 参数为非零。

`hardclock` 可执行不同的任务，例如：

- 运行当前进程的虚拟时间和配置文件时间（如果激活，则递减相应的计时器，并分别生成 `SIGVTALRM` 或 `SIGPROF`）。
- 递增一天中的时间，处理任何 ntpd(8) 或 adjtime(2) 引起的更改和闰秒，以及与 PPS 信号或外部时钟保持同步所需的任何补偿（如果内核支持）。
- 调度 softclock 中断（[swi(9)](swi.9.md)）处理。
- 收集 [hwpmc(4)](../man4/hwpmc.4.md) 统计信息。
- 启用时执行设备轮询（参见 [polling(4)](../man4/polling.4.md)）。
- 实现软件 [watchdog(9)](watchdog.9.md) 处理。
- 入队 [epoch(9)](epoch.9.md) 处理。

## 参见

`adjtime(2)`, `ntp_adjtime(2)`, `signal(3)`, [hwpmc(4)](../man4/hwpmc.4.md), [polling(4)](../man4/polling.4.md), `ntpd(8)`, [epoch(9)](epoch.9.md), [eventtimers(9)](eventtimers.9.md), [hz(9)](hz.9.md), [swi(9)](swi.9.md), [watchdog(9)](watchdog.9.md)
