# sched_4bsd.4

`sched_4bsd` — 4.4BSD 调度器

## 名称

`sched_4bsd`

## 概要

`options SCHED_4BSD`

## 描述

`sched_4bsd` 调度器是传统的系统调度器，在负载情况下提供高吞吐量和稳定的交互式响应。

以下 sysctl 与 `sched_4bsd` 的操作相关：

**`kern.sched.name`** 此只读 sysctl 报告活动调度器的名称。

**`kern.sched.quantum`** 此读写 sysctl 报告或设置授予线程的时间片长度（以微秒为单位）。

**`kern.sched.ipiwakeup.enabled`** 此读写 sysctl 设置线程被唤醒时调度器是否生成处理器间中断（IPI）以通知空闲 CPU。否则，空闲 CPU 将等待到下一个时钟节拍才寻找新工作。

**`kern.sched.preemption`** 此只读 sysctl 报告内核是否配置为支持抢占，抢占可减少唤醒时运行低优先级线程的延迟。

某些 sysctl 仅在支持 SMP 的系统上可用。

## 参见

[sched_ule(4)](sched_ule.4.md), [sysctl(8)](../man8/sysctl.8.md)

## 历史

`sched_4bsd` 调度器自 BSD 诞生以来就以各种形式存在。

## 缺陷

虽然是一个高度稳健且经过时间考验的调度器，`sched_4bsd` 缺乏在非对称处理器配置（如超线程）中进行有利调度的特定知识。
