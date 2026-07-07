# selrecord(9)

`seldrain` — 记录和唤醒 select 请求

## 名称

`seldrain`, `selrecord`, `selwakeup`

## 概要

```c
#include <sys/param.h>
```

```c
#include <sys/selinfo.h>
```

```c
void
seldrain(struct selinfo *sip)

void
selrecord(struct thread *td, struct selinfo *sip)

void
selwakeup(struct selinfo *sip)
```

## 描述

`seldrain`、`selrecord` 和 `selwakeup` 是 select(2)、poll(2) 以及被选择的对象使用的三个核心函数。它们处理记录哪些线程在等待哪些对象，以及当对象上发生感兴趣的事件时唤醒适当线程的任务。

`selrecord` 记录调用线程对与给定对象相关的事件感兴趣。如果另一个线程已在等待该对象，将在 `sip` 中标记冲突，稍后由 `selwakeup` 处理。

`selrecord` 获取并释放 `sellock`。

`selwakeup` 由底层对象处理代码调用，以通知任何等待线程发生了感兴趣的事件。如果发生冲突，`selwakeup` 将递增 `nselcoll`，并在全局 cv 上广播以唤醒所有等待线程，以便它们能够处理它。如果等待该对象的线程当前未在休眠或等待通道不是 `selwait`，`selwakeup` 将清除 `TDF_SELECT` 标志，select(2) 和 poll(2) 在醒来时应注意到此标志。

`seldrain` 在指定对象销毁前刷新其等待者队列。对象处理代码必须确保一旦调用了 `seldrain`，就不能再使用 `*sip`。

在任何调用 `selrecord` 或 `selwakeup` 之前，`*sip` 的内容必须被清零（例如通过 softc 初始化），否则可能发生 panic。`selwakeup` 获取并释放 `sellock`，并可能获取和释放 `sched_lock`。`seldrain` 通常可以只是 `selwakeup` 的包装，但使用者通常不应依赖此特性。

## 参见

[poll(2)](../sys/poll.2.md), [select(2)](../sys/select.2.md)

## 作者

本手册页由 Chad David <davidc@FreeBSD.org> 和 Alfred Perlstein <alfred@FreeBSD.org> 编写。
