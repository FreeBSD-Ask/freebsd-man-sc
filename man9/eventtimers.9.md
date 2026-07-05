# eventtimers.9

`eventtimers` — 内核事件定时器子系统

## 名称

`eventtimers`

## 概要

```c
#include <sys/timeet.h>
```

```c
struct eventtimer;
typedef int et_start_t(struct eventtimer *et,
    sbintime_t first, sbintime_t period);
typedef int et_stop_t(struct eventtimer *et);
typedef void et_event_cb_t(struct eventtimer *et, void *arg);
typedef int et_deregister_cb_t(struct eventtimer *et, void *arg);
struct eventtimer {
	SLIST_ENTRY(eventtimer)	et_all;
	char			*et_name;
	int			et_flags;
#define ET_FLAGS_PERIODIC	1
#define ET_FLAGS_ONESHOT	2
#define ET_FLAGS_PERCPU		4
#define ET_FLAGS_C3STOP		8
#define ET_FLAGS_POW2DIV	16
	int			et_quality;
	int			et_active;
	uint64_t		et_frequency;
	sbintime_t		et_min_period;
	sbintime_t		et_max_period;
	et_start_t		*et_start;
	et_stop_t		*et_stop;
	et_event_cb_t		*et_event_cb;
	et_deregister_cb_t	*et_deregister_cb;
	void 			*et_arg;
	void			*et_priv;
	struct sysctl_oid	*et_sysctl;
};
```

```c
int
et_register(struct eventtimer *et)

int
et_deregister(struct eventtimer *et)

void
et_change_frequency(struct eventtimer *et, uint64_t newfreq)

ET_LOCK()

ET_UNLOCK()

struct eventtimer *
et_find(const char *name, int check, int want)

int
et_init(struct eventtimer *et, et_event_cb_t *event,
    et_deregister_cb_t *deregister, void *arg)

int
et_start(struct eventtimer *et, sbintime_t first, sbintime_t period)

int
et_stop(struct eventtimer *et)

int
et_ban(struct eventtimer *et)

int
et_free(struct eventtimer *et)
```

## 描述

事件定时器负责在指定时间或周期性生成中断，以运行不同的基于时间的事件。该子系统由三个主要部分组成：

**驱动** 管理硬件以生成所请求的时间事件。

**消费者** `sys/kern/kern_clocksource.c` 使用事件定时器为内核提供 `hardclock`、`statclock` 和 `profclock` 时间事件。

**粘合**代码 `sys/sys/timeet.h`、`sys/kern/kern_et.c` 为事件定时器驱动和消费者提供 API。

## 驱动 API

驱动 API 围绕 eventtimer 结构构建。要注册其功能，驱动分配该结构并调用 `et_register`。驱动应填写以下字段：

**ET_FLAGS_PERIODIC** 支持周期模式。
**ET_FLAGS_ONESHOT** 支持单次模式。
**ET_FLAGS_PERCPU** 定时器是每 CPU 的。
**ET_FLAGS_C3STOP** 定时器可能在 CPU 睡眠状态下停止。
**ET_FLAGS_POW2DIV** 定时器仅支持 2^n 分频。

**`et_name`** 用于管理目的的事件定时器唯一名称。

**`et_flags`** 描述定时器能力的标志集合：

**`et_quality`** 是一个抽象值，用于表明此 timecounter 是否优于其他 timecounter。值越高越好。

**`et_frequency`** 定时器振荡器的基础频率（如适用且已知）。消费者用它预测通过分频可获得的可能频率集合。如不适用或未知应为零。

**`et_min_period , et_max_period`** 可靠可编程的最小和最大时间周期。

**`et_start`** 驱动的定时器启动函数指针。

**`et_stop`** 驱动的定时器停止函数指针。

**`et_priv`** 驱动的私有数据存储。

事件定时器功能注册后，通过 `et_start` 和 `et_stop` 方法控制。调用 `et_start` 方法以启动指定的事件定时器。最后两个参数用于指定何时应生成事件。`first` 参数指定生成第一个事件之前的时间周期。在周期模式下，NULL 值指定第一个周期等于 `period` 参数值。`period` 参数指定周期模式下后续事件之间的时间周期。NULL 值指定单次模式。这两个参数中至少一个不应为 NULL。当事件时间到达时，驱动应调用 `et_event_cb` 回调函数，将 `et_arg` 作为第二个参数传入。调用 `et_stop` 方法以停止指定的事件定时器。对于每 CPU 事件定时器，`et_start` 和 `et_stop` 方法控制与当前 CPU 关联的定时器。

驱动可通过调用 `et_deregister` 注销其功能。

如果时钟硬件的频率在运行时可能改变（例如在节能模式下），驱动必须在每次更改时调用 `et_change_frequency`。如果给定的事件定时器是活动定时器，`et_change_frequency` 会在所有 CPU 上停止定时器，更新 `et->frequency`，然后在所有 CPU 上重启定时器，使所有当前事件按新频率重新调度。如果给定定时器当前不是活动的，`et_change_frequency` 仅更新 `et->frequency`。

## 消费者 API

`et_find` 允许消费者查找可用的事件定时器，可选地匹配特定名称和/或能力标志。消费者可读取返回的 eventtimer 结构，但不应修改它。找到所需的事件定时器后，应对其调用 `et_init`，提交 `event` 回调和可选的 `deregister` 回调函数，以及不透明参数 `arg`。该参数将作为参数传递给回调。事件回调函数会在调度的时间事件上调用。它从硬件中断上下文中调用，因此不允许睡眠。可能调用 Deregister 回调函数，以通知消费者该事件定时器功能不再可用。在此调用上，消费者应在返回前停止使用该事件定时器。

定时器找到并初始化后，可通过 `et_start` 和 `et_stop` 控制。参数与驱动 API 中描述的相同。每 CPU 事件定时器只能从特定 CPU 控制。

`et_ban` 允许消费者通过清除单次和周期能力标志将事件定时器标记为损坏（如果以某种方式检测到）。`et_free` 是 `et_init` 的反操作。它释放事件定时器供其他消费者使用。

应使用 `ET_LOCK` 和 `ET_UNLOCK` 宏在 `et_find`、`et_init` 和 `et_free` 调用周围管理 [mutex(9)](mutex.9.md) 锁，以串行化对已注册事件定时器列表和 `et_find` 返回的指针的访问。`et_start` 和 `et_stop` 调用应以消费者内部方式串行化，以避免并发访问定时器硬件。

## 参见

[eventtimers(4)](../man4/eventtimers.4.md)

## 作者

Alexander Motin <mav@FreeBSD.org>
